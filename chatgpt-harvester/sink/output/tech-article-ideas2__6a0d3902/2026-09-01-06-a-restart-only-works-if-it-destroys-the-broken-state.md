---
date: 2026-09-01
item_number: 6
title: A Restart Only Works If It Destroys the Broken State
summary: "Intel's GPU work provides an unusually physical demonstration of a general SRE rule."
angle: Why does restarting software work?
interests:
  - SRE
  - auto-remediation
  - state machines
  - Linux
  - hardware
format: Short post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 6. A Restart Only Works If It Destroys the Broken State


Intel's GPU work provides an unusually physical demonstration of a general SRE rule. 

**Angle:** Why does restarting software work?

Not because restart is magic.

It works because:

`broken state`

is usually stored inside:

`process memory / connection state / transient resources`

and restart destroys it.

If the broken state lives in:

`GPU firmware`

`NIC`

`BMC`

`database`

`external queue`

`remote dependency`

then restarting the application may accomplish nothing.

So before putting:

`restart service`

into an auto-remediation rule, ask:

> **Where does the failure state actually live, and does this action destroy it?**

That's a much better basis for remediation than “restarts usually fix this”.

**Matches:** SRE, auto-remediation, state machines, Linux, hardware.

**Format:** **Short post**

**Confidence: 0.99.**

---
