---
date: 2026-08-26
item_number: 2
title: "**“`--cached` Didn't Mean What the Application Thought It Meant”** — Long-form / technical short"
summary: "The mechanism behind CVE-2026-60004 is unusually educational. Gitea applied attacker-controlled patches in a **bare temporary clone**. Under particular conflict handling, Git's three-way fallback could write into what amounted to `$GIT_DIR`; that allowed an executable `post-index-change` hook to appear where Git would subsequently run it. The eventual fix switched the operation away from a bare clone."
angle: This is a classic abstraction-boundary failure.
interests:
  - Git internals
  - security engineering
  - testing
  - software assurance
  - agent-first Git work
format: "Long-form technical article** or **short post"
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 2. **“`--cached` Didn't Mean What the Application Thought It Meant”** — Long-form / technical short


The mechanism behind CVE-2026-60004 is unusually educational. Gitea applied attacker-controlled patches in a **bare temporary clone**. Under particular conflict handling, Git's three-way fallback could write into what amounted to `$GIT_DIR`; that allowed an executable `post-index-change` hook to appear where Git would subsequently run it. The eventual fix switched the operation away from a bare clone. 

**Angle:** This is a classic abstraction-boundary failure.

The application believed something resembling:

`git apply --cached → modify index only`.

But the actual semantics depended on:

`repository type + conflict state + Git fallback behaviour + filesystem layout`.

Security failed in the **composition of individually reasonable abstractions**.

There's a useful general rule:

> **If security depends on a tool *not* producing a side effect, test the invariant rather than trusting the option name.**

Examples include archive extraction, image conversion, compilers/plugins, Git hooks, package-manager scripts, templating engines, and document parsers.

This could make a very good code-level companion to the broader Gitea piece.

**Matches:** Git internals, security engineering, testing, software assurance, agent-first Git work.

**Format:** **Long-form technical article** or **short post**

**Confidence: 0.98.**

---
