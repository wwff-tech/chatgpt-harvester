---
date: 2026-05-12
item_number: 2
title: The Kernel Killed the Wrong Thing
summary: Memory overcommit in Linux can lead to OOM killer decisions that cascade into broader system instability.
angle: “Local optimisation, global failure” — resource pressure causing unpredictable kill patterns.
interests:
  - Linux
  - systems
  - SRE
format: Long form
suggested_points:
  - Overcommit behaviour and heuristics
  - OOM killer scoring
  - Container vs host interactions
  - Observability of memory pressure
  - Mitigation strategies (limits, cgroups v2 tuning)
conversation_id: 69cc692c-db90-8396-bc48-375ba1b6270e
label: tech article ideas
---

## 2) Memory Overcommit and OOM Kill Cascades


- **Title:** *The Kernel Killed the Wrong Thing*  
- **Summary:** Memory overcommit in Linux can lead to OOM killer decisions that cascade into broader system instability.  
- **Angle:** “Local optimisation, global failure” — resource pressure causing unpredictable kill patterns.  
- **Matches Interests:** Linux, systems, SRE  
- **Format:** **Long form**

- **Suggested Points to Cover:**
  - Overcommit behaviour and heuristics  
  - OOM killer scoring  
  - Container vs host interactions  
  - Observability of memory pressure  
  - Mitigation strategies (limits, cgroups v2 tuning)  

---
