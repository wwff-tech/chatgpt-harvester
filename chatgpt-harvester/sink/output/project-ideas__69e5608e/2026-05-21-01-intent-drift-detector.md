---
date: 2026-05-21
item_number: 1
title: Intent Drift Detector
interests:
suggested_points:
conversation_id: 69e5608e-48c0-83eb-9533-b3a6d9e148c7
label: project ideas
---

# 1. Intent Drift Detector


## Problem Statement

Teams state intentions:

- "reduce toil",
- "improve resilience",
- "enforce least privilege",
- "increase deployment velocity".

Months later the resulting system often behaves differently.

Intent drifts silently.

Examples:

- reliability automation increasing toil,
- security controls increasing exceptions,
- AI agents producing code that satisfies tasks but violates architecture.

## Approaches

### Approach A

Build explicit intent definitions:

```yaml
intent:
  objective: reduce toil
  target: 30%
  constraints:
    - no increase in pager load
    - maintain latency SLO
```

Continuously evaluate reality against intent.

### Approach B

Infer intent from:

- tickets,
- PRs,
- RFCs,
- postmortems,

and compare implementation outcomes.

## Suggested Tech Hints

- embeddings
- semantic diffing
- graph databases
- OpenTelemetry trace ingestion
- architecture decision records (ADRs)
- event sourcing

## Suggested Formats

- CI/CD gate
- architecture governance platform
- GitHub App
- engineering scorecard

## Why It Is a Good Fit

- Directly addresses agentic engineering governance
- Strong overlap with platform engineering
- Useful for consulting environments

## Why It Is Not a Good Fit

- Intent can be ambiguous
- Requires organisational adoption

## Revenue Potential

High

## Content Tie-In Potential

Extremely high

## Community Potential

High

## Tags

`intent-drift`
`architecture`
`governance`
`platform-engineering`
`agents`

## References

- https://opentelemetry.io/
- https://martinfowler.com/articles/architecture-decision-records.html

Supported by current trends around governance and intent-centric engineering. citeturn0academia58turn0search15

---
