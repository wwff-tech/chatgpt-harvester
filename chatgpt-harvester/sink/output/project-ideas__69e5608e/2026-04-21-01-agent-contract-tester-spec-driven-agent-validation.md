---
date: 2026-04-21
item_number: 1
title: “Agent Contract Tester” (Spec-Driven Agent Validation)
interests:
suggested_points:
conversation_id: 69e5608e-48c0-83eb-9533-b3a6d9e148c7
label: project ideas
---

## 1. “Agent Contract Tester” (Spec-Driven Agent Validation)


**Problem**  
Agent behaviour is non-deterministic and brittle. There’s no equivalent of contract testing (à la Pact) for agents interacting with tools, APIs, and environments.

**Approaches**
- Define contracts: expected inputs/outputs + invariants
- Replay-based validation (record real runs → fuzz variations)
- Property-based testing for agent behaviours

**Tech hints**
- Python + pytest integration
- Hypothesis (property-based testing)
- JSON Schema / OpenAPI contracts
- Event capture via OpenTelemetry

**Formats**
- CLI tool (`agent-test run`)
- CI plugin
- Library for agent frameworks

**Why good fit**
- Strong overlap with your reliability/SRE instincts
- Aligns with agent safety + observability themes
- High leverage for any agent system you build

**Why not**
- Hard to define meaningful contracts for open-ended tasks
- Risk of false confidence if tests are too narrow

**Revenue potential**
- Medium → High (teams will need this)

**Content potential**
- Very high (“Your agent passed tests and still broke prod”)

**Community potential**
- High (emerging gap)

**Tags**
`agent-testing`, `contracts`, `reliability`, `fuzzing`

**References**
- https://hypothesis.readthedocs.io/
- https://pact.io/

---
