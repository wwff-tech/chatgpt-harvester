/*
 * Drives runHarvest() through the staleness state machine.
 *
 * background.js is a classic service-worker script with no exports, so it is
 * evaluated in a vm context whose globals are stubbed chrome APIs; its
 * top-level function declarations then hang off that context.
 *
 * The case worth the harness: notified_at is what starts the seven-day
 * re-notify window, so recording it for a notification that never went out
 * buys silence rather than an alert.
 */
import assert from "node:assert/strict";
import fs from "node:fs";
import test from "node:test";
import vm from "node:vm";

const SOURCE = fs.readFileSync(new URL("../src/background.js", import.meta.url), "utf8");
const DAY = 86400000;
const CONV = { id: "conv-1", label: "tech article ideas" };

function harness({ notify_on_stale = true, feed_state = {}, latestMessageAgeMs = 0,
                   notifyFails = false } = {}) {
  const sent = [];
  const local = { feed_state, run_log: [], notification_targets: {} };
  const badge = {};

  const listener = () => ({ addListener() {} });
  const chrome = {
    storage: {
      sync: { get: async (d) => ({ ...d, sink_url: "http://sink", conversations: [CONV],
                                   stale_after_hours: 48, notify_on_stale }) },
      local: {
        get: async (keys) => {
          const want = typeof keys === "string" ? { [keys]: undefined } : keys;
          return Object.fromEntries(
            Object.keys(want).map((k) => [k, local[k] !== undefined ? local[k] : want[k]])
          );
        },
        set: async (obj) => Object.assign(local, obj),
      },
      onChanged: listener(),
    },
    action: { setBadgeText: (o) => (badge.text = o.text),
              setBadgeBackgroundColor: (o) => (badge.color = o.color) },
    alarms: { create() {}, clear() {}, get: async () => null, onAlarm: listener() },
    runtime: { onInstalled: listener(), onStartup: listener(), onMessage: listener(),
               getURL: (p) => p },
    notifications: {
      create: async (id, opts) => {
        if (notifyFails) throw new Error("no permission");
        sent.push({ id, ...opts });
      },
      onClicked: listener(),
      clear() {},
    },
    tabs: { create() {} },
  };

  const context = vm.createContext({
    chrome, console, fetch: async () => ({}), setTimeout, clearTimeout, URL, Date, Math, JSON,
  });
  vm.runInContext(SOURCE, context);

  // Stub the network entirely: processConversation is replaced so the run
  // exercises the staleness bookkeeping and nothing else.
  const latest = Date.now() - latestMessageAgeMs;
  vm.runInContext(
    `getAccessToken = async () => "token";
     processConversation = async (conv) => ({ status: "ok", http_status: 200,
                                              latest_message_time: ${latest} });`,
    context
  );

  return { context, sent, local, badge,
           run: () => vm.runInContext("runHarvest()", context) };
}

test("a fresh feed notifies nobody", async () => {
  const h = harness({ latestMessageAgeMs: 2 * 3600000 });
  await h.run();
  assert.equal(h.sent.length, 0);
  assert.equal(h.local.feed_state[CONV.id].stale, false);
});

test("a stale feed notifies and records when it did", async () => {
  const h = harness({ latestMessageAgeMs: 5 * DAY });
  await h.run();
  assert.equal(h.sent.length, 1);
  assert.match(h.sent[0].title, /gone quiet/);
  assert.ok(h.local.feed_state[CONV.id].notified_at, "a delivered alert is recorded");
});

test("notifications off: nothing is sent, and nothing is recorded as sent", async () => {
  const h = harness({ latestMessageAgeMs: 5 * DAY, notify_on_stale: false });
  await h.run();
  assert.equal(h.sent.length, 0);
  assert.equal(h.local.feed_state[CONV.id].stale, true, "still flagged for the badge");
  assert.equal(h.local.feed_state[CONV.id].notified_at, null,
    "recording this would start the re-notify window against an alert nobody got");
});

test("turning notifications on afterwards still gets the first alert", async () => {
  // The regression: with notified_at stamped while notifications were off,
  // dueAgain stayed false for seven days and enabling them bought silence.
  const off = harness({ latestMessageAgeMs: 5 * DAY, notify_on_stale: false });
  await off.run();

  const on = harness({ latestMessageAgeMs: 5 * DAY, notify_on_stale: true,
                       feed_state: off.local.feed_state });
  await on.run();
  assert.equal(on.sent.length, 1, "enabling notifications must produce the alert");
});

test("a failed notification is retried on the next run", async () => {
  const failed = harness({ latestMessageAgeMs: 5 * DAY, notifyFails: true });
  await failed.run();
  assert.equal(failed.local.feed_state[CONV.id].notified_at, null);

  const retry = harness({ latestMessageAgeMs: 5 * DAY,
                          feed_state: failed.local.feed_state });
  await retry.run();
  assert.equal(retry.sent.length, 1);
});

test("a feed that stays stale is not re-notified daily", async () => {
  const first = harness({ latestMessageAgeMs: 5 * DAY });
  await first.run();
  const next = harness({ latestMessageAgeMs: 6 * DAY, feed_state: first.local.feed_state });
  await next.run();
  assert.equal(next.sent.length, 0, "one nudge, not a daily reminder");
});

test("a feed still stale after a week is nudged again", async () => {
  const stale = { [CONV.id]: { label: CONV.label, stale: true,
    latest_message_time: Date.now() - 30 * DAY,
    notified_at: new Date(Date.now() - 8 * DAY).toISOString() } };
  const h = harness({ latestMessageAgeMs: 30 * DAY, feed_state: stale });
  await h.run();
  assert.equal(h.sent.length, 1);
});

test("recovery is announced and clears the record", async () => {
  const stale = { [CONV.id]: { label: CONV.label, stale: true,
    latest_message_time: Date.now() - 30 * DAY,
    notified_at: new Date().toISOString() } };
  const h = harness({ latestMessageAgeMs: 3600000, feed_state: stale });
  await h.run();
  assert.equal(h.sent.length, 1);
  assert.match(h.sent[0].title, /producing again/);
  assert.equal(h.local.feed_state[CONV.id].notified_at, null);
});

test("state for an unconfigured conversation is dropped", async () => {
  const h = harness({ latestMessageAgeMs: 3600000,
                      feed_state: { "gone-away": { stale: true, label: "old" } } });
  await h.run();
  assert.equal(h.local.feed_state["gone-away"], undefined, "or the badge stays stuck amber");
});
