# Azure Governance & Subscription Design

## RBAC Model
- **Owner** — full access including RBAC
- **Contributor** — manage resources, not RBAC
- **Reader** — view only
- Custom roles for least privilege

## Management Groups
```
Root MG
├── Platform MG (shared services)
│   ├── Connectivity (hub VNet)
│   └── Management (Log Analytics)
└── Landing Zones MG
    ├── Production
    ├── Non-Production
    └── Sandbox
```

## Azure Policy
- Enforce tagging, allowed regions, VM SKUs
- Deny public blob access
- Require TLS 1.2

## Cost Management
- Budgets and alerts per subscription
- Reserved instances for predictable workloads
- Dev/test pricing for non-prod subscriptions

## Microsoft Defender for Cloud
- Secure score
- Recommendations
- Regulatory compliance dashboards

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

