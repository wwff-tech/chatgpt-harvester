---
date: 2026-08-22
item_number: 8
title: "**“Kernel Maintenance Has a Garbage Collector, and It Just Found Hundreds of Drivers”** — Long-form / short essay"
summary: "Linux 7.3 has deprecated a substantial set of effectively unused 32-bit ARM platforms. Twenty-two of the remaining 28 legacy pre-device-tree board files are marked for eventual removal, along with support for several old CPU configurations and userspace ABIs. Once the platforms go, **hundreds of otherwise platform-specific drivers can also be removed**. Nothing is removed yet, giving any remaining users an LTS window to surface."
angle: "Software deletion has **dependency amplification** too."
interests:
  - Linux kernel
  - embedded ARM
  - technical debt
  - maintenance economics
  - legacy systems
format: "**Long-form article**, or a punchy short."
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 8. **“Kernel Maintenance Has a Garbage Collector, and It Just Found Hundreds of Drivers”** — Long-form / short essay


Linux 7.3 has deprecated a substantial set of effectively unused 32-bit ARM platforms. Twenty-two of the remaining 28 legacy pre-device-tree board files are marked for eventual removal, along with support for several old CPU configurations and userspace ABIs. Once the platforms go, **hundreds of otherwise platform-specific drivers can also be removed**. Nothing is removed yet, giving any remaining users an LTS window to surface. 

**Angle:** Software deletion has **dependency amplification** too.

One obsolete platform isn't merely:

`platform support = 20,000 lines`.

It pins:

`CPU quirks`

`drivers`

`ABIs`

`compiler workarounds`

`test paths`

`conditional branches`

`maintainer knowledge`.

Removing the root dependency lets an entire subtree disappear.

This is the inverse of dependency creep:

> **Deleting one architectural promise can make hundreds of implementation obligations collectible.**

There's a very good engineering-management analogy here. Compatibility promises are liabilities that compound interest.

**Matches:** Linux kernel, embedded ARM, technical debt, maintenance economics, legacy systems.

**Format:** **Long-form article**, or a punchy short.

**Confidence: 0.98.**

---
