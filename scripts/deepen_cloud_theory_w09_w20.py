#!/usr/bin/env python3
"""Deepen cloud theory files for weeks 9–20 with architect-level sections."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Each entry: relative path from weeks/ → content to append before **Next:** or at end
APPEND = {
    "week-09/theory/01-fundamentals.md": """

## Architect Deep Dive: Subscription & Governance

### Subscription strategy (production pattern)
| Subscription | Purpose | Example naming |
|--------------|---------|----------------|
| Platform | Hub VNet, Firewall, DNS, Log Analytics | `sub-platform-prod` |
| Landing zone — prod | Workload production | `sub-lz-orders-prod` |
| Landing zone — nonprod | Dev/test/staging | `sub-lz-orders-nonprod` |
| Sandbox | Experimentation, auto-delete policy | `sub-sandbox-{team}` |

**Rule of thumb:** One production workload (or product line) per subscription — blast radius and cost attribution.

### WAF pillar → Azure service mapping
| Pillar | Key questions | Azure levers |
|--------|---------------|--------------|
| Reliability | What fails first? RTO/RPO? | Availability Zones, paired regions, Traffic Manager |
| Security | Who can access what? | Entra ID, RBAC, Private Link, Defender |
| Cost | What's driving spend? | Reservations, budgets, right-sizing Advisor |
| Ops Excellence | Can we deploy safely daily? | IaC, App Insights, Automation |
| Performance | Where is latency? | CDN, caching, scale-out |

### Landing zone decision tree
```mermaid
flowchart TD
    A[New workload] --> B{Regulated / enterprise?}
    B -->|Yes| C[CAF + platform landing zone]
    B -->|No| D{Team < 5?}
    D -->|Yes| E[Single subscription + Policy baseline]
    D -->|No| C
    C --> F[Application landing zone subscription]
```

### Common interview mistakes
- Proposing one subscription for all environments without cost or blast-radius isolation
- Ignoring Azure Policy until after resources are deployed
- Selecting region without checking service availability and data residency

### Interview angle
*"We standardized on management groups + subscription per product line, enforced tagging via Policy deny, and cut orphaned resource spend 18% in quarter one."*
""",
    "week-09/theory/02-intermediate.md": """

## Architect Deep Dive: RBAC & Policy at Scale

### Custom role example (CI/CD deployer)
Grant **only** what the pipeline needs — not Contributor on the subscription:
- `Microsoft.Resources/deployments/write` on resource group
- `Microsoft.Web/sites/write` on App Service scope
- Deny `Microsoft.Authorization/*/write`

### Policy initiative composition
Bundle policies into an initiative assigned at management group:
1. Require tags: Environment, CostCenter, Owner
2. Deny public IP on NICs in production MG
3. Audit unused disks > 30 days
4. Enforce TLS 1.2 on Storage

### Cost guardrails
- **Budget alert** at 80% and 100% on each prod subscription
- **Cost anomaly detection** for sudden spikes (often misconfigured autoscale)
- **Tag-based chargeback** report monthly to product owners

### Defender for Cloud workflow
Weekly platform review: secure score trend → assign Critical/High to owners → block prod deploy pipeline if new Critical unmitigated > 7 days (after baseline period).
""",
    "week-09/theory/03-advanced.md": """

## Architect Deep Dive: Enterprise Adoption

### CAF migration waves
| Wave | Workloads | Risk |
|------|-----------|------|
| 1 | Dev/test, internal tools | Low |
| 2 | Non-critical customer-facing | Medium |
| 3 | Revenue-critical, data-heavy | High — requires landing zone maturity |

### Multi-region active-active (when justified)
Justify with business RTO/RPO and revenue at risk — not "best practice." Start active-passive with Front Door failover; evolve to active-active only when failover drill proves RTO gap.

### FinOps integration
Architect owns **unit economics**: cost per order, per API call, per tenant. Tag at deploy time via IaC — retroactive tagging fails at scale.
""",
    "week-10/theory/01-fundamentals.md": """

## Architect Deep Dive: Compute Selection

### Decision workflow
1. **Latency & scale pattern** — steady HTTP vs event bursts vs long-running
2. **Team ops capacity** — can they run K8s control plane?
3. **Compliance** — VNet isolation, dedicated hardware (Isolated tier)
4. **Cost model** — always-on vs consumption

