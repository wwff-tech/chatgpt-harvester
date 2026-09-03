---
date: 2026-08-21
item_number: 10
title: Left-field — “Reliability Is the Preservation of Options”
summary: The Linux scheduler rollback suggests a more general framing of resilience.
angle: "We normally describe reliability as:"
interests:
  - SRE
  - architecture
  - incident response
  - distributed systems
  - engineering judgement
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 10. Left-field — “Reliability Is the Preservation of Options”


The Linux scheduler rollback suggests a more general framing of resilience. 

**Angle:** We normally describe reliability as:

`uptime`

`redundancy`

`MTTR`

`error budgets`.

Another useful definition is:

> **How many safe moves remain after something unexpected happens?**

A brittle system has one path:

`forward`.

A resilient system preserves:

`rollback`

`fail over`

`degrade`

`disable feature`

`restore backup`

`isolate component`

`serve stale`

`switch provider`.

This makes optionality something you deliberately engineer.

A backwards-compatible schema preserves rollback.

A feature flag preserves disablement.

A replicated database preserves failover.

A cached copy preserves stale serving.

An offline deployment mechanism preserves recovery when GitHub disappears.

The design question becomes:

> **Which future emergency choices does this architecture permanently remove?**

That's a surprisingly powerful review heuristic.

**Matches:** SRE, architecture, incident response, distributed systems, engineering judgement.

**Format:** **Long-form article**

**Confidence: 0.99 — strongest evergreen idea tonight.**
