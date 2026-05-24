---
date: 2026-04-20
item_number: 5
title: “Async Decision Log (ADR as Event Stream)”
interests:
suggested_points:
conversation_id: 69e5608e-48c0-83eb-9533-b3a6d9e148c7
label: project ideas
---

## 5. “Async Decision Log (ADR as Event Stream)”


**Problem**  
Architectural Decision Records are static and often ignored. Real decisions happen in chats, tickets, and code.

**Approaches**
- Capture decisions as structured events
- Auto-generate ADRs from event streams
- Link decisions to code + infra changes

**Tech hints**
- Markdown + frontmatter
- Event ingestion (webhooks, git hooks)
- LLM summarisation (optional, local-first preferred)

**Formats**
- Git-based tool
- CLI + static site generator
- MCP server (very strong fit)

**Why good fit**
- Direct continuation of your “ADR as events” thinking
- Strong conceptual clarity

**Why not**
- Requires behaviour change to be effective
- Risk of over-automation losing nuance

**Revenue potential**
- Low → Medium

**Content potential**
- Very high (book-level)

**Community potential**
- Medium

**Tags**
`adr`, `events`, `architecture`, `knowledge`

**References**
- https://adr.github.io/
- https://martinfowler.com/articles/architecture-decision-records.html

---