### .NET workload mapping
| Pattern | First choice | Escalation path |
|---------|--------------|-----------------|
| REST API, predictable load | App Service Standard+ | Premium + autoscale |
| Sporadic events | Azure Functions Premium | Durable Functions workflows |
| Containerized, no K8s team | Container Apps | AKS when mesh/GitOps needed |
| Legacy .NET Framework | VM or App Service Windows | Containerize later |

### App Service production checklist
- [ ] Deployment slots + health check path hits DB/cache
- [ ] Managed Identity to Key Vault and SQL
- [ ] Autoscale on CPU **and** HTTP queue length
- [ ] Always On disabled only on non-prod cost saves
- [ ] ARR affinity off unless session state requires it

### Anti-pattern
Running AKS for a single stateless API because "it's cloud native" — 2 platform engineers worth of ops for no architectural benefit.
""",
    "week-10/theory/02-intermediate.md": """

## Architect Deep Dive: App Service & Functions Production

### Slot swap safe sequence
1. Deploy to staging slot
2. Run smoke + integration tests against staging URL
3. Warm-up ping `/health` (validates SQL, Redis)
4. Swap — monitor 5xx for 15 minutes
5. Rollback = swap back (instant)

### Functions architecture patterns
- **HTTP trigger** → thin API, delegate to service layer
- **Queue trigger** → async processing, idempotent handler
- **Durable Functions** → saga/orchestration without Service Bus choreography complexity for medium workflows

### VNet integration
App Service and Functions Premium integrate into spoke VNet for Private Link to SQL, Service Bus, and internal APIs — required for many enterprise security reviews.
""",
    "week-10/theory/03-advanced.md": """

## Architect Deep Dive: Multi-Compute Topologies

### Hybrid example: order platform
```mermaid
flowchart LR
    Client --> FD[Front Door]
    FD --> API[App Service - Order API]
    API --> SB[Service Bus]
    SB --> FN[Functions - notifications]
    API --> SQL[(Azure SQL)]
    FN --> SQL
```

API stays on App Service for team familiarity; bursty notification fan-out on Functions consumption/premium.

### Scale trigger review
Before Black Friday: load test 2× peak, verify autoscale rules, SQL DTU/vCore headroom, and connection pool limits on App Service plan instance count.
""",
    "week-11/theory/01-fundamentals.md": """

## Architect Deep Dive: Data Platform Strategy

### SQL vs Cosmos vs Blob — decision matrix
| Need | Service |
|------|---------|
| ACID transactions, relational | Azure SQL / PostgreSQL Flexible |
| Global low-latency document, flexible schema | Cosmos DB |
| Files, images, backups, data lake | Blob / ADLS Gen2 |
| Analytics warehouse | Synapse / dedicated SQL pool |
| Search | AI Search (formerly Cognitive Search) |

### Cosmos DB partition key (critical)
Choose key with high cardinality and even distribution — `tenantId` or `userId`, **not** `status` or `country` alone (hot partition).

### Azure SQL tier selection
- **General Purpose** — most .NET OLTP
- **Business Critical** — low latency, readable secondaries in-region
- **Hyperscale** — 100TB+, rapid scale storage

### Backup & RPO
SQL automated backups: point-in-time restore. Define RPO with business — 5 min RPO may require geo-redundant backup + sync replica, not GP defaults alone.
""",
    "week-11/theory/02-intermediate.md": """

## Architect Deep Dive: Polyglot Persistence

### Typical microservice data map
| Service | Store | Why |
|---------|-------|-----|
| Orders | Azure SQL | ACID, reporting |
| Product catalog | PostgreSQL + JSONB | Flexible attributes |
| Sessions / cart | Redis | TTL, speed |
| Product search | AI Search | Full-text, facets |
| Analytics events | Event Hubs → ADLS | Append-only lake |

### EF Core + Azure SQL operations
- Connection retry enabled (`EnableRetryOnFailure`)
- Read replicas via `ApplicationIntent=ReadOnly` for reporting queries
- Query Store enabled in production for regression detection
""",
    "week-11/theory/03-advanced.md": """

## Architect Deep Dive: Data Residency & Scale

### Geo-replication patterns
- **Active geo-replication** (SQL) — readable secondaries, manual failover
- **Cosmos multi-region writes** — trade-off: eventual consistency across regions
- **Blob GRS/RA-GRS** — DR for static assets

