---
date: 2026-08-29
item_number: 2
title: Security Defaults Fail When Nobody Knows What the Correct Value Is
summary: "KubeCap's 74.67% figure is more interesting than it initially looks."
angle: "Kubernetes gives us:"
interests:
  - Kubernetes
  - security UX
  - IAM
  - platform engineering
  - least privilege
format: Short post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 2. Security Defaults Fail When Nobody Knows What the Correct Value Is


KubeCap's 74.67% figure is more interesting than it initially looks. 

**Angle:** Kubernetes gives us:

```text
securityContext:
  capabilities:
    drop:
      - ALL
    add:
      - ...
```

The syntax is excellent.

The difficult bit is the ellipsis.

Security tooling often assumes operators know the least-privileged configuration and merely need encouragement to type it. In reality, determining the correct minimum can require understanding application code, libc, system calls, kernel behaviour, startup paths, and rare error paths.

So a useful security-design principle is:

> **If the secure configuration requires knowledge ordinary users don't possess, secure-by-default requires deriving that configuration for them.**

The same applies to IAM policies, seccomp profiles, network policy, CSP, firewall rules, and database permissions.

**Matches:** Kubernetes, security UX, IAM, platform engineering, least privilege.

**Format:** **Short post**

**Confidence: 0.99.**

---
