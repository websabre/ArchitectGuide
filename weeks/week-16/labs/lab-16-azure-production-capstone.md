# Lab 16: Azure Production Architecture Capstone

| **Week** | 16 | **Duration** | 8–12 hours (spread across week) |

## Capstone Brief

Design and document a **production-grade multi-tier SaaS** on Azure. This integrates Weeks 9–15: landing zone, compute, data, identity, networking, security, and messaging.

**Deliverable:** Architecture package (not full implementation) suitable for executive review.

## Requirements

| NFR | Target |
|-----|--------|
| Availability | 99.95% |
| Users | 50K MAU, 2K peak concurrent |
| Tenancy | Multi-tenant B2B SaaS |
| Compliance | SOC 2 ready (encryption, audit logs) |
| RPO / RTO | 1 hour / 4 hours |

## Deliverables Checklist

- [ ] C4 Context diagram
- [ ] C4 Container diagram
- [ ] Hub-spoke or simplified network diagram
- [ ] Identity flow (Entra ID + MI + Key Vault)
- [ ] Data platform choice (SQL vs Cosmos) with ADR
- [ ] Integration pattern (Service Bus or Event Grid) for async workflows
- [ ] Security controls mapped to WAF pillars
- [ ] Cost estimate (order of magnitude, monthly USD)
- [ ] DR runbook outline (1 page)
- [ ] 3 failure scenarios + mitigations

## Suggested Azure Services

- App Service (or AKS if justified in ADR)
- Azure SQL or Cosmos DB
- Service Bus
- Application Gateway or Front Door
- Key Vault, App Configuration
- Application Insights + Log Analytics
- Entra ID app registration

## Presentation (30 min)

1. Problem & tenants (5 min)
2. Architecture walkthrough (15 min)
3. Trade-offs & ADRs (7 min)
4. Roadmap if 6 more months (3 min)

## Rubric

| Criteria | Points |
|----------|--------|
| Requirements coverage | 20 |
| Architecture quality | 25 |
| Security & identity | 20 |
| Operability (observability, DR) | 20 |
| Documentation & ADRs | 15 |

**Pass:** ≥ 70/100

← [Month 4 capstone](../../../program/phase-04-month-04/capstone.md)
