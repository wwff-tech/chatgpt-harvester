---
date: 2026-08-08
item_number: 4
title: A Container Image Can OOM Your Container Runtime
summary: A recently patched containerd vulnerability, CVE-2026-47262, allows a malicious image to consume enough memory during container creation to kill the containerd process. Fixed versions include 1.7.33, 2.0.10, 2.1.9, 2.2.5, and 2.3.2. On Kubernetes, losing the runtime API turns what superficially sounds like an image-level DoS into a node-level availability problem.
angle: "*The container isn't your security boundary until the container exists.* Admission controls and runtime limits cannot protect the machinery that has to unpack and instantiate the hostile object first."
interests:
  - Kubernetes
  - containerd
  - gVisor/container isolation
  - SRE
  - supply-chain security
format: Short post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

## 4. A Container Image Can OOM Your Container Runtime


A recently patched containerd vulnerability, CVE-2026-47262, allows a malicious image to consume enough memory during container creation to kill the containerd process. Fixed versions include 1.7.33, 2.0.10, 2.1.9, 2.2.5, and 2.3.2. On Kubernetes, losing the runtime API turns what superficially sounds like an image-level DoS into a node-level availability problem. 

**Angle:** *The container isn't your security boundary until the container exists.* Admission controls and runtime limits cannot protect the machinery that has to unpack and instantiate the hostile object first.

**Matches:** Kubernetes, containerd, gVisor/container isolation, SRE, supply-chain security.

**Confidence: 0.96.**

---
