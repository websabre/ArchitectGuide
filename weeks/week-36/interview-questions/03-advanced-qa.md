# Week 36 — Advanced Q&A

> Q071–Q100: Premium format (Week 1 quality).

---


## Q071: E-Commerce High-Level Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | E-Commerce |
| **Frequency** | Very Common |

### Question

How would you implement E-Commerce High-Level Design with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Catalog, cart, checkout, payment, inventory, search — async order fulfillment.

### Detailed Answer (3–5 minutes)

**E-Commerce High-Level Design** (Capstone context)

Catalog, cart, checkout, payment, inventory, search — async order fulfillment.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

E-Commerce High-Level Design separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — E-Commerce-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q072: Checkout Flow Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Checkout |
| **Frequency** | Very Common |

### Question

How would you implement Checkout Flow Design with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Reserve inventory → payment → confirm → async ship; saga with compensation.

### Detailed Answer (3–5 minutes)

**Checkout Flow Design** (Capstone context)

Reserve inventory → payment → confirm → async ship; saga with compensation.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Checkout Flow Design separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Checkout-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q073: Uber-Like Matching Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Ride-Sharing |
| **Frequency** | Very Common |

### Question

How would you implement Uber-Like Matching Design with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Geospatial index, driver location stream, matching algorithm, surge pricing cache.

### Detailed Answer (3–5 minutes)

**Uber-Like Matching Design** (Capstone context)

Geospatial index, driver location stream, matching algorithm, surge pricing cache.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Uber-Like Matching Design separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Ride-Sharing-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q074: Notification System Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Notifications |
| **Frequency** | Very Common |

### Question

How would you implement Notification System Design with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Multi-channel fanout, template engine, preference center, rate limit per user.

### Detailed Answer (3–5 minutes)

**Notification System Design** (Capstone context)

Multi-channel fanout, template engine, preference center, rate limit per user.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Notification System Design separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Notifications-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q075: Search System Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Search |
| **Frequency** | Very Common |

### Question

How would you implement Search System Design with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Elasticsearch indexing pipeline, query parsing, ranking, autocomplete from trie/ES suggest.

### Detailed Answer (3–5 minutes)

**Search System Design** (Capstone context)

Elasticsearch indexing pipeline, query parsing, ranking, autocomplete from trie/ES suggest.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Search System Design separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Search-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q076: Payment Idempotency Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Payments |
| **Frequency** | Very Common |

### Question

How would you implement Payment Idempotency Design with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Idempotency-Key, ledger double-entry, webhook dedup, reconciliation batch.

### Detailed Answer (3–5 minutes)

**Payment Idempotency Design** (Capstone context)

Idempotency-Key, ledger double-entry, webhook dedup, reconciliation batch.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Payment Idempotency Design separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Payments-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q077: Inventory Consistency Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | E-Commerce |
| **Frequency** | Very Common |

### Question

How would you implement Inventory Consistency Design with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Optimistic concurrency, reservation TTL, oversell prevention audit.

### Detailed Answer (3–5 minutes)

**Inventory Consistency Design** (Capstone context)

Optimistic concurrency, reservation TTL, oversell prevention audit.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Inventory Consistency Design separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — E-Commerce-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q078: Cart Service Redis Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | E-Commerce |
| **Frequency** | Very Common |

### Question

How would you implement Cart Service Redis Design with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Redis hash per cart; TTL 30 days; merge anonymous on login.

### Detailed Answer (3–5 minutes)

**Cart Service Redis Design** (Capstone context)

Redis hash per cart; TTL 30 days; merge anonymous on login.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Cart Service Redis Design separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — E-Commerce-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q079: Product Catalog CDN Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | E-Commerce |
| **Frequency** | Very Common |

### Question

How would you implement Product Catalog CDN Design with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

CDN cache product pages; API cache-aside; invalidation on price change event.

### Detailed Answer (3–5 minutes)

**Product Catalog CDN Design** (Capstone context)

CDN cache product pages; API cache-aside; invalidation on price change event.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Product Catalog CDN Design separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — E-Commerce-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q080: Order Status Tracking

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | E-Commerce |
| **Frequency** | Very Common |

### Question

How would you implement Order Status Tracking with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

State machine; WebSocket or SSE push; event sourcing optional for audit.

