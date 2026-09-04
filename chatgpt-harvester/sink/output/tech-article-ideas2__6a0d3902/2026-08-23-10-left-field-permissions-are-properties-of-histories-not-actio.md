---
date: 2026-08-23
item_number: 10
title: Left-field — “Permissions Are Properties of Histories, Not Actions”
summary: Bounded Agents exposes a deeper security principle that is useful well beyond agents.
angle: "Conventional access control usually evaluates:"
interests:
  - IAM
  - policy-as-code
  - CI/CD
  - agent security
  - state machines
  - formal methods
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 10. Left-field — “Permissions Are Properties of Histories, Not Actions”


Bounded Agents exposes a deeper security principle that is useful well beyond agents. 

**Angle:** Conventional access control usually evaluates:

\[
Allowed(principal, action, resource)
\]

But many real security requirements are temporal:

> Alice may approve an invoice, but not one she created.

> A process may read secrets or communicate externally, but not both.

> A CI job may build an artefact or sign it, but the same identity should not control both stages.

> An agent may refund an order, but not after changing its delivery address.

The actual function is closer to:

\[
Allowed(history, principal, action, resource)
\]

That's a much richer security model.

We already use fragments of it under names such as separation of duties, transaction monitoring, taint tracking, Chinese-wall policies, and workflow state machines.

Agentic systems may simply be the thing that finally forces general-purpose infrastructure to take **history-sensitive authorisation** seriously.

**Matches:** IAM, policy-as-code, CI/CD, agent security, state machines, formal methods.

**Format:** **Long-form article**

**Confidence: 0.99 — probably the most reusable conceptual idea from today's scan.**
