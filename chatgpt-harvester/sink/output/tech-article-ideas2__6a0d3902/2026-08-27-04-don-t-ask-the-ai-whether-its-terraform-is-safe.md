---
date: 2026-08-27
item_number: 4
title: "Don't Ask the AI Whether Its Terraform Is Safe"
summary: The Ansible research gives a crisp companion principle.
angle: "Suppose an agent generates:"
interests:
  - Terraform/Ansible
  - CI/CD
  - policy-as-code
  - agentic engineering
format: Short post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 4. Don't Ask the AI Whether Its Terraform Is Safe


The Ansible research gives a crisp companion principle.

**Angle:** Suppose an agent generates:

```yaml
ansible.builtin.uri:
  url: https://internal.example
  validate_certs: false
```

You can ask another LLM:

> Is this secure?

Or you can write a rule:

`validate_certs == false → reject`.

The second is boring.

That's precisely why it is better.

AI coding systems should progressively turn recurring review comments into **deterministic rejection criteria**:

`human notices class of mistake`

→ `encode policy`

→ `machines reject forever`.

The reviewer then spends attention on genuinely novel judgement rather than rediscovering known invariants.

**Matches:** Terraform/Ansible, CI/CD, policy-as-code, agentic engineering.

**Format:** **Short post**

**Confidence: 0.99.**

---
