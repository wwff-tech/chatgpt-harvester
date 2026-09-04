---
date: 2026-08-31
item_number: 4
title: Agent Instructions Are Dependencies, So Version Them Like Dependencies
summary: "One particularly useful SWE-Skills-Bench result is that some skills made agents worse because their guidance **did not match the version or context of the target project**."
angle: "We tend to treat agent instructions as documentation:"
interests:
  - coding agents
  - CI
  - developer tooling
  - dependency management
  - agent-first engineering
format: Short post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 4. Agent Instructions Are Dependencies, So Version Them Like Dependencies


One particularly useful SWE-Skills-Bench result is that some skills made agents worse because their guidance **did not match the version or context of the target project**. 

**Angle:** We tend to treat agent instructions as documentation:

`SKILL.md`

`AGENTS.md`

`CLAUDE.md`

`prompt.md`.

But operationally they behave more like dependencies.

A skill saying:

> use API X this way

has compatibility requirements just like a library.

That suggests metadata such as:

`applies_to`

`framework_version`

`tested_with`

`last_verified`

`conflicts_with`

`expires_after`.

And CI could test the skill itself against representative tasks.

> **A stale agent skill is executable documentation debt.**

**Matches:** coding agents, CI, developer tooling, dependency management, agent-first engineering.

**Format:** **Short post**

**Confidence: 0.99.**

---
