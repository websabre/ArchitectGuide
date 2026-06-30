# Week 31 — Fundamentals Interview Q&A

> Q001–Q030: Premium format (Week 1 quality).
> See also: [DevOps Top 50](../../../interview-prep/devops-top-50-index.md)

---


## Q001: Terraform vs Bicep

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | IaC |
| **Frequency** | Very Common |

### Question

When do you choose Terraform vs Bicep for Azure infrastructure?

### Short Answer (30 seconds)

Bicep for Azure-only — day-zero resources, no state file. Terraform for multi-cloud or existing HCL investment. Document choice in ADR.

### Detailed Answer (3–5 minutes)

| Factor | Bicep | Terraform |
|--------|-------|----------|
| Azure | Day-zero | Slight lag |
| State | ARM tracks | Remote state required |
| Multi-cloud | No | Yes |

.NET Azure shop default: Bicep.

### Architecture Perspective

IaC choice is a 5-year decision — migration cost is high.

### Follow-up Questions

1. Coexist? — Yes with clear resource ownership boundaries.
2. AKS + multi-cloud? — Terraform or split by domain.

### Common Mistakes in Interviews

- Terraform always better in Azure-only context
- Ignoring state management overhead
- No ADR documenting choice

---

## Q002: Terraform Remote State

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Terraform |
| **Frequency** | Common |

### Question

How should Terraform state be stored for production?

### Short Answer (30 seconds)

Azure Storage or S3 with locking, encryption, versioning, RBAC restricted to platform team. Separate state per environment. Never commit state to Git.

### Detailed Answer (3–5 minutes)

State loss requires painful `terraform import` — treat as DR-critical. State contains sensitive values — encrypt and restrict access.

### Architecture Perspective

Junior architects design resources; senior architects design state strategy.

### Follow-up Questions

1. Workspaces vs separate state? — Separate state files for prod isolation.
2. State in Git? — Never; secrets leak in state files.

### Common Mistakes in Interviews

- Local state for production
- One state file for all environments
- No versioning on state blob

---

## Q003: Bicep Module Structure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Bicep |
| **Frequency** | Common |

### Question

How do you structure Bicep modules for multi-environment .NET platforms?

### Short Answer (30 seconds)

`/modules/` for reusable resources, `/environments/{dev,staging,prod}/` with `.bicepparam` differing SKUs. Same modules, different parameters — never fork module code.

### Detailed Answer (3–5 minutes)

Outputs: Key Vault URI, app name — consumed by app CI pipeline as environment variables.

### Architecture Perspective

Module boundaries mirror platform service catalog.

### Follow-up Questions

1. Bicep registry? — OCI artifacts for cross-subscription reuse.
2. Too many modules? — Balance granularity vs maintenance.

### Common Mistakes in Interviews

- Copy-paste Bicep per environment
- Modules too monolithic
- Hardcoded prod values in shared module

---

## Q004: IaC Drift Detection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | IaC |
| **Frequency** | Common |

### Question

How do you detect and prevent infrastructure drift?

### Short Answer (30 seconds)

Nightly `terraform plan` or `what-if` in CI alerts on diff. Azure Policy denies manual SKU changes. Emergency portal changes backported to IaC within 24 hours.

### Detailed Answer (3–5 minutes)

Drift scenario: manual SQL scale-up reverted by Monday apply → outage. Layers: Policy prevent → CI detect → apply correct OR update IaC if intentional.

### Architecture Perspective

Drift is governance failure — connects IaC, ops culture, incidents.

### Follow-up Questions

1. Intentional drift? — Break-glass with ticket and backport.
2. Black Friday freeze? — No prod IaC applies during peak.

### Common Mistakes in Interviews

- IaC without Policy enforcement
- Apply without reviewing plan diff
- Assuming teams won't use portal

---

## Q005: Policy as Code

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Governance |
| **Frequency** | Common |

### Question

How does Azure Policy complement IaC?

### Short Answer (30 seconds)

IaC defines desired state proactively; Policy enforces guardrails on any creation path including portal. Require tags, deny public storage, enforce regions.

### Detailed Answer (3–5 minutes)

