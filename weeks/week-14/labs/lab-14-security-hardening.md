# Lab 14: Azure Security Hardening

| **Week** | 14 | **Duration** | 120 min |

## Objectives
- [ ] Enable Microsoft Defender for Cloud
- [ ] Configure Private Link for SQL
- [ ] Apply Azure Policy (deny public storage)
- [ ] Review secure score and remediate findings

## Steps

### 1. Enable Defender Plans
```bash
az security pricing create --name VirtualMachines --tier Standard
az security pricing create --name SqlServers --tier Standard
az security pricing create --name AppServices --tier Standard
```

### 2. Private Endpoint for SQL
```bash
az network private-endpoint create \
  --name pe-sql --resource-group rg-architect-lab-09 \
  --vnet-name vnet-lab --subnet snet-app \
  --private-connection-resource-id <sql-server-id> \
  --group-id sqlServer --connection-name sql-connection

az network private-dns zone create --resource-group rg-architect-lab-09 \
  --name privatelink.database.windows.net
# Link zone to VNet, create DNS record group
```

### 3. Disable Public SQL Access
```bash
az sql server update --name <server> --resource-group rg-architect-lab-09 --enable-public-network false
```

### 4. Azure Policy — Deny Public Blob
```bash
az policy assignment create --name deny-public-storage \
  --policy <policy-definition-id> --scope /subscriptions/<sub-id>
```

### 5. Review Secure Score
Portal → Defender for Cloud → Recommendations. Document top 5 findings and remediation.

## Architect Report
1. Zero Trust checklist for your workload
2. OWASP Top 10 mapping to controls implemented
3. Cost of security controls vs risk of breach
