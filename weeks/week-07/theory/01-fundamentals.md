# SQL Server Architecture for Solution Architects

> **Week 07** | **Module:** [sql-server](../../../modules/sql-server/README.md)

## Learning Objectives
- Design SQL Server for HA, performance, and security
- Understand storage engine and indexing at architect depth
- Plan migration to Azure SQL

---

## 1. SQL Server Storage Engine

```
┌─────────────────────────────────────┐
│           Query Processor            │
│   (Parser → Optimizer → Executor)    │
├─────────────────────────────────────┤
│           Storage Engine             │
│  B+ Tree Indexes │ Transaction Log   │
│  Data Pages (8KB) │ Buffer Pool      │
└─────────────────────────────────────┘
```

**Key concepts:**
- **Pages:** 8KB units of storage — I/O happens at page level
- **Extents:** 8 pages (64KB)
- **Buffer pool:** Memory cache of data pages — more RAM = fewer disk reads
- **Transaction log:** Sequential write, point-in-time recovery

---

## 2. Indexing Strategy

| Index Type | Use Case |
|------------|----------|
| Clustered | Table sort order — one per table (usually PK) |
| Non-clustered | Additional lookup paths |
| Covering | INCLUDE columns — avoid key lookup |
| Filtered | Partial index on subset (`WHERE IsActive = 1`) |
| Columnstore | Analytics, OLAP workloads |

**Architect rules:**
1. Every FK should be indexed
2. Composite index: equality columns first, then range
3. Avoid over-indexing — slows writes
4. Review execution plans quarterly

```sql
-- Covering index example
CREATE INDEX IX_Orders_CustomerId ON Orders(CustomerId)
    INCLUDE (OrderDate, Total);
```

---

## 3. High Availability Options

| Feature | RTO | RPO | Use Case |
|---------|-----|-----|----------|
| Always On AG | Seconds–min | Near zero | Enterprise HA + read scale |
| Failover Cluster (FCI) | Minutes | Zero (shared storage) | Instance protection |
| Log Shipping | Minutes–hours | Minutes | Budget DR |
| Replication | Varies | Varies | Reporting, geo-distribute |

**Always On Availability Groups:**
- Primary + up to 8 secondaries
- Synchronous commit: zero data loss within region
- Asynchronous: cross-region DR with small RPO
- Readable secondaries for reporting

---

## 4. Partitioning

Split large tables by range, list, or hash — manageability and query performance.

```sql
CREATE PARTITION FUNCTION pf_OrderDate (datetime)
AS RANGE RIGHT FOR VALUES ('2024-01-01', '2025-01-01');
```

**Benefits:** Partition elimination in queries, sliding window for archival, parallel operations.

---

## 5. Security Architecture

| Feature | Purpose |
|---------|---------|
| TDE | Encrypt data files at rest |
| Always Encrypted | Client-side encryption, DBA can't see plaintext |
| Row-Level Security | Tenant isolation in shared DB |
| Dynamic Data Masking | Mask PII for non-privileged users |
| Audit | Compliance logging |

**Multi-tenant SaaS:** Row-Level Security with `tenantId` predicate — `SESSION_CONTEXT` sets tenant on connection.

---

## 6. Performance Troubleshooting

1. **Execution plans** — seek vs scan, key lookups, spills to tempdb
2. **Wait statistics** — PAGEIOLATCH (I/O), LCK_M_X (blocking), CXPACKET (parallelism)
3. **Missing indexes** — DMVs: `sys.dm_db_missing_index_details`
4. **Blocking chains** — `sp_whoisactive`, deadlock graphs

**Architect:** Set performance budgets — p99 query < 50ms for OLTP. Load test before launch.

---

## 7. SQL Server vs Azure SQL Decision

| Factor | On-Prem SQL | Azure SQL |
|--------|-------------|-----------|
| Management | You | Microsoft |
| Feature parity | Full | Near-full (gaps exist) |
| Licensing | Core/CAL + SA | DTU/vCore subscription |
| HA | You configure AG | Built-in geo-replication |

**Migration path:** Assess compatibility (DMA tool), migrate schema, DMS for data, parallel run, cutover.

**Next:** [02-tuning-labs.md](02-tuning-labs.md) | Week 08 PostgreSQL
