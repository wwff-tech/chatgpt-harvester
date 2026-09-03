---
date: 2026-08-13
item_number: 5
title: "**“The £5 Microcontroller Is Becoming a Tiny Linux-Class Network Appliance”** — Long-form / hardware post"
summary: "WCH's new **CH32V407/467** family combines a 200 MHz RISC-V MCU with integrated **10/100 Ethernet MAC and PHY**, high-speed 480 Mbps USB 2.0 PHY, and — on the CH32V467 — as much as **8 MB of on-chip PSRAM**. Reporting on the parts appeared today."
angle: "The Ethernet **PHY** is what caught my attention."
interests:
  - embedded electronics
  - PlatformIO
  - RISC-V
  - networking
  - ESP32-class devices
format: "**Long-form article** if benchmarked experimentally; otherwise a **short technical post**."
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 5. **“The £5 Microcontroller Is Becoming a Tiny Linux-Class Network Appliance”** — Long-form / hardware post


WCH's new **CH32V407/467** family combines a 200 MHz RISC-V MCU with integrated **10/100 Ethernet MAC and PHY**, high-speed 480 Mbps USB 2.0 PHY, and — on the CH32V467 — as much as **8 MB of on-chip PSRAM**. Reporting on the parts appeared today. 

**Angle:** The Ethernet **PHY** is what caught my attention.

Microcontrollers have had Ethernet MACs forever, but needing an external PHY adds BOM cost, board area, routing, magnetics decisions, and another component to source. Integrating it changes what counts as a trivial networked device.

Likewise, 8 MB of PSRAM radically changes the software envelope compared with the tens or hundreds of kilobytes historically associated with MCUs.

We're approaching a curious overlap:

`high-end MCU ↔ low-end application processor`

The MCU retains deterministic startup, simple firmware deployment, and low overhead, while acquiring enough memory and networking to run increasingly sophisticated services.

**Matches:** embedded electronics, PlatformIO, RISC-V, networking, ESP32-class devices.

**Format:** **Long-form article** if benchmarked experimentally; otherwise a **short technical post**.

**Confidence: 0.94 on the specifications reported; I'd verify WCH's primary datasheet before publishing electrical or production-design advice.**

---