### Data migration at scale
Use Azure Database Migration Service or staged bulk copy — never "big bang" cutover without parallel run validation and row-count reconciliation.
""",
    "week-12/theory/01-fundamentals.md": """

## Architect Deep Dive: Identity Architecture

### Identity hierarchy
```
Entra ID Tenant
├── Users & Groups
├── App Registrations (OAuth clients)
├── Enterprise Applications (service principals)
└── Managed Identities (Azure-hosted resources)
```

### Managed Identity first
**Never** store client secrets in App Service config for Azure-to-Azure calls. Use system-assigned MI on App Service → grant SQL `db_datareader` via Entra authentication.

### RBAC vs application permissions
- **RBAC** — who can manage Azure resources
- **API permissions** — what the app can do in Microsoft Graph or downstream APIs

### Conditional Access (architect awareness)
Production admin access: MFA + compliant device + named locations. Break-glass accounts excluded but monitored.
""",
    "week-12/theory/02-intermediate.md": """

## Architect Deep Dive: Auth Patterns for .NET APIs

### Recommended API auth stack
1. **Entra ID** — workforce and B2B
2. **Entra External ID / B2C** — customer identity
3. **JWT validation** — `Microsoft.Identity.Web` in ASP.NET Core
4. **APIM** — optional central JWT validation + rate limit

### Service-to-service
App Service MI → gets token for `api://downstream-app/.default` → calls Payment API with bearer token. No shared API keys in config.

### Least privilege example
CI/CD federated credential scoped to `repo:org/app:environment:production` — not subscription Contributor.
""",
    "week-12/theory/03-advanced.md": """

## Architect Deep Dive: Zero Trust on Azure

### Principles applied
- Verify explicitly (every request authenticated)
- Least privilege (RBAC + app roles)
- Assume breach (Private Link, no public SQL endpoints)

### PIM for break-glass
Just-in-time Owner on production subscription — approval + time-bound — satisfies auditor without standing admin access.
""",
    "week-13/theory/01-fundamentals.md": """

## Architect Deep Dive: Hub-Spoke Networking

### Reference topology
```mermaid
flowchart TB
    subgraph Hub
        FW[Azure Firewall]
        DNS[Private DNS]
        LA[Log Analytics]
    end
    subgraph Spoke1[Spoke - Orders]
        VNet1[VNet 10.1.0.0/16]
        App1[App Service VNet integrated]
    end
    subgraph Spoke2[Spoke - Payments]
        VNet2[VNet 10.2.0.0/16]
    end
    Spoke1 --> FW
    Spoke2 --> FW
    FW --> Internet
```

### When to use Private Link
SQL, Storage, Key Vault, Service Bus — eliminate public endpoints. App Service routes via VNet integration to private endpoint NICs.

### NSG rules mindset
Default deny inbound; allow only required paths. Document east-west rules between spokes — avoid "allow all VNet" shortcuts.
""",
    "week-13/theory/02-intermediate.md": """

## Architect Deep Dive: Ingress & Egress

### Front Door vs Application Gateway
| | Front Door | App Gateway |
|---|------------|-------------|
| Scope | Global, multi-region | Regional |
| WAF | Global WAF | Regional WAF |
| Use | Public SaaS, global users | Single-region VNet ingress |

### Egress control
Force outbound via Azure Firewall in hub — required for URL filtering and logging in regulated industries. App Service regional VNet integration sends outbound through spoke UDR to firewall.
""",
    "week-13/theory/03-advanced.md": """

## Architect Deep Dive: Multi-Region Networking

### Active-passive DNS
Front Door priority routing: primary region priority 1, secondary priority 2. Health probes on `/health` every 30s — automatic failover when primary unhealthy.

### Cross-region data
Networking failover ≠ data failover — align RPO with SQL geo-replication or Cosmos multi-region config before claiming DR readiness.
""",
    "week-14/theory/01-fundamentals.md": """

## Architect Deep Dive: Defense in Depth

### Layers
1. **Perimeter** — WAF, DDoS Protection Standard
2. **Network** — NSG, Private Link, Firewall
3. **Identity** — Entra ID, Conditional Access
4. **Application** — input validation, authZ policies
5. **Data** — TDE, encryption at rest, CMK if required