Defense in depth: Bicep deploys compliant resources; Policy catches manual mistakes and shadow IT. Initiative bundles map to SOC 2 controls.

### Architecture Perspective

Don't rely on IaC discipline alone at enterprise scale.

### Follow-up Questions

1. Terraform Sentinel? — Plan-time policy for TF shops.
2. Too restrictive? — Sandbox subscription for experimentation.

### Common Mistakes in Interviews

- Policy so strict developers cannot work
- No tag enforcement
- Policy without exemption process

---

## Q006: Environment Promotion with IaC

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | IaC |
| **Frequency** | Common |

### Question

How do you promote infrastructure changes from dev to production?

### Short Answer (30 seconds)

Same modules; PR triggers plan on dev+staging; merge applies staging; production requires approval gate. Never `terraform apply` prod from laptop.

### Detailed Answer (3–5 minutes)

Parameter differences: dev S1 SQL, prod P2 with zone redundancy. Prod apply only from pipeline service principal with separate state file.

### Architecture Perspective

Environment promotion integrates IaC and CI/CD design.

### Follow-up Questions

1. Ephemeral PR environments? — Deploy on PR open, destroy on close.
2. Blue-green infra? — Separate resource groups + traffic switch.

### Common Mistakes in Interviews

- Different module code per environment
- Manual prod changes
- Prod apply from developer laptop

---

## Q007: Brownfield IaC Import

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | IaC |
| **Frequency** | Occasional |

### Question

How do you bring manually created Azure resources under IaC?

### Short Answer (30 seconds)

Inventory, write matching Bicep/Terraform, import, verify plan shows zero changes, enable Policy to prevent drift.

### Detailed Answer (3–5 minutes)

`terraform import` or Bicep `existing` keyword. Prioritize by blast radius — prod SQL before dev storage. `az bicep decompile` is starting point only — needs cleanup.

### Architecture Perspective

Most architects inherit brownfield — import strategy is practical gold.

### Follow-up Questions

1. Delete and recreate? — Downtime and data loss — avoid.
2. Import all at once? — Phased by resource group.

### Common Mistakes in Interviews

- Assuming decompile is production-ready
- No drift prevention after import
- Managing same resource in TF and Bicep

---

## Q008: IaC Testing in Pull Requests

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | IaC |
| **Frequency** | Common |

### Question

How do you test IaC changes before production apply?

### Short Answer (30 seconds)

`terraform validate`, Checkov/tfsec, plan/what-if commented on PR, ephemeral environment smoke test.

### Detailed Answer (3–5 minutes)

Prod plan with read-only SP — preview without apply. Auto-destroy ephemeral envs after 24h.

### Architecture Perspective

IaC CI as important as application CI — misconfigured NSG worse than a bug.

### Follow-up Questions

1. fmt check? — `terraform fmt -check` in CI.
2. Cost of ephemeral envs? — Budget alerts and auto-teardown.

### Common Mistakes in Interviews

- First apply in prod without plan review
- No static analysis
- Skipping what-if on Bicep PRs

---

## Q009: GitOps vs Push Deployment

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Deployment |
| **Frequency** | Common |

### Question

Compare GitOps and push-based CI/CD for Kubernetes vs App Service.

### Short Answer (30 seconds)

Push: pipeline calls deploy API. GitOps: Argo CD reconciles cluster to Git. GitOps ideal for AKS; push fine for App Service and Bicep pipelines.

### Detailed Answer (3–5 minutes)

AKS 10+ services → GitOps reduces kubectl-from-CI risk. App Service + Bicep → push model with desired-state in pipeline is equivalent.

### Architecture Perspective

Model choice depends on compute platform — not universal GitOps.

### Follow-up Questions

1. GitOps for App Service? — Less common; Bicep pipeline is desired-state pattern.
2. Rollback? — Git revert vs redeploy artifact.

### Common Mistakes in Interviews

- GitOps without understanding reconciliation loop
- kubectl apply from laptop to prod
- Mandating GitOps for 3 App Service APIs

---

## Q010: FinOps Tags in IaC

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

How do you enforce cost allocation tags through IaC?

### Short Answer (30 seconds)

