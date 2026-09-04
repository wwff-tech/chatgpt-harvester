---
date: 2026-08-22
item_number: 5
title: "**“Sixteen Milliseconds Were Hiding Inside a TLB Flush”** — Long-form / technical article"
summary: "Linux 7.3 includes an x86 memory-management change developed after ByteDance engineers observed **scheduling delays reaching 16 ms on a 16-core production machine**. TLB shootdowns use inter-processor interrupts; callers could wait for remote CPUs with pre-emption disabled, delaying high-priority work. The merged changes permit pre-emption during parts of that wait, with ByteDance reporting latency reductions of up to 90% in its testing."
angle: This is a beautiful example of why tail latency often lives somewhere completely different from the application producing the symptom.
interests:
  - Linux kernel
  - host latency
  - SRE
  - DPDK
  - interrupts
  - NUMA/multicore systems
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 5. **“Sixteen Milliseconds Were Hiding Inside a TLB Flush”** — Long-form / technical article


Linux 7.3 includes an x86 memory-management change developed after ByteDance engineers observed **scheduling delays reaching 16 ms on a 16-core production machine**. TLB shootdowns use inter-processor interrupts; callers could wait for remote CPUs with pre-emption disabled, delaying high-priority work. The merged changes permit pre-emption during parts of that wait, with ByteDance reporting latency reductions of up to 90% in its testing. 

**Angle:** This is a beautiful example of why tail latency often lives somewhere completely different from the application producing the symptom.

An operator sees:

`packet processing woke up 16 ms late`.

The causal chain can be:

`unrelated process exits`

→ `memory mappings removed`

→ `TLB invalidation`

→ `IPI sent to other CPUs`

→ `current CPU waits`

→ `pre-emption unavailable`

→ **your supposedly high-priority task can't run**.

Nothing is “slow” in the conventional utilisation sense.

This would make an excellent article about **latency archaeology**: tracing an application-level outlier downward through scheduler state, interrupt handling, memory management, and cross-core coordination.

It also reinforces yesterday's “your CPU is a tiny distributed system” theme: TLB shootdown is literally a distributed invalidation protocol running across cores.

**Matches:** Linux kernel, host latency, SRE, DPDK, interrupts, NUMA/multicore systems.

**Format:** **Long-form article**

**Confidence: 0.99.**

---
