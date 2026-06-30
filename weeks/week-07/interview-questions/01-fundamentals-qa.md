# Week 07 — Fundamentals Interview Q&A

> Q001–Q030: Premium format (Week 1 quality).
> See also: [Interview prep hub](../../../interview-prep/README.md)

---


## Q001: Clustered vs Non-Clustered Index

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Indexing |
| **Frequency** | Very Common |

### Question

Explain clustered vs non-clustered indexes in SQL Server. How do you decide?

### Short Answer (30 seconds)

Clustered index defines physical row order (one per table). Non-clustered is separate structure with pointer to row. Cluster on primary access path — usually PK or most common range query column.

### Detailed Answer (3–5 minutes)

**Clustered:** Table data IS the leaf level of the index. Range scans on clustered key are sequential I/O — fast.

**Non-clustered:** Separate B-tree with row locator (RID or clustered key). Covering index includes all query columns — avoids key lookup.

**Architect decisions:**
- OLTP: clustered on PK (GUID clustered bad — random inserts fragment)
- Wide table many queries: multiple non-clustered with careful write overhead
- Reporting: columnstore index (different structure) for analytics

**Anti-pattern:** GUID clustered PK on high-insert table — page splits, fragmentation.

### Architecture Perspective

Index strategy drives write amplification and read latency at scale.

### Follow-up Questions

1. **INCLUDE columns? — Covering index avoids lookup — trade storage for read speed.**
2. **Filtered index? — Index subset of rows — smaller, faster for sparse queries.**

### Common Mistakes in Interviews

- Clustered index on random GUID PK
- Index every column — write throughput dies
- No index maintenance plan (rebuild/reorganize)

---

## Q002: Execution Plans and Query Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Performance |
| **Frequency** | Very Common |

### Question

How do architects approach slow queries in production SQL Server?

### Short Answer (30 seconds)

Capture plan with Query Store or Extended Events, identify scans/seeks/hash spills, fix with indexes or rewrite. Set baseline p95 latency SLO per critical query.

### Detailed Answer (3–5 minutes)

**Process:**
1. Identify top CPU/duration queries (Query Store)
2. Analyze plan — table scan, key lookup, sort, hash match warnings
3. Fix: index, rewrite JOIN order, split query, archive old data
4. Verify with plan regression tests

**Architect:** Mandate Query Store enabled on all prod databases. Block deployments causing plan regressions.

Parameter sniffing: same query different plans for different parameter values — `OPTION (RECOMPILE)` or `OPTIMIZE FOR UNKNOWN` strategically.

### Architecture Perspective

Query tuning is ongoing architecture — not one-time DBA task.

### Follow-up Questions

1. **Key lookup cost? — For each NC index match, fetch row from clustered — expensive at scale.**
2. **When split read/write? — Read replicas for reporting queries over 500ms.**

### Common Mistakes in Interviews

- Tuning without measuring production workload
- Hint-heavy SQL instead of proper indexes
- Ignoring parameter sniffing on critical SP

---

## Q003: Isolation Levels

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Transactions |
| **Frequency** | Very Common |

### Question

Compare SQL Server isolation levels. What would you use for a financial ledger?

### Short Answer (30 seconds)

Read Committed default. Serializable strongest but deadlocks. Snapshot (RCSI) good for read-heavy with acceptable staleness. Financial ledger: Serializable or Repeatable Read for critical sections + app-level idempotency.

### Detailed Answer (3–5 minutes)

| Level | Dirty Read | Non-repeatable | Phantom |
|-------|------------|----------------|--------|
| Read Uncommitted | Yes | Yes | Yes |
| Read Committed | No | Yes | Yes |
| Repeatable Read | No | No | Yes |
| Serializable | No | No | No |
| Snapshot (RCSI) | No | No* | No* |

*Uses row versioning — readers don't block writers.

**Ledger:** Strong consistency on balance updates — often Serializable range locks on account row + optimistic concurrency (`rowversion`).

### Architecture Perspective

Wrong isolation causes double-spend bugs or excessive blocking.

### Follow-up Questions

1. **RCSI vs Snapshot isolation? — RCSI statement-level; Snapshot transaction-level consistent view.**
2. **Deadlock handling? — Retry with exponential backoff; consistent lock order.**

### Common Mistakes in Interviews

- Read Uncommitted in production for 'speed'
- Serializable everywhere — deadlock storm
- Ignoring rowversion for optimistic concurrency

---

## Q004: Partitioning Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Scale |
| **Frequency** | Common |

### Question

When and how do you partition large SQL Server tables?

### Short Answer (30 seconds)

Partition when table exceeds manageable maintenance size (100M+ rows) or need sliding window archive. Range partition on date common — switch partitions in/out for archive.

### Detailed Answer (3–5 minutes)

**Benefits:** Partition elimination in queries (scan one month not all history), fast archive via `SWITCH PARTITION`, parallel maintenance.

**Keys:** Partition function on `CreatedDate` monthly; align indexes.

**Architect:** Partitioning adds complexity — don't partition 10M row table prematurely. Use when backup/restore per partition or archive SLA requires it.

### Architecture Perspective

Partitioning is operational architecture for data lifecycle.

### Follow-up Questions

1. **Partition alignment? — Indexes must align on same key for switch.**
2. **Cross-partition queries? — Defeat elimination — design queries to filter on partition key.**

