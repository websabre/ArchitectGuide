# Week 10 — Azure Compute & App Services Diagrams

## 1. App Service vs AKS Decision

```mermaid
flowchart TD
    A[.NET workload] --> B{Need K8s ecosystem?}
    B -->|No| AS[App Service / Container Apps]
    B -->|Yes| AKS[AKS]
    AS --> C[PaaS ops - faster ship]
    AKS --> D[Fine-grained control - more ops]
```

## 2. App Service Scaling

```mermaid
flowchart LR
    Monitor[CPU / Queue Depth] --> Rule[Autoscale Rule]
    Rule --> ScaleOut[Add instances]
    Rule --> ScaleIn[Remove instances]
    ScaleOut --> Plan[App Service Plan]
```

## 3. Deployment Slots

```mermaid
sequenceDiagram
    participant Dev
    participant Staging as Staging Slot
    participant Prod as Production Slot

    Dev->>Staging: Deploy v2
    Dev->>Staging: Warm-up / smoke tests
    Dev->>Prod: Swap slots
    Note over Prod: Instant cutover + rollback via swap back
```

## 4. Container Apps — Dapr Sidecar

```mermaid
flowchart LR
    subgraph Pod
        App[.NET API]
        Dapr[Dapr Sidecar]
    end
    App <--> Dapr
    Dapr --> SB[Service Bus]
    Dapr --> State[State Store]
```

## 5. AKS Ingress Path

```mermaid
flowchart LR
    Internet --> AGIC[App Gateway Ingress]
    AGIC --> Svc[Kubernetes Service]
    Svc --> Pod1[Pod]
    Svc --> Pod2[Pod]
```

## Practice Exercise

When would you choose Container Apps over App Service for a .NET 8 microservice with KEDA scaling on Service Bus queue depth?

---

[← Back to Week 10](../README.md)
