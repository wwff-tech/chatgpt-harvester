---
date: 2026-08-29
item_number: 3
title: "**“Kubernetes Has Two New Storage Bugs That Are Really Namespace Bugs”** — Long-form / security short"
summary: "The official Kubernetes CVE feed was updated on **27 August** with **CVE-2026-3864 and CVE-2026-3865**, affecting the NFS and SMB CSI drivers respectively. Both involve path traversal through `subDir`, potentially allowing operations to affect unintended directories on the backing storage server."
angle: "Don't write “two new Kubernetes CVEs”. The common mechanism is much better."
interests:
  - Kubernetes
  - CSI
  - storage
  - NFS/SMB
  - container security
  - multi-tenancy
format: "Long-form technical article** or **security short"
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 3. **“Kubernetes Has Two New Storage Bugs That Are Really Namespace Bugs”** — Long-form / security short


The official Kubernetes CVE feed was updated on **27 August** with **CVE-2026-3864 and CVE-2026-3865**, affecting the NFS and SMB CSI drivers respectively. Both involve path traversal through `subDir`, potentially allowing operations to affect unintended directories on the backing storage server. 

Kubernetes official CVE feed

**Angle:** Don't write “two new Kubernetes CVEs”. The common mechanism is much better.

Kubernetes presents something like:

`namespace → PVC → subdirectory`

and users reasonably infer:

> my storage boundary ends here.

But the actual storage server has its own namespace, path resolution rules, permissions, symlinks, and protocol semantics.

This creates a recurring distributed-systems security problem:

> **A namespace boundary enforced in one layer may not survive translation into the namespace beneath it.**

We've seen variants with:

`container path → host path`

`URL path → filesystem path`

`object name → S3 key`

`tenant → database schema`

`Git path → working tree`.

Path traversal is really an **abstraction disagreement about where “inside” ends**.

**Matches:** Kubernetes, CSI, storage, NFS/SMB, container security, multi-tenancy.

**Format:** **Long-form technical article** or **security short**

**Confidence: 0.98.**

---
