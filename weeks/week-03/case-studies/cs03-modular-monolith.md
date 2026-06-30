# Case Study: Monolith to Modular Monolith

| **Industry** | Banking | **Week** | 03 | **Difficulty** | Expert |

## Context

15-year .NET Framework monolith, 800K LOC, shared SQL database, 40 developers. Deployment: monthly, 6-hour window. Regulators require audit trail for all changes.

## Pain Points

- Any change risks breaking unrelated modules
- 4-hour integration test suite
- New developer onboarding: 3 months

## Your Task

Propose architecture evolution (not microservices yet). Define module boundaries, communication patterns, and migration plan.

## Reference Solution

### Target: Modular Monolith

- **Modules:** Accounts, Transactions, Compliance, Reporting
- **Separate schemas** per module in same SQL instance (first step)
- **In-process events** (MediatR) replacing direct cross-module calls
- **Anti-corruption layers** for legacy integrations
- **Architecture tests** enforce module boundaries

### Migration (12 months)

| Phase | Duration | Action |
|-------|----------|--------|
| 1 | Month 1–3 | Define bounded contexts, create project structure |
| 2 | Month 4–6 | Schema separation, ACL for legacy |
| 3 | Month 7–9 | Replace cross-module calls with domain events |
| 4 | Month 10–12 | Extract Compliance to separate service (first microservice) |

### Metrics

- Deployment frequency: monthly → weekly
- Integration test time: 4hr → 45min (module-scoped)
- Lead time for change: 3 weeks → 5 days

## Interview Angle

STAR story: "Structured modernization without big-bang rewrite."
