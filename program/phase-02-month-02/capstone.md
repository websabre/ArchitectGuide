# Month 2 Capstone — E-Commerce Data Layer at Scale

> **Phase 2** | Complete after weeks in this month.

## Brief

Design data layer for 10M users: SQL vs NoSQL, indexing, caching, read replicas.

## Scenario

**ShopVerse** is a fast-growing e-commerce marketplace projecting **10M registered users** and **50K orders/hour** peak within 18 months. The current single SQL Server instance is hitting connection and I/O limits. The CTO has budget for one major data-platform change this year. Constraints: must support ACID checkout, sub-100 ms product search, and GDPR right-to-erasure. Stakeholders include data engineering (wants a unified lake), SRE (demands observable query paths), and finance (cost-per-query matters). You are designing the target data architecture before Black Friday load testing.

## Architecture Expectations

A passing solution must cover polyglot persistence with evidence-based trade-offs:

- **ER diagram** — core entities: User, Product, Order, OrderLine, Inventory, Payment
- **Read/write split** — primary vs read replicas or CQRS projection paths
- **Indexing strategy** — covering indexes for top 5 queries with estimated cardinality
- **Caching layer** — what to cache (product catalog, session cart), TTL, invalidation
- **Sharding or partitioning plan** — even if deferred, document trigger thresholds
- **SQL vs NoSQL decision tree** — when to use PostgreSQL, Redis, Elasticsearch, or blob storage
- **NFRs** — RPO/RTO for orders, P95 query latency, connection-pool sizing
- **Mermaid data-flow diagram** — checkout write path vs product browse read path

## Deliverables

- [ ] **ER diagram** (Mermaid `erDiagram` or dbdiagram.io export)
- [ ] **Sharding / partitioning strategy** — shard key rationale and re-sharding plan
- [ ] **Index design doc** — top 5 queries with `EXPLAIN` assumptions or equivalent
- [ ] **Database selection decision tree** — flowchart for workload → store mapping
- [ ] **Caching architecture diagram** — Redis layers, cache-aside vs write-through
- [ ] **ADR: SQL vs NoSQL** — checkout vs catalog vs search stores
- [ ] **ADR: read replica vs CQRS** — consistency trade-offs
- [ ] **Capacity estimate** — storage growth, IOPS, connection counts at 10M users
- [ ] **Mermaid data-flow diagram** — read vs write paths

## Evaluation Rubric

| Criteria | Points |
|----------|--------|
| Requirements clarity | 20 |
| Architecture quality | 30 |
| Trade-off documentation | 20 |
| Production realism | 15 |
| Presentation / ADRs | 15 |

**Requirements clarity (20 pts)**

- Workload profile quantified (users, orders/hr, read/write ratio)
- Consistency requirements per entity (strong vs eventual)
- Compliance constraints (GDPR erasure) addressed

**Architecture quality (30 pts)**

- ER model normalized appropriately with justified denormalization
- Index design matches actual query patterns
- Caching invalidation strategy is coherent

**Trade-off documentation (20 pts)**

- SQL vs NoSQL decision tree covers edge cases
- Sharding deferral triggers are explicit
- ADRs compare at least two alternatives per decision

**Production realism (15 pts)**

- Connection pooling and replica lag handling
- Failover / RPO-RTO for order data
- Cost order-of-magnitude included

**Presentation / ADRs (15 pts)**

- Diagrams legible at architecture-review scale
- Walkthrough covers Black Friday scenario
- ADRs linked from data architecture index

**Pass:** ≥ 70 points

## Timeline

Suggested **2-week sprint** at end of Month 2:

| Day | Focus |
|-----|-------|
| **Mon W1** | Quantify workload — users, QPS, read/write ratio, peak events |
| **Tue W1** | ER diagram + entity consistency requirements |
| **Wed W1** | Top 5 queries + index design |
| **Thu W1** | Caching layer diagram + invalidation rules |
| **Fri W1** | ADR: SQL vs NoSQL decision tree |
| **Mon W2** | Sharding / partitioning strategy + deferral triggers |
| **Tue W2** | Read replica vs CQRS ADR; data-flow diagram |
| **Wed W2** | Capacity estimate + cost model |
| **Thu W2** | Peer review — Black Friday walkthrough |
| **Fri W2** | Submit package; self-score against rubric |

## References

- [Week 05 — Data Structures for System Design](../../weeks/week-05/README.md)
- [Week 06 — Algorithms & Complexity Analysis](../../weeks/week-06/README.md)
- [Week 07 — SQL Server Architecture & Tuning](../../weeks/week-07/README.md)
- [Week 08 — PostgreSQL & Polyglot Persistence](../../weeks/week-08/README.md)

← [Phase overview](README.md) | [SYLLABUS](../../SYLLABUS.md)
