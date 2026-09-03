---
date: 2026-08-20
item_number: 7
title: "**“RISC-V Servers Have Reached the 256-Entry Reorder Buffer Stage”** — Short post / hardware article"
summary: "StarFive announced its **Dubhe-100** server-class RISC-V CPU IP. The design is RVA23-compliant, with a 15-stage pipeline, six-wide issue, a **256-entry reorder buffer**, and an out-of-order vector implementation. StarFive says customers are already designing server SoCs around it."
angle: This complements the Spectre story from last week beautifully.
interests:
  - RISC-V
  - CPU architecture
  - Linux
  - servers
  - compilers
  - embedded-to-datacentre evolution
format: "**Short post**, unless there is enough microarchitectural material for a deeper comparison."
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 7. **“RISC-V Servers Have Reached the 256-Entry Reorder Buffer Stage”** — Short post / hardware article


StarFive announced its **Dubhe-100** server-class RISC-V CPU IP. The design is RVA23-compliant, with a 15-stage pipeline, six-wide issue, a **256-entry reorder buffer**, and an out-of-order vector implementation. StarFive says customers are already designing server SoCs around it. 

**Angle:** This complements the Spectre story from last week beautifully.

Early RISC-V discussion was often about simplicity and openness.

A six-wide, deeply out-of-order CPU with a 256-entry ROB is not simple.

And that's good.

High-performance general-purpose CPUs converge on complexity because hiding latency and extracting instruction-level parallelism are genuinely difficult problems.

RISC-V is increasingly separating:

`simple/open ISA`

from:

`very complicated implementation`.

That's exactly what a mature architecture should allow.

**Matches:** RISC-V, CPU architecture, Linux, servers, compilers, embedded-to-datacentre evolution.

**Format:** **Short post**, unless there is enough microarchitectural material for a deeper comparison.

**Confidence: 0.96.**

---