Mandatory tags in modules: Environment, CostCenter, Owner, Application. Azure Policy denies untagged resources.

### Detailed Answer (3–5 minutes)

FinOps reports impossible without tags at provision time. Limit to 5–7 mandatory tags to avoid sprawl.

### Architecture Perspective

FinOps starts at provision — retrofitting 500 resources is painful.

### Follow-up Questions

1. Showback? — Tags enable team cost dashboards.
2. Optional tags? — Policy should enforce, not audit only.

### Common Mistakes in Interviews

- Optional tags in modules
- No Policy enforcement
- 15+ mandatory tags slowing deployments

---




## Q011: Bicep vs Terraform Decision Framework

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | IaC |
| **Frequency** | Very Common |

### Question

Walk through your decision framework for Bicep vs Terraform on an Azure-only .NET platform.

### Short Answer (30 seconds)

Azure-only greenfield → Bicep (day-zero resources, ARM-backed state). Multi-cloud or existing TF investment → Terraform. Document in ADR with 5-year migration cost estimate.

### Detailed Answer (3–5 minutes)

**Decision matrix:**
| Factor | Bicep | Terraform |
|--------|-------|----------|
| Azure coverage | Day-zero | Slight lag |
| State management | ARM tracks | Remote backend required |
| Multi-cloud | No | Yes |
| Team skills | ARM DSL learning curve | HCL widely known |
| Module registry | ACR OCI | Terraform Registry |

**Hybrid:** Bicep for Azure PaaS; Terraform for Cloudflare + Azure. Clear ownership boundary per resource group.

**Architect:** Coexistence OK — never manage same resource in both tools.

### Architecture Perspective

IaC choice is long-lived — interviewers want criteria not tribal preference.

### Follow-up Questions

1. **Pulumi/C#? — Option when team wants IaC in C# — evaluate team appetite.**
2. **Switching cost? — High — pick deliberately in ADR.**

### Common Mistakes in Interviews

- Terraform for 100% Azure with no multi-cloud plan
- Same resource in Bicep and Terraform
- No ADR documenting IaC choice

---

## Q012: Bicep Module Composition

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Bicep |
| **Frequency** | Common |

### Question

How do you compose Bicep modules for a .NET platform landing zone?

### Short Answer (30 seconds)

Layer modules: `network.bicep` → `keyVault.bicep` → `appService.bicep` → `appInsights.bicep`. Parent template orchestrates; modules expose minimal params and outputs.

### Detailed Answer (3–5 minutes)

**Structure:**
```
modules/
  networking/vnet.bicep
  compute/appServicePlan.bicep
  security/keyVault.bicep
main.bicep  # wires modules
```

**Rules:**
- Modules 50–150 lines — not monolithic 800-line file
- Outputs: `keyVaultUri`, `appServiceName` for pipeline consumption
- Semantic versioning via Bicep registry OCI artifacts

**Architect:** Module catalog mirrors platform service offerings.

### Architecture Perspective

Module composition enables environment promotion with same building blocks.

### Follow-up Questions

1. **Nested vs registry modules? — Registry for cross-subscription reuse.**
2. **Too granular? — Balance copy-paste vs 40-module dependency graph.**

### Common Mistakes in Interviews

- 800-line monolithic main.bicep
- Copy-paste module per environment
- Modules with hardcoded prod SKU

---

## Q013: Terraform State Backend on Azure Storage

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Terraform |
| **Frequency** | Common |

### Question

Configure Terraform remote state on Azure Storage for production workloads.

### Short Answer (30 seconds)

Storage account with versioning, encryption, private endpoint, RBAC restricted to platform pipeline SP. Separate container per environment.

### Detailed Answer (3–5 minutes)

**Backend config:**
```hcl
backend "azurerm" {
  resource_group_name  = "rg-tfstate-prod"
  storage_account_name = "sttfstateprod"
  container_name       = "tfstate-order"
  key                  = "prod.terraform.tfstate"
}
```

**Hardening:**
- Blob versioning enabled — recover corrupted state
- `Storage Blob Data Contributor` only for pipeline SP
- No public network access

**Architect:** State is DR-critical — backup strategy documented.

