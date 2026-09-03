---
date: 2026-08-29
item_number: 10
title: Left-field — “Least Privilege Is an Inference Problem”
summary: KubeCap suggests a broader security framing.
angle: "We usually phrase least privilege as a moral imperative:"
interests:
  - IAM
  - Kubernetes
  - capability security
  - policy generation
  - security modelling
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 10. Left-field — “Least Privilege Is an Inference Problem”


KubeCap suggests a broader security framing. 

**Angle:** We usually phrase least privilege as a moral imperative:

> Give software only what it needs.

But that hides the difficult question:

> **How do you know what it needs?**

For a non-trivial application, required authority is a function of:

`reachable code`

`configuration`

`input`

`environment`

`error paths`

`dependencies`

`kernel behaviour`

`future workload`.

So least privilege is fundamentally an **inference problem under uncertainty**.

That suggests security tooling should stop merely checking:

`Are capabilities restricted?`

and start answering:

`Observed required authority: X`

`Statically reachable authority: Y`

`Configured authority: Z`

with:

\[
X \subseteq Y \subseteq Z
\]

The interesting security metric then becomes the **authority gap**:

\[
G = Z - Y
\]

Everything in that gap is privilege the application possesses without an identified reason to possess it.

The same model works for IAM, network access, filesystem permissions, Kubernetes RBAC, database grants, and agent tools.

**Matches:** IAM, Kubernetes, capability security, policy generation, security modelling.

**Format:** **Long-form article**

**Confidence: 0.99 — strongest evergreen concept today.**
