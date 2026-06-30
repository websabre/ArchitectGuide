# AWS Fundamentals — Intermediate

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



## Architect Deep Dive: AWS Identity & Landing Zone

### Control Tower vs manual
Control Tower for greenfield AWS org — guardrails, account vending. Brownfield: incremental Organizations + SCPs.

### IAM best practices
- No long-lived access keys for humans
- OIDC federation from GitHub Actions (same pattern as Azure)
- Permission boundaries on CI roles

**Next:** [03-advanced.md](03-advanced.md)
