---
date: 2026-08-09
item_number: 1
title: "Signed Provenance Can Prove You Faithfully Built the Attacker's Code"
summary: "The current npm supply-chain campaign around `keyv`/`cacheable` is a much more interesting story than “npm got compromised again”. The wider campaign has affected hundreds of packages, with some reporting putting the poisoned dependency footprint above 1,300 releases/packages and roughly two billion monthly downloads."
angle: "*Provenance is evidence, not innocence.* Explore SLSA, OIDC trusted publishing, signatures, reproducible builds, maintainer compromise, dependency cooldowns, and why none individually establishes intent. A useful analogy is TLS: a valid certificate proves which endpoint you reached, not that the endpoint isn't malicious."
interests:
  - CI/CD
  - GitHub Actions
  - OIDC
  - supply-chain security
  - platform engineering
  - agentic infrastructure
format: Long-form
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 1. Signed Provenance Can Prove You Faithfully Built the Attacker's Code


The current npm supply-chain campaign around `keyv`/`cacheable` is a much more interesting story than “npm got compromised again”. The wider campaign has affected hundreds of packages, with some reporting putting the poisoned dependency footprint above 1,300 releases/packages and roughly two billion monthly downloads. 

The nastier architectural point is that compromised maintainers and CI pipelines can produce malware through the **legitimate publishing machinery**. Provenance can therefore correctly tell you *where an artefact came from* without telling you whether you should trust what produced it.

**Angle:** *Provenance is evidence, not innocence.* Explore SLSA, OIDC trusted publishing, signatures, reproducible builds, maintainer compromise, dependency cooldowns, and why none individually establishes intent. A useful analogy is TLS: a valid certificate proves which endpoint you reached, not that the endpoint isn't malicious.

**Matches:** CI/CD, GitHub Actions, OIDC, supply-chain security, platform engineering, agentic infrastructure.

**Confidence: 0.97 — strongest pick today.**

---
