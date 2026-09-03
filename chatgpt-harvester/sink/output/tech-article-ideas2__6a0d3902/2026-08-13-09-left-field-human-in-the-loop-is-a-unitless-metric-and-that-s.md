---
date: 2026-08-13
item_number: 9
title: "Left-field — “Human-in-the-Loop Is a Unitless Metric, and That's the Problem”"
summary: "The Taiwan incident makes a broader systems problem visible: saying a system has “human oversight” tells us almost nothing about the amount of leverage the machine provides."
angle: "Define an approximate **automation amplification factor**:"
interests:
  - SRE
  - automation
  - HITL
  - agent governance
  - systems safety
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 9. Left-field — “Human-in-the-Loop Is a Unitless Metric, and That's the Problem”


The Taiwan incident makes a broader systems problem visible: saying a system has “human oversight” tells us almost nothing about the amount of leverage the machine provides. 

**Angle:** Define an approximate **automation amplification factor**:

\[
A = \frac{\text{consequential machine actions}}{\text{human decisions}}
\]

A conventional admin session might have modest amplification.

Terraform already has considerably more:

`terraform apply` → 300 infrastructure mutations.

GitOps can have more still:

`git merge` → fleet-wide convergence.

An agent swarm can potentially make it enormous.

Safety therefore isn't simply:

`human present = safe`

It depends on:

`amplification × reversibility × blast radius × observability`

That could become a genuinely useful framework spanning SRE, AI agents, CI/CD, robotics, and industrial automation.

**Matches:** SRE, automation, HITL, agent governance, systems safety.

**Format:** **Long-form article**

**Confidence: 0.97 — my favourite conceptual seed tonight.**

---
