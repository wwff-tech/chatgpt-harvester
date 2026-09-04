---
date: 2026-08-11
item_number: 1
title: Ransomware Has Discovered High Availability
summary: "Microsoft Threat Intelligence published a fresh technical analysis on 10 August of **DeadLock**, a Rust-based ransomware operation whose recovery infrastructure combines the Session decentralised messaging network with blockchain-backed services. Earlier analysis found it using Polygon smart contracts to dynamically distribute proxy addresses, making conventional infrastructure disruption substantially harder."
angle: "Don't make this primarily a ransomware article. Make it a **distributed-systems article where the system happens to be malicious**."
interests:
  - distributed systems
  - reliability engineering
  - decentralisation
  - threat modelling
  - security architecture
format: Long-form
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 1. Ransomware Has Discovered High Availability


Microsoft Threat Intelligence published a fresh technical analysis on 10 August of **DeadLock**, a Rust-based ransomware operation whose recovery infrastructure combines the Session decentralised messaging network with blockchain-backed services. Earlier analysis found it using Polygon smart contracts to dynamically distribute proxy addresses, making conventional infrastructure disruption substantially harder. 

**Angle:** Don't make this primarily a ransomware article. Make it a **distributed-systems article where the system happens to be malicious**.

Attackers have independently arrived at many of the same architectural requirements we value in production:

`no SPOF → replaceable endpoints → replicated state → censorship resistance → service discovery → encrypted messaging → graceful infrastructure loss`

The uncomfortable observation is that good architecture is morally neutral. The same properties that make IPFS, Matrix, Tor, service discovery, and distributed control planes resilient also make adversarial infrastructure resilient.

A particularly interesting section could compare defender and attacker SLOs. The attacker doesn't need five-nines availability; they merely need their control/recovery plane to remain *eventually reachable*. That radically changes the economics.

**Matches:** distributed systems, reliability engineering, decentralisation, threat modelling, security architecture.

**Confidence: 0.97.**

---
