# Microservices Top 50 — Part 1 (Q001–Q008)

> [Part 2](microservices-top-50-qa-part2.md) | [Part 3](microservices-top-50-qa-part3.md) | [Index](microservices-top-50-index.md)

---

## Q001: CAP Theorem

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Distributed Systems |
| **Week** | 21 |

### Question

Explain CAP theorem. How does it guide microservices data store selection?

### Short Answer (30 seconds)

In a partition, you choose Consistency or Availability — not both. Partition tolerance is required in distributed systems. Pick CP (SQL, strong consistency) for financial ledgers; AP (eventual consistency) for catalogs and analytics.

### Detailed Answer (3–5 minutes)

**CAP:** Consistency (all nodes see same data), Availability (every request gets a response), Partition tolerance (network splits happen).

During a partition, you cannot have all three. Cloud microservices always assume partitions — so the real choice is CP vs AP.

| Workload | Choice | Example |
|----------|--------|---------|
| Payment ledger | CP | SQL with strong consistency |
| Product catalog | AP | Cosmos with session consistency |
| Shopping cart | AP | Redis with TTL |

**Architect:** Document consistency requirements per bounded context — not one global rule.

### Follow-up Questions

1. **Is CA possible?** — Only on single node; not in distributed production.
2. **BASE vs ACID?** — Basically Available, Soft state, Eventual consistency for AP systems.

### Common Mistakes

- Quoting CAP without mapping to business requirements
- Strong consistency everywhere (kills availability under partition)

---

## Q002: When to Split the Monolith

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Decomposition |
| **Week** | 22 |

### Question

When should you decompose a monolith into microservices?

### Short Answer (30 seconds)

Split when you have independent scale needs, team boundaries (Conway's Law), deployment pain, or technology diversity — not because microservices are fashionable. Start with modular monolith if team < 10.

### Detailed Answer (3–5 minutes)

**Good reasons:** Order service needs 10x scale vs catalog; separate teams own billing vs shipping; monthly deploys block all features; one module needs GPU workload.

**Bad reasons:** Resume-driven architecture; 5-user internal tool; no DevOps maturity.

**Path:** Modular monolith → strangler fig → extract highest-value service first.

### Common Mistakes

- Big-bang rewrite
- Splitting before CI/CD and observability exist

---

## Q003: Sync vs Async Communication

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Communication |
| **Week** | 22 |

### Question

When do you use synchronous HTTP vs asynchronous messaging between microservices?

### Short Answer

Sync when the user waits for the result (checkout total). Async when fire-and-forget or long-running (send email, generate report). Avoid sync chains deeper than 2–3 hops.

### Detailed Answer

Sync: simpler debugging, coupling in time. Async: resilience, scale, but complexity in ordering and idempotency.

**Rule:** If failure requires immediate user feedback → sync with timeout + circuit breaker. Otherwise → event.

### Common Mistakes

- Sync call chain of 6 services for page load
- Async for "get order status" user query without polling/WebSocket

---

## Q004: API Gateway Responsibilities

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Gateway |
| **Week** | 22 |

### Question

What belongs in an API gateway vs in individual microservices?

### Short Answer

Gateway: TLS termination, auth, rate limiting, routing, request aggregation. Services: business logic, domain validation, data access. Never put domain rules only in gateway.

### Detailed Answer

Azure APIM / Ocelot / Kong patterns: JWT validation at edge, route `/orders` → order service. BFF may sit behind gateway for mobile-specific aggregation.

**Anti-pattern:** All validation in gateway — duplicates logic, drifts from services.

---

## Q005: Database Per Service

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Data |
| **Week** | 22 |

### Question

Explain database-per-service. How do you handle cross-service queries?

### Short Answer

Each service owns its schema — no foreign keys across DBs. Cross-service data via APIs, events, or read models (CQRS). Reporting uses data warehouse fed by events.

### Detailed Answer

Order service has Order DB; Inventory has Inventory DB. Order line stores `productId` not JOIN to product table — fetch product via API or cache denormalized snapshot on order placed event.

### Common Mistakes

- Shared database antipattern (hidden monolith)
- Distributed JOIN attempts

---

## Q006: Circuit Breaker Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Resilience |
| **Week** | 21 |

### Question

How does a circuit breaker protect a microservices system?

### Short Answer

After failure threshold, stop calling failing service — fail fast. Half-open probes for recovery. Prevents thread exhaustion cascading across system.

### Detailed Answer

Polly in .NET: 50% failures in 30s → open circuit 60s → half-open test request. Pair with fallback (cached response, degraded mode).

**Architect:** Define per-dependency policies — payment stricter than recommendations.

---

## Q007: Idempotency in Distributed APIs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reliability |
| **Week** | 21 |

### Question

Why are idempotency keys critical in microservices?

### Short Answer

At-least-once delivery and client retries cause duplicate operations. Idempotency-Key + server-side dedup ensures paying once, creating one order.

### Detailed Answer

Store key in Redis/SQL with response cache TTL 24h. Same key returns same response without re-executing side effects.

---

## Q008: Bounded Context

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DDD |
| **Week** | 23 |

### Question

What is a bounded context and how does it map to microservices?

### Short Answer

Explicit boundary where a domain model applies. One bounded context often becomes one microservice — aligned with team ownership.

### Detailed Answer

"Customer" means different things in Billing (payer) vs Support (ticket submitter) — separate contexts, separate models, integrate via events or ACL.

**Next:** [Part 2](microservices-top-50-qa-part2.md) →
