# Week 11 — Azure Data Platform Diagrams

## 1. Polyglot Persistence

```mermaid
flowchart TB
    API[.NET API] --> SQL[(Azure SQL - transactional)]
    API --> Cosmos[(Cosmos DB - session/catalog)]
    API --> Blob[Blob Storage - documents]
    API --> Cache[Redis - hot reads]
```

## 2. Cosmos DB Partition Strategy

```mermaid
flowchart LR
    Doc[Document] --> PK[Partition Key: tenantId]
    PK --> P1[Physical Partition 1]
    PK --> P2[Physical Partition 2]
```

> **Architect note:** Avoid hot partitions — shard high-traffic tenants.

## 3. Event Ingestion to Lake

```mermaid
flowchart LR
    Apps[.NET Services] --> EH[Event Hubs]
    EH --> ADLS[Data Lake Gen2]
    ADLS --> Synapse[Synapse Analytics]
```

## 4. CQRS Read/Write Split

```mermaid
flowchart LR
    Write[Write API] --> SQLW[(SQL Primary)]
    SQLW -->|CDC| Proj[Projection Worker]
    Proj --> CosmosR[(Cosmos Read Model)]
    Read[Read API] --> CosmosR
```

## 5. Backup & DR for Data Tier

```mermaid
flowchart TB
    Primary[(Primary Region DB)] --> Geo[Geo-Replica]
    Primary --> PITR[Point-in-Time Restore]
```

## Practice Exercise

Design partition keys for multi-tenant SaaS orders in Cosmos DB (10K tenants, uneven sizes).

---

[← Back to Week 11](../README.md)
