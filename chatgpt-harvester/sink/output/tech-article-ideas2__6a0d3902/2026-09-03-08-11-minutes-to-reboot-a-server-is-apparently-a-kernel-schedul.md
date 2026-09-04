---
date: 2026-09-03
item_number: 8
title: "**“11 Minutes to Reboot a Server Is Apparently a Kernel Scheduling Problem”** — Short systems post"
summary: "A Linux patch series for **asynchronous device shutdown** reached revision 21 today after more than two years of work. Devices that explicitly opt in can shut down in parallel rather than serially; one test system reportedly fell from **11 minutes to 55 seconds**, and another from 80 seconds to 11."
angle: Shutdown is a dependency graph masquerading as a list.
interests:
  - Linux kernel
  - systemd
  - servers
  - NVMe
  - dependency graphs
  - performance engineering
format: Short post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 8. **“11 Minutes to Reboot a Server Is Apparently a Kernel Scheduling Problem”** — Short systems post


A Linux patch series for **asynchronous device shutdown** reached revision 21 today after more than two years of work. Devices that explicitly opt in can shut down in parallel rather than serially; one test system reportedly fell from **11 minutes to 55 seconds**, and another from 80 seconds to 11. 

**Angle:** Shutdown is a dependency graph masquerading as a list.

If:

`device A`

and:

`device B`

have no shutdown dependency, doing:

`A → wait → B → wait`

is needless serialization.

This is the same optimisation behind:

`parallel CI`

`systemd boot`

`DAG schedulers`

`Terraform`

`build systems`.

But shutdown has a much nastier correctness requirement: incorrectly parallelising dependent teardown can lose data or wedge hardware.

So the real problem is:

> **Discover enough independence to parallelise safely.**

That's a lovely compact systems story.

**Matches:** Linux kernel, systemd, servers, NVMe, dependency graphs, performance engineering.

**Format:** **Short post**

**Confidence: 0.98; the patches remain under review rather than merged.**

---
