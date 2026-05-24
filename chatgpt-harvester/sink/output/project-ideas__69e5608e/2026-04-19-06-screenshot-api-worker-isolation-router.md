---
date: 2026-04-19
item_number: 6
title: Screenshot/API Worker Isolation Router
interests:
suggested_points:
conversation_id: 69e5608e-48c0-83eb-9533-b3a6d9e148c7
label: project ideas
---

## 6. Screenshot/API Worker Isolation Router


(Directly useful for your current product)

**Problem**  
Free vs paid workloads, noisy neighbours, and security isolation for browser workers.

**Approaches**
- Queue routing (RabbitMQ) by tier
- Worker pools per trust level
- Optional “dedicated worker” scheduling

**Tech hints**
- RabbitMQ (routing keys)
- Playwright workers
- Podman/gVisor isolation
- Redis for rate limiting

**Formats**
- Internal service
- Eventually exposed as config in your API

**Why good fit**
- Immediate ROI for your current launch
- Evolves into a differentiator (“dedicated rendering workers”)

**Why not**
- Not very novel
- Mostly engineering effort, less “idea”

**Revenue potential**
- High (direct monetisation lever)

**Content potential**
- Medium

**Community potential**
- Low (specific use case)

**Tags**
`screenshot-api`, `queueing`, `isolation`, `playwright`

**References**
- https://www.rabbitmq.com/tutorials  
- https://playwright.dev  

---
