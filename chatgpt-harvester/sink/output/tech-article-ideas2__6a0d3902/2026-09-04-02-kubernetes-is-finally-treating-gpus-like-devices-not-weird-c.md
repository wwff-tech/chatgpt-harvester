---
date: 2026-09-04
item_number: 2
title: Kubernetes Is Finally Treating GPUs Like Devices, Not Weird CPUs
summary: "The same Kubernetes 1.37 DRA update graduates **Extended Resource support to GA**. Existing workloads can continue requesting resources such as `example.com/gpu`, while a DRA driver performs the actual device allocation underneath; workloads don't need to adopt `ResourceClaim` immediately. Device taints are also now stable, and DRA can expose richer per-device state and metadata."
angle: "Kubernetes's historical resource abstraction works beautifully for:"
interests:
  - Kubernetes
  - GPUs
  - heterogeneous compute
  - platform engineering
  - AI infrastructure
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 2. Kubernetes Is Finally Treating GPUs Like Devices, Not Weird CPUs


The same Kubernetes 1.37 DRA update graduates **Extended Resource support to GA**. Existing workloads can continue requesting resources such as `example.com/gpu`, while a DRA driver performs the actual device allocation underneath; workloads don't need to adopt `ResourceClaim` immediately. Device taints are also now stable, and DRA can expose richer per-device state and metadata. 

**Angle:** Kubernetes's historical resource abstraction works beautifully for:

`CPU = divisible quantity`

`RAM = divisible quantity`.

Hardware accelerators aren't like that.

A GPU, FPGA, NIC, DPU, or other accelerator has:

`identity`

`topology`

`firmware`

`health`

`capabilities`

`locality`

and sometimes:

`fractional capacity`.

DRA is Kubernetes gradually acknowledging that **hardware allocation is a scheduling domain in its own right**, rather than pretending every scarce resource can be represented by an integer attached to a node.

The compatibility mechanism is particularly good engineering: existing `nvidia.com/gpu: 1`-style workloads can remain unchanged while the allocation machinery underneath evolves.

> Good infrastructure migrations change the implementation before they force everyone to change the interface.

**Matches:** Kubernetes, GPUs, heterogeneous compute, platform engineering, AI infrastructure.

**Format:** **Long-form article**

**Confidence: 0.99.**

---
