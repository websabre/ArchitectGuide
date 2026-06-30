# Architecture Reviews & ADRs

> **Week 41** | **Module:** [case-studies](../../../modules/case-studies/README.md)

## Learning Objectives
- Run effective architecture review meetings
- Write decision-quality ADRs
- Apply C4 model for communication

---

## 1. ADR Template

```markdown
# ADR-042: Adopt Event Sourcing for Order Service

## Status
Accepted | 2026-03-15

## Context
Order state changes need full audit trail for SOX compliance...

## Decision
Use event sourcing with Azure Cosmos DB change feed...

## Consequences
+ Complete audit history
+ Temporal queries
- Team learning curve
- Increased storage cost

## Alternatives Considered
1. Audit log table — rejected: no point-in-time replay
2. CDC from SQL — rejected: schema coupling
```

**Architect rule:** ADR when decision is hard to reverse or affects multiple teams.

---

## 2. C4 Model Levels

| Level | Audience | Content |
|-------|----------|---------|
| **1 Context** | Executives | System in world |
| **2 Container** | Architects, leads | Apps, DBs, queues |
| **3 Component** | Developers | Internal modules |
| **4 Code** | IDE | Classes (rarely documented) |

**Week 41 focus:** Context + Container for stakeholder alignment.

---

## 3. Architecture Review Process

1. **Intake** — RFC or ADR draft submitted
2. **Pre-read** — Reviewers get 48h with C4 diagrams
3. **Session** — 60 min: author presents, Q&A, risks
4. **Outcome** — Approved / Approved with conditions / Deferred
5. **Follow-up** — Track conditions in backlog

**Review checklist:**
- [ ] NFRs addressed (scale, security, cost)
- [ ] Failure modes identified
- [ ] Operational runbook exists
- [ ] Migration path from current state

---

## 4. Reviewing Legacy .NET Monoliths

| Signal | Modernization Path |
|--------|-------------------|
| Single deployable | Strangler fig |
| Shared database | Bounded context extraction |
| No tests | Characterization tests first |
| .NET Framework | .NET 8 migration parallel track |

**Architect:** Don't propose microservices day one. Identify seams, prioritize by business value.

---

## 5. Governance Without Bureaucracy

| Heavy (avoid) | Light (prefer) |
|---------------|----------------|
| Approval for every PR | ADR for cross-cutting decisions |
| 20-person review board | 2–3 designated architects |
| Months to approve | 1-week RFC cycle |

**Next:** Week 42 FinOps & DR
