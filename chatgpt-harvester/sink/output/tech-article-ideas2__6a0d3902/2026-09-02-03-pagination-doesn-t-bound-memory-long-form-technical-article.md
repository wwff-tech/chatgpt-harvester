---
date: 2026-09-02
item_number: 3
title: "**“Pagination Doesn't Bound Memory”** — Long-form / technical article"
summary: "Kubernetes 1.37 has enabled etcd **RangeStream** at beta by default when paired with etcd 3.7. Previously, large collection reads were paginated by number of keys, but each page was still completely assembled in memory before transmission. Large objects could therefore create unpredictable memory spikes in both etcd and the API server."
angle: "“Use pagination” is standard advice for large APIs, but it hides an assumption:"
interests:
  - Kubernetes
  - etcd
  - API design
  - distributed systems
  - SRE
  - resource exhaustion
format: Long-form technical article
suggested_points:
conversation_id: 6a0d3902-8420-83eb-a699-be83a73b0c48
label: tech article ideas2
---

### 3. **“Pagination Doesn't Bound Memory”** — Long-form / technical article


Kubernetes 1.37 has enabled etcd **RangeStream** at beta by default when paired with etcd 3.7. Previously, large collection reads were paginated by number of keys, but each page was still completely assembled in memory before transmission. Large objects could therefore create unpredictable memory spikes in both etcd and the API server. 

RangeStream instead sends adaptively sized chunks and lets kube-apiserver decode and discard them progressively. 

Kubernetes RangeStream explanation

**Angle:** “Use pagination” is standard advice for large APIs, but it hides an assumption:

\[
size(object_1) \approx size(object_2)
\]

Consider:

`LIST 100 objects`

where objects are 2 KiB.

Fine.

Now:

`LIST 100 objects`

where each object is 2 MiB.

Same pagination.

Very different resource requirement.

Kubernetes's previous design bounded:

`number of objects`.

RangeStream effectively bounds:

`bytes retained at once`.

That is a much stronger resource invariant.

There's a useful general API-design rule here:

> **If the failure mode is resource exhaustion, bound the resource rather than a proxy for the resource.**

`100 requests` doesn't bound CPU.

`100 messages` doesn't bound queue memory.

`100 files` doesn't bound disk.

`100 Kubernetes objects` doesn't bound RAM.

**Matches:** Kubernetes, etcd, API design, distributed systems, SRE, resource exhaustion.

**Format:** **Long-form technical article**

**Confidence: 0.99.**

---
