---
date: 2026-08-24
item_number: 8
title: "**“RAID Picks Its Own Fast Path at Boot. More Software Probably Should.”** — Short technical post"
summary: Linux 7.3 improves the boot-time benchmarking used to select RAID5/6 XOR and parity implementations. Linux already tests available implementations during initialisation to choose the fastest path for the actual machine — for example, deciding between hardware-accelerated variants such as AVX2 and AVX-512 — rather than assuming one implementation wins universally. The new work improves the benchmark methodology and adds KUnit benchmark coverage.
angle: "This is a neat middle ground between:"
interests:
  - Linux
  - RAID/storage
  - CPU optimisation
  - benchmarking
  - performance engineering
format: Short technical post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 8. **“RAID Picks Its Own Fast Path at Boot. More Software Probably Should.”** — Short technical post


Linux 7.3 improves the boot-time benchmarking used to select RAID5/6 XOR and parity implementations. Linux already tests available implementations during initialisation to choose the fastest path for the actual machine — for example, deciding between hardware-accelerated variants such as AVX2 and AVX-512 — rather than assuming one implementation wins universally. The new work improves the benchmark methodology and adds KUnit benchmark coverage. 

**Angle:** This is a neat middle ground between:

`compile-time decision`

and:

`continuous adaptive optimisation`.

If a hardware property is stable across a boot, benchmark once:

`machine starts`

→ `measure candidate implementations`

→ `select winner`

→ `use until reboot`.

That avoids enormous matrices of assumptions about CPU models while avoiding runtime adaptation complexity.

There are plenty of analogous candidates: compression algorithms, checksum implementations, crypto primitives, memcpy variants, encoding paths, and storage strategies.

**Matches:** Linux, RAID/storage, CPU optimisation, benchmarking, performance engineering.

**Format:** **Short technical post**

**Confidence: 0.97.**

---
