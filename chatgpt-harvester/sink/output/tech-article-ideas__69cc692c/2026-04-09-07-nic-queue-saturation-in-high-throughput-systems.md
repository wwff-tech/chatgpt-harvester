---
date: 2026-04-09
item_number: 7
title: Your Network Card is the Bottleneck
summary: High-throughput systems often hit NIC queue limits before CPU or memory, causing packet drops and latency spikes.
angle: “The hidden bottleneck” — performance tuning below the usual layers.
interests:
  - Networking
  - performance engineering
format: Short post
suggested_points:
  - NIC queues, interrupts, and buffering
  - "Symptoms: packet loss, jitter, uneven latency"
  - Tuning parameters (RSS, RPS, queue sizes)
  - Interaction with kernel networking stack
  - Observability and tooling
conversation_id: 69cc692c-db90-8396-bc48-375ba1b6270e
label: tech article ideas
---

## 7) NIC Queue Saturation in High-Throughput Systems


- **Title:** *Your Network Card is the Bottleneck*  
- **Summary:** High-throughput systems often hit NIC queue limits before CPU or memory, causing packet drops and latency spikes.  
- **Angle:** “The hidden bottleneck” — performance tuning below the usual layers.  
- **Matches Interests:** Networking, performance engineering  
- **Format:** **Short post**

- **Suggested Points to Cover:**
  - NIC queues, interrupts, and buffering  
  - Symptoms: packet loss, jitter, uneven latency  
  - Tuning parameters (RSS, RPS, queue sizes)  
  - Interaction with kernel networking stack  
  - Observability and tooling  

---