### Common Mistakes in Interviews

- Partitioning without query filter on key
- Too many partitions — metadata overhead
- Partition key not in most queries

---

## Q005: Always On Availability Groups

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | HA/DR |
| **Frequency** | Very Common |

### Question

Design SQL Server HA with Always On AG. RPO/RTO considerations?

### Short Answer (30 seconds)

Synchronous replica in same region — RPO=0, automatic failover. Async cross-region — RPO>0 (seconds lag), manual or automatic failover for DR.

### Detailed Answer (3–5 minutes)

**Architecture:**
- Primary + sync secondary (same AZ/region) for HA
- Async replica in DR region for geo
- Listener for app connection string
- Quorum: cloud witness (blob) or file share witness

**RTO:** Failover ~30-120 seconds depending on recovery. **RPO:** Sync = 0; async = replication lag.

.NET apps: connection string `MultiSubnetFailover=True`, retry logic for transient errors.

### Architecture Perspective

Database HA is architect-owned NFR — apps must handle failover.

### Follow-up Questions

1. **Readable secondary? — Offload reporting — watch lag for stale reads.**
2. **Distributed AG? — Cross-domain/geo — more complex topology.**

### Common Mistakes in Interviews

- Single instance for production payment DB
- No app retry on failover transient errors
- Async replica assumed RPO=0

---

## Q006: TempDB Contention

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Performance |
| **Frequency** | Occasional |

### Question

What causes tempdb contention and how do you mitigate it?

### Short Answer (30 seconds)

Tempdb shared by all databases — version store (RCSI), sorts, spools, temp tables. Contention on allocation pages (SGAM/PFS) at high concurrency.

### Detailed Answer (3–5 minutes)

**Mitigations:**
- Multiple tempdb data files (1 per CPU core up to 8)
- Right-size memory reduce spills to tempdb
- Reduce RCSI if version store huge
- Trace flags for allocation contention (legacy)

**Architect:** Monitor tempdb growth and latency — spikes correlate with bad queries (sort warnings in plan).

### Architecture Perspective

Tempdb is silent bottleneck in busy SQL estates.

### Follow-up Questions

1. **Sort warning in plan? — Data spilling to tempdb — increase memory grant or index.**
2. **Temp tables vs table variables? — Temp tables stats help optimizer — table variables often row estimate 1.**

### Common Mistakes in Interviews

- Ignoring tempdb in capacity planning
- Single tempdb file on 32-core server
- RCSI without version store monitoring

---

## Q007: Deadlock Analysis

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Concurrency |
| **Frequency** | Common |

### Question

How do you diagnose and prevent deadlocks in SQL Server?

### Short Answer (30 seconds)

Extended Events `xml_deadlock_report`, analyze cycle graph, fix lock order. App: retry transient deadlock error 1205. Design: consistent access order, shorten transactions.

### Detailed Answer (3–5 minutes)

**Prevention:**
1. Access tables in same order across SPs
2. Keep transactions short — no external API calls inside txn
3. Use snapshot isolation where appropriate
4. Appropriate index reduces lock footprint

**Architect:** Deadlocks indicate design issue — not just 'SQL problem.' Review transaction boundaries in application layer.

### Architecture Perspective

Deadlocks bridge DBA and application architecture.

### Follow-up Questions

1. **Lock escalation? — Row locks → table lock — use `ROWLOCK` hints sparingly or partition.**
2. **Application retry on 1205? — Standard pattern with max retries.**

### Common Mistakes in Interviews

- Long transactions holding locks during HTTP calls
- Inconsistent table access order across services
- Ignoring deadlock graph in incident review

---

## Q008: Columnstore Indexes

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Analytics |
| **Frequency** | Common |

### Question

When use columnstore vs rowstore in SQL Server?

### Short Answer (30 seconds)

Columnstore for analytical scans aggregating millions of rows (DW, reporting). Rowstore for OLTP point lookups and small range queries.

### Detailed Answer (3–5 minutes)

**Columnstore:** Compresses columns, batch mode execution — 10x faster for aggregations. **NCCI** on OLTP for hybrid analytics.

**Architect:** Separate reporting workload to read replica with columnstore vs mixing heavy analytics on OLTP primary.

### Architecture Perspective

Right index type for workload separates OLTP from analytics architecture.

### Follow-up Questions

1. **CCI vs NCCI? — Clustered columnstore for DW fact tables; nonclustered on OLTP for selective analytics.**
2. **Batch mode? — Vectorized execution — requires columnstore segment.**

### Common Mistakes in Interviews

- Columnstore on tiny OLTP tables
- Heavy analytics on primary OLTP without replica
- No compression maintenance on columnstore

---

## Q009: Connection Pooling

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | .NET + SQL |
| **Frequency** | Very Common |

### Question

How should .NET applications manage SQL Server connections?

### Short Answer (30 seconds)

Always use connection pooling (default in SqlConnection). Pool per connection string. Set appropriate `Max Pool Size`, timeout, retry. Never open connection per row.

### Detailed Answer (3–5 minutes)

**Architect standards:**
- One connection string config via Key Vault
- `Microsoft.Data.SqlClient` with AAD auth where possible
- Polly retry for transient faults (error 40613, 40197, 40501)
- `Min Pool Size` for warm pools on high-traffic APIs

