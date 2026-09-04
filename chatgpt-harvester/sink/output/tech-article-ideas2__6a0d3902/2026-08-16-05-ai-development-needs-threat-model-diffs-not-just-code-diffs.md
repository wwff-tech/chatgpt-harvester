---
date: 2026-08-16
item_number: 5
title: AI Development Needs Threat-Model Diffs, Not Just Code Diffs
summary: "A USENIX Enigma session proposes continuously deriving threat models from source, infrastructure, and configuration, then comparing the resulting models over time. The key observation is excellent: AI-assisted development can alter **trust boundaries, privilege relationships, attack surfaces, and data flows without introducing anything a conventional vulnerability scanner recognises as a bug**."
angle: This connects strongly with the declared/permitted/observed architecture idea from the 14 August scan.
interests:
  - GitOps
  - Terraform
  - agentic engineering
  - threat modelling
  - platform security
  - CI/CD
format: Long-form
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 5. AI Development Needs Threat-Model Diffs, Not Just Code Diffs


A USENIX Enigma session proposes continuously deriving threat models from source, infrastructure, and configuration, then comparing the resulting models over time. The key observation is excellent: AI-assisted development can alter **trust boundaries, privilege relationships, attack surfaces, and data flows without introducing anything a conventional vulnerability scanner recognises as a bug**. 

**Angle:** This connects strongly with the declared/permitted/observed architecture idea from the 14 August scan.

A PR might say:

```text
+ service B can call service C
```

and every individual line can be perfectly valid.

But the architectural diff is:

```text
BEFORE:
internet → A → B

AFTER:
internet → A → B → production-secrets
```

Nothing is “vulnerable”. The **security posture changed**.

That suggests CI should eventually produce artefacts alongside ordinary diffs:

`code diff`

`infrastructure diff`

`authority diff`

`threat-model diff`

`runtime-policy diff`

The last three are arguably far more useful to a reviewer of agent-generated infrastructure than another thousand lines of Terraform.

**Matches:** GitOps, Terraform, agentic engineering, threat modelling, platform security, CI/CD.

**Confidence: 0.98 — excellent article/tool idea.**

---
