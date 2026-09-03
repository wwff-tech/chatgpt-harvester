---
date: 2026-08-27
item_number: 9
title: Left-field — “A Robot API Needs Units in Its Type System”
summary: MHS opens a surprisingly deep software-design problem.
angle: Plenty of physical disasters begin with semantically valid numbers.
interests:
  - embedded engineering
  - robotics
  - API design
  - type systems
  - agents
  - safety
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 9. Left-field — “A Robot API Needs Units in Its Type System”


MHS opens a surprisingly deep software-design problem. 

**Angle:** Plenty of physical disasters begin with semantically valid numbers.

The canonical software horror story is unit confusion:

`125 metres`

interpreted as:

`125 feet`.

Agents controlling physical systems make this considerably more consequential.

A hardware protocol ideally shouldn't expose:

`set_speed(100)`.

It should expose something conceptually closer to:

`set_speed(100_mm_per_second)`,

with machine-readable:

`range: 0..250 mm/s`

`acceleration-limit: 1000 mm/s²`

`requires-door-closed: true`.

This is essentially **dependent typing for machinery**, even if implemented much more pragmatically through schemas and constraints.

Physical APIs should make unsafe states difficult to express, not merely document them in prose for the model to remember.

**Matches:** embedded engineering, robotics, API design, type systems, agents, safety.

**Format:** **Long-form article**

**Confidence: 0.99 — excellent left-field piece.**

---
