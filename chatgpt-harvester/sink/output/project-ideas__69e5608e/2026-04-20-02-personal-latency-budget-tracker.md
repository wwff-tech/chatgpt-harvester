---
date: 2026-04-20
item_number: 2
title: Personal Latency Budget Tracker
interests:
suggested_points:
conversation_id: 69e5608e-48c0-83eb-9533-b3a6d9e148c7
label: project ideas
---

## 2. Personal Latency Budget Tracker


**Problem**  
SREs track system latency budgets obsessively, but personal workflows (deep work, task switching) are full of invisible latency drains.

**Approaches**
- Passive tracking: keyboard/mouse + window focus events
- Active tagging: annotate tasks with expected vs actual time
- “Latency SLOs” for personal work (e.g. task switching < X mins/day)

**Tech hints**
- Python daemon (cross-platform input hooks)
- SQLite event store
- Lightweight analytics (DuckDB)
- Optional browser plugin

**Formats**
- CLI + dashboard
- Daily report generator
- Markdown export (journal-style)

**Why good fit**
- Bridges SRE mindset with ADHD optimisation
- Quantifies something you already reason about qualitatively

**Why not**
- Risk of becoming noise/overhead
- Privacy implications if not strictly local-first

**Revenue potential**
- Low → Medium

**Content potential**
- Very high (novel framing)

**Community potential**
- Medium (niche but compelling)

**Tags**
`latency`, `productivity`, `adhd`, `observability`

**References**
- https://queue.acm.org/detail.cfm?id=1854041 (latency thinking)
- https://www.rescuetime.com/ (adjacent, but weaker model)

---
