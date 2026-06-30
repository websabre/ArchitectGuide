# Week 38 — Advanced Q&A

---


## Q071: Rate limiting

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Security |

### Question

What are the trade-offs of Rate limiting in a production RAG & Vector Search system?

### Short Answer (30 seconds)

Rate limiting: use when public apis, abuse prevention; avoid when internal-only admin apis. In RAG & Vector Search, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Rate limiting** in the context of RAG & Vector Search.

**When to use:** Public APIs, abuse prevention

**When to avoid:** Internal-only admin APIs

**Production example:** Token bucket at API gateway

**Architect lens (Trade-offs):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q072: Multi-region design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Availability |

### Question

What failure modes occur when Multi-region design is misapplied in RAG & Vector Search?

### Short Answer (30 seconds)

Multi-region design: use when 99.99% sla, global users; avoid when cost-sensitive internal tools. In RAG & Vector Search, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Multi-region design** in the context of RAG & Vector Search.

**When to use:** 99.99% SLA, global users

**When to avoid:** Cost-sensitive internal tools

**Production example:** Active-passive with Traffic Manager

**Architect lens (Failure modes):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q073: RESHADED framework

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Methodology |

### Question

How do you justify RESHADED framework to non-technical stakeholders in a RAG & Vector Search initiative?

### Short Answer (30 seconds)

RESHADED framework: use when every whiteboard interview; avoid when jumping to boxes. In RAG & Vector Search, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**RESHADED framework** in the context of RAG & Vector Search.

**When to use:** Every whiteboard interview

**When to avoid:** Jumping to boxes

**Production example:** Requirements before components

**Architect lens (Stakeholder):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q074: Capacity estimation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Estimation |

### Question

How does Capacity estimation affect cost and operability in RAG & Vector Search?

### Short Answer (30 seconds)

Capacity estimation: use when back-of-envelope qps/storage; avoid when exact numbers without assumptions. In RAG & Vector Search, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Capacity estimation** in the context of RAG & Vector Search.

**When to use:** Back-of-envelope QPS/storage

**When to avoid:** Exact numbers without assumptions

**Production example:** 100M users × 10KB = 1TB profile data

**Architect lens (Cost):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q075: Load balancing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Scale |

### Question

At what scale does Load balancing become necessary in RAG & Vector Search?

### Short Answer (30 seconds)

Load balancing: use when horizontal scale; avoid when single server wishful thinking. In RAG & Vector Search, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Load balancing** in the context of RAG & Vector Search.

**When to use:** Horizontal scale

**When to avoid:** Single server wishful thinking

**Production example:** L7 ALB with health checks

**Architect lens (Scale):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q076: Caching layers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Caching |

### Question

What are the trade-offs of Caching layers in a production RAG & Vector Search system?

### Short Answer (30 seconds)

Caching layers: use when read-heavy, hot keys; avoid when cache everything including auth. In RAG & Vector Search, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Caching layers** in the context of RAG & Vector Search.

**When to use:** Read-heavy, hot keys

**When to avoid:** Cache everything including auth

**Production example:** Redis cache-aside for product pages

**Architect lens (Trade-offs):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q077: CDN

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Edge |

### Question

What failure modes occur when CDN is misapplied in RAG & Vector Search?

### Short Answer (30 seconds)

CDN: use when static assets, global users; avoid when dynamic personalized api at edge. In RAG & Vector Search, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**CDN** in the context of RAG & Vector Search.

**When to use:** Static assets, global users

**When to avoid:** Dynamic personalized API at edge

**Production example:** CloudFront for SPA bundles

**Architect lens (Failure modes):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q078: Database sharding

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Data Scale |

### Question

How do you justify Database sharding to non-technical stakeholders in a RAG & Vector Search initiative?

### Short Answer (30 seconds)

Database sharding: use when write scale beyond single node; avoid when day-one sharding for 100 users. In RAG & Vector Search, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Database sharding** in the context of RAG & Vector Search.

**When to use:** Write scale beyond single node

**When to avoid:** Day-one sharding for 100 users

**Production example:** Shard by tenantId hash

**Architect lens (Stakeholder):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q079: Read replicas

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Data Scale |

### Question

How does Read replicas affect cost and operability in RAG & Vector Search?

### Short Answer (30 seconds)

Read replicas: use when read-heavy workloads; avoid when strong consistency on replicas. In RAG & Vector Search, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Read replicas** in the context of RAG & Vector Search.

**When to use:** Read-heavy workloads

**When to avoid:** Strong consistency on replicas

**Production example:** 5:1 read/write ratio to replicas

**Architect lens (Cost):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q080: Message queues

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Async |

### Question

At what scale does Message queues become necessary in RAG & Vector Search?

### Short Answer (30 seconds)

Message queues: use when decouple producers/consumers; avoid when sync for fire-and-forget. In RAG & Vector Search, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Message queues** in the context of RAG & Vector Search.

**When to use:** Decouple producers/consumers

**When to avoid:** Sync for fire-and-forget

