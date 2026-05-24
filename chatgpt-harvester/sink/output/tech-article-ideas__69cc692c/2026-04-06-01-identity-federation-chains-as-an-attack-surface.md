---
date: 2026-04-06
item_number: 1
title: "SSO All the Way Down: When Trust Chains Become Attack Chains"
summary: Complex identity federation (OIDC/SAML across SaaS and cloud) creates transitive trust paths where a single weak link can compromise multiple systems.
angle: Map identity flows as graphs, not pairs — highlight how indirect trust relationships expand blast radius.
interests:
  - IAM
  - cloud security
  - system modelling
format: Long form
suggested_points:
  - Visualising identity as a graph (users → IdP → SaaS → cloud roles)
  - "Real-world failure mode: compromised SaaS → cloud access"
  - Token propagation and scope creep across systems
  - "Auditing challenges: who *actually* has access?"
  - "Mitigations: trust boundaries, scoped tokens, federation minimisation"
conversation_id: 69cc692c-db90-8396-bc48-375ba1b6270e
label: tech article ideas
---

## 1) Identity Federation Chains as an Attack Surface


- **Title:** *SSO All the Way Down: When Trust Chains Become Attack Chains*  
- **Summary:** Complex identity federation (OIDC/SAML across SaaS and cloud) creates transitive trust paths where a single weak link can compromise multiple systems.  
- **Angle:** Map identity flows as graphs, not pairs — highlight how indirect trust relationships expand blast radius.  
- **Matches Interests:** IAM, cloud security, system modelling  
- **Format:** **Long form**  

- **Suggested Points to Cover:**
  - Visualising identity as a graph (users → IdP → SaaS → cloud roles)  
  - Real-world failure mode: compromised SaaS → cloud access  
  - Token propagation and scope creep across systems  
  - Auditing challenges: who *actually* has access?  
  - Mitigations: trust boundaries, scoped tokens, federation minimisation  

---