### Key Vault architecture
- Secrets, keys, certificates centralized
- RBAC: deploy pipeline gets `Secrets User` on specific vault
- Soft delete + purge protection enabled in production

### Microsoft Defender for Cloud
Enable on all subscriptions in landing zone — feed Critical findings to backlog with SLA.
""",
    "week-14/theory/02-intermediate.md": """

## Architect Deep Dive: Application Security

### OWASP API top risks — architect responses
| Risk | Mitigation |
|------|------------|
| Broken auth | Entra ID + policy-based authZ |
| Excessive data exposure | DTO projection, pagination |
| Rate limiting | APIM or ASP.NET rate limiter |
| Injection | parameterized queries, ORM |

### Secret scanning in CI
GitGuardian / Defender for DevOps on every PR — block merge on verified secret leak.
""",
    "week-14/theory/03-advanced.md": """

## Architect Deep Dive: Compliance Architecture

### SOC 2 / ISO mapping (simplified)
- **CC6** logical access → Entra ID + RBAC
- **CC7** monitoring → Log Analytics, Defender
- **CC8** change management → IaC pipeline audit logs

### Data classification
Tag SQL columns and Blob containers Public/Internal/Confidential/Restricted — drives encryption and access patterns.
""",
    "week-15/theory/01-fundamentals.md": """

## Architect Deep Dive: Messaging Selection

### Service Bus vs Event Grid vs Event Hubs
| Service | Pattern | Example |
|---------|---------|---------|
| Service Bus | Commands, workflows, ordering | `ProcessOrder` queue |
| Event Grid | Reactive notifications | Blob created → trigger Function |
| Event Hubs | High-volume event stream | Clickstream, IoT ingress |

### Reliability trio
1. **Outbox** — atomic DB write + message intent
2. **Idempotent consumer** — `messageId` dedup table
3. **DLQ** — poison messages isolated with alert

### At-least-once reality
Design every handler to be idempotent — exactly-once is a myth without distributed transactions you should avoid.
""",
    "week-15/theory/02-intermediate.md": """

## Architect Deep Dive: Integration Patterns

### Saga on Azure
Choreography: OrderPlaced event → Inventory + Payment subscribers. Orchestration: Durable Functions or Logic Apps for visual workflows with compensation.

### APIM as integration hub
External partners connect via APIM — throttling, JWT, request transformation — backend microservices stay private on VNet.
""",
    "week-15/theory/03-advanced.md": """

## Architect Deep Dive: Event-Driven at Scale

### Schema governance
Event schema in Git (AsyncAPI / CloudEvents envelope) — breaking changes require versioned topic or `eventType` v2 suffix.

### Ordering
Service Bus sessions on `orderId` when sequential processing required — accept throughput trade-off.
""",
    "week-16/theory/01-capstone-guide.md": """

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
""",
    "week-17/theory/01-fundamentals.md": """

## Architect Deep Dive: AWS for Multi-Cloud Architects

### Azure ↔ AWS concept map
| Azure | AWS |
|-------|-----|
| Resource Group | (tags + account structure) |
| App Service | Elastic Beanstalk / App Runner |
| Azure SQL | RDS SQL Server / Aurora |
| Service Bus | SQS + SNS |
| Entra ID | IAM Identity Center |
| Key Vault | Secrets Manager |
| AKS | EKS |

### Account strategy
Separate accounts per environment (AWS Organizations) — mirrors Azure subscription isolation.

### When AWS in Azure shop
Acquired company on AWS, specific ML service, or customer mandate — integrate via private connectivity (ExpressRoute + Direct Connect) not public internet replication.
""",
    "week-17/theory/02-intermediate.md": """

## Architect Deep Dive: AWS Identity & Landing Zone

### Control Tower vs manual
Control Tower for greenfield AWS org — guardrails, account vending. Brownfield: incremental Organizations + SCPs.

### IAM best practices
- No long-lived access keys for humans
- OIDC federation from GitHub Actions (same pattern as Azure)
- Permission boundaries on CI roles
""",
    "week-17/theory/02-compute-overview.md": """

## Architect Deep Dive: AWS Compute for .NET

| AWS service | .NET fit |
|-------------|----------|
| ECS Fargate | Containers without K8s |
| EKS | Full K8s — same trade-offs as AKS |
| Lambda | Event handlers — cold start awareness |
| Elastic Beanstalk | Closest to App Service simplicity |

