# Week 40 — Expert Q&A

---


## Q101: AI Architecture Capstone — Production incident — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Methodology |
| **Type** | Scenario |

### Scenario

A AI Architecture Capstone system experiences cascading failures. Walk through your response using concepts including RESHADED framework.

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply RESHADED framework correctly (Every whiteboard interview)
- Avoid anti-pattern: Jumping to boxes
- Reference: Requirements before components

---

## Q102: AI Architecture Capstone — Architecture review — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Estimation |
| **Type** | Scenario |

### Scenario

Review a team's AI Architecture Capstone design that omits Capacity estimation. What risks do you flag?

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply Capacity estimation correctly (Back-of-envelope QPS/storage)
- Avoid anti-pattern: Exact numbers without assumptions
- Reference: 100M users × 10KB = 1TB profile data

---

## Q103: AI Architecture Capstone — Build vs buy — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scale |
| **Type** | Scenario |

### Scenario

Leadership wants to build in-house vs buy SaaS for AI Architecture Capstone. How does Load balancing inform your recommendation?

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply Load balancing correctly (Horizontal scale)
- Avoid anti-pattern: Single server wishful thinking
- Reference: L7 ALB with health checks

---

## Q104: AI Architecture Capstone — Regulatory audit — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Caching |
| **Type** | Scenario |

### Scenario

Auditors question your AI Architecture Capstone architecture regarding Caching layers. How do you respond?

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply Caching layers correctly (Read-heavy, hot keys)
- Avoid anti-pattern: Cache everything including auth
- Reference: Redis cache-aside for product pages

---

## Q105: AI Architecture Capstone — Scale 10x — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Edge |
| **Type** | Scenario |

### Scenario

Traffic will 10x in 6 months. What changes involving CDN do you prioritize in AI Architecture Capstone?

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply CDN correctly (Static assets, global users)
- Avoid anti-pattern: Dynamic personalized API at edge
- Reference: CloudFront for SPA bundles

---

## Q106: AI Architecture Capstone — Production incident — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Data Scale |
| **Type** | Scenario |

### Scenario

A AI Architecture Capstone system experiences cascading failures. Walk through your response using concepts including Database sharding.

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply Database sharding correctly (Write scale beyond single node)
- Avoid anti-pattern: Day-one sharding for 100 users
- Reference: Shard by tenantId hash

---

## Q107: AI Architecture Capstone — Architecture review — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Data Scale |
| **Type** | Scenario |

### Scenario

Review a team's AI Architecture Capstone design that omits Read replicas. What risks do you flag?

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply Read replicas correctly (Read-heavy workloads)
- Avoid anti-pattern: Strong consistency on replicas
- Reference: 5:1 read/write ratio to replicas

---

## Q108: AI Architecture Capstone — Build vs buy — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Async |
| **Type** | Scenario |

### Scenario

Leadership wants to build in-house vs buy SaaS for AI Architecture Capstone. How does Message queues inform your recommendation?

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply Message queues correctly (Decouple producers/consumers)
- Avoid anti-pattern: Sync for fire-and-forget
- Reference: SQS between order and email

---

## Q109: AI Architecture Capstone — Regulatory audit — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Security |
| **Type** | Scenario |

### Scenario

Auditors question your AI Architecture Capstone architecture regarding Rate limiting. How do you respond?

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply Rate limiting correctly (Public APIs, abuse prevention)
- Avoid anti-pattern: Internal-only admin APIs
- Reference: Token bucket at API gateway

---

## Q110: AI Architecture Capstone — Scale 10x — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Availability |
| **Type** | Scenario |

### Scenario

Traffic will 10x in 6 months. What changes involving Multi-region design do you prioritize in AI Architecture Capstone?

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply Multi-region design correctly (99.99% SLA, global users)
- Avoid anti-pattern: Cost-sensitive internal tools
- Reference: Active-passive with Traffic Manager

---

