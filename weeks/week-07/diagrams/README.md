# Week 07 — SQL Server Architecture Diagrams

## 1. Query Execution Path

```mermaid
flowchart LR
    SQL[SQL Query] --> Parser
    Parser --> Optimizer
    Optimizer --> Plan[Execution Plan]
    Plan --> Engine[Storage Engine]
    Engine --> Idx{Index seek?}
    Idx -->|Yes| Fast[Seek + Key Lookup]
    Idx -->|No| Scan[Table Scan]
```

## 2. Index Design — Covering Index

```mermaid
flowchart TB
    Q[SELECT OrderId Status Total WHERE CustomerId = @id]
    Q --> NC[Nonclustered Index on CustomerId INCLUDE Status Total]
    NC --> NoLookup[Key lookup avoided]
```

## 3. Isolation Levels Trade-off

```mermaid
flowchart TD
    RU[READ UNCOMMITTED] --> Dirty[Dirty reads]
    RC[READ COMMITTED] --> Default[Default - blocking writes]
    RR[REPEATABLE READ] --> Phantom[Phantom risk reduced]
    SN[SNAPSHOT] --> Version[Row versioning - readers no block]
```

## 4. Always On Availability Group

```mermaid
flowchart LR
    subgraph Primary["Primary Replica"]
        P[(SQL Primary)]
    end
    subgraph Secondary["Secondary Replicas"]
        S1[(Sync Replica)]
        S2[(Async Replica)]
    end
    App[.NET App] --> Listener[AG Listener]
    Listener --> P
    P -->|sync| S1
    P -->|async| S2
```

## 5. Partitioning Large Tables

```mermaid
flowchart TB
    Orders[Orders Table] --> P2024[Partition 2024]
    Orders --> P2025[Partition 2025]
    Orders --> P2026[Partition 2026]
```

> **Architect note:** Partition elimination requires query filter on partition key (e.g., `OrderDate`).

## Practice Exercise

Draw AG failover flow. When would you choose SNAPSHOT isolation for a reporting API?

---

[← Back to Week 07](../README.md)
