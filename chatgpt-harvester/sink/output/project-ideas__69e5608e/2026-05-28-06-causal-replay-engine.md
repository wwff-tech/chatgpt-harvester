---
date: 2026-05-28
item_number: 6
title: Causal Replay Engine
summary: "Current observability systems replay: - logs, - traces, - metrics."
interests:
suggested_points:
conversation_id: 69e5608e-48c0-83eb-9533-b3a6d9e148c7
label: project ideas
---

# 6. Causal Replay Engine


## Problem Statement

Current observability systems replay:
- logs,
- traces,
- metrics.

They rarely replay:
- causality,
- reasoning,
- assumptions,
- operational decisions.

Recent causal observability research demonstrates major gains when systems maintain explicit causal representations. 

## Approaches

### Approach A

Capture causal snapshots during incidents.

Replay:
- dependencies,
- inferred hypotheses,
- topology state,
- operator decisions.

### Approach B

Allow agents to compare historical incidents against current operational state.

## Suggested Tech Hints

- temporal graphs
- event sourcing
- causal inference
- OpenTelemetry integration
- replay systems

## Suggested Formats

- incident platform
- observability layer
- postmortem tooling
- AI-SRE assistant

## Why It Is A Good Fit

- Strong SRE relevance
- AI-native operational tooling
- Differentiated from standard replay systems

## Why It Is Not A Good Fit

- Complex modelling problem
- Difficult causal correctness validation

## Revenue Potential

High

## Content Tie-In Potential

Very High

## Community Potential

High

## Tags

`causality`
`incident-response`
`sre`
`replay`
`observability`

## References

- Causely benchmark study 
- Time and observability causality failures 

---
