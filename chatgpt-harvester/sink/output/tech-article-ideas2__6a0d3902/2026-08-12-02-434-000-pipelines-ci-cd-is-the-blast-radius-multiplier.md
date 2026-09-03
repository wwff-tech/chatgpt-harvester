---
date: 2026-08-12
item_number: 2
title: "434,000 Pipelines: CI/CD Is the Blast-Radius Multiplier"
summary: The same LiteLLM reporting is useful from a completely different perspective. Hundreds of thousands of CI/CD pipelines potentially interacting with one compromised component illustrates why build systems are disproportionately valuable targets.
angle: Production is deliberately difficult to change. CI exists specifically to change production.
interests:
  - GitHub Actions
  - GitOps
  - OIDC
  - Kubernetes
  - supply chain
  - platform security
format: Short post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 2. 434,000 Pipelines: CI/CD Is the Blast-Radius Multiplier


The same LiteLLM reporting is useful from a completely different perspective. Hundreds of thousands of CI/CD pipelines potentially interacting with one compromised component illustrates why build systems are disproportionately valuable targets. 

**Angle:** Production is deliberately difficult to change. CI exists specifically to change production.

That means compromising CI gives an attacker something better than root on one machine:

- trusted artefact production,
- cloud identities,
- registry credentials,
- signing opportunities,
- deployment authority,
- secret access,
- and a route into many environments.

The concise thesis:

**“CI/CD isn't adjacent to production. It's the machine authorised to manufacture production.”**

That's why securing runners, Actions, package resolution, OIDC claims, and release credentials deserves a different threat model from ordinary development infrastructure.

**Matches:** GitHub Actions, GitOps, OIDC, Kubernetes, supply chain, platform security.

**Confidence: 0.96.**

---
