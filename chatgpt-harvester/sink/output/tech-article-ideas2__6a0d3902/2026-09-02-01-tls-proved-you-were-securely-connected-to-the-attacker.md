---
date: 2026-09-02
item_number: 1
title: TLS Proved You Were Securely Connected to the Attacker
summary: "Between **28 and 30 August**, attackers hijacked a more-specific route covering infrastructure used by Virtualizor. Because certificate-authority validation traffic followed the same poisoned route, the attacker obtained a **technically valid Let's Encrypt certificate** for the victim domains. The hijacked update endpoint then served a malicious Virtualizor package to a small number of hypervisor hosts."
angle: This is an unusually good demonstration of why TLS and software signing solve different problems.
interests:
  - BGP
  - PKI
  - supply-chain security
  - Linux hosting
  - software signing
  - CI/CD
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 1. TLS Proved You Were Securely Connected to the Attacker


Between **28 and 30 August**, attackers hijacked a more-specific route covering infrastructure used by Virtualizor. Because certificate-authority validation traffic followed the same poisoned route, the attacker obtained a **technically valid Let's Encrypt certificate** for the victim domains. The hijacked update endpoint then served a malicious Virtualizor package to a small number of hypervisor hosts. 

Worse, Virtualizor's updater did **not cryptographically verify the update package itself**. The vendor is now adding package signing. 

Virtualizor's incident report

**Angle:** This is an unusually good demonstration of why TLS and software signing solve different problems.

TLS established:

`connection → holder of certificate for update.example`.

But the routing system had temporarily changed **who could demonstrate control of that name**.

What the updater actually needed was:

`package → signed by release authority`.

Those trust chains should ideally terminate independently:

```text
Network path ─→ DNS/IP ─→ TLS PKI
                          │
                          ✕
                          │
Software ─→ digest ─→ release signing key
```

If compromising routing can both redirect the request **and satisfy the mechanism used to authenticate the response**, you have correlated trust.

The broader principle is excellent:

> **Transport authenticity should not be the sole source of artefact authenticity.**

This applies to OS packages, container images, firmware, agent skills, Terraform providers, browser extensions, and GitHub release binaries.

**Matches:** BGP, PKI, supply-chain security, Linux hosting, software signing, CI/CD.

**Format:** **Long-form article**

**Confidence: 0.99 — strongest article today.**

---
