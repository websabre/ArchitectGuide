# Week 15 — Azure Integration Patterns Diagrams

## 1. Async Messaging — Outbox

```mermaid
sequenceDiagram
    participant API
    participant DB
    participant Outbox as Outbox Worker
    participant SB as Service Bus

    API->>DB: Commit order + outbox row
    Outbox->>DB: Poll outbox
    Outbox->>SB: Publish event
    Outbox->>DB: Mark sent
```

## 2. Event Grid Fan-Out

```mermaid
flowchart LR
    Blob[Blob Upload] --> EG[Event Grid]
    EG --> Fn1[Function: Virus Scan]
    EG --> Fn2[Function: Thumbnail]
    EG --> LA[Logic App: Notify]
```

## 3. Logic Apps — Enterprise Integration

```mermaid
flowchart LR
    SB[Service Bus] --> LA[Logic App]
    LA --> SAP[SAP Connector]
    LA --> SQL[(SQL)]
```

## 4. API Management Gateway

```mermaid
flowchart LR
    Client --> APIM[API Management]
    APIM -->|rate limit JWT validate| API[Backend .NET API]
```

## 5. Saga via Service Bus Sessions

```mermaid
sequenceDiagram
    participant Orch as Orchestrator
    participant SB as Service Bus Session

    Orch->>SB: Command Reserve
    SB-->>Orch: Reply OK
    Orch->>SB: Command Charge
    SB-->>Orch: Reply FAIL
    Orch->>SB: Compensate Release
```

## Practice Exercise

Choose Event Grid vs Service Bus for order-created notifications to 5 downstream systems.

---

[← Back to Week 15](../README.md)
