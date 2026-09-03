---
date: 2026-08-19
item_number: 2
title: Bandwidth Is the Wrong Metric for Secret Exfiltration
summary: "The Cloudflare research provides an excellent compact security lesson: **12 bits per second sounds useless until the thing you want is only a few hundred bytes long**."
angle: "Security impact is:"
interests:
  - security engineering
  - side channels
  - IAM
  - threat modelling
format: Short post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 2. Bandwidth Is the Wrong Metric for Secret Exfiltration


The Cloudflare research provides an excellent compact security lesson: **12 bits per second sounds useless until the thing you want is only a few hundred bytes long**. 

**Angle:** Security impact is:

`channel bandwidth × time available × value density of target data`

not simply channel bandwidth.

A 100-byte credential at 12 bit/s is theoretically on the order of a minute. Conversely, exfiltrating a database would be absurdly slow.

This generalises to DNS tunnelling, timing channels, LEDs, power analysis, cache attacks, and constrained covert channels.

The useful question isn't:

> Is the channel fast?

It's:

> **Is it fast enough for the smallest thing that grants substantially more authority?**

That often means tokens and keys.

**Matches:** security engineering, side channels, IAM, threat modelling.

**Format:** **Short post**

**Confidence: 0.99.**

---
