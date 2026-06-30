# Week 16 — Azure Capstone Architecture Diagrams

## 1. Reference 3-Tier .NET SaaS on Azure

```mermaid
flowchart TB
    User --> FD[Azure Front Door + WAF]
    FD --> App[App Service / AKS]
    App --> MI[Managed Identity]
    MI --> SQL[(Azure SQL)]
    App --> Redis[Azure Cache for Redis]
    App --> SB[Service Bus]
    App --> AI[App Insights]
    App --> KV[Key Vault]
```

## 2. Multi-Region Active-Passive

```mermaid
flowchart LR
    subgraph Primary["East US"]
        PApp[App]
        PDB[(SQL Primary)]
    end
    subgraph DR["West US"]
        DApp[App standby]
        DDB[(SQL Geo-Replica)]
    end
    FD[Front Door] --> PApp
    FD -.->|failover| DApp
    PDB --> DDB
```

## 3. Observability — End to End

```mermaid
flowchart LR
    OTel[OpenTelemetry SDK] --> AI[Application Insights]
    AI --> WB[Workbooks + Alerts]
    AI --> AM[Azure Monitor Action Groups]
```

## 4. CI/CD to Azure

```mermaid
flowchart LR
    GH[GitHub] --> GHA[Actions]
    GHA --> ACR[Container Registry]
    ACR --> AS[App Service Slot]
    GHA --> IaC[Bicep Deploy]
```

## 5. Cost Governance

```mermaid
flowchart TB
    Tags[Resource Tags] --> Cost[Cost Management]
    Budget[Budget Alerts] --> Action[Auto-shutdown dev]
```

## Practice Exercise

Produce a single-page architecture for Week 16 capstone: 3-tier SaaS with DR and observability.

---

[← Back to Week 16](../README.md)
