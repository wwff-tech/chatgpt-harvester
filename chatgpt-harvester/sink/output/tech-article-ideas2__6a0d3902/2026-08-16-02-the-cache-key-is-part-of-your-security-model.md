---
date: 2026-08-16
item_number: 2
title: The Cache Key Is Part of Your Security Model
summary: HijackKV generalises beautifully beyond LLMs.
angle: "A cache key is effectively an assertion:"
interests:
  - CDN/caching
  - HTTP
  - multi-tenancy
  - security
  - API architecture
format: Short post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 2. The Cache Key Is Part of Your Security Model


HijackKV generalises beautifully beyond LLMs. 

**Angle:** A cache key is effectively an assertion:

> These two requests are equivalent for the purpose of reusing this result.

If the assertion omits a security-relevant dimension, isolation disappears.

Classic examples include:

`URL` without `Authorization`

`query` without `tenant_id`

`rendered page` without `locale/permissions`

and now:

`token chunk` without its originating context.

A useful rule of thumb:

**Every cache key is a miniature threat model.**

**Matches:** CDN/caching, HTTP, multi-tenancy, security, API architecture.

**Format:** **Short post**

**Confidence: 0.99.**

---
