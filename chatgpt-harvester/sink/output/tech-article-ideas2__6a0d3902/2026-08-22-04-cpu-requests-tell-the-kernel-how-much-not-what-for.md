---
date: 2026-08-22
item_number: 4
title: CPU Requests Tell the Kernel How Much. Not What For.
summary: "Resource quantity and resource **semantics** are different things."
angle: "Compare:"
interests:
  - Kubernetes
  - SRE
  - Linux scheduling
  - platform APIs
format: Short post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 4. CPU Requests Tell the Kernel How Much. Not What For.


`sched_ext` sub-schedulers expose an interesting weakness in ordinary resource specifications. A container asking for four CPUs says almost nothing about what behaviour it actually needs from those CPUs. 

**Angle:** Compare:

`video encoder → maximise throughput`

`game server → minimise wake-up jitter`

`build job → opportunistic throughput`

`packet processor → deterministic latency`

`background ML inference → power efficiency`.

All might request:

`cpu: 4`.

Resource quantity and resource **semantics** are different things.

We already encode some semantics for storage:

`IOPS`

`latency`

`durability`

`access mode`.

CPU scheduling may eventually deserve something similar.

**Matches:** Kubernetes, SRE, Linux scheduling, platform APIs.

**Format:** **Short post**

**Confidence: 0.97.**

---