### Detailed Answer (3–5 minutes)

**Order Status Tracking** (Capstone context)

State machine; WebSocket or SSE push; event sourcing optional for audit.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Order Status Tracking separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — E-Commerce-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q081: Recommendation Engine Integration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | E-Commerce |
| **Frequency** | Very Common |

### Question

How would you implement Recommendation Engine Integration with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Async batch + real-time feature store; fallback to popular if model down.

### Detailed Answer (3–5 minutes)

**Recommendation Engine Integration** (Capstone context)

Async batch + real-time feature store; fallback to popular if model down.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Recommendation Engine Integration separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — E-Commerce-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q082: Flash Sale Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | E-Commerce |
| **Frequency** | Very Common |

### Question

How would you implement Flash Sale Architecture with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Queue checkout, waiting room, cache inventory count, rate limit.

### Detailed Answer (3–5 minutes)

**Flash Sale Architecture** (Capstone context)

Queue checkout, waiting room, cache inventory count, rate limit.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Flash Sale Architecture separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — E-Commerce-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q083: Driver Location Geospatial

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Ride-Sharing |
| **Frequency** | Very Common |

### Question

How would you implement Driver Location Geospatial with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Redis GEO or H3 cells; update stream Kafka; query nearest N drivers.

### Detailed Answer (3–5 minutes)

**Driver Location Geospatial** (Capstone context)

Redis GEO or H3 cells; update stream Kafka; query nearest N drivers.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Driver Location Geospatial separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Ride-Sharing-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q084: Surge Pricing Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Ride-Sharing |
| **Frequency** | Very Common |

### Question

How would you implement Surge Pricing Design with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Demand/supply ratio per geohash; cache multiplier; broadcast price update.

### Detailed Answer (3–5 minutes)

**Surge Pricing Design** (Capstone context)

Demand/supply ratio per geohash; cache multiplier; broadcast price update.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Surge Pricing Design separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Ride-Sharing-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q085: Ride Matching Algorithm

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Ride-Sharing |
| **Frequency** | Very Common |

### Question

How would you implement Ride Matching Algorithm with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Greedy nearest; batch matching at scale; cancel and re-match flow.

### Detailed Answer (3–5 minutes)

**Ride Matching Algorithm** (Capstone context)

Greedy nearest; batch matching at scale; cancel and re-match flow.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Ride Matching Algorithm separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Ride-Sharing-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q086: Push Notification Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Notifications |
| **Frequency** | Very Common |

### Question

How would you implement Push Notification Scale with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

APNs/FCM token registry; batch send; priority queue for OTP.

### Detailed Answer (3–5 minutes)

**Push Notification Scale** (Capstone context)

APNs/FCM token registry; batch send; priority queue for OTP.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Push Notification Scale separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Notifications-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q087: Email SMS Notification Pipeline

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Notifications |
| **Frequency** | Very Common |

### Question

How would you implement Email SMS Notification Pipeline with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Queue workers per channel; provider failover; unsubscribe compliance.

### Detailed Answer (3–5 minutes)

**Email SMS Notification Pipeline** (Capstone context)

Queue workers per channel; provider failover; unsubscribe compliance.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Email SMS Notification Pipeline separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Notifications-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q088: Notification Preference Store

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Notifications |
| **Frequency** | Very Common |

### Question

How would you implement Notification Preference Store with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Per-user channel prefs; quiet hours; GDPR marketing opt-out.

### Detailed Answer (3–5 minutes)

**Notification Preference Store** (Capstone context)

Per-user channel prefs; quiet hours; GDPR marketing opt-out.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Notification Preference Store separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Notifications-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q089: Search Index Pipeline

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Search |
| **Frequency** | Very Common |

### Question

How would you implement Search Index Pipeline with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

CDC from DB → Kafka → ES bulk index; alias swap for reindex.

### Detailed Answer (3–5 minutes)

**Search Index Pipeline** (Capstone context)

CDC from DB → Kafka → ES bulk index; alias swap for reindex.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Search Index Pipeline separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Search-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q090: Autocomplete Latency

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Search |
| **Frequency** | Very Common |

### Question

How would you implement Autocomplete Latency with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

ES completion suggester <50ms; prefix cache; debounce client.

