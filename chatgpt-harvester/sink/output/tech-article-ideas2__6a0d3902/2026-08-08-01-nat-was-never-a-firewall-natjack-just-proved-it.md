---
date: 2026-08-08
item_number: 1
title: NAT Was Never a Firewall. NatJack Just Proved It.
summary: "Black Hat researcher Malcolm Stagg disclosed **NatJack**, a family of attacks against NAT connection tracking. An attacker merely sharing the same NAT boundary can potentially hijack TCP connections, poison DNS replies, identify mapped ports, or exhaust the NAT table; testing covered 32 products/configurations, and every implementation tested was susceptible to at least part of the attack family. Linux and Windows received CVEs, while Cisco and Apple regard much of the behaviour as a design limitation rather than a vulnerability."
angle: "This is almost tailor-made for a networking/SRE essay: *NAT's accidental security properties became assumed security guarantees*. VLAN and switch-port isolation do not necessarily save you because NatJack attacks shared state at L3/L4. There is also a lovely architectural argument here about the danger of building security assumptions atop mechanisms that were designed for something entirely different."
interests:
  - networking
  - Linux
  - cloud networking
  - Kubernetes
  - zero trust
  - systems architecture
format: Long-form
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

## 1. NAT Was Never a Firewall. NatJack Just Proved It.


Black Hat researcher Malcolm Stagg disclosed **NatJack**, a family of attacks against NAT connection tracking. An attacker merely sharing the same NAT boundary can potentially hijack TCP connections, poison DNS replies, identify mapped ports, or exhaust the NAT table; testing covered 32 products/configurations, and every implementation tested was susceptible to at least part of the attack family. Linux and Windows received CVEs, while Cisco and Apple regard much of the behaviour as a design limitation rather than a vulnerability. 

**Angle:** This is almost tailor-made for a networking/SRE essay: *NAT's accidental security properties became assumed security guarantees*. VLAN and switch-port isolation do not necessarily save you because NatJack attacks shared state at L3/L4. There is also a lovely architectural argument here about the danger of building security assumptions atop mechanisms that were designed for something entirely different.

**Matches:** networking, Linux, cloud networking, Kubernetes, zero trust, systems architecture.

**Confidence: 0.95 — my strongest non-AI pick today.**

---
