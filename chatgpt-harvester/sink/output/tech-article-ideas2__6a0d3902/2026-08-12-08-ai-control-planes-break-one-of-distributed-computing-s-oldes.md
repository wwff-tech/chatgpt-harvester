---
date: 2026-08-12
item_number: 8
title: "**“AI Control Planes Break One of Distributed Computing's Oldest Assumptions”** — Long-form / research seed"
summary: "A recent paper proposes the term **Post-Deterministic Distributed Systems** for systems containing conventional software alongside stochastic agents. Its central observation is worthwhile even if the terminology doesn't stick: traditional distributed systems generally assume that a correct participant executes specified behaviour deterministically; an LLM-backed participant can produce different internal reasoning and actions while still satisfying the same semantic goal."
angle: This intersects beautifully with SRE.
interests:
  - agentic infrastructure
  - distributed systems
  - state machines
  - policy gates
  - SRE
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 8. **“AI Control Planes Break One of Distributed Computing's Oldest Assumptions”** — Long-form / research seed


A recent paper proposes the term **Post-Deterministic Distributed Systems** for systems containing conventional software alongside stochastic agents. Its central observation is worthwhile even if the terminology doesn't stick: traditional distributed systems generally assume that a correct participant executes specified behaviour deterministically; an LLM-backed participant can produce different internal reasoning and actions while still satisfying the same semantic goal. 

**Angle:** This intersects beautifully with SRE.

Distributed systems already cope with:

`message loss`

`reordering`

`latency`

`crashes`

`Byzantine participants`

but an agent introduces something slightly different:

`same state + same request → several individually reasonable next states`

You don't necessarily want deterministic model output. You want **deterministic invariants around non-deterministic decision-making**.

So:

`stochastic proposal → deterministic policy → deterministic state transition → observable result`

is probably a more useful architecture than trying to force the model itself to behave deterministically.

**Matches:** agentic infrastructure, distributed systems, state machines, policy gates, SRE.

**Confidence: 0.92 on the underlying problem; 0.65 that “post-deterministic distributed systems” becomes useful lasting terminology.**

---
