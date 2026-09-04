---
date: 2026-05-12
item_number: 3
title: Config Change Lineage Tracker
interests:
suggested_points:
conversation_id: 69e5608e-48c0-83eb-9533-b3a6d9e148c7
label: project ideas
---

# 3. Config Change Lineage Tracker


**Problem**  
Infrastructure changes are tracked individually, but not as part of a causal chain:
- who changed what,  
- why it was changed,  
- what downstream effects occurred.

**Approaches**
- Link config changes to incidents and outcomes  
- Build causal chains of infra evolution  
- Provide impact analysis  

**Tech hints**
- Git integration  
- Change-event correlation  
- Integration with Terraform  
- Time-series + graph DB  

**Formats**
- CLI tool  
- Dashboard  
- CI/CD plugin  

**Why good fit**
- Strong SRE relevance  
- Improves debugging and audits  

**Why not**
- Correlation complexity  
- Requires disciplined workflows  

**Revenue potential**  
High  

**Content potential**  
High  

**Community potential**  
High  

**Tags**  
`infra`, `lineage`, `sre`, `changes`

**References**
- https://developer.hashicorp.com/terraform/docs  
- https://sre.google/sre-book/  

---
