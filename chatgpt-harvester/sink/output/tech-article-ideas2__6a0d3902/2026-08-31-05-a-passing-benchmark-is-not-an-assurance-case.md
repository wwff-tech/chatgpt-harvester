---
date: 2026-08-31
item_number: 5
title: A Passing Benchmark Is Not an Assurance Case
summary: "A new evidence-centred survey of LLMs in software engineering and software security argues that current evaluations repeatedly conflate different properties: functional correctness, security, operational reliability, evidence provenance, and the authority granted to an agent. It highlights weak test oracles, data leakage, changing harnesses, proxy security metrics, and poorly reported human intervention as recurring validity problems."
angle: "A benchmark tells you:"
interests:
  - agent evaluation
  - software assurance
  - security
  - formal methods
  - agent governance
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 5. A Passing Benchmark Is Not an Assurance Case


A new evidence-centred survey of LLMs in software engineering and software security argues that current evaluations repeatedly conflate different properties: functional correctness, security, operational reliability, evidence provenance, and the authority granted to an agent. It highlights weak test oracles, data leakage, changing harnesses, proxy security metrics, and poorly reported human intervention as recurring validity problems. 

Evidence-Centred Survey of LLM Software Engineering and Security

**Angle:** A benchmark tells you:

`system passed test X under conditions Y`.

Deployment requires a much larger claim:

`system is sufficiently trustworthy for authority Z`.

Those are radically different.

I'd borrow the **assurance case** concept from safety engineering:

```text
Claim:
Agent may safely modify production Terraform.

Evidence:
- functional evaluation
- security-policy evaluation
- sandbox escape testing
- tool-authority analysis
- regression testing
- provenance
- human-review measurements
```

No single benchmark proves the claim.

This is particularly important because an agent that scores 95% while only editing a disposable branch and an agent scoring 95% while holding AWS administrator credentials are **not equivalent systems**.

Capability should increasingly be reported alongside **authority**.

**Matches:** agent evaluation, software assurance, security, formal methods, agent governance.

**Format:** **Long-form article**

**Confidence: 0.97.**

---
