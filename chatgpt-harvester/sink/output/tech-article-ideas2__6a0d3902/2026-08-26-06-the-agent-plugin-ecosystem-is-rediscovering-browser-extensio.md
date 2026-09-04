---
date: 2026-08-26
item_number: 6
title: The Agent Plugin Ecosystem Is Rediscovering Browser Extensions, Only With Shell Access
summary: "The same research found both accidental and deliberately malicious credential leakage among third-party agent skills, with **76.3% of leakage requiring joint analysis of code and natural-language instructions** to detect."
angle: "This is the bit I'd worry about more than prompt injection."
interests:
  - agents
  - capability security
  - plugin architecture
  - supply-chain security
  - MCP
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 6. The Agent Plugin Ecosystem Is Rediscovering Browser Extensions, Only With Shell Access


The same research found both accidental and deliberately malicious credential leakage among third-party agent skills, with **76.3% of leakage requiring joint analysis of code and natural-language instructions** to detect. 

**Angle:** This is the bit I'd worry about more than prompt injection.

Agent skills combine:

`third-party code`

`natural-language instructions`

`credentials`

`filesystem`

`network`

`tool execution`.

We've seen this movie before with:

`browser extensions`

`IDE plugins`

`npm packages`

`mobile apps`.

Except an agent extension may inherit considerably more ambient authority.

Static source scanning is also weakened because part of the executable semantics now lives in natural language.

That suggests agent skill marketplaces will eventually need the equivalent of:

`permission manifests`

`capability declarations`

`signing/provenance`

`sandboxing`

`network permissions`

`secret brokering`

`automated behavioural analysis`.

Installing a skill should probably look less like `pip install` and more like granting permissions to an Android application.

**Matches:** agents, capability security, plugin architecture, supply-chain security, MCP.

**Format:** **Long-form article**

**Confidence: 0.99.**

---
