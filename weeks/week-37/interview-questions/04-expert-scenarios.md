# Week 37 — Expert Q&A

---


## Q101: AI/ML Architecture — Build vs buy — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Async |
| **Type** | Scenario |

### Scenario

Leadership wants to build in-house vs buy SaaS for AI/ML Architecture. How does Message queues inform your recommendation?

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply Message queues correctly (Decouple producers/consumers)
- Avoid anti-pattern: Sync for fire-and-forget
- Reference: SQS between order and email

---

## Q102: AI/ML Architecture — Regulatory audit — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Security |
| **Type** | Scenario |

### Scenario

Auditors question your AI/ML Architecture architecture regarding Rate limiting. How do you respond?

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply Rate limiting correctly (Public APIs, abuse prevention)
- Avoid anti-pattern: Internal-only admin APIs
- Reference: Token bucket at API gateway

---

## Q103: AI/ML Architecture — Scale 10x — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Availability |
| **Type** | Scenario |

### Scenario

Traffic will 10x in 6 months. What changes involving Multi-region design do you prioritize in AI/ML Architecture?

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply Multi-region design correctly (99.99% SLA, global users)
- Avoid anti-pattern: Cost-sensitive internal tools
- Reference: Active-passive with Traffic Manager

---

## Q104: AI/ML Architecture — Production incident — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Methodology |
| **Type** | Scenario |

### Scenario

A AI/ML Architecture system experiences cascading failures. Walk through your response using concepts including RESHADED framework.

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply RESHADED framework correctly (Every whiteboard interview)
- Avoid anti-pattern: Jumping to boxes
- Reference: Requirements before components

---

## Q105: AI/ML Architecture — Architecture review — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Estimation |
| **Type** | Scenario |

### Scenario

Review a team's AI/ML Architecture design that omits Capacity estimation. What risks do you flag?

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply Capacity estimation correctly (Back-of-envelope QPS/storage)
- Avoid anti-pattern: Exact numbers without assumptions
- Reference: 100M users × 10KB = 1TB profile data

---

## Q106: AI/ML Architecture — Build vs buy — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scale |
| **Type** | Scenario |

### Scenario

Leadership wants to build in-house vs buy SaaS for AI/ML Architecture. How does Load balancing inform your recommendation?

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply Load balancing correctly (Horizontal scale)
- Avoid anti-pattern: Single server wishful thinking
- Reference: L7 ALB with health checks

---

## Q107: AI/ML Architecture — Regulatory audit — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Caching |
| **Type** | Scenario |

### Scenario

Auditors question your AI/ML Architecture architecture regarding Caching layers. How do you respond?

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply Caching layers correctly (Read-heavy, hot keys)
- Avoid anti-pattern: Cache everything including auth
- Reference: Redis cache-aside for product pages

---

## Q108: AI/ML Architecture — Scale 10x — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Edge |
| **Type** | Scenario |

### Scenario

Traffic will 10x in 6 months. What changes involving CDN do you prioritize in AI/ML Architecture?

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply CDN correctly (Static assets, global users)
- Avoid anti-pattern: Dynamic personalized API at edge
- Reference: CloudFront for SPA bundles

---

## Q109: AI/ML Architecture — Production incident — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Data Scale |
| **Type** | Scenario |

### Scenario

A AI/ML Architecture system experiences cascading failures. Walk through your response using concepts including Database sharding.

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply Database sharding correctly (Write scale beyond single node)
- Avoid anti-pattern: Day-one sharding for 100 users
- Reference: Shard by tenantId hash

---

## Q110: AI/ML Architecture — Architecture review — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Data Scale |
| **Type** | Scenario |

### Scenario

Review a team's AI/ML Architecture design that omits Read replicas. What risks do you flag?

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply Read replicas correctly (Read-heavy workloads)
- Avoid anti-pattern: Strong consistency on replicas
- Reference: 5:1 read/write ratio to replicas

---

## Q111: AI/ML Architecture — Build vs buy — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Async |
| **Type** | Scenario |

### Scenario

Leadership wants to build in-house vs buy SaaS for AI/ML Architecture. How does Message queues inform your recommendation?

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply Message queues correctly (Decouple producers/consumers)
- Avoid anti-pattern: Sync for fire-and-forget
- Reference: SQS between order and email

---

## Q112: AI/ML Architecture — Regulatory audit — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Security |
| **Type** | Scenario |

### Scenario

Auditors question your AI/ML Architecture architecture regarding Rate limiting. How do you respond?

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply Rate limiting correctly (Public APIs, abuse prevention)
- Avoid anti-pattern: Internal-only admin APIs
- Reference: Token bucket at API gateway

---

## Q113: AI/ML Architecture — Scale 10x — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Availability |
| **Type** | Scenario |

### Scenario

Traffic will 10x in 6 months. What changes involving Multi-region design do you prioritize in AI/ML Architecture?

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply Multi-region design correctly (99.99% SLA, global users)
- Avoid anti-pattern: Cost-sensitive internal tools
- Reference: Active-passive with Traffic Manager

---

## Q114: AI/ML Architecture — Production incident — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Methodology |
| **Type** | Scenario |

### Scenario

A AI/ML Architecture system experiences cascading failures. Walk through your response using concepts including RESHADED framework.

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply RESHADED framework correctly (Every whiteboard interview)
- Avoid anti-pattern: Jumping to boxes
- Reference: Requirements before components

---

## Q115: AI/ML Architecture — Architecture review — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Estimation |
| **Type** | Scenario |

### Scenario

Review a team's AI/ML Architecture design that omits Capacity estimation. What risks do you flag?

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply Capacity estimation correctly (Back-of-envelope QPS/storage)
- Avoid anti-pattern: Exact numbers without assumptions
- Reference: 100M users × 10KB = 1TB profile data

---

## Q116: AI/ML Architecture — Build vs buy — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scale |
| **Type** | Scenario |

### Scenario

Leadership wants to build in-house vs buy SaaS for AI/ML Architecture. How does Load balancing inform your recommendation?

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply Load balancing correctly (Horizontal scale)
- Avoid anti-pattern: Single server wishful thinking
- Reference: L7 ALB with health checks

---

## Q117: AI/ML Architecture — Regulatory audit — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Caching |
| **Type** | Scenario |

### Scenario

Auditors question your AI/ML Architecture architecture regarding Caching layers. How do you respond?

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply Caching layers correctly (Read-heavy, hot keys)
- Avoid anti-pattern: Cache everything including auth
- Reference: Redis cache-aside for product pages

---

## Q118: AI/ML Architecture — Scale 10x — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Edge |
| **Type** | Scenario |

### Scenario

Traffic will 10x in 6 months. What changes involving CDN do you prioritize in AI/ML Architecture?

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply CDN correctly (Static assets, global users)
- Avoid anti-pattern: Dynamic personalized API at edge
- Reference: CloudFront for SPA bundles

---

## Q119: AI/ML Architecture — Production incident — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Data Scale |
| **Type** | Scenario |

### Scenario

A AI/ML Architecture system experiences cascading failures. Walk through your response using concepts including Database sharding.

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply Database sharding correctly (Write scale beyond single node)
- Avoid anti-pattern: Day-one sharding for 100 users
- Reference: Shard by tenantId hash

---

## Q120: AI/ML Architecture — Architecture review — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Data Scale |
| **Type** | Scenario |

### Scenario

Review a team's AI/ML Architecture design that omits Read replicas. What risks do you flag?

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply Read replicas correctly (Read-heavy workloads)
- Avoid anti-pattern: Strong consistency on replicas
- Reference: 5:1 read/write ratio to replicas

---
