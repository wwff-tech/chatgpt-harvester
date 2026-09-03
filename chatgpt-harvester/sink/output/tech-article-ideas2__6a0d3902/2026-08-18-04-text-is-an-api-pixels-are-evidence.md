---
date: 2026-08-18
item_number: 4
title: Text Is an API. Pixels Are Evidence.
summary: The KVM idea exposes a useful systems trade-off. Text is enormously easier to automate, but the original video remains the ground truth from which that text was inferred.
angle: "This crops up everywhere:"
interests:
  - observability
  - automation
  - OCR
  - agent tooling
  - systems design
format: Short post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 4. Text Is an API. Pixels Are Evidence.


The KVM idea exposes a useful systems trade-off. Text is enormously easier to automate, but the original video remains the ground truth from which that text was inferred. 

**Angle:** This crops up everywhere:

`OCR ← screenshot`

`DOM ← rendered page`

`metrics ← system behaviour`

`logs ← execution`

`LLM extraction ← document`.

Derived structured data is useful precisely because it discards information.

So for automation:

> **act on the abstraction, retain the evidence.**

A BIOS automation system might navigate using extracted text but archive the source frame around consequential changes. That's a generally useful pattern for agent tooling too.

**Matches:** observability, automation, OCR, agent tooling, systems design.

**Format:** **Short post**

**Confidence: 0.96.**

---
