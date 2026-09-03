---
date: 2026-08-21
item_number: 7
title: "**“A Terabyte of Swap Used to Cost Half a Gigabyte of RAM Just to Exist”** — Short technical post"
summary: "Linux 7.2 completes another phase of the swap-table redesign. Among other changes, it removes static metadata structures so overhead approaches zero when swap space is unused. The reported example is striking: configuring a **1 TB swap device previously consumed roughly 512 MB of static RAM metadata**."
angle: "This is a lovely example of **metadata becoming the scaling limit**."
interests:
  - Linux memory management
  - large-memory systems
  - capacity engineering
  - kernel internals
format: Short technical post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 7. **“A Terabyte of Swap Used to Cost Half a Gigabyte of RAM Just to Exist”** — Short technical post


Linux 7.2 completes another phase of the swap-table redesign. Among other changes, it removes static metadata structures so overhead approaches zero when swap space is unused. The reported example is striking: configuring a **1 TB swap device previously consumed roughly 512 MB of static RAM metadata**. 

**Angle:** This is a lovely example of **metadata becoming the scaling limit**.

Engineers naturally reason about the thing being stored:

`1 TB swap`

but large systems often fail on the structures describing the thing:

`page tables`

`inodes`

`connection tracking`

`Kubernetes objects`

`filesystem metadata`

`metrics cardinality`.

At small scale:

\[
data \gg metadata
\]

At sufficient scale, metadata becomes a first-class capacity-planning problem.

The broader lesson:

> **Whenever you scale something by 1,000×, ask what bookkeeping also scales by 1,000×.**

**Matches:** Linux memory management, large-memory systems, capacity engineering, kernel internals.

**Format:** **Short technical post**

**Confidence: 0.98.**

---
