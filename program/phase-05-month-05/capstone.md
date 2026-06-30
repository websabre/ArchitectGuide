# Month 5 Capstone — Same Workload: Azure vs AWS

> **Phase 5** | Complete after weeks in this month.

## Brief

Design payment API on both clouds; document portable vs locked-in choices.

## Scenario

**FinBridge Payments** is a fintech ISV (~200 engineers) whose largest customer demands **cloud portability** — they must run the payment orchestration API on either Azure or AWS with ≤4-week migration if the contract changes. The API handles **5K TPS** peak, tokenizes card data (PCI DSS), and integrates with three acquirers. Constraints: no proprietary SDK lock-in where an open standard exists, secrets in managed vaults only, and observability must be vendor-neutral (OpenTelemetry). Stakeholders include the customer's enterprise architect (wants comparison evidence), legal (data-processing agreements per cloud), and platform team (Terraform for both). You are delivering a dual-cloud reference architecture and primary-cloud recommendation.

## Architecture Expectations

A passing solution must show deliberate portability vs optimization trade-offs:

- **Side-by-side service mapping** — compute, API gateway, secrets, messaging, SQL, observability
- **Payment API C4 Container diagram** — one logical design, two deployment views
- **Portable layer** — .NET 8, OpenTelemetry, Terraform/Pulumi modules, container images
- **Cloud-specific optimizations** — called out explicitly as lock-in risks
- **Security equivalence** — KMS/Key Vault, WAF, private networking on both clouds
- **Migration path** — 4-week switch plan with data migration and DNS cutover
- **NFRs** — 5K TPS, P99 < 150 ms, PCI scope minimization
- **Cost comparison** — order-of-magnitude monthly on Azure vs AWS at steady state

## Deliverables

- [ ] **Side-by-side comparison table** — 15+ service mappings (Azure ↔ AWS)
- [ ] **C4 Container diagram** — logical + Azure deployment + AWS deployment views
- [ ] **ADR: primary cloud choice** — recommendation with scoring matrix
- [ ] **ADR: portability boundary** — what stays portable vs cloud-native
- [ ] **Migration runbook outline** — 4-week cloud-switch plan
- [ ] **Terraform module structure** — shared vs cloud-specific directories
- [ ] **PCI scope diagram** — CDE boundary on each cloud
- [ ] **Cost comparison table** — steady-state and burst scenarios
- [ ] **Mermaid deployment diagram** — traffic flow on primary cloud

## Evaluation Rubric

| Criteria | Points |
|----------|--------|
| Requirements clarity | 20 |
| Architecture quality | 30 |
| Trade-off documentation | 20 |
| Production realism | 15 |
| Presentation / ADRs | 15 |

**Requirements clarity (20 pts)**

- Workload profile (TPS, data volume, regions) quantified
- Portability requirements vs performance requirements balanced
- PCI and compliance scope defined per cloud

**Architecture quality (30 pts)**

- Service mappings are accurate and complete for the workload
- Both deployments achieve functional equivalence
- Portable abstractions do not leak cloud specifics into domain code

**Trade-off documentation (20 pts)**

- Primary cloud ADR uses weighted criteria (cost, skills, features)
- Lock-in risks rated (low/medium/high) per component
- Migration path covers stateful data and secrets

**Production realism (15 pts)**

- Networking (VPC/VNet, private endpoints) on both sides
- Observability exportable via OpenTelemetry
- DR and multi-AZ/zone patterns addressed

**Presentation / ADRs (15 pts)**

- Comparison table usable by customer's enterprise architect
- 20-minute dual-cloud walkthrough prepared
- ADRs reference comparison table rows

**Pass:** ≥ 70 points

## Timeline

Suggested **2-week sprint** at end of Month 5:

| Day | Focus |
|-----|-------|
| **Mon W1** | Workload profile + portability requirements workshop |
| **Tue W1** | Logical C4 Container diagram (cloud-agnostic) |
| **Wed W1** | Azure deployment view + service mapping rows 1–8 |
| **Thu W1** | AWS deployment view + service mapping rows 9–15 |
| **Fri W1** | PCI scope diagrams for both clouds |
| **Mon W2** | ADR: primary cloud choice (scoring matrix) |
| **Tue W2** | ADR: portability boundary; Terraform module layout |
| **Wed W2** | Migration runbook + cost comparison |
| **Thu W2** | Peer review — customer architect Q&A rehearsal |
| **Fri W2** | Submit package; self-score against rubric |

## References

- [Week 17 — AWS Fundamentals & WAF](../../weeks/week-17/README.md)
- [Week 18 — AWS Compute & Serverless](../../weeks/week-18/README.md)
- [Week 19 — AWS Data, Storage & Networking](../../weeks/week-19/README.md)
- [Week 20 — Multi-Cloud & Azure vs AWS Architecture](../../weeks/week-20/README.md)

← [Phase overview](README.md) | [SYLLABUS](../../SYLLABUS.md)
