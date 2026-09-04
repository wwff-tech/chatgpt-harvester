---
date: 2026-08-19
item_number: 1
title: Serverless Isolation Just Met the Microarchitecture
summary: "Researchers disclosed a remote Spectre attack against Cloudflare Workers today. They demonstrated extracting a JWT from a **co-located victim Worker in Cloudflare's production environment at up to 12 bits/second**, reportedly around 360× faster than the researchers' earlier 2021 technique. Cloudflare says the attack has been mitigated."
angle: This is much more interesting than “Spectre still exists”.
interests:
  - cloud isolation
  - serverless
  - CPU architecture
  - side channels
  - multi-tenancy
  - security
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 1. Serverless Isolation Just Met the Microarchitecture


Researchers disclosed a remote Spectre attack against Cloudflare Workers today. They demonstrated extracting a JWT from a **co-located victim Worker in Cloudflare's production environment at up to 12 bits/second**, reportedly around 360× faster than the researchers' earlier 2021 technique. Cloudflare says the attack has been mitigated. 

**Angle:** This is much more interesting than “Spectre still exists”.

Serverless isolation presents a particularly difficult abstraction:

`tenant A JavaScript`

`───────────────`

`tenant B JavaScript`

while underneath:

`same CPU → shared caches → predictors → speculative machinery`

Software can provide immaculate logical isolation while the processor continues sharing **physical history**.

There is a lovely systems argument here: virtualisation keeps creating increasingly convincing abstractions of dedicated computers, but microarchitectural state stubbornly refuses to respect the abstraction boundary.

The 12-bit/s rate is also a useful antidote to dismissing side channels because they are “slow”. A JWT, API key, cryptographic secret, or capability token is tiny. You don't need to exfiltrate `/var/lib/postgresql`.

**Matches:** cloud isolation, serverless, CPU architecture, side channels, multi-tenancy, security.

**Format:** **Long-form article**

**Confidence: 0.99 — strongest technical story today.**

---
