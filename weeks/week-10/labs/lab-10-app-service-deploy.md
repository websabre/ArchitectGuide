# Lab 10: Deploy .NET 8 API to Azure App Service

| **Week** | 10 | **Duration** | 90 min |

## Objectives
- [ ] Deploy .NET 8 Minimal API to App Service
- [ ] Configure deployment slot (staging)
- [ ] Enable Managed Identity + Key Vault reference
- [ ] Set up Application Insights

## Steps

### 1. Create App Service Plan (Linux, B1)
```bash
az appservice plan create --name asp-archlab --resource-group rg-architect-lab-09 --sku B1 --is-linux
az webapp create --name order-api-lab-$RANDOM --resource-group rg-architect-lab-09 --plan asp-archlab --runtime "DOTNETCORE:8.0"
```

### 2. Deploy from Local
```bash
dotnet publish -c Release
az webapp deploy --resource-group rg-architect-lab-09 --name <app-name> --src-path ./bin/Release/net8.0/publish
```

### 3. Staging Slot
```bash
az webapp deployment slot create --name <app-name> --resource-group rg-architect-lab-09 --slot staging
```

### 4. Managed Identity
```bash
az webapp identity assign --name <app-name> --resource-group rg-architect-lab-09
```

### 5. Application Insights
```bash
az monitor app-insights component create --app order-api-insights --location eastus --resource-group rg-architect-lab-09
```

## Architect Notes
- B1 for lab only — production needs Standard+ with autoscale
- Always use slots for zero-downtime deploy
- Never put secrets in App Settings — Key Vault references

## Cleanup
Delete resource group after lab.
