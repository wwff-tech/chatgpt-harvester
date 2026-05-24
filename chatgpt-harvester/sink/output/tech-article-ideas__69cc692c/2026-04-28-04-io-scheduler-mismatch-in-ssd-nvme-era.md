---
date: 2026-04-28
item_number: 4
title: Your IO Scheduler is Optimising for the Wrong Hardware
summary: Legacy IO schedulers can degrade performance on modern SSD/NVMe devices when not properly configured.
angle: “Defaults lag hardware evolution” — tuning required for modern storage.
interests:
  - Linux
  - storage
  - performance engineering
format: Short post
suggested_points:
  - Differences between schedulers (noop, mq-deadline, kyber)
  - SSD vs HDD assumptions
  - Observability of IO behaviour
  - Tuning recommendations
  - Impact in virtualised/cloud environments
conversation_id: 69cc692c-db90-8396-bc48-375ba1b6270e
label: tech article ideas
---

## 4) IO Scheduler Mismatch in SSD/NVMe Era


- **Title:** *Your IO Scheduler is Optimising for the Wrong Hardware*  
- **Summary:** Legacy IO schedulers can degrade performance on modern SSD/NVMe devices when not properly configured.  
- **Angle:** “Defaults lag hardware evolution” — tuning required for modern storage.  
- **Matches Interests:** Linux, storage, performance engineering  
- **Format:** **Short post**

- **Suggested Points to Cover:**
  - Differences between schedulers (noop, mq-deadline, kyber)  
  - SSD vs HDD assumptions  
  - Observability of IO behaviour  
  - Tuning recommendations  
  - Impact in virtualised/cloud environments  

---
