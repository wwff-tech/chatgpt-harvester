---
date: 2026-08-25
item_number: 4
title: Recovery Is a Different Operating Mode
summary: The GitHub incident supports a broader reliability principle. During restoration, some services had already recovered while others — particularly Copilot components — remained constrained, and retries complicated bringing them back.
angle: "We often model:"
interests:
  - SRE
  - graceful degradation
  - incident response
  - state machines
format: Short post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 4. Recovery Is a Different Operating Mode


The GitHub incident supports a broader reliability principle. During restoration, some services had already recovered while others — particularly Copilot components — remained constrained, and retries complicated bringing them back. 

**Angle:** We often model:

`healthy ↔ unhealthy`.

Real systems have another important state:

`healthy → failed → recovering → healthy`.

During `recovering`:

- caches may be empty;
- connection pools are rebuilding;
- replicas may be resynchronising;
- queues may contain backlog;
- clients are retrying;
- operators are changing things.

So perhaps recovery deserves explicit policy:

`reduced admission limits`

`disabled expensive features`

`prioritised request classes`

`stricter retry budgets`

`progressive reopening`.

**Recovery isn't merely “healthy, but not yet”. It has different safe operating limits.**

**Matches:** SRE, graceful degradation, incident response, state machines.

**Format:** **Short post**

**Confidence: 0.99.**

---
