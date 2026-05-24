---
date: 2026-05-03
item_number: 4
title: Your Bottleneck is Crossing the Kernel Boundary
summary: High syscall rates can dominate latency in low-latency or high-throughput systems.
angle: “The cost of abstraction” — kernel transitions as hidden overhead.
interests:
  - Performance engineering
  - Linux
  - low-level optimisation
format: Short post
suggested_points:
  - What syscalls cost in modern CPUs
  - Workloads most affected
  - Techniques to reduce overhead (batching, io_uring)
  - Observability tools
  - Trade-offs in complexity
conversation_id: 69cc692c-db90-8396-bc48-375ba1b6270e
label: tech article ideas
---

## 4) Syscall Overhead in High-Frequency Workloads


- **Title:** *Your Bottleneck is Crossing the Kernel Boundary*  
- **Summary:** High syscall rates can dominate latency in low-latency or high-throughput systems.  
- **Angle:** “The cost of abstraction” — kernel transitions as hidden overhead.  
- **Matches Interests:** Performance engineering, Linux, low-level optimisation  
- **Format:** **Short post**

- **Suggested Points to Cover:**
  - What syscalls cost in modern CPUs  
  - Workloads most affected  
  - Techniques to reduce overhead (batching, io_uring)  
  - Observability tools  
  - Trade-offs in complexity  

---
