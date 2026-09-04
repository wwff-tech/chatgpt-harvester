---
date: 2026-08-15
item_number: 7
title: "**“Someone Is Building an RTOS in Rust for the ESP32-S3 — and It's Not Just Async With Extra Steps”** — Experimental post"
summary: "A newly open-sourced project called **Rivet** is implementing an RTOS kernel in Rust across ARM Cortex-M, RISC-V, and Xtensa. Its author reports pre-emptive scheduling, priority inheritance, tickless operation, static task resources, no kernel allocator, cooperative async below the scheduler, and dual-core SMP support on the ESP32-S3."
angle: This one deserves experimentation rather than punditry.
interests:
  - ESP32-S3
  - Rust
  - embedded electronics
  - RTOS design
  - RISC-V
format: Short post now; long-form only after hands-on testing.
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 7. **“Someone Is Building an RTOS in Rust for the ESP32-S3 — and It's Not Just Async With Extra Steps”** — Experimental post


A newly open-sourced project called **Rivet** is implementing an RTOS kernel in Rust across ARM Cortex-M, RISC-V, and Xtensa. Its author reports pre-emptive scheduling, priority inheritance, tickless operation, static task resources, no kernel allocator, cooperative async below the scheduler, and dual-core SMP support on the ESP32-S3. 

**Angle:** This one deserves experimentation rather than punditry.

The particularly interesting architectural combination is:

`pre-emptive real-time tasks`

plus

`cooperative async tasks`

rather than forcing embedded Rust into either pure async or conventional RTOS semantics.

I'd explore whether this gives a useful separation:

`hard-ish timing work → scheduled task`

`I/O concurrency → async executor`

Then test it against FreeRTOS on an ESP32-S3: interrupt latency, context-switch cost, memory footprint, priority inversion behaviour, multicore scheduling, and failure/debugging ergonomics.

**Matches:** ESP32-S3, Rust, embedded electronics, RTOS design, RISC-V.

**Format:** **Short post now; long-form only after hands-on testing.**

**Confidence: 0.84** — interesting young project, not something I'd recommend for production yet.

Rivet RTOS repository

---
