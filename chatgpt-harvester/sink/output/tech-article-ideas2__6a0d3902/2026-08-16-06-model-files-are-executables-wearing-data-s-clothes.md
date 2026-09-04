---
date: 2026-08-16
item_number: 6
title: "Model Files Are Executables Wearing Data's Clothes"
summary: "USENIX researchers systematically examined pickle-based ML model poisoning across five major frameworks. They found **22 model-loading paths, 19 missed entirely by existing scanners**, plus 133 exploitable function gadgets. Some techniques bypassed every scanner tested; even the strongest scanner missed 89% of the gadget-based attacks."
angle: Python developers already know that unpickling arbitrary data is code execution.
interests:
  - Python
  - ML infrastructure
  - supply chain
  - sandboxing
  - secure formats
format: Long-form
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 6. Model Files Are Executables Wearing Data's Clothes


USENIX researchers systematically examined pickle-based ML model poisoning across five major frameworks. They found **22 model-loading paths, 19 missed entirely by existing scanners**, plus 133 exploitable function gadgets. Some techniques bypassed every scanner tested; even the strongest scanner missed 89% of the gadget-based attacks. 

**Angle:** Python developers already know that unpickling arbitrary data is code execution.

Yet ML infrastructure has culturally normalised downloading multi-gigabyte “model files” from strangers and feeding them into complex loaders.

The interesting broader category is **active artefacts masquerading as passive artefacts**:

`pickle`

`office macros`

`PDF`

`container image`

`CI YAML`

`package metadata/hooks`

`model checkpoint`

If consuming an artefact can invoke behaviour, its security model should look closer to **installing software** than opening data.

Safetensors and restricted loaders help, but the deeper principle is architectural: don't ask scanners to perfectly recognise malicious behaviour inside a format whose semantics permit arbitrary behaviour.

**Matches:** Python, ML infrastructure, supply chain, sandboxing, secure formats.

**Confidence: 0.98.**

---