### Detailed Answer (3–5 minutes)

**Autocomplete Latency** (Capstone context)

ES completion suggester <50ms; prefix cache; debounce client.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Autocomplete Latency separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Search-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q091: Full Stack Observability Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Capstone |
| **Frequency** | Common |

### Question

How would you implement Full Stack Observability Design with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Trace checkout path end-to-end; SLO per step; alert on burn.

### Detailed Answer (3–5 minutes)

**Full Stack Observability Design** (Capstone context)

Trace checkout path end-to-end; SLO per step; alert on burn.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Full Stack Observability Design separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Capstone-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q092: Multi-Region E-Commerce

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | E-Commerce |
| **Frequency** | Common |

### Question

How would you implement Multi-Region E-Commerce with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Read local catalog; write central orders or cell-based users.

### Detailed Answer (3–5 minutes)

**Multi-Region E-Commerce** (Capstone context)

Read local catalog; write central orders or cell-based users.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Multi-Region E-Commerce separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — E-Commerce-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q093: Fraud Detection Hook

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Payments |
| **Frequency** | Common |

### Question

How would you implement Fraud Detection Hook with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Pre-auth fraud score; async ML; block high-risk before capture.

### Detailed Answer (3–5 minutes)

**Fraud Detection Hook** (Capstone context)

Pre-auth fraud score; async ML; block high-risk before capture.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Fraud Detection Hook separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Payments-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q094: Return Refund Flow

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | E-Commerce |
| **Frequency** | Common |

### Question

How would you implement Return Refund Flow with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Reverse saga; inventory return; partial refund state machine.

### Detailed Answer (3–5 minutes)

**Return Refund Flow** (Capstone context)

Reverse saga; inventory return; partial refund state machine.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Return Refund Flow separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — E-Commerce-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q095: Wishlist and Personalization

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | E-Commerce |
| **Frequency** | Common |

### Question

How would you implement Wishlist and Personalization with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

User-scoped data; event stream for recommendations.

### Detailed Answer (3–5 minutes)

**Wishlist and Personalization** (Capstone context)

User-scoped data; event stream for recommendations.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Wishlist and Personalization separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — E-Commerce-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q096: Rate Limit Public APIs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | API Design |
| **Frequency** | Common |

### Question

How would you implement Rate Limit Public APIs with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Tier per API key; sliding window Redis; 429 response.

### Detailed Answer (3–5 minutes)

**Rate Limit Public APIs** (Capstone context)

Tier per API key; sliding window Redis; 429 response.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Rate Limit Public APIs separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — API Design-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q097: API Gateway Aggregation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | API Design |
| **Frequency** | Common |

### Question

How would you implement API Gateway Aggregation with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

BFF aggregates cart+user+promo; reduce chatty mobile calls.

### Detailed Answer (3–5 minutes)

**API Gateway Aggregation** (Capstone context)

BFF aggregates cart+user+promo; reduce chatty mobile calls.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

API Gateway Aggregation separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — API Design-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q098: Data Model E-Commerce

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Data Model |
| **Frequency** | Common |

### Question

How would you implement Data Model E-Commerce with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Orders, line items, payments, shipments — access pattern driven.

### Detailed Answer (3–5 minutes)

**Data Model E-Commerce** (Capstone context)

Orders, line items, payments, shipments — access pattern driven.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Data Model E-Commerce separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Data Model-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q099: Capstone Time Management

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Interview Skills |
| **Frequency** | Common |

### Question

How would you implement Capstone Time Management with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

45-min full design: 5 clarify, 10 boxes, 20 checkout deep dive, 5 scale.

### Detailed Answer (3–5 minutes)

**Capstone Time Management** (Capstone context)

45-min full design: 5 clarify, 10 boxes, 20 checkout deep dive, 5 scale.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Capstone Time Management separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Interview Skills-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q100: Capstone Phased Evolution

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Interview Skills |
| **Frequency** | Common |

### Question

How would you implement Capstone Phased Evolution with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

MVP → scale → global — close every capstone with phases.

### Detailed Answer (3–5 minutes)

**Capstone Phased Evolution** (Capstone context)

MVP → scale → global — close every capstone with phases.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Capstone Phased Evolution separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Interview Skills-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---
