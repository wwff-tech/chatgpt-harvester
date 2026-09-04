---
date: 2026-04-20
item_number: 3
title: Secrets Exposure Blast Radius Visualiser
interests:
suggested_points:
conversation_id: 69e5608e-48c0-83eb-9533-b3a6d9e148c7
label: project ideas
---

## 3. Secrets Exposure Blast Radius Visualiser


**Problem**  
Secrets leaks (env vars, logs, commits) happen — but teams struggle to understand *impact scope* quickly.

**Approaches**
- Graph model: secret → services → dependencies
- Scan logs/repos → map usage
- Simulate compromise scenarios (“what could this unlock?”)

**Tech hints**
- Python + graph DB (Neo4j or networkx initially)
- TruffleHog-style scanning
- SBOM ingestion (CycloneDX)

**Formats**
- CLI report tool
- Web UI for graph exploration
- CI integration

**Why good fit**
- Strong security + systems thinking overlap
- Concrete, real-world pain point

**Why not**
- Data collection is messy
- Partial visibility reduces usefulness

**Revenue potential**
- High (security tooling)

**Content potential**
- High

**Community potential**
- Medium → High

**Tags**
`secrets`, `security`, `blast-radius`, `sbom`

**References**
- https://github.com/trufflesecurity/trufflehog
- https://cyclonedx.org/

---
