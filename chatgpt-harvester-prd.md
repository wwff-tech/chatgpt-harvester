# ChatGPT Conversation Harvester — MV3 Extension

## Context

A single-user Chromium extension that captures the current state of one or more ChatGPT conversations on a daily schedule and POSTs them to a configurable HTTP sink. Motivated by the need to snapshot conversations that are updated daily by ChatGPT Tasks (or similar), where manual copy-paste is impractical and public share links are point-in-time.

Target user: the author. No multi-tenant concerns, no Chrome Web Store distribution — side-loaded unpacked.

## Goals

- Fire-and-forget daily capture with no dependency on a tab being open.
- Survive browser restarts and missed windows without losing schedule.
- Configurable via an options page: conversation IDs, sink URL, time of day.
- Capture full conversation JSON (ChatGPT's internal backend API shape), not scraped DOM.
- Surface auth and fetch failures visibly without spamming.

## Non-goals

- Chrome Web Store publication.
- Browsers outside Chromium (Chrome, Brave, Edge, Arc).
- Multiple ChatGPT accounts.
- Sink-side storage, diffing, or alerting — separate concern.
- Real-time or streaming capture; daily cadence is sufficient.

## Architecture

MV3 service worker + options page + minimal popup for status and manual trigger. No content script; all fetches run from the service worker with `host_permissions` providing cookie context.

Flow:

1. `chrome.alarms.create('daily', { when, periodInMinutes: 1440 })` seeded on install and on config change.
2. Alarm handler in the service worker:
   - `GET https://chatgpt.com/api/auth/session` → extract `accessToken` from JSON body. Cookies carried automatically.
   - For each configured `conversation_id`: `GET /backend-api/conversation/<id>` with `Authorization: Bearer <accessToken>`.
   - POST `{ fetched_at, conversation_id, label, payload }` to the sink URL.
   - Append outcome to a local ring buffer.
3. Badge text reflects last run state: empty on success, `!` on partial failure, `×` on auth failure.

## Config model

Stored in `chrome.storage.sync`:

```json
{
  "sink_url": "https://ingest.example.com/chatgpt",
  "sink_auth_header": "Bearer <token>",
  "schedule_local_time": "05:05",
  "conversations": [
    { "id": "69cc692c-db90-8396-bc48-375ba1b6270e", "label": "Tech Article Ideas" }
  ]
}
```

- `schedule_local_time` is resolved against the browser's local timezone; next fire time is recomputed on config change and on browser startup.
- `sink_auth_header` is optional; added verbatim to the outgoing POST.
- `conversations` is a list from day one — adding a second chat is a config change, not a code change.

## Auth flow

ChatGPT's frontend auth is a two-step exchange:

1. A long-lived `__Secure-next-auth.session-token` cookie is set by the SSO login flow.
2. `/api/auth/session` exchanges that cookie for a short-lived (~1hr) `accessToken` JWT in the response body.
3. Backend API calls require `Authorization: Bearer <accessToken>`.

With `host_permissions: ["https://chatgpt.com/*"]`, service-worker `fetch()` carries the session cookie automatically. No cookie manipulation needed, and — critically — no TLS fingerprinting issues because the request originates inside Chrome itself.

Failure modes to detect explicitly:

- `/api/auth/session` returns an empty or unexpected object → user is logged out.
- 401 on backend API → access token expired mid-run; refresh once and retry, then give up.
- Non-JSON response (HTML, Cloudflare challenge) → log the first 500 chars and bail.

## Storage

- `chrome.storage.sync` — config, bounded by the 100KB quota (irrelevant at this scale).
- `chrome.storage.local` — run log, last 50 entries as a ring buffer: `{ timestamp, conversation_id, status, http_status?, error? }`.
- No payload persistence inside the extension. The sink owns durable storage.

## Error handling

- Each conversation fetch is independent; one failure does not abort the rest of the run.
- Sink POST retried with exponential backoff: 3 attempts, 1s / 4s / 16s.
- All thrown errors are caught and logged with `error.message` and a truncated stack.
- No user-facing notifications beyond the badge; the popup shows detail on demand.

## Observability

Popup surfaces:

- Last run timestamp and overall status.
- Per-conversation status for the most recent run.
- "Run now" button for immediate manual trigger.
- "Export log" dumping the ring buffer as JSON for inspection.

Service worker logs use the `[harvester]` prefix for easy filtering in `chrome://extensions` → "Inspect views → service worker".

## Acceptance criteria

1. Side-loaded into Chrome, configured with one conversation ID and a local sink, and left alone, the extension POSTs the conversation JSON once per day at the configured time.
2. Closing and reopening the browser does not cause missed runs if the configured time passed while closed — `chrome.alarms` catches up on next startup.
3. Logging out of ChatGPT causes the next run to fail with a distinct auth-failure state, visible in the popup within one click.
4. Changing the sink URL in options takes effect on the next run without reloading the extension.
5. Manual "Run now" from the popup triggers an immediate harvest and reports the outcome inline.
6. Removing a conversation from config removes it from subsequent runs without leaving orphaned alarms or log noise.

## Open questions

- Ring-buffer retention: 50 entries, or last-30-days by timestamp? 50 is simpler; 30 days gives better forensic range at a few KB cost.
- On permanent auth failure, should the extension POST a `{ status: "logged_out" }` heartbeat to the sink so server-side alerting can fire, or is the badge sufficient?
- Should the popup expose a diff view between consecutive captures? Instinct says no — that is a sink-side concern — but worth a sanity check.

## Assumptions (flagged)

- Chromium MV3 only. Firefox MV3 support is still awkward; Safari is out.
- Single-user, single-browser-profile. `storage.sync` is convenient but not relied upon.
- The sink URL is under the author's control and accepts arbitrary JSON bodies.
- Conversation IDs are stable (they are, at time of writing).
- `/api/auth/session` and `/backend-api/conversation/<id>` remain roughly shaped as they are today. Breakage is expected eventually; logging is the main mitigation.

## Out of scope / future

- WebSocket-based live capture.
- OAuth rather than cookie piggybacking (not offered by OpenAI for individual users).
- Firefox or Safari ports.
- Sink-side schema, durable storage, diffing, notification.
- Credential rotation or encryption at rest for `sink_auth_header`.
- Capturing conversations the user does not own (shared links, team workspaces).

## Suggested repo layout

```
chatgpt-harvester/
├── manifest.json
├── src/
│   ├── background.js      # service worker: alarm + fetch + sink POST
│   ├── options.html
│   ├── options.js         # reads/writes chrome.storage.sync
│   ├── popup.html
│   └── popup.js           # last-run status, run-now, export-log
├── icons/
│   ├── 16.png
│   ├── 48.png
│   └── 128.png
└── README.md
```

No build step unless TypeScript or bundling is adopted later; plain JS keeps the side-load iteration loop short.

## Manifest sketch

```json
{
  "manifest_version": 3,
  "name": "ChatGPT Conversation Harvester",
  "version": "0.1.0",
  "description": "Daily POST of one or more ChatGPT conversations to a configurable sink.",
  "permissions": ["storage", "alarms"],
  "host_permissions": ["https://chatgpt.com/*"],
  "background": { "service_worker": "src/background.js" },
  "options_page": "src/options.html",
  "action": {
    "default_popup": "src/popup.html",
    "default_icon": { "16": "icons/16.png", "48": "icons/48.png", "128": "icons/128.png" }
  },
  "icons": { "16": "icons/16.png", "48": "icons/48.png", "128": "icons/128.png" }
}
```

Note: the sink URL domain is deliberately *not* in `host_permissions`. MV3 allows `fetch()` to arbitrary origins from service workers as long as CORS is satisfied on the sink side — keeps the permission prompt narrow.
