---
date: 2026-08-24
item_number: 7
title: BGP Security Failed Because an Old Security Workaround Ate the New Security Metadata
summary: "Cloudflare's RFC 9234 deployment research found something wonderfully systems-y. BGP Roles and the Only-to-Customer (OTC) attribute are designed to make route-leak prevention partly self-enforcing rather than relying entirely on hand-written operator policy. But Cloudflare found two large Tier-1 networks stripping OTC; the networks confirmed this was the result of **defensive configurations introduced after earlier BGP error-handling incidents**. One, Arelion, changed behaviour after Cloudflare's report; GTT was still stripping OTC when Cloudflare published."
angle: "This is a nearly perfect example of **security controls composing badly across time**."
interests:
  - BGP
  - networking
  - SRE
  - Internet infrastructure
  - security controls
  - operational debt
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 7. BGP Security Failed Because an Old Security Workaround Ate the New Security Metadata


Cloudflare's RFC 9234 deployment research found something wonderfully systems-y. BGP Roles and the Only-to-Customer (OTC) attribute are designed to make route-leak prevention partly self-enforcing rather than relying entirely on hand-written operator policy. But Cloudflare found two large Tier-1 networks stripping OTC; the networks confirmed this was the result of **defensive configurations introduced after earlier BGP error-handling incidents**. One, Arelion, changed behaviour after Cloudflare's report; GTT was still stripping OTC when Cloudflare published. 

**Angle:** This is a nearly perfect example of **security controls composing badly across time**.

Historical incident:

`unexpected BGP attribute → trouble`

therefore:

`strip unfamiliar attributes defensively`.

Later security mechanism:

`transitive OTC attribute → route-leak protection`.

Result:

`old defence → destroys new defence`.

Nobody needed to misconfigure the new mechanism directly.

This is the infrastructure equivalent of an old WAF rule breaking modern authentication.

The broader argument is:

> **Every defensive workaround has a compatibility horizon.**

Controls introduced during an incident should have owners, rationale, and eventual revalidation — otherwise emergency mitigations become permanent undocumented protocol semantics.

**Matches:** BGP, networking, SRE, Internet infrastructure, security controls, operational debt.

**Format:** **Long-form article**

**Confidence: 0.99 — excellent SRE/security piece.**

---