**Anti-pattern:** `Pooling=false` — exhausts SQL connections under load.

### Architecture Perspective

Connection exhaustion takes down entire API farm.

### Follow-up Questions

1. **DbContext lifetime? — Scoped per request in ASP.NET — never singleton.**
2. **MARS disabled why? — Multiple active result sets complicate pooling — usually off.**

### Common Mistakes in Interviews

- New connection per query
- Singleton DbContext in web app
- No transient fault handling on Azure SQL

---

## Q010: SQL Server vs Azure SQL Decision

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Cloud |
| **Frequency** | Very Common |

### Question

When SQL Server on VM vs Azure SQL Database vs Managed Instance?

### Short Answer (30 seconds)

Azure SQL DB: PaaS, single DB scale, serverless dev. Managed Instance: near 100% SQL Server compatibility, instance scope. VM: full control, licensing, legacy extensions.

### Detailed Answer (3–5 minutes)

| Option | Best For |
|--------|----------|
| Azure SQL Database | New cloud-native apps, elastic scale |
| SQL Managed Instance | Lift-and-shift needing linked server, agent |
| SQL on VM | Legacy, custom extensions, full OS control |

**Architect:** Start Azure SQL DB Hyperscale for large OLTP unless MI feature required. Document compatibility matrix in ADR.

### Architecture Perspective

Cloud SQL choice affects ops burden and feature availability for years.

### Follow-up Questions

1. **Hyperscale when? — Large OLTP >4TB or fast scale requirements.**
2. **DTU vs vCore? — vCore for production — predictable CPU/memory.**

### Common Mistakes in Interviews

- SQL VM without HA configuration
- MI for simple new app — overkill
- Ignoring Azure SQL firewall/private endpoint

---

## Q011: Non-Clustered Covering Index

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Indexing |
| **Frequency** | Very Common |

### Question

Design a non-clustered covering index for a high-volume order lookup query. What goes in the key vs INCLUDE?

### Short Answer (30 seconds)

Key columns: equality and range predicates in WHERE/JOIN order. INCLUDE: SELECT columns only — avoids key lookup. Covering index serves query entirely from NC index leaf.

### Detailed Answer (3–5 minutes)

**Example query:**
```sql
SELECT OrderId, Status, TotalAmount
FROM Orders
WHERE CustomerId = @id AND OrderDate >= @from
ORDER BY OrderDate DESC;
```

**Index:**
```sql
CREATE NONCLUSTERED INDEX IX_Orders_CustomerDate
ON Orders (CustomerId, OrderDate DESC)
INCLUDE (Status, TotalAmount);
```

**Architect rules:**
- Leading key column = most selective equality filter (`CustomerId`)
- `OrderDate` in key supports range + sort — avoids separate sort operator
- INCLUDE only columns needed — wider index = slower writes

**Verify:** Plan shows **Index Seek** + **Key Lookup absent** — `SELECT` columns in INCLUDE only.

**Trade-off:** Each NC index adds write overhead on INSERT/UPDATE — cap indexes per table via review.

### Architecture Perspective

Covering indexes are the primary tool architects use to eliminate key lookups at scale.

### Follow-up Questions

1. **When is key lookup acceptable? — Few rows returned (<100) — lookup cost negligible.**
2. **INCLUDE vs composite key? — Key affects sort/group; INCLUDE is payload only.**

### Common Mistakes in Interviews

- INCLUDE every SELECT column — bloated index
- Wrong key column order — scan instead of seek
- No plan verification after index deploy

---

## Q012: Query Execution Plan Reads

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Performance |
| **Frequency** | Very Common |

### Question

How do you interpret logical reads vs physical reads in a SQL Server execution plan?

### Short Answer (30 seconds)

Logical reads = pages read from buffer cache (8 KB pages). Physical reads = disk I/O. High logical reads on hot query = missing/wrong index or scan. Physical reads on repeat execution = memory pressure or cold cache.

### Detailed Answer (3–5 minutes)

**Reading plans:**
- **Table/Index Scan** — high reads, bad on large tables
- **Index Seek** — starts at key, reads subset
- **Key Lookup (RID/Bookmark Lookup)** — NC seek + clustered fetch per row — expensive at volume

**SET STATISTICS IO ON:**
```
Table 'Orders'. Scan count 1, logical reads 45000
```

**Architect workflow:**
1. Baseline logical reads per critical query at p95 row count
2. Compare after index change — target 10–100x reduction on scans
3. Correlate with `sys.dm_os_wait_stats` PAGEIOLATCH if physical reads dominate

**Cardinality estimates:** Wildly wrong estimates → bad join order — update statistics or use Query Store forced plan only after root-cause fix.

### Architecture Perspective

Logical reads are the architect's unit of cost — cheaper than guessing from elapsed time alone.

### Follow-up Questions

1. **Actual vs estimated rows? — >10x off signals stale stats or parameter sniffing.**
2. **Read-ahead reads? — Sequential prefetch — normal for large scans.**

### Common Mistakes in Interviews

- Tune only elapsed time ignoring IO
- Accept 50K logical reads on OLTP point query
- Force plan without measuring reads before/after

---

## Q013: Isolation Levels Deep Dive

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Transactions |
| **Frequency** | Very Common |

### Question

Walk through a money-transfer scenario under Read Committed, Repeatable Read, Serializable, and RCSI. What anomalies remain?

