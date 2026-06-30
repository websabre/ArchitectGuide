#!/usr/bin/env python3
"""Generate cloud theory 02/03, phase capstones, and supporting assets."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Azure weeks 9-16, AWS 17-20 — (topic, module_slug, [(filename, content), ...])
CLOUD_WEEKS = {
    9: ("Azure Fundamentals & WAF", "azure-fundamentals", [
        ("03-advanced.md", """# Azure Fundamentals — Advanced

> **Week 09** | **Level:** Advanced

## Multi-Subscription Strategy for Enterprise

```mermaid
flowchart TB
    MG[Management Group Root]
    MG --> Platform[Platform MG]
    MG --> Apps[Application MG]
    Platform --> subNet[sub-connectivity]
    Platform --> subMgmt[sub-management]
    Apps --> subProd[sub-prod-team-a]
    Apps --> subNonProd[sub-nonprod-team-a]
```

## CAF Migration Stages

1. **Strategy** — Business justification, skills
2. **Plan** — Landing zone, migration plan
3. **Ready** — Landing zone deployed
4. **Adopt** — Migrate workloads
5. **Govern** — Policy, cost, security
6. **Manage** — Operate, optimize

## Architect Interview Scenarios

- Design subscriptions for 5 teams with SOC 2
- Justify zone redundancy vs cost for 99.9% SLA
- Map WAF pillars to a specific workload trade-off

**Premium Q&A:** [Azure Top 50](../../../interview-prep/azure-top-50-index.md)

**Previous:** [02-intermediate.md](02-intermediate.md) | [Week 09](../README.md)
"""),
    ]),
    10: ("Azure Compute", "azure-services", [
        ("03-advanced.md", """# Azure Compute — Advanced

> **Week 10** | **Level:** Advanced

## Autoscale Patterns

| Signal | App Service | AKS |
|--------|-------------|-----|
| CPU | Built-in rules | HPA + metrics server |
| Queue depth | Custom metric | KEDA |
| Schedule | Scale up before business hours | CronHPA |

## Cold Start Mitigation

- **Functions:** Premium plan with pre-warmed instances
- **Container Apps:** min replicas > 0 for latency-sensitive
- **App Service:** Always On (non-consumption plans)

## Multi-Region Compute

- Front Door → regional App Services
- Session affinity implications for stateful apps
- Deployment slots per region vs global slot swap

**Previous:** [02-intermediate.md](02-intermediate.md) | **Lab:** [week-10 labs](../labs/)
"""),
    ]),
    11: ("Azure Data Platform", "azure-data", [
        ("02-intermediate.md", """# Azure Data Platform — Intermediate

> **Week 11** | **Level:** Intermediate

## SQL vs Cosmos — Decision Matrix

| Factor | Azure SQL | Cosmos DB |
|--------|-----------|-----------|
| Data model | Relational, ACID | Document / multi-model |
| Scale pattern | Vertical + read replicas | Horizontal partition key |
| Consistency | Strong default | Tunable (5 levels) |
| Cost at low scale | Often cheaper | RU minimums add up |

## Partition Key Design (Cosmos)

- High cardinality (userId, tenantId) — avoid hot partitions
- Include in queries — cross-partition scans are expensive
- Synthetic keys for even distribution when natural key skews

## Blob Lifecycle Policies

```
Hot (30 days) → Cool (90 days) → Archive
```

Architect: align tier to access pattern; archive for compliance retention.

**Next:** [03-advanced.md](03-advanced.md)
"""),
        ("03-advanced.md", """# Azure Data Platform — Advanced

> **Week 11** | **Level:** Advanced

## Multi-Region Data Architecture

- **SQL:** Active geo-replication (readable secondaries) vs failover groups (RPO ~5s)
- **Cosmos:** Multi-region writes with session consistency for most apps
- **Synapse:** Separate compute pools for ETL vs ad-hoc analytics

## RU/s Sizing and Cost Control

- Start with autoscale max RU; monitor 429 throttling
- Serverless for dev/spiky; provisioned for predictable production
- Partition merge/split planning before 20GB per partition limit

## Architect Scenario

Design data layer for multi-tenant SaaS: 500 tenants, 10K TPS reads, 500 TPS writes.

**Deliverables:** ER diagram, partition strategy, DR RPO/RTO, cost estimate order of magnitude.
"""),
    ]),
    12: ("Azure Identity", "azure-identity", [
        ("02-intermediate.md", """# Azure Identity — Intermediate

