# Lab 09: Azure Landing Zone Setup

| **Week** | 09 | **Duration** | 90 min | **Requires** | Azure free account

## Objectives
- [ ] Create resource group with tagging policy
- [ ] Deploy basic VNet with subnets
- [ ] Configure RBAC with least privilege
- [ ] Set up budget alert

## Steps

### 1. Login and Set Subscription
```bash
az login
az account set --subscription "<your-subscription-id>"
```

### 2. Create Resource Group with Tags
```bash
az group create \
  --name rg-architect-lab-09 \
  --location eastus \
  --tags Environment=Dev CostCenter=Learning Owner=ArchitectGuide
```

### 3. Create VNet
```bash
az network vnet create \
  --resource-group rg-architect-lab-09 \
  --name vnet-lab \
  --address-prefix 10.1.0.0/16 \
  --subnet-name snet-app \
  --subnet-prefix 10.1.1.0/24
```

### 4. RBAC — Reader Role
```bash
az role assignment create \
  --assignee "<user-email>" \
  --role "Reader" \
  --scope /subscriptions/<sub-id>/resourceGroups/rg-architect-lab-09
```

### 5. Budget Alert
```bash
az consumption budget create \
  --budget-name lab-budget \
  --amount 50 \
  --category cost \
  --time-grain monthly
```

## Lab Report
1. Map your setup to WAF pillars
2. What would change for production landing zone?
3. Write ADR: single subscription vs multi-subscription

## Cleanup
```bash
az group delete --name rg-architect-lab-09 --yes --no-wait
```
