/*
 * ChatGPT Conversation Harvester — MV3 Service Worker
 *
 * Periodically fetches ChatGPT conversations via the internal API
 * and POSTs them to a configurable sink endpoint.
 */

/* ------------------------------------------------------------------ */
/*  Utilities                                                         */
/* ------------------------------------------------------------------ */

function log(level, ...args) {
  (console[level] || console.log).call(console, "[harvester]", ...args);
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function appendToRingBuffer(entry) {
  const data = await chrome.storage.local.get({ run_log: [] });
  const runLog = data.run_log;
  runLog.push(entry);
  while (runLog.length > 50) {
    runLog.shift();
  }
  await chrome.storage.local.set({ run_log: runLog });
}

/* ------------------------------------------------------------------ */
/*  Auth                                                              */
/* ------------------------------------------------------------------ */

async function getAccessToken() {
  let response;
  try {
    response = await fetch("https://chatgpt.com/api/auth/session");
  } catch (err) {
    throw new Error(`Network error fetching auth session: ${err.message}`);
  }

  let body;
  try {
    body = await response.json();
  } catch (_) {
    // Non-JSON response — likely Cloudflare challenge page
    let text;
    try {
      text = await response.text();
    } catch (_) {
      text = "(unable to read response body)";
    }
    log("error", "Auth response was not JSON. First 500 chars:", text.slice(0, 500));
    throw new Error("Auth response was not JSON (possible Cloudflare challenge)");
  }

  if (!body || !body.accessToken) {
    throw new Error("Auth session returned empty or missing accessToken");
  }

  return body.accessToken;
}

/* ------------------------------------------------------------------ */
/*  Conversation fetch                                                */
/* ------------------------------------------------------------------ */

const FETCH_401 = Symbol("FETCH_401");

async function fetchConversation(conversationId, accessToken) {
  let response;
  try {
    response = await fetch(
      `https://chatgpt.com/backend-api/conversation/${conversationId}`,
      {
        headers: { Authorization: `Bearer ${accessToken}` },
      }
    );
  } catch (err) {
    throw new Error(`Network error fetching conversation ${conversationId}: ${err.message}`);
  }

  if (response.status === 401) {
    return FETCH_401;
  }

  if (!response.ok) {
    throw new Error(
      `Conversation fetch failed for ${conversationId}: HTTP ${response.status}`
    );
  }

  return response.json();
}

/* ------------------------------------------------------------------ */
/*  Sink POST                                                         */
/* ------------------------------------------------------------------ */

async function postToSink(sinkUrl, authHeader, conversationId, label, payload) {
  const body = JSON.stringify({
    fetched_at: new Date().toISOString(),
    conversation_id: conversationId,
    label,
    payload,
  });

  const headers = { "Content-Type": "application/json" };
  if (authHeader) {
    headers["Authorization"] = authHeader;
  }

  const delays = [1000, 4000, 16000];
  let lastError;

  for (let attempt = 0; attempt < 4; attempt++) {
    try {
      const response = await fetch(sinkUrl, {
        method: "POST",
        headers,
        body,
      });

      if (response.ok) {
        return { ok: true, status: response.status };
      }

      lastError = new Error(`Sink responded with HTTP ${response.status}`);
      lastError.httpStatus = response.status;
    } catch (err) {
      lastError = new Error(`Sink network error: ${err.message}`);
    }

    if (attempt < 3) {
      log("warn", `Sink POST attempt ${attempt + 1} failed, retrying in ${delays[attempt]}ms...`);
      await sleep(delays[attempt]);
    }
  }

  throw lastError;
}

/* ------------------------------------------------------------------ */
/*  Badge helpers                                                     */
/* ------------------------------------------------------------------ */

function setBadge(text, color) {
  chrome.action.setBadgeText({ text });
  chrome.action.setBadgeBackgroundColor({ color });
}

/* ------------------------------------------------------------------ */
/*  Orchestrator                                                      */
/* ------------------------------------------------------------------ */

let isRunning = false;

async function runHarvest() {
  if (isRunning) {
    log("warn", "Harvest already in progress, skipping");
    return { success: false, summary: "Harvest already in progress" };
  }

  isRunning = true;
  log("info", "Starting harvest run");

  try {
    // Read config
    const config = await chrome.storage.sync.get({
      sink_url: "",
      sink_auth_header: "",
      schedule_local_time: "",
      conversations: [],
    });

    const { sink_url, sink_auth_header, conversations } = config;

    if (!sink_url) {
      log("error", "No sink_url configured");
      return { success: false, summary: "No sink_url configured" };
    }

    if (!conversations || conversations.length === 0) {
      log("warn", "No conversations configured");
      return { success: false, summary: "No conversations configured" };
    }

    // Acquire access token
    let accessToken;
    try {
      accessToken = await getAccessToken();
    } catch (err) {
      log("error", "Auth failed:", err.message);
      setBadge("\u00d7", "#e53935");

      const authFailTimestamp = new Date().toISOString();
      for (const conv of conversations) {
        await appendToRingBuffer({
          timestamp: authFailTimestamp,
          conversation_id: conv.id,
          label: conv.label,
          status: "auth_error",
          error: err.message,
        });
      }

      const lastRun = {
        timestamp: authFailTimestamp,
        overall_status: "auth_failure",
      };
      await chrome.storage.local.set({ last_run: lastRun });

      return { success: false, summary: `Auth failed: ${err.message}` };
    }

    // Use a single timestamp for the entire run so popup can correlate entries
    const runTimestamp = new Date().toISOString();

    // Process each conversation independently
    const results = [];

    for (const conv of conversations) {
      let result;
      try {
        result = await processConversation(conv, accessToken, sink_url, sink_auth_header);
      } catch (err) {
        result = { status: "fetch_error", error: err.message };
      }

      // Handle 401 — re-auth once and retry
      if (result === FETCH_401) {
        log("info", `Got 401 for ${conv.id}, re-fetching access token`);
        try {
          accessToken = await getAccessToken();
          result = await processConversation(conv, accessToken, sink_url, sink_auth_header);
          if (result === FETCH_401) {
            result = { status: "auth_error", error: "401 after token refresh" };
          }
        } catch (err) {
          result = { status: "auth_error", error: err.message };
        }
      }

      const logEntry = {
        timestamp: runTimestamp,
        conversation_id: conv.id,
        label: conv.label,
        ...(typeof result === "object" ? result : {}),
      };

      await appendToRingBuffer(logEntry);
      results.push(logEntry);
    }

    // Compute overall status
    const allOk = results.every((r) => r.status === "ok");
    const anyAuthError = results.some((r) => r.status === "auth_error");
    let overall_status;

    if (allOk) {
      overall_status = "ok";
      setBadge("", "#43a047");
    } else if (anyAuthError && results.every((r) => r.status === "auth_error")) {
      overall_status = "auth_failure";
      setBadge("\u00d7", "#e53935");
    } else {
      overall_status = "partial";
      setBadge("!", "#fb8c00");
    }

    const lastRun = {
      timestamp: runTimestamp,
      overall_status,
    };
    await chrome.storage.local.set({ last_run: lastRun });

    const okCount = results.filter((r) => r.status === "ok").length;
    const summary = `${okCount}/${results.length} conversations harvested (${overall_status})`;
    log("info", "Harvest complete:", summary);

    return { success: overall_status === "ok", summary };
  } finally {
    isRunning = false;
  }
}

async function processConversation(conv, accessToken, sinkUrl, sinkAuthHeader) {
  // Fetch conversation
  const payload = await fetchConversation(conv.id, accessToken);

  if (payload === FETCH_401) {
    return FETCH_401;
  }

  // POST to sink
  try {
    const sinkResult = await postToSink(sinkUrl, sinkAuthHeader, conv.id, conv.label, payload);
    return { status: "ok", http_status: sinkResult.status };
  } catch (err) {
    return {
      status: "sink_error",
      http_status: err.httpStatus,
      error: err.message,
    };
  }
}

/* ------------------------------------------------------------------ */
/*  Alarm management                                                  */
/* ------------------------------------------------------------------ */

function scheduleAlarm(timeStr) {
  if (!timeStr || !/^\d{2}:\d{2}$/.test(timeStr)) {
    log("warn", "Invalid schedule_local_time:", timeStr);
    return;
  }

  const [hours, minutes] = timeStr.split(":").map(Number);

  const now = new Date();
  const target = new Date();
  target.setHours(hours, minutes, 0, 0);

  // If the target time has already passed today, schedule for tomorrow
  if (target.getTime() <= now.getTime()) {
    target.setDate(target.getDate() + 1);
  }

  const when = target.getTime();
  log("info", `Scheduling daily-harvest alarm for ${target.toLocaleString()}`);

  chrome.alarms.create("daily-harvest", {
    when,
    periodInMinutes: 1440,
  });
}

chrome.alarms.onAlarm.addListener((alarm) => {
  if (alarm.name === "daily-harvest") {
    log("info", "Daily alarm fired");
    runHarvest();
  }
});

/* ------------------------------------------------------------------ */
/*  Lifecycle                                                         */
/* ------------------------------------------------------------------ */

async function onInstalledOrStartup() {
  const config = await chrome.storage.sync.get({ schedule_local_time: "" });
  if (config.schedule_local_time) {
    scheduleAlarm(config.schedule_local_time);
  }
}

chrome.runtime.onInstalled.addListener(() => {
  log("info", "Extension installed/updated");
  onInstalledOrStartup();
});

chrome.runtime.onStartup.addListener(() => {
  log("info", "Browser started");
  onInstalledOrStartup();
});

chrome.storage.onChanged.addListener((changes, areaName) => {
  if (areaName === "sync" && changes.schedule_local_time) {
    const newTime = changes.schedule_local_time.newValue;
    log("info", "schedule_local_time changed to:", newTime);
    if (newTime) {
      scheduleAlarm(newTime);
    } else {
      chrome.alarms.clear("daily-harvest");
      log("info", "Cleared daily-harvest alarm");
    }
  }
});

/* ------------------------------------------------------------------ */
/*  Message handler                                                   */
/* ------------------------------------------------------------------ */

chrome.runtime.onMessage.addListener((message, _sender, sendResponse) => {
  if (message.action === "run_now") {
    runHarvest().then((result) => {
      sendResponse(result);
    }).catch((err) => {
      log("error", "runHarvest error:", err.message);
      sendResponse({ success: false, summary: err.message });
    });
    return true; // async response
  }

  if (message.action === "get_status") {
    Promise.all([
      chrome.storage.local.get({ last_run: null }),
      chrome.alarms.get("daily-harvest"),
    ]).then(([data, alarm]) => {
      sendResponse({
        last_run: data.last_run,
        next_alarm: alarm ? alarm.scheduledTime : null,
      });
    }).catch((err) => {
      log("error", "get_status error:", err.message);
      sendResponse({ last_run: null, next_alarm: null });
    });
    return true; // async response
  }
});
