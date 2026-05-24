---
date: 2026-04-28
item_number: 1
title: “Context Drift Auditor” (When Your Inputs Rot)
interests:
suggested_points:
conversation_id: 69e5608e-48c0-83eb-9533-b3a6d9e148c7
label: project ideas
---

## 1. “Context Drift Auditor” (When Your Inputs Rot)


**Problem**  
Systems (LLMs, pipelines, dashboards) rely on context that becomes stale or misaligned, but continues to be trusted.

**Approaches**
- Track provenance + timestamp of context inputs  
- Detect divergence from source-of-truth  
- Alert on “context staleness risk”  

**Tech hints**
- Metadata tagging (timestamp, source, confidence)  
- Hash comparison / checksum validation  
- Scheduled revalidation jobs  
- Optional lightweight graph of dependencies  

**Formats**
- CLI audit tool  
- Background service  
- CI validation step  

**Why good fit**
- Strong alignment with your interest in provenance and drift  
- High leverage across AI + traditional systems  

**Why not**
- Requires discipline in context tagging  
- Partial visibility limits effectiveness  

**Revenue potential**
- Medium → High  

**Content potential**
- Very high  

**Community potential**
- High  

**Tags**
`context`, `drift`, `provenance`, `integrity`

**References**
- https://slsa.dev/  
- https://w3.org/TR/prov-overview/  

---
