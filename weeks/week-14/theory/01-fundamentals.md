# Azure Security Architecture

## Zero Trust on Azure
1. Verify explicitly (identity + context)
2. Least privilege access (RBAC)
3. Assume breach (segmentation, monitoring)

## Defense in Depth
```
Internet → WAF → App Gateway → NSG → App → Private Endpoint → Data
```

## Microsoft Defender for Cloud
- CSPM (posture management)
- CWP (workload protection)
- Defender for SQL, Storage, Containers

## Microsoft Sentinel
- SIEM + SOAR
- KQL queries for threat detection
- Automated playbooks

## Encryption
- At rest: SSE, TDE (SQL), CMK in Key Vault
- In transit: TLS 1.2+
- Double encryption for compliance

## Architect Deep Dive: Defense in Depth

### Layers
1. **Perimeter** — WAF, DDoS Protection Standard
2. **Network** — NSG, Private Link, Firewall
3. **Identity** — Entra ID, Conditional Access
4. **Application** — input validation, authZ policies
5. **Data** — TDE, encryption at rest, CMK if required

### Key Vault architecture
- Secrets, keys, certificates centralized
- RBAC: deploy pipeline gets `Secrets User` on specific vault
- Soft delete + purge protection enabled in production

### Microsoft Defender for Cloud
Enable on all subscriptions in landing zone — feed Critical findings to backlog with SLA.

