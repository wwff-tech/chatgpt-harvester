---
date: 2026-08-16
item_number: 1
title: Your AI Cache Is Shared Mutable State. Treat It Like It.
summary: "USENIX researchers have demonstrated **HijackKV**, an attack against position-independent LLM KV-cache reuse. These optimisations reuse cached computation when identical text appears in different requests; the problem is that the cached representation encodes the *context in which that text was originally processed*. An attacker can therefore poison a benign-looking reusable chunk so a later victim inherits attacker-controlled behaviour even though no malicious text appears in the victim's input. The paper reports a 94% average one-shot success rate."
angle: "Ignore the AI-specific terminology initially. This is a classic systems failure:"
interests:
  - caching
  - LLM infrastructure
  - distributed systems
  - multi-tenancy
  - security architecture
format: Long-form
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 1. Your AI Cache Is Shared Mutable State. Treat It Like It.


USENIX researchers have demonstrated **HijackKV**, an attack against position-independent LLM KV-cache reuse. These optimisations reuse cached computation when identical text appears in different requests; the problem is that the cached representation encodes the *context in which that text was originally processed*. An attacker can therefore poison a benign-looking reusable chunk so a later victim inherits attacker-controlled behaviour even though no malicious text appears in the victim's input. The paper reports a 94% average one-shot success rate. 

**Angle:** Ignore the AI-specific terminology initially. This is a classic systems failure:

`optimisation → shared state → hidden provenance → confused consumer`

We've seen relatives of it in shared caches, deduplication, branch predictors, CDN cache poisoning, speculative execution, and connection pools.

The important design question is:

> **When is a computed artefact equivalent enough to be safely reused?**

Text equality isn't sufficient if the computation also depends on invisible context.

That opens a broader article about **cache keys as security boundaries**. If an output depends on `{input, context, identity, policy, version}`, but you key it only on `{input}`, you've created cross-context state leakage.

**Matches:** caching, LLM infrastructure, distributed systems, multi-tenancy, security architecture.

**Confidence: 0.99 — strongest technical piece tonight.**

---
