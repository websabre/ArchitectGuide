# Month 3 Capstone — Azure 3-Tier SaaS

> **Phase 3** | Complete after weeks in this month.

## Brief

Landing zone + App Service + SQL + Entra ID for multi-tenant SaaS.

## Scenario

**ComplianceTrack** is a Series B RegTech SaaS startup (~80 employees) selling audit-workflow software to financial firms. They need an Azure production baseline for **multi-tenant SaaS** serving 200 tenants today, scaling to 2,000. Constraints: SOC 2 Type II in progress, data residency in US + EU, tenant isolation is non-negotiable. Stakeholders include the CISO (Entra ID + Conditional Access), FinOps (tagging and budget alerts), and customer success (tenant onboarding in <24 hours). You are designing the Azure landing zone and 3-tier application architecture for the architecture council.

## Architecture Expectations

A passing solution must align with Azure Well-Architected Framework pillars:

- **Landing zone** — management groups, subscriptions, resource groups, tagging policy
- **C4 Context + Container diagrams** — SaaS platform, tenants, identity provider, data stores
- **3-tier compute** — App Service (or equivalent) + Azure SQL + storage/cache layer
- **Multi-tenant identity** — Entra ID B2B or B2C strategy, app registration, RBAC per tenant
- **Network baseline** — VNet integration, private endpoints for SQL, no public DB access
- **Observability** — Application Insights, Log Analytics workspace, alert rules
- **NFRs** — 99.9% SLA target, RPO ≤ 1 hr, tenant data isolation model (pool vs silo)
- **Cost estimate** — order-of-magnitude monthly at 200 and 2,000 tenants

## Deliverables

- [ ] **C4 Context + Container diagrams** (Mermaid or draw.io)
- [ ] **Landing zone diagram** — subscriptions, MG hierarchy, policy assignments
- [ ] **Identity architecture diagram** — Entra ID flows, app roles, tenant onboarding
- [ ] **Network diagram** — VNet, subnets, private endpoints, App Service integration
- [ ] **Tenant isolation ADR** — pooled vs siloed database decision
- [ ] **ADR: compute tier** — App Service plan SKU rationale
- [ ] **WAF pillar checklist** — reliability, security, cost, ops, performance mapped
- [ ] **Cost estimate spreadsheet or table** — 200-tenant and 2,000-tenant scenarios
- [ ] **Tenant onboarding runbook outline** — provision → configure → verify

## Evaluation Rubric

| Criteria | Points |
|----------|--------|
| Requirements clarity | 20 |
| Architecture quality | 30 |
| Trade-off documentation | 20 |
| Production realism | 15 |
| Presentation / ADRs | 15 |

**Requirements clarity (20 pts)**

- Multi-tenant model defined (pooled, siloed, or hybrid)
- Compliance and residency requirements explicit
- Scale targets for tenants and concurrent users

**Architecture quality (30 pts)**

- Landing zone follows CAF / WAF guidance
- Identity flows cover onboarding, authN, authZ
- Network design eliminates public data-plane exposure

**Trade-off documentation (20 pts)**

- Tenant isolation ADR compares pool vs silo with cost impact
- Compute SKU justified against scale and SLA
- Alternatives (Container Apps, AKS) acknowledged

**Production realism (15 pts)**

- Backup, geo-replication, or DR mentioned for SQL
- Monitoring and alerting wired to SLOs
- Tagging and cost governance in place

**Presentation / ADRs (15 pts)**

- Diagrams suitable for CISO and FinOps audiences
- 20-minute review narrative prepared
- ADRs indexed and cross-linked

**Pass:** ≥ 70 points

## Timeline

Suggested **2-week sprint** at end of Month 3:

| Day | Focus |
|-----|-------|
| **Mon W1** | Tenant model workshop — isolation, residency, scale targets |
| **Tue W1** | Landing zone + subscription/MG diagram |
| **Wed W1** | C4 Context + Container diagrams |
| **Thu W1** | Identity architecture — Entra ID flows |
| **Fri W1** | Network diagram + private endpoints |
| **Mon W2** | ADR: tenant isolation + compute tier |
| **Tue W2** | WAF checklist + observability design |
| **Wed W2** | Cost estimate (200 vs 2,000 tenants) |
| **Thu W2** | Tenant onboarding runbook; peer review |
| **Fri W2** | Submit package; self-score against rubric |

## References

- [Week 09 — Azure Fundamentals & WAF](../../weeks/week-09/README.md)
- [Week 10 — Azure Compute & App Services](../../weeks/week-10/README.md)
- [Week 11 — Azure Data Platform](../../weeks/week-11/README.md)
- [Week 12 — Azure Identity & Key Services Integration](../../weeks/week-12/README.md)

← [Phase overview](README.md) | [SYLLABUS](../../SYLLABUS.md)
