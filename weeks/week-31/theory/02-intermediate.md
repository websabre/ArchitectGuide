# IaC — Intermediate: Enterprise Patterns

> **Week 31** | Policy as code, remote state, multi-subscription

## 1. Policy as Code

**Azure Policy** + Bicep:

```bicep
resource policy 'Microsoft.Authorization/policyAssignments@2022-06-01' = {
  name: 'require-tags'
  properties: {
    policyDefinitionId: '/providers/Microsoft.Authorization/policyDefinitions/...'
    parameters: {
      tagName: { value: 'Environment' }
    }
  }
}
```

**Terraform:** Sentinel or OPA for plan validation.

---

## 2. Remote State & Locking

```hcl
terraform {
  backend "azurerm" {
    resource_group_name  = "rg-tfstate"
    storage_account_name = "sttfstate"
    container_name       = "tfstate"
    key                  = "prod.terraform.tfstate"
  }
}
```

**Never** commit state to Git. Use blob locking (Azure) or DynamoDB (AWS).

---

## 3. Workspaces vs Separate State per Environment

| Approach | Use When |
|----------|----------|
| Terraform workspaces | Small teams, similar envs |
| Separate state files | Prod isolation, different subscriptions |
| Separate repos | Strict compliance boundaries |

**Architect:** Prod state in separate subscription with RBAC — only platform team can apply.

---

## 4. Importing Existing Resources

Brownfield: `terraform import` or `az resource export` → Bicep.

**Process:**
1. Inventory manual resources
2. Import into IaC
3. Plan should show no changes
4. Enforce policy to prevent drift

---

## 5. Cost Tags in IaC

```bicep
var tags = {
  Environment: environment
  CostCenter: costCenter
  Owner: ownerEmail
  ManagedBy: 'Bicep'
}
```

FinOps starts at provisioning — untagged resources are invisible in cost reports.
