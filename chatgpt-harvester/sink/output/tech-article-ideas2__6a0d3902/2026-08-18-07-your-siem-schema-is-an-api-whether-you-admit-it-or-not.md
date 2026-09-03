---
date: 2026-08-18
item_number: 7
title: Your SIEM Schema Is an API, Whether You Admit It or Not
summary: "Today is also the cut-over date for Google's revised Workspace Admin Audit Log schema: old and new events had been emitted in parallel since February, but from **18 August** the new events replace the old ones. Google warned that queries, alerts, saved investigations, BigQuery processing, and downstream workflows might require changes."
angle: Logs are routinely treated as implementation output rather than an interface.
interests:
  - observability
  - SIEM
  - APIs
  - security operations
  - schema evolution
format: Short post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 7. Your SIEM Schema Is an API, Whether You Admit It or Not


Today is also the cut-over date for Google's revised Workspace Admin Audit Log schema: old and new events had been emitted in parallel since February, but from **18 August** the new events replace the old ones. Google warned that queries, alerts, saved investigations, BigQuery processing, and downstream workflows might require changes. 

**Angle:** Logs are routinely treated as implementation output rather than an interface.

Then organisations build:

`alerting`

`security automation`

`billing`

`compliance`

`incident response`

`ML`

on top of them.

Congratulations: **you have an API. It just has worse versioning.**

There's a useful piece here about treating telemetry schemas like protobuf/API schemas: version them, test consumers, dual-publish during migration, and contract-test critical detections.

Google's six-month dual-emission window is actually a reasonable example of how to do this.

**Matches:** observability, SIEM, APIs, security operations, schema evolution.

**Format:** **Short post**

**Confidence: 0.97.**

---
