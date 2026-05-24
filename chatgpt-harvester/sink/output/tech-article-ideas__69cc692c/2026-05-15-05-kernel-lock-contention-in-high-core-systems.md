---
date: 2026-05-15
item_number: 5
title: Your Kernel Doesn’t Scale Linearly
summary: On high-core machines, kernel lock contention can limit scalability, even when user-space code is well parallelised.
angle: “Shared state bottlenecks” — kernel internals constraining throughput.
interests:
  - Linux
  - performance engineering
  - systems
format: Long form
suggested_points:
  - Common contended locks (runqueue, memory, IO)
  - Symptoms in real workloads
  - Profiling techniques
  - Kernel tuning and patching
  - Architectural workarounds
conversation_id: 69cc692c-db90-8396-bc48-375ba1b6270e
label: tech article ideas
---

## 5) Kernel Lock Contention in High-Core Systems


- **Title:** *Your Kernel Doesn’t Scale Linearly*  
- **Summary:** On high-core machines, kernel lock contention can limit scalability, even when user-space code is well parallelised.  
- **Angle:** “Shared state bottlenecks” — kernel internals constraining throughput.  
- **Matches Interests:** Linux, performance engineering, systems  
- **Format:** **Long form**

- **Suggested Points to Cover:**
  - Common contended locks (runqueue, memory, IO)  
  - Symptoms in real workloads  
  - Profiling techniques  
  - Kernel tuning and patching  
  - Architectural workarounds  

---
