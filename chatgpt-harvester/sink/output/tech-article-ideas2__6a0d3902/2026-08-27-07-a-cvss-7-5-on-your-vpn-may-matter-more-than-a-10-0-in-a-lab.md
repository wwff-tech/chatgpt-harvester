---
date: 2026-08-27
item_number: 7
title: "**“A CVSS 7.5 on Your VPN May Matter More Than a 10.0 in a Lab”** — Long-form / security short"
summary: "CISA's current Known Exploited Vulnerabilities additions include six actively exploited flaws across Citrix NetScaler, Microsoft SQL Server, Linux, Red Hat, and AjaxPro. Particularly notable is **CVE-2026-8452 in NetScaler ADC/Gateway**: originally described as a memory-overflow/denial-of-service issue, it is now confirmed exploited, and US federal agencies have been given until **29 August** to remediate it."
angle: "Vulnerability severity scores answer:"
interests:
  - vulnerability management
  - SRE
  - Internet edge
  - security operations
  - patch prioritisation
format: "**Long-form article** or concise security post."
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 7. **“A CVSS 7.5 on Your VPN May Matter More Than a 10.0 in a Lab”** — Long-form / security short


CISA's current Known Exploited Vulnerabilities additions include six actively exploited flaws across Citrix NetScaler, Microsoft SQL Server, Linux, Red Hat, and AjaxPro. Particularly notable is **CVE-2026-8452 in NetScaler ADC/Gateway**: originally described as a memory-overflow/denial-of-service issue, it is now confirmed exploited, and US federal agencies have been given until **29 August** to remediate it. 

**Angle:** Vulnerability severity scores answer:

> How bad *could* this vulnerability be?

Operators need:

> **How urgently should *this particular instance* be fixed?**

Those are different functions.

A useful operational model is closer to:

\[
Urgency =
ExploitEvidence
\times Exposure
\times Authority
\times AssetCriticality
\times RemediationConfidence
\]

A middling-severity vulnerability on an Internet-facing VPN concentrator with active exploitation can easily outrank a nominal CVSS 10 flaw in an isolated service.

CISA KEV is useful because it injects one extremely valuable binary signal:

`attackers are actually using this`.

**Matches:** vulnerability management, SRE, Internet edge, security operations, patch prioritisation.

**Format:** **Long-form article** or concise security post.

**Confidence: 0.99.**

---
