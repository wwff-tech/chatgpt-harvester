---
date: 2026-09-04
item_number: 1
title: Your Scheduler Became O(N²) Because Everything Woke Up
summary: "Kubernetes 1.37 adds a new `PreQueueingHint` path for Dynamic Resource Allocation. Previously, a ResourceClaim event could cause the scheduler to reconsider **every unschedulable Pod**; during large scale-ups this produced O(N²) behaviour. The new implementation indexes affected Pods so the requeue decision becomes approximately O(1), with Kubernetes reporting roughly doubled scheduling throughput in early benchmarks."
angle: "The DRA specifics are useful, but the article is really about **accidental fan-out**."
interests:
  - Kubernetes
  - scheduler internals
  - SRE
  - distributed systems
  - performance engineering
format: Long-form technical article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 1. Your Scheduler Became O(N²) Because Everything Woke Up


Kubernetes 1.37 adds a new `PreQueueingHint` path for Dynamic Resource Allocation. Previously, a ResourceClaim event could cause the scheduler to reconsider **every unschedulable Pod**; during large scale-ups this produced O(N²) behaviour. The new implementation indexes affected Pods so the requeue decision becomes approximately O(1), with Kubernetes reporting roughly doubled scheduling throughput in early benchmarks. 

**Angle:** The DRA specifics are useful, but the article is really about **accidental fan-out**.

A system receives one event:

`resource changed`

and reacts with:

`wake everybody who might possibly care`.

At small scale that's wonderfully simple. At large scale:

\[
Events \times PotentialConsumers
\]

quietly becomes your scalability limit.

This pattern appears everywhere: Kubernetes controllers, cache invalidation, CI pipelines, filesystem watchers, service discovery, pub/sub, and agent orchestration. The better abstraction is often not “broadcast and let consumers decide”, but **maintain enough dependency information to address only affected consumers**.

The trade-off is equally worth discussing: you exchange cheap implementation simplicity for indexes that themselves need to remain correct.

**Matches:** Kubernetes, scheduler internals, SRE, distributed systems, performance engineering.

**Format:** **Long-form technical article**

**Confidence: 0.99.**

Kubernetes 1.37 DRA update

---
