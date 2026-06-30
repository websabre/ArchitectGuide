# Week 39 — Intermediate Q&A

---


## Q031: Multi-region design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Availability |

### Question

What are the trade-offs of Multi-region design in a production LLMOps & Responsible AI system?

### Short Answer (30 seconds)

Multi-region design: use when 99.99% sla, global users; avoid when cost-sensitive internal tools. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Multi-region design** in the context of LLMOps & Responsible AI.

**When to use:** 99.99% SLA, global users

**When to avoid:** Cost-sensitive internal tools

**Production example:** Active-passive with Traffic Manager

**Architect lens (Trade-offs):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q032: RESHADED framework

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Methodology |

### Question

What failure modes occur when RESHADED framework is misapplied in LLMOps & Responsible AI?

### Short Answer (30 seconds)

RESHADED framework: use when every whiteboard interview; avoid when jumping to boxes. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**RESHADED framework** in the context of LLMOps & Responsible AI.

**When to use:** Every whiteboard interview

**When to avoid:** Jumping to boxes

**Production example:** Requirements before components

**Architect lens (Failure modes):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q033: Capacity estimation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Estimation |

### Question

How do you justify Capacity estimation to non-technical stakeholders in a LLMOps & Responsible AI initiative?

### Short Answer (30 seconds)

Capacity estimation: use when back-of-envelope qps/storage; avoid when exact numbers without assumptions. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Capacity estimation** in the context of LLMOps & Responsible AI.

**When to use:** Back-of-envelope QPS/storage

**When to avoid:** Exact numbers without assumptions

**Production example:** 100M users × 10KB = 1TB profile data

**Architect lens (Stakeholder):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q034: Load balancing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Scale |

### Question

How does Load balancing affect cost and operability in LLMOps & Responsible AI?

### Short Answer (30 seconds)

Load balancing: use when horizontal scale; avoid when single server wishful thinking. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Load balancing** in the context of LLMOps & Responsible AI.

**When to use:** Horizontal scale

**When to avoid:** Single server wishful thinking

**Production example:** L7 ALB with health checks

**Architect lens (Cost):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q035: Caching layers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Caching |

### Question

At what scale does Caching layers become necessary in LLMOps & Responsible AI?

### Short Answer (30 seconds)

Caching layers: use when read-heavy, hot keys; avoid when cache everything including auth. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Caching layers** in the context of LLMOps & Responsible AI.

**When to use:** Read-heavy, hot keys

**When to avoid:** Cache everything including auth

**Production example:** Redis cache-aside for product pages

**Architect lens (Scale):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q036: CDN

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Edge |

### Question

What are the trade-offs of CDN in a production LLMOps & Responsible AI system?

### Short Answer (30 seconds)

CDN: use when static assets, global users; avoid when dynamic personalized api at edge. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**CDN** in the context of LLMOps & Responsible AI.

**When to use:** Static assets, global users

**When to avoid:** Dynamic personalized API at edge

**Production example:** CloudFront for SPA bundles

**Architect lens (Trade-offs):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q037: Database sharding

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Data Scale |

### Question

What failure modes occur when Database sharding is misapplied in LLMOps & Responsible AI?

### Short Answer (30 seconds)

Database sharding: use when write scale beyond single node; avoid when day-one sharding for 100 users. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Database sharding** in the context of LLMOps & Responsible AI.

**When to use:** Write scale beyond single node

**When to avoid:** Day-one sharding for 100 users

**Production example:** Shard by tenantId hash

**Architect lens (Failure modes):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q038: Read replicas

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Data Scale |

### Question

How do you justify Read replicas to non-technical stakeholders in a LLMOps & Responsible AI initiative?

### Short Answer (30 seconds)

Read replicas: use when read-heavy workloads; avoid when strong consistency on replicas. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Read replicas** in the context of LLMOps & Responsible AI.

**When to use:** Read-heavy workloads

**When to avoid:** Strong consistency on replicas

