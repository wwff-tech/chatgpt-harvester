---
date: 2026-08-24
item_number: 1
title: The GPU Is Becoming a Network
summary: "Intel engineers proposed **DRM Fabric** today: vendor-neutral, protocol-agnostic Linux infrastructure for describing scale-up interconnects between GPUs and AI accelerators. Its topology is explicitly modelled as `fabric → endpoint → port → peer`, and peers can even represent accelerators controlled by another OS or switches in another trust domain. The proposal arrives just after AMD's substantial UALink work."
angle: Stop treating an accelerator as a PCIe peripheral.
interests:
  - Linux
  - GPU/AI infrastructure
  - Kubernetes
  - networking
  - distributed systems
  - topology-aware scheduling
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 1. The GPU Is Becoming a Network


Intel engineers proposed **DRM Fabric** today: vendor-neutral, protocol-agnostic Linux infrastructure for describing scale-up interconnects between GPUs and AI accelerators. Its topology is explicitly modelled as `fabric → endpoint → port → peer`, and peers can even represent accelerators controlled by another OS or switches in another trust domain. The proposal arrives just after AMD's substantial UALink work. 

**Angle:** Stop treating an accelerator as a PCIe peripheral.

A modern accelerator system increasingly resembles:

`CPU`

`├── GPU A ── high-speed fabric ── GPU B`

`│                 │`

`│               switch`

`│                 │`

`└── GPU C ───────── GPU D`

Once topology affects bandwidth, memory reachability, placement, failure domains, and peer-to-peer transfers, **accelerator scheduling becomes network scheduling**.

That raises some very SRE-shaped questions. How do you represent degraded links? How does an orchestrator distinguish four GPUs sharing a fast fabric from four merely present GPUs? How do you expose topology without making every application hardware-specific? What happens when a fabric crosses an OS or trust boundary?

There is a particularly good Kubernetes argument here. Today's resource request says roughly:

`nvidia.com/gpu: 4`

Tomorrow it may need to say something closer to:

> four mutually reachable accelerators with minimum interconnect properties.

That's a qualitative shift from **resource counting to topology allocation**.

**Matches:** Linux, GPU/AI infrastructure, Kubernetes, networking, distributed systems, topology-aware scheduling.

**Format:** **Long-form article**

**Confidence: 0.99 — strongest systems piece today.**

---
