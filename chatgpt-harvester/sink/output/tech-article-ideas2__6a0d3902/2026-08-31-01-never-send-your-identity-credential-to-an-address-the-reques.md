---
date: 2026-08-31
item_number: 1
title: Never Send Your Identity Credential to an Address the Requester Chooses
summary: "A recently disclosed flaw in Red Hat Ansible Automation Platform's HashiCorp Vault credential plugin, **CVE-2026-12564**, has an unusually clean failure mode. A user able to create and test a Vault credential could supply a malicious Vault URL; the controller would then read its **own Kubernetes service-account token and send it to that endpoint** as part of Kubernetes authentication."
angle: "This isn't really a Vault bug, or even an Ansible bug. It's a confused-deputy problem:"
interests:
  - Kubernetes
  - Ansible
  - Vault
  - workload identity
  - IAM
  - confused-deputy attacks
  - platform security
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 1. Never Send Your Identity Credential to an Address the Requester Chooses


A recently disclosed flaw in Red Hat Ansible Automation Platform's HashiCorp Vault credential plugin, **CVE-2026-12564**, has an unusually clean failure mode. A user able to create and test a Vault credential could supply a malicious Vault URL; the controller would then read its **own Kubernetes service-account token and send it to that endpoint** as part of Kubernetes authentication. 

The stolen identity reportedly has enough authority to read secrets and manipulate pods in control-plane namespaces, turning what looks like a credential-integration bug into Kubernetes privilege escalation. 

**Angle:** This isn't really a Vault bug, or even an Ansible bug. It's a confused-deputy problem:

`low-privilege user chooses destination`

→ `high-privilege service attaches its credential`

→ `request leaves trust boundary`.

The same dangerous pattern appears in:

`webhook testing`

`OIDC callbacks`

`cloud metadata proxies`

`Git repository validation`

`package registries`

`agent tools`.

A useful invariant for platform software is:

> **Untrusted input may select data, or it may select a destination, but allowing it to select a destination to which privileged credentials are automatically attached deserves extreme scrutiny.**

SSRF filtering helps, but the stronger design is usually **credential audience binding**: a credential usable by Vault should not be a general Kubernetes bearer credential worth stealing.

**Matches:** Kubernetes, Ansible, Vault, workload identity, IAM, confused-deputy attacks, platform security.

**Format:** **Long-form article**

**Confidence: 0.97.** I'd verify against Red Hat's primary advisory before publishing exact affected-version details; the technical mechanism is well described in current vulnerability reporting.

---
