---
date: 2026-08-09
item_number: 3
title: Stop Phishing Humans. Steal the Service Account.
summary: "A particularly interesting section of the same August 6 cloud-threat report concerns JINX-0163, a cloud-native extortion group deliberately targeting **non-human identities** — service accounts and IAM roles — rather than employees. In one case, compromise of one GCP service account reportedly led to thousands of secrets across multiple projects; the group operates across AWS, Azure, GCP, Okta, and Snowflake."
angle: Human IAM has improved enormously — MFA, WebAuthn, conditional access, device trust — while machine identities frequently still have long-lived credentials and sprawling privilege.
interests:
  - IAM
  - cloud
  - Kubernetes
  - Terraform
  - zero trust
  - security architecture
format: Long-form
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 3. Stop Phishing Humans. Steal the Service Account.


A particularly interesting section of the same August 6 cloud-threat report concerns JINX-0163, a cloud-native extortion group deliberately targeting **non-human identities** — service accounts and IAM roles — rather than employees. In one case, compromise of one GCP service account reportedly led to thousands of secrets across multiple projects; the group operates across AWS, Azure, GCP, Okta, and Snowflake. 

**Angle:** Human IAM has improved enormously — MFA, WebAuthn, conditional access, device trust — while machine identities frequently still have long-lived credentials and sprawling privilege.

The provocative thesis could be:

> **We spent twenty years building zero trust for humans, then quietly gave the robots admin keys.**

Then move into workload identity, SPIFFE/SPIRE, AWS/GCP workload federation, short-lived credentials, secretless workloads, Terraform-state exposure, and graph-based privilege analysis.

**Matches:** IAM, cloud, Kubernetes, Terraform, zero trust, security architecture.

**Confidence: 0.96.**

---
