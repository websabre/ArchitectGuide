# Week 34 — Advanced Q&A

> Q071–Q100: Premium format (Week 1 quality).

---


## Q071: Cache-Aside Pattern .NET

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Caching |
| **Frequency** | Very Common |

### Question

How would you implement Cache-Aside Pattern .NET with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Read: check Redis, miss → DB → populate. Write: update DB, invalidate cache key.

### Detailed Answer (3–5 minutes)

**Cache-Aside Pattern .NET** (Scalability context)

Read: check Redis, miss → DB → populate. Write: update DB, invalidate cache key.

**Production implementation:**
```csharp
var cached = await _cache.GetAsync<Product>(key);
if (cached is null) {
    cached = await _db.Products.FindAsync(id);
    await _cache.SetAsync(key, cached, TimeSpan.FromMinutes(5));
}
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

Cache-Aside Pattern .NET separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Caching-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q072: Read-Through vs Write-Through

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Caching |
| **Frequency** | Very Common |

### Question

How would you implement Read-Through vs Write-Through with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Read-through: cache loads on miss. Write-through: sync write cache+DB. Choose per consistency need.

### Detailed Answer (3–5 minutes)

**Read-Through vs Write-Through** (Scalability context)

Read-through: cache loads on miss. Write-through: sync write cache+DB. Choose per consistency need.

**Production implementation:**
```csharp
var cached = await _cache.GetAsync<Product>(key);
if (cached is null) {
    cached = await _db.Products.FindAsync(id);
    await _cache.SetAsync(key, cached, TimeSpan.FromMinutes(5));
}
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

Read-Through vs Write-Through separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Caching-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q073: CDN Azure Front Door

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | CDN |
| **Frequency** | Very Common |

### Question

How would you implement CDN Azure Front Door with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Static assets, cacheable API GETs; cache key rules; purge on deploy via versioned URLs.

### Detailed Answer (3–5 minutes)

**CDN Azure Front Door** (Scalability context)

Static assets, cacheable API GETs; cache key rules; purge on deploy via versioned URLs.

**Production implementation:**
```csharp
var cached = await _cache.GetAsync<Product>(key);
if (cached is null) {
    cached = await _db.Products.FindAsync(id);
    await _cache.SetAsync(key, cached, TimeSpan.FromMinutes(5));
}
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

CDN Azure Front Door separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — CDN-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q074: Database Read Replicas

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Scaling |
| **Frequency** | Very Common |

### Question

How would you implement Database Read Replicas with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Route analytics to replica; primary for writes; monitor replication lag threshold.

### Detailed Answer (3–5 minutes)

**Database Read Replicas** (Scalability context)

Route analytics to replica; primary for writes; monitor replication lag threshold.

**Production implementation:**
```csharp
var cached = await _cache.GetAsync<Product>(key);
if (cached is null) {
    cached = await _db.Products.FindAsync(id);
    await _cache.SetAsync(key, cached, TimeSpan.FromMinutes(5));
}
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

Database Read Replicas separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Scaling-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q075: Horizontal Sharding Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Sharding |
| **Frequency** | Very Common |

### Question

How would you implement Horizontal Sharding Strategy with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Shard key: tenantId hash; avoid cross-shard queries in hot path; resharding plan documented.

### Detailed Answer (3–5 minutes)

**Horizontal Sharding Strategy** (Scalability context)

Shard key: tenantId hash; avoid cross-shard queries in hot path; resharding plan documented.

**Production implementation:**
```csharp
var cached = await _cache.GetAsync<Product>(key);
if (cached is null) {
    cached = await _db.Products.FindAsync(id);
    await _cache.SetAsync(key, cached, TimeSpan.FromMinutes(5));
}
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

Horizontal Sharding Strategy separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Sharding-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q076: Load Balancer Layer 7

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Load Balancing |
| **Frequency** | Very Common |

### Question

How would you implement Load Balancer Layer 7 with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Azure App Gateway path routing, WAF, cookie affinity only when required.

### Detailed Answer (3–5 minutes)

**Load Balancer Layer 7** (Scalability context)

Azure App Gateway path routing, WAF, cookie affinity only when required.

**Production implementation:**
```csharp
var cached = await _cache.GetAsync<Product>(key);
if (cached is null) {
    cached = await _db.Products.FindAsync(id);
    await _cache.SetAsync(key, cached, TimeSpan.FromMinutes(5));
}
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

