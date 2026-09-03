---
date: 2026-08-29
item_number: 8
title: "**“A PCIe Error Can Be Real Without Being Worth Waking the Operator Up”** — Short technical post"
summary: "Linux 7.3 adds support for PCIe 7.0 **Advisory Non-Fatal Errors**. These represent errors hardware can report but which are masked by default because they don't necessarily justify the operational response associated with ordinary non-fatal AER events. Linux also gains related PCI improvements for newer Intel and Nvidia platforms."
angle: This is a surprisingly good observability analogy.
interests:
  - PCIe
  - hardware reliability
  - observability
  - SRE
  - servers
format: Short technical post
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 8. **“A PCIe Error Can Be Real Without Being Worth Waking the Operator Up”** — Short technical post


Linux 7.3 adds support for PCIe 7.0 **Advisory Non-Fatal Errors**. These represent errors hardware can report but which are masked by default because they don't necessarily justify the operational response associated with ordinary non-fatal AER events. Linux also gains related PCI improvements for newer Intel and Nvidia platforms. 

**Angle:** This is a surprisingly good observability analogy.

Hardware increasingly distinguishes:

`nothing happened`

from:

`something happened and was corrected`

from:

`something happened and you should care`

from:

`something happened and the machine is dying`.

That's exactly the distinction monitoring systems often fail to make.

A signal isn't valuable merely because it is technically true.

Operational observability requires:

\[
SignalValue \approx Information \times Actionability
\]

Reporting every corrected hardware event at maximum severity simply trains operators to ignore hardware events.

**Matches:** PCIe, hardware reliability, observability, SRE, servers.

**Format:** **Short technical post**

**Confidence: 0.96.**

---