### Architecture Perspective

Remote state is prerequisite for team IaC — local state is solo-dev only.

### Follow-up Questions

1. **State per env vs workspace? — Separate state files for prod isolation preferred.**
2. **Sensitive values in state? — Encrypt; restrict access; use sensitive outputs carefully.**

### Common Mistakes in Interviews

- Local terraform.tfstate committed to Git
- Single state file for dev and prod
- No blob versioning on state account

---

## Q014: Terraform State Locking

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Terraform |
| **Frequency** | Common |

### Question

How does state locking prevent concurrent Terraform applies and what breaks it?

### Short Answer (30 seconds)

Azure backend uses blob lease for lock during `apply`. Concurrent apply fails with lock error — prevents state corruption.

### Detailed Answer (3–5 minutes)

**Failure modes:**
- CI job killed mid-apply — stale lock remains
- Fix: `terraform force-unlock LOCK_ID` after verifying no running apply

**Prevention:**
- Timeout on pipeline jobs
- One apply per state file at a time (`concurrency` group in GitHub Actions)
- Never apply prod from laptop while pipeline runs

**Architect:** Locking is why remote state mandatory for teams — local state has no lock.

### Architecture Perspective

State locking incidents are common ops scenarios — know unlock procedure.

### Follow-up Questions

1. **DynamoDB locking on AWS? — Same concept — Azure uses blob lease.**
2. **Bicep locking? — ARM deployment locking at resource group level — different mechanism.**

### Common Mistakes in Interviews

- Two pipeline applies to prod simultaneously
- Force-unlock without checking running jobs
- No concurrency control in CI pipeline

---

## Q015: IaC Drift Detection Automation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | IaC |
| **Frequency** | Common |

### Question

Automate infrastructure drift detection for Bicep and Terraform managed resources.

### Short Answer (30 seconds)

Nightly scheduled pipeline: `terraform plan -detailed-exitcode` or `az deployment group what-if` — alert on non-empty diff. Azure Policy denies unauthorized changes.

### Detailed Answer (3–5 minutes)

**Layers:**
1. **Prevent:** Policy denies public IP, enforces SKU whitelist
2. **Detect:** Nightly plan/what-if in read-only mode
3. **Remediate:** Auto-apply correct state OR backport portal hotfix to IaC within 24h

**Alert:** Slack message with diff summary — assign owner.

**Architect:** Black Friday manual scale-up must be backported or reverted Monday.

### Architecture Perspective

Drift detection closes the loop on IaC governance.

### Follow-up Questions

1. **Intentional break-glass? — Ticket + 24h backport SLA.**
2. **Drift on auto-scaled resources? — Exclude scale sets from strict drift or use target tracking in IaC.**

### Common Mistakes in Interviews

- Portal changes never reconciled to IaC
- Drift detected but no owner assigned
- Auto-apply drift without human review on prod

---

## Q016: Bicep What-If Preview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Bicep |
| **Frequency** | Common |

### Question

How do you use Bicep what-if in pull request workflows?

### Short Answer (30 seconds)

CI runs `az deployment group what-if` with read-only SP; bot comments predicted creates/modifies/deletes on PR. Reviewers see blast radius before merge.

### Detailed Answer (3–5 minutes)

**Pipeline:**
```bash
az deployment group what-if \
  --resource-group rg-order-staging \
  --template-file main.bicep \
  --parameters @staging.bicepparam
```

**PR comment:** Parse JSON output — highlight destructive changes (delete, SKU downgrade).

**Architect:** What-if is Bicep's plan equivalent — mandatory for prod-bound PRs.

### Architecture Perspective

What-if prevents surprise deletions — common IaC incident source.

### Follow-up Questions

1. **What-if vs validate? — Validate syntax only; what-if shows actual ARM changes.**
2. **Scope? — Resource group deployment for most .NET workloads; subscription for landing zone.**

### Common Mistakes in Interviews

- First visibility of changes at apply time
- What-if skipped for 'small' PRs
- No highlight of destructive changes in PR

---

## Q017: Policy as Code with Azure Policy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Governance |
| **Frequency** | Common |

### Question

