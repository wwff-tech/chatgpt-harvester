---
date: 2026-08-17
item_number: 9
title: Left-field — “A Maintenance Port Is an API With Terrible Documentation”
summary: The aircraft work suggests a broader hardware/software analogy.
angle: "Hardware interfaces *are APIs*."
interests:
  - embedded systems
  - electronics
  - hardware security
  - capability modelling
  - systems architecture
format: Long-form
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 9. Left-field — “A Maintenance Port Is an API With Terrible Documentation”


The aircraft work suggests a broader hardware/software analogy. 

**Angle:** Hardware interfaces *are APIs*.

A connector defines:

`physical transport`

`protocol`

`commands`

`authority`

`trust assumptions`

`failure modes`.

Yet hardware reviews often treat an unused connector as a physical artefact rather than an exposed capability.

The same applies to:

`test pads`

`UART headers`

`JTAG`

`SWD`

`factory USB`

`diagnostic CAN`

`server BMC interfaces`.

That suggests hardware should have something analogous to an API inventory:

> **What physical interfaces exist on the finished product, what authority does each expose, and what authenticates the caller?**

There is even a nice connection to yesterday's “authority bill of materials”: physical interfaces belong on it too.

**Matches:** embedded systems, electronics, hardware security, capability modelling, systems architecture.

**Confidence: 0.97.**

---
