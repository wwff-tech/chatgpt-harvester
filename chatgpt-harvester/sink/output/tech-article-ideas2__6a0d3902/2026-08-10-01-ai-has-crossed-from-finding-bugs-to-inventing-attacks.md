---
date: 2026-08-10
item_number: 1
title: AI Has Crossed From Finding Bugs to Inventing Attacks
summary: "PortSwigger Research published the full results behind James Kettle's Black Hat/DEF CON **HTTP Terminator** work on 5 August. This is substantially more interesting than another “LLM found CVEs” story: the system generated previously unknown HTTP desynchronisation techniques and attack chains that worked against banks, government infrastructure, and security products. Crucially, Kettle deliberately pushed it until autonomy *stopped working* and mapped where human–AI collaboration still beat the autonomous system."
angle: "Don't write “AI can hack now”. The better article is about **automation crossing the novelty boundary**."
interests:
  - agentic AI
  - heterogeneous agents
  - security research
  - HTTP/proxies
  - automated evaluation
  - systems thinking
format: Long-form
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 1. AI Has Crossed From Finding Bugs to Inventing Attacks


PortSwigger Research published the full results behind James Kettle's Black Hat/DEF CON **HTTP Terminator** work on 5 August. This is substantially more interesting than another “LLM found CVEs” story: the system generated previously unknown HTTP desynchronisation techniques and attack chains that worked against banks, government infrastructure, and security products. Crucially, Kettle deliberately pushed it until autonomy *stopped working* and mapped where human–AI collaboration still beat the autonomous system. 

**Angle:** Don't write “AI can hack now”. The better article is about **automation crossing the novelty boundary**.

Kettle's architecture separates ideation, evaluation, weaponisation, anomaly detection, and cascading exploration. That's remarkably close to how good scientific tooling works: generate hypotheses cheaply, build strong falsification machinery, then recursively investigate anomalies.

The most interesting finding may actually be the failures. Kettle explicitly set out to exceed current model capability to identify where expert human intuition still contributes. 

That gives you a much better thesis:

**“The useful question isn't whether AI can replace a security researcher. It's which parts of the research loop have become mechanically scalable.”**

**Matches:** agentic AI, heterogeneous agents, security research, HTTP/proxies, automated evaluation, systems thinking.

**Confidence: 0.99 — strongest idea today.**

---
