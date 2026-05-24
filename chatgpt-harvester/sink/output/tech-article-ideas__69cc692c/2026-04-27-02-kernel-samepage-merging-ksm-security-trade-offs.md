---
date: 2026-04-27
item_number: 2
title: Memory Deduplication Can Leak Data
summary: KSM improves memory efficiency by merging identical pages, but can expose side channels across processes or tenants.
angle: “Efficiency vs isolation” — optimisation introducing covert channels.
interests:
  - Security
  - Linux
  - low-level systems
format: Long form
suggested_points:
  - How KSM works
  - Side-channel attack vectors
  - Cloud and virtualisation implications
  - When to disable vs enable
  - Alternative memory optimisation strategies
conversation_id: 69cc692c-db90-8396-bc48-375ba1b6270e
label: tech article ideas
---

## 2) Kernel Samepage Merging (KSM) Security Trade-offs


- **Title:** *Memory Deduplication Can Leak Data*  
- **Summary:** KSM improves memory efficiency by merging identical pages, but can expose side channels across processes or tenants.  
- **Angle:** “Efficiency vs isolation” — optimisation introducing covert channels.  
- **Matches Interests:** Security, Linux, low-level systems  
- **Format:** **Long form**

- **Suggested Points to Cover:**
  - How KSM works  
  - Side-channel attack vectors  
  - Cloud and virtualisation implications  
  - When to disable vs enable  
  - Alternative memory optimisation strategies  

---
