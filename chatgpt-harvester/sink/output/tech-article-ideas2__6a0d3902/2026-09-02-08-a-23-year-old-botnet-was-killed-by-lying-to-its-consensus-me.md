---
date: 2026-09-02
item_number: 8
title: "**“A 23-Year-Old Botnet Was Killed by Lying to Its Consensus Mechanism”** — Long-form / left-field"
summary: "The **Sality** botnet, first seen in 2003, has finally been disrupted. Its decentralised P2P architecture helped it survive for more than two decades, but peers blindly trusted network membership information without authentication. CrowdStrike exploited that behaviour to manipulate peer lists, progressively removing attacker-controlled super-peers and inserting sinkholes until infected machines became isolated from their controller."
angle: This is far more interesting as a distributed-systems story than malware news.
interests:
  - distributed systems
  - networking
  - security protocols
  - botnets
  - consensus/gossip
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 8. **“A 23-Year-Old Botnet Was Killed by Lying to Its Consensus Mechanism”** — Long-form / left-field


The **Sality** botnet, first seen in 2003, has finally been disrupted. Its decentralised P2P architecture helped it survive for more than two decades, but peers blindly trusted network membership information without authentication. CrowdStrike exploited that behaviour to manipulate peer lists, progressively removing attacker-controlled super-peers and inserting sinkholes until infected machines became isolated from their controller. 

**Angle:** This is far more interesting as a distributed-systems story than malware news.

Sality gained resilience by eliminating:

`central command server`.

But decentralisation created another requirement:

> How does a peer know another peer is legitimate?

Apparently, not well enough.

The property that made takedown difficult:

`distributed membership`

also created the mechanism ultimately used to destroy it:

`distributed membership poisoning`.

There is a beautiful broader lesson:

> **Removing the central authority does not remove trust. It moves trust into the protocol.**

That applies to:

`P2P systems`

`service discovery`

`gossip protocols`

`blockchains`

`federation`

`mesh networking`.

Decentralised systems still need authenticated membership, or an attacker can become the topology.

**Matches:** distributed systems, networking, security protocols, botnets, consensus/gossip.

**Format:** **Long-form article**

**Confidence: 0.99 — excellent left-field piece.**

---
