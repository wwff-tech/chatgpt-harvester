---
date: 2026-08-08
item_number: 5
title: "`kubectl logs` Shouldn't Be Able to Read `/etc/shadow`"
summary: "Another containerd issue, CVE-2026-53489, involved CRI checkpoint restoration accepting a symlinked `container.log`; under the affected conditions this could expose an arbitrary host file through `kubectl logs`. It is fixed in containerd 2.1.9, 2.2.5, and 2.3.2. Interestingly, several teams independently found it, including GKE Security using Gemini and Anthropic researchers using Claude."
angle: There are actually two posts here. The immediate one is about seemingly innocuous observability interfaces crossing privilege boundaries. The second is evidence for AI-assisted security discovery without needing another speculative “AI will find all the bugs” piece.
interests:
  - Kubernetes
  - Linux
  - container security
  - observability
  - AI-assisted engineering
format: Short post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

## 5. `kubectl logs` Shouldn't Be Able to Read `/etc/shadow`


Another containerd issue, CVE-2026-53489, involved CRI checkpoint restoration accepting a symlinked `container.log`; under the affected conditions this could expose an arbitrary host file through `kubectl logs`. It is fixed in containerd 2.1.9, 2.2.5, and 2.3.2. Interestingly, several teams independently found it, including GKE Security using Gemini and Anthropic researchers using Claude. 

**Angle:** There are actually two posts here. The immediate one is about seemingly innocuous observability interfaces crossing privilege boundaries. The second is evidence for AI-assisted security discovery without needing another speculative “AI will find all the bugs” piece.

**Matches:** Kubernetes, Linux, container security, observability, AI-assisted engineering.

**Confidence: 0.95.**

---
