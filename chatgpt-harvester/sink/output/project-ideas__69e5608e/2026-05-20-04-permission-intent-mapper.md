---
date: 2026-05-20
item_number: 4
title: Permission Intent Mapper
interests:
suggested_points:
conversation_id: 69e5608e-48c0-83eb-9533-b3a6d9e148c7
label: project ideas
---

# 4. Permission Intent Mapper


## Problem
Security policies encode rules, but not:
- intent,
- business rationale,
- historical context.

This leads to:
- orphaned permissions,
- impossible audits,
- security debt.

## Approaches
- Link permissions to explicit intent records  
- Track historical justification changes  
- Detect permissions with decayed rationale  

## Suggested tech hints
- IAM graph modelling  
- Policy-as-code integration using Open Policy Agent  
- Expiry metadata  
- Semantic similarity detection for duplicate permissions  

## Suggested formats
- IAM dashboard  
- Compliance reporting layer  
- CLI auditor  

## Why it is a good fit
- Zero-trust complexity keeps increasing  
- Governance and explainability are becoming operational blockers  

## Why it is not a good fit
- Enterprise integration complexity  
- Organisational politics around ownership  

## Revenue potential
High

## Content tie-in potential
High

## Community potential
Medium

## Tags/keywords
`security`, `iam`, `zero-trust`, `governance`, `permissions`

## References
- https://www.openpolicyagent.org/
- https://owasp.org/www-project-top-10/
- https://csrc.nist.gov/projects/zero-trust-architecture

---