Load Balancer Layer 7 separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Load Balancing-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q077: Hot Key Mitigation Redis

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Caching |
| **Frequency** | Very Common |

### Question

How would you implement Hot Key Mitigation Redis with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Split key replicas, local L1 cache, read replicas, request coalescing.

### Detailed Answer (3–5 minutes)

**Hot Key Mitigation Redis** (Scalability context)

Split key replicas, local L1 cache, read replicas, request coalescing.

**Production implementation:**
```csharp
var cached = await _cache.GetAsync<Product>(key);
if (cached is null) {
    cached = await _db.Products.FindAsync(id);
    await _cache.SetAsync(key, cached, TimeSpan.FromMinutes(5));
}
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

Hot Key Mitigation Redis separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Caching-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q078: Cache Stampede Prevention

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Caching |
| **Frequency** | Very Common |

### Question

How would you implement Cache Stampede Prevention with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

TTL jitter, single-flight mutex, stale-while-revalidate, probabilistic early refresh.

### Detailed Answer (3–5 minutes)

**Cache Stampede Prevention** (Scalability context)

TTL jitter, single-flight mutex, stale-while-revalidate, probabilistic early refresh.

**Production implementation:**
```csharp
var cached = await _cache.GetAsync<Product>(key);
if (cached is null) {
    cached = await _db.Products.FindAsync(id);
    await _cache.SetAsync(key, cached, TimeSpan.FromMinutes(5));
}
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

Cache Stampede Prevention separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Caching-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q079: Write-Behind Caching

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Caching |
| **Frequency** | Very Common |

### Question

How would you implement Write-Behind Caching with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Buffer writes to cache, async flush to DB — risk of data loss; only for analytics counts.

### Detailed Answer (3–5 minutes)

**Write-Behind Caching** (Scalability context)

Buffer writes to cache, async flush to DB — risk of data loss; only for analytics counts.

**Production implementation:**
```csharp
var cached = await _cache.GetAsync<Product>(key);
if (cached is null) {
    cached = await _db.Products.FindAsync(id);
    await _cache.SetAsync(key, cached, TimeSpan.FromMinutes(5));
}
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

Write-Behind Caching separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Caching-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q080: Cache Invalidation Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Caching |
| **Frequency** | Very Common |

### Question

How would you implement Cache Invalidation Strategy with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

TTL + event-driven invalidation on write; versioned cache keys for deploy safety.

### Detailed Answer (3–5 minutes)

**Cache Invalidation Strategy** (Scalability context)

TTL + event-driven invalidation on write; versioned cache keys for deploy safety.

**Production implementation:**
```csharp
var cached = await _cache.GetAsync<Product>(key);
if (cached is null) {
    cached = await _db.Products.FindAsync(id);
    await _cache.SetAsync(key, cached, TimeSpan.FromMinutes(5));
}
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

Cache Invalidation Strategy separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Caching-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q081: Consistent Hashing Ring

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Distributed Cache |
| **Frequency** | Very Common |

### Question

How would you implement Consistent Hashing Ring with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Redis Cluster slot migration; minimal key remap on node add/remove.

### Detailed Answer (3–5 minutes)

**Consistent Hashing Ring** (Scalability context)

Redis Cluster slot migration; minimal key remap on node add/remove.

**Production implementation:**
```csharp
var cached = await _cache.GetAsync<Product>(key);
if (cached is null) {
    cached = await _db.Products.FindAsync(id);
    await _cache.SetAsync(key, cached, TimeSpan.FromMinutes(5));
}
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

Consistent Hashing Ring separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Distributed Cache-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q082: Connection Pool Sizing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Scaling |
| **Frequency** | Very Common |

### Question

How would you implement Connection Pool Sizing with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

pods × pool size < DB max_connections; formula in runbook.

### Detailed Answer (3–5 minutes)

**Connection Pool Sizing** (Scalability context)

pods × pool size < DB max_connections; formula in runbook.

**Production implementation:**
```csharp
var cached = await _cache.GetAsync<Product>(key);
if (cached is null) {
    cached = await _db.Products.FindAsync(id);
    await _cache.SetAsync(key, cached, TimeSpan.FromMinutes(5));
}
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