> **Week 12** | **Level:** Intermediate

## Conditional Access Policies

| Control | Example |
|---------|---------|
| Require MFA | All users except break-glass |
| Block legacy auth | POP/IMAP/SMTP AUTH |
| Require compliant device | Production admin portals |
| Sign-in risk | Block high risk, require MFA medium |

## Managed Identity Patterns

```mermaid
flowchart LR
    App[App Service] -->|MI token| KV[Key Vault]
    App -->|MI token| SQL[Azure SQL]
    Pipeline[GitHub Actions OIDC] -->|federated cred| Entra[Entra ID]
    Pipeline --> Deploy[Azure Deploy]
```

## OBO (On-Behalf-Of) Flow

User token → API → downstream API with user context preserved. Required for delegated permissions across microservices.

**Next:** [03-advanced.md](03-advanced.md)
"""),
        ("03-advanced.md", """# Azure Identity — Advanced

> **Week 12** | **Level:** Advanced

## Zero Trust on Azure

- Verify explicitly: Conditional Access + continuous access evaluation
- Least privilege: PIM for admin roles, scoped RBAC
- Assume breach: Defender for Cloud, logging to Log Analytics

## B2B vs B2C

| | B2B | B2C |
|---|-----|-----|
| Users | Partner orgs in your tenant | Consumer identities |
| Use | Supplier portal | Customer login |
| Directory | Guest users | Separate B2C tenant |

## Architect Checklist

- [ ] No secrets in appsettings — Key Vault references
- [ ] CI/CD uses OIDC federation, not long-lived SP secrets
- [ ] API exposes only required scopes
- [ ] Service principals documented with owners

**Cross-cutting:** [Security](../../../docs/cross-cutting/security/README.md)
"""),
    ]),
    13: ("Azure Networking", "azure-architecture", [
        ("02-intermediate.md", """# Azure Networking — Intermediate

> **Week 13** | **Level:** Intermediate

## Hub-Spoke Topology

```mermaid
flowchart TB
    Hub[Hub VNet - Firewall DNS]
    Spoke1[Spoke - App Team A]
    Spoke2[Spoke - App Team B]
    Hub --> Spoke1
    Hub --> Spoke2
    Hub --> OnPrem[ExpressRoute VPN]
```

## Private Link vs Service Endpoints

| Feature | Service Endpoint | Private Endpoint |
|---------|------------------|------------------|
| Traffic | Stays on Azure backbone | Private IP in your VNet |
| DNS | Public endpoint | Private DNS zone required |
| Exfiltration protection | Partial | Stronger |

**Architect default:** Private Link for SQL, Storage, Key Vault in production.

**Next:** [03-advanced.md](03-advanced.md)
"""),
        ("03-advanced.md", """# Azure Networking — Advanced

> **Week 13** | **Level:** Advanced

## Application Gateway vs Front Door

| Factor | App Gateway | Front Door |
|--------|-------------|------------|
| Layer | Regional L7 | Global L7 |
| WAF | Regional WAF | Global WAF |
| Use | Single region | Multi-region, global users |

## DNS Strategy

- Azure DNS private zones linked to VNets
- Split-horizon DNS for hybrid
- TTL planning for failover (lower TTL = faster failover, more queries)

## Capstone Tie-In

Design hub-spoke for 3 teams with shared firewall and private SQL access.

**Cross-cutting:** [Networking fundamentals](../../../docs/cross-cutting/networking-fundamentals/README.md)
"""),
    ]),
    14: ("Azure Security", "azure-security", [
        ("02-intermediate.md", """# Azure Security — Intermediate

> **Week 14** | **Level:** Intermediate

## Defense in Depth Layers

1. **Identity** — Entra ID, Conditional Access
2. **Network** — NSG, Firewall, Private Link
3. **Compute** — Patching, Defender for Servers
4. **Data** — Encryption at rest (CMK vs PMK), TDE
5. **Application** — WAF, input validation, OWASP

## Key Vault Architecture

- Separate vaults per environment (prod/nonprod)
- RBAC over access policies for new deployments
- Soft delete + purge protection in production
- Rotation via automation runbooks or Key Vault rotation

## WAF Rules Strategy

- OWASP 3.2 managed rule set baseline
- Custom rules for rate limiting, geo-blocking
- False positive tuning in detection mode before prevention

**Next:** [03-advanced.md](03-advanced.md)
"""),
        ("03-advanced.md", """# Azure Security — Advanced

