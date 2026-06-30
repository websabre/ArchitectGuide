# Week 12 — Azure Identity & Integration Diagrams

## 1. Entra ID — OAuth Flow for .NET API

```mermaid
sequenceDiagram
    participant User
    participant SPA as Blazor SPA
    participant Entra as Entra ID
    participant API as .NET API

    User->>SPA: Login
    SPA->>Entra: Authorization Code + PKCE
    Entra-->>SPA: Access Token
    SPA->>API: Bearer token
    API->>API: Validate JWT + scopes
```

## 2. Managed Identity to Key Vault

```mermaid
flowchart LR
    App[App Service] --> MI[System-Assigned MI]
    MI --> KV[Key Vault Secrets]
    App --> SQL[(Azure SQL)]
    MI --> SQL
```

## 3. RBAC Layers

```mermaid
flowchart TB
    Sub[Subscription] --> RG[Resource Group]
    RG --> Res[App Service]
    Entra[Entra Group: App-Admins] -->|Role: Contributor| RG
```

## 4. Service Bus — Topics & Subscriptions

```mermaid
flowchart LR
    Pub[Order Service] --> Topic[order-events]
    Topic --> Sub1[inventory-sub]
    Topic --> Sub2[notification-sub]
    Sub1 --> Inv[Inventory Worker]
    Sub2 --> Email[Email Worker]
```

## 5. Event Grid vs Service Bus

```mermaid
flowchart TD
    A[Event type?] --> B{Ordering required?}
    B -->|Yes| SB[Service Bus Queue/Topic]
    B -->|No| EG[Event Grid fan-out]
```

## Practice Exercise

Draw identity flow for a multi-tenant API using `tenantId` claim + per-tenant Key Vault references.

---

[← Back to Week 12](../README.md)
