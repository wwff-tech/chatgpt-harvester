---
date: 2026-04-28
item_number: 2
title: The Kernel Decided Your Process Had to Die
summary: Linux memory overcommit can lead to sudden, non-deterministic process termination under pressure.
angle: “Optimistic allocation meets harsh reality” — performance vs predictability trade-offs.
interests:
  - Linux
  - performance engineering
  - SRE
format: Long form
suggested_points:
  - Overcommit modes and heuristics
  - OOM killer decision logic
  - Failure patterns in containerised workloads
  - Tuning vm settings and cgroups
  - Designing for graceful degradation
conversation_id: 69cc692c-db90-8396-bc48-375ba1b6270e
label: tech article ideas
---

## 2) Memory Overcommit and the OOM Killer’s Dark Corners


- **Title:** *The Kernel Decided Your Process Had to Die*  
- **Summary:** Linux memory overcommit can lead to sudden, non-deterministic process termination under pressure.  
- **Angle:** “Optimistic allocation meets harsh reality” — performance vs predictability trade-offs.  
- **Matches Interests:** Linux, performance engineering, SRE  
- **Format:** **Long form**

- **Suggested Points to Cover:**
  - Overcommit modes and heuristics  
  - OOM killer decision logic  
  - Failure patterns in containerised workloads  
  - Tuning vm settings and cgroups  
  - Designing for graceful degradation  

---
