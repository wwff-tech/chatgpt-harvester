---
date: 2026-05-01
item_number: 3
title: Adaptive Rate-Limit Orchestrator
interests:
suggested_points:
conversation_id: 69e5608e-48c0-83eb-9533-b3a6d9e148c7
label: project ideas
---

## 3. Adaptive Rate-Limit Orchestrator


**Problem**  
Static rate limits fail under dynamic conditions (traffic spikes, partial outages, cascading failures).

**Approaches**
- Adjust rate limits based on system health  
- Coordinate limits across services  
- Prioritise critical traffic  

**Tech hints**
- Feedback loops from metrics (latency, error rate)  
- Token bucket variants  
- Integration with API gateways  

**Formats**
- Middleware service  
- Kubernetes controller  
- API gateway plugin  

**Why good fit**
- Strong SRE alignment  
- Immediate operational value  

**Why not**
- Risk of oscillation  
- Requires careful tuning  

**Revenue potential**
- High  

**Content potential**
- High  

**Community potential**
- Medium  

**Tags**
`rate-limiting`, `sre`, `traffic`, `resilience`

**References**
- https://stripe.com/blog/rate-limiters  
- https://envoyproxy.io/  

---
