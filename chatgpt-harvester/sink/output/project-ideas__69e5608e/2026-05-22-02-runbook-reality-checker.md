---
date: 2026-05-22
item_number: 2
title: Runbook Reality Checker
summary: The first time many runbooks are exercised is during an incident.
interests:
suggested_points:
conversation_id: 69e5608e-48c0-83eb-9533-b3a6d9e148c7
label: project ideas
---

# 2. Runbook Reality Checker


## Problem Statement

Most operational runbooks are:

- partially obsolete,
- never tested,
- missing environmental assumptions.

The first time many runbooks are exercised is during an incident.

## Approaches

### Approach A

Execute runbooks in ephemeral environments continuously.

Detect:

- broken commands,
- missing permissions,
- dependency failures.

### Approach B

Generate synthetic incident scenarios and score runbook success rates.

## Suggested Tech Hints

- Kubernetes namespaces
- ephemeral test environments
- container snapshots
- chaos engineering
- workflow execution graphs

## Suggested Formats

- SRE platform plugin
- CLI validator
- GitHub Action
- Incident readiness dashboard

## Why It Is A Good Fit

- Clear operational value
- Direct SRE relevance
- Produces measurable outcomes

## Why It Is Not A Good Fit

- Infrastructure-heavy
- Simulation realism is difficult

## Revenue Potential

High

## Content Tie-In Potential

High

## Community Potential

High

## Tags

`sre`
`runbooks`
`incident-response`
`chaos-engineering`
`validation`

## References

- https://sre.google/sre-book/
- https://principlesofchaos.org/

---