**Production example:** 5:1 read/write ratio to replicas

**Architect lens (Stakeholder):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q039: Message queues

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Async |

### Question

How does Message queues affect cost and operability in LLMOps & Responsible AI?

### Short Answer (30 seconds)

Message queues: use when decouple producers/consumers; avoid when sync for fire-and-forget. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Message queues** in the context of LLMOps & Responsible AI.

**When to use:** Decouple producers/consumers

**When to avoid:** Sync for fire-and-forget

**Production example:** SQS between order and email

**Architect lens (Cost):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q040: Rate limiting

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |

### Question

At what scale does Rate limiting become necessary in LLMOps & Responsible AI?

### Short Answer (30 seconds)

Rate limiting: use when public apis, abuse prevention; avoid when internal-only admin apis. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Rate limiting** in the context of LLMOps & Responsible AI.

**When to use:** Public APIs, abuse prevention

**When to avoid:** Internal-only admin APIs

**Production example:** Token bucket at API gateway

**Architect lens (Scale):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q041: Multi-region design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Availability |

### Question

What are the trade-offs of Multi-region design in a production LLMOps & Responsible AI system?

### Short Answer (30 seconds)

Multi-region design: use when 99.99% sla, global users; avoid when cost-sensitive internal tools. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Multi-region design** in the context of LLMOps & Responsible AI.

**When to use:** 99.99% SLA, global users

**When to avoid:** Cost-sensitive internal tools

**Production example:** Active-passive with Traffic Manager

**Architect lens (Trade-offs):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q042: RESHADED framework

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Methodology |

### Question

What failure modes occur when RESHADED framework is misapplied in LLMOps & Responsible AI?

### Short Answer (30 seconds)

RESHADED framework: use when every whiteboard interview; avoid when jumping to boxes. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**RESHADED framework** in the context of LLMOps & Responsible AI.

**When to use:** Every whiteboard interview

**When to avoid:** Jumping to boxes

**Production example:** Requirements before components

**Architect lens (Failure modes):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q043: Capacity estimation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Estimation |

### Question

How do you justify Capacity estimation to non-technical stakeholders in a LLMOps & Responsible AI initiative?

### Short Answer (30 seconds)

Capacity estimation: use when back-of-envelope qps/storage; avoid when exact numbers without assumptions. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Capacity estimation** in the context of LLMOps & Responsible AI.

**When to use:** Back-of-envelope QPS/storage

**When to avoid:** Exact numbers without assumptions

**Production example:** 100M users × 10KB = 1TB profile data

**Architect lens (Stakeholder):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q044: Load balancing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Scale |

### Question

How does Load balancing affect cost and operability in LLMOps & Responsible AI?

### Short Answer (30 seconds)

Load balancing: use when horizontal scale; avoid when single server wishful thinking. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Load balancing** in the context of LLMOps & Responsible AI.

**When to use:** Horizontal scale

**When to avoid:** Single server wishful thinking

**Production example:** L7 ALB with health checks

**Architect lens (Cost):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q045: Caching layers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Caching |

### Question

At what scale does Caching layers become necessary in LLMOps & Responsible AI?

### Short Answer (30 seconds)

Caching layers: use when read-heavy, hot keys; avoid when cache everything including auth. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Caching layers** in the context of LLMOps & Responsible AI.

**When to use:** Read-heavy, hot keys

**When to avoid:** Cache everything including auth

**Production example:** Redis cache-aside for product pages

**Architect lens (Scale):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q046: CDN

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Edge |

### Question

What are the trade-offs of CDN in a production LLMOps & Responsible AI system?

### Short Answer (30 seconds)

CDN: use when static assets, global users; avoid when dynamic personalized api at edge. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**CDN** in the context of LLMOps & Responsible AI.

**When to use:** Static assets, global users

**When to avoid:** Dynamic personalized API at edge

**Production example:** CloudFront for SPA bundles

**Architect lens (Trade-offs):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q047: Database sharding

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Data Scale |

