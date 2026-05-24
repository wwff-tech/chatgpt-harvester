---
date: 2026-04-26
item_number: 1
title: “Audit Trail Synthesiser” (Human-Readable System Narratives)
interests:
suggested_points:
conversation_id: 69e5608e-48c0-83eb-9533-b3a6d9e148c7
label: project ideas
---

## 1. “Audit Trail Synthesiser” (Human-Readable System Narratives)


**Problem**  
Logs, traces, and events exist, but reconstructing a coherent “story” of what happened requires significant effort and expertise.

**Approaches**
- Convert event streams into structured narratives (timeline + causality)
- Collapse low-signal events into grouped actions
- Highlight anomalies and decision points

**Tech hints**
- OpenTelemetry ingestion
- Graph traversal + causal inference
- Structured summarisation (schema-first, LLM optional)
- DuckDB for local aggregation

**Formats**
- CLI (`trace → narrative`)
- HTML report generator
- Incident postmortem tool

**Why good fit**
- Strong alignment with your focus on explainability
- High leverage during incidents and audits
- Works locally for privacy

**Why not**
- Risk of incorrect causal inference
- Needs high-quality telemetry

**Revenue potential**
- Medium → High

**Content potential**
- Very high (“Your logs are not telling you the story”)

**Community potential**
- High

**Tags**
`observability`, `audit`, `tracing`, `explainability`

**References**
- https://opentelemetry.io/  
- https://jaegertracing.io/  

---
