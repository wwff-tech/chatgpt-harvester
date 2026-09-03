---
date: 2026-08-01
item_number: 8
title: "Mandatory Access Control Isn't Immune to Concurrency Bugs"
summary: "An Ubuntu-tracked AppArmor issue involving sleeping while holding a spinlock can allow an unprivileged user to trigger kernel deadlock or panic. It's a reminder that security modules are still kernel code, with all the usual concurrency pitfalls."
angle: "Discuss operational resilience, not just exploitability: availability failures matter too."
interests:
  - Linux
  - Kernel engineering
  - SRE
format: Short post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

## 8) AppArmor Bugs Still Matter Operationally


**Suggested title:** *Mandatory Access Control Isn't Immune to Concurrency Bugs*

**Summary:**  
An Ubuntu-tracked AppArmor issue involving sleeping while holding a spinlock can allow an unprivileged user to trigger kernel deadlock or panic. It's a reminder that security modules are still kernel code, with all the usual concurrency pitfalls. 

**Angle**

Discuss operational resilience, not just exploitability: availability failures matter too.

**Matches your interests**

- Linux
- Kernel engineering
- SRE

**Format**

**Short post**

---
