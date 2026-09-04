---
date: 2026-08-14
item_number: 7
title: The Cloud Scheduler Wants Into Your Kernel
summary: "Another recent systems paper uses Linux **SchedExt/SCX** to let a serverless control plane influence host CPU scheduling rather than leaving all decisions to CFS. In its experiments, workload-aware scheduling reduced energy consumption by about 15%, with a 5% invocation-cost increase, and cut request latency by as much as 50% under heavy load."
angle: This is a fascinating erosion of a traditional abstraction boundary.
interests:
  - Linux
  - schedulers
  - serverless
  - SRE
  - performance engineering
  - eBPF/SCX
format: Long-form
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 7. The Cloud Scheduler Wants Into Your Kernel


Another recent systems paper uses Linux **SchedExt/SCX** to let a serverless control plane influence host CPU scheduling rather than leaving all decisions to CFS. In its experiments, workload-aware scheduling reduced energy consumption by about 15%, with a 5% invocation-cost increase, and cut request latency by as much as 50% under heavy load. 

**Angle:** This is a fascinating erosion of a traditional abstraction boundary.

Historically:

`application → scheduler → CPU`

The application describes work; the kernel decides how to schedule it.

But the serverless platform knows things the kernel doesn't:

- function identity,
- expected duration,
- invocation history,
- customer priority,
- SLO,
- cold-start state,
- economic value.

SchedExt makes it increasingly practical to feed that **semantic workload knowledge downward**.

The architectural question is whether this produces better optimisation or a horrifying coupling between orchestration and kernel policy.

Probably both.

**Matches:** Linux, schedulers, serverless, SRE, performance engineering, eBPF/SCX.

**Confidence: 0.91 — excellent systems seed.**

---
