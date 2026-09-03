---
date: 2026-08-23
item_number: 4
title: Patch the Image, Not the Server
summary: "Unraid's reasoning includes an interesting operational property: the Fedora/uCore base lets it issue security-only image updates separately from broader Unraid releases."
angle: "Traditional patching mutates a machine:"
interests:
  - immutable infrastructure
  - GitOps
  - Linux
  - SRE
  - fleet patching
format: Short post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 4. Patch the Image, Not the Server


Unraid's reasoning includes an interesting operational property: the Fedora/uCore base lets it issue security-only image updates separately from broader Unraid releases. 

**Angle:** Traditional patching mutates a machine:

`state A + package transactions → hopefully state B`.

Image-based systems instead produce:

`known image A → known image B`.

That gives security patching properties SREs normally have to build themselves:

- reproducibility,
- straightforward rollback,
- fleet convergence,
- easier attestation,
- less configuration drift.

The trade-off is that local snowflake modifications become deliberately inconvenient.

That's not necessarily a defect.

**Matches:** immutable infrastructure, GitOps, Linux, SRE, fleet patching.

**Format:** **Short post**

**Confidence: 0.98.**

---
