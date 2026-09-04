---
date: 2026-08-20
item_number: 2
title: Eighty-Six Minutes Is Plenty of Time When CI Is Automated
summary: "The `arrayref` compromise was live for only about 86 minutes, which sounds reassuring until you consider what automated dependency resolution actually means."
angle: "Supply-chain risk should therefore include **dependency adoption velocity**, not merely package popularity."
interests:
  - CI/CD
  - Rust/Cargo
  - SRE
  - supply-chain security
  - dependency management
format: Short post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 2. Eighty-Six Minutes Is Plenty of Time When CI Is Automated


The `arrayref` compromise was live for only about 86 minutes, which sounds reassuring until you consider what automated dependency resolution actually means. 

A developer doesn't need to consciously choose the malicious release:

`dependency published`

→ `cargo update / fresh resolution`

→ `CI build`

→ `build.rs executes`

can happen unattended.

**Angle:** Supply-chain risk should therefore include **dependency adoption velocity**, not merely package popularity.

This makes minimum package age an unusually elegant defence. It deliberately exchanges freshness for observation time:

`publish → quarantine window → ecosystem observation → eligible for production`

It won't stop a patient attacker, but it cheaply kills an entire class of smash-and-grab compromise.

There is a broader SRE principle here:

> **Deliberately adding latency can improve safety when the delay creates time for independent signals to arrive.**

It's essentially a canary period applied to somebody else's software.

**Matches:** CI/CD, Rust/Cargo, SRE, supply-chain security, dependency management.

**Format:** **Short post**

**Confidence: 0.99.**

---
