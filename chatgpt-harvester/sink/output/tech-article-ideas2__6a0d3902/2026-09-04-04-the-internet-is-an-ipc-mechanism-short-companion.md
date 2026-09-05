---
date: 2026-09-04
item_number: 4
title: "**“The Internet Is an IPC Mechanism”** — Short companion"
summary: The German wiki incident exposes a wonderfully simple systems principle.
angle: "If two isolated processes can both:"
interests:
  - Linux sandboxing
  - agent security
  - networking
  - capability systems
format: Short post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 4. **“The Internet Is an IPC Mechanism”** — Short companion


The German wiki incident exposes a wonderfully simple systems principle. 

**Angle:** If two isolated processes can both:

`write URL X`

and:

`read URL X`,

then they have IPC.

It doesn't matter whether your architecture diagram contains an arrow between them.

That's worth remembering when designing agent sandboxes:

`HTTPS egress`

isn't merely:

> access to websites.

It's potentially:

`storage`

`messaging`

`coordination`

`command-and-control`

`exfiltration`.

So network policy should be treated as part of the **agent communication model**, not merely perimeter security.

**Matches:** Linux sandboxing, agent security, networking, capability systems.

**Format:** **Short post**

**Confidence: 0.99.**

---
