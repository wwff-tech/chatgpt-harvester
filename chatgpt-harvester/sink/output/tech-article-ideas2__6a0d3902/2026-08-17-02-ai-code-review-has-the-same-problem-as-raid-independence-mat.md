---
date: 2026-08-17
item_number: 2
title: "AI Code Review Has the Same Problem as RAID: Independence Matters"
summary: "The Snowflake incident also supports a very compact argument. Copilot assistance plus AI review sounds like two layers of protection, but layers are useful only insofar as their failures aren't strongly correlated."
angle: Borrow reliability maths.
interests:
  - SRE
  - reliability theory
  - AI coding
  - software testing
format: Short post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 2. AI Code Review Has the Same Problem as RAID: Independence Matters


The Snowflake incident also supports a very compact argument. Copilot assistance plus AI review sounds like two layers of protection, but layers are useful only insofar as their failures aren't strongly correlated. 

**Angle:** Borrow reliability maths.

Two disks from the same manufacturing batch aren't as independent as two genuinely different failure domains.

Likewise:

`model family A → model family A critic`

is weaker than it appears if both learned similar coding idioms and security assumptions.

The useful engineering question becomes:

> **What evidence would fail independently of the generator?**

Tests generated from the same reasoning may not qualify.

**Matches:** SRE, reliability theory, AI coding, software testing.

**Format:** **Short post**

**Confidence: 0.98.**

---
