---
date: 2026-09-02
item_number: 4
title: Backpressure Works Better When the Protocol Can Express It
summary: "RangeStream also replaces a somewhat artificial request/response model:"
angle: Streaming is often sold as a latency optimisation.
interests:
  - distributed systems
  - Python iterators
  - networking
  - etcd
  - APIs
format: Short post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 4. Backpressure Works Better When the Protocol Can Express It


RangeStream also replaces a somewhat artificial request/response model:

`request`

→ `construct enormous answer`

→ `send enormous answer`

with:

`request`

→ `produce chunk`

→ `consume chunk`

→ `produce next chunk`. 

**Angle:** Streaming is often sold as a latency optimisation.

Its more important property can be **resource coupling**.

The consumer's ability to receive data constrains how much the producer needs to materialise.

That's the essence of backpressure.

You see the same benefit in:

`Unix pipes`

`TCP windows`

`reactive streams`

`iterators`

`database cursors`

`object-store multipart operations`.

Sometimes streaming isn't about making the first byte arrive sooner.

It's about making **the entire operation possible without constructing the universe in RAM first**.

**Matches:** distributed systems, Python iterators, networking, etcd, APIs.

**Format:** **Short post**

**Confidence: 0.99.**

---
