---
date: 2026-09-02
item_number: 10
title: "**Left-field — “Bound the Thing That Can Kill You”** — Long-form / evergreen"
summary: Kubernetes RangeStream gives this an excellent concrete hook.
angle: "Systems frequently constrain an easy-to-count proxy:"
interests:
  - SRE
  - distributed systems
  - capacity planning
  - agent governance
  - Kubernetes
format: Long-form evergreen article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 10. **Left-field — “Bound the Thing That Can Kill You”** — Long-form / evergreen


Kubernetes RangeStream gives this an excellent concrete hook. 

**Angle:** Systems frequently constrain an easy-to-count proxy:

`100 objects`

`10 requests/sec`

`1,000 queue messages`

`20 worker processes`.

But the actual failure variable might be:

`bytes`

`CPU seconds`

`database work`

`memory`

`fan-out`

`external API cost`.

If object sizes vary by 1,000×, then:

`LIMIT 100`

is barely a resource limit at all.

A stronger engineering discipline is:

1. identify the quantity whose exhaustion causes failure;
2. measure or estimate it directly;
3. put the bound there.

So:

`message count → queue bytes`

`request count → concurrency/work budget`

`object count → memory bytes`

`agent tool calls → authority/cost budget`.

The agent connection is particularly nice: limiting an agent to **100 actions** says almost nothing if action #73 is `terraform destroy`.

> **Bound the dangerous resource, not whatever happens to be easiest to count.**

**Matches:** SRE, distributed systems, capacity planning, agent governance, Kubernetes.

**Format:** **Long-form evergreen article**

**Confidence: 0.99.**