Connection Pool Sizing separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Scaling-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q083: Autoscale Rules AKS

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Scaling |
| **Frequency** | Very Common |

### Question

How would you implement Autoscale Rules AKS with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

CPU + custom metric (queue depth); scale-out fast, scale-in slow; min replicas for baseline.

### Detailed Answer (3–5 minutes)

**Autoscale Rules AKS** (Scalability context)

CPU + custom metric (queue depth); scale-out fast, scale-in slow; min replicas for baseline.

**Production implementation:**
```csharp
var cached = await _cache.GetAsync<Product>(key);
if (cached is null) {
    cached = await _db.Products.FindAsync(id);
    await _cache.SetAsync(key, cached, TimeSpan.FromMinutes(5));
}
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

Autoscale Rules AKS separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Scaling-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q084: Database Vertical Scale Limits

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Scaling |
| **Frequency** | Very Common |

### Question

How would you implement Database Vertical Scale Limits with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

When CPU >70% sustained — plan shard before vertical ceiling.

### Detailed Answer (3–5 minutes)

**Database Vertical Scale Limits** (Scalability context)

When CPU >70% sustained — plan shard before vertical ceiling.

**Production implementation:**
```csharp
var cached = await _cache.GetAsync<Product>(key);
if (cached is null) {
    cached = await _db.Products.FindAsync(id);
    await _cache.SetAsync(key, cached, TimeSpan.FromMinutes(5));
}
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

Database Vertical Scale Limits separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Scaling-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q085: Geo-Distributed Cache

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Caching |
| **Frequency** | Very Common |

### Question

How would you implement Geo-Distributed Cache with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Redis Enterprise active-active; session stickiness; conflict resolution policy.

### Detailed Answer (3–5 minutes)

**Geo-Distributed Cache** (Scalability context)

Redis Enterprise active-active; session stickiness; conflict resolution policy.

**Production implementation:**
```csharp
var cached = await _cache.GetAsync<Product>(key);
if (cached is null) {
    cached = await _db.Products.FindAsync(id);
    await _cache.SetAsync(key, cached, TimeSpan.FromMinutes(5));
}
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

Geo-Distributed Cache separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Caching-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q086: Cache Warming Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Caching |
| **Frequency** | Very Common |

### Question

How would you implement Cache Warming Strategy with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Pre-load hot keys before launch; scheduled refresh; monitor hit rate.

### Detailed Answer (3–5 minutes)

**Cache Warming Strategy** (Scalability context)

Pre-load hot keys before launch; scheduled refresh; monitor hit rate.

**Production implementation:**
```csharp
var cached = await _cache.GetAsync<Product>(key);
if (cached is null) {
    cached = await _db.Products.FindAsync(id);
    await _cache.SetAsync(key, cached, TimeSpan.FromMinutes(5));
}
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

Cache Warming Strategy separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Caching-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q087: Negative Caching

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Caching |
| **Frequency** | Very Common |

### Question

How would you implement Negative Caching with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Cache 404 for non-existent keys short TTL — prevent DB hammer on attacks.

### Detailed Answer (3–5 minutes)

**Negative Caching** (Scalability context)

Cache 404 for non-existent keys short TTL — prevent DB hammer on attacks.

**Production implementation:**
```csharp
var cached = await _cache.GetAsync<Product>(key);
if (cached is null) {
    cached = await _db.Products.FindAsync(id);
    await _cache.SetAsync(key, cached, TimeSpan.FromMinutes(5));
}
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

Negative Caching separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Caching-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q088: Cache Penetration Attack

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Caching |
| **Frequency** | Very Common |

### Question

How would you implement Cache Penetration Attack with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Bloom filter for existence; rate limit; random TTL on miss.

### Detailed Answer (3–5 minutes)

**Cache Penetration Attack** (Scalability context)

Bloom filter for existence; rate limit; random TTL on miss.

**Production implementation:**
```csharp
var cached = await _cache.GetAsync<Product>(key);
if (cached is null) {
    cached = await _db.Products.FindAsync(id);
    await _cache.SetAsync(key, cached, TimeSpan.FromMinutes(5));
}
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

