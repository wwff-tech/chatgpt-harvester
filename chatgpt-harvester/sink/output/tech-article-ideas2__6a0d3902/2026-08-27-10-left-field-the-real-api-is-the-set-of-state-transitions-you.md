---
date: 2026-08-27
item_number: 10
title: Left-field — “The Real API Is the Set of State Transitions You Permit”
summary: Physical agents also expose a weakness in how we normally think about APIs.
angle: "We typically describe an API as a collection of functions:"
interests:
  - state machines
  - agent governance
  - embedded systems
  - safety engineering
  - capability security
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 10. Left-field — “The Real API Is the Set of State Transitions You Permit”


Physical agents also expose a weakness in how we normally think about APIs. 

**Angle:** We typically describe an API as a collection of functions:

`open()`

`move()`

`heat()`

`close()`.

But safety usually depends on **sequence**:

`open → heat`

may be forbidden;

`close → verify → heat`

may be safe.

So the true interface is not merely:

\[
API = \{operations\}
\]

but:

\[
API = \{allowed\ state\ transitions\}
\]

That's already how good industrial controllers, transaction systems, network protocols, and workflow engines behave.

Agents make the distinction impossible to ignore because they are unusually good at finding legal operations and composing them into unexpected sequences.

The natural implementation is a state machine sitting **outside the model**:

```text
IDLE → LOADED → SEALED → ACTIVE → COOLING → SAFE_TO_OPEN
```

The agent chooses among currently legal transitions; it does not decide what transitions are legal.

That is probably a stronger general architecture for high-authority agents too.

**Matches:** state machines, agent governance, embedded systems, safety engineering, capability security.

**Format:** **Long-form article**

**Confidence: 0.99 — strongest evergreen concept tonight.**
