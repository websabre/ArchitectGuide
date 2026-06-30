# AWS Fundamentals & Well-Architected Framework

> **Week 17** | **Module:** [aws-fundamentals](../../../modules/aws-fundamentals/README.md)

## AWS Global Infrastructure
- **Regions** — geographic (us-east-1, eu-west-1)
- **Availability Zones** — isolated datacenters within region (3+ per region)
- **Edge Locations** — CloudFront CDN points of presence

## AWS Account Strategy
```
AWS Organization
├── Management Account
├── OU: Production
│   ├── account-prod-app-a
│   └── account-prod-app-b
├── OU: Non-Production
│   ├── account-dev
│   └── account-staging
└── OU: Security (log archive, audit)
```

**Control Tower:** Landing zone automation — guardrails, account vending.

## Well-Architected Framework (6 Pillars)
1. **Operational Excellence** — Observability, IaC, runbooks
2. **Security** — IAM, encryption, detective controls
3. **Reliability** — Multi-AZ, auto-healing, DR
4. **Performance Efficiency** — Right-sizing, serverless, caching
5. **Cost Optimization** — Reserved, Spot, rightsizing
6. **Sustainability** — Resource efficiency (newer pillar)

*Azure has 5 pillars; AWS has 6 — know both for multi-cloud interviews.*

## Core IAM Concepts
| Concept | Azure Equivalent |
|---------|------------------|
| IAM User | Entra ID user (local IAM user avoid in prod) |
| IAM Role | Managed Identity / App Registration |
| IAM Policy | RBAC role definition (JSON) |
| Permission boundary | — |
| SCP (Organizations) | Azure Policy at MG level |

**Best practice:** No long-lived access keys. Roles for EC2/Lambda. OIDC for GitHub Actions.

## Shared Responsibility Model
| AWS Manages | You Manage |
|-------------|------------|
| Hypervisor, physical | Data, OS (IaaS), app, IAM |
| Managed services (RDS) | Data, config, access |



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

**Next:** [02-compute-overview.md](02-compute-overview.md)
