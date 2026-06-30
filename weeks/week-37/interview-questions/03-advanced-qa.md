# Week 37 — Advanced Q&A

---


## Q071: Message queues

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Async |

### Question

What are the trade-offs of Message queues in a production AI/ML Architecture system?

### Short Answer (30 seconds)

Message queues: use when decouple producers/consumers; avoid when sync for fire-and-forget. In AI/ML Architecture, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Message queues** in the context of AI/ML Architecture.

**When to use:** Decouple producers/consumers

**When to avoid:** Sync for fire-and-forget

**Production example:** SQS between order and email

**Architect lens (Trade-offs):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q072: Rate limiting

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Security |

### Question

What failure modes occur when Rate limiting is misapplied in AI/ML Architecture?

### Short Answer (30 seconds)

Rate limiting: use when public apis, abuse prevention; avoid when internal-only admin apis. In AI/ML Architecture, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Rate limiting** in the context of AI/ML Architecture.

**When to use:** Public APIs, abuse prevention

**When to avoid:** Internal-only admin APIs

**Production example:** Token bucket at API gateway

**Architect lens (Failure modes):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q073: Multi-region design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Availability |

### Question

How do you justify Multi-region design to non-technical stakeholders in a AI/ML Architecture initiative?

### Short Answer (30 seconds)

Multi-region design: use when 99.99% sla, global users; avoid when cost-sensitive internal tools. In AI/ML Architecture, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Multi-region design** in the context of AI/ML Architecture.

**When to use:** 99.99% SLA, global users

**When to avoid:** Cost-sensitive internal tools

**Production example:** Active-passive with Traffic Manager

**Architect lens (Stakeholder):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q074: RESHADED framework

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Methodology |

### Question

How does RESHADED framework affect cost and operability in AI/ML Architecture?

### Short Answer (30 seconds)

RESHADED framework: use when every whiteboard interview; avoid when jumping to boxes. In AI/ML Architecture, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**RESHADED framework** in the context of AI/ML Architecture.

**When to use:** Every whiteboard interview

**When to avoid:** Jumping to boxes

**Production example:** Requirements before components

**Architect lens (Cost):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q075: Capacity estimation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Estimation |

### Question

At what scale does Capacity estimation become necessary in AI/ML Architecture?

### Short Answer (30 seconds)

Capacity estimation: use when back-of-envelope qps/storage; avoid when exact numbers without assumptions. In AI/ML Architecture, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Capacity estimation** in the context of AI/ML Architecture.

**When to use:** Back-of-envelope QPS/storage

**When to avoid:** Exact numbers without assumptions

**Production example:** 100M users × 10KB = 1TB profile data

**Architect lens (Scale):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q076: Load balancing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Scale |

### Question

What are the trade-offs of Load balancing in a production AI/ML Architecture system?

### Short Answer (30 seconds)

Load balancing: use when horizontal scale; avoid when single server wishful thinking. In AI/ML Architecture, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Load balancing** in the context of AI/ML Architecture.

**When to use:** Horizontal scale

**When to avoid:** Single server wishful thinking

**Production example:** L7 ALB with health checks

**Architect lens (Trade-offs):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q077: Caching layers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Caching |

### Question

What failure modes occur when Caching layers is misapplied in AI/ML Architecture?

### Short Answer (30 seconds)

Caching layers: use when read-heavy, hot keys; avoid when cache everything including auth. In AI/ML Architecture, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Caching layers** in the context of AI/ML Architecture.

**When to use:** Read-heavy, hot keys

**When to avoid:** Cache everything including auth

**Production example:** Redis cache-aside for product pages

**Architect lens (Failure modes):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q078: CDN

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Edge |

### Question

How do you justify CDN to non-technical stakeholders in a AI/ML Architecture initiative?

### Short Answer (30 seconds)

CDN: use when static assets, global users; avoid when dynamic personalized api at edge. In AI/ML Architecture, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**CDN** in the context of AI/ML Architecture.

**When to use:** Static assets, global users

**When to avoid:** Dynamic personalized API at edge

**Production example:** CloudFront for SPA bundles

**Architect lens (Stakeholder):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q079: Database sharding

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Data Scale |

### Question

How does Database sharding affect cost and operability in AI/ML Architecture?

### Short Answer (30 seconds)

Database sharding: use when write scale beyond single node; avoid when day-one sharding for 100 users. In AI/ML Architecture, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Database sharding** in the context of AI/ML Architecture.

**When to use:** Write scale beyond single node

**When to avoid:** Day-one sharding for 100 users

**Production example:** Shard by tenantId hash

**Architect lens (Cost):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q080: Read replicas

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Data Scale |

### Question

At what scale does Read replicas become necessary in AI/ML Architecture?

### Short Answer (30 seconds)

Read replicas: use when read-heavy workloads; avoid when strong consistency on replicas. In AI/ML Architecture, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Read replicas** in the context of AI/ML Architecture.

**When to use:** Read-heavy workloads

**When to avoid:** Strong consistency on replicas

