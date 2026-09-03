---
date: 2026-08-27
item_number: 3
title: "Infrastructure-as-Code Has a New Threat Model: Plausibly Wrong at Machine Speed"
summary: "New research surfaced today examining **security smells in AI-generated Ansible code**. The work evaluates generated IaC for insecure patterns and investigates ways of preventing them before the generated automation reaches real infrastructure."
angle: This is more interesting than asking whether an LLM writes insecure YAML.
interests:
  - Ansible
  - agentic coding
  - infrastructure-as-code
  - policy gating
  - SRE
  - security
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 3. Infrastructure-as-Code Has a New Threat Model: Plausibly Wrong at Machine Speed


New research surfaced today examining **security smells in AI-generated Ansible code**. The work evaluates generated IaC for insecure patterns and investigates ways of preventing them before the generated automation reaches real infrastructure. 

I would verify the underlying paper in detail before quoting its numerical results; today's available indexing is enough to establish the research topic, but not enough for me to treat reported figures as publication-grade evidence.

**Angle:** This is more interesting than asking whether an LLM writes insecure YAML.

IaC has an unusual property:

`ordinary bad code → application bug`

while:

`bad IaC → infrastructure policy`.

A model hallucinating:

`0.0.0.0/0`

`mode: "0777"`

`validate_certs: false`

`become: true`

`latest`

`curl | sh`

can turn a textual mistake directly into deployed authority.

The answer isn't necessarily a better model.

IaC is unusually well suited to **deterministic post-generation verification**:

`agent → Ansible`

→ `schema`

→ `ansible-lint`

→ `Semgrep/Checkov`

→ `policy-as-code`

→ `diff`

→ `approval/deployment`.

This is exactly the verification-asymmetry sweet spot from last week's discussion: generating infrastructure configuration can be difficult, while proving many important safety properties is comparatively cheap.

**Matches:** Ansible, agentic coding, infrastructure-as-code, policy gating, SRE, security.

**Format:** **Long-form article**

**Confidence: 0.91 on the current research hook; 0.99 on the architectural argument.**

---