### Short Answer (30 seconds)

Read Committed: no dirty reads; balance can change between statements. Repeatable Read: same row stable; phantoms possible. Serializable: range locks prevent phantoms; deadlock risk. RCSI: row versions — readers don't block writers; statement-level consistency.

### Detailed Answer (3–5 minutes)

**Transfer $100 A→B under RC:**
1. Read A balance 500 ✓
2. Concurrent debit A 400 → committed
3. Read A again 100 — overdraft if app assumed 500

**Fix with app:** `UPDLOCK, HOLDLOCK` on debit row or Serializable for transfer SP only.

**RCSI:** `READ_COMMITTED_SNAPSHOT ON` — readers use tempdb version store. Writers never blocked by readers — great for read-heavy OLTP. **Cost:** tempdb version store growth; long transactions block cleanup.

**Snapshot isolation (allow_snapshot_isolation):** Transaction sees point-in-time start snapshot — good for long report inside txn.

**Architect:** Default RC + RCSI for most OLTP; escalate to Serializable only on ledger critical sections; document in ADR.

### Architecture Perspective

Isolation is a product decision — architects map financial rules to SQL semantics.

### Follow-up Questions

1. **Lost update without proper locking? — Two reads same balance both write — use rowversion optimistic concurrency.**
2. **Hint OPTIMIZE FOR SERIALIZABLE scope? — Prefer explicit isolation in procedure.**

### Common Mistakes in Interviews

- Serializable on all API calls
- RCSI without tempdb monitoring
- No rowversion on balance updates

---

## Q014: Always On AG Failover

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | HA/DR |
| **Frequency** | Very Common |

### Question

Design automatic failover for Always On AG. What must the application handle?

### Short Answer (30 seconds)

Sync replica + cluster quorum + listener. Automatic failover on node failure ~30–90s. App: `MultiSubnetFailover=True`, retry transient errors (40613, 40197), connection pool drain on failover.

### Detailed Answer (3–5 minutes)

**Topology:**
- Primary + sync secondary same region (RPO=0)
- Async DR replica (RPO = lag)
- Cloud witness or file share witness for quorum

**Failover sequence:**
1. WSFC detects node loss
2. Secondary promoted
3. Listener DNS updates to new primary
4. In-flight connections fail — **apps must retry**

**.NET pattern:**
```csharp
services.AddDbContext<AppDb>(o => o.UseSqlServer(conn,
    sql => sql.EnableRetryOnFailure(maxRetryCount: 5)));
```

**Readable secondary:** `ApplicationIntent=ReadOnly` — route reports; accept replication lag.

**Architect:** Load test failover quarterly — measure RTO against SLO.

### Architecture Perspective

Failover is an application contract — not invisible to code.

### Follow-up Questions

1. **Forced manual failover when? — Patching primary — planned failover to secondary.**
2. **Distributed AG for geo? — Chain AGs across regions — complex DR topology.**

### Common Mistakes in Interviews

- Hard-coded server name not listener
- No retry on failover during deploy
- Assume readable secondary is real-time

---

## Q015: Partitioning SWITCH

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Scale |
| **Frequency** | Common |

### Question

Explain `ALTER TABLE ... SWITCH PARTITION` for archive. What constraints must hold?

### Short Answer (30 seconds)

SWITCH moves data between aligned partitioned tables instantly — metadata operation. Staging table must match schema, indexes, check constraints, and live on same filegroup/partition scheme.

### Detailed Answer (3–5 minutes)

**Archive pattern:**
```sql
-- Staging table same structure as Orders
ALTER TABLE Orders SWITCH PARTITION 1 TO OrdersArchive PARTITION 1;
```

**Requirements:**
- Partition schemes aligned (same function)
- Indexes aligned on partition key
- CHECK constraint on staging enforces partition boundary
- No foreign keys referencing switched partition without disable

**Architect:** Monthly sliding window — new empty partition, switch old to archive, backup/drop archive partition. **Sub-second** vs DELETE millions of rows.

**Pitfall:** SWITCH to table on different filegroup without alignment fails.

### Architecture Perspective

SWITCH is how architects meet data-retention SLAs without maintenance-window DELETE.

### Follow-up Questions

1. **Split partition function? — Add boundary before SWITCH IN new month.**
2. **MERGE partition boundary? — Remove old boundary after archive dropped.**

### Common Mistakes in Interviews

- Non-aligned indexes on partitioned table
- SWITCH without matching CHECK on staging
- FK constraints blocking SWITCH

---

## Q016: Tempdb Contention Fixes

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Performance |
| **Frequency** | Common |

### Question

Production shows PFS/SGAM latch waits on tempdb. What is your remediation plan?

### Short Answer (30 seconds)

Add tempdb data files (1 per CPU up to 8), equal size/growth, right-size memory to reduce spills, tune RCSI version store, fix queries with sort/hash warnings.

### Detailed Answer (3–5 minutes)

**Diagnosis:**
```sql
SELECT * FROM sys.dm_os_wait_stats
WHERE wait_type LIKE 'PAGE%LATCH%';
```
Latch contention on allocation bitmap pages when many sessions create temp objects concurrently.

