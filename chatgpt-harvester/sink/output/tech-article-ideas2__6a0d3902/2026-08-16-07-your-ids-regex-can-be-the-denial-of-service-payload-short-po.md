---
date: 2026-08-16
item_number: 7
title: "**“Your IDS Regex Can Be the Denial-of-Service Payload”** — Short post / technical article"
summary: "Another USENIX paper examines regex denial of service involving **backreferences**, a case existing detectors often miss. Applied to the Snort ruleset, the researchers found 48 previously unknown problematic expressions. Crafted traffic could add roughly 0.6–1.2 seconds of rule-evaluation time and even trigger PCRE matching limits in ways that bypass alerts."
angle: "This has a lovely operational irony:"
interests:
  - SRE
  - observability
  - IDS/WAF
  - performance engineering
  - ReDoS
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 7. **“Your IDS Regex Can Be the Denial-of-Service Payload”** — Short post / technical article


Another USENIX paper examines regex denial of service involving **backreferences**, a case existing detectors often miss. Applied to the Snort ruleset, the researchers found 48 previously unknown problematic expressions. Crafted traffic could add roughly 0.6–1.2 seconds of rule-evaluation time and even trigger PCRE matching limits in ways that bypass alerts. 

**Angle:** This has a lovely operational irony:

> The security control becomes the attack surface because it performs more work on hostile input than the system it protects.

Generalise it to:

`WAF rules`

`SIEM regex`

`log parsers`

`IDS signatures`

`schema validators`

`malware scanners`

These all deliberately ingest adversarial data, so their **computational complexity is part of the threat model**.

That is particularly relevant to observability pipelines: a log line should not be able to consume unbounded CPU merely because somebody wrote a heroic regex six years ago.

**Matches:** SRE, observability, IDS/WAF, performance engineering, ReDoS.

**Confidence: 0.97.**

---
