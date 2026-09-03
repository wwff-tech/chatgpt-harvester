---
date: 2026-08-21
item_number: 1
title: "**“Thunderbolt Just Became a 40 Gbit/s Null-Modem Cable”** — Long-form / experimental article"
summary: "Linux 7.2 includes **USB4STREAM**, exposing host-to-host USB4 connections through `/dev/tbstreamX`. Applications can use ordinary `read()` and `write()` operations to move raw data directly between two connected systems without first constructing an IP network between them."
angle: "Forget file transfer. This is interesting because it gives commodity machines a **high-bandwidth, low-friction point-to-point fabric using a port many already have**."
interests:
  - Linux
  - homelab
  - mini-PCs
  - networking
  - distributed systems
  - local AI
format: Long-form after benchmarking
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 1. **“Thunderbolt Just Became a 40 Gbit/s Null-Modem Cable”** — Long-form / experimental article


Linux 7.2 includes **USB4STREAM**, exposing host-to-host USB4 connections through `/dev/tbstreamX`. Applications can use ordinary `read()` and `write()` operations to move raw data directly between two connected systems without first constructing an IP network between them. 

There is already community interest in applying it to distributed inference, including llama.cpp RPC-style workloads, although I found no mature implementation doing that yet. 

**Angle:** Forget file transfer. This is interesting because it gives commodity machines a **high-bandwidth, low-friction point-to-point fabric using a port many already have**.

Conceptually:

`machine A → /dev/tbstream0 → USB4 cable → /dev/tbstream0 → machine B`

That invites experiments with:

- distributed LLM inference,
- zero-copy transport,
- VM migration,
- replicated storage,
- fast backups,
- shared-memory-ish protocols,
- camera/instrument acquisition,
- ad-hoc two-node clusters.

The obvious article is empirical: compare USB4STREAM with Thunderbolt networking and 10 GbE for throughput, latency, CPU utilisation, small-message performance, and zero-copy possibilities.

For homelab use, the particularly interesting question is whether **two memory-rich mini-PCs connected by one cable become a useful poor man's inference cluster** without NICs, switches, or spare PCIe slots.

**Matches:** Linux, homelab, mini-PCs, networking, distributed systems, local AI.

**Format:** **Long-form after benchmarking**

**Confidence: 0.99 on the kernel feature; 0.75 that it materially improves distributed inference without runtime work.**

---
