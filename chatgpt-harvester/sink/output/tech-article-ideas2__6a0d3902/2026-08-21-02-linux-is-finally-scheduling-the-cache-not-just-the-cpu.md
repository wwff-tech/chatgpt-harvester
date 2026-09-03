---
date: 2026-08-21
item_number: 2
title: Linux Is Finally Scheduling the Cache, Not Just the CPU
summary: "Another substantial Linux 7.2 change is **cache-aware scheduling** for systems with multiple last-level-cache domains. The scheduler can preferentially place related work so it shares cache topology rather than unnecessarily bouncing tasks and data between LLC domains."
angle: CPU count has become an increasingly bad description of a computer.
interests:
  - Linux kernel
  - host latency
  - NUMA
  - AMD hardware
  - performance engineering
  - SRE
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 2. Linux Is Finally Scheduling the Cache, Not Just the CPU


Another substantial Linux 7.2 change is **cache-aware scheduling** for systems with multiple last-level-cache domains. The scheduler can preferentially place related work so it shares cache topology rather than unnecessarily bouncing tasks and data between LLC domains. 

This matters particularly for chiplet systems such as multi-CCD AMD CPUs and increasingly complex server processors.

**Angle:** CPU count has become an increasingly bad description of a computer.

An ostensibly symmetric:

`32-core machine`

may physically resemble:

`8 cores → LLC A`

`8 cores → LLC B`

`8 cores → LLC C`

`8 cores → LLC D`

with significantly different costs depending on where a thread runs and where its working set currently lives.

That means modern scheduling is increasingly about **data placement**, not simply compute placement.

There is a good progression to explain:

`SMP → NUMA → chiplets → heterogeneous cores → accelerators`

Each generation makes the abstraction:

> “here are N interchangeable CPUs”

slightly less true.

The provocative title alternative would be **“Your 32-Core CPU Is a Tiny Distributed System.”**

**Matches:** Linux kernel, host latency, NUMA, AMD hardware, performance engineering, SRE.

**Format:** **Long-form article**

**Confidence: 0.98.**

---
