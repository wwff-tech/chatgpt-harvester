---
date: 2026-05-21
item_number: 3
title: Observability Completeness Scanner
interests:
suggested_points:
conversation_id: 69e5608e-48c0-83eb-9533-b3a6d9e148c7
label: project ideas
---

# 3. Observability Completeness Scanner


## Problem Statement

AI-generated code frequently underperforms on observability concerns.

Humans continue fixing logs and telemetry after generation. citeturn0academia56

Most organisations lack a way to assess observability coverage systematically.

## Approaches

### Approach A

Score repositories:

- logging coverage,
- tracing coverage,
- metrics coverage,
- alertability.

### Approach B

Detect unobservable execution paths automatically.

## Suggested Tech Hints

- AST analysis
- trace coverage graphs
- OpenTelemetry schema inspection
- code property graphs

## Suggested Formats

- CI gate
- PR reviewer bot
- platform engineering dashboard

## Why It Is a Good Fit

- Clear operational value
- Agent-generated code magnifies issue
- Objective metrics possible

## Why It Is Not a Good Fit

- Language ecosystem complexity
- False positives

## Revenue Potential

High

## Content Tie-In Potential

High

## Community Potential

High

## Tags

`observability`
`logging`
`tracing`
`telemetry`
`ai-generated-code`

## References

- https://opentelemetry.io/
- https://arxiv.org/abs/2604.09409

---
