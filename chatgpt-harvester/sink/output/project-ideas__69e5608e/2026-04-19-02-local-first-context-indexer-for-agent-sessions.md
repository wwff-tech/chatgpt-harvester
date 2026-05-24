---
date: 2026-04-19
item_number: 2
title: Local-First “Context Indexer” for Agent Sessions
interests:
suggested_points:
conversation_id: 69e5608e-48c0-83eb-9533-b3a6d9e148c7
label: project ideas
---

## 2. Local-First “Context Indexer” for Agent Sessions


**Problem**  
Agent sessions lose context across runs. Dev vs prod drift. No structured, queryable memory of “what the system looked like”.

**Approaches**
- File watcher + AST parsing → structured index
- LSP-backed semantic extraction
- Snapshot + diff system (like git but semantic)

**Tech hints**
- Python + `watchdog`
- tree-sitter / ast
- SQLite + FTS5
- embeddings (optional, local model)

**Formats**
- CLI daemon
- MCP server (this is a *very* good fit)
- VSCode extension later

**Why good fit**
- You’ve literally described this problem already
- Fits your “agents are lossy reconstructors” thesis
- Low infra overhead, high usefulness

**Why not**
- Hard to define “correct” abstraction level
- Risk of over-engineering vs just using git + grep

**Revenue potential**
- Medium (dev productivity tool)

**Content potential**
- Very high (this is book material)

**Community potential**
- High among agentic dev crowd

**Tags**
`agent-memory`, `ast`, `indexing`, `mcp`, `devtools`

**References**
- tree-sitter: https://tree-sitter.github.io  
- LSP spec: https://microsoft.github.io/language-server-protocol/  

---
