---
date: 2026-08-30
item_number: 4
title: Credential Rotation Is an Application Feature, Not Just a Platform Feature
summary: "The Pod Certificate design includes automatic credential rotation, but Kubernetes explicitly notes that **applications must notice and reload the changed credential**, via mechanisms such as `inotify` or polling."
angle: This is one of those details that repeatedly destroys otherwise good secret-management architectures.
interests:
  - Kubernetes
  - Vault
  - PKI
  - application reliability
  - SRE
format: Short post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 4. Credential Rotation Is an Application Feature, Not Just a Platform Feature


The Pod Certificate design includes automatic credential rotation, but Kubernetes explicitly notes that **applications must notice and reload the changed credential**, via mechanisms such as `inotify` or polling. 

**Angle:** This is one of those details that repeatedly destroys otherwise good secret-management architectures.

Platform:

`secret rotates every hour ✓`

Application:

`read certificate at startup`

→ `run for six months`.

Effective credential lifetime:

`six months`.

So rotation requires an end-to-end property:

`issuer rotates`

→ `delivery updates`

→ `application reloads`

→ `old credential expires`

→ `peer accepts new trust state`.

A useful operational test is therefore not:

> Can Vault/Kubernetes/etc. rotate this secret?

but:

> **Can I rotate it underneath a live workload and observe the workload continue without restart or stale authentication?**

**Matches:** Kubernetes, Vault, PKI, application reliability, SRE.

**Format:** **Short post**

**Confidence: 0.99.**

---
