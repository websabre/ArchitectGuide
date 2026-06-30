# Week 08 — PostgreSQL Architecture Diagrams

## 1. MVCC Read Consistency

```mermaid
sequenceDiagram
    participant T1 as Txn A
    participant T2 as Txn B
    participant Heap

    T1->>Heap: UPDATE row v1 to v2
    Note over Heap: v1 kept until Txn A commits
    T2->>Heap: SELECT sees v1
    T1->>Heap: COMMIT
    T2->>Heap: SELECT still v1 snapshot
```

## 2. Streaming Replication

```mermaid
flowchart LR
    Primary[(Primary PG)] -->|WAL stream| Replica1[(Hot Standby)]
    Primary -->|async| Replica2[(Read Replica)]
    App[.NET Npgsql] --> PgBouncer[PgBouncer]
    PgBouncer --> Primary
    Reader[Report Svc] --> Replica2
```

## 3. JSONB Document Model

```mermaid
flowchart TB
    Table[products] --> Col[id uuid]
    Table --> Json[attributes jsonb]
    Json --> GIN[GIN Index on attributes]
```

## 4. Vacuum / Bloat Lifecycle

```mermaid
flowchart TD
    Update[UPDATE creates new row version] --> Dead[Dead tuples accumulate]
    Dead --> Autovac[Autovacuum]
    Autovac --> Reclaim[Space reclaim + freeze xid]
```

## 5. Migration from SQL Server

```mermaid
flowchart LR
    SS[SQL Server] --> DMS[Azure DMS / pgloader]
    DMS --> PG[(PostgreSQL)]
    App[EF Core] --> Dual[Dual-write window]
    Dual --> Cutover[DNS cutover]
```

## Practice Exercise

Explain why long-running transactions block vacuum. Design read/write split for 500 RPS API.

---

[← Back to Week 08](../README.md)
