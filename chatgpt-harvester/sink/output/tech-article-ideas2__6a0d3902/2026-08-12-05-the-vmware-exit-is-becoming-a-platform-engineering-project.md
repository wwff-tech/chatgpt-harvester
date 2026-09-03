---
date: 2026-08-12
item_number: 5
title: The VMware Exit Is Becoming a Platform-Engineering Project
summary: "Today SUSE announced that Australian provider Centorrino Technologies is moving hosted infrastructure onto SUSE Virtualization, with plans to migrate **thousands of virtual machines**. The interesting bit isn't this particular customer; it's another concrete example of post-Broadcom VMware displacement reaching large operational fleets rather than merely appearing in architecture discussions."
angle: "Most VMware-alternative articles compare feature matrices. That's the least interesting part."
interests:
  - Kubernetes
  - platform engineering
  - virtualisation
  - Linux
  - infrastructure migration
format: Long-form
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 5. The VMware Exit Is Becoming a Platform-Engineering Project


Today SUSE announced that Australian provider Centorrino Technologies is moving hosted infrastructure onto SUSE Virtualization, with plans to migrate **thousands of virtual machines**. The interesting bit isn't this particular customer; it's another concrete example of post-Broadcom VMware displacement reaching large operational fleets rather than merely appearing in architecture discussions. 

**Angle:** Most VMware-alternative articles compare feature matrices. That's the least interesting part.

The harder migration is organisational:

`VMware-specific operations → generic infrastructure capabilities`

Backup, networking, storage, identity, VM lifecycle, templates, monitoring, DR, automation, support processes, and operator knowledge all have hidden VMware assumptions.

KubeVirt-based systems also produce an interesting inversion:

> Kubernetes used to run inside VMs. Increasingly, Kubernetes is being asked to run the VMs.

That means organisations may end up with one declarative infrastructure substrate for containers **and** legacy machines — attractive, but with a very different failure domain from vSphere.

**Matches:** Kubernetes, platform engineering, virtualisation, Linux, infrastructure migration.

**Confidence: 0.90.**

---