**Fix checklist:**
1. **Multiple data files** — same initial size (e.g. 8 files × 4 GB on 16-core)
2. **Uniform autogrowth** — prevent one file absorbing all growth
3. **Reduce tempdb pressure** — fix queries spilling (sort warning, hash warning in plan)
4. **RCSI audit** — version store in tempdb — long txn blocks cleanup
5. **Temp table** → table variable only when stats not needed (optimizer estimates 1 row)

**Architect:** tempdb on fast local SSD (Azure tempdb optimization on MI). Alert on tempdb data file >80% full.

### Architecture Perspective

Tempdb is shared infrastructure — architects treat it like a critical service.

### Follow-up Questions

1. **Trace flag 1118/1117 still needed? — Modern SQL reduces need — verify version docs.**
2. **Temp table indexing? — Index large temp tables used in joins.**

### Common Mistakes in Interviews

- Single 1 GB tempdb file on 32-core
- Ignore sort warnings in top queries
- Long transactions with RCSI unmonitored

---

## Q017: Deadlock Graph Analysis

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Concurrency |
| **Frequency** | Common |

### Question

How do you read a SQL Server deadlock graph and fix the root cause?

### Short Answer (30 seconds)

Extended Events `xml_deadlock_report` — victim marked with X. Cycle shows resources (key/page) and statements. Fix: consistent lock order, shorter txns, better indexes, retry 1205.

### Detailed Answer (3–5 minutes)

**Reading graph:**
- **Process nodes** — SPIDs, isolation level, statement text
- **Resource nodes** — lock type (Key, Page, Object), mode (S, X, U)
- **Cycle** — A holds R1 wants R2; B holds R2 wants R1

**Common architect fixes:**
1. **Lock order** — always update `Accounts` before `Transactions`
2. **Shrink transaction** — no HTTP call inside `BEGIN TRAN`
3. **Index** — reduce lock footprint (seek vs scan locks more rows)
4. **Snapshot** — RCSI removes reader/writer deadlocks
5. **App retry** — catch error 1205 with jittered retry (max 3)

**Not a fix:** `SET DEADLOCK_PRIORITY LOW` on reports — moves problem, doesn't solve.

### Architecture Perspective

Deadlock graphs connect application transaction design to DBA symptoms.

### Follow-up Questions

1. **Lock escalation in graph? — Row → table lock — partition or ROWLOCK hint sparingly.**
2. **Deadlock vs blocking? — Blocking is wait chain; deadlock is cycle.**

### Common Mistakes in Interviews

- Kill victim SPID as permanent fix
- Different table order in two services
- Deadlock graph never captured in prod

---

## Q018: Columnstore for Analytics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Analytics |
| **Frequency** | Common |

### Question

When deploy clustered vs nonclustered columnstore for analytics on SQL Server?

### Short Answer (30 seconds)

CCI on DW fact tables (bulk load, segment compression). NCCI on OLTP for selective analytics without duplicating warehouse. Batch mode execution requires columnstore segment.

### Detailed Answer (3–5 minutes)

**CCI (Clustered Columnstore):**
- Fact tables millions+ rows
- Bulk insert / minimal singleton updates
- 10x compression; segment elimination on date filters

**NCCI on OLTP:**
- Hybrid — operational reports without ETL delay
- Trade-off: NC columnstore maintenance on hot writes

**Architect pattern:**
- OLTP rowstore primary
- Nightly ETL to DW with CCI
- Or readable AG secondary with CCI for reporting

**Avoid:** CCI on small dimension tables — rowstore + B-tree faster for lookups.

### Architecture Perspective

Columnstore placement separates OLTP path from analytics path.

### Follow-up Questions

1. **Tuple mover? — Closed rowgroups — rebuild if too many open deltas.**
2. **Batch mode on rowstore? — Limited — columnstore is the analytics enabler.**

### Common Mistakes in Interviews

- CCI on high-update OLTP table
- Analytics on primary without replica
- No segment health monitoring

---

## Q019: Connection Pooling Sizing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | .NET + SQL |
| **Frequency** | Very Common |

### Question

How do you size `Max Pool Size` and SQL Server `max connections` for a .NET API farm?

### Short Answer (30 seconds)

Pool size ≈ (instances × pool max) < SQL max connections − headroom. Default 100 per connection string. Size from concurrent requests × avg query duration, not thread count.

### Detailed Answer (3–5 minutes)

**Formula (starting point):**
```
Required connections ≈ RPS × avg_query_seconds × safety_factor
```
Example: 500 RPS × 0.02s × 2 = 20 concurrent — pool 50–100 sufficient per instance.

**Architect checklist:**
- One pool per unique connection string (different DB = different pool)
- `Min Pool Size` warm pool for burst APIs
- `Connection Timeout=30` — fail fast don't hang
- **Never** `Pooling=false`
- EF Core: scoped DbContext — one connection per request typically

**Azure SQL:** DTU/vCore tier caps connections — validate tier before scaling instances.

**Monitor:** `sys.dm_exec_connections`, app `NumberOfActiveConnectionPools`.

### Architecture Perspective

Connection math prevents the silent 'server max connections' outage.

### Follow-up Questions

1. **DbContext pool vs connection pool? — DbContext pool reuses context; still uses SqlConnection pool underneath.**
2. **MARS impact? — Multiple active result sets — rarely needed; disable.**

### Common Mistakes in Interviews

- 10 instances × default 100 pool > SQL limit
- Singleton DbContext on web API
- No alert on connection exhaustion

