# Infrastructure as Code — Terraform & Bicep

> **Week 31** | **Module:** [iac-terraform-bicep](../../../modules/iac-terraform-bicep/README.md)

## Learning Objectives
- Choose Terraform vs Bicep for Azure/AWS
- Design modular, reusable IaC
- Manage state, drift, and environment promotion

---

## 1. IaC Principles

| Principle | Description |
|-----------|-------------|
| **Declarative** | Describe desired state, tool reconciles |
| **Idempotent** | Same input = same output |
| **Version controlled** | Git is source of truth |
| **Reviewable** | PR review for infra changes |
| **Testable** | Plan/dry-run before apply |

---

## 2. Bicep (Azure-Native)

```bicep
param location string = resourceGroup().location
param appName string

resource plan 'Microsoft.Web/serverfarms@2022-09-01' = {
  name: '${appName}-plan'
  location: location
  sku: { name: 'P1v3', tier: 'PremiumV3' }
}

resource app 'Microsoft.Web/sites@2022-09-01' = {
  name: appName
  location: location
  properties: { serverFarmId: plan.id }
  identity: { type: 'SystemAssigned' }
}
```

**Pros:** Day-zero Azure resources, compiles to ARM, modules, no state file (ARM tracks).

---

## 3. Terraform (Multi-Cloud)

```hcl
resource "azurerm_linux_web_app" "app" {
  name                = var.app_name
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  service_plan_id     = azurerm_service_plan.plan.id

  identity {
    type = "SystemAssigned"
  }
}
```

**State file:** Tracks deployed resources. Store remotely (Azure Storage, S3 + DynamoDB lock).

```bash
terraform plan    # preview changes
terraform apply   # deploy
terraform destroy # tear down
```

---

## 4. Terraform vs Bicep Decision

| Factor | Bicep | Terraform |
|--------|-------|-----------|
| Azure-only | ✅ Preferred | OK |
| Multi-cloud | ❌ | ✅ Preferred |
| State management | ARM handles | You manage |
| Module ecosystem | Growing | Large (Registry) |
| Team knows HCL | — | ✅ |

**Architect:** .NET Azure shop → Bicep default. Multi-cloud mandate → Terraform.

---

## 5. Module Design

```
infra/
├── modules/
│   ├── app-service/
│   ├── sql-database/
│   └── service-bus/
├── environments/
│   ├── dev/
│   │   └── main.bicep
│   ├── staging/
│   └── prod/
```

**Environment promotion:** Same modules, different parameter files. `prod.bicepparam` has larger SKUs.

---

## 6. Drift Detection

**Drift:** Manual portal changes differ from IaC.

| Tool | Action |
|------|--------|
| `terraform plan` | Shows drift |
| Azure Policy | Deny non-compliant |
| Scheduled plan in CI | Alert on drift |

**Architect policy:** No manual production changes. Emergency changes must be backported to IaC within 24 hours.

---

## 7. Testing IaC

- **Static analysis:** `bicep build`, `terraform validate`, Checkov, tfsec
- **Plan in PR:** CI runs plan, comments diff on PR
- **Integration:** Deploy to ephemeral environment, run smoke tests

**Next:** Week 32 Observability
