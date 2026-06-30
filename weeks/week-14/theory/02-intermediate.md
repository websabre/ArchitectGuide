# Azure Security — Intermediate

> **Week 14** | **Level:** Intermediate

## Defense in Depth Layers

1. **Identity** — Entra ID, Conditional Access
2. **Network** — NSG, Firewall, Private Link
3. **Compute** — Patching, Defender for Servers
4. **Data** — Encryption at rest (CMK vs PMK), TDE
5. **Application** — WAF, input validation, OWASP

## Key Vault Architecture

- Separate vaults per environment (prod/nonprod)
- RBAC over access policies for new deployments
- Soft delete + purge protection in production
- Rotation via automation runbooks or Key Vault rotation

## WAF Rules Strategy

- OWASP 3.2 managed rule set baseline
- Custom rules for rate limiting, geo-blocking
- False positive tuning in detection mode before prevention



## Architect Deep Dive: Application Security

### OWASP API top risks — architect responses
| Risk | Mitigation |
|------|------------|
| Broken auth | Entra ID + policy-based authZ |
| Excessive data exposure | DTO projection, pagination |
| Rate limiting | APIM or ASP.NET rate limiter |
| Injection | parameterized queries, ORM |

### Secret scanning in CI
GitGuardian / Defender for DevOps on every PR — block merge on verified secret leak.

**Next:** [03-advanced.md](03-advanced.md)