> **Week 14** | **Level:** Advanced

## Threat Modeling (STRIDE)

| Threat | Mitigation on Azure |
|--------|---------------------|
| Spoofing | MFA, managed identity |
| Tampering | Immutable storage, signing |
| Repudiation | Diagnostic logs, Activity Log |
| Information disclosure | Private Link, encryption |
| Denial of service | Front Door rate limits, DDoS Standard |
| Elevation of privilege | Least privilege RBAC, PIM |

## DevSecOps Pipeline

```
PR → Sonar/Snyk → Build → Container scan → Deploy to staging → DAST
```

Architect: define quality gates — block on critical CVEs.

**Cross-cutting:** [Security deep dive](../../../docs/cross-cutting/security/README.md)
"""),
    ]),
    15: ("Azure Integration", "azure-integration", [
        ("02-intermediate.md", """# Azure Integration — Intermediate

> **Week 15** | **Level:** Intermediate

## Messaging Service Selection

| Pattern | Service |
|---------|---------|
| Queue (point-to-point) | Service Bus Queue |
| Pub/sub with topics | Service Bus Topic |
| Event routing (reactive) | Event Grid |
| High-volume streaming | Event Hubs |
| Orchestration | Logic Apps / Durable Functions |

## Service Bus vs Event Hubs

- **Service Bus:** Orders, commands, lower volume, sessions, transactions
- **Event Hubs:** Telemetry, clickstreams, millions of events/sec

## Idempotency and Duplicate Detection

- MessageId + duplicate detection window (Service Bus)
- Idempotent consumers with business key dedup table
- Outbox pattern for DB + message atomicity

**Next:** [03-advanced.md](03-advanced.md)
"""),
        ("03-advanced.md", """# Azure Integration — Advanced

> **Week 15** | **Level:** Advanced

## Event-Driven Architecture on Azure

```mermaid
flowchart LR
    API[Order API] --> SB[Service Bus]
    SB --> Inv[Inventory Service]
    SB --> Pay[Payment Service]
    API --> EG[Event Grid]
    EG --> FN[Azure Functions]
```

## Saga Patterns

- **Choreography:** Events only — simpler, harder to debug
- **Orchestration:** Durable Functions / Logic Apps — visible state, more coupling

## Architect Scenario

Order placed → reserve inventory → charge payment → confirm order. Design failure compensation for payment timeout.

**Related:** [Week 35 messaging](../../week-35/theory/)
"""),
    ]),
    16: ("Azure Production Capstone", "azure-architecture", [
        ("02-intermediate.md", """# Azure Production Capstone — Intermediate Review

> **Week 16** | **Level:** Intermediate

## Capstone Architecture Checklist

| Area | Must Document |
|------|---------------|
| Compute | App Service vs AKS justification |
| Data | SQL/Cosmos choice, DR |
| Identity | Entra, MI, Key Vault |
| Network | Hub-spoke or simplified with Private Link |
| Integration | Service Bus / Event Grid |
| Observability | App Insights, alerts, dashboards |
| Security | WAF, NSG, Defender |
| Cost | Budget alerts, right-sizing |

## C4 Diagram Requirements

- **Context:** Users, external systems
- **Container:** APIs, databases, message bus
- **Component:** Optional for critical service

**Guide:** [01-capstone-guide.md](01-capstone-guide.md)
"""),
        ("03-advanced.md", """# Azure Production Capstone — Advanced Review

> **Week 16** | **Level:** Advanced

## Production Readiness Review

### SLA Math

- App Service 99.95% ≈ 22 min downtime/month
- Multi-region active-active for 99.99%+
- Document dependency chain — weakest link sets SLA

### DR Runbook Outline

1. Detection (alert threshold)
2. Decision (failover criteria)
3. Execution (DNS, traffic manager)
4. Validation (synthetic tests)
5. Communication (status page, stakeholders)

### Interview Presentation (10 min)

1. Problem & requirements (2 min)
2. Architecture diagram walkthrough (4 min)
3. Key trade-offs & ADRs (3 min)
4. What you'd do with 6 more months (1 min)

**Month 4 capstone:** [program/phase-04](../../../program/phase-04-month-04/capstone.md)
"""),
    ]),
    17: ("AWS Fundamentals", "aws-fundamentals", [
        ("02-intermediate.md", """# AWS Fundamentals — Intermediate

> **Week 17** | **Level:** Intermediate

