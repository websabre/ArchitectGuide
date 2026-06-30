# Technical Interview Intensive — System Design & Microservices

> **Week 47** | Review Months 6–9

## Daily Schedule

| Day | Focus |
|-----|-------|
| Mon | Microservices decomposition, DDD boundaries |
| Tue | Resilience (circuit breaker, saga, outbox) |
| Wed | Docker/K8s architecture questions |
| Thu | System design (URL shortener, chat, payments) |
| Fri | Full 45-min system design mock |

---

## System Design Checklist

```
1. Requirements (5 min)
   - Functional: core features
   - Non-functional: scale, latency, availability
   - Estimates: DAU, QPS, storage

2. High-level (10 min)
   - API design
   - Data model
   - Core components diagram

3. Deep dive (20 min)
   - Bottlenecks
   - Caching, sharding
   - Failure handling

4. Wrap-up (10 min)
   - Monitoring
   - Trade-offs recap
   - What you'd do with more time
```

---

## Microservices Interview Themes

- When NOT to use microservices
- Distributed monolith signals
- Service mesh: when worth the complexity
- Data consistency without 2PC

**Resources:** [Weeks 21–24](../../week-21/README.md), [Weeks 33–36](../../week-33/README.md)
