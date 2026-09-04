---
date: 2026-08-14
item_number: 10
title: Left-field — “The Most Accurate Architecture Diagram Might Be the One Nobody Drew”
summary: "The eBPF dependency work suggests a broader systems idea: architecture documentation is normally **intent**, whereas telemetry describes **behaviour**."
angle: "Treat architecture as three separate models:"
interests:
  - observability
  - C4
  - GitOps
  - network policy
  - eBPF
  - platform engineering
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 10. Left-field — “The Most Accurate Architecture Diagram Might Be the One Nobody Drew”


The eBPF dependency work suggests a broader systems idea: architecture documentation is normally **intent**, whereas telemetry describes **behaviour**. 

**Angle:** Treat architecture as three separate models:

`declared architecture` — what engineers believe exists

`permitted architecture` — what policy allows to exist

`observed architecture` — what actually exists

Drift between those graphs is information.

If `observed ⊄ declared`, you've discovered undocumented coupling.

If `permitted ≫ observed`, you've discovered excess authority.

If `declared ⊄ observed`, you've potentially discovered dead architecture.

This could become an interesting platform capability: continuously compile architecture diagrams from runtime evidence and diff them against C4/GitOps/policy definitions.

**Matches:** observability, C4, GitOps, network policy, eBPF, platform engineering.

**Format:** **Long-form article**

**Confidence: 0.97 — strongest evergreen idea from today's scan.**
