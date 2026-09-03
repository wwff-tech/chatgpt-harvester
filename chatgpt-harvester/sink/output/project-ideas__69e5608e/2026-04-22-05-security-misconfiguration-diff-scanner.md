---
date: 2026-04-22
item_number: 5
title: Security Misconfiguration Diff Scanner
interests:
suggested_points:
conversation_id: 69e5608e-48c0-83eb-9533-b3a6d9e148c7
label: project ideas
---

## 5. Security Misconfiguration Diff Scanner


**Problem**  
Security posture drifts subtly over time; changes are small, but cumulative risk increases.

**Approaches**
- Snapshot configs (IAM, K8s RBAC, firewall rules)
- Diff over time with risk scoring
- Alert on “meaningful” changes

**Tech hints**
- Cloud provider APIs
- YAML/JSON diffing
- Policy engine (OPA or custom rules)

**Formats**
- CLI tool
- CI/CD check
- Scheduled audit service

**Why good fit**
- Strong security + infra overlap
- Practical and immediately useful

**Why not**
- Competes with existing tools
- Needs careful signal filtering

**Revenue potential**
- Medium → High

**Content potential**
- Medium → High

**Community potential**
- Medium

**Tags**
`security`, `misconfig`, `diff`, `cloud`

**References**
- https://cloudcustodian.io/  
- https://github.com/aquasecurity/kube-bench  

---
