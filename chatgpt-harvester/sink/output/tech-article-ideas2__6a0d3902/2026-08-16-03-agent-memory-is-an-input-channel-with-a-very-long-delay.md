---
date: 2026-08-16
item_number: 3
title: Agent Memory Is an Input Channel With a Very Long Delay
summary: "Another new USENIX paper, **FragFuse**, attacks agent access controls through long-term memory. Prohibited material is fragmented across apparently benign interactions, stored separately, then later retrieved and recombined. The final request need never contain the forbidden content itself. Across three access-control mechanisms, the researchers report an average bypass rate of 86.3%."
angle: "This is worth writing about because it isn't fundamentally a prompt-injection story."
interests:
  - agent memory
  - IAM
  - taint tracking
  - state machines
  - policy enforcement
  - security architecture
format: Long-form
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 3. Agent Memory Is an Input Channel With a Very Long Delay


Another new USENIX paper, **FragFuse**, attacks agent access controls through long-term memory. Prohibited material is fragmented across apparently benign interactions, stored separately, then later retrieved and recombined. The final request need never contain the forbidden content itself. Across three access-control mechanisms, the researchers report an average bypass rate of 86.3%. 

**Angle:** This is worth writing about because it isn't fundamentally a prompt-injection story.

It is a **temporal security problem**.

Most security controls inspect:

`request(t) → decision(t)`

A stateful agent actually operates on:

`request(t) + memory(t−n … t−1) → decision(t)`

Memory therefore turns many individually harmless writes into a later dangerous read.

Databases solved related problems through provenance, row-level security, taint, transaction boundaries, and ownership. Agent memory systems largely haven't.

The important architectural rule may be:

> **Authorisation must survive storage.**

If data entered memory under principal A, context X, or trust level Y, retrieving it later should not erase those labels.

**Matches:** agent memory, IAM, taint tracking, state machines, policy enforcement, security architecture.

**Confidence: 0.99 — particularly strong fit.**

---
