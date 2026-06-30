# Azure Production Architecture Capstone

## Scenario
Design a multi-region .NET 8 SaaS platform on Azure:
- 50K users, 99.95% SLA
- EU + US data residency
- PCI compliance for payments
- $15K/month budget target

## Required Components
1. Landing zone design (management groups, subscriptions)
2. Network topology (hub-spoke, Private Link)
3. Compute (App Service or Container Apps)
4. Data (SQL Database geo-replication)
5. Identity (Entra ID, Managed Identity)
6. Messaging (Service Bus for async)
7. Monitoring (App Insights, Sentinel)
8. DR strategy (RTO 1hr, RPO 15min)
9. CI/CD (GitHub Actions + Bicep)
10. Cost estimate

## Reference Architecture Checklist
- [ ] WAF pillars addressed in design doc
- [ ] ADRs for major decisions
- [ ] C4 Context + Container diagrams
- [ ] Threat model completed
- [ ] Cost breakdown by service
- [ ] Runbook for failover

## Assessment Rubric
| Criteria | Weight |
|----------|--------|
| Requirements coverage | 25% |
| Security & compliance | 20% |
| Reliability & DR | 20% |
| Cost optimization | 15% |
| Documentation quality | 10% |
| Presentation clarity | 10% |

## Architect Deep Dive: Production Readiness Review

### Go-live checklist (abbreviated)
- [ ] SLO defined and dashboard live
- [ ] Runbooks for top 5 failure modes
- [ ] DR drill completed (documented RTO/RPO achieved)
- [ ] Load test at 2× peak passed
- [ ] Secrets in Key Vault, no plain text in config
- [ ] Alerts route to on-call with escalation
- [ ] ADRs published for major decisions
- [ ] Rollback tested (slot swap or previous artifact tag)

### Capstone presentation structure
1. Business context (30 sec)
2. Architecture diagram (2 min)
3. Key decisions + trade-offs (3 min)
4. Non-functionals: how you meet SLO/cost/security (2 min)
5. Evolution at 10× (1 min)

