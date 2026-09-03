---
date: 2026-08-26
item_number: 8
title: "**“RISC-V Has Reached the Point Where You Can Put It in a Normal Rack and Run CUDA”** — Short post / watch item"
summary: "SiFive is showing the **BigSky SF-2U870**, a rackable 2U RISC-V development server with 32 P870-D cores, 256 GB DDR5, PCIe 5.0, U.2 NVMe, 10/25 GbE, and room for GPUs. RHEL 10 and Ubuntu 26.04 are supported, and SiFive says CUDA is already running on the platform as part of its work with Nvidia."
angle: "Don't benchmark it against Xeon yet. That's not what the machine is for."
interests:
  - RISC-V
  - Linux
  - servers
  - CI
  - CUDA/GPU compute
  - hardware portability
format: Short post / watch item
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 8. **“RISC-V Has Reached the Point Where You Can Put It in a Normal Rack and Run CUDA”** — Short post / watch item


SiFive is showing the **BigSky SF-2U870**, a rackable 2U RISC-V development server with 32 P870-D cores, 256 GB DDR5, PCIe 5.0, U.2 NVMe, 10/25 GbE, and room for GPUs. RHEL 10 and Ubuntu 26.04 are supported, and SiFive says CUDA is already running on the platform as part of its work with Nvidia. 

**Angle:** Don't benchmark it against Xeon yet. That's not what the machine is for.

The milestone is that RISC-V developers can now put:

`standard rack server`

`standard enterprise Linux`

`standard NVMe`

`standard OCP NIC`

`standard PCIe GPU`

into CI and discover everything in their software that accidentally assumes:

`server == x86_64 / aarch64`.

That's how an architecture becomes boring enough to matter.

The real success metric isn't SPECint. It's whether software projects start adding:

`riscv64`

to ordinary CI matrices and then stop talking about it.

**Matches:** RISC-V, Linux, servers, CI, CUDA/GPU compute, hardware portability.

**Format:** **Short post / watch item**

**Confidence: 0.96.**

---