**Production example:** SQS between order and email

**Architect lens (Scale):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q081: Rate limiting

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Security |

### Question

What are the trade-offs of Rate limiting in a production RAG & Vector Search system?

### Short Answer (30 seconds)

Rate limiting: use when public apis, abuse prevention; avoid when internal-only admin apis. In RAG & Vector Search, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Rate limiting** in the context of RAG & Vector Search.

**When to use:** Public APIs, abuse prevention

**When to avoid:** Internal-only admin APIs

**Production example:** Token bucket at API gateway

**Architect lens (Trade-offs):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q082: Multi-region design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Availability |

### Question

What failure modes occur when Multi-region design is misapplied in RAG & Vector Search?

### Short Answer (30 seconds)

Multi-region design: use when 99.99% sla, global users; avoid when cost-sensitive internal tools. In RAG & Vector Search, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Multi-region design** in the context of RAG & Vector Search.

**When to use:** 99.99% SLA, global users

**When to avoid:** Cost-sensitive internal tools

**Production example:** Active-passive with Traffic Manager

**Architect lens (Failure modes):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q083: RESHADED framework

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Methodology |

### Question

How do you justify RESHADED framework to non-technical stakeholders in a RAG & Vector Search initiative?

### Short Answer (30 seconds)

RESHADED framework: use when every whiteboard interview; avoid when jumping to boxes. In RAG & Vector Search, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**RESHADED framework** in the context of RAG & Vector Search.

**When to use:** Every whiteboard interview

**When to avoid:** Jumping to boxes

**Production example:** Requirements before components

**Architect lens (Stakeholder):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q084: Capacity estimation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Estimation |

### Question

How does Capacity estimation affect cost and operability in RAG & Vector Search?

### Short Answer (30 seconds)

Capacity estimation: use when back-of-envelope qps/storage; avoid when exact numbers without assumptions. In RAG & Vector Search, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Capacity estimation** in the context of RAG & Vector Search.

**When to use:** Back-of-envelope QPS/storage

**When to avoid:** Exact numbers without assumptions

**Production example:** 100M users × 10KB = 1TB profile data

**Architect lens (Cost):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q085: Load balancing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Scale |

### Question

At what scale does Load balancing become necessary in RAG & Vector Search?

### Short Answer (30 seconds)

Load balancing: use when horizontal scale; avoid when single server wishful thinking. In RAG & Vector Search, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Load balancing** in the context of RAG & Vector Search.

**When to use:** Horizontal scale

**When to avoid:** Single server wishful thinking

**Production example:** L7 ALB with health checks

**Architect lens (Scale):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q086: Caching layers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Caching |

### Question

What are the trade-offs of Caching layers in a production RAG & Vector Search system?

### Short Answer (30 seconds)

Caching layers: use when read-heavy, hot keys; avoid when cache everything including auth. In RAG & Vector Search, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Caching layers** in the context of RAG & Vector Search.

**When to use:** Read-heavy, hot keys

**When to avoid:** Cache everything including auth

**Production example:** Redis cache-aside for product pages

**Architect lens (Trade-offs):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q087: CDN

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Edge |

### Question

What failure modes occur when CDN is misapplied in RAG & Vector Search?

### Short Answer (30 seconds)

CDN: use when static assets, global users; avoid when dynamic personalized api at edge. In RAG & Vector Search, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**CDN** in the context of RAG & Vector Search.

**When to use:** Static assets, global users

**When to avoid:** Dynamic personalized API at edge

**Production example:** CloudFront for SPA bundles

**Architect lens (Failure modes):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q088: Database sharding

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Data Scale |

### Question

How do you justify Database sharding to non-technical stakeholders in a RAG & Vector Search initiative?

### Short Answer (30 seconds)

Database sharding: use when write scale beyond single node; avoid when day-one sharding for 100 users. In RAG & Vector Search, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Database sharding** in the context of RAG & Vector Search.

**When to use:** Write scale beyond single node

**When to avoid:** Day-one sharding for 100 users

**Production example:** Shard by tenantId hash

**Architect lens (Stakeholder):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q089: Read replicas

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Data Scale |

### Question

How does Read replicas affect cost and operability in RAG & Vector Search?

### Short Answer (30 seconds)

Read replicas: use when read-heavy workloads; avoid when strong consistency on replicas. In RAG & Vector Search, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Read replicas** in the context of RAG & Vector Search.

**When to use:** Read-heavy workloads

**When to avoid:** Strong consistency on replicas

**Production example:** 5:1 read/write ratio to replicas

**Architect lens (Cost):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q090: Message queues

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Async |

### Question

At what scale does Message queues become necessary in RAG & Vector Search?

### Short Answer (30 seconds)

Message queues: use when decouple producers/consumers; avoid when sync for fire-and-forget. In RAG & Vector Search, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Message queues** in the context of RAG & Vector Search.

**When to use:** Decouple producers/consumers

**When to avoid:** Sync for fire-and-forget

**Production example:** SQS between order and email

