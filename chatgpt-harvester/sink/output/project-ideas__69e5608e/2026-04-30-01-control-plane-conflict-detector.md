---
date: 2026-04-30
item_number: 1
title: Control Plane Conflict Detector
interests:
suggested_points:
conversation_id: 69e5608e-48c0-83eb-9533-b3a6d9e148c7
label: project ideas
---

## 1. Control Plane Conflict Detector


**Problem**  
Multiple control mechanisms (autoscalers, CI/CD, manual overrides, agents) act on the same resources, causing oscillations or instability.

**Approaches**
- Detect conflicting actions (e.g., scale up vs scale down loops)  
- Identify overlapping control domains  
- Surface “control contention” hotspots  

**Tech hints**
- Event stream aggregation (Kubernetes events, CI logs)  
- Rule-based conflict detection  
- Time-series correlation  

**Formats**
- CLI diagnostic tool  
- Kubernetes controller/plugin  
- Dashboard visualisation  

**Why good fit**
- Strong SRE alignment  
- Increasingly relevant with automation-heavy systems  

**Why not**
- Requires deep integration into systems  
- Hard to generalise across environments  

**Revenue potential**
- Medium → High  

**Content potential**
- High  

**Community potential**
- Medium  

**Tags**
`control-plane`, `kubernetes`, `sre`, `automation`

**References**
- https://kubernetes.io/docs/concepts/  
- https://martinfowler.com/articles/microservices.html  

---
