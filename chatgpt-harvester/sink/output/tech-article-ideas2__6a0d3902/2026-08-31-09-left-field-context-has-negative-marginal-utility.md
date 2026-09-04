---
date: 2026-08-31
item_number: 9
title: Left-field — “Context Has Negative Marginal Utility”
summary: SWE-Skills-Bench gives a quantitative hook for something agent engineering has been circling for a while.
angle: "We often assume:"
interests:
  - agent architecture
  - context engineering
  - RAG
  - developer agents
  - cognitive systems
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 9. Left-field — “Context Has Negative Marginal Utility”


SWE-Skills-Bench gives a quantitative hook for something agent engineering has been circling for a while. 

**Angle:** We often assume:

\[
UsefulContext(n+1) \ge UsefulContext(n)
\]

More information cannot hurt.

Except it can.

Additional context can be:

`irrelevant`

`stale`

`contradictory`

`over-specific`

`attention-consuming`.

So agent context may behave more like cache or working memory than a knowledge base.

There is probably an optimum:

\[
Utility(C) =
RelevantInformation(C)
-
Interference(C)
-
TokenCost(C)
\]

After that point, adding knowledge reduces performance.

That suggests a very different agent architecture:

`huge external memory`

+ `aggressive retrieval`

+ **`tiny task-specific working context`**

rather than endlessly expanding system prompts and instruction files.

**Matches:** agent architecture, context engineering, RAG, developer agents, cognitive systems.

**Format:** **Long-form article**

**Confidence: 0.99 on the principle; the exact shape of that utility curve will be highly model- and task-dependent.**

---
