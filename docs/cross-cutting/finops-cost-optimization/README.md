# FinOps & Cost Optimization — Deep Dive

> **Primary weeks:** 9, 20, 42 | **Interview target:** 30+ questions

## What FinOps Means for Architects

FinOps is not "make finance happy" — it is designing systems where **cost is a first-class non-functional requirement** alongside availability, security, and performance. Architects own the structural decisions (multi-region, redundancy tier, data retention) that drive 80% of the bill.

---

## FinOps Principles

| Principle | Architect Action |
|-----------|------------------|
| Teams need visibility | Tagging strategy, cost dashboards per service |
| Everyone takes ownership | Cost review in architecture sign-off |
| Decisions are data-driven | Unit economics: $/transaction, $/tenant/month |
| Centralized commitment buying | RI/Savings Plan recommendations from platform team |

---

## Cost Allocation Foundation

### Mandatory Tags (enforce via policy)

| Tag | Purpose |
|-----|---------|
| `Environment` | prod / staging / dev |
| `CostCenter` | Chargeback |
| `Application` | Workload grouping |
| `Owner` | Accountability |

**Azure:** Azure Policy deny deploy without tags  
**AWS:** SCP + AWS Config rules

---

## Compute Cost Optimization

| Strategy | Azure | AWS |
|----------|-------|-----|
| Right-sizing | Advisor, Monitor metrics | Compute Optimizer |
| Reserved capacity | 1–3 year reservations | RI / Savings Plans |
| Spot / preemptible | Spot VMs, AKS spot node pools | Spot instances |
| Scale to zero | Container Apps, Functions consumption | Lambda, App Runner scale |
| Off-hours shutdown | Automation runbooks for dev | Instance Scheduler |

**Architect rule:** Production baseline on reservations; burst on pay-as-you-go or spot.

---

## Data & Storage Cost

| Service | Optimization |
|---------|--------------|
| Blob / S3 | Lifecycle policies → Cool → Archive |
| SQL / RDS | Right-size vCores; dev uses serverless/serverless v2 |
| Cosmos / DynamoDB | Right RU/RCU; on-demand for unknown; avoid cross-partition scans |
| Log Analytics / CloudWatch | Sampling, retention policies, log level discipline |

**Hidden cost:** Verbose logging at INFO in high-traffic API — can exceed compute cost.

---

## Networking Cost

- **Egress** is expensive — serve static from CDN; keep traffic in-region
- **NAT Gateway** charges per GB — VPC endpoints / Private Link reduce NAT traffic
- **Cross-AZ traffic** — design chatty microservices with AZ awareness
- **ExpressRoute / Direct Connect** — fixed port cost; justify vs VPN

---

## Multi-Cloud Cost Comparison Framework

When comparing Azure vs AWS for same workload:

1. **Compute** — normalize to vCPU-hours + memory
2. **Data** — storage GB-month + IOPS + egress
3. **Licensing** — SQL license included vs BYOL
4. **Operations** — engineer hours (hidden cost)
5. **Commitments** — existing enterprise agreements

Document in ADR — not spreadsheet theater.

---

## Unit Economics (Interview Gold)

```
Cost per order = (monthly infra cost) / (monthly orders)
Cost per active user = ...
```

Architects who quote **$/transaction at design time** stand out in senior interviews.

**Example:** Multi-region active-active doubles compute but may reduce revenue loss from outage — express as trade-off, not just "it's expensive."

---

## FinOps in the SDLC

| Phase | Activity |
|-------|----------|
| Design | Order-of-magnitude estimate (pricing calculator) |
| Build | Budget alerts on subscription/account |
| Operate | Monthly cost review per application tag |
| Optimize | Quarterly right-sizing + commitment review |

---

## Architect FinOps Checklist

- [ ] Tagging strategy documented and enforced
- [ ] Budget alerts at 80% and 100%
- [ ] Dev/test auto-shutdown or separate low-cost subscriptions
- [ ] Lifecycle policies on all object storage
- [ ] Log retention aligned to compliance (not infinite)
- [ ] Reservations/Savings Plans for stable baseline
- [ ] Cost estimate in every major ADR
- [ ] Unit economics defined for core transactions

---

## Interview Questions

1. How do you estimate cloud cost for a new microservice?
2. When is multi-region active-active worth the cost?
3. Reserved instances vs on-demand — decision framework?
4. How do you prevent surprise bills from logging or egress?
5. Explain FinOps to a CTO in 2 minutes.

## Related Weeks

- [Week 09 — Azure Fundamentals](../../../weeks/week-09/README.md)
- [Week 20 — Multi-Cloud](../../../weeks/week-20/README.md)
- [Week 42 — Enterprise Governance](../../../weeks/week-42/README.md)
- [Cross-cutting index](../README.md) | [Docs hub](../../README.md)
