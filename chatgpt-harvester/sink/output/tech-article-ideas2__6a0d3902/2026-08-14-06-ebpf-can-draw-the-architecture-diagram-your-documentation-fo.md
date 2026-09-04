---
date: 2026-08-14
item_number: 6
title: "**“eBPF Can Draw the Architecture Diagram Your Documentation Forgot”** — Long-form / experimental article"
summary: "Recent research uses eBPF network tracing to infer runtime microservice dependencies **without application instrumentation**. In its 20-service test environment, it recovered every service identity, identified 32 dependency edges from three minutes of traffic, then used that graph to choose a migration sequence that reduced simulated cross-VM traffic exposure by 27% versus arbitrary ordering."
angle: "The migration algorithm is secondary. The interesting idea is **observed architecture versus declared architecture**."
interests:
  - eBPF
  - observability
  - microservices
  - platform engineering
  - architecture discovery
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 6. **“eBPF Can Draw the Architecture Diagram Your Documentation Forgot”** — Long-form / experimental article


Recent research uses eBPF network tracing to infer runtime microservice dependencies **without application instrumentation**. In its 20-service test environment, it recovered every service identity, identified 32 dependency edges from three minutes of traffic, then used that graph to choose a migration sequence that reduced simulated cross-VM traffic exposure by 27% versus arbitrary ordering. 

There is an important caveat: at near-saturation load, throughput fell only 4.4%, but median latency rose **383%** and p99 by **1,050%**. The authors explicitly recommend off-peak capture or dedicated sampling. 

**Angle:** The migration algorithm is secondary. The interesting idea is **observed architecture versus declared architecture**.

CMDB says A talks to B.

Terraform says A *can* talk to B.

Network policy says A is *allowed* to talk to B.

eBPF says:

> A actually talks to B 18,000 times per minute.

Those are four different graphs.

A platform capable of continuously comparing them could identify undocumented dependencies, dead permissions, unexpected coupling, and migration risk.

**Matches:** eBPF, observability, microservices, platform engineering, architecture discovery.

**Confidence: 0.93 on the idea; the experiment is deliberately small, so I would not generalise its performance numbers.**

---
