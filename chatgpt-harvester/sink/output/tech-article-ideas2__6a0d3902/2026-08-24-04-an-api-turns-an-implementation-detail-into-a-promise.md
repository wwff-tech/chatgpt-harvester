---
date: 2026-08-24
item_number: 4
title: An API Turns an Implementation Detail Into a Promise
summary: "AF_ALG gives a compact version of yesterday's “technical debt is a promise” idea."
angle: Internal functionality is relatively cheap to change.
interests:
  - APIs
  - Linux
  - platform architecture
  - security
  - technical debt
format: Short post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 4. An API Turns an Implementation Detail Into a Promise


AF_ALG gives a compact version of yesterday's “technical debt is a promise” idea. 

**Angle:** Internal functionality is relatively cheap to change.

Expose it through an API and suddenly:

`implementation`

becomes:

`consumer dependency`

becomes:

`compatibility obligation`

becomes:

`security boundary`.

So the cost of adding an API is not just the code required to expose something.

It is the **future set of things you are no longer free to change**.

The best interface may therefore be the smallest one that expresses actual consumer requirements rather than everything the implementation happens to be capable of doing.

**Matches:** APIs, Linux, platform architecture, security, technical debt.

**Format:** **Short post**

**Confidence: 0.99.**

---
