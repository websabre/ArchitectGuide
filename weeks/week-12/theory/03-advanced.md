# Azure Identity — Advanced

> **Week 12** | **Level:** Advanced

## Zero Trust on Azure

- Verify explicitly: Conditional Access + continuous access evaluation
- Least privilege: PIM for admin roles, scoped RBAC
- Assume breach: Defender for Cloud, logging to Log Analytics

## B2B vs B2C

| | B2B | B2C |
|---|-----|-----|
| Users | Partner orgs in your tenant | Consumer identities |
| Use | Supplier portal | Customer login |
| Directory | Guest users | Separate B2C tenant |

## Architect Checklist

- [ ] No secrets in appsettings — Key Vault references
- [ ] CI/CD uses OIDC federation, not long-lived SP secrets
- [ ] API exposes only required scopes
- [ ] Service principals documented with owners

**Cross-cutting:** [Security](../../../docs/cross-cutting/security/README.md)

## Architect Deep Dive: Zero Trust on Azure

### Principles applied
- Verify explicitly (every request authenticated)
- Least privilege (RBAC + app roles)
- Assume breach (Private Link, no public SQL endpoints)

### PIM for break-glass
Just-in-time Owner on production subscription — approval + time-bound — satisfies auditor without standing admin access.

