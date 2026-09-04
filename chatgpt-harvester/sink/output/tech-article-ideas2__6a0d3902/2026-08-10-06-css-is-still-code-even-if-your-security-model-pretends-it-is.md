---
date: 2026-08-10
item_number: 6
title: "**“CSS Is Still Code, Even If Your Security Model Pretends It Isn't”** — Long-form or technical short"
summary: Another PortSwigger Research Black Hat presentation demonstrated attacks using only HTML and CSS against webmail systems, including deanonymisation of users of a privacy-oriented encrypted mail provider and complete account takeover chains against multiple major providers. The techniques traversed CSS sanitisation, CSP, and trusted HTML filtering.
angle: "Avoid the specific exploit rabbit-hole initially. There is a more general security principle:"
interests:
  - web security
  - browser internals
  - email
  - language design
  - security boundaries
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 6. **“CSS Is Still Code, Even If Your Security Model Pretends It Isn't”** — Long-form or technical short


Another PortSwigger Research Black Hat presentation demonstrated attacks using only HTML and CSS against webmail systems, including deanonymisation of users of a privacy-oriented encrypted mail provider and complete account takeover chains against multiple major providers. The techniques traversed CSS sanitisation, CSP, and trusted HTML filtering. 

**Angle:** Avoid the specific exploit rabbit-hole initially. There is a more general security principle:

**Passive languages have an annoying habit of becoming active languages.**

CSS acquired network fetches, selectors capable of interrogating document state, conditional behaviour, fonts, animations, calculations, variables, and increasingly sophisticated layout logic.

We've repeatedly done this with configuration formats, templating languages, CI YAML, SQL, regexes, spreadsheets, and PDF.

A fun working title might be:

**“It's Only Data, Right Up Until the Data Gets an `if` Statement.”**

**Matches:** web security, browser internals, email, language design, security boundaries.

**Confidence: 0.94.**

---
