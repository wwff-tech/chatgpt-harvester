---
date: 2026-08-21
item_number: 9
title: Left-field — “Sometimes the Fastest Network Is No Network at All”
summary: "USB4STREAM raises a broader architectural question. We routinely reach for TCP/IP because it is ubiquitous, interoperable, routable, observable, and extraordinarily well engineered. But those properties carry costs that aren't always useful for a point-to-point relationship."
angle: "If the actual topology is permanently:"
interests:
  - networking
  - Linux
  - retrocomputing
  - distributed systems
  - homelab
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 9. Left-field — “Sometimes the Fastest Network Is No Network at All”


USB4STREAM raises a broader architectural question. We routinely reach for TCP/IP because it is ubiquitous, interoperable, routable, observable, and extraordinarily well engineered. But those properties carry costs that aren't always useful for a point-to-point relationship. 

**Angle:** If the actual topology is permanently:

`A ↔ B`

why necessarily build:

`application`

`TCP`

`IP`

`network interface`

`virtual/physical network`

`IP`

`TCP`

`application`?

Raw transports have obvious downsides: custom framing, flow control, error handling, authentication, debugging, and reduced interoperability. **Those are substantial; TCP earned its popularity.**

But USB4STREAM makes the trade-off experimentally accessible on commodity hardware.

There's a nice historical progression:

`RS-232 null modem`

→ `parallel link`

→ `FireWire`

→ `InfiniBand/RDMA`

→ `Thunderbolt/USB4 raw streams`.

Sometimes the correct network for two machines is still just **a wire between two machines**.

**Matches:** networking, Linux, retrocomputing, distributed systems, homelab.

**Format:** **Long-form article**

**Confidence: 0.97.**

---
