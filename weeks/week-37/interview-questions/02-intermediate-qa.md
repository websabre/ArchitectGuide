# Week 37 — Intermediate Q&A

---


## Q031: Message queues

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q032: Rate limiting

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q033: Multi-region design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q034: RESHADED framework

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q035: Capacity estimation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q036: Load balancing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q037: Caching layers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q038: CDN

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q039: Database sharding

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q040: Read replicas

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q041: Message queues

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q042: Rate limiting

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q043: Multi-region design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q044: RESHADED framework

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q045: Capacity estimation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q046: Load balancing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q047: Caching layers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q048: CDN

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q049: Database sharding

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q050: Read replicas

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q051: Message queues

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q052: Rate limiting

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q053: Multi-region design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q054: RESHADED framework

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q055: Capacity estimation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q056: Load balancing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q057: Caching layers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q058: CDN

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q059: Database sharding

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q060: Read replicas

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q061: Message queues

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q062: Rate limiting

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q063: Multi-region design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q064: RESHADED framework

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q065: Capacity estimation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q066: Load balancing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q067: Caching layers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q068: CDN

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q069: Database sharding

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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

## Q070: Read replicas

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
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
