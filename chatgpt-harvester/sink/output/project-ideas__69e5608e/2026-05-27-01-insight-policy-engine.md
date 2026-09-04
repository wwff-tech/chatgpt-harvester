---
date: 2026-05-27
item_number: 1
title: Insight Policy Engine
interests:
suggested_points:
conversation_id: 69e5608e-48c0-83eb-9533-b3a6d9e148c7
label: project ideas
---

# 1. Insight Policy Engine


## Problem Statement

Most agent systems optimise:

- execution,
- completion,
- throughput.

Very few optimise:

> Was this worth interrupting a human for?

Recent research argues that future coding agents should be evaluated by the quality of their "insight policy" rather than merely autonomy. 

Examples:

- opening unnecessary tickets,
- generating noisy alerts,
- proposing trivial PRs,
- escalating irrelevant findings.

## Approaches

### Approach A

Create a scoring layer that evaluates:

- novelty,
- urgency,
- confidence,
- potential impact.

Only high-value insights reach humans.

### Approach B

Learn user-specific interruption preferences.

Adapt escalation behaviour over time.

## Suggested Tech Hints

- ranking models
- reinforcement learning from feedback
- event streams
- embeddings
- confidence scoring
- retrieval systems

## Suggested Formats

- agent middleware
- Slack integration
- VS Code extension
- GitHub bot

## Why It Is A Good Fit

- Directly aligned with long-horizon agents
- Human attention is increasingly scarce
- Applicable across vendors

## Why It Is Not A Good Fit

- Requires behavioural data
- Difficult to define "useful"

## Revenue Potential

High

## Content Tie-In Potential

Very High

## Community Potential

High

## Tags

`agents`
`attention-management`
`signal-vs-noise`
`agentops`
`human-in-the-loop`

## References

- Proactive coding agent research 

---
