# Lab 12: Entra ID, Managed Identity & Key Vault

| **Week** | 12 | **Duration** | 120 min |

## Objectives
- [ ] Register app in Entra ID
- [ ] Configure Managed Identity on App Service
- [ ] Store and retrieve secrets from Key Vault
- [ ] Configure API authentication with JWT

## Steps

### 1. Create Key Vault
```bash
az keyvault create --name kv-archlab-$RANDOM --resource-group rg-architect-lab-09 \
  --location eastus --enable-rbac-authorization true

az keyvault secret set --vault-name <kv> --name SqlConnectionString \
  --value "Server=tcp:...;Database=ordersdb;..."
```

### 2. App Service Managed Identity
```bash
az webapp identity assign --name <app-name> --resource-group rg-architect-lab-09
PRINCIPAL_ID=$(az webapp identity show --name <app-name> --resource-group rg-architect-lab-09 --query principalId -o tsv)
az role assignment create --role "Key Vault Secrets User" --assignee $PRINCIPAL_ID --scope <keyvault-id>
```

### 3. Key Vault Reference in App Settings
```
SqlConnection=@Microsoft.KeyVault(SecretUri=https://<kv>.vault.azure.net/secrets/SqlConnectionString/)
```

### 4. Entra ID App Registration for API
```bash
# Register API app, expose scope, register client app
# Configure App Service Authentication (Easy Auth) or JWT validation in .NET
```

### 5. .NET JWT Validation
```csharp
builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddMicrosoftIdentityWebApi(builder.Configuration.GetSection("AzureAd"));
```

## Security Checklist
- [ ] No secrets in source code or appsettings committed to git
- [ ] Key Vault soft delete enabled
- [ ] Least-privilege RBAC on Key Vault
- [ ] HTTPS only on App Service

## Architect Report
1. Client credentials vs auth code — which for your internal Order API?
2. Draw identity flow diagram for user → API → SQL via MI
3. What changes for multi-tenant SaaS?
