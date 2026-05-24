---
date: 2026-05-16
item_number: 7
title: Your Disk Isn’t Slow—Your Metadata Is
summary: Workloads with high metadata operations (e.g. many small files) can bottleneck on filesystem metadata performance rather than raw IO.
angle: “IO isn’t just throughput” — metadata as a limiting factor.
interests:
  - Storage
  - Linux
  - performance engineering
format: Short post
suggested_points:
  - Metadata operations explained
  - Workload patterns that trigger issues
  - Filesystem differences (ext4, XFS, etc.)
  - Observability tools
  - Mitigation approaches
conversation_id: 69cc692c-db90-8396-bc48-375ba1b6270e
label: tech article ideas
---

## 7) Filesystem Metadata Bottlenecks


- **Title:** *Your Disk Isn’t Slow—Your Metadata Is*  
- **Summary:** Workloads with high metadata operations (e.g. many small files) can bottleneck on filesystem metadata performance rather than raw IO.  
- **Angle:** “IO isn’t just throughput” — metadata as a limiting factor.  
- **Matches Interests:** Storage, Linux, performance engineering  
- **Format:** **Short post**

- **Suggested Points to Cover:**
  - Metadata operations explained  
  - Workload patterns that trigger issues  
  - Filesystem differences (ext4, XFS, etc.)  
  - Observability tools  
  - Mitigation approaches  

---
