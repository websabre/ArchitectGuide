# Azure Security — Advanced

> **Week 14** | **Level:** Advanced

## Threat Modeling (STRIDE)

| Threat | Mitigation on Azure |
|--------|---------------------|
| Spoofing | MFA, managed identity |
| Tampering | Immutable storage, signing |
| Repudiation | Diagnostic logs, Activity Log |
| Information disclosure | Private Link, encryption |
| Denial of service | Front Door rate limits, DDoS Standard |
| Elevation of privilege | Least privilege RBAC, PIM |

## DevSecOps Pipeline

```
PR → Sonar/Snyk → Build → Container scan → Deploy to staging → DAST
```

Architect: define quality gates — block on critical CVEs.

**Cross-cutting:** [Security deep dive](../../../docs/cross-cutting/security/README.md)

## Architect Deep Dive: Compliance Architecture

### SOC 2 / ISO mapping (simplified)
- **CC6** logical access → Entra ID + RBAC
- **CC7** monitoring → Log Analytics, Defender
- **CC8** change management → IaC pipeline audit logs

### Data classification
Tag SQL columns and Blob containers Public/Internal/Confidential/Restricted — drives encryption and access patterns.