### Question

What failure modes occur when Database sharding is misapplied in LLMOps & Responsible AI?

### Short Answer (30 seconds)

Database sharding: use when write scale beyond single node; avoid when day-one sharding for 100 users. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Database sharding** in the context of LLMOps & Responsible AI.

**When to use:** Write scale beyond single node

**When to avoid:** Day-one sharding for 100 users

**Production example:** Shard by tenantId hash

**Architect lens (Failure modes):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q048: Read replicas

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Data Scale |

### Question

How do you justify Read replicas to non-technical stakeholders in a LLMOps & Responsible AI initiative?

### Short Answer (30 seconds)

Read replicas: use when read-heavy workloads; avoid when strong consistency on replicas. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Read replicas** in the context of LLMOps & Responsible AI.

**When to use:** Read-heavy workloads

**When to avoid:** Strong consistency on replicas

**Production example:** 5:1 read/write ratio to replicas

**Architect lens (Stakeholder):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q049: Message queues

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Async |

### Question

How does Message queues affect cost and operability in LLMOps & Responsible AI?

### Short Answer (30 seconds)

Message queues: use when decouple producers/consumers; avoid when sync for fire-and-forget. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Message queues** in the context of LLMOps & Responsible AI.

**When to use:** Decouple producers/consumers

**When to avoid:** Sync for fire-and-forget

**Production example:** SQS between order and email

**Architect lens (Cost):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q050: Rate limiting

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |

### Question

At what scale does Rate limiting become necessary in LLMOps & Responsible AI?

### Short Answer (30 seconds)

Rate limiting: use when public apis, abuse prevention; avoid when internal-only admin apis. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Rate limiting** in the context of LLMOps & Responsible AI.

**When to use:** Public APIs, abuse prevention

**When to avoid:** Internal-only admin APIs

**Production example:** Token bucket at API gateway

**Architect lens (Scale):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q051: Multi-region design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Availability |

### Question

What are the trade-offs of Multi-region design in a production LLMOps & Responsible AI system?

### Short Answer (30 seconds)

Multi-region design: use when 99.99% sla, global users; avoid when cost-sensitive internal tools. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Multi-region design** in the context of LLMOps & Responsible AI.

**When to use:** 99.99% SLA, global users

**When to avoid:** Cost-sensitive internal tools

**Production example:** Active-passive with Traffic Manager

**Architect lens (Trade-offs):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q052: RESHADED framework

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Methodology |

### Question

What failure modes occur when RESHADED framework is misapplied in LLMOps & Responsible AI?

### Short Answer (30 seconds)

RESHADED framework: use when every whiteboard interview; avoid when jumping to boxes. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**RESHADED framework** in the context of LLMOps & Responsible AI.

**When to use:** Every whiteboard interview

**When to avoid:** Jumping to boxes

**Production example:** Requirements before components

**Architect lens (Failure modes):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q053: Capacity estimation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Estimation |

### Question

How do you justify Capacity estimation to non-technical stakeholders in a LLMOps & Responsible AI initiative?

### Short Answer (30 seconds)

Capacity estimation: use when back-of-envelope qps/storage; avoid when exact numbers without assumptions. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Capacity estimation** in the context of LLMOps & Responsible AI.

**When to use:** Back-of-envelope QPS/storage

**When to avoid:** Exact numbers without assumptions

**Production example:** 100M users × 10KB = 1TB profile data

**Architect lens (Stakeholder):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q054: Load balancing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Scale |

### Question

How does Load balancing affect cost and operability in LLMOps & Responsible AI?

### Short Answer (30 seconds)

Load balancing: use when horizontal scale; avoid when single server wishful thinking. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Load balancing** in the context of LLMOps & Responsible AI.

**When to use:** Horizontal scale

**When to avoid:** Single server wishful thinking

**Production example:** L7 ALB with health checks

**Architect lens (Cost):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q055: Caching layers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Caching |

### Question

