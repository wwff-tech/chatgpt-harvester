---
date: 2026-08-22
item_number: 10
title: Left-field — “Technical Debt Is Often a Promise, Not Code”
summary: The ARM cleanup points towards a broader definition of technical debt.
angle: "We usually visualise technical debt as ugly implementation:"
interests:
  - software architecture
  - platform lifecycle
  - engineering leadership
  - APIs
  - legacy systems
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 10. Left-field — “Technical Debt Is Often a Promise, Not Code”


The ARM cleanup points towards a broader definition of technical debt. 

**Angle:** We usually visualise technical debt as ugly implementation:

`bad abstraction`

`old library`

`hacky code`.

But the expensive thing may actually be the **promise the code exists to uphold**:

> We still support this architecture.

> This API remains backwards-compatible.

> This configuration format still loads.

> This customer can still authenticate this way.

> This filesystem still mounts.

Once the promise exists, clean code doesn't eliminate its maintenance cost.

That suggests distinguishing:

`implementation debt` — poor means of satisfying requirements

from:

`obligation debt` — requirements whose continuing value no longer exceeds their maintenance cost.

The latter is often impossible to refactor away.

You have to **stop promising it**.

**Matches:** software architecture, platform lifecycle, engineering leadership, APIs, legacy systems.

**Format:** **Long-form article**

**Confidence: 0.99 — strongest evergreen idea today.**
