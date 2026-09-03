---
date: 2026-08-23
item_number: 8
title: "**“Open-Source Radio Links Are Quietly Doing Ridiculous Things”** — Short technical post"
summary: "A current hardware project is documenting home-built **ExpressLRS receivers**, including the engineering that lets low-power 2.4 GHz links achieve extremely long control ranges. ExpressLRS uses LoRa-derived chirp spread spectrum techniques rather than conventional Wi-Fi-style modulation, trading throughput for link budget and robustness."
angle: Avoid the drone framing and explain the engineering trade.
interests:
  - embedded electronics
  - RF
  - ESP32-adjacent work
  - telemetry
  - drones
format: Short technical post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 8. **“Open-Source Radio Links Are Quietly Doing Ridiculous Things”** — Short technical post


A current hardware project is documenting home-built **ExpressLRS receivers**, including the engineering that lets low-power 2.4 GHz links achieve extremely long control ranges. ExpressLRS uses LoRa-derived chirp spread spectrum techniques rather than conventional Wi-Fi-style modulation, trading throughput for link budget and robustness. 

**Angle:** Avoid the drone framing and explain the engineering trade.

Wireless systems live inside something like:

`bandwidth ↔ SNR ↔ symbol rate ↔ processing gain ↔ latency ↔ range`.

Wi-Fi optimises heavily towards bandwidth.

ELRS asks:

> What if the payload is tiny and losing the link is much worse than waiting another few milliseconds?

Suddenly tens of bytes of control data can travel astonishing distances on sub-watt transmitters.

That is a useful practical introduction to **processing gain and link-budget engineering**, with obvious LoRa, telemetry, embedded, and sensor-network comparisons.

**Matches:** embedded electronics, RF, ESP32-adjacent work, telemetry, drones.

**Format:** **Short technical post**

**Confidence: 0.91 — left-field, but technically rich.**

---