Design Azure Policy initiatives that complement Bicep deployments for a .NET platform.

### Short Answer (30 seconds)

IaC deploys desired state; Policy catches portal drift and non-IaC creation paths. Initiative bundles: require tags, deny public storage, allowed regions, enforce Managed Identity.

### Detailed Answer (3–5 minutes)

**Example policies:**
- `Deny` — Storage account public access
- `AuditIfNotExists` — Diagnostic settings on App Service
- `DeployIfNotExists` — Auto-enable Defender

**Mapping:** Policy initiative per compliance framework (SOC 2 CC6, CC7).

**Architect:** Policy exemption process with expiry — not permanent exceptions.

### Architecture Perspective

Policy as code is defense in depth beyond IaC discipline.

### Follow-up Questions

1. **Terraform Sentinel? — Plan-time policy for TF shops — Azure Policy for ARM resources.**
2. **Policy vs RBAC? — Policy restricts resource config; RBAC restricts who can create.**

### Common Mistakes in Interviews

- Policy so strict developers use shadow subscriptions
- No exemption workflow
- IaC-only governance without Policy

---

## Q018: Bicep Parameter Files Per Environment

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Bicep |
| **Frequency** | Common |

### Question

How do `.bicepparam` files enable safe multi-environment deployments?

### Short Answer (30 seconds)

Same `main.bicep` module; `dev.bicepparam`, `staging.bicepparam`, `prod.bicepparam` differ SKUs, capacity, feature flags. Never fork template per environment.

### Detailed Answer (3–5 minutes)

**Example:**
```bicep
// prod.bicepparam
using 'main.bicep'
param appServiceSku = 'P2v3'
param sqlSku = 'GP_Gen5_4'
param enableZoneRedundant = true
```

**CI:** PR triggers what-if for all environments. Prod apply requires approval.

**Architect:** Parameter files are promotion mechanism — template unchanged across envs.

### Architecture Perspective

Parameter files embody DRY multi-environment IaC.

### Follow-up Questions

1. **Secrets in bicepparam? — Reference Key Vault — never plain text.**
2. **Default params? — `main.bicep` defaults for dev only — prod explicit in bicepparam.**

### Common Mistakes in Interviews

- Separate main-prod.bicep fork
- Prod SKU hardcoded in shared module
- Secrets committed in bicepparam files

---

## Q019: Key Vault Secret References in IaC

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Security |
| **Frequency** | Common |

### Question

Reference Key Vault secrets from Bicep without exposing values in templates.

### Short Answer (30 seconds)

Use `getSecret()` in Bicep with user-assigned MI granted Key Vault Secrets User. App Service `keyVaultReference` for runtime — secret never in ARM template output.

### Detailed Answer (3–5 minutes)

**Pattern:**
```bicep
resource app 'Microsoft.Web/sites@2022-03-01' = {
  properties: {
    siteConfig: {
      appSettings: [{
        name: 'ConnectionStrings__Default'
        value: '@Microsoft.KeyVault(SecretUri=${sqlConnSecretUri})'
      }]
    }
  }
}
```

**Pipeline:** Deploy MI + Key Vault access before app referencing secrets.

**Architect:** No secrets in Git, state, or pipeline logs — ever.

### Architecture Perspective

Secret references separate deployment-time from secret value exposure.

### Follow-up Questions

1. **Key Vault purge protection? — Enable on prod — prevent accidental secret deletion.**
2. **Rotation? — Update secret version in Key Vault — app picks up new version if configured.**

### Common Mistakes in Interviews

- Connection string in bicepparam plain text
- Key Vault secret in Terraform output
- Secret echoed in what-if output logged publicly

---

## Q020: CI Validation for Bicep Pull Requests

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | IaC |
| **Frequency** | Common |

### Question

What Bicep validation runs on every pull request before merge?

### Short Answer (30 seconds)

`bicep build`, `bicep lint`, what-if against staging RG, Checkov/static analysis, and optional PSRule for Azure best practices.

### Detailed Answer (3–5 minutes)

**CI pipeline:**
1. `az bicep build --file main.bicep` — compile check
2. `bicep lint` — linter rules
3. Checkov scan — security misconfigurations
4. What-if — predicted changes
5. Cost estimate — `az cost management` preview if available

