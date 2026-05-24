---
date: 2026-05-09
item_number: 5
title: Security Patches That Still Cost You Performance
summary: Mitigations like KPTI continue to impact syscall-heavy workloads, particularly in latency-sensitive systems.
angle: “Security tax persists” — long-tail performance implications of mitigations.
interests:
  - Linux
  - performance engineering
  - security
format: Short post
suggested_points:
  - Why KPTI exists
  - Workloads most affected
  - Measuring impact
  - Mitigation strategies (batching, io_uring)
  - Risk vs performance trade-offs
conversation_id: 69cc692c-db90-8396-bc48-375ba1b6270e
label: tech article ideas
---

## 5) Kernel Page Table Isolation Overheads (KPTI)


- **Title:** *Security Patches That Still Cost You Performance*  
- **Summary:** Mitigations like KPTI continue to impact syscall-heavy workloads, particularly in latency-sensitive systems.  
- **Angle:** “Security tax persists” — long-tail performance implications of mitigations.  
- **Matches Interests:** Linux, performance engineering, security  
- **Format:** **Short post**

- **Suggested Points to Cover:**
  - Why KPTI exists  
  - Workloads most affected  
  - Measuring impact  
  - Mitigation strategies (batching, io_uring)  
  - Risk vs performance trade-offs  

---