---

## Q020: Parameter Sniffing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Performance |
| **Frequency** | Very Common |

### Question

Explain parameter sniffing and your escalation ladder for fixing bad plans.

### Short Answer (30 seconds)

Optimizer compiles plan using first parameter values — great for one shape, catastrophic for another. Fix: statistics, indexes, rewrite; last resort: `OPTIMIZE FOR`, `RECOMPILE`, Query Store forced plan.

### Detailed Answer (3–5 minutes)

**Symptom:** Same SP fast for `@id=1` (one row), slow for `@id` rare (millions) — plan optimized for wrong cardinality.

**Escalation ladder:**
1. **Index** — eliminate scan regardless of parameter
2. **Update statistics** with full scan on skewed column
3. **`OPTION (RECOMPILE)`** — compile per execution — CPU cost
4. **`OPTIMIZE FOR (@id UNKNOWN)`** — average plan
5. **Query Store forced plan** — after A/B validation only
6. **Local variable / dynamic SQL** — sometimes helps — test carefully

**Architect:** Ban plan hints without documented incident ticket. Enable Query Store on all prod DBs — catch regressions on deploy.

### Architecture Perspective

Parameter sniffing is why 'works in dev, fails in prod' on stored procedures.

### Follow-up Questions

1. **Local variable sniffing? — Assign param to local — sometimes different estimate.**
2. **Query Store wait stats? — Identify plans with regression after release.**

### Common Mistakes in Interviews

- OPTIMIZE FOR hint as first fix
- No Query Store on production
- Ignore skewed column statistics

---

## Q021: Statistics Auto-Update

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Performance |
| **Frequency** | Common |

### Question

How do SQL Server statistics affect plans and when override auto-update?

### Short Answer (30 seconds)

Statistics histograms drive cardinality estimates. Auto-update async (2014+) reduces blocking. Override: manual UPDATE STATISTICS on large tables post bulk load; incremental stats on partitioned tables.

### Detailed Answer (3–5 minutes)

**Auto-update triggers:**
- SQL Server tracks modification counter vs rowcount threshold
- Stale stats → scan instead of seek, bad join order, hash spills

**Architect practices:**
```sql
UPDATE STATISTICS Orders WITH FULLSCAN;
-- Or incremental on partitioned:
UPDATE STATISTICS Orders PARTITION 3;
```
- Post ETL bulk load: manual stats update job
- `AUTO_UPDATE_STATISTICS_ASYNC ON` for OLTP — compile with old stats, update in background
- Monitor: `sys.dm_db_stats_properties` — modification_count vs rows

**Filtered indexes** need separate statistics on filter column.

### Architecture Perspective

Statistics hygiene is preventive architecture — cheaper than firefighting bad plans.

### Follow-up Questions

1. **Auto_create_statistics off? — Rare — leave on unless proven harm.**
2. **Stats on computed columns? — Needed if queried.**

### Common Mistakes in Interviews

- Rebuild index without updating stats
- Bulk load Friday no stats job
- Never check modification_count

---

## Q022: Index Maintenance Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Operations |
| **Frequency** | Common |

### Question

Design index maintenance for a 2TB OLTP database. Rebuild vs reorganize?

### Short Answer (30 seconds)

Reorganize online for 5–30% fragmentation; rebuild for >30% or legacy editions. Partition-level maintenance; avoid full nightly rebuild all indexes.

### Detailed Answer (3–5 minutes)

**Ola Hallengren pattern** (industry standard):
- `IndexOptimize` procedure — thresholds per index
- **Reorganize:** online, log-light, mild fragmentation
- **Rebuild:** `ONLINE=ON` (Enterprise) — heavier but fixes fragmentation + updates stats

**Architect rules:**
- Maintain hot indexes weekly; cold indexes monthly
- **Don't** rebuild every index nightly — IO storm
- Align with backup window — log growth during rebuild
- Columnstore: `REORGANIZE`/`REBUILD` for open rowgroups

**Azure SQL:** Auto-tuning may recommend — review before auto-apply in prod.

### Architecture Perspective

Index maintenance is capacity planning — not religion about nightly rebuild.

### Follow-up Questions

1. **Fill factor when? — Reduce page splits on random insert keys — not default 100 on GUID PK.**
2. **Fragmentation on SSD? — Less seek penalty — maintain less aggressively than HDD era.**

### Common Mistakes in Interviews

- REBUILD ALL every night
- No fragmentation monitoring
- Maintenance during peak traffic

---

## Q023: Query Store Regression

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Performance |
| **Frequency** | Very Common |

### Question

Query Store shows plan regression after deploy. What is your response?

### Short Answer (30 seconds)

Identify regressed query in Query Store, compare plans, force last good plan short-term, fix root cause (stats, index, code), remove force after fix verified.

### Detailed Answer (3–5 minutes)

**Workflow:**
1. Query Store → Regressed Queries report post-deploy
2. Compare plans: operator change (seek→scan), CE version change
3. **Emergency:** `sp_query_store_force_plan` last known good
4. **Root cause:** missing index, stats, parameter sniffing, CE upgrade
5. **Verify** under production load — unforce when fixed

**Architect:** CI gate — compare Query Store baseline in staging with production-like data volume. Block release if critical query regresses >2x duration.

