---
date: 2026-08-12
item_number: 7
title: "Kubernetes 1.37's Interesting Feature Is the Upgrade You Should Already Have Done"
summary: "Kubernetes 1.37 is due on **26 August**, but one operationally important prerequisite predates it: Kubernetes 1.36 dropped support for containerd 1.x, making containerd 2.x the baseline for current releases. Operators carrying older node images therefore have a runtime migration hiding underneath what may appear to be an ordinary Kubernetes upgrade."
angle: "Use it as an example of **dependency cliffs**."
interests:
  - Kubernetes
  - containerd
  - EKS
  - Linux
  - platform lifecycle
format: Short post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 7. Kubernetes 1.37's Interesting Feature Is the Upgrade You Should Already Have Done


Kubernetes 1.37 is due on **26 August**, but one operationally important prerequisite predates it: Kubernetes 1.36 dropped support for containerd 1.x, making containerd 2.x the baseline for current releases. Operators carrying older node images therefore have a runtime migration hiding underneath what may appear to be an ordinary Kubernetes upgrade. 

**Angle:** Use it as an example of **dependency cliffs**.

Most infrastructure migrations aren't caused by the feature you want. They're caused by accumulated prerequisites:

`Kubernetes upgrade`

↓ requires

`containerd upgrade`

↓ exposes

`config migration / cgroups / plugins`

↓ requires

`node-image rebuild`

Suddenly a version bump is a platform project.

This is why good upgrade planning traverses the dependency graph **before** reading the headline features.

**Matches:** Kubernetes, containerd, EKS, Linux, platform lifecycle.

**Confidence: 0.88** on the article value; verify exact runtime compatibility against your target distributions before publishing operational guidance.

---
