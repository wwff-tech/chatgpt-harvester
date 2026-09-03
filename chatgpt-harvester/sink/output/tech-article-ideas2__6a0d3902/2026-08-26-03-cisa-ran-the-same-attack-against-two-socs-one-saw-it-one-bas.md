---
date: 2026-08-26
item_number: 3
title: "CISA Ran the Same Attack Against Two SOCs. One Saw It. One Basically Didn't."
summary: "CISA published **“A Tale of Two SOCs”** on 25 August, comparing red-team assessments of two critical-infrastructure organisations. The striking result is the contrast: one organisation detected much of the activity and repeatedly forced the red team to change tactics; the other failed to detect significant malicious activity during the assessment."
angle: "This is much better than another list of SOC best practices because it is effectively an **A/B test against adversarial behaviour**."
interests:
  - SRE/observability
  - incident response
  - detection engineering
  - security operations
  - adversarial testing
format: Long-form article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 3. CISA Ran the Same Attack Against Two SOCs. One Saw It. One Basically Didn't.


CISA published **“A Tale of Two SOCs”** on 25 August, comparing red-team assessments of two critical-infrastructure organisations. The striking result is the contrast: one organisation detected much of the activity and repeatedly forced the red team to change tactics; the other failed to detect significant malicious activity during the assessment. 

CISA — A Tale of Two SOCs

**Angle:** This is much better than another list of SOC best practices because it is effectively an **A/B test against adversarial behaviour**.

Both organisations faced a skilled attacker.

The variable was defensive capability.

I'd focus less on products and more on feedback loops:

`telemetry`

→ `detection`

→ `human interpretation`

→ `response`

→ `attacker forced to adapt`.

A good SOC doesn't merely produce alerts. It **changes the attacker's economics while the intrusion is happening**.

That suggests an interesting effectiveness metric:

> How frequently does defensive action force the attacker to abandon a working path and spend effort finding another one?

That's closer to measuring control effectiveness than “number of alerts generated”.

**Matches:** SRE/observability, incident response, detection engineering, security operations, adversarial testing.

**Format:** **Long-form article**

**Confidence: 0.99 — probably the best pure security article today.**

---