Cache Penetration Attack separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Caching-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q089: Multi-Level Cache

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Caching |
| **Frequency** | Very Common |

### Question

How would you implement Multi-Level Cache with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

L1 in-memory 2s TTL + L2 Redis + L3 CDN — measure hit rate per tier.

### Detailed Answer (3–5 minutes)

**Multi-Level Cache** (Scalability context)

L1 in-memory 2s TTL + L2 Redis + L3 CDN — measure hit rate per tier.

**Production implementation:**
```csharp
var cached = await _cache.GetAsync<Product>(key);
if (cached is null) {
    cached = await _db.Products.FindAsync(id);
    await _cache.SetAsync(key, cached, TimeSpan.FromMinutes(5));
}
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

Multi-Level Cache separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Caching-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q090: Shard Key Selection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Sharding |
| **Frequency** | Very Common |

### Question

How would you implement Shard Key Selection with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

High cardinality, even distribution, query locality — tenantId classic for SaaS.

### Detailed Answer (3–5 minutes)

**Shard Key Selection** (Scalability context)

High cardinality, even distribution, query locality — tenantId classic for SaaS.

**Production implementation:**
```csharp
var cached = await _cache.GetAsync<Product>(key);
if (cached is null) {
    cached = await _db.Products.FindAsync(id);
    await _cache.SetAsync(key, cached, TimeSpan.FromMinutes(5));
}
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

Shard Key Selection separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Sharding-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q091: Read Your Writes

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Consistency |
| **Frequency** | Common |

### Question

How would you implement Read Your Writes with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Session token routes to primary post-write; or short TTL blocking read.

### Detailed Answer (3–5 minutes)

**Read Your Writes** (Scalability context)

Session token routes to primary post-write; or short TTL blocking read.

**Production implementation:**
```csharp
var cached = await _cache.GetAsync<Product>(key);
if (cached is null) {
    cached = await _db.Products.FindAsync(id);
    await _cache.SetAsync(key, cached, TimeSpan.FromMinutes(5));
}
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

Read Your Writes separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Consistency-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q092: Replica Lag Handling

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Scaling |
| **Frequency** | Common |

### Question

How would you implement Replica Lag Handling with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Monitor lag; route away if >5s; stale read acceptable endpoints documented.

### Detailed Answer (3–5 minutes)

**Replica Lag Handling** (Scalability context)

Monitor lag; route away if >5s; stale read acceptable endpoints documented.

**Production implementation:**
```csharp
var cached = await _cache.GetAsync<Product>(key);
if (cached is null) {
    cached = await _db.Products.FindAsync(id);
    await _cache.SetAsync(key, cached, TimeSpan.FromMinutes(5));
}
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

Replica Lag Handling separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Scaling-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q093: Load Test Methodology

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Scaling |
| **Frequency** | Common |

### Question

How would you implement Load Test Methodology with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Baseline, 2× peak, soak 4hr, spike — in staging with prod-like data volume.

### Detailed Answer (3–5 minutes)

**Load Test Methodology** (Scalability context)

Baseline, 2× peak, soak 4hr, spike — in staging with prod-like data volume.

**Production implementation:**
```csharp
var cached = await _cache.GetAsync<Product>(key);
if (cached is null) {
    cached = await _db.Products.FindAsync(id);
    await _cache.SetAsync(key, cached, TimeSpan.FromMinutes(5));
}
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

Load Test Methodology separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Scaling-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q094: Rate Limit at Edge

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Scaling |
| **Frequency** | Common |

### Question

How would you implement Rate Limit at Edge with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Front Door rate limit per IP/client; protect origin during viral event.

### Detailed Answer (3–5 minutes)

**Rate Limit at Edge** (Scalability context)

Front Door rate limit per IP/client; protect origin during viral event.

**Production implementation:**
```csharp
var cached = await _cache.GetAsync<Product>(key);
if (cached is null) {
    cached = await _db.Products.FindAsync(id);
    await _cache.SetAsync(key, cached, TimeSpan.FromMinutes(5));
}
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

