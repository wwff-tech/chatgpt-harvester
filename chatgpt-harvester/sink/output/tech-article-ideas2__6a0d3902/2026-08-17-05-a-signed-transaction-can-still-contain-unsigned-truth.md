---
date: 2026-08-17
item_number: 5
title: A Signed Transaction Can Still Contain Unsigned Truth
summary: "Researchers at University of Massachusetts Amherst disclosed a lovely protocol failure today involving expired contactless cards. Their relay attack can modify the expiry date presented to a payment terminal; the critical detail is that the expiration date used by the terminal **isn't cryptographically protected**. An arbitrary future date can therefore make an expired card appear current, even after the customer has received a replacement."
angle: "Don't make this primarily a payment-card article."
interests:
  - cryptography
  - protocol design
  - WebAuthn-adjacent security
  - threat modelling
format: Long-form
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 5. A Signed Transaction Can Still Contain Unsigned Truth


Researchers at University of Massachusetts Amherst disclosed a lovely protocol failure today involving expired contactless cards. Their relay attack can modify the expiry date presented to a payment terminal; the critical detail is that the expiration date used by the terminal **isn't cryptographically protected**. An arbitrary future date can therefore make an expired card appear current, even after the customer has received a replacement. 

**Angle:** Don't make this primarily a payment-card article.

It's an excellent example of **partial authentication**.

A protocol can contain strong cryptography while still making a security decision using one field outside the authenticated envelope.

Conceptually:

`MAC(signature, A + B + C)`

followed by:

`authorise(A, B, C, D)`

means **D controls security without being authenticated**.

That pattern occurs everywhere: JWT claims handled outside validation, HTTP headers inserted by proxies, unsigned package metadata, webhook routing data, certificate metadata, and hardware bus sideband signals.

The useful review question is:

> **List every input to the authorisation decision. Which of them is actually authenticated?**

**Matches:** cryptography, protocol design, WebAuthn-adjacent security, threat modelling.

**Confidence: 0.99 — excellent teaching article.**

---