**Compatibility level** change can flip CE — test before upgrade.

### Architecture Perspective

Query Store turns plan regression from mystery to managed incident.

### Follow-up Questions

1. **Query Store capture mode? — AUTO default — ALL for short debug window only.**
2. **Plan forcing persistence? — Survives restart — document forced plans.**

### Common Mistakes in Interviews

- Force plan without root-cause ticket
- Query Store OFF on production
- Upgrade compatibility without CE testing

---

## Q024: Lock Escalation Prevention

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Concurrency |
| **Frequency** | Common |

### Question

When does lock escalation happen and how do architects prevent it?

### Short Answer (30 seconds)

SQL escalates row/page locks to table lock when ~5000 locks on single statement. Prevention: partition table, index for seek, `ALTER TABLE SET LOCK_ESCALATION AUTO|DISABLE|TABLE`, shorten transactions.

### Detailed Answer (3–5 minutes)

**Symptom:** One UPDATE blocks entire table — `LCK_M_X` waits spike.

**Mitigations:**
1. **Partition** — escalation per partition not whole table
2. **Better index** — fewer rows locked per seek
3. **`LOCK_ESCALATION = AUTO`** (default) or `TABLE` for staging tables only
4. **`DISABLE`** — rare; risk memory for lock objects
5. **Batch updates** — `UPDATE TOP (1000)` loops

**Architect:** Never `DISABLE` on core OLTP without load test — 100K row locks consume memory.

**Rowlock hint** — doesn't prevent escalation alone.

### Architecture Perspective

Lock escalation turns row-level design into table-level outage.

### Follow-up Questions

1. **Partition elimination + escalation? — Locks scoped to touched partitions.**
2. **Table variable escalation? — Different rules — often fewer locks.**

### Common Mistakes in Interviews

- Single UPDATE touching 1M rows one statement
- LOCK_ESCALATION DISABLE without memory test
- No index on WHERE column in bulk update

---

## Q025: RCSI vs Snapshot Isolation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Transactions |
| **Frequency** | Common |

### Question

Compare Read Committed Snapshot Isolation vs Snapshot isolation level in SQL Server.

### Short Answer (30 seconds)

RCSI: database option, statement-level consistent reads, default for new readers. Snapshot: transaction-level point-in-time, `SET TRANSACTION ISOLATION LEVEL SNAPSHOT`, `ALLOW_SNAPSHOT_ISOLATION ON`.

### Detailed Answer (3–5 minutes)

| Feature | RCSI | Snapshot |
|---------|------|----------|
| Scope | DB-wide default RC | Per-transaction opt-in |
| Consistency | Per statement | Entire transaction |
| Version store | tempdb | tempdb |
| Update conflicts | N/A (writers block writers) | Reader-writer conflict error 3960 |

**RCSI:** Readers never block writers — default architect choice for OLTP read-heavy.

**Snapshot:** Long report sees stable snapshot — no phantoms within txn — good for consistent export.

**Both:** Version store in tempdb — monitor `sys.dm_tran_version_store`.

### Architecture Perspective

Choosing RCSI vs Snapshot is consistency-duration trade-off.

### Follow-up Questions

1. **Enable both? — Common — RCSI default + snapshot for long reads.**
2. **Version store cleanup blocked? — Find oldest active transaction.**

### Common Mistakes in Interviews

- RCSI without tempdb sizing
- Snapshot txn hours long blocking cleanup
- Confuse RCSI with Read Uncommitted

---

## Q026: Filegroup Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Storage |
| **Frequency** | Occasional |

### Question

When use multiple filegroups in SQL Server architecture?

### Short Answer (30 seconds)

Separate data filegroups for partitioning, tiered storage (hot SSD vs cold), piecemeal restore, and controlling file placement — not default single PRIMARY only at scale.

### Detailed Answer (3–5 minutes)

**Patterns:**
- **PRIMARY** — system objects
- **FG_HOT** — current year data on premium storage
- **FG_ARCHIVE** — old partitions on cheaper storage
- **FILESTREAM** filegroup for blobs

**Piecemeal restore:** Restore one filegroup while others online — enterprise DR pattern.

**Architect:** Align filegroups with partition scheme — `ON FG_2024` per year partition.

**Avoid:** Many empty filegroups without partition strategy — operational noise.

### Architecture Perspective

Filegroups are the physical layer under logical partitioning.

### Follow-up Questions

1. **Log file separate disk? — Transaction log on low-latency disk — sequential write.**
2. **Multiple data files per filegroup? — Proportional fill for IO parallelism.**

### Common Mistakes in Interviews

- Everything on PRIMARY single file
- Filegroup without partition alignment
- Archive on same tier as hot data

---

## Q027: Log File Sizing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Storage |
| **Frequency** | Common |

### Question

How do you size and manage the SQL Server transaction log?

### Short Answer (30 seconds)

Pre-size log to avoid autogrowth during peak. Size for largest bulk operation + replication/AG lag headroom. Backup log frequently in FULL recovery — log reuse depends on backup.

### Detailed Answer (3–5 minutes)

**Sizing approach:**
1. Measure log generation during peak hour (MB/min)
2. Add headroom for AG sync lag or long txn
3. Set fixed size + growth increment (e.g. 8 GB chunks not 10%)

**Recovery models:**
- **SIMPLE:** log truncates at checkpoint — dev/test
- **FULL:** log backup required — production with point-in-time restore

