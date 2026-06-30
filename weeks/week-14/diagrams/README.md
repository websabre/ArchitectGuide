# Week 14 — Azure Security Architecture Diagrams

## 1. Defense in Depth

```mermaid
flowchart TB
    Edge[WAF / Front Door] --> Id[Entra ID + MFA]
    Id --> Net[NSG + Private Link]
    Net --> App[App Hardening]
    App --> Data[Encryption CMK]
    Data --> Monitor[Defender + Sentinel]
```

## 2. Key Vault — CMK for SQL

```mermaid
sequenceDiagram
    participant SQL as Azure SQL
    participant KV as Key Vault
    participant MI as Managed Identity

    SQL->>MI: Authenticate
    MI->>KV: Wrap/unwrap DEK
    KV-->>SQL: Key material
```

## 3. Zero Trust Request Flow

```mermaid
flowchart LR
    User --> MFA[MFA Verified]
    MFA --> CA[Conditional Access]
    CA --> Token[JWT with risk score]
    Token --> API[API Policy Check]
```

## 4. Secret Rotation

```mermaid
flowchart LR
    KV[Key Vault] --> App[App Service Refs]
    Rot[Rotation Function] --> KV
    App -->|reload on next access| KV
```

## 5. Threat Detection Pipeline

```mermaid
flowchart LR
    Logs[App Insights / Activity Log] --> Sentinel[Microsoft Sentinel]
    Sentinel --> Playbook[Logic App Playbook]
    Playbook --> Ticket[ServiceNow]
```

## Practice Exercise

Map OWASP API Top 10 controls to Azure services for a public .NET API.

---

[← Back to Week 14](../README.md)
