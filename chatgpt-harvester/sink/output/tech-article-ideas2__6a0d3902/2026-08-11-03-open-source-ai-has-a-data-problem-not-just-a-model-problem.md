---
date: 2026-08-11
item_number: 3
title: Open Source AI Has a Data Problem, Not Just a Model Problem
summary: "Open-source models are only partially reproducible when their training corpus is unavailable, legally ambiguous, or impossible to reconstruct. We've spent decades developing infrastructure for reproducible **software** builds but very little equivalent machinery for reproducible **dataset** builds."
angle: "This is the AI story I'd actually pay attention to today."
interests:
  - open source
  - AI infrastructure
  - reproducibility
  - provenance
  - supply-chain thinking
format: Long-form
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 3. Open Source AI Has a Data Problem, Not Just a Model Problem


**OpenWALDO** launched today, 11 August, led by Gregory Kurtzer. The project is proposing a community-governed corpus of openly licensed web data for AI training, with provenance, licensing metadata, filtering, versioning, and reproducible dataset snapshots treated as infrastructure rather than an opaque preprocessing step. 

**Angle:** This is the AI story I'd actually pay attention to today.

Open-source models are only partially reproducible when their training corpus is unavailable, legally ambiguous, or impossible to reconstruct. We've spent decades developing infrastructure for reproducible **software** builds but very little equivalent machinery for reproducible **dataset** builds.

Think:

`Git → source provenance`

`SBOM → dependency provenance`

`OCI → artefact distribution`

`OpenWALDO-like corpus → training-data provenance`

That leads naturally to the provocative question:

**Can a model meaningfully be called open source if nobody except its creator can reproduce the input artefact from which it was built?**

There are legitimate copyright, privacy, deletion, and data-sovereignty complications here too; immutable dataset provenance and the right to remove data are not automatically compatible.

**Matches:** open source, AI infrastructure, reproducibility, provenance, supply-chain thinking.

**Confidence: 0.95.**

---
