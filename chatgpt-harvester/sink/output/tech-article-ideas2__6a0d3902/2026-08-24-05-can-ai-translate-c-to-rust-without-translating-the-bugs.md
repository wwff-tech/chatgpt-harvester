---
date: 2026-08-24
item_number: 5
title: Can AI Translate C to Rust Without Translating the Bugs?
summary: "Canonical is co-funding a three-year University of Bristol PhD project investigating whether AI can translate **large, mature C codebases into safe Rust**, rather than merely generating new Rust from specifications. The project is explicitly aimed at legacy software rather than toy benchmark translation."
angle: "This clears the AI bar because the interesting problem isn't generation."
interests:
  - Rust
  - C
  - AI-assisted engineering
  - formal verification
  - testing
  - Linux/open source
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 5. Can AI Translate C to Rust Without Translating the Bugs?


Canonical is co-funding a three-year University of Bristol PhD project investigating whether AI can translate **large, mature C codebases into safe Rust**, rather than merely generating new Rust from specifications. The project is explicitly aimed at legacy software rather than toy benchmark translation. 

**Angle:** This clears the AI bar because the interesting problem isn't generation.

It's **semantic archaeology**.

A mature C codebase contains:

`documented behaviour`

`undocumented behaviour`

`undefined behaviour`

`implementation-defined behaviour`

`caller assumptions`

`ABI assumptions`

`timing assumptions`

`bugs somebody depends upon`.

A syntactically beautiful Rust translation can compile perfectly while changing any of those.

The difficult question is therefore not:

> Can an LLM produce equivalent-looking Rust?

It is:

> **What evidence establishes behavioural equivalence when the original program is itself the specification?**

That naturally leads into differential testing, fuzzing both implementations with identical inputs, property testing, ABI capture, syscall tracing, performance envelopes, and eventually formal methods for tractable components.

There is also an interesting safety paradox: some undefined behaviour is exactly what you *want* the Rust translation to eliminate. So the desired transform isn't even strict equivalence:

`preserve intended semantics`

while:

`reject accidental unsafe semantics`.

Determining which is which may be harder than writing either version.

**Matches:** Rust, C, AI-assisted engineering, formal verification, testing, Linux/open source.

**Format:** **Long-form article**

**Confidence: 0.98 on the topic; far lower that AI translation will prove economical at large scale until the verification problem improves.**

---
