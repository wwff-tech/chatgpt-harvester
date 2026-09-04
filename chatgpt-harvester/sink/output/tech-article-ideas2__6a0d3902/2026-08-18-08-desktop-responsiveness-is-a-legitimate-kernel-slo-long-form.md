---
date: 2026-08-18
item_number: 8
title: "**“Desktop Responsiveness Is a Legitimate Kernel SLO”** — Long-form / experimental article"
summary: "A fun systems development surfaced today: Linux scheduler developer **Con Kolivas has returned with a kernel patchset after roughly a decade away**, reviving discussion around optimising perceived desktop responsiveness rather than aggregate throughput. Community interest is already focusing on whether those old trade-offs remain relevant on modern many-core hardware."
angle: This is worth writing only if you benchmark it yourself.
interests:
  - Linux kernel
  - latency
  - schedulers
  - performance engineering
  - benchmarking
format: Long-form only after testing
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 8. **“Desktop Responsiveness Is a Legitimate Kernel SLO”** — Long-form / experimental article


A fun systems development surfaced today: Linux scheduler developer **Con Kolivas has returned with a kernel patchset after roughly a decade away**, reviving discussion around optimising perceived desktop responsiveness rather than aggregate throughput. Community interest is already focusing on whether those old trade-offs remain relevant on modern many-core hardware. 

**Angle:** This is worth writing only if you benchmark it yourself.

Server performance tends to optimise quantities such as:

`throughput`

`CPU utilisation`

`requests/sec`

`p99 latency`.

Desktop users care about something closer to:

> *I started compiling on 15 cores; does the editor on core 16 still feel instant?*

That's an SLO too.

It would be interesting to construct an intentionally hostile workload and measure **interactive latency under saturation** across stock Linux and the patchset rather than reporting compilation benchmarks.

That also gives you a good discussion of why optimising mean throughput can worsen human-perceived performance.

**Matches:** Linux kernel, latency, schedulers, performance engineering, benchmarking.

**Format:** **Long-form only after testing**

**Confidence: 0.83 on present news value; 0.95 that a properly instrumented benchmark would make a good article.**

---
