---
date: 2026-08-24
item_number: 10
title: Left-field — “The Safest Rewrite May Need to Be Deliberately Incompatible”
summary: The C-to-Rust research raises an awkward problem that software-rewrite discussions usually avoid.
angle: Suppose the old implementation accepts malformed input because of undefined behaviour.
interests:
  - Rust/C
  - security engineering
  - testing
  - protocol compatibility
  - software archaeology
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 10. Left-field — “The Safest Rewrite May Need to Be Deliberately Incompatible”


The C-to-Rust research raises an awkward problem that software-rewrite discussions usually avoid. 

**Angle:** Suppose the old implementation accepts malformed input because of undefined behaviour.

A perfect behavioural translation preserves that behaviour.

A safe translation rejects it.

So:

\[
\text{behavioural equivalence} \neq \text{safety equivalence}
\]

The same problem appears when replacing:

`permissive parser → strict parser`

`old TLS stack → modern TLS`

`legacy auth → modern auth`

`C implementation → memory-safe implementation`.

Compatibility tests may actually punish the new implementation for **correctly deleting unsafe behaviour**.

That means a security rewrite needs three buckets:

`must preserve`

`may change`

`must eliminate`.

If you cannot classify observed behaviour into those categories, “100% compatible” may be exactly the wrong success criterion.

**Matches:** Rust/C, security engineering, testing, protocol compatibility, software archaeology.

**Format:** **Long-form article**

**Confidence: 0.99.**
