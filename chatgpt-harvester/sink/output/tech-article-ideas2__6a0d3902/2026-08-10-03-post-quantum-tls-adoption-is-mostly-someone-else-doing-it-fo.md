---
date: 2026-08-10
item_number: 3
title: Post-Quantum TLS Adoption Is Mostly Someone Else Doing It For You
summary: "A new UK measurement study published on 3 August scanned **4,665 organisations across ten sectors**. Among reachable services, 44% of HTTPS endpoints supported evaluated post-quantum key exchange, versus only **6.4% of SMTP endpoints**. Only 144 organisations supported PQC across both web and mail."
angle: This is really an abstraction-layer story.
interests:
  - TLS
  - PKI
  - cloud infrastructure
  - security
  - measurement
  - SRE
format: Long-form
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 3. Post-Quantum TLS Adoption Is Mostly Someone Else Doing It For You


A new UK measurement study published on 3 August scanned **4,665 organisations across ten sectors**. Among reachable services, 44% of HTTPS endpoints supported evaluated post-quantum key exchange, versus only **6.4% of SMTP endpoints**. Only 144 organisations supported PQC across both web and mail. 

The surprising result is what predicts adoption: **infrastructure provider identity was substantially more predictive than organisational sector**. A separate global study based on more than two billion TLS handshakes reaches a similar conclusion — much apparent PQ-TLS progress is actually managed providers deploying it underneath their customers. 

**Angle:** This is really an abstraction-layer story.

We often measure a company's “technology adoption” when what we're actually measuring is:

> Cloudflare/Akamai/AWS/Google/etc upgraded something and 300,000 customers inherited it.

That's arguably **exactly how infrastructure progress should work**.

But it also means external scanners can dramatically overestimate an organisation's actual cryptographic readiness. The UK study found no post-quantum certificate signatures at all, despite the much healthier key-exchange numbers. 

**Matches:** TLS, PKI, cloud infrastructure, security, measurement, SRE.

**Confidence: 0.98 — excellent data-driven article.**

---
