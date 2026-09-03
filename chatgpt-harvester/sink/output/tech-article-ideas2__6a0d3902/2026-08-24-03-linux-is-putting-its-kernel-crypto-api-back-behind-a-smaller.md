---
date: 2026-08-24
item_number: 3
title: Linux Is Putting Its Kernel Crypto API Back Behind a Smaller Door
summary: "Linux 7.3 further restricts **AF_ALG**, the socket interface that exposes the kernel cryptography subsystem to userspace. After zero-copy and offload functionality were removed and AF_ALG was deprecated in Linux 7.2, 7.3 adds an `af_alg_restrict` sysctl whose default exposes only an allow-list of algorithms still required by known consumers such as `iwd`. Administrators can opt back into unrestricted access or disable it entirely."
angle: This is a good example of a capability that sounds architecturally elegant but creates an awkward maintenance boundary.
interests:
  - Linux
  - cryptography
  - API design
  - attack-surface reduction
  - kernel security
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 3. Linux Is Putting Its Kernel Crypto API Back Behind a Smaller Door


Linux 7.3 further restricts **AF_ALG**, the socket interface that exposes the kernel cryptography subsystem to userspace. After zero-copy and offload functionality were removed and AF_ALG was deprecated in Linux 7.2, 7.3 adds an `af_alg_restrict` sysctl whose default exposes only an allow-list of algorithms still required by known consumers such as `iwd`. Administrators can opt back into unrestricted access or disable it entirely. 

**Angle:** This is a good example of a capability that sounds architecturally elegant but creates an awkward maintenance boundary.

The kernel already has cryptographic implementations, so:

> Why duplicate them in userspace?

sounds sensible.

But exposing an internal subsystem externally converts implementation into **supported attack surface**.

The important transition is:

`kernel has capability X`

therefore not necessarily:

`userspace should have generic access to X`.

AF_ALG's history makes a useful article about **capability minimisation through interface design**. Once you expose a general interface, every internal algorithm potentially acquires external callers, compatibility obligations, security consequences, and maintenance costs.

Linux's response is interesting because it isn't binary removal. It is effectively:

`known-needed subset → default`

`everything → explicit opt-in`.

That's the principle of least privilege applied to an API surface.

**Matches:** Linux, cryptography, API design, attack-surface reduction, kernel security.

**Format:** **Long-form article**

**Confidence: 0.99.**

---
