---
date: 2026-08-13
item_number: 4
title: "Open Architecture Doesn't Mean Open Microarchitecture"
summary: "The same RISC-V research provides a neat educational point: two processors implementing the same ISA can have radically different security characteristics because speculative machinery lives beneath the architectural contract."
angle: Draw the analogy to APIs.
interests:
  - CPU architecture
  - API design
  - security engineering
  - formal specification
format: Short post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 4. Open Architecture Doesn't Mean Open Microarchitecture


The same RISC-V research provides a neat educational point: two processors implementing the same ISA can have radically different security characteristics because speculative machinery lives beneath the architectural contract. 

**Angle:** Draw the analogy to APIs.

An API tells you:

> what behaviour I promise.

It generally does **not** tell you:

> how I achieve it.

Security failures routinely emerge in the latter.

RISC-V therefore gives a very clean hardware example of why **specification compliance is necessary but insufficient evidence of system security**.

**Matches:** CPU architecture, API design, security engineering, formal specification.

**Format:** **Short post**

**Confidence: 0.95.**

---
