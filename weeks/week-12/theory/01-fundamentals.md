# Azure Identity Architecture

## Entra ID (Azure AD)
- Users, groups, app registrations
- Conditional Access policies
- MFA enforcement

## Managed Identity
- System-assigned (lifecycle tied to resource)
- User-assigned (shared across resources)
- No credentials in code — ever

## Authentication Patterns
| Pattern | Use Case |
|---------|----------|
| Client credentials | Service-to-service |
| Authorization code + PKCE | Web/mobile apps |
| On-behalf-of (OBO) | API calling downstream API |
| Managed Identity | Azure resource to Azure service |

## Key Vault
- Secrets, keys, certificates
- Reference from App Service/Functions config
- RBAC + access policies
- Soft delete + purge protection

## Architect Deep Dive: Identity Architecture

### Identity hierarchy
```
Entra ID Tenant
├── Users & Groups
├── App Registrations (OAuth clients)
├── Enterprise Applications (service principals)
└── Managed Identities (Azure-hosted resources)
```

### Managed Identity first
**Never** store client secrets in App Service config for Azure-to-Azure calls. Use system-assigned MI on App Service → grant SQL `db_datareader` via Entra authentication.

### RBAC vs application permissions
- **RBAC** — who can manage Azure resources
- **API permissions** — what the app can do in Microsoft Graph or downstream APIs

### Conditional Access (architect awareness)
Production admin access: MFA + compliant device + named locations. Break-glass accounts excluded but monitored.

