---
date: 2026-08-22
item_number: 9
title: Left-field — “Plugging In a USB Stick Is a Remote Procedure Call to Your Kernel”
summary: The NTFS vulnerability suggests a deliberately provocative reframing.
angle: "“Remote” normally means network distance, but from the perspective of a trust boundary, physical transport isn't particularly special."
interests:
  - embedded systems
  - Linux
  - hardware security
  - API design
  - threat modelling
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 9. Left-field — “Plugging In a USB Stick Is a Remote Procedure Call to Your Kernel”


The NTFS vulnerability suggests a deliberately provocative reframing. 

**Angle:** “Remote” normally means network distance, but from the perspective of a trust boundary, physical transport isn't particularly special.

A USB storage device effectively sends:

`please parse this superblock`

`please instantiate these inodes`

`please honour these metadata attributes`

`please expose this namespace`.

That's an API.

The transport happens to be NAND flash and USB rather than TCP.

Once you think this way, a lot of hardware becomes easier to threat-model:

`USB device → RPC endpoint`

`PCIe card → DMA-capable peer`

`maintenance connector → network interface`

`filesystem image → structured request`

`firmware blob → executable artefact`.

The useful principle is:

> **Trust boundaries are defined by authority, not distance.**

**Matches:** embedded systems, Linux, hardware security, API design, threat modelling.

**Format:** **Long-form article**

**Confidence: 0.98.**

---
