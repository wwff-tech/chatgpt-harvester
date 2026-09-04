---
date: 2026-08-24
item_number: 2
title: Four GPUs Is Not a Resource Specification
summary: "DRM Fabric exposes a problem we've already encountered with NUMA and CPU scheduling: **quantity increasingly fails to describe useful compute**."
angle: "Compare two allocations:"
interests:
  - Kubernetes
  - scheduling
  - GPUs
  - NUMA
  - platform APIs
format: Short post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 2. Four GPUs Is Not a Resource Specification


DRM Fabric exposes a problem we've already encountered with NUMA and CPU scheduling: **quantity increasingly fails to describe useful compute**. 

**Angle:** Compare two allocations:

`4 × GPU connected through one fast fabric`

and:

`4 × GPU scattered across PCIe roots / hosts / slower links`.

Both satisfy:

`gpu: 4`.

They can have radically different performance.

The same pattern exists elsewhere:

`cpu: 32` ignores LLC/NUMA topology;

`disk: 10 TB` ignores IOPS and failure domains;

`network: 10 Gbit/s` ignores latency;

`gpu: 4` ignores interconnect.

A useful platform-engineering principle:

> **Resources become topology when the cost of communication approaches the cost of computation.**

**Matches:** Kubernetes, scheduling, GPUs, NUMA, platform APIs.

**Format:** **Short post**

**Confidence: 0.98.**

---
