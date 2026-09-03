---
date: 2026-08-12
item_number: 3
title: We Need an SBOM for Authority
summary: "The LiteLLM case also exposes something conventional SBOMs don't describe well. An SBOM can tell you *which software is present* but not that a component can read four model-provider keys, assume an AWS role, publish to a registry, or trigger 600 deployment pipelines."
angle: "Explore an **Authority Bill of Materials**."
interests:
  - IAM
  - policy-as-code
  - Kubernetes
  - agent security
  - SBOMs
  - platform engineering
format: Long-form
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 3. We Need an SBOM for Authority


The LiteLLM case also exposes something conventional SBOMs don't describe well. An SBOM can tell you *which software is present* but not that a component can read four model-provider keys, assume an AWS role, publish to a registry, or trigger 600 deployment pipelines. 

**Angle:** Explore an **Authority Bill of Materials**.

For each workload:

`identity → credentials → delegated identities → APIs → writable resources → egress → downstream automation`

Imagine asking:

> If this component became malicious right now, what could it cause to happen?

That's subtly different from attack-path analysis. It is a property of the deployed architecture that could potentially be generated alongside an SBOM.

Kubernetes service accounts, IAM role bindings, Vault policies, GitHub OIDC trust policies, network policy, MCP tool declarations, and cloud resource policies already contain much of the raw data.

An ABOM might therefore be something a platform can actually **compile**.

**Matches:** IAM, policy-as-code, Kubernetes, agent security, SBOMs, platform engineering.

**Confidence: 0.95 — less newsy, but potentially the most original article here.**

---
