---
date: 2026-08-22
item_number: 3
title: Linux Can Now Run Different CPU Schedulers for Different Parts of the Machine
summary: "Linux 7.3's sched_ext sub-scheduler support is now considered feature-complete. A root BPF scheduler can delegate a cgroup subtree — together with revocable CPU grants — to a nested scheduler, which then controls scheduling decisions for its workloads."
angle: This is a considerably bigger conceptual change than “Linux lets you write schedulers in BPF”.
interests:
  - Linux kernel
  - eBPF
  - Kubernetes
  - platform engineering
  - performance
  - workload isolation
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 3. Linux Can Now Run Different CPU Schedulers for Different Parts of the Machine


Linux 7.3's sched_ext sub-scheduler support is now considered feature-complete. A root BPF scheduler can delegate a cgroup subtree — together with revocable CPU grants — to a nested scheduler, which then controls scheduling decisions for its workloads. 

**Angle:** This is a considerably bigger conceptual change than “Linux lets you write schedulers in BPF”.

Historically:

`machine → kernel scheduler → all workloads`

We're moving towards:

`machine`

`├─ latency-sensitive service → scheduler A`

`├─ batch jobs → scheduler B`

`├─ VM/container group → scheduler C`

`└─ desktop workloads → scheduler D`

That starts to make CPU scheduling look less like a global kernel policy and more like a **hierarchical resource-control API**.

The particularly interesting platform-engineering question is whether orchestration systems eventually start selecting scheduling policy as a workload property:

`latency-class: interactive`

`throughput-class: batch`

`cpu-policy: energy-efficient`

rather than merely requesting `cpu: 4`.

At that point the Kubernetes scheduler decides *which machine* runs the workload, while a workload-specific kernel scheduler decides **how time behaves once it gets there**.

**Matches:** Linux kernel, eBPF, Kubernetes, platform engineering, performance, workload isolation.

**Format:** **Long-form article**

**Confidence: 0.99 — probably my favourite systems piece today.**

---
