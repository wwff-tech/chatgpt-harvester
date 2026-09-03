---
date: 2026-08-14
item_number: 2
title: "Your Agent's Tools Matter More Than Another Page of Prompt Engineering"
summary: "A new study from Purdue, Microsoft Research, and the University of Chicago ran **11,700 coding-agent trajectories** while holding underlying capabilities broadly similar but changing how those capabilities were exposed. Structured low-level interfaces improved repeatability by as much as **4.7×**, while CodeAct-style Python interfaces achieved similar performance with **41.6% fewer steps and 56.3% fewer tokens**."
angle: "This is unusually good evidence for treating **agent harness design as API design**."
interests:
  - coding agents
  - MCP/tool design
  - agent harnesses
  - APIs
  - developer tooling
format: Long-form
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 2. Your Agent's Tools Matter More Than Another Page of Prompt Engineering


A new study from Purdue, Microsoft Research, and the University of Chicago ran **11,700 coding-agent trajectories** while holding underlying capabilities broadly similar but changing how those capabilities were exposed. Structured low-level interfaces improved repeatability by as much as **4.7×**, while CodeAct-style Python interfaces achieved similar performance with **41.6% fewer steps and 56.3% fewer tokens**. 

Perhaps more interestingly, lightweight tools allowing agents to record intermediate reasoning had **limited effect**. 

**Angle:** This is unusually good evidence for treating **agent harness design as API design**.

We've spent enormous effort asking:

> Which model?

and:

> Which prompt?

The paper suggests another major variable:

> **What shape does the world have from the model's perspective?**

A shell, structured filesystem API, semantic search, Python execution environment, and thirty narrow MCP tools may expose nominally identical capabilities but create radically different search spaces.

There's an excellent Unix comparison available: good tools don't merely add capability; they make useful actions **cheap to express and easy to compose**.

**Matches:** coding agents, MCP/tool design, agent harnesses, APIs, developer tooling.

**Confidence: 0.98 — very strong fit.**

---
