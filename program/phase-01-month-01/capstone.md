# Month 1 Capstone — Design a Modular .NET API

> **Phase 1** | Complete after weeks in this month.

## Brief

Build a Clean Architecture order API with ADRs, 3+ patterns, async I/O, and assessment ≥70% on weeks 1–4.

## Scenario

**Northwind Logistics** is a mid-market B2B shipping company (~400 engineers, 12 .NET teams) modernizing a monolithic order-management system. The VP of Engineering wants a reference API that teams can fork for new bounded contexts. Constraints: .NET 8 only, no cloud dependencies yet, must run on a developer laptop with Docker Compose for SQL Server. Stakeholders include platform engineering (wants consistency), security (requires audit trails on order mutations), and product (needs sub-200 ms P95 on read endpoints). You are the lead architect presenting the design to the architecture review board before any sprint starts.

## Architecture Expectations

A passing solution must demonstrate architect-level thinking, not just working code:

- **Clean Architecture layers** — Domain, Application, Infrastructure, and API with dependency rule enforced (inward-only references)
- **C4 Container diagram** — show API, application services, persistence, and external notification stub
- **3+ design patterns** — e.g., Repository, Mediator (CQRS-lite), Strategy for pricing rules — each justified in an ADR
- **Async I/O throughout** — no blocking calls on request threads; document `ConfigureAwait` and thread-pool implications
- **Type strategy** — records for DTOs/commands, classes for entities with behavior, structs only where justified
- **NFRs documented** — latency targets, structured logging, health checks (`/health`, `/ready`), correlation IDs
- **Mermaid sequence diagram** — happy-path order creation flow

## Deliverables

- [ ] **C4 Context + Container diagrams** (Mermaid or Structurizr export)
- [ ] **Clean Architecture layer map** — project/solution structure with dependency arrows
- [ ] **2 ADRs** — (1) pattern choices, (2) async I/O and resilience strategy
- [ ] **OpenAPI spec** — `orders` CRUD + `POST /orders/{id}/cancel` with request/response examples
- [ ] **Mermaid sequence diagram** — create-order flow including validation and persistence
- [ ] **NFR appendix** — latency, logging, health endpoints, error contract (`ProblemDetails`)
- [ ] **120+ interview questions practiced** from weeks 1–4
- [ ] **Month 1 Top 50 self-assessment** — score ≥70% ([interview prep](../../interview-prep/month-01-top-50-part1.md))

## Evaluation Rubric

| Criteria | Points |
|----------|--------|
| Requirements clarity | 20 |
| Architecture quality | 30 |
| Trade-off documentation | 20 |
| Production realism | 15 |
| Presentation / ADRs | 15 |

**Requirements clarity (20 pts)**

- Functional scope bounded (in/out of scope listed)
- NFRs quantified (P95 latency, availability target)
- Stakeholder concerns mapped to design decisions

**Architecture quality (30 pts)**

- Clean Architecture layers correctly separated
- 3+ patterns applied with clear responsibility boundaries
- Async pipeline with no sync-over-async anti-patterns

**Trade-off documentation (20 pts)**

- ADRs follow Nygard format (context, decision, consequences)
- Alternatives considered for patterns and persistence
- Type choices (record/class/struct) explained

**Production realism (15 pts)**

- Health checks, structured logging, correlation IDs
- Error handling contract documented
- Local-dev story (Docker Compose) described

**Presentation / ADRs (15 pts)**

- Diagrams readable without verbal explanation
- 15-minute walkthrough narrative prepared
- ADRs linked from README or architecture index

**Pass:** ≥ 70 points

## Timeline

Suggested **2-week sprint** at end of Month 1:

| Day | Focus |
|-----|-------|
| **Mon W1** | Scope workshop — define bounded context, NFRs, stakeholder sign-off |
| **Tue W1** | C4 Context + Container diagrams; layer project structure |
| **Wed W1** | ADR-001 pattern selection; sketch domain model |
| **Thu W1** | ADR-002 async strategy; OpenAPI draft |
| **Fri W1** | Sequence diagram + error/health contract |
| **Mon W2** | Peer review — swap diagrams with study partner |
| **Tue W2** | Revise ADRs from feedback; add NFR appendix |
| **Wed W2** | Rehearse 15-min architecture walkthrough |
| **Thu W2** | Complete Month 1 Top 50 self-assessment |
| **Fri W2** | Submit package; self-score against rubric |

## References

- [Week 01 — C# Language Mastery](../../weeks/week-01/README.md)
- [Week 02 — .NET Runtime & Ecosystem](../../weeks/week-02/README.md)
- [Week 03 — SOLID & Clean Architecture](../../weeks/week-03/README.md)
- [Week 04 — Design Patterns](../../weeks/week-04/README.md)
- [Case study: Order API performance](../../weeks/week-01/case-studies/cs01-order-api-performance.md)

← [Phase overview](README.md) | [SYLLABUS](../../SYLLABUS.md)
