# Lab 30 — GitHub Actions CI/CD for .NET Microservice

**Duration:** 3–4 hours

## Objectives
- Build multi-stage pipeline: build → test → scan → deploy
- Use OIDC to Azure (no stored credentials)
- Deploy to Azure App Service staging slot

## Pipeline Skeleton

```yaml
permissions:
  id-token: write
  contents: read

jobs:
  build-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-dotnet@v4
        with:
          dotnet-version: '8.0.x'
      - run: dotnet test -c Release --collect:"XPlat Code Coverage"
      - uses: azure/login@v2
        with:
          client-id: ${{ secrets.AZURE_CLIENT_ID }}
          tenant-id: ${{ secrets.AZURE_TENANT_ID }}
          subscription-id: ${{ secrets.AZURE_SUBSCRIPTION_ID }}

  deploy-staging:
    needs: build-test
    environment: staging
    steps:
      - uses: azure/webapps-deploy@v3
        with:
          app-name: order-api
          slot-name: staging
```

## Tasks
1. Add branch protection requiring CI pass
2. Add CodeQL security scan job
3. Swap staging → production on manual workflow_dispatch
4. Add deployment summary with commit SHA and artifact version

## Deliverables
- [ ] Working pipeline on push to main
- [ ] Secrets via GitHub Environments
- [ ] Rollback documented (redeploy previous SHA)
