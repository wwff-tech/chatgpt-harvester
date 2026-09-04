---
date: 2026-09-03
item_number: 9
title: "**Left-field — “Compression Is Sometimes Cheaper Than Buying More Disks”** — Long-form / systems short"
summary: "Cloudflare's cache-transcoding experiment stores eligible cached responses internally using Zstandard, then decompresses them before serving. In controlled testing, eligible assets shrank by roughly **2.8×**; Cloudflare estimates the architecture could trade a few percent more CPU for **petabytes of effective cache capacity** plus lower inter-datacentre bandwidth."
angle: The interesting thing is the economics of asymmetric work.
interests:
  - caching
  - CDNs
  - performance engineering
  - storage
  - compression
  - distributed systems
format: "**Long-form technical article** or substantial short."
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 9. **Left-field — “Compression Is Sometimes Cheaper Than Buying More Disks”** — Long-form / systems short


Cloudflare's cache-transcoding experiment stores eligible cached responses internally using Zstandard, then decompresses them before serving. In controlled testing, eligible assets shrank by roughly **2.8×**; Cloudflare estimates the architecture could trade a few percent more CPU for **petabytes of effective cache capacity** plus lower inter-datacentre bandwidth. 

**Angle:** The interesting thing is the economics of asymmetric work.

Compression costs:

`once per cache fill`.

Storage savings persist:

`for lifetime of object`.

Bandwidth savings occur:

`every cache-tier transfer`.

Decompression costs:

`every serve`.

So the decision isn't:

> Is compression expensive?

It's:

\[
Benefit =
(StorageSaved \times Lifetime)
+
(NetworkSaved \times Transfers)
-
CPUCost
\]

Cloudflare even found that compressing only hot objects wasn't optimal; a simple eligibility threshold captured most of the storage benefit without materially fixing the decode cost. 

This is exactly the sort of optimisation where infrastructure economics beat intuition.

**Matches:** caching, CDNs, performance engineering, storage, compression, distributed systems.

**Format:** **Long-form technical article** or substantial short.

**Confidence: 0.99 on the prototype measurements; production economics remain experimental.**

---
