---
date: 2026-08-28
item_number: 1
title: Multi-Tenancy Is Only as Strong as the Most Boring Tenant Feature
summary: "cPanel & WHM disclosed **CVE-2026-65643** on 27 August. An authenticated customer permitted to add parked or addon domains can create arbitrary files on the underlying server, leading to **root code execution and control of every account, site, and database on that host**. All supported branches were affected and patched builds are available."
angle: "Domain parking sounds almost aggressively uninteresting. That's precisely why this is a good story."
interests:
  - Linux
  - multi-tenancy
  - control planes
  - hosting
  - privilege separation
  - platform security
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 1. Multi-Tenancy Is Only as Strong as the Most Boring Tenant Feature


cPanel & WHM disclosed **CVE-2026-65643** on 27 August. An authenticated customer permitted to add parked or addon domains can create arbitrary files on the underlying server, leading to **root code execution and control of every account, site, and database on that host**. All supported branches were affected and patched builds are available. 

**Angle:** Domain parking sounds almost aggressively uninteresting. That's precisely why this is a good story.

Shared hosting promises:

`customer A`

`customer B`

`customer C`

all sharing:

`one privileged control plane + one operating system`

while believing the tenancy boundaries underneath are meaningful.

A feature whose business semantics are merely:

> attach another hostname to my account

has somehow acquired a path to:

> write arbitrary host files as root.

The broader lesson is that **feature privilege and implementation privilege can be wildly different**.

For every control-plane operation, ask:

`What does the user think they are requesting?`

versus:

`What authority must the implementation exercise to fulfil it?`

The gap between those two is often where catastrophic multi-tenant vulnerabilities live.

**Matches:** Linux, multi-tenancy, control planes, hosting, privilege separation, platform security.

**Format:** **Long-form article**

**Confidence: 0.99 — strongest security article today.**

cPanel security advisory

---
