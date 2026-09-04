---
date: 2026-05-30
item_number: 1
title: Tool Budget Broker
interests:
suggested_points:
conversation_id: 69e5608e-48c0-83eb-9533-b3a6d9e148c7
label: project ideas
---

# 1. Tool Budget Broker


## Problem Statement

Most agent systems optimise:

- correctness,
- latency,
- task completion.

Few optimise:

- tool costs,
- API consumption,
- risk exposure,
- permission usage.

Recent MCP deployment research highlights missing infrastructure around adaptive budgeting and tool governance. 

## Approaches

### Approach A

Assign every agent:

- cost budget,
- latency budget,
- permission budget,
- risk budget.

Agents must allocate resources intelligently.

### Approach B

Broker tool requests through a central controller.

Continuously optimise:

- tool choice,
- invocation frequency,
- fallback behaviour.

## Suggested Tech Hints

- Open Policy Agent
- Redis
- GraphQL gateway
- MCP proxy
- OpenTelemetry
- Rate-limiting frameworks

## Suggested Formats

- MCP middleware
- Agent gateway
- Enterprise governance platform
- Open-source infrastructure project

## Why It Is A Good Fit

- Aligns with real enterprise concerns
- Protocol agnostic
- Fits current governance trends

## Why It Is Not A Good Fit

- Requires deep integration
- Difficult to model business risk accurately

## Revenue Potential

High

## Content Tie-In Potential

Very High

## Community Potential

High

## Tags

`mcp`
`agent-governance`
`tool-budgeting`
`agentops`
`policy`

## References

- MCP production deployment patterns 
- Governance failures in enterprise agents 

---
