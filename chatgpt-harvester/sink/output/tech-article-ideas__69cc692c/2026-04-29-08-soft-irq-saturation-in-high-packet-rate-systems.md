---
date: 2026-04-29
item_number: 8
title: Your CPU Isn’t Busy—Your Interrupts Are
summary: High packet rates can overwhelm soft IRQ processing, causing latency spikes and packet drops.
angle: “Invisible CPU work” — kernel-level processing dominates performance.
interests:
  - Networking
  - Linux
  - performance tuning
format: Short post
suggested_points:
  - How soft IRQs work
  - Symptoms of saturation
  - Observability tools (/proc/softirqs, perf)
  - Tuning (RPS/XPS, IRQ affinity)
  - Hardware vs software balancing
conversation_id: 69cc692c-db90-8396-bc48-375ba1b6270e
label: tech article ideas
---

## 8) Soft IRQ Saturation in High Packet Rate Systems


- **Title:** *Your CPU Isn’t Busy—Your Interrupts Are*  
- **Summary:** High packet rates can overwhelm soft IRQ processing, causing latency spikes and packet drops.  
- **Angle:** “Invisible CPU work” — kernel-level processing dominates performance.  
- **Matches Interests:** Networking, Linux, performance tuning  
- **Format:** **Short post**

- **Suggested Points to Cover:**
  - How soft IRQs work  
  - Symptoms of saturation  
  - Observability tools (/proc/softirqs, perf)  
  - Tuning (RPS/XPS, IRQ affinity)  
  - Hardware vs software balancing  

---
