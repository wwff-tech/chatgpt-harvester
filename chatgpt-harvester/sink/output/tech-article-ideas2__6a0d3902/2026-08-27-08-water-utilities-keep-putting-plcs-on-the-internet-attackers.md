---
date: 2026-08-27
item_number: 8
title: "**“Water Utilities Keep Putting PLCs on the Internet. Attackers Keep Finding Them.”** — Short / medium article"
summary: "Fresh reporting today puts the scale of July's campaign against US water and wastewater infrastructure at **more than 100 targeted Internet-exposed systems**. The activity frequently involved exposed PLCs and follows the Siemens S7 warnings covered last week. Importantly, “targeted” does not mean all 100 were successfully compromised."
angle: "Don't write “critical infrastructure cybersecurity is bad”. We know."
interests:
  - embedded systems
  - networking
  - OT/ICS
  - zero trust
  - capability security
format: Short/medium article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 8. **“Water Utilities Keep Putting PLCs on the Internet. Attackers Keep Finding Them.”** — Short / medium article


Fresh reporting today puts the scale of July's campaign against US water and wastewater infrastructure at **more than 100 targeted Internet-exposed systems**. The activity frequently involved exposed PLCs and follows the Siemens S7 warnings covered last week. Importantly, “targeted” does not mean all 100 were successfully compromised. 

**Angle:** Don't write “critical infrastructure cybersecurity is bad”. We know.

The more useful question is:

> **Why does a PLC need globally routable reachability at all?**

Operational technology often accumulated remote access organically:

`vendor support`

`remote engineering`

`telemetry`

`pandemic-era remote working`

`temporary maintenance`.

Each individually sounds reasonable.

The resulting topology:

`Internet → engineering interface → physical process`

is not.

There is a good architecture piece in treating remote OT access as an **explicit temporary capability**:

`identity-aware access`

→ `broker/jump host`

→ `time-limited authorisation`

→ `specific device`

→ `specific operations`

with the PLC itself never directly Internet-reachable.

**Matches:** embedded systems, networking, OT/ICS, zero trust, capability security.

**Format:** **Short/medium article**

**Confidence: 0.97.**

---