**Architect alerts:**
- Log >80% full
- `LOG_BACKUP` wait — AG replica not applying
- VLF count high from tiny autogrowths — rebuild log after right-size

**Never** shrink log routinely — regrows cause VLFs and perf hit.

### Architecture Perspective

Transaction log is the durability backbone — architects size it proactively.

### Follow-up Questions

1. **Log reuse wait? — `CHECKPOINT` or log backup not occurring.**
2. **Bulk-logged recovery? — Bulk load window — understand PITR gap.**

### Common Mistakes in Interviews

- Log autogrowth 10% on 100GB log
- FULL recovery without log backup job
- Shrink log file after every backup

---

## Q028: Backup Strategy FULL DIFF LOG

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | HA/DR |
| **Frequency** | Very Common |

### Question

Design backup strategy for SQL Server with RPO 15 minutes and RTO 1 hour.

### Short Answer (30 seconds)

FULL weekly, DIFF daily, LOG every 15 min. Test restore monthly. Copy backups to geo-redundant storage. AG sync replica is HA not backup substitute.

### Detailed Answer (3–5 minutes)

**Schedule example:**
| Backup | Frequency | Retention |
|--------|-----------|----------|
| FULL | Weekly Sunday | 4 weeks |
| DIFF | Daily | 7 days |
| LOG | Every 15 min | 7 days |

**RPO 15 min:** log backup interval ≤15 min.
**RTO 1 hr:** restore FULL + latest DIFF + log chain to target time — practice runbook.

**Architect:**
- `CHECKSUM` on backups — verify restore
- Immutable/offsite copy (Azure Backup, S3 Object Lock)
- **AG is not backup** — logical corruption replicates
- Encrypt backups (TDE encrypts at rest; backup encryption optional layer)

### Architecture Perspective

Backup strategy is tested restore — not backup job existence.

### Follow-up Questions

1. **Piecemeal restore? — Filegroup restore for large DB partial recovery.**
2. **Azure SQL automated backup? — PITR built-in — know retention by tier.**

### Common Mistakes in Interviews

- AG replica instead of backups
- Never test restore
- LOG backup every 6 hours with RPO 15 min claim

---

## Q029: Security TDE and Always Encrypted

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Security |
| **Frequency** | Common |

### Question

When use TDE vs Always Encrypted for SQL Server compliance?

### Short Answer (30 seconds)

TDE: encrypt data at rest transparently — DBA sees plaintext. Always Encrypted: client-side encryption — DBA/cloud admin cannot read column values.

### Detailed Answer (3–5 minutes)

**TDE:**
- Protects disk/backup theft
- Minimal app change
- Azure SQL TDE on by default
- Key in Key Vault (BYOK)

**Always Encrypted:**
- SSN, PCI columns — even sysadmin can't SELECT plaintext
- Deterministic vs randomized encryption — deterministic allows equality, weaker
- App uses Always Encrypted provider in SqlClient

**Architect matrix:**
| Threat | TDE | AE |
|--------|-----|----|
| Stolen backup file | ✓ | ✓ |
| Malicious DBA | ✗ | ✓ |
| App compromise | ✗ | ✗ (keys in app) |

Combine TDE (at-rest) + AE (sensitive columns) for defense in depth.

### Architecture Perspective

Encryption choice maps to threat model — architects document which threat each layer addresses.

### Follow-up Questions

1. **Column encryption key rotation? — AE supports rotation workflow.**
2. **Ledger tables? — Tamper-evident audit — complement encryption.**

### Common Mistakes in Interviews

- TDE alone for PCI column from DBA
- AE on all columns — query limitations
- CMK in same account as database

---

## Q030: SQL Server on VM vs Azure SQL

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Cloud |
| **Frequency** | Very Common |

### Question

Decision framework: SQL Server on Azure VM vs Azure SQL Database vs Managed Instance?

### Short Answer (30 seconds)

Azure SQL DB: new cloud-native, per-DB scale, serverless dev. MI: near 100% compatibility, instance features. VM: OS control, legacy extensions, bring-your-own-license.

### Detailed Answer (3–5 minutes)

**Decision tree:**
1. Need linked server, SQL Agent jobs, cross-DB queries? → **MI** or **VM**
2. New microservice single DB, elastic scale? → **Azure SQL DB** (Hyperscale for large OLTP)
3. Custom OS, third-party DLL, legacy? → **VM**
4. Minimize ops? → **PaaS** (DB or MI)

| Factor | SQL DB | MI | VM |
|--------|--------|----|----|
| Ops burden | Low | Medium | High |
| Feature parity | Subset | ~100% | 100% |
| Cost predictability | Per DB | Per vCore | VM + license |

**Architect:** ADR with compatibility checklist. Start Azure SQL DB unless MI feature gate. VM last resort for lift-and-shift debt.

### Architecture Perspective

Cloud SQL choice locks ops model for years — framework prevents default-to-VM.

### Follow-up Questions

1. **Hyperscale limits? — 100TB, fast scale — verify feature gaps vs MI.**
2. **Azure Arc SQL? — Hybrid management — on-prem + cloud policy.**

### Common Mistakes in Interviews

- VM for greenfield simple API
- MI when single Azure SQL DB suffices
- No private endpoint on production PaaS

---
