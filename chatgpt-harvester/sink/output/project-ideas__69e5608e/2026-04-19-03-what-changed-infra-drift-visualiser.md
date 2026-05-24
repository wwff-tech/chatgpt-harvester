---
date: 2026-04-19
item_number: 3
title: “What Changed?” – Infra Drift Visualiser
interests:
suggested_points:
conversation_id: 69e5608e-48c0-83eb-9533-b3a6d9e148c7
label: project ideas
---

## 3. “What Changed?” – Infra Drift Visualiser


**Problem**  
Infra drift happens silently across Terraform, K8s, and runtime config. Diff tools are fragmented and low-signal.

**Approaches**
- Snapshot infra state → compare over time
- Event-driven: ingest CloudEvents + derive state
- Graph-based diff (nodes = resources, edges = relationships)

**Tech hints**
- Neo4j / graph model OR simple SQLite graph tables
- Terraform state parsing
- Kubernetes API watcher
- Mermaid/Graphviz output

**Formats**
- Web UI + API
- CLI report generator
- Scheduled job + dashboard

**Why good fit**
- Aligns with your SRE + event-driven mindset
- Ties into ADRs as events (nice synergy)

**Why not**
- Many partial tools exist (none great, though)
- Needs careful UX to avoid noise

**Revenue potential**
- Medium (observability niche)

**Content potential**
- High (“Why your infra is lying to you”)

**Community potential**
- Medium

**Tags**
`infra`, `drift`, `kubernetes`, `terraform`, `observability`

**References**
- https://github.com/bridgecrewio/checkov  
- https://github.com/derailed/k9s  

---