**Production example:** 5:1 read/write ratio to replicas

**Architect lens (Scale):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q081: Message queues

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Async |

### Question

What are the trade-offs of Message queues in a production AI/ML Architecture system?

### Short Answer (30 seconds)

Message queues: use when decouple producers/consumers; avoid when sync for fire-and-forget. In AI/ML Architecture, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Message queues** in the context of AI/ML Architecture.

**When to use:** Decouple producers/consumers

**When to avoid:** Sync for fire-and-forget

**Production example:** SQS between order and email

**Architect lens (Trade-offs):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q082: Rate limiting

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Security |

### Question

What failure modes occur when Rate limiting is misapplied in AI/ML Architecture?

### Short Answer (30 seconds)

Rate limiting: use when public apis, abuse prevention; avoid when internal-only admin apis. In AI/ML Architecture, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Rate limiting** in the context of AI/ML Architecture.

**When to use:** Public APIs, abuse prevention

**When to avoid:** Internal-only admin APIs

**Production example:** Token bucket at API gateway

**Architect lens (Failure modes):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q083: Multi-region design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Availability |

### Question

How do you justify Multi-region design to non-technical stakeholders in a AI/ML Architecture initiative?

### Short Answer (30 seconds)

Multi-region design: use when 99.99% sla, global users; avoid when cost-sensitive internal tools. In AI/ML Architecture, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Multi-region design** in the context of AI/ML Architecture.

**When to use:** 99.99% SLA, global users

**When to avoid:** Cost-sensitive internal tools

**Production example:** Active-passive with Traffic Manager

**Architect lens (Stakeholder):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q084: RESHADED framework

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Methodology |

### Question

How does RESHADED framework affect cost and operability in AI/ML Architecture?

### Short Answer (30 seconds)

RESHADED framework: use when every whiteboard interview; avoid when jumping to boxes. In AI/ML Architecture, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**RESHADED framework** in the context of AI/ML Architecture.

**When to use:** Every whiteboard interview

**When to avoid:** Jumping to boxes

**Production example:** Requirements before components

**Architect lens (Cost):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q085: Capacity estimation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Estimation |

### Question

At what scale does Capacity estimation become necessary in AI/ML Architecture?

### Short Answer (30 seconds)

Capacity estimation: use when back-of-envelope qps/storage; avoid when exact numbers without assumptions. In AI/ML Architecture, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Capacity estimation** in the context of AI/ML Architecture.

**When to use:** Back-of-envelope QPS/storage

**When to avoid:** Exact numbers without assumptions

**Production example:** 100M users × 10KB = 1TB profile data

**Architect lens (Scale):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q086: Load balancing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Scale |

### Question

What are the trade-offs of Load balancing in a production AI/ML Architecture system?

### Short Answer (30 seconds)

Load balancing: use when horizontal scale; avoid when single server wishful thinking. In AI/ML Architecture, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Load balancing** in the context of AI/ML Architecture.

**When to use:** Horizontal scale

**When to avoid:** Single server wishful thinking

**Production example:** L7 ALB with health checks

**Architect lens (Trade-offs):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q087: Caching layers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Caching |

### Question

What failure modes occur when Caching layers is misapplied in AI/ML Architecture?

### Short Answer (30 seconds)

Caching layers: use when read-heavy, hot keys; avoid when cache everything including auth. In AI/ML Architecture, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Caching layers** in the context of AI/ML Architecture.

**When to use:** Read-heavy, hot keys

**When to avoid:** Cache everything including auth

**Production example:** Redis cache-aside for product pages

**Architect lens (Failure modes):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q088: CDN

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Edge |

### Question

How do you justify CDN to non-technical stakeholders in a AI/ML Architecture initiative?

### Short Answer (30 seconds)

CDN: use when static assets, global users; avoid when dynamic personalized api at edge. In AI/ML Architecture, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**CDN** in the context of AI/ML Architecture.

**When to use:** Static assets, global users

**When to avoid:** Dynamic personalized API at edge

**Production example:** CloudFront for SPA bundles

**Architect lens (Stakeholder):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q089: Database sharding

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Data Scale |

### Question

How does Database sharding affect cost and operability in AI/ML Architecture?

### Short Answer (30 seconds)

Database sharding: use when write scale beyond single node; avoid when day-one sharding for 100 users. In AI/ML Architecture, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Database sharding** in the context of AI/ML Architecture.

**When to use:** Write scale beyond single node

**When to avoid:** Day-one sharding for 100 users

**Production example:** Shard by tenantId hash

**Architect lens (Cost):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q090: Read replicas

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Data Scale |

### Question

At what scale does Read replicas become necessary in AI/ML Architecture?

### Short Answer (30 seconds)

Read replicas: use when read-heavy workloads; avoid when strong consistency on replicas. In AI/ML Architecture, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Read replicas** in the context of AI/ML Architecture.

**When to use:** Read-heavy workloads

**When to avoid:** Strong consistency on replicas

**Production example:** 5:1 read/write ratio to replicas