**Architect lens (Scale):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q091: Rate limiting

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Security |

### Question

What are the trade-offs of Rate limiting in a production RAG & Vector Search system?

### Short Answer (30 seconds)

Rate limiting: use when public apis, abuse prevention; avoid when internal-only admin apis. In RAG & Vector Search, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Rate limiting** in the context of RAG & Vector Search.

**When to use:** Public APIs, abuse prevention

**When to avoid:** Internal-only admin APIs

**Production example:** Token bucket at API gateway

**Architect lens (Trade-offs):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q092: Multi-region design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Availability |

### Question

What failure modes occur when Multi-region design is misapplied in RAG & Vector Search?

### Short Answer (30 seconds)

Multi-region design: use when 99.99% sla, global users; avoid when cost-sensitive internal tools. In RAG & Vector Search, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Multi-region design** in the context of RAG & Vector Search.

**When to use:** 99.99% SLA, global users

**When to avoid:** Cost-sensitive internal tools

**Production example:** Active-passive with Traffic Manager

**Architect lens (Failure modes):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q093: RESHADED framework

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Methodology |

### Question

How do you justify RESHADED framework to non-technical stakeholders in a RAG & Vector Search initiative?

### Short Answer (30 seconds)

RESHADED framework: use when every whiteboard interview; avoid when jumping to boxes. In RAG & Vector Search, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**RESHADED framework** in the context of RAG & Vector Search.

**When to use:** Every whiteboard interview

**When to avoid:** Jumping to boxes

**Production example:** Requirements before components

**Architect lens (Stakeholder):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q094: Capacity estimation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Estimation |

### Question

How does Capacity estimation affect cost and operability in RAG & Vector Search?

### Short Answer (30 seconds)

Capacity estimation: use when back-of-envelope qps/storage; avoid when exact numbers without assumptions. In RAG & Vector Search, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Capacity estimation** in the context of RAG & Vector Search.

**When to use:** Back-of-envelope QPS/storage

**When to avoid:** Exact numbers without assumptions

**Production example:** 100M users × 10KB = 1TB profile data

**Architect lens (Cost):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q095: Load balancing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Scale |

### Question

At what scale does Load balancing become necessary in RAG & Vector Search?

### Short Answer (30 seconds)

Load balancing: use when horizontal scale; avoid when single server wishful thinking. In RAG & Vector Search, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Load balancing** in the context of RAG & Vector Search.

**When to use:** Horizontal scale

**When to avoid:** Single server wishful thinking

**Production example:** L7 ALB with health checks

**Architect lens (Scale):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q096: Caching layers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Caching |

### Question

What are the trade-offs of Caching layers in a production RAG & Vector Search system?

### Short Answer (30 seconds)

Caching layers: use when read-heavy, hot keys; avoid when cache everything including auth. In RAG & Vector Search, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Caching layers** in the context of RAG & Vector Search.

**When to use:** Read-heavy, hot keys

**When to avoid:** Cache everything including auth

**Production example:** Redis cache-aside for product pages

**Architect lens (Trade-offs):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q097: CDN

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Edge |

### Question

What failure modes occur when CDN is misapplied in RAG & Vector Search?

### Short Answer (30 seconds)

CDN: use when static assets, global users; avoid when dynamic personalized api at edge. In RAG & Vector Search, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**CDN** in the context of RAG & Vector Search.

**When to use:** Static assets, global users

**When to avoid:** Dynamic personalized API at edge

**Production example:** CloudFront for SPA bundles

**Architect lens (Failure modes):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q098: Database sharding

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Data Scale |

### Question

How do you justify Database sharding to non-technical stakeholders in a RAG & Vector Search initiative?

### Short Answer (30 seconds)

Database sharding: use when write scale beyond single node; avoid when day-one sharding for 100 users. In RAG & Vector Search, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Database sharding** in the context of RAG & Vector Search.

**When to use:** Write scale beyond single node

**When to avoid:** Day-one sharding for 100 users

**Production example:** Shard by tenantId hash

**Architect lens (Stakeholder):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q099: Read replicas

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Data Scale |

### Question

How does Read replicas affect cost and operability in RAG & Vector Search?

### Short Answer (30 seconds)

Read replicas: use when read-heavy workloads; avoid when strong consistency on replicas. In RAG & Vector Search, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Read replicas** in the context of RAG & Vector Search.

**When to use:** Read-heavy workloads

**When to avoid:** Strong consistency on replicas

**Production example:** 5:1 read/write ratio to replicas

**Architect lens (Cost):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q100: Message queues

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Async |

### Question

At what scale does Message queues become necessary in RAG & Vector Search?

### Short Answer (30 seconds)

Message queues: use when decouple producers/consumers; avoid when sync for fire-and-forget. In RAG & Vector Search, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Message queues** in the context of RAG & Vector Search.

**When to use:** Decouple producers/consumers

**When to avoid:** Sync for fire-and-forget

**Production example:** SQS between order and email

**Architect lens (Scale):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---
