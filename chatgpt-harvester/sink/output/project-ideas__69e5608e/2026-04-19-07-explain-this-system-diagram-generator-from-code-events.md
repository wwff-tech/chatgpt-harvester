---
date: 2026-04-19
item_number: 7
title: “Explain This System” – Diagram Generator from Code + Events
interests:
suggested_points:
conversation_id: 69e5608e-48c0-83eb-9533-b3a6d9e148c7
label: project ideas
---

## 7. “Explain This System” – Diagram Generator from Code + Events


**Problem**  
Understanding systems is slow. Docs drift. Diagrams are outdated.

**Approaches**
- Static: parse code → infer components
- Dynamic: ingest events/logs → infer flows
- Hybrid: combine both into living diagrams

**Tech hints**
- AST parsing
- OpenTelemetry traces
- Mermaid / Graphviz
- FastAPI backend

**Formats**
- CLI + HTML output
- VSCode extension
- CI step (generate diagrams on PR)

**Why good fit**
- Aligns with your “diagrams as reasoning tools” belief
- Strong book tie-in

**Why not**
- Hard inference problem
- Risk of “cool demo, low daily use”

**Revenue potential**
- Low → Medium

**Content potential**
- Very high

**Community potential**
- Medium

**Tags**
`diagrams`, `observability`, `ast`, `otel`

**References**
- https://opentelemetry.io  
- https://mermaid.js.org
