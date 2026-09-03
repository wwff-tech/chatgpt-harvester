---
date: 2026-05-20
item_number: 1
title: Operational Memory Layer
summary: "This creates: - repeated incidents, - configuration archaeology, - fragile tribal knowledge."
interests:
suggested_points:
conversation_id: 69e5608e-48c0-83eb-9533-b3a6d9e148c7
label: project ideas
---

# 1. Operational Memory Layer


## Problem
Modern infrastructure loses institutional memory:
- why alerts were tuned,
- why retries were added,
- why a workaround exists,
- why an SLO changed.

This creates:
- repeated incidents,
- configuration archaeology,
- fragile tribal knowledge.

## Approaches
- Attach rationale metadata to infra/config/code changes  
- Build searchable timelines of operational intent  
- Auto-link incidents ↔ mitigations ↔ architectural decisions  

## Suggested tech hints
- Git hooks + commit enrichment  
- OpenTelemetry trace correlation  
- Event sourcing  
- Vector search over postmortems  
- Knowledge graph storage  

Use:
- OpenTelemetry
- graph DBs,
- semantic embeddings,
- immutable append-only logs.

## Suggested formats
- Internal platform  
- Grafana plugin  
- VSCode extension  
- Incident review system  
- CLI timeline explorer  

## Why it is a good fit
- Strong SRE pain point  
- Organisational memory is massively undervalued  
- Fits current “AI observability” discussions 

## Why it is not a good fit
- Requires cultural adoption  
- Metadata hygiene can decay quickly  

## Revenue potential
High

## Content tie-in potential
Extremely high

## Community potential
High

## Tags/keywords
`operational-memory`, `sre`, `incident-management`, `knowledge-graphs`, `observability`

## References
- https://opentelemetry.io/
- https://sre.google/sre-book/
- https://martinfowler.com/eaaDev/EventSourcing.html

---
