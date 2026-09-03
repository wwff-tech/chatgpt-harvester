---
date: 2026-08-25
item_number: 3
title: A Retry Loop Turned Recovery Traffic Into Incident Traffic
summary: "GitHub's August 17 outage write-up describes a **7 hour 47 minute outage** triggered when a critical component in its Central US infrastructure failed to scale under a new traffic peak. During recovery, errors in some Copilot services triggered a **client-side retry loop that increased traffic**, and GitHub had to mitigate that behaviour before safely restoring service."
angle: The root scaling failure matters, but the retry behaviour is the better article.
interests:
  - SRE
  - distributed systems
  - GitHub
  - APIs
  - reliability engineering
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 3. A Retry Loop Turned Recovery Traffic Into Incident Traffic


GitHub's August 17 outage write-up describes a **7 hour 47 minute outage** triggered when a critical component in its Central US infrastructure failed to scale under a new traffic peak. During recovery, errors in some Copilot services triggered a **client-side retry loop that increased traffic**, and GitHub had to mitigate that behaviour before safely restoring service. 

**Angle:** The root scaling failure matters, but the retry behaviour is the better article.

Retries are normally described as a resilience mechanism:

`request fails → retry → success`.

At fleet scale:

`failure`

→ `millions of clients retry`

→ `recovering service receives more traffic`

→ `service fails harder`

→ `more retries`.

The mechanism intended to survive failure becomes **positive feedback**.

This is why retry design needs:

`exponential backoff`

`jitter`

`bounded attempts`

`retry budgets`

`server Retry-After`

`circuit breaking`

and, critically, **load shedding during recovery**.

There's a useful deeper point: steady-state capacity and **recovery capacity** are different things. A service recovering cold caches, reconnecting dependencies, and rebuilding state may tolerate *less* traffic than before the incident.

> **Design retries for the capacity of the system while wounded, not while healthy.**

**Matches:** SRE, distributed systems, GitHub, APIs, reliability engineering.

**Format:** **Long-form article**

**Confidence: 0.99 — excellent practical SRE piece.**

---
