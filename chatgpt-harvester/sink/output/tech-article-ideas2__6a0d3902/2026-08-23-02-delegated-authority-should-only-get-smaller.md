---
date: 2026-08-23
item_number: 2
title: Delegated Authority Should Only Get Smaller
summary: "The same paper formalises a property it calls **Blast Radius Monotonicity**: as authority moves down a delegation chain, the reachable blast radius should never increase."
angle: "That's a wonderfully useful invariant independent of LLMs:"
interests:
  - IAM
  - OIDC
  - Kubernetes operators
  - agents
  - CI/CD
  - capability security
format: Short post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 2. Delegated Authority Should Only Get Smaller


The same paper formalises a property it calls **Blast Radius Monotonicity**: as authority moves down a delegation chain, the reachable blast radius should never increase. 

**Angle:** That's a wonderfully useful invariant independent of LLMs:

`human`

→ `orchestrator`

→ `specialist agent`

→ `tool`

should mean:

\[
Authority_{n+1} \subseteq Authority_n
\]

Yet real automation frequently does the opposite.

A GitHub workflow invokes Terraform using an AWS role more privileged than the person who started it. An agent calls an MCP server whose service account can access more resources than the agent itself. A Kubernetes workload talks to a privileged operator.

Delegation has accidentally become **privilege amplification**.

There is a strong short post in simply asking of every delegation boundary:

> **Can the callee cause something the caller could not?**

Sometimes that is deliberately necessary, but it should be conspicuous.

**Matches:** IAM, OIDC, Kubernetes operators, agents, CI/CD, capability security.

**Format:** **Short post**

**Confidence: 0.99.**

---
