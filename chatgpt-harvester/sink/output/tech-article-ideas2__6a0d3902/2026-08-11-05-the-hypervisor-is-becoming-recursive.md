---
date: 2026-08-11
item_number: 5
title: The Hypervisor Is Becoming Recursive
summary: "QEMU 11.1 is nearing release with expanded **ARM nested-virtualisation** support alongside RISC-V work; the QEMU project currently lists 11.1 release candidates while its documentation already reflects 11.1-era changes."
angle: "Nested virtualisation used to be mostly a curiosity or a cloud-provider requirement. It's becoming much more practically useful as developer infrastructure starts stacking isolation layers:"
interests:
  - QEMU/KVM
  - gVisor
  - container isolation
  - Linux
  - homelab
  - agent sandboxes
format: Short post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 5. The Hypervisor Is Becoming Recursive


QEMU 11.1 is nearing release with expanded **ARM nested-virtualisation** support alongside RISC-V work; the QEMU project currently lists 11.1 release candidates while its documentation already reflects 11.1-era changes. 

**Angle:** Nested virtualisation used to be mostly a curiosity or a cloud-provider requirement. It's becoming much more practically useful as developer infrastructure starts stacking isolation layers:

`host → VM → Kubernetes → microVM/container sandbox`

and increasingly:

`cloud VM → local VM/microVM → agent sandbox`

The agentic-development angle is worth a paragraph, but don't make it the headline. The real story is that **virtualisation is becoming composable infrastructure rather than a single boundary**.

Also worth exploring where nesting stops being sensible: performance counters, IOMMU, GPU passthrough, timing, networking complexity, and debugging become increasingly strange.

**Matches:** QEMU/KVM, gVisor, container isolation, Linux, homelab, agent sandboxes.

**Confidence: 0.88.**

---
