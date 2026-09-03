---
date: 2026-08-25
item_number: 6
title: "**“Attestation Is Becoming Observability You Can Cryptographically Prove”** — Long-form / watch item"
summary: "The Linux Foundation announced **TRACE** today, an open specification developed with AMD, Intel, Microsoft, OPAQUE, and TII. TRACE aims to bind runtime environment, software, policy, data classification, and tool usage into portable cryptographically verifiable evidence for confidential and AI workloads, building on existing standards including RATS, EAT, SLSA, SCITT, SPIFFE, and EAR."
angle: Ignore most of the AI branding.
interests:
  - confidential computing
  - SPIFFE
  - supply-chain security
  - agent governance
  - workload identity
  - observability
format: Long-form/watch item
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 6. **“Attestation Is Becoming Observability You Can Cryptographically Prove”** — Long-form / watch item


The Linux Foundation announced **TRACE** today, an open specification developed with AMD, Intel, Microsoft, OPAQUE, and TII. TRACE aims to bind runtime environment, software, policy, data classification, and tool usage into portable cryptographically verifiable evidence for confidential and AI workloads, building on existing standards including RATS, EAT, SLSA, SCITT, SPIFFE, and EAR. 

**Angle:** Ignore most of the AI branding.

Normal observability says:

> “This workload says it ran version X with policy Y.”

Attestation tries to say:

> **“Here is cryptographic evidence that the measured workload environment was X when Y occurred.”**

That's an important shift from **reported state to evidenced state**.

There is an interesting convergence happening:

`SBOM → what software exists`

`SLSA/provenance → how artefact was built`

`SPIFFE → who workload is`

`attestation → what environment is executing`

`audit log → what it did`.

TRACE is trying to compose several of those into a portable evidence chain.

I'd remain cautious until implementations exist. Specifications are cheap; interoperability is where this becomes interesting.

**Matches:** confidential computing, SPIFFE, supply-chain security, agent governance, workload identity, observability.

**Format:** **Long-form/watch item**

**Confidence: 0.96 on the architectural significance; 0.70 on practical adoption this early.**

---
