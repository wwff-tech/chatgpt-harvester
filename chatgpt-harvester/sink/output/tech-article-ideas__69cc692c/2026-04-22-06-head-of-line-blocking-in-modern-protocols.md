---
date: 2026-04-22
item_number: 6
title: Parallelism Still Queues Somewhere
summary: Even with HTTP/2 and HTTP/3, head-of-line blocking can persist at different layers, affecting performance.
angle: “You can move the bottleneck, not remove it” — protocol evolution shifts constraints.
interests:
  - Networking
  - performance
format: Short post
suggested_points:
  - HOL blocking in different protocol layers
  - Improvements in HTTP/2 and QUIC
  - Remaining bottlenecks (application, TCP fallback)
  - Observability challenges
  - Mitigation strategies
conversation_id: 69cc692c-db90-8396-bc48-375ba1b6270e
label: tech article ideas
---

## 6) Head-of-Line Blocking in Modern Protocols


- **Title:** *Parallelism Still Queues Somewhere*  
- **Summary:** Even with HTTP/2 and HTTP/3, head-of-line blocking can persist at different layers, affecting performance.  
- **Angle:** “You can move the bottleneck, not remove it” — protocol evolution shifts constraints.  
- **Matches Interests:** Networking, performance  
- **Format:** **Short post**

- **Suggested Points to Cover:**
  - HOL blocking in different protocol layers  
  - Improvements in HTTP/2 and QUIC  
  - Remaining bottlenecks (application, TCP fallback)  
  - Observability challenges  
  - Mitigation strategies  

---
