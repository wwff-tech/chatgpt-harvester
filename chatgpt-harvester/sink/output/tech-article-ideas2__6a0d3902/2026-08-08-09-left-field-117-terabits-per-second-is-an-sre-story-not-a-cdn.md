---
date: 2026-08-08
item_number: 9
title: Left-field — “117 Terabits per Second Is an SRE Story, Not a CDN Benchmark”
summary: "AWS says CloudFront peaked above **117 Tbps** while serving World Cup traffic when Spain scored in extra time during the 19 July final. The interesting characteristic is synchronisation: millions of humans react to the same event simultaneously, creating correlated rather than statistically independent demand."
angle: "Use live sport as a vehicle for explaining **coordinated omission in capacity planning**. Autoscaling models often assume demand rises; real events produce discontinuities. Goals, election results, software releases, emergency alerts, and celebrity deaths are effectively distributed barrier synchronisations executed by humans."
interests:
  - CDN
  - HAProxy
  - caching
  - SRE
  - queueing theory
  - distributed systems
format: Long-form
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

## 9. Left-field — “117 Terabits per Second Is an SRE Story, Not a CDN Benchmark”


AWS says CloudFront peaked above **117 Tbps** while serving World Cup traffic when Spain scored in extra time during the 19 July final. The interesting characteristic is synchronisation: millions of humans react to the same event simultaneously, creating correlated rather than statistically independent demand. 

**Angle:** Use live sport as a vehicle for explaining **coordinated omission in capacity planning**. Autoscaling models often assume demand rises; real events produce discontinuities. Goals, election results, software releases, emergency alerts, and celebrity deaths are effectively distributed barrier synchronisations executed by humans.

That could become a very good essay: *“Humans Are the World's Largest Distributed System, and Sometimes They All `wake()` at Once.”*

**Matches:** CDN, HAProxy, caching, SRE, queueing theory, distributed systems.

**Confidence: 0.92.**

---
