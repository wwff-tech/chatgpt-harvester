---
date: 2026-08-18
item_number: 5
title: "**“NASA Ground Control Had an Authentication Function That Didn't Authenticate”** — Short post / security article"
summary: "Fresh reporting today highlights **CVE-2026-60112** in NASA's open-source AMMOS Instrument Toolkit GUI. The underlying advisory was published on 29 July: versions before 2.5.1 allowed an unauthenticated network client to obtain a valid session and then pass arbitrary commands to the AIT command bus. The flaw carries a 9.8 CVSS v3.1 score."
angle: The spacecraft angle is fun, but the architecture is more instructive.
interests:
  - API security
  - distributed systems
  - authentication
  - command-and-control systems
  - space infrastructure
format: "**Short post**, or a longer piece on authentication invariants."
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 5. **“NASA Ground Control Had an Authentication Function That Didn't Authenticate”** — Short post / security article


Fresh reporting today highlights **CVE-2026-60112** in NASA's open-source AMMOS Instrument Toolkit GUI. The underlying advisory was published on 29 July: versions before 2.5.1 allowed an unauthenticated network client to obtain a valid session and then pass arbitrary commands to the AIT command bus. The flaw carries a 9.8 CVSS v3.1 score. 

**Angle:** The spacecraft angle is fun, but the architecture is more instructive.

Apparently:

`create session`

did not establish identity, while:

`send command(session)`

trusted the existence of that session.

That's a classic case of confusing:

`session establishment`

with:

`authentication`.

It generalises beautifully to cookies, WebSockets, API tokens, agent sessions, message queues, and internal service identities.

**A session is state, not proof of identity.**

I'd resist sensationalising this into “hackers can command NASA spacecraft”; exploitability depends on deployment and network exposure. The software flaw itself is enough.

**Matches:** API security, distributed systems, authentication, command-and-control systems, space infrastructure.

**Format:** **Short post**, or a longer piece on authentication invariants.

**Confidence: 0.98 on the vulnerability mechanics; substantially lower on claims about actual reachable spacecraft, which I would omit.**

---
