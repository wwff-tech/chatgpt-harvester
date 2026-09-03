---
date: 2026-05-23
item_number: 1
title: Causal Topology Builder
summary: AI agents repeatedly spend tokens reconstructing topology from raw telemetry.
interests:
suggested_points:
conversation_id: 69e5608e-48c0-83eb-9533-b3a6d9e148c7
label: project ideas
---

# 1. Causal Topology Builder


## Problem Statement

Current observability stacks collect:

- metrics,
- traces,
- logs,
- events.

But they rarely understand:

- causality,
- dependency meaning,
- operational relationships.

AI agents repeatedly spend tokens reconstructing topology from raw telemetry. 

## Approaches

### Approach A

Continuously build:

- service graphs,
- dependency graphs,
- ownership graphs,
- failure graphs.

Expose them as a queryable knowledge layer.

### Approach B

Generate causal explanations:

> "Latency increased because Service A saturated Redis which delayed queue consumers."

rather than merely displaying correlated metrics.

## Suggested Tech Hints

- OpenTelemetry ingestion
- graph databases
- property graphs
- Bayesian networks
- causal inference
- event sourcing

## Suggested Formats

- platform engineering service
- observability add-on
- AI-agent middleware
- architecture explorer

## Why It Is A Good Fit

- Strong alignment with agentic SRE
- Applicable across multiple observability vendors
- Increasingly valuable as systems grow

## Why It Is Not A Good Fit

- Significant modelling complexity
- Difficult to validate causality automatically

## Revenue Potential

High

## Content Tie-In Potential

Very High

## Community Potential

High

## Tags

`causality`
`observability`
`sre`
`graph-database`
`topology`

## References

- OpenTelemetry
- SREGym benchmark 
- Causely paper 

---
