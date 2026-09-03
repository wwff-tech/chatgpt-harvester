---
date: 2026-09-01
item_number: 8
title: "**“CPU Scheduling Now Needs to Know What Kind of Core It Is Looking At”** — Short technical post"
summary: "New Linux patches for upcoming AMD Zen 6 client processors show three core classes with substantially different performance characteristics. Pending ACPI standards don't yet expose all the information Linux needs, so the proposed kernel support temporarily hard-codes maximum-frequency values: 5025 for performance cores, 3524 for dense/efficiency cores, and 2399 for the new low-power cores."
angle: "We've gone from:"
interests:
  - Linux scheduling
  - AMD
  - heterogeneous compute
  - ACPI
  - performance engineering
format: Short technical post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 8. **“CPU Scheduling Now Needs to Know What Kind of Core It Is Looking At”** — Short technical post


New Linux patches for upcoming AMD Zen 6 client processors show three core classes with substantially different performance characteristics. Pending ACPI standards don't yet expose all the information Linux needs, so the proposed kernel support temporarily hard-codes maximum-frequency values: 5025 for performance cores, 3524 for dense/efficiency cores, and 2399 for the new low-power cores. 

**Angle:** We've gone from:

`CPU = N interchangeable cores`

to:

`CPU = heterogeneous compute topology`.

The scheduler now has to reason about:

`performance`

`power`

`thermal budget`

`task characteristics`

`core type`

rather than merely:

`idle CPU available`.

And here Linux is temporarily blocked by something wonderfully mundane: **firmware hasn't yet standardised how to describe the topology precisely enough**.

Hardware capability can therefore arrive before the vocabulary needed to expose it.

That is a recurring systems problem:

> You can't schedule a property the control plane cannot describe.

The same issue appears with GPU fabrics, NUMA, storage tiers, and network locality.

**Matches:** Linux scheduling, AMD, heterogeneous compute, ACPI, performance engineering.

**Format:** **Short technical post**

**Confidence: 0.98.**

---
