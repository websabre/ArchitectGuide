# Week 09 — Intermediate Q&A

> Q001–Q050: Premium format (Week 1 quality).  
> **Topic:** Azure Fundamentals & WAF | **Count:** 50

---


## Q001: Azure Well-Architected Framework

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Azure WAF |
| **Frequency** | Very Common |

### Question

What are the five WAF pillars and how do you use them in an architecture review?

### Short Answer (30 seconds)

Reliability, Security, Cost Optimization, Operational Excellence, Performance Efficiency. I score each design decision against all five and prioritize gaps by business risk.

### Detailed Answer (3–5 minutes)

The Azure WAF pillars guide trade-off conversations:

1. **Reliability** — HA, DR, autoscale, health probes
2. **Security** — identity, encryption, network isolation, Defender
3. **Cost Optimization** — right-sizing, reservations, tagging, lifecycle policies
4. **Operational Excellence** — IaC, monitoring, runbooks, CI/CD
5. **Performance Efficiency** — caching, CDN, appropriate SKU, async I/O

**Review process:** For each component, ask which pillar it serves and which pillar might be neglected. Payment API: Security + Reliability first; internal admin tool: Cost + Operational Excellence may lead.

Document findings in architecture review template — not just verbal opinions.

### Architecture Perspective

Interviewers want structured reviews, not random service name drops.

### Follow-up Questions

1. **Sixth pillar sustainability? — Azure adds sustainability — consider carbon footprint for large estates.**
2. **WAF vs CAF? — WAF optimizes workloads; CAF guides cloud adoption journey.**

### Common Mistakes in Interviews

- Naming services without pillar mapping
- Security-only reviews ignoring cost
- No prioritized remediation list

---

## Q002: Subscription and Management Group Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Very Common |

### Question

Design Azure subscriptions for 5 product teams with SOC 2 requirements.

### Short Answer (30 seconds)

Management groups: Platform (connectivity, identity) + Application (workloads). Per team: prod and nonprod subscriptions. Separate security/audit subscription. Policy at MG level.

### Detailed Answer (3–5 minutes)

**Hierarchy example:**
```
Root MG
├── Platform MG (sub-connectivity, sub-management)
└── Application MG
    ├── Team A (sub-prod, sub-nonprod)
    └── Team B (sub-prod, sub-nonprod)
```

**SOC 2 drivers:** audit log retention subscription, deny public endpoints via policy, break-glass admin separate from daily ops.

**Architect:** Subscription = blast radius + billing boundary. Not one sub per microservice — operational overhead.

### Architecture Perspective

Subscription design is day-one architect decision — painful to fix later.

### Follow-up Questions

1. **How many subscriptions? — Enough for isolation, not so many nobody can manage.**
2. **Enterprise Agreement vs MCA billing? — Affects invoice structure not technical design.**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation
- Policies only at resource group level

---

## Q003: Azure Policy vs RBAC

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Very Common |

### Question

Difference between Azure Policy and RBAC? Give examples of each.

### Short Answer (30 seconds)

RBAC: who can do what (Authorization). Policy: what is allowed in environment regardless of who (Governance guardrails).

### Detailed Answer (3–5 minutes)

**RBAC:** 'Dev team Contributor on nonprod RG' — they can deploy VMs if policy allows.

**Policy:** 'Deny creation of VMs without tag Environment' — applies even to Owner.

**Combine:** Least privilege RBAC + deny policies for compliance (no public SQL, required tags, allowed regions only).

**Architect:** Policy initiatives bundle related policies — 'SOC2 baseline' assigned to prod MG.

### Architecture Perspective

Confusing Policy and RBAC is common interview failure.

### Follow-up Questions

1. **Policy effect types? — Deny, Audit, DeployIfNotExists, Modify.**
2. **Blueprint vs Bicep stack? — Blueprints legacy; template specs + Bicep for landing zones now.**

### Common Mistakes in Interviews

- Using RBAC alone for compliance
- Policy without exemption process
- Contributor on subscription for developers

---

## Q004: Regions and Availability Zones

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reliability |
| **Frequency** | Very Common |

### Question

When deploy zone-redundant vs single-zone? Cost trade-off?

### Short Answer (30 seconds)

Zone-redundant for 99.99% SLA on critical paths (App Service Premium v3, SQL zone redundant, AKS across AZs). Single-zone for dev and non-critical internal tools.

### Detailed Answer (3–5 minutes)

**Availability Zone:** separate datacenters within region — protects datacenter failure.

**Region pair:** DR geography — async replication for DR (not same as AZ).

**Cost:** Zone-redundant SKUs ~1.5-2x compute; worth it for revenue-critical workloads.

**Architect:** Document SLA math — 99.95% App Service ≈ 22 min/month downtime; zone-redundant improves within region.

### Architecture Perspective

AZ vs region confusion fails senior interviews.

### Follow-up Questions

1. **Region pairs and DR? — Paired region for Microsoft's DR recommendations — not automatic failover.**
2. **Sovereign clouds? — Azure Government/China — separate regions and compliance.**

### Common Mistakes in Interviews

- Single zone for production payment API
- Confusing region with availability zone
- No DR plan because 'Azure is reliable'

---

## Q005: Cloud Adoption Framework (CAF)

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | CAF |
| **Frequency** | Common |

### Question

Summarize CAF methodology stages for enterprise Azure migration.

### Short Answer (30 seconds)

Strategy → Plan → Ready → Adopt → Govern → Manage. Architects lead Ready (landing zone) and Govern; Adopt is iterative migration waves.

### Detailed Answer (3–5 minutes)

**Ready:** Deploy platform landing zone — networking, identity, policy, monitoring.
**Adopt:** Migrate workloads in waves — assess, migrate, optimize.
**Govern:** Policy, cost, security baselines ongoing.

**Architect deliverable:** Migration plan with wave prioritization by risk and business value — not big-bang.

### Architecture Perspective

CAF shows you know enterprise adoption beyond single-app deploy.

### Follow-up Questions

1. **Assess phase tools? — Azure Migrate for discovery and sizing.**
2. **Innovate vs Migrate? — Modernize during migrate vs lift-and-shift — document per workload.**

### Common Mistakes in Interviews

- Skip landing zone — deploy apps directly
- No wave plan — migrate everything at once
- Govern only after everything deployed

---

## Q006: Resource Tagging Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Very Common |

### Question

Mandatory tags for enterprise Azure? How enforce?

### Short Answer (30 seconds)

Environment, CostCenter, Owner, Application (minimum). Enforce via Azure Policy deny deploy without tags. FinOps reports by CostCenter.

### Detailed Answer (3–5 minutes)

**Implementation:**
```json
// Policy: require tag Environment on resource groups
```

**Architect:** Tag at resource group inheritance where possible. Automation runbook fixes drift. Monthly untagged resource report to owners.

Tags drive chargeback, automation (shutdown dev nights), and incident routing.

### Architecture Perspective

Tags are architect-level FinOps foundation.

### Follow-up Questions

1. **Inherited tags from RG? — Prefer RG-level tags applied to resources.**
2. **Case sensitivity? — Tag keys case-sensitive — standardize casing doc.**

### Common Mistakes in Interviews

- Optional tags nobody fills
- No policy enforcement
- Tags only for cost — ignore Owner for incidents

---

## Q007: Azure Landing Zone

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Landing Zone |
| **Frequency** | Very Common |

### Question

Platform landing zone vs application landing zone?

### Short Answer (30 seconds)

Platform LZ: shared connectivity, DNS, firewall, identity, monitoring — central platform team. Application LZ: workload-specific subscriptions inheriting platform policies.

### Detailed Answer (3–5 minutes)

**Platform provides:** Hub VNet, ExpressRoute gateway, Entra ID integration, Log Analytics workspace, Policy assignments.