**Merge gate:** All pass + platform team review for networking changes.

**Architect:** IaC PR checks as rigorous as application PR checks.

### Architecture Perspective

CI validation catches NSG open to world before apply.

### Follow-up Questions

1. **Module registry publish? — Separate pipeline on tag — consumers pin version.**
2. **Breaking module change? — Semver major bump in registry.**

### Common Mistakes in Interviews

- Validate only on prod apply
- No lint rules enabled
- Skip what-if for time savings

---

## Q021: Terraform Workspaces vs Separate State

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Terraform |
| **Frequency** | Common |

### Question

When use Terraform workspaces vs separate state files per environment?

### Short Answer (30 seconds)

Separate state files per environment for production isolation. Workspaces for ephemeral dev sandboxes only — workspace switching error risks prod apply.

### Detailed Answer (3–5 minutes)

**Separate state (recommended prod):**
```
backend key = "prod/order.tfstate"
backend key = "staging/order.tfstate"
```

**Workspaces:** Same backend, different workspace name — lighter but `-workspace=prod` typo danger.

**Architect:** Prod state isolation is non-negotiable — separate backend key or storage container.

### Architecture Perspective

Workspace vs state is common Terraform interview trap.

### Follow-up Questions

1. **Terragrunt? — Wrapper for DRY backend config per env.**
2. **Ephemeral env? — Workspace or separate state destroyed on PR close.**

### Common Mistakes in Interviews

- Prod and dev share workspace
- Workspace select in script without confirmation
- No concurrency lock per state

---

## Q022: Import Existing Azure Resources

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | IaC |
| **Frequency** | Common |

### Question

Import manually created Azure resources into Bicep or Terraform management.

### Short Answer (30 seconds)

Inventory resource → author matching template → `terraform import` or Bicep `existing` + incremental adoption → verify plan shows zero changes → enable Policy.

### Detailed Answer (3–5 minutes)

**Terraform:**
```bash
terraform import azurerm_resource_group.rg /subscriptions/.../resourceGroups/rg-order
```

**Bicep:** `resource kv 'Microsoft.KeyVault/vaults@...' existing = { name: 'kv-prod' }` then expand to full definition.

**Phasing:** Import prod SQL first (highest drift risk), dev storage later.

**Architect:** `az bicep decompile` is starting point — never production-ready without review.

### Architecture Perspective

Brownfield import is reality — architects phase by blast radius.

### Follow-up Questions

1. **Delete and recreate? — Data loss — avoid for stateful resources.**
2. **Import entire subscription day one? — Phased by resource group.**

### Common Mistakes in Interviews

- Decompile output deployed unreviewed
- Import without drift prevention Policy
- Managing same VM in portal and IaC

---

## Q023: Azure Resource Naming Conventions

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | IaC |
| **Frequency** | Common |

### Question

Define a resource naming convention for a multi-team Azure .NET platform.

### Short Answer (30 seconds)

`{type}-{workload}-{env}-{region}-{instance}` — e.g., `app-order-prod-eus-01`, `kv-shared-prod-eus`, `sql-order-stg-eus`. Enforce via Policy and Bicep parameters.

### Detailed Answer (3–5 minutes)

**Components:**
- **Type prefix:** `app`, `func`, `sql`, `st`, `kv`, `rg`
- **Workload:** `order`, `payment`, `shared`
- **Env:** `dev`, `stg`, `prod`
- **Region:** `eus`, `weu`

**Limits:** Storage account 3–24 lowercase alphanumeric — abbreviate.

**Architect:** Naming in platform module — teams pass `workloadName` only; convention applied automatically.

### Architecture Perspective

Naming enables automation, cost allocation, and on-call clarity.

### Follow-up Questions

1. **Global uniqueness? — Storage and Key Vault names global — include random suffix if needed.**
2. **Rename resource? — Often recreate — get naming right at provision.**

### Common Mistakes in Interviews

- Random portal-generated names
- Different convention per team
- No naming in IaC modules — manual each time

---

## Q024: Tagging Strategy Enforcement

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

