---
date: 2026-08-25
item_number: 1
title: AI Has Made Code Cheap. Maintainer Attention Is Still Expensive.
summary: "The QEMU project was hit today by a single reporter filing **more than 125 bug reports in under ten minutes**, largely raw UBSan/assertion output without meaningful analysis or proposed fixes. Red Hat virtualisation engineer Daniel Berrangé described the effect as essentially a denial-of-service attack on maintainers."
angle: "Don't make this another “AI slop is bad” article. The systems problem is much more interesting:"
interests:
  - open source
  - Linux/QEMU
  - agentic engineering
  - software assurance
  - SRE
  - review queues
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 1. AI Has Made Code Cheap. Maintainer Attention Is Still Expensive.


The QEMU project was hit today by a single reporter filing **more than 125 bug reports in under ten minutes**, largely raw UBSan/assertion output without meaningful analysis or proposed fixes. Red Hat virtualisation engineer Daniel Berrangé described the effect as essentially a denial-of-service attack on maintainers. 

**Angle:** Don't make this another “AI slop is bad” article. The systems problem is much more interesting:

`generation cost → ~0`

while:

`verification + triage cost → human time`.

Open-source contribution systems were designed around an implicit economic assumption: **submitting something useful enough to look plausible cost the submitter non-trivial effort**.

LLMs destroy that assumption.

Rate limits help, but I'd go further. Future contribution systems may need **proof-of-work in the semantic sense**, not cryptocurrency:

`bug report`

→ `minimal reproducer`

→ `tested affected version`

→ `deduplication search`

→ `bisect if feasible`

→ `machine-verifiable artefact`

before scarce maintainer attention is consumed.

The key principle:

> **When production becomes cheaper than verification, admission control must move towards the verifier.**

This applies equally to PRs, vulnerability reports, generated tests, support tickets, and agent-generated infrastructure changes.

**Matches:** open source, Linux/QEMU, agentic engineering, software assurance, SRE, review queues.

**Format:** **Long-form article**

**Confidence: 0.99 — strongest piece today.**

---
