---
date: 2026-04-18
item_number: 1
title: Your TLS Cert Was Revoked—Your System Didn’t Notice
summary: Certificate revocation mechanisms (CRLs, OCSP) are inconsistently enforced, meaning compromised certs may still be trusted in practice.
angle: “Revocation vs reality” — security guarantees that depend on optional checks.
interests:
  - Security
  - networking
  - SRE
format: Long form
suggested_points:
  - How revocation is supposed to work
  - Why clients skip or soft-fail checks
  - OCSP stapling and its limitations
  - Real-world risk scenarios
  - Hardening strategies and trade-offs
conversation_id: 69cc692c-db90-8396-bc48-375ba1b6270e
label: tech article ideas
---

## 1) Certificate Revocation is Still Broken


- **Title:** *Your TLS Cert Was Revoked—Your System Didn’t Notice*  
- **Summary:** Certificate revocation mechanisms (CRLs, OCSP) are inconsistently enforced, meaning compromised certs may still be trusted in practice.  
- **Angle:** “Revocation vs reality” — security guarantees that depend on optional checks.  
- **Matches Interests:** Security, networking, SRE  
- **Format:** **Long form**

- **Suggested Points to Cover:**
  - How revocation is supposed to work  
  - Why clients skip or soft-fail checks  
  - OCSP stapling and its limitations  
  - Real-world risk scenarios  
  - Hardening strategies and trade-offs  

---
