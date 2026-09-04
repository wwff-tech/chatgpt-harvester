---
date: 2026-08-09
item_number: 10
title: "Left-field: “A Rollback Window Is a Temporal API”"
summary: "The seven-day EKS rollback feature exposes an under-discussed systems concept: some operations aren't merely allowed or forbidden; **their validity decays with time and subsequent state transitions**."
angle: "Treat time as part of an API's state machine."
interests:
  - state machines
  - distributed systems
  - SRE
  - API design
  - platform engineering
format: Long-form
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 10. Left-field: “A Rollback Window Is a Temporal API”


The seven-day EKS rollback feature exposes an under-discussed systems concept: some operations aren't merely allowed or forbidden; **their validity decays with time and subsequent state transitions**. 

**Angle:** Treat time as part of an API's state machine.

`upgrade → rollbackable → incompatible-change → committed`

is conceptually similar to transaction commit points, undo logs, garbage-collection grace periods, certificate overlap, blue/green deployments, event retention, and saga compensation.

That could become a broader article about designing systems with explicit **reversibility budgets**: not merely *can we undo this?*, but *for how long, under which invariants, and at what cost?*

**Matches:** state machines, distributed systems, SRE, API design, platform engineering.

**Confidence: 0.90.**