## AWS Organizations & SCPs

- **Organization** → OUs → Accounts (mirror Azure MG → Subscription)
- **SCP (Service Control Policy):** Guardrails — deny regions, deny root API keys
- **Control Tower:** Landing zone automation

## IAM Best Practices

| Practice | Implementation |
|----------|----------------|
| No root for daily ops | Break-glass only |
| Roles not users for apps | EC2 instance profile, Lambda execution role |
| Least privilege | Permission boundaries |
| Cross-account | Role assumption with external ID |

## Well-Architected Review

Six pillars (adds Sustainability to Azure's five). Run WAFR before major launches.

**Also see:** [02-compute-overview.md](02-compute-overview.md)

**Next:** [03-advanced.md](03-advanced.md)
"""),
        ("03-advanced.md", """# AWS Fundamentals — Advanced

> **Week 17** | **Level:** Advanced

## Multi-Account Strategy

```
Organization Root
├── Security OU (log archive, audit)
├── Infrastructure OU (shared networking)
└── Workloads OU
    ├── prod-account
    └── nonprod-account
```

## Cost Allocation

- Mandatory tags via SCP + Config rules
- Cost Explorer + CUR to S3 for FinOps
- Reserved Instances / Savings Plans for baseline

**Premium Q&A:** [AWS Top 50](../../../interview-prep/aws-top-50-index.md)
"""),
    ]),
    18: ("AWS Compute", "aws-compute", [
        ("02-intermediate.md", """# AWS Compute — Intermediate

> **Week 18** | **Level:** Intermediate

## Compute Selection Matrix

| Workload | Service |
|----------|---------|
| .NET API always-on | ECS Fargate / EKS / Elastic Beanstalk |
| Spiky HTTP | Lambda + API Gateway |
| Long-running batch | EC2 / Batch |
| Containers without K8s ops | ECS Fargate |

## Lambda Cold Starts (.NET)

- Native AOT (where supported) reduces init time
- Provisioned concurrency for latency-sensitive paths
- Keep handlers small; reuse static clients

## ECS vs EKS

| | ECS | EKS |
|---|-----|-----|
| Ops burden | Lower | Higher |
| Portability | AWS-native | Kubernetes standard |
| Team skill | AWS-focused | K8s experience |

**Next:** [03-advanced.md](03-advanced.md)
"""),
        ("03-advanced.md", """# AWS Compute — Advanced

> **Week 18** | **Level:** Advanced

## Multi-AZ and Auto Scaling

- ALB across 2+ AZs — health checks, deregistration delay
- ASG: target tracking on CPU or custom CloudWatch metric
- Blue/green with CodeDeploy or separate target groups

## Serverless Architecture Limits

- Lambda 15 min timeout — not for long jobs
- API Gateway payload limits — use S3 presigned for uploads
- Step Functions for orchestration across Lambdas

## Architect Scenario

Migrate .NET Framework monolith on EC2 to modern .NET on AWS — phased approach with ALB path-based routing.
"""),
    ]),
    19: ("AWS Data & Networking", "aws-networking", [
        ("02-intermediate.md", """# AWS Data & Networking — Intermediate

> **Week 19** | **Level:** Intermediate

## VPC Design

```
VPC 10.0.0.0/16
├── Public subnets (ALB, NAT Gateway)
├── Private subnets (ECS, RDS)
└── Isolated subnets (RDS only, no NAT)
```

## RDS vs DynamoDB

| | RDS/Aurora | DynamoDB |
|---|------------|----------|
| Model | SQL | Key-value/document |
| Scale | Read replicas, Aurora Serverless | On-demand or provisioned RCU/WCU |
| Use | Transactions, joins | High scale key access |

## S3 Storage Classes

- Standard → IA → Glacier Instant → Glacier Deep Archive
- Intelligent-Tiering for unknown access patterns

**Next:** [03-advanced.md](03-advanced.md)
"""),
        ("03-advanced.md", """# AWS Data & Networking — Advanced

> **Week 19** | **Level:** Advanced

## Hybrid Connectivity

- **Site-to-Site VPN:** Quick, limited bandwidth
- **Direct Connect:** Dedicated, predictable latency, higher setup
- **Transit Gateway:** Hub for VPC + on-prem connectivity

## PrivateLink vs VPC Endpoints

- **Gateway endpoint:** S3, DynamoDB (route table)
- **Interface endpoint:** Most other services (ENI in subnet)

## Route 53 Patterns

- Failover routing with health checks
- Latency-based routing for global users
- Weighted routing for blue/green

**Cross-cutting:** [Networking fundamentals](../../../docs/cross-cutting/networking-fundamentals/README.md)
"""),
    ]),
    20: ("Multi-Cloud", "multi-cloud", [
        ("02-intermediate.md", """# Multi-Cloud Architecture — Intermediate

> **Week 20** | **Level:** Intermediate

## Azure ↔ AWS Service Mapping

| Capability | Azure | AWS |
|------------|-------|-----|
| VM | Virtual Machines | EC2 |
| PaaS API | App Service | Elastic Beanstalk / App Runner |
| Kubernetes | AKS | EKS |
| Serverless | Functions | Lambda |
| SQL | Azure SQL | RDS / Aurora |
| NoSQL | Cosmos DB | DynamoDB |
| Object storage | Blob | S3 |
| Identity | Entra ID | IAM + Cognito |
| Secrets | Key Vault | Secrets Manager |
| Messaging | Service Bus | SQS/SNS |

## What's Actually Portable

| Portable | Locked-in |
|----------|-----------|
| Containers + K8s | PaaS-specific bindings |
| Terraform (with caveats) | Native serverless triggers |
| OpenTelemetry | Proprietary AI services |
| PostgreSQL | Cosmos DB specific APIs |

**Next:** [03-advanced.md](03-advanced.md)
"""),
        ("03-advanced.md", """# Multi-Cloud Architecture — Advanced

> **Week 20** | **Level:** Advanced

## FARCS Framework (Interview)

- **F**unctional requirements
- **A**vailability / DR
- **R**eplication / data residency
- **C**ost
- **S**ecurity / compliance

## FinOps Across Clouds

- Unit economics: cost per transaction, per tenant
- Commitment strategies: RIs, Savings Plans, Azure Reservations
- Tagging enforcement via policy (Azure Policy, SCPs)

## Architect Scenario

CTO wants active-active in Azure and AWS for payment API. Design portable core + cloud-specific adapters. Document trade-offs.

**Cross-cutting:** [FinOps](../../../docs/cross-cutting/finops-cost-optimization/README.md)

**Premium Q&A:** [Azure Top 50](../../../interview-prep/azure-top-50-index.md) | [AWS Top 50](../../../interview-prep/aws-top-50-index.md)
"""),
    ]),
}

CAPSTONES = {
    1: ("Design a Modular .NET API", "Build a Clean Architecture order API with ADRs, 3+ patterns, async I/O, and assessment ≥70% on weeks 1–4.", [
        "Clean Architecture layers documented",
        "2 ADRs (pattern choice, async strategy)",
        "120+ interview questions practiced",
        "Month 1 Top 50: score self ≥70%",
    ]),
    2: ("E-Commerce Data Layer at Scale", "Design data layer for 10M users: SQL vs NoSQL, indexing, caching, read replicas.", [
        "ER diagram + sharding strategy",
        "Index design for top 5 queries",
        "Database selection decision tree",
    ]),
    3: ("Azure 3-Tier SaaS", "Landing zone + App Service + SQL + Entra ID for multi-tenant SaaS.", [
        "C4 Context + Container diagrams",
        "Identity architecture diagram",
        "Cost estimate order of magnitude",
    ]),
    4: ("Multi-Region Azure Production", "99.95% SLA design with DR, networking, security, integration.", [
        "Hub-spoke network diagram",
        "DR runbook outline",
        "Security controls mapped to WAF",
    ]),
    5: ("Same Workload: Azure vs AWS", "Design payment API on both clouds; document portable vs locked-in choices.", [
        "Side-by-side comparison table",
        "ADR: primary cloud choice",
        "Migration path if switching clouds",
    ]),
    6: ("12-Service E-Commerce Platform", "Microservices decomposition, events, sagas, API gateway.", [
        "Bounded context map",
        "Event choreography diagram",
        "3 failure scenarios + mitigations",
    ]),
    7: ("Deploy .NET to AKS with GitOps", "Containerize microservice, deploy AKS, configure HPA and ingress.", [
        "Multi-stage Dockerfile",
        "Helm chart or manifests in Git",
        "Argo CD or Flux sync demo",
    ]),
    8: ("Full DevOps Platform", "Month 8 capstone: Bicep + GitHub Actions OIDC + OTel + feature flags.", [
        "[lab-32-month8-capstone.md](../../weeks/week-32/labs/lab-32-month8-capstone.md)",
    ]),
    9: ("System Design Whiteboard Marathon", "5 designs: URL shortener, chat, payments, feed, notifications — 45 min each.", [
        "RESHADED framework used each session",
        "Self-score ≥75/100 on 3+ designs",
    ]),
    10: ("Enterprise Document Intelligence Copilot", "RAG architecture with security, LLMOps, cost model.", [
        "Week 40 capstone brief complete",
        "Eval pipeline on 50 golden questions",
    ]),
    11: ("Enterprise Case Study Marathon", "4 case studies with full architecture reviews.", [
        "Week 44 case studies CS44-A through D",
        "2 ADRs per case minimum",
    ]),
    12: ("Graduation Portfolio + Panel Mock", "Portfolio package + 3-round panel mock interview.", [
        "5+ architecture diagrams in portfolio",
        "10 STAR stories rehearsed",
        "[Panel mock ≥80% rubric](../../interview-prep/mock-interviews/mock-06-panel-loop.md)",
    ]),
}


def write_cloud_theory():
    for week, (_topic, _module, files) in CLOUD_WEEKS.items():
        tdir = ROOT / f"weeks/week-{week:02d}/theory"
        tdir.mkdir(parents=True, exist_ok=True)
        for fname, content in files:
            path = tdir / fname
            if not path.exists() or path.stat().st_size < 200:
                path.write_text(content.strip() + "\n", encoding="utf-8")
                print(f"Wrote {path.relative_to(ROOT)}")
            else:
                print(f"Skip (exists): {path.relative_to(ROOT)}")


def write_capstones():
    program = ROOT / "program"
    for month, (title, brief, deliverables) in CAPSTONES.items():
        matches = list(program.glob(f"phase-{month:02d}-*"))
        if not matches:
            print(f"No phase folder for month {month}")
            continue
        phase_dir = matches[0]
        lines = [
            f"# Month {month} Capstone — {title}\n\n",
            f"> **Phase {month}** | Complete after weeks in this month.\n\n",
            "## Brief\n\n", f"{brief}\n\n",
            "## Deliverables\n\n",
        ]
        for d in deliverables:
            if d.startswith("["):
                lines.append(f"- {d}\n")
            else:
                lines.append(f"- [ ] {d}\n")
        lines.extend([
            "\n## Rubric (100 points)\n\n",
            "| Criteria | Points |\n|----------|--------|\n",
            "| Requirements clarity | 20 |\n",
            "| Architecture quality | 30 |\n",
            "| Trade-off documentation | 20 |\n",
            "| Production realism | 15 |\n",
            "| Presentation / ADRs | 15 |\n\n",
            "**Pass:** ≥ 70 points\n\n",
            f"← [Phase overview](README.md) | [SYLLABUS](../../SYLLABUS.md)\n",
        ])
        (phase_dir / "capstone.md").write_text("".join(lines), encoding="utf-8")
        readme = phase_dir / "README.md"
        if readme.exists() and "capstone.md" not in readme.read_text(encoding="utf-8"):
            text = readme.read_text(encoding="utf-8")
            text = text.replace(
                "## Month-End Capstone",
                f"## Month Capstone\n\n**[capstone.md](capstone.md)** — {title}\n\n## Month-End Capstone",
            )
            readme.write_text(text, encoding="utf-8")
        print(f"Capstone month {month}")


def update_theory_readmes():
    for week in CLOUD_WEEKS:
        tdir = ROOT / f"weeks/week-{week:02d}/theory"
        if not tdir.exists():
            continue
        files = sorted(f for f in tdir.glob("*.md") if f.name != "README.md")
        if not files:
            continue
        lines = [
            f"# Week {week:02d} — Theory\n\n",
            f"> [← Week {week:02d} overview](../README.md)\n\n",
            "## Files\n\n",
        ]
        for f in files:
            lines.append(f"- [{f.name}]({f.name})\n")
        start = files[0].name
        lines.extend([
            f"\n**Start here:** [{start}]({start})\n\n",
            "---\n\n",
            f"[← Back to Week {week:02d}](../README.md)\n",
        ])
        (tdir / "README.md").write_text("".join(lines), encoding="utf-8")
        print(f"Updated theory README week {week:02d}")


if __name__ == "__main__":
    write_cloud_theory()
    write_capstones()
    update_theory_readmes()
    print("Done")