**Architect tip:** Prefer managed PaaS/container service until K8s operational maturity proven.
""",
    "week-17/theory/03-advanced.md": """

## Architect Deep Dive: Hybrid Identity

### Entra ID + AWS IAM Identity Center
Single sign-on for engineers across clouds — reduces credential sprawl and audit complexity.
""",
    "week-18/theory/01-fundamentals.md": """

## Architect Deep Dive: AWS Serverless & Containers

### Lambda + .NET
Use for async, bursty work — not latency-sensitive synchronous APIs at high QPS (cold starts). Provisioned concurrency for predictable latency.

### ECS vs EKS decision
Same as Container Apps vs AKS on Azure — start ECS Fargate, graduate to EKS when mesh/GitOps/custom operators required.
""",
    "week-18/theory/02-intermediate.md": """

## Architect Deep Dive: Serverless Integration

### Event-driven AWS pattern
S3 upload → EventBridge → Lambda → DynamoDB metadata — mirror with Blob → Event Grid → Function → Cosmos.
""",
    "week-18/theory/03-advanced.md": """

## Architect Deep Dive: Multi-Region AWS

Route 53 health checks + failover routing — equivalent to Azure Front Door priority pools. Validate data replication separately.
""",
    "week-19/theory/01-fundamentals.md": """

## Architect Deep Dive: AWS Data & Networking

### VPC design parallels
AWS VPC ≈ Azure VNet — public/private subnets, NAT gateway (cost awareness — ~$32/mo+ per NAT), security groups ≈ NSG.

### RDS vs Aurora
RDS for standard SQL Server/MySQL/Postgres. Aurora when AWS-native scale and fast failover needed — evaluate cost vs Azure SQL BC tier equivalent.
""",
    "week-19/theory/02-intermediate.md": """

## Architect Deep Dive: Cross-Cloud Networking

Private connectivity between Azure and AWS for replication or hybrid apps — VPN or partner interconnect; architect documents bandwidth, latency, and operational ownership.
""",
    "week-19/theory/03-advanced.md": """

## Architect Deep Dive: Data Sovereignty Multi-Cloud

When data must stay in EU: pin Azure West Europe **and** AWS eu-west-1 — document which system of record lives where to avoid compliance gaps.
""",
    "week-20/theory/01-fundamentals.md": """

## Architect Deep Dive: Multi-Cloud Strategy

### Valid reasons
- Acquisition integration timeline
- Best-of-breed service (specific AI, specific region)
- Avoid single-vendor negotiation lock-in (with eyes open on operational cost)

### Invalid reasons
- "Avoid vendor lock-in" without quantifying portability cost — you will be multi-cloud operational forever

### Portable layer
Kubernetes, Terraform, OpenTelemetry, PostgreSQL, S3-compatible APIs — abstract where ROI clear; embrace managed services where team velocity matters.
""",
    "week-20/theory/02-intermediate.md": """

## Architect Deep Dive: Abstraction Patterns

### Active-active pitfalls
Split-brain data, conflicting writes, doubled operational runbooks. Prefer active-passive per cloud with clear failover runbook until team proves multi-master competence.
""",
    "week-20/theory/03-advanced.md": """

## Architect Deep Dive: Exit Strategy

Every managed service choice should note **migration cost** in ADR: "If we leave Azure SQL, we need logical export + downtime window of X hours." Honesty beats faux portability.
""",
}


def deepen_file(rel_path: str, appendix: str) -> None:
    path = ROOT / "weeks" / rel_path
    if not path.exists():
        print(f"SKIP missing {rel_path}")
        return
    text = path.read_text(encoding="utf-8")
    marker = "## Architect Deep Dive"
    if marker in text:
        print(f"SKIP already deepened {rel_path}")
        return
    if "**Next:**" in text:
        text = text.replace("**Next:**", appendix + "\n**Next:**", 1)
    else:
        text = text.rstrip() + appendix + "\n"
    path.write_text(text, encoding="utf-8")
    print(f"Deepened {rel_path}")


def main():
    for rel, content in APPEND.items():
        deepen_file(rel, content)
    print("Done — cloud theory weeks 9–20 deepened")


if __name__ == "__main__":
    main()
