---
date: 2026-04-19
item_number: 5
title: Signed Event Bus for Small Systems
interests:
suggested_points:
conversation_id: 69e5608e-48c0-83eb-9533-b3a6d9e148c7
label: project ideas
---

## 5. Signed Event Bus for Small Systems


**Problem**  
Most small systems lack trustable event pipelines. Webhooks are unauthenticated or weakly verified.

**Approaches**
- CloudEvents + signature envelope standard
- Lightweight broker (RabbitMQ/MQTT)
- Optional federation between nodes

**Tech hints**
- Python + FastAPI
- RabbitMQ / NATS
- Ed25519 signing
- JSON canonicalisation

**Formats**
- Library + reference service
- CLI tools for signing/verification

**Why good fit**
- Direct overlap with your CloudEvents + provenance thinking
- Could underpin multiple other tools

**Why not**
- Feels “infrastructure-y” (harder to sell)
- Needs adoption to matter

**Revenue potential**
- Low → Medium (unless wrapped into product)

**Content potential**
- Very high (fits your book + patterns work)

**Community potential**
- High among infra nerds

**Tags**
`cloudevents`, `signing`, `event-driven`, `security`

**References**
- https://cloudevents.io  
- https://github.com/sigstore  

---
