# Month 4 Capstone — Multi-Region Azure Production

> **Phase 4** | Complete after weeks in this month.

## Brief

99.95% SLA design with DR, networking, security, integration.

## Scenario

**GlobalPay EU** is a payment-orchestration platform (~600 engineers) processing **€2B/year** across **EU-West and EU-North** regions. Regulators require **99.95% availability** and documented DR with RPO ≤ 15 minutes. A recent regional outage cost €400K in SLA credits. Constraints: all traffic must traverse inspected hub network, PCI DSS scope must not expand, and partner banks integrate via private APIs. Stakeholders include network engineering (hub-spoke mandate), security (WAF + DDoS), and integration (Service Bus vs Event Hubs for partner events). You are producing the production architecture for quarterly architecture review.

## Architecture Expectations

A passing solution must demonstrate enterprise-grade Azure production patterns:

- **Hub-spoke network topology** — shared services VNet, spoke per workload, peering, firewall inspection
- **Multi-region active-active or active-passive** — traffic routing via Front Door or Traffic Manager
- **DR architecture** — Azure Site Recovery or geo-redundant services; RPO/RTO documented
- **Security controls mapped to WAF** — NSGs, Private Link, Key Vault, Defender, DDoS Protection
- **Integration layer** — API Management, Service Bus or Event Hubs for async partner events
- **Observability** — centralized logging, distributed tracing, SLO dashboards
- **NFRs** — 99.95% SLA math, failover test cadence, blast-radius containment
- **Mermaid DR failover sequence** — regional failure → traffic shift → recovery validation

## Deliverables

- [ ] **Hub-spoke network diagram** — address space, peering, firewall paths, Private Link
- [ ] **Multi-region architecture diagram** — primary/secondary, replication, traffic manager
- [ ] **DR runbook outline** — detection → failover → validation → failback
- [ ] **Security controls matrix** — WAF pillars → Azure services → config
- [ ] **Integration architecture diagram** — sync APIs + async messaging patterns
- [ ] **ADR: active-active vs active-passive** — consistency and cost trade-offs
- [ ] **ADR: messaging backbone** — Service Bus vs Event Hubs for partner events
- [ ] **SLO / SLA worksheet** — error budget, uptime calculation for 99.95%
- [ ] **Mermaid DR failover sequence diagram**

## Evaluation Rubric

| Criteria | Points |
|----------|--------|
| Requirements clarity | 20 |
| Architecture quality | 30 |
| Trade-off documentation | 20 |
| Production realism | 15 |
| Presentation / ADRs | 15 |

**Requirements clarity (20 pts)**

- SLA target decomposed into component SLOs
- RPO/RTO and regulatory constraints explicit
- PCI scope boundaries documented

**Architecture quality (30 pts)**

- Hub-spoke design routes all egress/ingress correctly
- Multi-region strategy is internally consistent
- Integration patterns separate sync from async concerns

**Trade-off documentation (20 pts)**

- Active-active vs passive ADR with split-brain mitigation
- Messaging ADR covers ordering, duplication, poison messages
- Cost vs resilience trade-offs quantified

**Production realism (15 pts)**

- DR runbook includes test schedule and rollback
- Security matrix maps to actual Azure controls
- Observability tied to SLO alerting

**Presentation / ADRs (15 pts)**

- Diagrams survive scrutiny from network and security teams
- Failover walkthrough rehearsed (15 min)
- ADRs cross-reference network and integration diagrams

**Pass:** ≥ 70 points

## Timeline

Suggested **2-week sprint** at end of Month 4:

| Day | Focus |
|-----|-------|
| **Mon W1** | SLA decomposition — component SLOs, error budget |
| **Tue W1** | Hub-spoke network diagram |
| **Wed W1** | Multi-region topology + traffic routing |
| **Thu W1** | Security controls matrix (WAF mapping) |
| **Fri W1** | Integration architecture — APIs + messaging |
| **Mon W2** | ADR: active-active vs passive; DR runbook outline |
| **Tue W2** | ADR: messaging backbone; failover sequence diagram |
| **Wed W2** | SLO worksheet + observability design |
| **Thu W2** | Peer review — simulate regional failover walkthrough |
| **Fri W2** | Submit package; self-score against rubric |

## References

- [Week 13 — Azure Networking Architecture](../../weeks/week-13/README.md)
- [Week 14 — Azure Security Architecture](../../weeks/week-14/README.md)
- [Week 15 — Azure Integration & Messaging](../../weeks/week-15/README.md)
- [Week 16 — Azure Production Architecture Capstone](../../weeks/week-16/README.md)
- [Case study: Hub-spoke network](../../weeks/week-13/case-studies/cs13-hub-spoke-network.md)

← [Phase overview](README.md) | [SYLLABUS](../../SYLLABUS.md)
