---
date: 2026-08-30
item_number: 1
title: The AI Cloud Is Relearning Twenty Years of Multi-Tenant Security the Hard Way
summary: "SemiAnalysis published results today from four months of testing across **25 neocloud providers and 32 clusters**. Researchers report finding cross-tenant metadata exposure, reachable BMC networks, missing network isolation, incorrectly configured InfiniBand security keys, storage RBAC failures, overprivileged monitoring, container/VM escapes, and at least one vulnerability chain producing demonstrated cross-tenant RCE between test tenants. Providers were notified and the disclosed examples were reportedly remediated."
angle: "Don't write “neoclouds are insecure”. The better argument is that GPU infrastructure is colliding with the same economics that produced hyperscaler security architecture."
interests:
  - Kubernetes
  - cloud security
  - GPU infrastructure
  - networking
  - BMCs
  - multi-tenancy
  - platform engineering
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 1. The AI Cloud Is Relearning Twenty Years of Multi-Tenant Security the Hard Way


SemiAnalysis published results today from four months of testing across **25 neocloud providers and 32 clusters**. Researchers report finding cross-tenant metadata exposure, reachable BMC networks, missing network isolation, incorrectly configured InfiniBand security keys, storage RBAC failures, overprivileged monitoring, container/VM escapes, and at least one vulnerability chain producing demonstrated cross-tenant RCE between test tenants. Providers were notified and the disclosed examples were reportedly remediated. 

**Angle:** Don't write “neoclouds are insecure”. The better argument is that GPU infrastructure is colliding with the same economics that produced hyperscaler security architecture.

Early hosting looked like:

`many customers → one Unix machine → permissions`.

Cloud eventually evolved:

`tenant → identity boundary → VPC → VM → isolated control plane → hardware/firmware lifecycle`.

GPU scarcity and cost are pushing new providers towards aggressive sharing of extraordinarily expensive hardware, but some appear to be skipping parts of that evolutionary history.

Particularly interesting is the sheer number of **non-CPU trust boundaries** involved:

`BMC`

`InfiniBand fabric`

`BlueField DPU`

`GPU`

`storage network`

`Kubernetes control plane`

`monitoring stack`.

A conventional cloud threat model centred around VM isolation is incomplete.

> **AI infrastructure has turned the server's peripheral architecture into part of the tenant security model.**

**Matches:** Kubernetes, cloud security, GPU infrastructure, networking, BMCs, multi-tenancy, platform engineering.

**Format:** **Long-form article**

**Confidence: 0.97.** The evidence is detailed and based on broad hands-on testing, but this is one research organisation's assessment rather than an independent industry-wide audit.

---
