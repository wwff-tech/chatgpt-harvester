---
date: 2026-08-26
item_number: 4
title: "Detection Is Useful When It Changes the Attacker's Plan"
summary: The CISA comparison suggests a much better way to think about detection quality than dashboard volume.
angle: A detection that fires but changes nothing has limited operational value.
interests:
  - security architecture
  - observability
  - SRE
  - incident response
format: Short post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 4. Detection Is Useful When It Changes the Attacker's Plan


The CISA comparison suggests a much better way to think about detection quality than dashboard volume. 

**Angle:** A detection that fires but changes nothing has limited operational value.

A detection that causes:

`credential revoked`

`host isolated`

`route blocked`

`account challenged`

`service constrained`

forces the adversary to spend additional time and capability.

So perhaps a useful defensive measure is **attacker work amplification**:

\[
A = \frac{\text{attacker effort after controls}}
         {\text{attacker effort without controls}}
\]

You don't need perfect prevention if every successful defensive layer makes continuing materially more expensive.

That maps rather nicely onto SRE thinking: resilience isn't necessarily preventing every failure; sometimes it is preventing one failure from becoming the easy path to the next.

**Matches:** security architecture, observability, SRE, incident response.

**Format:** **Short post**

**Confidence: 0.98.**

---