At what scale does Caching layers become necessary in LLMOps & Responsible AI?

### Short Answer (30 seconds)

Caching layers: use when read-heavy, hot keys; avoid when cache everything including auth. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Caching layers** in the context of LLMOps & Responsible AI.

**When to use:** Read-heavy, hot keys

**When to avoid:** Cache everything including auth

**Production example:** Redis cache-aside for product pages

**Architect lens (Scale):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q056: CDN

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Edge |

### Question

What are the trade-offs of CDN in a production LLMOps & Responsible AI system?

### Short Answer (30 seconds)

CDN: use when static assets, global users; avoid when dynamic personalized api at edge. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**CDN** in the context of LLMOps & Responsible AI.

**When to use:** Static assets, global users

**When to avoid:** Dynamic personalized API at edge

**Production example:** CloudFront for SPA bundles

**Architect lens (Trade-offs):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q057: Database sharding

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Data Scale |

### Question

What failure modes occur when Database sharding is misapplied in LLMOps & Responsible AI?

### Short Answer (30 seconds)

Database sharding: use when write scale beyond single node; avoid when day-one sharding for 100 users. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Database sharding** in the context of LLMOps & Responsible AI.

**When to use:** Write scale beyond single node

**When to avoid:** Day-one sharding for 100 users

**Production example:** Shard by tenantId hash

**Architect lens (Failure modes):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q058: Read replicas

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Data Scale |

### Question

How do you justify Read replicas to non-technical stakeholders in a LLMOps & Responsible AI initiative?

### Short Answer (30 seconds)

Read replicas: use when read-heavy workloads; avoid when strong consistency on replicas. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Read replicas** in the context of LLMOps & Responsible AI.

**When to use:** Read-heavy workloads

**When to avoid:** Strong consistency on replicas

**Production example:** 5:1 read/write ratio to replicas

**Architect lens (Stakeholder):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q059: Message queues

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Async |

### Question

How does Message queues affect cost and operability in LLMOps & Responsible AI?

### Short Answer (30 seconds)

Message queues: use when decouple producers/consumers; avoid when sync for fire-and-forget. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Message queues** in the context of LLMOps & Responsible AI.

**When to use:** Decouple producers/consumers

**When to avoid:** Sync for fire-and-forget

**Production example:** SQS between order and email

**Architect lens (Cost):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q060: Rate limiting

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |

### Question

At what scale does Rate limiting become necessary in LLMOps & Responsible AI?

### Short Answer (30 seconds)

Rate limiting: use when public apis, abuse prevention; avoid when internal-only admin apis. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Rate limiting** in the context of LLMOps & Responsible AI.

**When to use:** Public APIs, abuse prevention

**When to avoid:** Internal-only admin APIs

**Production example:** Token bucket at API gateway

**Architect lens (Scale):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q061: Multi-region design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Availability |

### Question

What are the trade-offs of Multi-region design in a production LLMOps & Responsible AI system?

### Short Answer (30 seconds)

Multi-region design: use when 99.99% sla, global users; avoid when cost-sensitive internal tools. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Multi-region design** in the context of LLMOps & Responsible AI.

**When to use:** 99.99% SLA, global users

**When to avoid:** Cost-sensitive internal tools

**Production example:** Active-passive with Traffic Manager

**Architect lens (Trade-offs):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q062: RESHADED framework

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Methodology |

### Question

What failure modes occur when RESHADED framework is misapplied in LLMOps & Responsible AI?

### Short Answer (30 seconds)

RESHADED framework: use when every whiteboard interview; avoid when jumping to boxes. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**RESHADED framework** in the context of LLMOps & Responsible AI.

**When to use:** Every whiteboard interview

**When to avoid:** Jumping to boxes

**Production example:** Requirements before components

**Architect lens (Failure modes):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q063: Capacity estimation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Estimation |

### Question

How do you justify Capacity estimation to non-technical stakeholders in a LLMOps & Responsible AI initiative?

