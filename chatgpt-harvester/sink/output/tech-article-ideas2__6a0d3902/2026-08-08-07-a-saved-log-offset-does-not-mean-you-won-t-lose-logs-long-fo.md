---
date: 2026-08-08
item_number: 7
title: "“A Saved Log Offset Does Not Mean You Won't Lose Logs” — Long-form or technical short"
summary: "A paper published this week tested recovery guarantees through Docker's Logs API. Its LogDeck implementation achieved exact recovery in all 60 tests, whereas stock Grafana Alloy was exact in 20/60; a key failure mode was rediscovering containers that exited or restarted while the collector was unavailable. The authors' important distinction is between **remembering where you read to** and **being able to reacquire the source afterwards**."
angle: "This is a wonderfully SRE-ish subject: *durable cursor ≠ durable delivery*. Generalise it to queues, CDC, tailing files, Kubernetes logs, and event consumers. Exactly-once discussions often obsess over offsets and deduplication while ignoring lifecycle identity."
interests:
  - observability
  - distributed systems
  - Docker
  - logging
  - reliability engineering
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

## 7. “A Saved Log Offset Does Not Mean You Won't Lose Logs” — Long-form or technical short


A paper published this week tested recovery guarantees through Docker's Logs API. Its LogDeck implementation achieved exact recovery in all 60 tests, whereas stock Grafana Alloy was exact in 20/60; a key failure mode was rediscovering containers that exited or restarted while the collector was unavailable. The authors' important distinction is between **remembering where you read to** and **being able to reacquire the source afterwards**. 

**Angle:** This is a wonderfully SRE-ish subject: *durable cursor ≠ durable delivery*. Generalise it to queues, CDC, tailing files, Kubernetes logs, and event consumers. Exactly-once discussions often obsess over offsets and deduplication while ignoring lifecycle identity.

**Matches:** observability, distributed systems, Docker, logging, reliability engineering.

**Confidence: 0.88 — niche, but very much your sort of niche.**

---
