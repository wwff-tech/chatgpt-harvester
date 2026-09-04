---
date: 2026-08-23
item_number: 1
title: RBAC Is Not Enough When Two Legal Actions Make One Illegal Outcome
summary: "A new paper, **Bounded Agents**, attacks a subtle weakness in agent security: most authorisation systems evaluate each operation independently. An agent may legitimately have permission to *read confidential data* and legitimately have permission to *send an external message*, while the composition of those actions is exactly the thing you wanted to prohibit."
angle: This is not really an AI-specific problem.
interests:
  - agentic AI
  - IAM
  - policy engines
  - state machines
  - MCP/tool governance
  - zero trust
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 1. RBAC Is Not Enough When Two Legal Actions Make One Illegal Outcome


A new paper, **Bounded Agents**, attacks a subtle weakness in agent security: most authorisation systems evaluate each operation independently. An agent may legitimately have permission to *read confidential data* and legitimately have permission to *send an external message*, while the composition of those actions is exactly the thing you wanted to prohibit. 

Its proposed Agentic Principal Chain carries authorisation state across a session, narrows scope through delegation, tracks budgets, and checks combinations of prior and proposed actions. In its evaluation, exfiltration in compromised-model AgentDojo tests fell from 75–100% to zero, although there was a measurable utility cost. 

**Angle:** This is not really an AI-specific problem.

Ordinary authorisation asks:

`may Alice perform X on Y?`

Stateful automation increasingly requires:

`given everything this principal has already done, may it now perform X on Y?`

That resembles transaction monitoring, information-flow control, Chinese-wall policies, capability systems, and state machines more than conventional RBAC.

A useful example:

`read(prod-secret) = allowed`

`POST(external-api) = allowed`

but:

`read(prod-secret) → POST(external-api) = denied`.

The really interesting principle is **composition closure**: permissions are not necessarily safe under composition.

That applies to CI/CD and infrastructure automation too. `terraform plan`, `read secret`, and `open PR` may each be reasonable agent capabilities while particular sequences are not.

**Matches:** agentic AI, IAM, policy engines, state machines, MCP/tool governance, zero trust.

**Format:** **Long-form article**

**Confidence: 0.99 — strongest conceptual piece today.**

Bounded Agents paper

---