Rate Limit at Edge separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Scaling-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q095: Partition Tolerance Cache

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Distributed Cache |
| **Frequency** | Common |

### Question

How would you implement Partition Tolerance Cache with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Split brain: prefer availability with stale cache vs hard fail — document.

### Detailed Answer (3–5 minutes)

**Partition Tolerance Cache** (Scalability context)

Split brain: prefer availability with stale cache vs hard fail — document.

**Production implementation:**
```csharp
var cached = await _cache.GetAsync<Product>(key);
if (cached is null) {
    cached = await _db.Products.FindAsync(id);
    await _cache.SetAsync(key, cached, TimeSpan.FromMinutes(5));
}
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

Partition Tolerance Cache separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Distributed Cache-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q096: Elasticache vs Azure Redis

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Caching |
| **Frequency** | Common |

### Question

How would you implement Elasticache vs Azure Redis with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Enterprise features, clustering, persistence — tier selection matrix.

### Detailed Answer (3–5 minutes)

**Elasticache vs Azure Redis** (Scalability context)

Enterprise features, clustering, persistence — tier selection matrix.

**Production implementation:**
```csharp
var cached = await _cache.GetAsync<Product>(key);
if (cached is null) {
    cached = await _db.Products.FindAsync(id);
    await _cache.SetAsync(key, cached, TimeSpan.FromMinutes(5));
}
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

Elasticache vs Azure Redis separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Caching-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q097: SQL Read Scale-Out

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Scaling |
| **Frequency** | Common |

### Question

How would you implement SQL Read Scale-Out with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Azure SQL Hyperscale read replicas; elastic pools for dev/test.

### Detailed Answer (3–5 minutes)

**SQL Read Scale-Out** (Scalability context)

Azure SQL Hyperscale read replicas; elastic pools for dev/test.

**Production implementation:**
```csharp
var cached = await _cache.GetAsync<Product>(key);
if (cached is null) {
    cached = await _db.Products.FindAsync(id);
    await _cache.SetAsync(key, cached, TimeSpan.FromMinutes(5));
}
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

SQL Read Scale-Out separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Scaling-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q098: Aspire Connection Resilience

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Scaling |
| **Frequency** | Common |

### Question

How would you implement Aspire Connection Resilience with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

.NET Polly retry, circuit breaker on HttpClient and DB connections.

### Detailed Answer (3–5 minutes)

**Aspire Connection Resilience** (Scalability context)

.NET Polly retry, circuit breaker on HttpClient and DB connections.

**Production implementation:**
```csharp
var cached = await _cache.GetAsync<Product>(key);
if (cached is null) {
    cached = await _db.Products.FindAsync(id);
    await _cache.SetAsync(key, cached, TimeSpan.FromMinutes(5));
}
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

Aspire Connection Resilience separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Scaling-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q099: Capacity Headroom Planning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Scaling |
| **Frequency** | Common |

### Question

How would you implement Capacity Headroom Planning with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

2× headroom for failover; autoscale max from capacity calc.

### Detailed Answer (3–5 minutes)

**Capacity Headroom Planning** (Scalability context)

2× headroom for failover; autoscale max from capacity calc.

**Production implementation:**
```csharp
var cached = await _cache.GetAsync<Product>(key);
if (cached is null) {
    cached = await _db.Products.FindAsync(id);
    await _cache.SetAsync(key, cached, TimeSpan.FromMinutes(5));
}
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

Capacity Headroom Planning separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Scaling-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q100: Scaling State Machines

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Scaling |
| **Frequency** | Common |

### Question

How would you implement Scaling State Machines with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Identify stateful vs stateless components — scale stateless horizontally first.

### Detailed Answer (3–5 minutes)

**Scaling State Machines** (Scalability context)

Identify stateful vs stateless components — scale stateless horizontally first.

**Production implementation:**
```csharp
var cached = await _cache.GetAsync<Product>(key);
if (cached is null) {
    cached = await _db.Products.FindAsync(id);
    await _cache.SetAsync(key, cached, TimeSpan.FromMinutes(5));
}
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

Scaling State Machines separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Scaling-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---
