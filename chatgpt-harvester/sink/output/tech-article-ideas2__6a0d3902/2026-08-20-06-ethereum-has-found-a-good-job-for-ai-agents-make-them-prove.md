---
date: 2026-08-20
item_number: 6
title: "Ethereum Has Found a Good Job for AI Agents: Make Them Prove It"
summary: "The Ethereum Foundation launched **better.codes** today with Yukon and zkSecurity. Agents compete to improve error-correcting codes used in hash-based SNARK research, but crucially the objective isn't judged by another model: candidate improvements are evaluated against **machine-checked soundness**."
angle: Forget the blockchain aspect if desired. The architecture is the story.
interests:
  - agentic AI
  - formal verification
  - testing
  - search/optimisation
  - security engineering
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 6. Ethereum Has Found a Good Job for AI Agents: Make Them Prove It


The Ethereum Foundation launched **better.codes** today with Yukon and zkSecurity. Agents compete to improve error-correcting codes used in hash-based SNARK research, but crucially the objective isn't judged by another model: candidate improvements are evaluated against **machine-checked soundness**. 

**Angle:** Forget the blockchain aspect if desired. The architecture is the story.

A lot of agent research currently looks like:

`agent generates → model judges → benchmark says 73%`.

This looks more like:

`agent searches → formal machinery verifies → objectively better artefact survives`.

That is a much healthier domain for high-autonomy agents because **verification is substantially cheaper and more trustworthy than generation**.

This suggests a useful criterion for agent suitability:

\[
\text{agent value} \propto
\frac{\text{search-space difficulty}}
{\text{verification difficulty}}
\]

Agents should be unusually effective where solutions are difficult to discover but cheap to prove correct.

SAT solving, compiler optimisation, circuit design, formal proofs, scheduling, configuration optimisation, and some infrastructure planning all fit that shape.

**Matches:** agentic AI, formal verification, testing, search/optimisation, security engineering.

**Format:** **Long-form article**

**Confidence: 0.98 — my favourite AI story today.**

---
