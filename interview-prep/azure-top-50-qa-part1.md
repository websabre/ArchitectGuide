# Azure Top 50 Interview Q&A — Detailed Answers

> **Premium bank** — Full answers matching Week 1 Q001–Q010 quality.  
> Covers Weeks 9–16 topics. Use for architect and cloud architect interviews.

| Section | Questions | Topics |
|---------|-----------|--------|
| [Fundamentals & WAF](#section-1-fundamentals--waf) | Q001–Q008 | Subscriptions, WAF pillars, landing zones |
| [Compute](#section-2-compute) | Q009–Q014 | App Service, Functions, AKS, Container Apps |
| [Data Platform](#section-3-data-platform) | Q015–Q020 | SQL, Cosmos DB, Blob, data architecture |
| [Identity & Security](#section-4-identity--security) | Q021–Q030 | Entra ID, Managed Identity, Zero Trust, Key Vault |
| [Networking](#section-5-networking) | Q031–Q038 | VNet, hub-spoke, Private Link, Front Door |
| [Integration & Messaging](#section-6-integration--messaging) | Q039–Q046 | Service Bus, Event Grid, Event Hubs, APIM |
| [Architecture Scenarios](#section-7-architecture-scenarios) | Q047–Q050 | Multi-region, DR, cost, capstone |

---

## Section 1: Fundamentals & WAF

## Q001: Azure Well-Architected Framework Pillars

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Azure WAF |
| **Frequency** | Very Common |
| **Week** | 09 |

### Question

What are the five pillars of the Azure Well-Architected Framework? How do you apply them in an architecture review?

### Short Answer (30 seconds)

Reliability, Security, Cost Optimization, Operational Excellence, and Performance Efficiency. In every review I map design decisions to each pillar, identify gaps, and prioritize fixes by business impact.

### Detailed Answer (3–5 minutes)

The Azure WAF provides five pillars:

1. **Reliability** — System recovers from failures and meets SLA. Design for redundancy (availability zones), health probes, automatic failover, chaos testing, defined RTO/RPO.

2. **Security** — Protect data and assets. Identity-first (Entra ID, Managed Identity), encryption at rest/transit, network segmentation (Private Link, NSG), Defender for Cloud, least-privilege RBAC.

3. **Cost Optimization** — Maximize business value per dollar. Right-sizing, reserved instances, autoscale down, storage tiering, tagging for chargeback, eliminate idle resources.

4. **Operational Excellence** — Run and monitor production effectively. IaC (Bicep/Terraform), CI/CD, observability (App Insights), runbooks, blameless postmortems, deployment slots.

5. **Performance Efficiency** — Scale to meet demand. Choose right compute tier, caching (Redis), CDN, async processing, load testing before launch.

**How I apply in reviews:** I use a scorecard per pillar (1–5) for the proposed architecture. Example: a single-region App Service with no DR scores low on Reliability; I document that and propose geo-replication if SLA requires 99.95%.

### Architecture Perspective

Interviewers want to see WAF as a **decision lens**, not a certification checklist. Connect pillars to trade-offs: "We accepted higher cost (Cost) for zone redundancy (Reliability)."

### Follow-up Questions

1. **Which pillar is most neglected?**
   - Cost Optimization — teams over-provision and never right-size. Operational Excellence — many skip runbooks and DR testing.

2. **WAF vs CAF?**
   - WAF = how to design workloads well. CAF (Cloud Adoption Framework) = organizational migration journey (strategy, plan, ready, adopt, govern).

### Common Mistakes in Interviews

- Listing pillars without explaining how they'd evaluate a real design
- Treating pillars as independent — they conflict (Security vs Cost, Performance vs Cost)

---

## Q002: Subscription and Landing Zone Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Azure Governance |
| **Frequency** | Common |
| **Week** | 09 |

### Question

How do you design Azure subscriptions and management groups for an enterprise with 5 product teams?

### Short Answer

Use management groups for hierarchy (Platform vs Landing Zones), separate subscriptions per environment (prod/nonprod) per workload or team, enforce policy at MG level, and tag everything for cost allocation.

### Detailed Answer

**Recommended structure:**

```
Tenant Root Group
├── Platform (MG)
│   ├── sub-connectivity (hub VNet, Firewall, DNS)
│   ├── sub-management (Log Analytics, Automation)
│   └── sub-identity (if dedicated)
└── Landing Zones (MG)
    ├── sub-prod-team-a
    ├── sub-nonprod-team-a
    ├── sub-prod-team-b
    └── sub-sandbox (shared, time-limited)
```

**Principles:**
- **Subscription as security boundary** — RBAC and policy scoped per sub
- **Blast radius** — prod subscription isolated from sandbox experimentation
- **Cost visibility** — one subscription per team/environment enables clear billing
- **Azure Policy at MG level** — allowed regions, required tags, deny public storage

**For 5 teams:** Start with 10–15 subscriptions (prod + nonprod per team), not one subscription for everything. Use Azure Cost Management + tags (CostCenter, Owner, Environment, Application).

### Architecture Perspective

Wrong subscription design is expensive to fix later. Architects set this in month one — not after 200 resource groups in one subscription.

### Follow-up Questions

1. **One sub per team or per app?**
   - Per team per environment for mid-size enterprise. Per app only when regulatory isolation required (PCI, HIPAA workloads).

2. **Sandbox strategy?**
   - Shared sandbox sub with budget caps, auto-shutdown policies, 30-day resource TTL via Policy.

### Common Mistakes in Interviews

- "One subscription is simpler" — ignores RBAC blast radius and cost allocation
- No mention of management groups or Azure Policy

---

## Q003: Azure Region and Availability Zone Selection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Azure Reliability |
| **Frequency** | Common |
| **Week** | 09 |

### Question

When would you deploy across Availability Zones vs multiple Regions?

### Short Answer

Zones for HA within a region (datacenter failure). Regions for DR and data residency. Use zone-redundant services for 99.99% within region; active-active regions for 99.99%+ and geographic compliance.

### Detailed Answer

| Strategy | Protects Against | Typical SLA | Latency |
|----------|------------------|-------------|---------|
| Single zone | Nothing | 99.9% | Lowest |
| Multi-zone (same region) | Datacenter failure | 99.99% | Low |
| Multi-region | Regional outage | 99.99%+ | Higher |
| Multi-region active-active | Regional outage + zero RTO | Highest | Routing complexity |

**Zone example:** App Service zone-redundant plan + Azure SQL zone-redundant database in East US zones 1, 2, 3.

**Region example:** Primary East US, secondary West US with Front Door failover + SQL geo-replication for RPO < 15 min.

**Data residency:** EU customers → deploy in West Europe; US in East US. GDPR may prohibit cross-border replication — use region-paired DR within EU (West Europe + North Europe).

### Architecture Perspective

Zones are not DR across regions — a regional outage (rare but real) requires multi-region design. Cost: zone-redundant ~2x; multi-region ~2x+ with data replication.

### Follow-up Questions

1. **All services support zones?**
   - No — verify per service. Some PaaS is zone-redundant by default (Storage GRS).

2. **Zone vs Set?**
   - Availability Sets are VM-level (legacy). Zones are datacenter-level — preferred for new designs.

### Common Mistakes in Interviews

- Assuming zones = DR (they're not — same region)
- Ignoring data residency when discussing multi-region

---

## Q004: Azure RBAC vs Azure Policy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Azure Governance |
| **Frequency** | Common |
| **Week** | 09 |

### Question

What's the difference between Azure RBAC and Azure Policy?

### Short Answer

RBAC controls **who** can do **what** (authorization). Policy controls **what is allowed** in the environment (governance/compliance), regardless of who deploys.

### Detailed Answer

**Azure RBAC:**
- Who: User, group, service principal, managed identity
- What: Actions on resource types (e.g., `Microsoft.Compute/virtualMachines/read`)
- Roles: Owner, Contributor, Reader, custom roles
- Example: "Dev team can Contributor on nonprod sub only"

**Azure Policy:**
- Rules evaluated at resource create/update
- Effects: Deny, Audit, Append, DeployIfNotExists, Modify
- Example: "Deny creation of VMs without 'Environment' tag"
- Example: "Audit public IP on storage accounts"

**Together:** RBAC grants a developer Contributor access; Policy denies deploying NC-series GPUs in prod or requires HTTPS-only storage.

### Architecture Perspective

Mature enterprises use Policy for guardrails (prevent mistakes) and RBAC for least privilege (limit blast radius). Policy as code in repo alongside Bicep.

### Follow-up Questions

1. **Policy vs ARM/Bicep?**
   - IaC defines intent for one deployment. Policy enforces org-wide rules on every deployment.

2. **Deny vs Audit?**
   - Deny in prod (block violations). Audit in dev (discover drift, educate teams).

### Common Mistakes in Interviews

- Using RBAC to try to enforce tagging (use Policy Append/Modify instead)
- Giving Owner role when Contributor suffices

---

## Q005: Tagging Strategy for FinOps

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Common |
| **Week** | 09, 42 |

### Question

What tags should every Azure resource have, and how do you enforce them?

### Short Answer

Minimum: Environment, CostCenter, Owner, Application. Enforce with Azure Policy (Deny if missing), report with Cost Management, review monthly in FinOps cadence.

### Detailed Answer

**Required tags:**
| Tag | Purpose | Example |
|-----|---------|---------|
| Environment | prod/staging/dev | prod |
| CostCenter | Chargeback | CC-4521 |
| Owner | Accountability | team-payments@company.com |
| Application | Workload grouping | order-api |

**Optional:** Version, DataClassification, Criticality, CreatedDate

**Enforcement:**
```json
// Policy: Require tag on resource groups
"effect": "deny",
"field": "tags['Environment']",
"exists": false
```

**FinOps workflow:**
1. Policy denies untagged deployments in prod
2. Cost Management filters by CostCenter
3. Monthly review: top 10 spenders, orphaned resources, right-sizing recommendations from Advisor
4. Budget alerts at 80%, 100%, 120%

### Architecture Perspective

Untagged resources = ungoverned cloud = bill shock. Architects mandate tagging in landing zone design before first workload deploys.

### Common Mistakes in Interviews

- Tags only for cost — also needed for automation, policy, and incident response
- Manual tagging — must be Policy-enforced

---

## Q006: IaaS vs PaaS vs SaaS on Azure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Cloud Models |
| **Frequency** | Very Common |
| **Week** | 09, 10 |

### Question

Explain IaaS, PaaS, and SaaS. When would you choose each on Azure for a .NET workload?

### Short Answer

IaaS = you manage OS (VMs). PaaS = you manage app (App Service, SQL Database). SaaS = you use software (Microsoft 365). Prefer PaaS for .NET APIs unless you need OS-level control.

### Detailed Answer

| Model | Azure Example | You Manage | Provider Manages |
|-------|---------------|------------|------------------|
| IaaS | Virtual Machines | OS, runtime, app, data | Hardware, network, hypervisor |
| PaaS | App Service, Azure SQL | App, data | OS, runtime, patching, scaling |
| SaaS | Dynamics 365, Salesforce | Configuration | Everything else |

**.NET API decision tree:**
- **App Service** — default for standard web APIs (80% of cases)
- **Container Apps / AKS** — containers, microservices, custom runtime needs
- **VMs** — legacy apps, custom OS config, software not supported on PaaS
- **Azure SQL** — managed database (not SQL on VM unless specific need)

**Trade-off:** PaaS reduces ops burden but less control. IaaS = more control, more patching responsibility.

### Architecture Perspective

"Lift and shift to VM" is valid for migration phase 1; target PaaS for phase 2 optimization. Interviewers want migration thinking, not just definitions.

### Follow-up Questions

1. **Is AKS IaaS or PaaS?**
   - Container orchestration platform — you manage containers/pods; Azure manages control plane (managed K8s).

2. **When SQL on VM vs Azure SQL?**
   - VM: SQL Server features not in Azure SQL, full instance control. Azure SQL: default for new apps, automated patching, built-in HA.

### Common Mistakes in Interviews

- "PaaS is always better" — ignores compliance, legacy, and feature gaps
- Not mentioning operational cost of IaaS

---

## Q007: Azure Resource Manager (ARM) and IaC

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | IaC |
| **Frequency** | Common |
| **Week** | 09, 31 |

### Question

What is ARM, and how do Bicep and Terraform relate to it?

### Short Answer

ARM is Azure's deployment and management layer. Bicep compiles to ARM JSON (Azure-native). Terraform uses Azure provider to call ARM APIs (multi-cloud). Both are IaC — choose Bicep for Azure-only, Terraform for multi-cloud.

### Detailed Answer

**ARM (Azure Resource Manager):**
- Declarative templates (JSON)
- Resource groups as deployment boundary
- RBAC, Policy, tags applied at ARM layer
- Idempotent deployments

**Bicep:**
- DSL that transpiles to ARM
- Cleaner syntax, modules, loops
- First-class Azure support, day-zero new resources

**Terraform:**
- HCL language, Azure RM provider
- State file management, plan/apply workflow
- Multi-cloud (Azure + AWS + GCP)

**Architect choice:**
| Factor | Bicep | Terraform |
|--------|-------|-----------|
| Azure-only shop | ✅ Preferred | OK |
| Multi-cloud | ❌ | ✅ Preferred |
| Team knows HCL | — | ✅ |
| Azure Portal export | ✅ Easy | Manual |

**Best practice:** Modules for repeated patterns (VNet, App Service plan). Store in Git. PR review for infra changes. Separate state per environment.

### Common Mistakes in Interviews

- Manual portal changes in production without IaC
- No mention of drift detection or state management (Terraform)

---

## Q008: Azure SLA and Composite SLA

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Reliability |
| **Frequency** | Occasional |
| **Week** | 09, 16 |

### Question

How do you calculate composite SLA for a multi-service Azure architecture?

### Short Answer

Multiply individual SLAs for serial dependencies. For parallel/redundant paths, combine with (1 - (1-SLA1)(1-SLA2)). Design to meet business SLA, not assume services add up.

### Detailed Answer

**Serial (chain):** SLA_total = SLA1 × SLA2 × SLA3

Example: App Service 99.95% × Azure SQL 99.99% = 99.94% composite

**Parallel (redundant):** SLA_total = 1 - (1-SLA1)(1-SLA2)

Example: Two 99.9% regions active-active ≈ 99.999%

**Implications:**
- Adding services in series **lowers** composite SLA
- Redundancy **raises** availability but increases cost
- If business needs 99.95% and composite is 99.9%, add redundancy or upgrade SKUs

**Architect workflow:**
1. Map dependency chain (user → Front Door → App → SQL → Storage)
2. Look up SLAs per SKU
3. Calculate composite
4. Compare to business requirement
5. Document gap and mitigation in ADR

### Follow-up Questions

1. **SLA vs SLO vs SLI?**
   - SLI = metric (availability %). SLO = internal target. SLA = contractual with credits.

2. **Planned maintenance?**
   - Most Azure PaaS SLAs exclude customer-caused issues; some maintenance is zero-downtime (zone redundancy).

### Common Mistakes in Interviews

- Claiming 100% availability with two 99.9% services in series
- Ignoring dependency chain — only citing best component SLA

---

*Continued in [azure-top-50-qa-part2.md](azure-top-50-qa-part2.md) (Q009–Q030) and [azure-top-50-qa-part3.md](azure-top-50-qa-part3.md) (Q031–Q050)*

## Quick Index

| Q# | Topic |
|----|-------|
| Q001 | WAF pillars |
| Q002 | Subscription strategy |
| Q003 | Zones vs regions |
| Q004 | RBAC vs Policy |
| Q005 | Tagging / FinOps |
| Q006 | IaaS/PaaS/SaaS |
| Q007 | ARM / Bicep / Terraform |
| Q008 | Composite SLA |
