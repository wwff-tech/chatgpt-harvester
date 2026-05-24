---
date: 2026-05-11
item_number: 1
title: “System Intent Validator” (Are We Still Doing the Right Thing?)
interests:
suggested_points:
conversation_id: 69e5608e-48c0-83eb-9533-b3a6d9e148c7
label: project ideas
---

# 1. “System Intent Validator” (Are We Still Doing the Right Thing?)


**Problem**  
Systems drift from original intent while still passing local checks (tests, SLOs, policies).

**Approaches**
- Define high-level system intent (goals, invariants)  
- Continuously validate behaviour against intent  
- Detect divergence early  

**Tech hints**
- Intent-as-code (high-level invariants)  
- Policy engines like entity["software","Open Policy Agent","policy engine"]  
- Graph-based system modelling  
- Periodic validation jobs  

**Formats**
- CI/CD validation layer  
- Observability plugin  
- Governance dashboard  

**Why good fit**
- Strong alignment with platform engineering + AI systems  
- Addresses subtle failure modes  

**Why not**
- Hard to formalise intent  
- Risk of oversimplification  

**Revenue potential**  
High  

**Content potential**  
Very high  

**Community potential**  
Medium → High  

**Tags**  
`intent`, `validation`, `systems`, `governance`

**References**
- https://www.openpolicyagent.org/  
- https://martinfowler.com/architecture/  

---
