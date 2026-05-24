---
date: 2026-04-29
item_number: 1
title: “Feedback Loop Integrity Checker” (Are You Measuring the Right Thing?)
interests:
suggested_points:
conversation_id: 69e5608e-48c0-83eb-9533-b3a6d9e148c7
label: project ideas
---

## 1. “Feedback Loop Integrity Checker” (Are You Measuring the Right Thing?)


**Problem**  
Systems optimise for metrics that drift away from real goals (e.g., latency vs user experience, agent success vs correctness).

**Approaches**
- Map metrics → decisions → outcomes  
- Detect divergence between proxy metrics and real-world impact  
- Flag “optimising the wrong thing” scenarios  

**Tech hints**
- Metric correlation analysis (Pearson/Spearman + lag analysis)  
- Causal inference approximations  
- Time-series pipelines (e.g., Prometheus + Python analysis layer)  

**Formats**
- CLI analysis tool  
- Dashboard plugin  
- Periodic audit report  

**Why good fit**
- Strong SRE + AI alignment  
- Directly addresses Goodhart’s Law in practice  

**Why not**
- Requires well-defined “ground truth”  
- Causality is hard to prove  

**Revenue potential**
- Medium → High  

**Content potential**
- Very high  

**Community potential**
- High  

**Tags**
`feedback-loops`, `metrics`, `sre`, `ai`

**References**
- https://en.wikipedia.org/wiki/Goodhart%27s_law  
- https://prometheus.io/  

---
