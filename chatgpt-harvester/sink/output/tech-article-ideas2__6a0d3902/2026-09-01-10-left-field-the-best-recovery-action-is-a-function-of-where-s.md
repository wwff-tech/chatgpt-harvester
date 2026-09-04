---
date: 2026-09-01
item_number: 10
title: Left-field — “The Best Recovery Action Is a Function of Where State Lives”
summary: "Intel's cold-reset work gives this a concrete hardware hook, but the idea generalises much further."
angle: "Model a failure as corrupt or undesirable state located at some layer:"
interests:
  - SRE
  - automated remediation
  - state machines
  - control theory
  - hardware reliability
  - Kubernetes
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 10. Left-field — “The Best Recovery Action Is a Function of Where State Lives”


Intel's cold-reset work gives this a concrete hardware hook, but the idea generalises much further. 

**Angle:** Model a failure as corrupt or undesirable state located at some layer:

`request`

`process`

`container`

`kernel driver`

`device`

`host`

`cluster`

`external dependency`.

Then choose a recovery action whose **destruction boundary contains that state**:

\[
RecoveryBoundary \supseteq FailureState
\]

but preferably not much more.

If a connection is broken:

`reconnect`.

If process state is broken:

`restart process`.

If GPU state is broken:

`reset GPU`.

If kernel state is broken:

`reboot host`.

If persisted application state is broken:

`restore/repair data`.

Too-small recovery boundaries don't fix the fault.

Too-large ones create unnecessary blast radius.

That gives auto-remediation systems a much stronger conceptual model than a bag of recipes like:

`if error X → restart pod`.

**Matches:** SRE, automated remediation, state machines, control theory, hardware reliability, Kubernetes.

**Format:** **Long-form article**

**Confidence: 0.99 — strongest evergreen systems idea today.**
