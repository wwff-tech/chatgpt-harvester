---
date: 2026-08-21
item_number: 3
title: "**“Revert Is a Feature, Not an Admission of Failure”** — Long-form / short essay"
summary: Linux 7.2 was intended to switch DRM GPU scheduling from FIFO to a new fairness-oriented scheduler. Late real-world testing found serious regressions under sustained GPU load, including severe frame-rate drops and desktop freezes. Rather than trying to rush a correction, maintainers reverted the change with a roughly 20-patch series and left the fair scheduler experimental.
angle: "The technically impressive bit isn't that the original change was correct."
interests:
  - SRE
  - Linux
  - change management
  - release engineering
  - reliability
format: "**Long-form article**, although the central argument also works as a strong short."
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 3. **“Revert Is a Feature, Not an Admission of Failure”** — Long-form / short essay


Linux 7.2 was intended to switch DRM GPU scheduling from FIFO to a new fairness-oriented scheduler. Late real-world testing found serious regressions under sustained GPU load, including severe frame-rate drops and desktop freezes. Rather than trying to rush a correction, maintainers reverted the change with a roughly 20-patch series and left the fair scheduler experimental. 

Fixes were already being developed within days. 

**Angle:** The technically impressive bit isn't that the original change was correct.

**It wasn't.**

The impressive engineering property is that the project retained enough reversibility to say:

`new design → regression discovered → restore known-good design → ship`

instead of:

`new design → regression → emergency patch → patch the patch → release anyway`.

There's a strong SRE argument here:

> **Reversibility is a reliability capability.**

Git, feature flags, immutable deployment artefacts, database migration design, backwards-compatible APIs, canaries, and Kubernetes rollout history all have value partly because they preserve routes backwards.

“Fix forward” is sometimes necessary, but treating it as inherently more sophisticated than rollback is backwards. Under time pressure, **known-good is evidence; hurried fix is hypothesis**.

**Matches:** SRE, Linux, change management, release engineering, reliability.

**Format:** **Long-form article**, although the central argument also works as a strong short.

**Confidence: 0.99.**

---
