---
date: 2026-08-15
item_number: 9
title: Left-field — “Code Review Is a Congestion-Control Problem”
summary: The Debian debate points towards something broader than AI. Open-source contribution has traditionally assumed that producing a patch costs enough effort to naturally rate-limit submissions. Generative tooling destroys that assumption.
angle: Internet protocols already solved an analogous problem.
interests:
  - SRE
  - queueing theory
  - engineering management
  - open source
  - agentic development
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 9. Left-field — “Code Review Is a Congestion-Control Problem”


The Debian debate points towards something broader than AI. Open-source contribution has traditionally assumed that producing a patch costs enough effort to naturally rate-limit submissions. Generative tooling destroys that assumption. 

**Angle:** Internet protocols already solved an analogous problem.

If senders transmit faster than receivers can process:

`queue grows → latency grows → loss occurs → sender backs off`

Software collaboration rarely has explicit congestion control.

Imagine contribution systems exposing reviewer pressure:

`review capacity = 40 points/week`

and submissions carrying estimated verification cost:

`typo = 1`

`dependency bump = 2`

`new subsystem = 30`

`4,000-line agent-generated refactor = 200`

Admission could then respond to **review cost**, not merely PR count.

It sounds slightly absurd until you notice that large organisations already approximate this manually through change freezes, CODEOWNERS, approval requirements, and merge queues.

**Matches:** SRE, queueing theory, engineering management, open source, agentic development.

**Format:** **Long-form article**

**Confidence: 0.97.**

---
