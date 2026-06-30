# Lab 29 — Feature Flags with Azure App Configuration

**Duration:** 2–3 hours | **Prerequisites:** Azure subscription, .NET 8 SDK

## Objectives
- Configure Azure App Configuration with feature flags
- Integrate `Microsoft.FeatureManagement` in ASP.NET Core
- Practice percentage rollout and targeting

## Steps

### 1. Create App Configuration

```bash
az appconfig create -n appconfig-order-dev -g rg-dev -l eastus --sku Standard
az appconfig feature set -n NewCheckout --label dev --connection-string "..." --description "New checkout flow"
```

### 2. Add to ASP.NET Core

```csharp
builder.Configuration.AddAzureAppConfiguration(options =>
    options.Connect(connectionString).UseFeatureFlags());

builder.Services.AddFeatureManagement();
```

### 3. Use in Controller

```csharp
[FeatureGate("NewCheckout")]
[HttpPost("checkout/v2")]
public async Task<IActionResult> CheckoutV2(...) { }
```

### 4. Percentage Rollout

Enable for 10% of users; monitor error rate; increase to 50%, then 100%.

## Deliverables
- [ ] Feature flag toggles without redeploy
- [ ] Targeting filter by user ID
- [ ] Document rollback procedure in ADR format

## Rubric
| Criteria | Points |
|----------|--------|
| App Config integrated | 25 |
| Percentage rollout works | 25 |
| Kill switch documented | 25 |
| No hardcoded flags in code | 25 |
