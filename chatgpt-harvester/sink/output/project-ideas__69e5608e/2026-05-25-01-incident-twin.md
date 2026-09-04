---
date: 2026-05-25
item_number: 1
title: Incident Twin
interests:
suggested_points:
conversation_id: 69e5608e-48c0-83eb-9533-b3a6d9e148c7
label: project ideas
---

# 1. Incident Twin


## Problem Statement

Postmortems reconstruct incidents after the fact.

During incidents, engineers typically operate with:

- incomplete telemetry,
- stale dashboards,
- fragmented context,
- contradictory signals.

The operational picture is constantly changing.

## Approaches

### Approach A

Build a continuously updated incident model:

- dependencies,
- affected services,
- recent changes,
- inferred impact.

Maintain a live "digital twin" of the incident.

### Approach B

Use causal reasoning to update probable root causes as new telemetry arrives.

Move from static dashboards to dynamic incident hypotheses.

## Suggested Tech Hints

- OpenTelemetry ingestion
- Graph databases
- Bayesian networks
- Event correlation
- Topology discovery
- Causal inference

Research around causal intelligence layers for SRE appears increasingly relevant. 

## Suggested Formats

- Incident management platform
- Grafana extension
- Slack assistant
- CLI investigation tool

## Why It Is A Good Fit

- Strong alignment with AI-assisted SRE
- Direct operational value
- Differentiated from traditional monitoring

## Why It Is Not A Good Fit

- High modelling complexity
- Risk of false confidence

## Revenue Potential

High

## Content Tie-In Potential

Very High

## Community Potential

High

## Tags

`incident-management`
`causal-ai`
`sre`
`digital-twin`
`observability`

## References

- OpenTelemetry
- SREGym research 
- Causely research 

---
