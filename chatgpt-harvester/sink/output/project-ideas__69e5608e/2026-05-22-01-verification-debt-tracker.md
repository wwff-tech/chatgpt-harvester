---
date: 2026-05-22
item_number: 1
title: Verification Debt Tracker
summary: Over time organisations accumulate risk because validation effort lags behind change velocity.
interests:
suggested_points:
conversation_id: 69e5608e-48c0-83eb-9533-b3a6d9e148c7
label: project ideas
---

# 1. Verification Debt Tracker


## Problem Statement

Teams understand:

- technical debt,
- security debt,
- operational debt.

Few track:

- **verification debt**.

Examples:

- AI-generated code with weak tests,
- unvalidated runbooks,
- unverified infrastructure changes,
- stale assumptions,
- undocumented manual procedures.

Over time organisations accumulate risk because validation effort lags behind change velocity.

## Approaches

### Approach A

Create a verification score for repositories:

- test coverage,
- observability coverage,
- ownership coverage,
- documentation freshness,
- deployment validation.

### Approach B

Track verification debt as a first-class metric alongside error budgets.

Generate trends and projected risk accumulation.

## Suggested Tech Hints

- Git mining
- static analysis
- CI/CD metadata
- code ownership graphs
- OpenTelemetry ingestion
- ADR parsing

## Suggested Formats

- GitHub App
- Engineering scorecard
- Platform engineering dashboard
- CI quality gate

## Why It Is A Good Fit

- AI-generated code increases verification demand
- Useful regardless of model vendor
- Fits platform engineering trends

## Why It Is Not A Good Fit

- Requires organisational buy-in
- Risk scoring can become subjective

## Revenue Potential

High

## Content Tie-In Potential

Very High

## Community Potential

High

## Tags

`verification`
`technical-debt`
`platform-engineering`
`quality`
`ai-generated-code`

## References

- OpenTelemetry
- https://martinfowler.com/
- Research on verification-first engineering 

---