## Q111: AI Architecture Capstone — Production incident — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Methodology |
| **Type** | Scenario |

### Scenario

A AI Architecture Capstone system experiences cascading failures. Walk through your response using concepts including RESHADED framework.

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply RESHADED framework correctly (Every whiteboard interview)
- Avoid anti-pattern: Jumping to boxes
- Reference: Requirements before components

---

## Q112: AI Architecture Capstone — Architecture review — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Estimation |
| **Type** | Scenario |

### Scenario

Review a team's AI Architecture Capstone design that omits Capacity estimation. What risks do you flag?

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply Capacity estimation correctly (Back-of-envelope QPS/storage)
- Avoid anti-pattern: Exact numbers without assumptions
- Reference: 100M users × 10KB = 1TB profile data

---

## Q113: AI Architecture Capstone — Build vs buy — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scale |
| **Type** | Scenario |

### Scenario

Leadership wants to build in-house vs buy SaaS for AI Architecture Capstone. How does Load balancing inform your recommendation?

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply Load balancing correctly (Horizontal scale)
- Avoid anti-pattern: Single server wishful thinking
- Reference: L7 ALB with health checks

---

## Q114: AI Architecture Capstone — Regulatory audit — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Caching |
| **Type** | Scenario |

### Scenario

Auditors question your AI Architecture Capstone architecture regarding Caching layers. How do you respond?

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply Caching layers correctly (Read-heavy, hot keys)
- Avoid anti-pattern: Cache everything including auth
- Reference: Redis cache-aside for product pages

---

## Q115: AI Architecture Capstone — Scale 10x — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Edge |
| **Type** | Scenario |

### Scenario

Traffic will 10x in 6 months. What changes involving CDN do you prioritize in AI Architecture Capstone?

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply CDN correctly (Static assets, global users)
- Avoid anti-pattern: Dynamic personalized API at edge
- Reference: CloudFront for SPA bundles

---

## Q116: AI Architecture Capstone — Production incident — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Data Scale |
| **Type** | Scenario |

### Scenario

A AI Architecture Capstone system experiences cascading failures. Walk through your response using concepts including Database sharding.

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply Database sharding correctly (Write scale beyond single node)
- Avoid anti-pattern: Day-one sharding for 100 users
- Reference: Shard by tenantId hash

---

## Q117: AI Architecture Capstone — Architecture review — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Data Scale |
| **Type** | Scenario |

### Scenario

Review a team's AI Architecture Capstone design that omits Read replicas. What risks do you flag?

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply Read replicas correctly (Read-heavy workloads)
- Avoid anti-pattern: Strong consistency on replicas
- Reference: 5:1 read/write ratio to replicas

---

## Q118: AI Architecture Capstone — Build vs buy — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Async |
| **Type** | Scenario |

### Scenario

Leadership wants to build in-house vs buy SaaS for AI Architecture Capstone. How does Message queues inform your recommendation?

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply Message queues correctly (Decouple producers/consumers)
- Avoid anti-pattern: Sync for fire-and-forget
- Reference: SQS between order and email

---

## Q119: AI Architecture Capstone — Regulatory audit — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Security |
| **Type** | Scenario |

### Scenario

Auditors question your AI Architecture Capstone architecture regarding Rate limiting. How do you respond?

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply Rate limiting correctly (Public APIs, abuse prevention)
- Avoid anti-pattern: Internal-only admin APIs
- Reference: Token bucket at API gateway

---

## Q120: AI Architecture Capstone — Scale 10x — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Availability |
| **Type** | Scenario |

### Scenario

Traffic will 10x in 6 months. What changes involving Multi-region design do you prioritize in AI Architecture Capstone?

### What Interviewers Evaluate

Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.

### Recommended Response Structure

Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.

### Key Points to Cover

- Apply Multi-region design correctly (99.99% SLA, global users)
- Avoid anti-pattern: Cost-sensitive internal tools
- Reference: Active-passive with Traffic Manager

---
