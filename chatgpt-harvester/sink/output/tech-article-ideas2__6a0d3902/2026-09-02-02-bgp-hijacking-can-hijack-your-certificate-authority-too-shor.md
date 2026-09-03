---
date: 2026-09-02
item_number: 2
title: "**“BGP Hijacking Can Hijack Your Certificate Authority Too”** — Short companion"
summary: The really lovely technical detail in the Virtualizor incident is how the valid TLS certificate appeared.
angle: "PKI asks:"
interests:
  - networking
  - BGP
  - TLS/PKI
  - security architecture
format: Short post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 2. **“BGP Hijacking Can Hijack Your Certificate Authority Too”** — Short companion


The really lovely technical detail in the Virtualizor incident is how the valid TLS certificate appeared.

The attacker announced `162.55.80.0/24`, which was more specific than Hetzner's surrounding `/16`. Standard longest-prefix routing therefore directed traffic towards the attacker. Let's Encrypt's automated validation followed that same Internet routing state and consequently validated the attacker-controlled endpoint. 

**Angle:** PKI asks:

> Does this party control the domain?

But domain control itself eventually bottoms out in infrastructure:

`DNS`

`routing`

`HTTP validation`

`email`

or another external mechanism.

If an attacker can temporarily manipulate the infrastructure used to establish control, they may obtain a credential that remains **cryptographically impeccable**.

This is a neat example of a recurring security mistake:

> **Cryptography can prove a false premise perfectly.**

The mathematics wasn't broken.

The assertion being signed was.

**Matches:** networking, BGP, TLS/PKI, security architecture.

**Format:** **Short post**

**Confidence: 0.99.**

---
