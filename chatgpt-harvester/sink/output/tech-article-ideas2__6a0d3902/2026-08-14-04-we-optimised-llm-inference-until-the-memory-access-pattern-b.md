---
date: 2026-08-14
item_number: 4
title: We Optimised LLM Inference Until the Memory Access Pattern Became the Prompt
summary: "The vulnerability isn't an ordinary memory disclosure. The optimisation itself creates the signal: skipping inactive neuron accesses makes memory behaviour depend on the processed tokens."
angle: Performance optimisations are information channels.
interests:
  - LLM infrastructure
  - side channels
  - confidential computing
  - CPU architecture
  - performance engineering
format: Long-form
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 4. We Optimised LLM Inference Until the Memory Access Pattern Became the Prompt


**SparSEEty**, new research from Yonsei University, attacks sparse LLM-serving systems by observing input-dependent neuron weight accesses. The researchers demonstrate reconstruction of both prompt and response tokens with reported BLEU scores above **0.95**, including against inference running inside an Intel TDX confidential VM. 

The vulnerability isn't an ordinary memory disclosure. The optimisation itself creates the signal: skipping inactive neuron accesses makes memory behaviour depend on the processed tokens. 

**Angle:** **Performance optimisations are information channels.**

We have seen this repeatedly:

`cache → timing leak`

`branch prediction → Spectre`

`compression → CRIME/BREACH`

`deduplication → cross-tenant inference`

and now:

`sparse inference → token-dependent memory access`

The important security review question therefore isn't merely:

> Does this optimisation preserve correctness?

but:

> **What previously constant behaviour has become input-dependent?**

That is a very reusable threat-modelling heuristic.

**Matches:** LLM infrastructure, side channels, confidential computing, CPU architecture, performance engineering.

**Confidence: 0.97 — best deep technical piece today.**

---
