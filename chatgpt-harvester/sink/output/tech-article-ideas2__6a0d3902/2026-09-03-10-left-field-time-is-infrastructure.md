---
date: 2026-09-03
item_number: 10
title: Left-field — “Time Is Infrastructure”
summary: The Telstra outage is the hook, but this deserves the evergreen treatment.
angle: "Computers don't possess time."
interests:
  - Linux
  - distributed systems
  - networking
  - SRE
  - embedded electronics
  - GPS
  - systems fundamentals
format: Long-form evergreen article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 10. Left-field — “Time Is Infrastructure”


The Telstra outage is the hook, but this deserves the evergreen treatment.

**Angle:** Computers don't possess time.

They possess:

`oscillators`

plus:

`external assertions about time`

plus:

`algorithms for reconciling them`.

Yet we build enormous distributed systems assuming:

`now()`

is basically a fact.

It isn't.

Bad time can break:

`TLS certificate validity`

`Kerberos`

`distributed databases`

`leases`

`logs`

`event ordering`

`billing`

`telecom networks`

`TOTP`

`scheduled jobs`.

And there are several subtly different requirements:

`accurate wall clock`

`monotonic elapsed time`

`frequency synchronisation`

`phase synchronisation`

`causal ordering`.

NTP, PTP, GPS, monotonic clocks, and logical clocks solve different pieces.

A strong article could start with **“One GPS card thought it was 2006”** and then progressively dismantle the innocent-looking `time.time()` abstraction.

**Matches:** Linux, distributed systems, networking, SRE, embedded electronics, GPS, systems fundamentals.

**Format:** **Long-form evergreen article**

**Confidence: 0.99 — strongest left-field/evergreen idea today.**
