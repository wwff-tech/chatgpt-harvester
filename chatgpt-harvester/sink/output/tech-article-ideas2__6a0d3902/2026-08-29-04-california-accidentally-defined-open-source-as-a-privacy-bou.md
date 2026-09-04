---
date: 2026-08-29
item_number: 4
title: California Accidentally Defined Open Source as a Privacy Boundary
summary: "California's legislature has passed **AB 1856**, amending the state's Digital Age Assurance Act before it takes effect on **1 January 2027**. The amended definition excludes operating-system providers distributing software under licences permitting recipients to **copy, redistribute, and modify it**, effectively exempting distributions such as Debian, Fedora, Ubuntu, Arch, and the BSDs from the OS-level age-signal requirement. The bill is now awaiting the governor's action."
angle: "The interesting bit isn't Californian politics. It is **why the original architecture didn't map cleanly onto open source**."
interests:
  - Linux
  - Debian
  - privacy
  - open source
  - decentralised systems
  - software regulation
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 4. California Accidentally Defined Open Source as a Privacy Boundary


California's legislature has passed **AB 1856**, amending the state's Digital Age Assurance Act before it takes effect on **1 January 2027**. The amended definition excludes operating-system providers distributing software under licences permitting recipients to **copy, redistribute, and modify it**, effectively exempting distributions such as Debian, Fedora, Ubuntu, Arch, and the BSDs from the OS-level age-signal requirement. The bill is now awaiting the governor's action. 

**Angle:** The interesting bit isn't Californian politics. It is **why the original architecture didn't map cleanly onto open source**.

The law implicitly assumed:

`device`

→ `operating-system vendor`

→ `vendor account`

→ `known user`

→ `age signal`

→ `application store`.

That architecture approximately describes:

`Apple / Google / Microsoft`.

It does not describe:

`Debian mirror`

→ `ISO`

→ `user`

→ `apt repositories`

→ `arbitrary software`.

There may be no central organisation possessing either the identity relationship or technical control required to produce the signal.

So this is an unusually concrete example of regulation accidentally encoding **a particular software architecture as though it were universal**.

I'd be careful with the headline: the bill's exemption is licence-based rather than a philosophical declaration that open source is inherently private. But the architectural contrast is genuinely useful.

**Matches:** Linux, Debian, privacy, open source, decentralised systems, software regulation.

**Format:** **Long-form article**

**Confidence: 0.97.**

---
