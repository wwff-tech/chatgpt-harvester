---
date: 2026-08-31
item_number: 2
title: "**“Bearer Tokens Turn SSRF Into Identity Theft”** — Short companion"
summary: The Ansible flaw is also a nice demonstration of why proof-of-possession credentials matter.
angle: "With a bearer token:"
interests:
  - Kubernetes
  - SPIFFE
  - PKI
  - Vault
  - workload identity
format: Short post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 2. **“Bearer Tokens Turn SSRF Into Identity Theft”** — Short companion


The Ansible flaw is also a nice demonstration of why proof-of-possession credentials matter.

**Angle:** With a bearer token:

`service sends token to attacker`

→ `attacker possesses token`

→ `attacker is service`.

There is no further distinction.

Contrast that with a credential whose use requires a private key that never leaves the workload:

`certificate leaks`

→ `attacker lacks private key`

→ `credential alone is insufficient`.

This dovetails nicely with yesterday's Kubernetes Pod Certificates story. Credential design can make the difference between:

`SSRF`

and:

`SSRF + complete identity transfer`.

**Matches:** Kubernetes, SPIFFE, PKI, Vault, workload identity.

**Format:** **Short post**

**Confidence: 0.99 on the principle.**

---
