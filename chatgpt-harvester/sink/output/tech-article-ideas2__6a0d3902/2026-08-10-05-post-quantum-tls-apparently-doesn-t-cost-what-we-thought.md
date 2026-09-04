---
date: 2026-08-10
item_number: 5
title: "Post-Quantum TLS Apparently Doesn't Cost What We Thought"
summary: "The larger longitudinal PQ-TLS study performed more than **two billion TLS handshakes across one million domains and eleven geographic vantage points**. Contrary to earlier experimental expectations, it found no meaningful Internet-level latency penalty from PQ-TLS, while deployment converged heavily around one hybrid construction."
angle: "This is a useful example of **benchmarking the wrong layer**."
interests:
  - performance engineering
  - TLS
  - latency
  - networking
  - measurement methodology
format: Short post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 5. Post-Quantum TLS Apparently Doesn't Cost What We Thought


The larger longitudinal PQ-TLS study performed more than **two billion TLS handshakes across one million domains and eleven geographic vantage points**. Contrary to earlier experimental expectations, it found no meaningful Internet-level latency penalty from PQ-TLS, while deployment converged heavily around one hybrid construction. 

**Angle:** This is a useful example of **benchmarking the wrong layer**.

A cryptographic operation can have measurable microbenchmark overhead while having effectively irrelevant end-to-end impact once network latency, TCP/TLS setup, CDN topology, and application processing dominate.

Very SRE lesson:

**“A component can get significantly slower without the system getting meaningfully slower.”**

**Matches:** performance engineering, TLS, latency, networking, measurement methodology.

**Confidence: 0.94.**

---
