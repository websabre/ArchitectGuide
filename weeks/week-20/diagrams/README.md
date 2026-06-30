# Week 20 — Multi-Cloud Architecture Diagrams

## 1. Active-Active Multi-Cloud (Conceptual)

```mermaid
flowchart TB
    GSLB[Global Load Balancer / Traffic Manager] --> Azure[Azure Region]
    GSLB --> AWS[AWS Region]
    Azure --> DB1[(Azure SQL)]
    AWS --> DB2[(RDS)]
    DB1 <-.->|async repl conflict mgmt| DB2
```

## 2. Cloud-Agnostic Abstraction

```mermaid
flowchart LR
    App[.NET Core API] --> Abs[IStorage IMessaging ICache]
    Abs --> AzureAdp[Azure Adapters]
    Abs --> AWSAdp[AWS Adapters]
```

## 3. DR — Primary Azure, DR AWS

```mermaid
flowchart LR
    Prod[Azure Primary] -->|replicate| DR[AWS DR Warm]
    TM[Traffic Manager] --> Prod
    TM -.->|failover| DR
```

## 4. Observability Across Clouds

```mermaid
flowchart LR
    AzureAI[App Insights] --> OTel[OpenTelemetry Collector]
    AWSXRay[X-Ray / CloudWatch] --> OTel
    OTel --> Grafana[Grafana / Datadog]
```

## 5. Decision — Single vs Multi-Cloud

```mermaid
flowchart TD
    A[Workload] --> B{Regulatory multi-cloud?}
    B -->|No| C[Single cloud + DR region]
    B -->|Yes| D[Multi-cloud with explicit TCO]
    D --> E[Avoid lowest-common-denominator trap]
```

## Practice Exercise

Build a comparison table (5 rows) for the same .NET API on Azure App Service vs AWS ECS Fargate.

---

[← Back to Week 20](../README.md)
