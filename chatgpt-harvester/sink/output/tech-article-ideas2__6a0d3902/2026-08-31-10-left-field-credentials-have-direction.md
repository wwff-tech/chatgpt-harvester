---
date: 2026-08-31
item_number: 10
title: Left-field — “Credentials Have Direction”
summary: The Ansible/Vault vulnerability suggests a useful security abstraction.
angle: "We normally model a credential as:"
interests:
  - IAM
  - SPIFFE
  - Kubernetes
  - Vault
  - zero trust
  - network policy
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 10. Left-field — “Credentials Have Direction”


The Ansible/Vault vulnerability suggests a useful security abstraction.

**Angle:** We normally model a credential as:

`principal → credential → resource`.

But credentials also have an implicit **direction of travel**.

A Kubernetes service-account token should flow:

`pod → Kubernetes API`.

If an integration causes it to flow:

`pod → arbitrary Vault URL`

something has gone wrong even before we know whether the destination is malicious.

That suggests attaching flow constraints to credentials:

`audience`

`permitted destinations`

`permitted protocols`

`proof-of-possession`

`network egress policy`.

Then secret management becomes less about:

> Where can this secret be read?

and more about:

> **Where is this identity permitted to travel?**

That ties together audience-bound JWTs, mTLS, SPIFFE, egress policy, metadata-service protections, and capability URLs surprisingly neatly.

**Matches:** IAM, SPIFFE, Kubernetes, Vault, zero trust, network policy.

**Format:** **Long-form article**

**Confidence: 0.99 — strongest evergreen security idea today.**
