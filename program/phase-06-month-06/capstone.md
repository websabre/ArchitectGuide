# Month 6 Capstone — 12-Service E-Commerce Platform

> **Phase 6** | Complete after weeks in this month.

## Brief

Microservices decomposition, events, sagas, API gateway.

## Scenario

**MegaMart Digital** is replatforming a legacy e-commerce monolith into **12 bounded-context microservices** ahead of a holiday launch. The platform must support **100K concurrent shoppers**, event-driven inventory updates, and checkout sagas across payment, fulfillment, and loyalty services. Constraints: teams are autonomous (you cannot mandate shared databases), eventual consistency is acceptable for catalog, but checkout must be strongly consistent. Stakeholders include domain leads (own 12 services), SRE (needs blast-radius limits), and the API product owner (single public API surface). You are the principal architect producing the target microservices landscape.

## Architecture Expectations

A passing solution must show distributed-systems maturity:

- **Bounded context map** — 12 services with upstream/downstream relationships (DDD)
- **Event choreography diagram** — domain events, topics/queues, consumer groups
- **Saga design** — checkout orchestration (choreography vs orchestration justified)
- **API gateway pattern** — BFF vs edge gateway, auth termination, rate limiting
- **Data ownership** — database-per-service; no shared tables
- **Failure scenarios** — 3+ with detection, mitigation, and compensating transactions
- **NFRs** — latency budgets per hop, idempotency, dead-letter handling
- **C4 Container diagram** — all 12 services with integration styles labeled

## Deliverables

- [ ] **Bounded context map** — context diagram with relationships (partnership, ACL, etc.)
- [ ] **C4 Container diagram** — 12 services, gateway, message broker, data stores
- [ ] **Event choreography diagram** (Mermaid) — publish/subscribe flows for order lifecycle
- [ ] **Saga sequence diagram** — checkout happy path + compensation path
- [ ] **ADR: choreography vs orchestration** — for checkout saga
- [ ] **ADR: API gateway topology** — BFF per channel vs unified gateway
- [ ] **3 failure scenarios doc** — e.g., payment timeout, inventory oversell, broker partition
- [ ] **Service catalog table** — name, owner, datastore, sync/async interfaces
- [ ] **Latency budget worksheet** — end-to-end checkout P95 decomposition

## Evaluation Rubric

| Criteria | Points |
|----------|--------|
| Requirements clarity | 20 |
| Architecture quality | 30 |
| Trade-off documentation | 20 |
| Production realism | 15 |
| Presentation / ADRs | 15 |

**Requirements clarity (20 pts)**

- 12 services named with clear bounded contexts
- Consistency requirements per aggregate (checkout vs catalog)
- Scale targets and peak-traffic assumptions stated

**Architecture quality (30 pts)**

- Context map relationships are correct DDD partnership types
- Events carry sufficient context; no chatty cross-service DB access
- Saga compensations are complete and testable

**Trade-off documentation (20 pts)**

- Choreography vs orchestration ADR with failure-mode analysis
- Gateway ADR covers auth, versioning, and team autonomy
- Sync vs async choice justified per integration

**Production realism (15 pts)**

- Idempotency keys and outbox pattern where needed
- Dead-letter and retry policies documented
- Circuit breakers / bulkheads between critical paths

**Presentation / ADRs (15 pts)**

- Diagrams readable without a 30-minute preamble
- Failure scenario walkthrough rehearsed
- Service catalog usable by team leads

**Pass:** ≥ 70 points

## Timeline

Suggested **2-week sprint** at end of Month 6:

| Day | Focus |
|-----|-------|
| **Mon W1** | Domain workshop — identify 12 bounded contexts |
| **Tue W1** | Bounded context map + service catalog |
| **Wed W1** | C4 Container diagram |
| **Thu W1** | Event choreography diagram — order lifecycle |
| **Fri W1** | Saga sequence diagram (happy + compensation paths) |
| **Mon W2** | ADR: choreography vs orchestration |
| **Tue W2** | ADR: API gateway; latency budget worksheet |
| **Wed W2** | 3 failure scenarios + mitigations |
| **Thu W2** | Peer review — holiday peak walkthrough |
| **Fri W2** | Submit package; self-score against rubric |

## References

- [Week 21 — Distributed Systems Fundamentals](../../weeks/week-21/README.md)
- [Week 22 — Microservices Architecture](../../weeks/week-22/README.md)
- [Week 23 — Domain-Driven Design (DDD)](../../weeks/week-23/README.md)
- [Week 24 — Microservices Capstone](../../weeks/week-24/README.md)

← [Phase overview](README.md) | [SYLLABUS](../../SYLLABUS.md)
