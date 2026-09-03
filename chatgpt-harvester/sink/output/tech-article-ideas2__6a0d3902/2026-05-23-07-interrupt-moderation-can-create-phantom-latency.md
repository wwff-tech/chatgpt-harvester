---
date: 2026-05-23
item_number: 7
title: Your Network Was Fast but Your Packets Waited Anyway
summary: Modern NICs intentionally delay interrupts to improve throughput, sometimes creating latency spikes that are difficult to trace back to hardware settings.
angle: “Optimising averages can hurt outliers” — hardware tuning affecting user experience.
interests:
  - Linux
  - networking
  - performance engineering
format: Short post
suggested_points:
  - Interrupt moderation basics
  - Throughput versus latency trade-offs
  - Datacentre workload considerations
  - Observability blind spots
  - Tuning recommendations
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

## 7) Interrupt Moderation Can Create Phantom Latency


- **Title:** *Your Network Was Fast but Your Packets Waited Anyway*  
- **Summary:** Modern NICs intentionally delay interrupts to improve throughput, sometimes creating latency spikes that are difficult to trace back to hardware settings.
- **Angle:** “Optimising averages can hurt outliers” — hardware tuning affecting user experience.
- **Matches Interests:** Linux, networking, performance engineering
- **Format:** **Short post**

- **Suggested Points to Cover:**
  - Interrupt moderation basics
  - Throughput versus latency trade-offs
  - Datacentre workload considerations
  - Observability blind spots
  - Tuning recommendations

---
