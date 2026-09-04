---
date: 2026-08-15
item_number: 3
title: "The AI Code Problem Isn't Generation. It's Review Queueing Theory."
summary: "One of the anti-LLM Debian proposals makes a particularly interesting argument: Debian is not trying to maximise generated code, and volunteer maintainers can be harmed if automated generation produces more contributions than humans can responsibly review."
angle: Treat a software project as a queueing system.
interests:
  - agentic AI
  - SRE
  - queueing theory
  - open source
  - engineering leadership
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 3. The AI Code Problem Isn't Generation. It's Review Queueing Theory.


One of the anti-LLM Debian proposals makes a particularly interesting argument: Debian is not trying to maximise generated code, and volunteer maintainers can be harmed if automated generation produces more contributions than humans can responsibly review. 

This is a stronger systems argument than “AI code is bad”.

**Angle:** Treat a software project as a queueing system.

Before agents:

`human generation rate ≈ human review capacity`

With cheap generation:

`machine generation rate >> human review capacity`

If reviewers are the constrained resource, making contribution generation 100× cheaper can actually **reduce system throughput** by flooding the queue with superficially plausible work.

That is classic backpressure.

Good agent infrastructure therefore needs the same things as a distributed service:

- admission control,
- quotas,
- prioritisation,
- batching,
- automated validation,
- rejection before expensive processing,
- and producer backpressure.

A GitHub repository accepting agent PRs without rate limits is basically **an API endpoint with an unbounded request queue**.

**Matches:** agentic AI, SRE, queueing theory, open source, engineering leadership.

**Format:** **Long-form article**

**Confidence: 0.99 — possibly the most distinctive idea tonight.**

---
