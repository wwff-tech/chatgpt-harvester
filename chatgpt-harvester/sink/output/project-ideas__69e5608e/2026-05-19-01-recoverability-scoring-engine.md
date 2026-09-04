---
date: 2026-05-19
item_number: 1
title: Recoverability Scoring Engine
interests:
suggested_points:
conversation_id: 69e5608e-48c0-83eb-9533-b3a6d9e148c7
label: project ideas
---

# 1. Recoverability Scoring Engine


**Problem**  
Modern systems measure:
- uptime,
- latency,
- throughput,
- error budgets,

…but not:
- rollback difficulty,
- recovery complexity,
- reversibility.

Teams unknowingly optimise into fragile states.

**Approaches**
- Create recoverability metrics:
  - rollback time,
  - dependency entanglement,
  - blast-radius recovery cost.
- Generate “recoverability scores” for services and infra.

**Tech hints**
- Dependency graph analysis  
- Integration with OpenTelemetry traces  
- Kubernetes resource mapping  
- Incident/postmortem ingestion  
- Change-event correlation  

**Formats**
- CI/CD gate  
- Grafana plugin  
- CLI audit tool  
- Architectural scorecard platform  

**Why good fit**
- Strongly differentiated from standard observability  
- Maps directly to real operational pain  
- Strong SRE consulting applicability  

**Why not**
- Recoverability is partially subjective  
- Hard to model organisational processes  

**Revenue potential**  
High  

**Content potential**  
Very high  

**Community potential**  
High  

**Tags**  
`recoverability`, `sre`, `resilience`, `observability`, `rollback`

**References**
- https://sre.google/sre-book/  
- https://opentelemetry.io/  
- https://landing.google.com/sre/workbook/chapters/cascading-failures/  

---
