# ChatGPT Conversation Harvester

A Chrome extension (MV3) that captures ChatGPT conversations on a daily schedule and POSTs the full JSON to a configurable HTTP sink. Built for snapshotting conversations that are updated daily by ChatGPT Tasks, where manual export is impractical and share links are point-in-time.

Side-loaded only — not published to the Chrome Web Store.

## How it works

1. A `chrome.alarms` alarm fires once per day at a configured local time.
2. The service worker fetches a short-lived access token from ChatGPT's session endpoint (cookies are carried automatically via `host_permissions`).
3. For each configured conversation ID, it fetches the full conversation JSON from the backend API.
4. Each conversation payload is POSTed to the sink URL.
5. Results are logged to a local ring buffer and surfaced in the popup.

No content scripts, no DOM scraping — all fetches happen in the service worker.

## Installation

### Prerequisites

- A Chromium-based browser (Chrome, Brave, Edge, Arc)
- Logged into [chatgpt.com](https://chatgpt.com) in the browser profile where the extension will run

### Load the extension

1. Open `chrome://extensions/`
2. Enable **Developer mode** (toggle in the top right)
3. Click **Load unpacked**
4. Select the `chatgpt-harvester/` directory
5. The extension icon (teal square) appears in the toolbar

### Packaging as a `.crx`

To distribute the extension as a packaged file:

1. Open `chrome://extensions/`
2. Click **Pack extension**
3. Set **Extension root directory** to the `chatgpt-harvester/` folder
4. Leave **Private key file** empty on first pack (Chrome generates one as `chatgpt-harvester.pem` — keep this for future updates)
5. Click **Pack Extension**
6. Chrome creates `chatgpt-harvester.crx` alongside the directory

To install a `.crx` file, drag it onto `chrome://extensions/`.

> **Note:** Chromium may block `.crx` installs from outside the Web Store depending on policy. On managed machines, use the unpacked method instead.

### Packaging as a `.zip` (for manual distribution)

```bash
cd chatgpt-harvester/
zip -r ../chatgpt-harvester.zip . -x "sink/*" -x ".git/*"
```

Recipients can unpack and load as unpacked.

## Configuration

Right-click the extension icon → **Options**, or go to `chrome://extensions/` → ChatGPT Conversation Harvester → **Details** → **Extension options**.

| Field | Description |
|-------|-------------|
| **Sink URL** | HTTP(S) endpoint to POST conversation payloads to |
| **Sink Auth Header** | Optional `Authorization` header value, sent verbatim on each POST |
| **Schedule Time** | Local time of day to run (HH:MM) |
| **Conversations** | List of ChatGPT conversation IDs and labels |

### Finding a conversation ID

Open a conversation at `https://chatgpt.com/c/<conversation-id>` — the UUID in the URL is the ID.

## Popup

Click the extension icon to see:

- **Last run** status with a coloured indicator (green = ok, orange = partial failure, red = auth failure)
- **Next scheduled run** time
- **Per-conversation results** from the most recent run
- **Run Now** button for immediate manual harvest
- **Export Log** button to download the ring buffer as JSON

## Badge indicators

| Badge | Meaning |
|-------|---------|
| *(empty)* | Last run succeeded |
| `!` | Some conversations failed, others succeeded |
| `×` | Auth failure — you're likely logged out of ChatGPT |

## Dev sink

A minimal FastAPI server is included for local testing.

```bash
cd sink/
pip install -r requirements.txt
python server.py
```

Runs on `http://localhost:8484`. Endpoints:

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Health check |
| POST | `/chatgpt` | Receives conversation payloads, saves to `sink/data/` |
| GET | `/conversations` | Lists all saved payloads |

Set the extension's sink URL to `http://localhost:8484/chatgpt`.

The sink must serve CORS headers — the included server allows all origins.

## Post-processor

A script to convert captured JSON into readable markdown with YAML frontmatter.

```bash
cd sink/

# One markdown file per article idea, with parsed metadata
python postprocess.py data/ --mode items --outdir output/

# One markdown file per day
python postprocess.py data/ --mode daily --outdir output/

# Only process the latest capture per conversation
python postprocess.py data/ --latest-only --outdir output/
```

### Items mode

Parses numbered items (`## 1)`, `## 2)`, etc.) from assistant messages and extracts structured fields into frontmatter:

```yaml
---
date: 2026-04-18
item_number: 1
title: Your TLS Cert Was Revoked—Your System Didn't Notice
summary: Certificate revocation mechanisms (CRLs, OCSP) are...
angle: "Revocation vs reality" — security guarantees that...
interests:
  - Security
  - networking
format: Long form
suggested_points:
  - How revocation is supposed to work
  - Why clients skip or soft-fail checks
---
```

### Daily mode

Outputs the full assistant message per date with conversation metadata in frontmatter.

When a date has multiple assistant messages (e.g. a format tweak mid-day), items mode uses the latest one.

## Troubleshooting

### Service worker logs

1. Go to `chrome://extensions/`
2. Find ChatGPT Conversation Harvester
3. Click **service worker** under "Inspect views"
4. Filter the console by `[harvester]`

### Common issues

- **Badge shows `×`**: You're logged out of ChatGPT. Log in at [chatgpt.com](https://chatgpt.com) and try again.
- **Sink POST fails**: Check that the sink is running and CORS is configured. The sink URL domain is not in `host_permissions` — MV3 service workers can fetch arbitrary origins if the server responds with appropriate CORS headers.
- **Missed run**: `chrome.alarms` catches up on browser restart. If the browser was closed during the scheduled time, the alarm fires on next startup.

## Project structure

```
chatgpt-harvester/
├── manifest.json            # MV3 manifest
├── src/
│   ├── background.js        # Service worker: auth, fetch, sink POST, alarms
│   ├── options.html          # Configuration UI
│   ├── options.js
│   ├── popup.html            # Status and controls
│   └── popup.js
├── icons/
│   ├── 16.png
│   ├── 48.png
│   └── 128.png
└── sink/
    ├── server.py             # FastAPI dev sink
    ├── postprocess.py        # JSON → markdown converter
    ├── requirements.txt
    └── data/                 # Captured payloads (gitignored)
```

## License

MIT
