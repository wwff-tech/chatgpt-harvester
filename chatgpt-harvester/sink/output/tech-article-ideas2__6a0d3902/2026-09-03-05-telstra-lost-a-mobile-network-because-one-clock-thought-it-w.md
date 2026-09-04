---
date: 2026-09-03
item_number: 5
title: Telstra Lost a Mobile Network Because One Clock Thought It Was 2006
summary: "The external review into Telstra's July outage concluded that planned hardware maintenance caused a GPS timing card to reset and propagate an **incorrect date — 2006 — into parts of the mobile network**. Roughly 45% of calls and data sessions were affected. The review also found weak ownership of NTP/timing infrastructure, incomplete firmware maintenance, inadequate visibility, and early alarms that weren't effectively acted upon."
angle: This is a magnificent “invisible infrastructure” story.
interests:
  - SRE
  - NTP/PTP
  - networking
  - incident analysis
  - hidden dependencies
  - infrastructure ownership
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 5. Telstra Lost a Mobile Network Because One Clock Thought It Was 2006


The external review into Telstra's July outage concluded that planned hardware maintenance caused a GPS timing card to reset and propagate an **incorrect date — 2006 — into parts of the mobile network**. Roughly 45% of calls and data sessions were affected. The review also found weak ownership of NTP/timing infrastructure, incomplete firmware maintenance, inadequate visibility, and early alarms that weren't effectively acted upon. 

**Angle:** This is a magnificent “invisible infrastructure” story.

Architecture diagrams show:

`radio`

`packet core`

`routers`

`databases`.

Nobody draws:

`time`.

Yet distributed telecom systems depend on timing for enormous amounts of state and coordination.

The failure wasn't simply:

`GPS card returned bad date`.

It was that an organisation operating critical national infrastructure had allowed **time to become an under-owned dependency**.

That's a very SRE lesson.

Ask:

> Which services does everything depend upon but nobody thinks of as a product?

Candidates include:

`DNS`

`NTP/PTP`

`PKI`

`DHCP`

`identity`

`firmware`

`configuration distribution`.

These are often extremely reliable precisely because they're boring — which allows organisational knowledge around them to decay.

> **Reliability can hide criticality until the day it doesn't.**

**Matches:** SRE, NTP/PTP, networking, incident analysis, hidden dependencies, infrastructure ownership.

**Format:** **Long-form article**

**Confidence: 0.99.**

---