**Architect lens (Scale):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q091: Message queues

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Async |

### Question

What are the trade-offs of Message queues in a production AI/ML Architecture system?

### Short Answer (30 seconds)

Message queues: use when decouple producers/consumers; avoid when sync for fire-and-forget. In AI/ML Architecture, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Message queues** in the context of AI/ML Architecture.

**When to use:** Decouple producers/consumers

**When to avoid:** Sync for fire-and-forget

**Production example:** SQS between order and email

**Architect lens (Trade-offs):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q092: Rate limiting

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Security |

### Question

What failure modes occur when Rate limiting is misapplied in AI/ML Architecture?

### Short Answer (30 seconds)

Rate limiting: use when public apis, abuse prevention; avoid when internal-only admin apis. In AI/ML Architecture, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Rate limiting** in the context of AI/ML Architecture.

**When to use:** Public APIs, abuse prevention

**When to avoid:** Internal-only admin APIs

**Production example:** Token bucket at API gateway

**Architect lens (Failure modes):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q093: Multi-region design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Availability |

### Question

How do you justify Multi-region design to non-technical stakeholders in a AI/ML Architecture initiative?

### Short Answer (30 seconds)

Multi-region design: use when 99.99% sla, global users; avoid when cost-sensitive internal tools. In AI/ML Architecture, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Multi-region design** in the context of AI/ML Architecture.

**When to use:** 99.99% SLA, global users

**When to avoid:** Cost-sensitive internal tools

**Production example:** Active-passive with Traffic Manager

**Architect lens (Stakeholder):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q094: RESHADED framework

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Methodology |

### Question

How does RESHADED framework affect cost and operability in AI/ML Architecture?

### Short Answer (30 seconds)

RESHADED framework: use when every whiteboard interview; avoid when jumping to boxes. In AI/ML Architecture, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**RESHADED framework** in the context of AI/ML Architecture.

**When to use:** Every whiteboard interview

**When to avoid:** Jumping to boxes

**Production example:** Requirements before components

**Architect lens (Cost):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q095: Capacity estimation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Estimation |

### Question

At what scale does Capacity estimation become necessary in AI/ML Architecture?

### Short Answer (30 seconds)

Capacity estimation: use when back-of-envelope qps/storage; avoid when exact numbers without assumptions. In AI/ML Architecture, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Capacity estimation** in the context of AI/ML Architecture.

**When to use:** Back-of-envelope QPS/storage

**When to avoid:** Exact numbers without assumptions

**Production example:** 100M users × 10KB = 1TB profile data

**Architect lens (Scale):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q096: Load balancing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Scale |

### Question

What are the trade-offs of Load balancing in a production AI/ML Architecture system?

### Short Answer (30 seconds)

Load balancing: use when horizontal scale; avoid when single server wishful thinking. In AI/ML Architecture, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Load balancing** in the context of AI/ML Architecture.

**When to use:** Horizontal scale

**When to avoid:** Single server wishful thinking

**Production example:** L7 ALB with health checks

**Architect lens (Trade-offs):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q097: Caching layers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Caching |

### Question

What failure modes occur when Caching layers is misapplied in AI/ML Architecture?

### Short Answer (30 seconds)

Caching layers: use when read-heavy, hot keys; avoid when cache everything including auth. In AI/ML Architecture, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Caching layers** in the context of AI/ML Architecture.

**When to use:** Read-heavy, hot keys

**When to avoid:** Cache everything including auth

**Production example:** Redis cache-aside for product pages

**Architect lens (Failure modes):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q098: CDN

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Edge |

### Question

How do you justify CDN to non-technical stakeholders in a AI/ML Architecture initiative?

### Short Answer (30 seconds)

CDN: use when static assets, global users; avoid when dynamic personalized api at edge. In AI/ML Architecture, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**CDN** in the context of AI/ML Architecture.

**When to use:** Static assets, global users

**When to avoid:** Dynamic personalized API at edge

**Production example:** CloudFront for SPA bundles

**Architect lens (Stakeholder):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q099: Database sharding

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Data Scale |

### Question

How does Database sharding affect cost and operability in AI/ML Architecture?

### Short Answer (30 seconds)

Database sharding: use when write scale beyond single node; avoid when day-one sharding for 100 users. In AI/ML Architecture, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Database sharding** in the context of AI/ML Architecture.

**When to use:** Write scale beyond single node

**When to avoid:** Day-one sharding for 100 users

**Production example:** Shard by tenantId hash

**Architect lens (Cost):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q100: Read replicas

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Data Scale |

### Question

At what scale does Read replicas become necessary in AI/ML Architecture?

### Short Answer (30 seconds)

Read replicas: use when read-heavy workloads; avoid when strong consistency on replicas. In AI/ML Architecture, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Read replicas** in the context of AI/ML Architecture.

**When to use:** Read-heavy workloads

**When to avoid:** Strong consistency on replicas

**Production example:** 5:1 read/write ratio to replicas

**Architect lens (Scale):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---