Enforce mandatory tags through IaC and Azure Policy for cost allocation.

### Short Answer (30 seconds)

Mandatory tags: `Environment`, `CostCenter`, `Owner`, `Application`, `ManagedBy`. Policy `deny` if missing. Bicep module applies tags to all child resources.

### Detailed Answer (3–5 minutes)

**Policy:**
```json
"deny" if tags.CostCenter is empty on resource creation
```

**IaC:**
```bicep
var tags = {
  Environment: environment
  CostCenter: costCenter
  Owner: ownerEmail
}
```

**Limit:** 5–7 mandatory tags — more causes tag sprawl and deploy friction.

**Architect:** Tags at provision time — retrofitting 500 resources is painful.

### Architecture Perspective

Tagging connects IaC to FinOps showback/chargeback.

### Follow-up Questions

1. **Inherited tags? — Resource group tags propagate — set at RG in module.**
2. **Tag audit? — Monthly report untagged resources — Policy audit mode first.**

### Common Mistakes in Interviews

- 15 mandatory tags blocking dev velocity
- Tags optional in modules
- Audit-only Policy never upgraded to deny

---

## Q025: Landing Zone Bicep Modules

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | IaC |
| **Frequency** | Common |

### Question

What belongs in Azure landing zone Bicep modules for .NET workloads?

### Short Answer (30 seconds)

Hub-spoke networking, Log Analytics workspace, Key Vault, ACR, App Service Plan baseline, diagnostic settings, Private DNS — product teams deploy app modules into spoke.

### Detailed Answer (3–5 minutes)

**Module layers:**
1. **Platform landing zone** — subscription vending, policy, networking
2. **Workload landing zone** — RG, App Insights, app plan
3. **Application module** — App Service, SQL, Redis per service

**CAF alignment:** Microsoft Cloud Adoption Framework reference implementations.

**Architect:** Product team cannot create VNet — platform provides spoke subscription.

### Architecture Perspective

Landing zones scale governance — architects define platform vs product boundary.

### Follow-up Questions

1. **Terraform ALZ? — Azure Landing Zones — enterprise-scale alternative to custom Bicep.**
2. **Subscription vending? — Pipeline creates spoke per team from template.**

### Common Mistakes in Interviews

- Every team creates own VNet and firewall
- Landing zone monolith never updated
- No separation platform vs application modules

---

## Q026: Ephemeral Environments with IaC

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | IaC |
| **Frequency** | Common |

### Question

Provision ephemeral PR preview environments with Bicep and tear down on merge.

### Short Answer (30 seconds)

PR opened → pipeline deploys `rg-order-pr-1234` with App Service + SQL basic tier → comment preview URL → PR closed/merged → `az group delete`.

### Detailed Answer (3–5 minutes)

**Cost controls:**
- Auto-delete after 24h TTL tag
- Budget alert per PR RG
- Shared SQL server with per-PR database optional

**IaC:** Same modules as staging; `pr.bicepparam` with minimal SKUs.

**Architect:** Ephemeral envs need DNS wildcard `pr-1234.dev.contoso.com` and Key Vault access for test secrets.

### Architecture Perspective

Ephemeral environments accelerate integration feedback — IDP feature.

### Follow-up Questions

1. **Data seeding? — Flyway/EF migrate on deploy — synthetic data only.**
2. **Shared vs isolated ephemeral? — Isolated RG safer; shared cheaper.**

### Common Mistakes in Interviews

- PR environments never destroyed — cost spiral
- Ephemeral prod SKU sizing
- No TTL or budget alert on preview RGs

---

## Q027: GitOps Argo CD vs Pipeline Deploy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | GitOps |
| **Frequency** | Common |

### Question

Compare Argo CD GitOps and push-based pipeline deploy for AKS vs App Service.

### Short Answer (30 seconds)

AKS with 10+ services → Argo CD reconciles cluster to Git desired state. App Service + Bicep → push pipeline apply is simpler and equivalent desired-state pattern.

### Detailed Answer (3–5 minutes)

**GitOps (pull):**
- Cluster pulls manifests from Git
- Drift auto-corrected
- Rollback = git revert

