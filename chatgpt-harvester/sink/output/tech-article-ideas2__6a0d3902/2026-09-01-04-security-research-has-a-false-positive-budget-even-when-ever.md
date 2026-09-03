---
date: 2026-09-01
item_number: 4
title: Security Research Has a False-Positive Budget Even When Every Finding Is Technically True
summary: "WordPress's change highlights an important distinction: a report can describe a **real unintended behaviour** while still being low-value security work."
angle: "We normally reserve “false positive” for findings that aren't vulnerabilities."
interests:
  - AI security tooling
  - SRE
  - vulnerability management
  - observability
format: Short post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 4. Security Research Has a False-Positive Budget Even When Every Finding Is Technically True


WordPress's change highlights an important distinction: a report can describe a **real unintended behaviour** while still being low-value security work. 

**Angle:** We normally reserve “false positive” for findings that aren't vulnerabilities.

Operationally, however, there is another category:

`technically valid`

+ `negligible reachable impact`

+ `expensive to investigate`.

At scale, those behave rather like false positives because they consume the same scarce triage channel.

That suggests measuring automated security tooling using something closer to:

\[
Value =
\frac{\text{meaningful risk removed}}
{\text{human attention consumed}}
\]

rather than:

`bugs found`.

AI vulnerability scanners that generate 100× more valid findings but consume 200× more expert triage time may be a regression.

**Matches:** AI security tooling, SRE, vulnerability management, observability.

**Format:** **Short post**

**Confidence: 0.99.**

---
