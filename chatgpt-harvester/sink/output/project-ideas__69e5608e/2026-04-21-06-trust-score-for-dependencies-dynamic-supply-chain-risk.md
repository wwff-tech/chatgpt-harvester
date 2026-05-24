---
date: 2026-04-21
item_number: 6
title: “Trust Score for Dependencies” (Dynamic Supply Chain Risk)
interests:
suggested_points:
conversation_id: 69e5608e-48c0-83eb-9533-b3a6d9e148c7
label: project ideas
---

## 6. “Trust Score for Dependencies” (Dynamic Supply Chain Risk)


**Problem**  
Dependency risk is static (CVEs, stars), but real trust is dynamic (maintainer activity, release patterns, anomalies).

**Approaches**
- Aggregate signals: commits, releases, issues, CVEs
- Detect anomalies (sudden maintainer change, unusual releases)
- Score + alert

**Tech hints**
- GitHub API ingestion
- Time-series anomaly detection
- Simple scoring model → evolve later

**Formats**
- CLI tool
- CI plugin
- Dashboard

**Why good fit**
- Strong security + systems analysis overlap
- Timely given supply chain attacks

**Why not**
- Data quality varies
- Risk of misleading scores

**Revenue potential**
- Medium

**Content potential**
- High

**Community potential**
- Medium → High

**Tags**
`supply-chain`, `security`, `dependencies`, `risk`

**References**
- https://snyk.io/
- https://deps.dev/

---
