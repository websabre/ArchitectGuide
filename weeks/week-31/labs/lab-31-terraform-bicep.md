# Lab 31 — IaC: Bicep Module + Terraform Comparison

**Duration:** 3–4 hours

## Objectives
- Deploy App Service + SQL with Bicep modules
- Replicate with Terraform for comparison
- Run plan in CI on pull request

## Bicep Structure

```
infra/
├── modules/
│   ├── app-service.bicep
│   └── sql-database.bicep
└── main.bicep
```

Deploy:
```bash
az deployment group create -g rg-lab -f main.bicep -p appName=order-api-lab
```

## Terraform Equivalent

```bash
cd terraform/
terraform init
terraform plan -var="app_name=order-api-lab"
terraform apply
```

## Comparison Exercise

| Criteria | Bicep | Terraform |
|----------|-------|-----------|
| Lines of code | ? | ? |
| Plan output clarity | ? | ? |
| Module reuse | ? | ? |
| Team preference | Document | Document |

## Deliverables
- [ ] Both deploy identical resources (different naming prefix)
- [ ] `terraform plan` / `what-if` in GitHub Actions on PR
- [ ] ADR: which tool for your org and why