**Application team gets:** Spoke subscription, deploy App Service/SQL with guardrails.

**Architect:** Start from [Azure landing zone accelerator](https://learn.microsoft.com/azure/cloud-adoption-framework/ready/landing-zone/) — customize don't reinvent.

### Architecture Perspective

Landing zone vocabulary expected in Azure architect interviews.

### Follow-up Questions

1. **Terraform vs Bicep for LZ? — Team skill; Bicep native for Azure-only.**
2. **Brownfield landing zone? — Retrofit policies and networking on existing estate.**

### Common Mistakes in Interviews

- Every team builds own hub VNet
- No shared monitoring workspace
- Landing zone as one-time project never updated

---

## Q008: Azure RBAC Custom Roles

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

When create custom RBAC role vs built-in?

### Short Answer (30 seconds)

Custom when built-in too broad (Contributor) or too narrow. CI/CD deploy role: deploy App Service + read Key Vault secrets — not full Contributor.

### Detailed Answer (3–5 minutes)

**Pattern:** `Deploy-AppService-Prod` custom role at resource group scope for pipeline SP.

**Principle:** Least privilege per workload. Use [custom role definition](https://learn.microsoft.com/azure/role-based-access-control/custom-roles) in Bicep.

**PIM:** Just-in-time elevation for admin roles — reduce standing access.

### Architecture Perspective

Custom roles show production Azure governance experience.

### Follow-up Questions

1. **Role assignment scope? — Narrowest scope possible — RG not subscription.**
2. **Managed identity RBAC? — Grant MI access to Key Vault/SQL — no secrets in pipeline.**

### Common Mistakes in Interviews

- Contributor for CI/CD service principal
- Owner for developers on prod
- No PIM for subscription admins

---

## Q009: Cost Management and Budgets

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

Prevent surprise Azure bill for new product team?

### Short Answer (30 seconds)

Budget alerts at 80%/100%, cost allocation tags, dev environment auto-shutdown, right-size recommendations review monthly, Azure Reservations for stable baseline.

### Detailed Answer (3–5 minutes)

**Architect onboarding checklist:**
- Budget on subscription
- Policy: deny expensive SKUs in nonprod
- Log Analytics daily cap
- Review Advisor cost recommendations

**Unit economics:** Track $/transaction as feature scales.

### Architecture Perspective

FinOps is architect responsibility from day one.

### Follow-up Questions

1. **Cost anomaly detection? — Smart alerts on unusual spend patterns.**
2. **DevTest subscription benefit? — Reduced rates for nonprod — use where eligible.**

### Common Mistakes in Interviews

- No budget alerts
- Production SKUs in dev subscriptions
- Verbose logging to Log Analytics unbounded

---

## Q010: Choose Azure vs On-Premises

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Strategy |
| **Frequency** | Common |

### Question

Stakeholder asks 'why cloud?' — architect response framework?

### Short Answer (30 seconds)

FARCS: Flexibility, Availability, Recovery, Cost (TCO over 3-5 years), Security (shared responsibility). Not 'cloud is always cheaper' — honest TCO with ops labor.

### Detailed Answer (3–5 minutes)

**When Azure wins:** Variable scale, global reach, managed PaaS reduces ops, rapid experimentation.

**When hybrid/on-prem:** Strict latency to factory floor, existing sunk datacenter cost, regulatory constraints.

**Architect:** Hybrid common — Azure Arc for governance across environments.

### Architecture Perspective

Balanced cloud advocacy impresses executives.

### Follow-up Questions

1. **Repatriation trend? — Some workloads move back — architect stays workload-driven.**
2. **Egress cost in TCO? — Model data transfer out — often underestimated.**

### Common Mistakes in Interviews

- Cloud lift without ops model change
- Ignoring egress and support costs in TCO
- 100% cloud mandate without exception process

---

## Q011: Azure Resource Manager

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Very Common |

### Question

What is Azure Resource Manager and why is it central to Azure architecture?

### Short Answer (30 seconds)

ARM is the deployment and management layer for Azure — every resource lives in a resource group, is deployed via ARM templates/Bicep, and is governed through RBAC, Policy, and tags at defined scopes.

### Detailed Answer (3–5 minutes)

Azure Resource Manager (ARM) is the **control plane API** behind every Azure portal click, CLI command, and IaC deployment. It provides:

1. **Consistent resource model** — resources belong to resource groups, subscriptions, and management groups
2. **Declarative deployment** — Bicep/ARM templates define desired state; ARM reconciles
3. **RBAC and Policy enforcement** at scope hierarchy
4. **Idempotent operations** — redeploy same template safely

**Architect workflow:** Design landing zones as ARM/Bicep modules. Never create production resources manually in portal — drift and audit gaps follow.

**Example:** A `Microsoft.Web/sites` resource deploys through ARM with dependencies on App Service Plan and Log Analytics diagnostic settings defined in template.

### Architecture Perspective

ARM literacy separates architects who govern estates from those who click-deploy single apps.

### Follow-up Questions

1. **ARM vs classic Azure Service Manager? — ASM is legacy; all new workloads use ARM.**
2. **Resource provider registration? — Some services require `Microsoft.*` provider registered per subscription before deploy.**

### Common Mistakes in Interviews

- Confusing resource group with subscription boundary
- Manual portal changes without IaC backfill
- Ignoring ARM deployment dependencies and ordering

---

## Q012: Resource Locks

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Very Common |

### Question

When and how do you use Azure resource locks in production?

### Short Answer (30 seconds)

CanNotDelete locks on production resource groups and critical shared resources; ReadOnly for audit-only assets. Locks override RBAC — even Owner cannot delete without removing lock.

### Detailed Answer (3–5 minutes)

**Lock types:**
- **CanNotDelete** — modify allowed, delete blocked — default for prod RGs
- **ReadOnly** — no modifications — compliance archives, golden images

**Architect patterns:**
- Lock hub VNet, firewall, Log Analytics workspace at platform subscription
- Lock production SQL server (not individual DB if team needs schema deploy)
- Document lock removal in change management

**Gotcha:** Locks don't prevent data operations inside resources (SQL DELETE rows still works). Combine with RBAC and Policy.

**Break-glass:** Platform admin role can remove locks — audit Activity Log for lock changes.

### Architecture Perspective

Locks are cheap insurance against accidental deletion during incidents or mis-clicks.

### Follow-up Questions

1. **Lock at MG vs RG scope? — RG-level typical; subscription lock rare and heavy-handed.**
2. **Locks vs Policy deny delete? — Lock is simpler; Policy can enforce org-wide deny delete on tagged prod.**

### Common Mistakes in Interviews

- No locks on shared platform resources
- ReadOnly lock blocking legitimate deployments
- Assuming lock prevents data deletion inside SQL

---

## Q013: Deployment Stacks

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | IaC |
| **Frequency** | Common |

### Question

What are Azure deployment stacks and when use them over standard deployments?

### Short Answer (30 seconds)

Deployment stacks manage a set of resources as a unit with deny-delete/modify actions on managed resources — ideal for platform team baseline deployments that must not be drifted.

### Detailed Answer (3–5 minutes)

**Standard Bicep deploy:** Resources created but users can modify/delete outside template.

**Deployment stack:** ARM tracks managed resources; optional **denyDelete** or **denyModify** actions prevent drift. Deleting stack can delete all managed resources (configurable).

**Use cases:**
- Platform baseline (diagnostic settings, Defender plans)
- Shared monitoring agents
- Landing zone components owned by central team

**Architect:** Stacks complement Policy — stacks protect specific deployments; Policy governs entire subscription. Not replacement for full IaC pipeline.

### Architecture Perspective

Stacks solve 'someone deleted our monitoring config' drift problem.

### Follow-up Questions

1. **Stack vs Blueprint? — Blueprints deprecated; stacks + template specs + ALZ are current pattern.**
2. **Stack delete behavior? — Configure deleteResources: detach vs delete — critical for prod.**

### Common Mistakes in Interviews

- Using stacks for every app deploy — overkill
- denyModify blocking app team legitimate changes
- No stack versioning in pipeline

---

## Q014: Activity Log vs Diagnostic Logs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Observability |
| **Frequency** | Very Common |

### Question

Difference between Azure Activity Log and Diagnostic logs?

### Short Answer (30 seconds)

Activity Log = control plane operations (who created VM, changed NSG). Diagnostic logs = data plane telemetry from resources (App Service HTTP logs, SQL audit).

### Detailed Answer (3–5 minutes)

**Activity Log (Subscription level):**
- Administrative operations: create, update, delete resources
- Service health notifications
- Retention ~90 days default — export to Log Analytics for longer

**Diagnostic Settings (Resource level):**
- Resource-specific metrics and logs
- App Service: AppServiceHTTPLogs, ConsoleLogs
- SQL: SQLSecurityAuditEvents
- Sent to Log Analytics, Storage, or Event Hub

**Architect:** SOC 2 requires both — Activity Log for change audit; Diagnostic for workload forensics. Centralize in shared Log Analytics with RBAC separation.

### Architecture Perspective

Confusing the two is a common observability interview failure.

### Follow-up Questions

1. **Azure Monitor Activity Log vs Entra sign-in logs? — Entra logs are identity plane — separate diagnostic setting on Entra.**
2. **Retention strategy? — Activity Log 90 days insufficient — export day one.**

### Common Mistakes in Interviews

- Only Activity Log, no resource diagnostics
- Diagnostic logs without Log Analytics centralization
- No alert on Activity Log delete operations

---

## Q015: Azure Advisor

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Very Common |

### Question

How do architects use Azure Advisor at enterprise scale?

### Short Answer (30 seconds)

Advisor aggregates recommendations across cost, security, reliability, performance, and operational excellence — review weekly at platform level, monthly with app owners for remediation prioritization.

### Detailed Answer (3–5 minutes)

**Recommendation categories map to WAF pillars.**

**Enterprise workflow:**
1. Export Advisor score to Power BI / Azure Workbooks
2. Assign recommendations to owners via tagging
3. Policy can auto-remediate some (e.g., enable MFA)
4. Track suppression with documented justification

**Architect:** Don't treat Advisor as optional — it's free continuous review. Integrate high-severity security recs into architecture review gate.

### Architecture Perspective

Advisor demonstrates operational maturity beyond initial design.

### Follow-up Questions

1. **Advisor vs Defender for Cloud recommendations? — Overlap on security; Defender deeper CSPM; dedupe in reporting.**
2. **Suppress vs fix? — Suppress with expiry and reason — not permanent ignore.**

### Common Mistakes in Interviews

- Never reviewing Advisor recommendations
- Fixing cost recs before security recs without prioritization
- No ownership assignment for recommendations

---

## Q016: Service Health vs Resource Health

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reliability |
| **Frequency** | Common |

### Question

Explain Azure Service Health vs Resource Health for incident response.

### Short Answer (30 seconds)

Service Health = Azure platform events affecting regions/services (outages, maintenance). Resource Health = health of YOUR specific resource instance and remediation steps.

### Detailed Answer (3–5 minutes)

**Service Health:**
- Azure-wide or region-specific incidents
- Planned maintenance notifications
- Health history and root cause summaries
- Configure Action Groups for alerts

**Resource Health:**
- Per-resource availability status
- 'Unavailable — platform issue' vs 'user configuration issue'
- Suggested remediation (restart, redeploy)

**Architect runbook:** On alert, check Service Health first — if platform incident, don't fail over unnecessarily. Resource Health for single-resource degradation.

### Architecture Perspective

Distinguishing platform vs workload issues speeds incident triage.

### Follow-up Questions

1. **Service Health API for automation? — Yes — integrate with status page and ITSM.**
2. **Resource Health for App Service? — Shows if instance unhealthy — triggers autoscale/restart.**

### Common Mistakes in Interviews

- Debugging app code when Service Health shows region outage
- No Service Health alert subscriptions
- Ignoring planned maintenance windows

---

## Q017: Azure Monitor Metrics vs Logs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Observability |
| **Frequency** | Very Common |

### Question

When use Azure Monitor metrics vs logs for alerting and dashboards?

### Short Answer (30 seconds)

Metrics: numeric time-series, low latency, cheap — CPU, request count, queue depth. Logs: rich text/structured events — queries, joins, forensics. Alert on metrics for SLOs; investigate with logs.

### Detailed Answer (3–5 minutes)

**Metrics:**
- Pre-aggregated, 90-day retention (extendable)
- Near real-time alerting
- Metric alerts, autoscale triggers

**Logs (Log Analytics):**
- KQL queries across tables
- Cross-resource correlation
- Long retention for compliance

**Architect pattern:** Metric alert fires → runbook queries logs for root cause. Example: CPU metric alert → AppTraces KQL for slow dependency.

**Cost:** Log ingestion expensive at volume — sample verbose logs; use metrics for high-cardinality counters.

### Architecture Perspective

Metrics vs logs trade-off is foundational observability design.

### Follow-up Questions

1. **Platform metrics vs guest OS metrics? — Enable Diagnostic Settings for guest metrics on VMs.**
2. **Logs to metrics? — Log-based metrics for custom KPIs from KQL.**

### Common Mistakes in Interviews

- Alerting only on log queries for high-frequency signals
- No metric baseline before setting thresholds
- Ingesting all verbose logs unfiltered

---

## Q018: Log Analytics Workspace Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Observability |
| **Frequency** | Very Common |

### Question

Design Log Analytics workspace strategy for 20 subscriptions.

### Short Answer (30 seconds)

Central workspace per environment (prod/nonprod) in platform subscription; regional workspaces only if data residency requires; use Azure Monitor Agent; RBAC at workspace level.

### Detailed Answer (3–5 minutes)

**Patterns:**
1. **Single prod workspace** — simplest queries, cross-subscription dashboards
2. **Workspace per region** — data residency (EU vs US)
3. **Dedicated security workspace** — SOC access only

**Architect decisions:**
- Daily cap and alert on ingestion spike
- Retention: 90 default, 365+ for compliance tables
- Data collection rules (DCR) for AMA filtering

**Anti-pattern:** Workspace per app — query fragmentation and cost duplication.

### Architecture Perspective

Workspace topology affects query, cost, and compliance for years.

### Follow-up Questions

1. **Commitment tier pricing? — Reserve ingestion capacity for predictable volume.**
2. **Cross-workspace queries? — `union` in KQL or Azure Monitor multi-workspace.**

### Common Mistakes in Interviews

- One workspace per microservice
- No ingestion cap on nonprod
- Classic Log Analytics agents on new deployments

---

## Q019: Naming Conventions

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Very Common |

### Question

Define Azure naming convention for resources across landing zone.

### Short Answer (30 seconds)

Pattern: `{resource-type}-{workload}-{environment}-{region}-{instance}` e.g. `app-orders-prod-eus-01`. Document in CAF naming guide; enforce via Policy where possible.

### Detailed Answer (3–5 minutes)

**Components:**
- **Resource type abbreviation** — `vnet`, `kv`, `asp`, `sql` (from CAF abbreviations)
- **Workload/application** — business identifier
- **Environment** — prod, stg, dev, sbx
- **Region** — eus, weu (short code)
- **Instance** — 01, 02 for scale-out

**Architect:** Naming enables automation, cost allocation, and on-call routing. Global uniqueness required for some types (Storage, Key Vault).

**Policy:** Audit naming with regex; deny for critical types (Key Vault, Storage).

### Architecture Perspective

Naming conventions are day-one decisions — renaming Key Vault is painful.

### Follow-up Questions

1. **Azure naming tool? — Microsoft CAF naming convention reference.**
2. **Tags vs naming? — Naming for uniqueness and automation; tags for metadata.**

### Common Mistakes in Interviews

- Random portal-generated names in production
- No documented standard across teams
- Names exceeding length limits for Storage accounts

---

## Q020: Capacity Reservations

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

When use Azure capacity reservations vs savings plans vs reserved instances?

### Short Answer (30 seconds)

Capacity reservations guarantee compute capacity in a region/AZ without payment discount — use when SLA requires capacity during shortages. RIs/Savings Plans for cost discount on usage.

### Detailed Answer (3–5 minutes)

**Capacity Reservation:**
- Reserve VM or AKS node capacity in advance
- No cost discount — pay for reserved capacity whether used or not
- Combine with RI for discount + capacity guarantee

**Use when:** Large VM SKUs scarce in region, critical workloads during peak provisioning, AKS node pool scale events.

**Architect:** Capacity reservation is reliability play; Savings Plan/RI is FinOps play. Document in DR plan if reserved capacity is region-specific.

### Architecture Perspective

Capacity reservation vs reservation discount confuses many candidates.

### Follow-up Questions

1. **On-demand capacity reservation? — Azure Capacity Reservation for VMs — check current SKU support.**
2. **Zonal vs regional reservation? — Zonal ties to specific AZ for HA clusters.**

### Common Mistakes in Interviews

- Buying capacity reservation expecting cost savings
- No monitoring of unused reserved capacity
- Capacity reservation in wrong region for DR failover

---

## Q021: Azure Compliance Offerings

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compliance |
| **Frequency** | Very Common |

### Question

Map Azure compliance offerings to SOC 2 and ISO 27001 customer requirements.

### Short Answer (30 seconds)

Azure maintains certifications (SOC 1/2/3, ISO 27001, PCI DSS) at platform level — customers inherit for IaaS/PaaS controls; must implement workload controls (access, encryption, logging) for shared responsibility.

### Detailed Answer (3–5 minutes)

**Inherited from Microsoft:** Physical datacenter security, hypervisor, platform patching for PaaS.

**Customer responsibility:** Data classification, RBAC, network rules, application security, backup testing.

**Tools:**
- **Microsoft Purview Compliance Manager** — track control implementation
- **Azure Policy** regulatory compliance dashboard
- **Defender for Cloud** regulatory standards

**Architect deliverable:** Compliance matrix mapping each control to Azure service + evidence source (Policy compliance, Activity Log, Defender score).

### Architecture Perspective

Compliance interviews require shared responsibility clarity — not 'Azure is certified so we are.'

### Follow-up Questions

1. **SOC 2 Type I vs II? — Type II over period — customer audit often requires Type II evidence.**
2. **Azure Government for FedRAMP? — Separate cloud for US government workloads.**

### Common Mistakes in Interviews

- Claiming Azure cert covers application code vulnerabilities
- No customer control evidence collection
- Compliance as one-time checkbox not continuous Policy monitoring

---

## Q022: Data Residency

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compliance |
| **Frequency** | Very Common |

### Question

Design Azure architecture for EU data residency requirements.

### Short Answer (30 seconds)

Deploy workloads in EU regions only; Policy deny non-EU regions; use EU Data Boundary where applicable; Private Link keeps traffic in-region; document subprocessors and replication paths.

### Detailed Answer (3–5 minutes)

**Controls:**
1. **Allowed locations Policy** — deny deploy outside `westeurope`, `northeurope`
2. **Geo-redundant storage** — GRS replicates to paired region (still EU pair)
3. **SQL geo-replication** — verify secondary region acceptable
4. **Log Analytics** — workspace in EU;  
5. **Microsoft 365 / Entra** — EU Data Boundary for tenant data

**Architect:** Data residency ≠ data sovereignty. Sovereign clouds (e.g., Azure Government) for stricter requirements.

**Contract review:** AI services may process data in other regions — disclose Copilot/OpenAI routing.

### Architecture Perspective

Data residency is legal + technical — architects document data flows.

### Follow-up Questions

1. **Multi-region CDN impact? — Static assets may cache globally — use CDN rules or avoid for strict residency.**
2. **Backup vault region? — Backup data stays in chosen region — verify cross-region backup settings.**

### Common Mistakes in Interviews

- Using US-only regions for EU customer data
- GRS without legal review of paired region
- No Policy enforcement on region selection

---

## Q023: Shared Responsibility Model

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Explain shared responsibility model for Azure App Service vs IaaS VM.

### Short Answer (30 seconds)

App Service: Microsoft manages OS, runtime patching, physical security; customer manages app code, auth, connection strings, network integration config. IaaS VM: customer manages OS patching, antivirus, app — more control, more burden.

### Detailed Answer (3–5 minutes)

**Responsibility spectrum:**
```
SaaS ──► PaaS ──► IaaS ──► On-prem
(Microsoft owns more)     (Customer owns more)
```

**App Service customer owns:**
- Application vulnerabilities (SQL injection, auth bugs)
- Managed identity and Key Vault integration
- VNet integration and private endpoints
- Deployment pipeline security

**VM customer additionally owns:**
- OS patching, firewall on VM, disk encryption config

**Architect:** Choose PaaS to shift ops burden; document residual responsibilities in security architecture.

### Architecture Perspective

Shared responsibility is table stakes for cloud architect credibility.

### Follow-up Questions

1. **PaaS means no security work? — Common fatal interview mistake.**
2. **Container Apps shared model? — Similar PaaS — customer secures container image and config.**

### Common Mistakes in Interviews

- Assuming Microsoft patches application code
- IaaS without patch management process
- No distinction between models in security docs

---

## Q024: SLA Aggregation Math

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reliability |
| **Frequency** | Common |

### Question

Calculate composite SLA for API depending on App Service and SQL Database.

### Short Answer (30 seconds)

Composite SLA = product of component SLAs. App Service 99.95% × SQL 99.99% ≈ 99.94%. Add Front Door, Redis, etc. — chain weakest links.

### Detailed Answer (3–5 minutes)

**Formula:** `SLA_composite = SLA1 × SLA2 × ... × SLAn`

**Example:**
- App Service Standard: 99.95% (21.9 min/month max downtime)
- Azure SQL: 99.99% (4.3 min/month)
- Combined: 0.9995 × 0.9999 = 0.9994 → **99.94%**

**Architect:** Multi-region active-active improves beyond single-region SLA math. Document SLA budget per dependency — third-party SaaS often 99.9% drags composite down.

**N+1:** SLA math is theoretical — design for failure with retries, circuit breakers, caching.

### Architecture Perspective

SLA multiplication surprises stakeholders — architects quantify uptime honestly.

### Follow-up Questions

1. **SLA credits vs architecture? — Credits don't replace revenue loss — design for HA.**
2. **Zone redundancy SLA impact? — Zone-redundant SKUs often higher SLA — use published figures.**

### Common Mistakes in Interviews

- Adding SLAs instead of multiplying
- Ignoring dependencies in SLA calculation
- Promising 99.99% on single-region single-instance design

---

## Q025: Platform vs Workload RACI

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

Define RACI between platform team and application team in landing zone model.

### Short Answer (30 seconds)

Platform **Accountable** for hub network, firewall, identity baseline, Policy, central monitoring. Application team **Accountable** for app architecture, data, deployments within guardrails. Both **Consulted** on security exceptions.

### Detailed Answer (3–5 minutes)

**RACI example:**
| Activity | Platform | App Team |
|----------|----------|----------|
| Hub VNet / Firewall | A/R | C |
| Spoke subscription | R | A |
| App Service deploy | C | A/R |
| Azure Policy baseline | A/R | I |
| Incident P1 platform | A/R | C |
| App bug fix | I | A/R |

**Architect:** Publish RACI in Cloud Center of Excellence docs — reduces turf wars during incidents.

### Architecture Perspective

RACI clarity prevents 'not my job' during outages.

### Follow-up Questions

1. **RACI vs operating model? — RACI is who; operating model is how (ticket queues, SLAs).**
2. **Third-party MSP in RACI? — Define R for managed services explicitly.**

### Common Mistakes in Interviews

- Platform team deploying application code
- App team opening NSG rules on hub firewall without process
- No documented RACI — verbal agreements only

---

## Q026: Cloud Center of Excellence

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

What is a Cloud Center of Excellence (CCoE) and what should it deliver?

### Short Answer (30 seconds)

CCoE is a cross-functional team (architecture, security, FinOps, ops) establishing standards, guardrails, training, and self-service enablement — not a bottleneck approval committee.

### Detailed Answer (3–5 minutes)

**Deliverables:**
- Landing zone and IaC templates
- Approved service catalog and architecture patterns
- FinOps reporting and tagging standards
- Office hours and migration playbooks
- Architecture review board with SLAs

**Architect role:** Often leads or sits in CCoE — balances innovation vs risk.

**Anti-pattern:** CCoE as gatekeeper with 6-week ticket queues — drives shadow IT.

### Architecture Perspective

CCoE shows enterprise cloud maturity beyond individual projects.

### Follow-up Questions

1. **CCoE vs platform engineering? — Overlap; platform eng builds; CCoE governs and enables.**
2. **Measure CCoE success? — Time-to-production, policy compliance %, cloud spend variance.**

### Common Mistakes in Interviews

- CCoE blocks all deploys centrally
- No self-service templates — every request custom
- CCoE without business stakeholder representation

---

## Q027: Sandbox Subscriptions

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

Design sandbox subscription strategy for developer experimentation.

### Short Answer (30 seconds)

Dedicated sandbox MG with Policy (allowed SKUs, deny prod regions, cost caps), auto-expiring resources, no production data, separate from prod billing — developers Contributor on their sandbox sub only.

### Detailed Answer (3–5 minutes)

**Controls:**
- Budget alert at $100/month per sandbox
- Policy: deny creation of ExpressRoute, expensive GPU VMs
- Mandatory `Environment=sandbox` tag
- Monthly cleanup automation (delete untagged resources)

**Architect:** Sandboxes accelerate learning without risking prod Policy inheritance mistakes. Separate Entra group `Azure-Sandbox-Users`.

### Architecture Perspective

Sandbox strategy prevents 'experiment in prod subscription' anti-pattern.

### Follow-up Questions

1. **Sandbox vs dev subscription? — Dev is for integrated team workloads; sandbox is individual throwaway.**
2. **Azure Lab Services vs sandbox sub? — Lab Services for training classes; sandbox for architect/engineer R&D.**

### Common Mistakes in Interviews

- Developers Contributor on production subscription
- Sandbox without budget alerts
- Production secrets copied to sandbox

---

## Q028: DevTest Pricing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

How does Azure DevTest subscription pricing benefit architecture planning?

### Short Answer (30 seconds)

Visual Studio/DevTest subscriptions offer reduced rates on Windows VMs and select services for non-production — architect routes dev/test workloads to eligible subscriptions saving 15-40% on compute.

### Detailed Answer (3–5 minutes)

**Eligible:** Development and test workloads only — not production. Windows client VMs for testing, reduced compute rates.

**Architect planning:**
- Map environments: prod (full price), staging (DevTest if no SLA need), dev (DevTest)
- Combine with auto-shutdown schedules
- Policy deny prod tags in DevTest subscriptions

**Compliance:** Microsoft audits misuse — production traffic on DevTest violates terms.

### Architecture Perspective

FinOps-aware architects route nonprod to DevTest automatically.

### Follow-up Questions

1. **DevTest vs CSP dev/test offer? — Different programs — verify eligibility with EA/MCA.**
2. **Hybrid Benefit in DevTest? — Can stack with AHUB for Windows Server licensing savings.**

### Common Mistakes in Interviews

- Production APIs on DevTest subscription
- No separation between DevTest and prod subscriptions
- Assuming all Azure services discounted in DevTest

---

## Q029: Azure Lighthouse

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

Explain Azure Lighthouse for MSP and enterprise central management.

### Short Answer (30 seconds)

Lighthouse enables cross-tenant management — MSP or central IT manages customer/child tenant subscriptions with delegated RBAC without guest accounts, maintaining audit trail in managing tenant.

### Detailed Answer (3–5 minutes)

**Use cases:**
- MSP monitoring and patching customer estates
- Enterprise managing acquired company tenants
- Central SOC viewing Defender alerts across tenants

**Architect:** Define least-privilege delegated roles (e.g., Reader + specific Defender roles). Customer retains Owner; can remove delegation anytime.

**vs Guest users:** Lighthouse scales better — no B2B guest sprawl, unified automation from managing tenant.

### Architecture Perspective

Lighthouse is standard for multi-tenant Azure management architecture.

### Follow-up Questions

1. **Lighthouse vs Azure Arc? — Lighthouse for Azure tenant delegation; Arc for hybrid/on-prem resources.**
2. **Policy via Lighthouse? — Deploy policies from managing tenant to delegated subscriptions.**

### Common Mistakes in Interviews

- Guest Owner accounts in every customer tenant
- Over-privileged MSP Contributor delegation
- No customer audit of delegated actions

---

## Q030: Enterprise Agreement Hierarchy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

Describe Enterprise Agreement (EA) billing hierarchy impact on subscription design.

### Short Answer (30 seconds)

EA: Enrollment → Departments → Accounts → Subscriptions. Billing rolls up to enrollment; architects align subscription boundaries with department chargeback and quota allocation.

### Detailed Answer (3–5 minutes)

**Hierarchy:**
```
Enrollment (company)
└── Department (cost center / division)
    └── Account (owner / invoice section)
        └── Subscription (technical boundary)
```

**Architect considerations:**
- Subscription quota and ARM limits per subscription
- Chargeback reports map Department → tags/CostCenter
- MCA migration changing hierarchy — plan transition

**Not technical but drives:** How many subscriptions, who approves new subs, budget ownership.

### Architecture Perspective

Billing hierarchy influences subscription vending and FinOps reporting.

### Follow-up Questions

1. **EA vs MCA? — Modern Commerce Agreement replacing EA — similar concepts, different portal.**
2. **Enterprise dev/test offer? — Separate enrollment pricing for nonprod.**

### Common Mistakes in Interviews

- One subscription for entire enterprise
- Ignoring department chargeback in subscription layout
- No quota planning per enrollment

---

## Q031: Management Group Inheritance

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Very Common |

### Question

How do Policy and RBAC inherit through management group hierarchy?

### Short Answer (30 seconds)

Assignments at parent MG flow to all child MGs and subscriptions — explicit deny at child doesn't override parent allow unless using exemption. Design hierarchy top-down: root policies for baseline, child overrides sparingly.

### Detailed Answer (3–5 minutes)

**Inheritance rules:**
- Policy assignment at `Application-Prod` MG applies to all prod subscriptions beneath
- RBAC at MG grants access to all contained subscriptions
- **Deny assignments** block even Owner — separate from Policy

**Architect pattern:**
```
Root: Require tags, allowed locations
├── Platform MG: network policies
└── Application MG
    ├── Prod: deny public IP, require encryption
    └── NonProd: relaxed SKUs
```

Document exceptions with Policy exemption TTL and approval workflow.

### Architecture Perspective

MG inheritance is core landing zone governance — wrong hierarchy is expensive to fix.

### Follow-up Questions

1. **MG depth limits? — Up to 6 levels — keep shallow for clarity.**
2. **Subscription move between MGs? — Policies re-evaluate — test before move.**

### Common Mistakes in Interviews

- Policies assigned only at subscription level at scale
- Conflicting policies at sibling MGs without documentation
- No exemption workflow — permanent Policy overrides

---

## Q032: Deny Assignments

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

What are Azure deny assignments and when use them?

### Short Answer (30 seconds)

Deny assignments block actions even for Owner — used by Azure Blueprints (legacy), managed apps, and platform teams to protect critical resources from any deletion or modification.

### Detailed Answer (3–5 minutes)

**Unlike Policy Deny:** Deny assignment is RBAC-layer block — applies regardless of role including Owner (except break-glass with specific exclusion).

**Use cases:**
- Protect management group structure
- Managed application resources
- Recovery Services vault immutability scenarios

**Architect:** Rare for app teams to create — platform team applies to hub resources. Combine with CanNotDelete locks for defense in depth.

**Audit:** Activity Log shows denied operations with deny assignment ID.

### Architecture Perspective

Deny assignments are strongest Azure control short of subscription lock.

### Follow-up Questions

1. **Deny assignment vs Policy deny? — Deny assignment overrides RBAC; Policy evaluates at deploy/config time.**
2. **Who can create deny assignments? — Only specific roles like User Access Administrator with constraints.**

### Common Mistakes in Interviews

- Relying on Owner discipline alone for critical resources
- Deny assignment blocking legitimate emergency changes without process
- No break-glass exclusion documented

---

## Q033: Resource Graph

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Very Common |

### Question

Use Azure Resource Graph for governance at scale — example queries?

### Short Answer (30 seconds)

Resource Graph indexes ARM resources cross-subscription — query with KQL-like language for inventory, compliance drift, untagged resources, public endpoints.

### Detailed Answer (3–5 minutes)

**Example queries:**
```kusto
Resources
| where type == 'microsoft.web/sites'
| where properties.publicNetworkAccess == 'Enabled'

Resources
| where tags['Environment'] == '' or isnull(tags['Environment'])
```

**Architect use cases:**
- Weekly compliance report (public storage accounts)
- Pre-migration inventory
- Cost anomaly investigation (count VMs by SKU)

Integrate with Azure Automation, Logic Apps, or GitHub Actions for scheduled governance scans.

### Architecture Perspective

Resource Graph is architect's SQL for entire Azure estate.

### Follow-up Questions

1. **Resource Graph vs Log Analytics? — Resource Graph = current state inventory; Log Analytics = time-series events.**
2. **ARG API pagination? — Use `skipToken` for large estates in automation.**

### Common Mistakes in Interviews

- Manual portal inventory per subscription
- No scheduled compliance queries
- Ignoring ARG for pre-Policy audit baseline

---

## Q034: KQL for Governance

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Observability |
| **Frequency** | Common |

### Question

Write KQL patterns for governance monitoring in Log Analytics.

### Short Answer (30 seconds)

Query Activity Log tables for unauthorized changes, Policy non-compliance, sign-in anomalies — centralize governance signals in workbooks.

### Detailed Answer (3–5 minutes)

**Patterns:**
```kusto
AzureActivity
| where OperationNameValue has 'delete'
| where ActivityStatusValue == 'Success'
| summarize count() by Caller, ResourceGroup

PolicyState
| where ComplianceState == 'NonCompliant'
| summarize by PolicyAssignmentName
```

**Architect:** Build governance workbook: failed deployments, Policy drift, RBAC changes, Key Vault access anomalies. Alert on `Add Member to Owner` role assignments.

### Architecture Perspective

KQL connects audit logs to actionable governance alerts.

### Follow-up Questions

1. **KQL vs Resource Graph query language? — Different syntax and data sources — both needed.**
2. **Retention for AzureActivity table? — Match compliance — archive to Storage if >2 years.**

### Common Mistakes in Interviews

- No alerts on privileged role assignments
- Governance queries never scheduled
- Copy-paste KQL without understanding table schema

---

## Q035: Microsoft Purview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Data Governance |
| **Frequency** | Common |

### Question

Role of Microsoft Purview in Azure data architecture?

### Short Answer (30 seconds)

Purview provides data catalog, lineage, classification, and compliance mapping across Azure, on-prem, and multi-cloud — architects use it for sensitive data discovery and policy enforcement integration.

### Detailed Answer (3–5 minutes)

**Capabilities:**
- Automated scanning (SQL, Storage, Synapse, Power BI)
- Classification labels (PII, financial)
- Data lineage for impact analysis
- Compliance Manager integration

**Architect workflow:** Register data sources → scan → apply sensitivity labels → integrate with Defender for Cloud and DLP policies.

**Not a database** — metadata layer; plan scan schedules to avoid production load impact.

### Architecture Perspective

Purview answers 'where is our customer PII across Azure?'

### Follow-up Questions

1. **Purview vs Azure Policy? — Purview data governance; Policy infrastructure compliance.**
2. **Purview governance vs catalog? — Unified platform — catalog is consumer-facing discovery.**

### Common Mistakes in Interviews

- No data classification in regulated workloads
- Scanning prod without performance window
- Purview deployed without owner stewardship model

---

## Q036: Carbon Optimization

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Sustainability |
| **Frequency** | Common |

### Question

How do architects incorporate carbon optimization in Azure design?

### Short Answer (30 seconds)

Use Carbon Optimization in Emissions Impact Dashboard, prefer region with lower carbon intensity when latency allows, right-size compute, serverless/scale-to-zero, schedule dev shutdown, and track emissions KPI alongside cost.

### Detailed Answer (3–5 minutes)

**Tactics:**
- **Region selection** — Nordic regions often lower carbon grid
- **Right-sizing** — Advisor + idle resource elimination
- **PaaS over IaaS** — shared infrastructure efficiency
- **Reserved capacity** — higher utilization of physical hardware

**Architect:** Sustainability pillar in WAF reviews — document trade-offs when lowest-carbon region conflicts with latency SLA.

**Reporting:** Export Azure emissions data for ESG reporting.

### Architecture Perspective

Carbon awareness is increasingly asked in enterprise architect interviews.

### Follow-up Questions

1. **Carbon proxy metric? — vCore-hours and storage GB-months correlate with emissions.**
2. **Azure sustainability calculator? — Estimate before migrate.**

### Common Mistakes in Interviews

- Ignoring region carbon when latency SLA allows flexibility
- Oversized always-on dev environments
- Sustainability never mentioned in architecture review

---

## Q037: Architecture Review Cadence

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

Establish architecture review cadence for growing Azure estate.

### Short Answer (30 seconds)

Tiered reviews: lightweight ADR for team decisions; formal review board for new services, cross-subscription changes, and security exceptions; quarterly estate health review.

### Detailed Answer (3–5 minutes)

**Cadence:**
| Trigger | Review type | SLA |
|---------|-------------|-----|
| New Azure service adoption | Full board | 2 weeks |
| Standard pattern deploy | Self-service + ADR | Async |
| Policy exception | Security + architect | 1 week |
| Quarterly | Estate WAF assessment | Scheduled |

**Architect:** Publish decision log — searchable ADRs prevent re-litigating same choices.

**Inputs:** Threat model, cost estimate, SLA impact, operational runbook draft.

### Architecture Perspective

Review cadence balances agility with governance at scale.

### Follow-up Questions

1. **ADR format? — Context, decision, consequences, status — store in repo.**
2. **Review board size? — 5-7 voting members — avoid too large for decisions.**

### Common Mistakes in Interviews

- No review for new Azure service adoption
- Reviews as rubber stamp without threat modeling
- Decisions verbal only — no ADR trail

---

## Q038: Azure Migrate

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Migration |
| **Frequency** | Very Common |

### Question

Azure Migrate assessment workflow for datacenter to Azure migration?

### Short Answer (30 seconds)

Discover on-prem with appliance → assess readiness/ sizing/ cost/ dependencies → migrate in waves via server replication or modernize to PaaS.

### Detailed Answer (3–5 minutes)

**Phases:**
1. **Discover** — Azure Migrate appliance, agentless VMware/Hyper-V
2. **Assess** — Azure readiness, right-size SKU, monthly cost estimate, dependency mapping
3. **Migrate** — Agent-based replication for lift-shift; refactor path documented separately

**Architect:** Use dependency data for wave planning — migrate leaf apps before core databases.

**Modernize decision:** IIS app → assess for App Service compatibility before defaulting to VM.

### Architecture Perspective

Azure Migrate is standard enterprise migration entry point.

### Follow-up Questions

1. **Migrate vs Modernize? — 6R framework: Rehost, Refactor, Rearchitect, etc.**
2. **Database Migration Service? — Pair with Migrate for SQL/PostgreSQL cutover.**

### Common Mistakes in Interviews

- Lift-shift all VMs without assessment
- Ignore dependency map — migrate database before consumers
- No post-migrate right-sizing review

---

## Q039: Backup Vault Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reliability |
| **Frequency** | Common |

### Question

Design Azure Backup vault strategy across subscriptions and regions.

### Short Answer (30 seconds)

Central backup vault per environment/region in platform subscription; Backup Policies by workload type; immutability for ransomware protection; cross-region restore for DR.

### Detailed Answer (3–5 minutes)

**Design:**
- **Recovery Services vault** per region (backup data locality)
- **Soft delete + immutability** enabled on vault
- **Backup policies:** Daily app-consistent SQL; weekly VM; retention 30/90/365 tiers
- **RBAC:** Backup Operator for ops; no delete permission for app teams

**Architect:** Backup ≠ DR — define RPO/RTO per tier. Test restore quarterly — untested backup is wishful thinking.

### Architecture Perspective

Backup vault architecture protects against ransomware and operator error.

### Follow-up Questions

1. **Backup vault vs Backup center? — Backup center is management UI across vaults.**
2. **Azure Backup for AKS? — Backup via Azure Backup for AKS or Velero — evaluate workload.**

### Common Mistakes in Interviews

- App teams can delete backup vault
- No immutability on prod vault
- Backup never restored in testing

---

## Q040: Defender for Cloud Tiers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Compare Defender for Cloud plans and architect enrollment strategy.

### Short Answer (30 seconds)

Foundational (free): secure score, basic recommendations. CSPM: posture management. Workload protection plans (Servers, App Service, SQL, Storage, etc.) add threat detection — enable per workload class in prod.

### Detailed Answer (3–5 minutes)

**Plans:**
- **CSPM** — misconfiguration detection, regulatory compliance
- **Defender for Servers** — EDR integration, vulnerability management
- **Defender for App Service** — threat detection on PaaS
- **Defender for SQL** — anomaly detection

**Architect:** Enable CSPM org-wide via Policy. Add workload plans based on data classification — not one-size-all or none.

**Cost:** Per-resource pricing — budget Defender like any production service.

### Architecture Perspective

Defender tier selection maps to workload criticality and compliance.

### Follow-up Questions

1. **Defender vs Sentinel? — Defender detects; Sentinel SIEM aggregates — often paired.**
2. **Auto-provisioning agents? — Policy deploy AMA + Defender agents consistently.**

### Common Mistakes in Interviews

- Defender disabled to save cost on prod PII systems
- All plans enabled everywhere — FinOps waste
- Secure score treated as compliance certification

---

## Q041: Entra ID Tenant Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Very Common |

### Question

Design Entra ID tenant strategy for multi-brand enterprise.

### Short Answer (30 seconds)

Single tenant with B2B guests for partners OR separate tenants per brand with Entra ID B2B sync — single tenant simplifies licensing; multi-tenant for strict isolation (M&A, regulatory).

### Detailed Answer (3–5 minutes)

**Single tenant pattern:**
- Conditional Access policies by app sensitivity
- Dynamic groups for brand/department
- Separate app registrations per brand

**Multi-tenant pattern:**
- Post-M&A hold separate tenants until integration
- Azure Lighthouse or B2B for cross-tenant access

**Architect:** Tenant boundary is hard to merge — decide early. DNS custom domains (`brand1.com`, `brand2.com`) map to one tenant cleanly.

### Architecture Perspective

Tenant design is identity architecture foundation — expensive to reverse.

### Follow-up Questions

1. **B2B vs B2C? — B2B for partner employees; External ID (CIAM) for customer identities.**
2. **Hybrid identity? — Entra Connect sync on-prem AD — plan UPN suffixes.**

### Common Mistakes in Interviews

- New tenant per small project
- No Conditional Access on admin roles
- Guest users with excessive privileges

---

## Q042: Azure Firewall vs NSG

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

When Azure Firewall vs NSG for traffic control?

### Short Answer (30 seconds)

NSG: L3/L4 stateful filter on subnet/NIC — micro-segmentation. Azure Firewall: centralized L3-L7 inspection, FQDN filtering, threat intel, IDPS — hub network security.

### Detailed Answer (3–5 minutes)

**NSG use:**
- Allow SQL 1433 from App Service subnet only
- Deny inbound RDP from internet on subnet

**Azure Firewall use:**
- Egress FQDN filtering (allow `*.microsoft.com` only)
- Centralized logging and forced tunneling
- Application rules for outbound HTTP/S

**Architect:** Hub-spoke — Firewall in hub, NSGs in spokes for defense in depth. Don't duplicate same rules in both without documentation.

### Architecture Perspective

Firewall vs NSG layering is classic Azure network interview question.

### Follow-up Questions

1. **Firewall Premium vs Standard? — Premium adds IDPS and TLS inspection — compliance driver.**
2. **NSG vs Application Security Group? — ASGs simplify NSG rules by grouping NICs logically.**

### Common Mistakes in Interviews

- Replacing all NSGs with Firewall only — cost and complexity
- No egress filtering on prod subnets
- Firewall rules without naming and documentation

---

## Q043: Hub-Spoke Topology

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

Design hub-spoke network topology for enterprise Azure landing zone.

### Short Answer (30 seconds)

Hub VNet: firewall, VPN/ExpressRoute gateway, DNS, Bastion. Spoke VNets: workloads peer to hub; no spoke-to-spoke without hub inspection (or AVNM).

### Detailed Answer (3–5 minutes)

**Components:**
```
Hub (10.0.0.0/16)
├── Azure Firewall
├── ExpressRoute GW
├── DNS Private Resolver
Spoke A (10.1.0.0/16) ──peering──► Hub
Spoke B (10.2.0.0/16) ──peering──► Hub
```

**Architect decisions:**
- Use Virtual WAN hub at scale (100+ spokes)
- UDR default route `0.0.0.0/0` → Firewall private IP
- IP plan avoids overlap with on-prem

**CAF reference:** Implement via ALZ or Terraform/Bicep modules.

### Architecture Perspective

Hub-spoke is default enterprise Azure network pattern.

### Follow-up Questions

1. **VWAN vs classic hub? — VWAN simplifies large-scale routing and S2S VPN.**
2. **Spoke-to-spoke traffic? — Route through firewall or enable direct peering with governance.**

### Common Mistakes in Interviews

- Flat VNet per app with no central egress control
- Overlapping IP ranges with on-prem
- Peering without UDR to firewall

---

## Q044: Private Link Overview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

Explain Azure Private Link and architect use cases.

### Short Answer (30 seconds)

Private Link exposes PaaS services via private IP in your VNet — traffic stays on Microsoft backbone, no public endpoint needed.

### Detailed Answer (3–5 minutes)

**Components:**
- **Private Endpoint** — NIC in your subnet with private IP
- **Private DNS Zone** — `privatelink.database.windows.net` resolves to private IP

**Use cases:**
- SQL, Storage, Key Vault, App Service inbound private access
- Consumer connects without service public IP

**Architect:** Default deny public network access on PaaS + Private Endpoint. DNS is critical — broken DNS causes 'can't connect' incidents.

### Architecture Perspective

Private Link is standard zero-trust PaaS connectivity pattern.

### Follow-up Questions

1. **Private Link vs Service Endpoints? — Private Link gives private IP; service endpoints route over backbone but public IP target.**
2. **Private Link for App Service? — Inbound private endpoint on Premium v2+.**

### Common Mistakes in Interviews

- Public endpoints on prod databases
- Private endpoint without private DNS zone
- On-prem DNS not forwarding privatelink zones

---

## Q045: Bicep vs Terraform

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | IaC |
| **Frequency** | Very Common |

### Question

Choose Bicep vs Terraform for Azure-only landing zone.

### Short Answer (30 seconds)

Bicep: native Azure, no state file, day-zero support, ARM integration. Terraform: multi-cloud, mature module ecosystem, state management — choose by team skills and multi-cloud requirement.

### Detailed Answer (3–5 minutes)

**Bicep advantages:**
- Transpiles to ARM — no state drift file
- `what-if` and deployment stacks native
- Azure Quickstart modules

**Terraform advantages:**
- AWS/GCP same tooling
- Terragrunt for multi-env
- Large community modules

**Architect:** Azure-only shop → Bicep default. Multi-cloud mandate → Terraform with Azure provider. Don't maintain both for same resources.

### Architecture Perspective

IaC tool choice is organizational — architects standardize one.

### Follow-up Questions

1. **Bicep vs ARM JSON? — Bicep is authoring layer — always compiles to ARM.**
2. **Terraform state in Azure? — Store in Storage account with locking.**

### Common Mistakes in Interviews

- Portal-only deploys in production
- Both Bicep and Terraform managing same RG
- No PR review on IaC changes

---

## Q046: Template Specs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | IaC |
| **Frequency** | Common |

### Question

What are Azure Template Specs and when use them?

### Short Answer (30 seconds)

Template Specs are versioned Bicep/ARM templates stored as Azure resources — share approved patterns across subscriptions with RBAC control.

### Detailed Answer (3–5 minutes)

**Workflow:**
1. Platform team publishes `Template Spec` to shared resource group
2. App teams deploy via `Microsoft.Resources/deployments` referencing spec version
3. Version pinning ensures consistent landing patterns

**Architect use cases:**
- Approved App Service + SQL pattern
- Spoke VNet subscription provisioning
- Compliance baseline resources

**vs Git repo:** Template Spec is Azure-native artifact with RBAC; Git remains source of truth in CI/CD pipeline.

### Architecture Perspective

Template Specs enable self-service within guardrails.

### Follow-up Questions

1. **Template Spec vs Deployment stack? — Spec is template artifact; stack manages deployed resource lifecycle.**
2. **Version strategy? — Semantic versioning; deprecate old versions with sunset date.**

### Common Mistakes in Interviews

- Emailing Bicep files between teams
- No version pinning — always latest
- Template Spec without testing in CI

---

## Q047: What-If Deployment

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | IaC |
| **Frequency** | Common |

### Question

How use ARM/Bicep what-if before production deployment?

### Short Answer (30 seconds)

`az deployment group what-if` or Bicep what-if in CI pipeline previews creates/modifies/deletes without applying — mandatory gate before prod deploy.

### Detailed Answer (3–5 minutes)

**What-if output:**
- **Create** — new resources
- **Modify** — property changes (highlight destructive)
- **Delete** — resources removed from template scope

**Architect CI/CD:**
```bash
az deployment group what-if \
  --resource-group rg-orders-prod \
  --template-file main.bicep
```

Block pipeline on unexpected deletes. Pair with `canNotDelete` locks and Policy.

### Architecture Perspective

What-if prevents 'template deleted our SQL server' disasters.

### Follow-up Questions

1. **What-if vs validate? — Validate syntax; what-if shows actual delta against live state.**
2. **Incremental vs complete mode? — Complete mode deletes resources not in template — dangerous.**

### Common Mistakes in Interviews

- Deploy to prod without what-if
- Complete deployment mode by default
- Ignoring what-if delete warnings

---

## Q048: Role Assignment Best Practices

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Azure RBAC role assignment best practices for production?

### Short Answer (30 seconds)

Least privilege, narrowest scope, group-based assignments not individuals, PIM for admin roles, managed identities for apps, periodic access reviews.

### Detailed Answer (3–5 minutes)

**Patterns:**
- `Contributor` on resource group, not subscription
- Use built-in roles before custom
- Assign to Entra groups (`Azure-Orders-Prod-Contributors`)
- PIM eligible Owner on prod subscription — max 8 hour activation
- CI/CD: federated credential OIDC, custom deploy role

**Architect:** Quarterly access review via Entra ID Access Reviews. Deny `Owner` standing assignment via Policy audit.

### Architecture Perspective

RBAC hygiene is continuous — not one-time setup.

### Follow-up Questions

1. **ABAC vs RBAC? — Azure ABAC conditions on roles (e.g., tag match) — advanced least privilege.**
2. **Role assignment propagation delay? — Up to 30 minutes — plan deployment pipeline retries.**

### Common Mistakes in Interviews

- Owner assigned to developers permanently
- Individual user assignments not groups
- Service principal with Contributor on subscription

---

## Q049: Break-Glass Accounts

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Design break-glass accounts for Azure subscription emergency access.

### Short Answer (30 seconds)

Two cloud-only global admin accounts, excluded from Conditional Access, credentials in physical safe, monitored with alerts on any sign-in, tested quarterly, separate from daily admin accounts.

### Detailed Answer (3–5 minutes)

**Requirements:**
- `@company.onmicrosoft.com` — no MFA device dependency that could fail
- Excluded from CA policies that could lock everyone out
- Alert Sentinel/Defender on ANY login
- Document usage approval (two executives)

**Architect:** Break-glass is last resort — daily ops use PIM. Never use break-glass for routine deploys.

### Architecture Perspective

Break-glass design shows mature identity architecture.

### Follow-up Questions

1. **Break-glass vs emergency access in PIM? — PIM for normal elevation; break-glass when Entra/CA broken.**
2. **How many break-glass accounts? — Microsoft recommends at least 2 cloud-only emergency accounts.**

### Common Mistakes in Interviews

- Break-glass account used daily by admins
- Break-glass subject to same CA as everyone — locks out during CA misconfig
- No alerting on break-glass sign-in

---

## Q050: Subscription Vending

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

Implement subscription vending in Azure landing zone.

### Short Answer (30 seconds)

Automated pipeline creates subscription via EA/MCA API, assigns to MG, applies Policy, RBAC, network peering, and tags — self-service request via ServiceNow/Portal.

### Detailed Answer (3–5 minutes)

**Pipeline steps:**
1. Validate request (owner, cost center, environment)
2. Create subscription (Billing API / Account Factory)
3. Move to target MG
4. Deploy spoke via Template Spec (VNet, UDR, peering)
5. Assign RBAC to owner group
6. Register in CMDB

**Architect:** Subscription vending scales cloud adoption — manual sub creation doesn't past 20 teams.

**Tools:** Azure Landing Zone Accelerator, Terraform Cloud, custom Bicep + Azure DevOps.

### Architecture Perspective

Subscription vending is platform engineering deliverable for scale.

### Follow-up Questions

1. **Alias vs subscription? — Create subscription alias for programmatic repeatability.**
2. **Quota in vending? — Check regional vCPU quotas during vending workflow.**

### Common Mistakes in Interviews

- Manual subscription creation per request
- New subscriptions land in root MG ungoverned
- No RBAC template in vending pipeline

---
