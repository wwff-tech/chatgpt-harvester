document.addEventListener("DOMContentLoaded", async () => {
  const statusDot = document.getElementById("statusDot");
  const lastRunEl = document.getElementById("lastRun");
  const nextRunEl = document.getElementById("nextRun");
  const convList = document.getElementById("convList");
  const runBtn = document.getElementById("runBtn");
  const exportBtn = document.getElementById("exportBtn");
  const resultEl = document.getElementById("result");

  async function refresh() {
    const status = await chrome.runtime.sendMessage({ action: "get_status" });
    const { run_log = [] } = await chrome.storage.local.get("run_log");

    // Status header
    const lr = status.last_run;
    if (lr && lr.timestamp) {
      lastRunEl.textContent = "Last run: " + relativeTime(lr.timestamp);
      statusDot.className = "dot dot-" + (lr.overall_status || "none");
    } else {
      lastRunEl.textContent = "No runs yet";
      statusDot.className = "dot dot-none";
    }

    // Next run
    if (status.next_alarm) {
      nextRunEl.textContent = "Next: " + new Date(status.next_alarm).toLocaleString();
    } else {
      nextRunEl.textContent = "";
    }

    // Conversation list for most recent run
    convList.innerHTML = "";
    if (lr && lr.timestamp) {
      const entries = run_log.filter((e) => e.timestamp === lr.timestamp);
      for (const entry of entries) {
        const item = document.createElement("div");
        item.className = "conv-item";
        const label = document.createElement("span");
        label.className = "conv-label";
        label.textContent = entry.label || entry.conversation_id || "unknown";
        label.title = entry.conversation_id || "";
        const st = document.createElement("span");
        st.className = "status-" + entry.status;
        st.textContent = entry.status;
        item.appendChild(label);
        item.appendChild(st);
        convList.appendChild(item);
      }
    }
  }

  function relativeTime(iso) {
    const diff = Date.now() - new Date(iso).getTime();
    const mins = Math.floor(diff / 60000);
    if (mins < 1) return "just now";
    if (mins < 60) return mins + "m ago";
    const hrs = Math.floor(mins / 60);
    if (hrs < 24) return hrs + "h ago";
    const days = Math.floor(hrs / 24);
    return days + "d ago";
  }

  runBtn.addEventListener("click", async () => {
    runBtn.disabled = true;
    resultEl.textContent = "Running...";
    try {
      const resp = await chrome.runtime.sendMessage({ action: "run_now" });
      resultEl.textContent = resp.success ? resp.summary : "Error: " + resp.summary;
    } catch (err) {
      resultEl.textContent = "Error: " + err.message;
    }
    runBtn.disabled = false;
    await refresh();
  });

  exportBtn.addEventListener("click", async () => {
    const { run_log = [] } = await chrome.storage.local.get("run_log");
    const blob = new Blob([JSON.stringify(run_log, null, 2)], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "harvester-log.json";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  });

  await refresh();
});