### Short Answer (30 seconds)

Capacity estimation: use when back-of-envelope qps/storage; avoid when exact numbers without assumptions. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Capacity estimation** in the context of LLMOps & Responsible AI.

**When to use:** Back-of-envelope QPS/storage

**When to avoid:** Exact numbers without assumptions

**Production example:** 100M users × 10KB = 1TB profile data

**Architect lens (Stakeholder):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q064: Load balancing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Scale |

### Question

How does Load balancing affect cost and operability in LLMOps & Responsible AI?

### Short Answer (30 seconds)

Load balancing: use when horizontal scale; avoid when single server wishful thinking. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Load balancing** in the context of LLMOps & Responsible AI.

**When to use:** Horizontal scale

**When to avoid:** Single server wishful thinking

**Production example:** L7 ALB with health checks

**Architect lens (Cost):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q065: Caching layers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Caching |

### Question

At what scale does Caching layers become necessary in LLMOps & Responsible AI?

### Short Answer (30 seconds)

Caching layers: use when read-heavy, hot keys; avoid when cache everything including auth. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Caching layers** in the context of LLMOps & Responsible AI.

**When to use:** Read-heavy, hot keys

**When to avoid:** Cache everything including auth

**Production example:** Redis cache-aside for product pages

**Architect lens (Scale):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q066: CDN

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Edge |

### Question

What are the trade-offs of CDN in a production LLMOps & Responsible AI system?

### Short Answer (30 seconds)

CDN: use when static assets, global users; avoid when dynamic personalized api at edge. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**CDN** in the context of LLMOps & Responsible AI.

**When to use:** Static assets, global users

**When to avoid:** Dynamic personalized API at edge

**Production example:** CloudFront for SPA bundles

**Architect lens (Trade-offs):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q067: Database sharding

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Data Scale |

### Question

What failure modes occur when Database sharding is misapplied in LLMOps & Responsible AI?

### Short Answer (30 seconds)

Database sharding: use when write scale beyond single node; avoid when day-one sharding for 100 users. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Database sharding** in the context of LLMOps & Responsible AI.

**When to use:** Write scale beyond single node

**When to avoid:** Day-one sharding for 100 users

**Production example:** Shard by tenantId hash

**Architect lens (Failure modes):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q068: Read replicas

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Data Scale |

### Question

How do you justify Read replicas to non-technical stakeholders in a LLMOps & Responsible AI initiative?

### Short Answer (30 seconds)

Read replicas: use when read-heavy workloads; avoid when strong consistency on replicas. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Read replicas** in the context of LLMOps & Responsible AI.

**When to use:** Read-heavy workloads

**When to avoid:** Strong consistency on replicas

**Production example:** 5:1 read/write ratio to replicas

**Architect lens (Stakeholder):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q069: Message queues

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Async |

### Question

How does Message queues affect cost and operability in LLMOps & Responsible AI?

### Short Answer (30 seconds)

Message queues: use when decouple producers/consumers; avoid when sync for fire-and-forget. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Message queues** in the context of LLMOps & Responsible AI.

**When to use:** Decouple producers/consumers

**When to avoid:** Sync for fire-and-forget

**Production example:** SQS between order and email

**Architect lens (Cost):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---

## Q070: Rate limiting

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |

### Question

At what scale does Rate limiting become necessary in LLMOps & Responsible AI?

### Short Answer (30 seconds)

Rate limiting: use when public apis, abuse prevention; avoid when internal-only admin apis. In LLMOps & Responsible AI, this shapes reliability, cost, and team autonomy.

### Detailed Answer

**Rate limiting** in the context of LLMOps & Responsible AI.

**When to use:** Public APIs, abuse prevention

**When to avoid:** Internal-only admin APIs

**Production example:** Token bucket at API gateway

**Architect lens (Scale):** Document the decision in an ADR. Measure impact via SLIs — latency, error rate, and cost per transaction. Present trade-offs to stakeholders in business terms, not only technology.

---
