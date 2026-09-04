---
date: 2026-08-21
item_number: 4
title: A 20-Patch Revert Is Cheaper Than One Clever Emergency Fix
summary: The GPU scheduler revert is also a nice counterexample to the idea that rollback needs to be trivial to be worthwhile. The fair-scheduler work touched the scheduler core and multiple GPU/accelerator drivers, so returning to the previous architecture required a substantial revert series.
angle: "Teams sometimes resist rollback because:"
interests:
  - incident response
  - SRE
  - Git
  - release engineering
format: Short post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 4. A 20-Patch Revert Is Cheaper Than One Clever Emergency Fix


The GPU scheduler revert is also a nice counterexample to the idea that rollback needs to be trivial to be worthwhile. The fair-scheduler work touched the scheduler core and multiple GPU/accelerator drivers, so returning to the previous architecture required a substantial revert series. 

**Angle:** Teams sometimes resist rollback because:

> “It's complicated now.”

That's exactly when preserving the old path pays off.

The cost comparison isn't:

`20-patch revert`

versus:

`nothing`.

It is:

`20 patches restoring extensively exercised behaviour`

versus:

`new code written under release pressure to repair behaviour we don't yet understand`.

Complex rollback can still be the lower-risk operation.

**Matches:** incident response, SRE, Git, release engineering.

**Format:** **Short post**

**Confidence: 0.99.**

---
