---
date: 2026-05-20
item_number: 3
title: SRE Drift Narrative Engine
summary: "Very few explain: > “How did we end up here?”"
interests:
suggested_points:
conversation_id: 69e5608e-48c0-83eb-9533-b3a6d9e148c7
label: project ideas
---

# 3. SRE Drift Narrative Engine


## Problem
Most drift tools detect:
- config drift,
- infra drift,
- state drift.

Very few explain:
> “How did we end up here?”

## Approaches
- Construct chronological narratives from infra changes  
- Explain drift causality using telemetry + deployments + incidents  
- Generate “operational storyline” views  

## Suggested tech hints
- Temporal graph modelling  
- Distributed tracing  
- Deployment event ingestion  
- Causal inference systems  
- LLM summarisation over telemetry  

## Suggested formats
- Incident timeline tool  
- Drift investigation dashboard  
- “Git blame for infra state”  

## Why it is a good fit
- Drift is becoming a major issue in autonomous operations 
- Existing tooling focuses on detection, not explanation  

## Why it is not a good fit
- Hard attribution problem  
- Requires dense telemetry coverage  

## Revenue potential
High

## Content tie-in potential
Very high

## Community potential
High

## Tags/keywords
`drift`, `sre`, `observability`, `causality`, `infrastructure`

## References
- https://opentelemetry.io/
- https://arxiv.org/abs/2605.07161
- https://arxiv.org/abs/2604.11094

---
