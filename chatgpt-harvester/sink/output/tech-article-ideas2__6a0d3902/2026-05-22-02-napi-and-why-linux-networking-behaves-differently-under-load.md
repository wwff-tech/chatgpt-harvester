---
date: 2026-05-22
item_number: 2
title: Your NIC Stopped Interrupting the CPU on Purpose
summary: "Linux's New API (NAPI) switches between interrupt-driven and polling modes to handle packet bursts efficiently. Many networking behaviours observed in production stem directly from this design."
angle: “Performance through controlled laziness” — understanding the kernel mechanisms behind high-throughput networking.
interests:
  - Linux
  - networking
  - performance engineering
format: Short post
suggested_points:
  - Interrupt storms and historical problems
  - Polling versus interrupts
  - Latency and throughput implications
  - Interaction with modern NICs
  - Observability considerations
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

## 2) NAPI and Why Linux Networking Behaves Differently Under Load


- **Title:** *Your NIC Stopped Interrupting the CPU on Purpose*  
- **Summary:** Linux's New API (NAPI) switches between interrupt-driven and polling modes to handle packet bursts efficiently. Many networking behaviours observed in production stem directly from this design.
- **Angle:** “Performance through controlled laziness” — understanding the kernel mechanisms behind high-throughput networking.
- **Matches Interests:** Linux, networking, performance engineering
- **Format:** **Short post**

- **Suggested Points to Cover:**
  - Interrupt storms and historical problems
  - Polling versus interrupts
  - Latency and throughput implications
  - Interaction with modern NICs
  - Observability considerations

---