**Push pipeline:**
- CI calls `az deployment` or `kubectl apply`
- Simpler for PaaS
- Drift requires what-if detection

**Architect:** Match model to compute — don't mandate Argo for 3 App Service APIs.

### Architecture Perspective

GitOps is not universal — platform-dependent architecture choice.

### Follow-up Questions

1. **Flux vs Argo? — Both valid GitOps — organizational preference.**
2. **App Service GitOps? — Bicep in Git + pipeline is functional GitOps.**

### Common Mistakes in Interviews

- kubectl apply from developer laptop to prod
- Argo CD without understanding reconciliation loop
- GitOps mandated for simple PaaS workload

---

## Q028: IaC Security Testing with Checkov

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | IaC |
| **Frequency** | Common |

### Question

Integrate Checkov into IaC CI to catch misconfigurations before apply.

### Short Answer (30 seconds)

Run `checkov -d .` on Bicep/Terraform/ARM in PR pipeline. Gate on CRITICAL; suppress false positives with documented skip comments.

### Detailed Answer (3–5 minutes)

**Common catches:**
- Storage account public access enabled
- NSG allows 0.0.0.0/0 on 3389
- Key Vault soft delete disabled
- SQL no TLS enforcement

**Integration:**
```yaml
- run: pip install checkov && checkov -d infra/ --framework bicep
```

**Architect:** Checkov complements what-if — security rules what-if may not evaluate.

### Architecture Perspective

Static IaC analysis is shift-left for infrastructure security.

### Follow-up Questions

1. **tfsec vs Checkov? — Overlapping — pick one org standard.**
2. **Suppressions? — `# checkov:skip=CKV_AZURE_33 reason=...` with ticket reference.**

### Common Mistakes in Interviews

- Checkov only run manually
- All findings ignored
- No IaC scan in CI pipeline

---

## Q029: Blast Radius via Resource Groups

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | IaC |
| **Frequency** | Common |

### Question

How do resource group boundaries limit IaC blast radius?

### Short Answer (30 seconds)

Scope deployments per RG: `rg-order-prod` contains only order service resources. Failed apply or bad delete affects one workload — not entire subscription.

### Detailed Answer (3–5 minutes)

**Patterns:**
- One RG per microservice per environment
- Network hub in separate RG — peering not co-deployed with app
- State file scoped to RG deployment

**Deletion:** `az group delete` on wrong RG is recoverable if soft-delete enabled — still dangerous.

**Architect:** RG design in landing zone ADR — teams cannot deploy to shared networking RG.

### Architecture Perspective

Blast radius containment is IaC architecture fundamentals.

### Follow-up Questions

1. **Subscription per env? — Further isolation for regulated — higher overhead.**
2. **Locks? — CanNotDelete lock on prod RG — prevent accidental group delete.**

### Common Mistakes in Interviews

- Entire subscription in one template apply
- Shared RG for 12 microservices
- No delete locks on production resource groups

---

## Q030: IaC Code Review Standards

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Governance |
| **Frequency** | Common |

### Question

What should platform team enforce in IaC pull request review checklist?

### Short Answer (30 seconds)

What-if reviewed, no secrets plain text, tags present, naming convention, Checkov clean, module version pinned, destructive changes called out, rollback plan for prod.

### Detailed Answer (3–5 minutes)

**Review checklist:**
- [ ] What-if output attached
- [ ] No `0.0.0.0/0` without justification
- [ ] SKUs match environment bicepparam
- [ ] Diagnostic settings enabled
- [ ] Key Vault references not inline secrets
- [ ] Cost impact noted for SKU changes

**Ownership:** Platform reviews networking; product team reviews app resources.

**Architect:** IaC review is security review — not rubber stamp.

### Architecture Perspective

IaC review standards prevent prod outages from typo in NSG rule.

### Follow-up Questions

1. **Auto-approve bot? — Only for plan-only PRs with zero diff after apply.**
2. **CODEOWNERS? — `infra/` requires platform team approval.**

### Common Mistakes in Interviews

- IaC PR merged without what-if
- Junior dev solo approves prod networking change
- No checklist — ad hoc review

---
