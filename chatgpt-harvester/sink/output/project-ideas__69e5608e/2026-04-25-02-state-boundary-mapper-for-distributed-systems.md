---
date: 2026-04-25
item_number: 2
title: State Boundary Mapper for Distributed Systems
interests:
suggested_points:
conversation_id: 69e5608e-48c0-83eb-9533-b3a6d9e148c7
label: project ideas
---

## 2. State Boundary Mapper for Distributed Systems


**Problem**  
In distributed systems, state boundaries (ownership, consistency domains) are poorly understood, leading to subtle bugs and misconfigurations.

**Approaches**
- Infer boundaries from service communication patterns
- Map data ownership across services
- Visualise consistency zones and transitions

**Tech hints**
- OpenTelemetry traces
- Graph modelling (networkx or Neo4j)
- Service mesh data (if available)

**Formats**
- CLI + graph output
- Web UI for exploration
- CI artifact

**Why good fit**
- Deep SRE/system design alignment
- Helps reason about complex architectures

**Why not**
- Requires good instrumentation
- Inference may be incomplete

**Revenue potential**
- Medium → High

**Content potential**
- High

**Community potential**
- Medium

**Tags**
`distributed-systems`, `state`, `consistency`, `observability`

**References**
- https://opentelemetry.io/  
- https://martinfowler.com/articles/microservices.html  

---
