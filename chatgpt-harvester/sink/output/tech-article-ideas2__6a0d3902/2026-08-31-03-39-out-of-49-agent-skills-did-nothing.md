---
date: 2026-08-31
item_number: 3
title: 39 Out of 49 Agent Skills Did Nothing
summary: "A new benchmark, **SWE-Skills-Bench**, tests whether the increasingly popular practice of supplying coding agents with reusable instruction/skill packages actually improves end-to-end software-engineering performance. Across roughly **565 tasks**, 39 of the 49 evaluated skills produced **zero pass-rate improvement**, with an average gain of only **+1.2%**."
angle: This is a much more useful AI story than another model leaderboard because it tests an increasingly common engineering practice.
interests:
  - agent-assisted development
  - context engineering
  - coding agents
  - evaluation
  - developer tooling
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 3. 39 Out of 49 Agent Skills Did Nothing


A new benchmark, **SWE-Skills-Bench**, tests whether the increasingly popular practice of supplying coding agents with reusable instruction/skill packages actually improves end-to-end software-engineering performance. Across roughly **565 tasks**, 39 of the 49 evaluated skills produced **zero pass-rate improvement**, with an average gain of only **+1.2%**. 

Some specialised skills did help substantially — up to +30% — while three actually reduced success rates by as much as 10%. Token consumption ranged as high as a **451% increase without corresponding improvement**. 

SWE-Skills-Bench paper

**Angle:** This is a much more useful AI story than another model leaderboard because it tests an increasingly common engineering practice.

The obvious reaction is:

> Skills don't work.

I don't think that's the interesting conclusion.

Instead:

> **Context has carrying cost.**

Giving an agent more instructions isn't free. Every additional rule competes for attention, may conflict with repository-local evidence, can become stale, and consumes tokens.

The specialised skills that helped suggest the useful model is not:

`agent + giant handbook`.

It may instead be:

`task classification`

→ `retrieve one narrowly relevant skill`

→ `check version/context compatibility`

→ `execute`

→ `discard`.

In other words, **skills probably need routing and lifecycle management**, not merely a directory full of Markdown.

**Matches:** agent-assisted development, context engineering, coding agents, evaluation, developer tooling.

**Format:** **Long-form article**

**Confidence: 0.98 on the reported experiment; generalisation beyond the tested skills/models needs care.**

---
