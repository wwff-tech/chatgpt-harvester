---
date: 2026-09-02
item_number: 5
title: The Agent Should Ask for Authority, Not Inherit It
summary: "A small open-source project called OpenLeash received wider attention today. It places an authorisation layer between an AI agent and consequential actions: policies can return `ALLOW`, `DENY`, or require human approval, and successful authorisations produce **single-use, action-scoped cryptographic proof tokens**. Policies are YAML, audit records are append-only, and the system can run locally."
angle: "The implementation is early, so I wouldn't write a product endorsement. The architecture is the interesting bit."
interests:
  - agent governance
  - MCP
  - capability security
  - policy-as-code
  - HITL
  - local-first tooling
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 5. The Agent Should Ask for Authority, Not Inherit It


A small open-source project called OpenLeash received wider attention today. It places an authorisation layer between an AI agent and consequential actions: policies can return `ALLOW`, `DENY`, or require human approval, and successful authorisations produce **single-use, action-scoped cryptographic proof tokens**. Policies are YAML, audit records are append-only, and the system can run locally. 

**Angle:** The implementation is early, so I wouldn't write a product endorsement. The architecture is the interesting bit.

Most agents currently behave roughly as:

`user credentials`

→ `agent`

→ `tools`.

So if Mike can:

`delete production database`

then the agent potentially can too.

A better model is:

`user authority`

→ `policy`

→ **temporary action capability**

→ `tool`.

The difference is subtle but important.

Instead of giving the agent:

`permission to delete databases`

give it:

`permission to execute exactly delete(db=test-123), once, before 14:05`.

That moves agent security towards **capability-based authorisation** rather than inherited ambient authority.

And importantly, the authorisation decision sits outside the model.

> **The model proposes. Deterministic policy disposes.**

**Matches:** agent governance, MCP, capability security, policy-as-code, HITL, local-first tooling.

**Format:** **Long-form article**

**Confidence: 0.97 on the architecture; 0.75 on this specific young project becoming important.**

---
