---
date: 2026-05-27
item_number: 3
title: Observability Debt Scanner
interests:
suggested_points:
conversation_id: 69e5608e-48c0-83eb-9533-b3a6d9e148c7
label: project ideas
---

# 3. Observability Debt Scanner


## Problem Statement

Recent empirical research found AI coding agents frequently underperform regarding logging and observability requirements. Humans later repair many of these omissions. 

Observability debt accumulates silently.

## Approaches

### Approach A

Continuously score repositories for:

- logging coverage,
- tracing coverage,
- metrics instrumentation,
- alertability.

### Approach B

Detect execution paths lacking observability coverage.

Flag blind spots before deployment.

## Suggested Tech Hints

- AST analysis
- code property graphs
- OpenTelemetry schemas
- static analysis
- CI integration

## Suggested Formats

- GitHub bot
- CI/CD gate
- PR reviewer
- engineering scorecard

## Why It Is A Good Fit

- Objective value
- Strong SRE relevance
- Growing AI-code generation problem

## Why It Is Not A Good Fit

- Language-specific complexity
- Potential false positives

## Revenue Potential

High

## Content Tie-In Potential

High

## Community Potential

High

## Tags

`observability`
`logging`
`telemetry`
`sre`
`ai-generated-code`

## References

- OpenTelemetry
- Logging study 

---
