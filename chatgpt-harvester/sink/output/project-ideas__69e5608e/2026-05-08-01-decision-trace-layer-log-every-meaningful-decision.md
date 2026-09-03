---
date: 2026-05-08
item_number: 1
title: “Decision Trace Layer” (Log Every Meaningful Decision)
interests:
suggested_points:
conversation_id: 69e5608e-48c0-83eb-9533-b3a6d9e148c7
label: project ideas
---

# 1. “Decision Trace Layer” (Log Every Meaningful Decision)


**Problem**  
Modern systems log events, but not decisions. Critical choices (retry vs fail, escalate vs suppress, tool A vs tool B) are implicit.

**Approaches**
- Instrument systems to emit decision events  
- Capture context, inputs, alternatives, and confidence  
- Build replayable decision timelines  

**Tech hints**
- Extend OpenTelemetry with decision spans  
- Structured logging (JSON with decision schema)  
- Context propagation across services  
- Storage in columnar DB (ClickHouse-style)  

**Formats**
- Middleware SDK  
- Observability plugin  
- CLI trace explorer  

**Why good fit**
- Complements existing observability  
- High relevance for AI + SRE  
- Enables downstream tooling (audit, optimisation)

**Why not**
- Instrumentation overhead  
- Risk of excessive logging  

**Revenue potential**  
High  

**Content potential**  
Very high  

**Community potential**  
High  

**Tags**  
`decision-making`, `observability`, `tracing`, `ai`, `sre`

**References**
- https://opentelemetry.io/  
- https://queue.acm.org/detail.cfm?id=3526967  

---
