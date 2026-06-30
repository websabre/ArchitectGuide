# Month 2 Top 50 — Part 2 (Q018–Q050)

> SQL Server, PostgreSQL & Scenarios | [Part 1](month-02-top-50-part1.md) | [Index](month-02-top-50-index.md)

---

## Q018: Execution Plan Analysis

| **Week** | 07 | **Category** | SQL Server |

### Question
How do you read a SQL Server execution plan? What red flags do you look for?

### Short Answer (30 seconds)
Look for scans vs seeks, key lookups, sorts, hash matches, spills to tempdb, and high cost operators. Index seek on WHERE/JOIN columns is ideal.

### Detailed Answer
**Red flags:** Table scan on large table, key lookup (bookmark lookup) after index seek, sort operator on large dataset, warning icons (implicit conversion, missing index), high estimated vs actual rows (stale stats).

**Architect workflow:** Capture plan for top 10 slow queries weekly. Missing index DMV for recommendations.

---

## Q019: Partitioning Large Tables

| **Week** | 07 | **Category** | SQL Server |

### Question
When and how would you partition a 500M row SQL Server table?

### Short Answer
Partition by date range for archival (sliding window), manageability, and partition elimination in queries. Not a magic performance fix for all queries.

### Detailed Answer
Partition function on `OrderDate` monthly. Switch out old partitions to archive table instead of DELETE. Queries with `WHERE OrderDate > X` eliminate old partitions.

**Trade-off:** Cross-partition queries gain nothing. Operational complexity increases.

---

## Q020: TempDB Contention

| **Week** | 07 | **Category** | SQL Server |

### Question
What causes tempDB contention and how do you fix it?

### Short Answer
Heavy use of temp tables, sorts, hash joins spilling to tempdb. Multiple data files (1 per CPU core up to 8), proper sizing, fast storage (SSD).

---

## Q021: Connection Pooling

| **Week** | 07, 08 | **Category** | Database |

### Question
Explain connection pooling. What happens when pool is exhausted?

### Short Answer
ADO.NET/EF Core reuses open connections. Pool exhausted → timeout waiting for connection. Fix: reduce connection hold time, increase pool max (carefully), fix connection leaks, use PgBouncer for PostgreSQL.

### Detailed Answer
**Leak symptom:** `Timeout expired. The timeout period elapsed...` under load. **Fix:** Ensure `await using` on connections, don't hold connections across async gaps unnecessarily.

---

## Q022: Read Replica Lag

| **Week** | 07, 08 | **Category** | Database HA |

### Question
How do you handle read replica lag in application design?

### Short Answer
Route only tolerant reads to replica (reports, analytics). After write, read from primary (read-your-writes) or use session flag. Display "data may be delayed" if needed.

---

## Q023: pgvector for RAG

| **Week** | 08 | **Category** | PostgreSQL / AI |

### Question
When use PostgreSQL pgvector vs dedicated vector database?

### Short Answer
pgvector for small-medium RAG (< 1M vectors), existing Postgres ops team, simpler architecture. Dedicated (Pinecone, Azure AI Search) for large scale, hybrid search, managed ops.

---

## Q024: Database Migration Zero Downtime

| **Week** | 07, 08 | **Category** | Migration |

### Question
Outline zero-downtime schema migration for production database.

### Short Answer
Expand-contract pattern: add new column (nullable), dual-write, backfill, switch reads, remove old column. Tools: Flyway, Liquibase, EF migrations with care.

### Detailed Answer
**Never:** `ALTER COLUMN` blocking on 100M row table without strategy. **Use:** Online index operations, phased deployments, feature flags.

---

## Q025: CQRS Read Model from SQL

| **Week** | 08 | **Category** | Architecture |

### Question
When separate read database from write database?

### Short Answer
Read/write ratio > 10:1, different optimization needs, search requirements (Elasticsearch), or team scale. Accept eventual consistency on reads.

---

## Q026: Heap vs Clustered Index Table

| **Week** | 07 | **Category** | SQL Server |

### Question
When would a heap (no clustered index) be acceptable?

### Short Answer
Rarely in production OLTP. Staging tables, bulk load intermediate tables, append-only logs where range scans never happen. Generally: always have clustered index.

---

## Q027: Covering Index Design

| **Week** | 07 | **Category** | SQL Server |

### Question
Design covering index for: `SELECT Id, Total, Status FROM Orders WHERE CustomerId = @id ORDER BY CreatedAt DESC`

### Short Answer
`CREATE INDEX IX_Orders_CustomerId ON Orders(CustomerId, CreatedAt DESC) INCLUDE (Total, Status)` — seek on CustomerId, sorted order, all columns covered.

---

## Q028: Deadlock Handling

| **Week** | 07 | **Category** | SQL Server |

### Question
How do architects minimize deadlocks?

### Short Answer
Consistent lock ordering across transactions, short transactions, appropriate isolation level (READ COMMITTED SNAPSHOT), retry logic for victim, avoid user interaction inside transactions.

---

## Q029: Isolation Levels

| **Week** | 07, 08 | **Category** | Transactions |

### Question
Compare READ COMMITTED, REPEATABLE READ, SERIALIZABLE, SNAPSHOT.

### Short Answer
Higher isolation = more consistency, more blocking/less concurrency. SNAPSHOT (RCSI) uses row versioning — readers don't block writers. Default READ COMMITTED usually sufficient.

---

## Q030: Data Archival Strategy

| **Week** | 07 | **Category** | Data Lifecycle |

### Question
Design archival for 10-year order history, queries only on last 2 years.

### Short Answer
Partition by year, switch old partitions to archive table/S3 Parquet, keep hot data on fast storage. Azure SQL elastic pool or Synapse for analytics on archive.

---

## Q031–Q040: Quick Reference (Intermediate)

| Q# | Topic | Short Answer |
|----|-------|--------------|
| Q031 | Skip list | Redis sorted sets; O(log n) concurrent access |
| Q032 | Trie | Autocomplete, IP routing prefix match |
| Q033 | Priority queue | Task scheduling, Dijkstra, top-K |
| Q034 | Amortized analysis | Dynamic array insert; burst vs sustained cost |
| Q035 | Graph BFS | Shortest path unweighted, level-order |
| Q036 | Dijkstra | Weighted shortest path, maps/routing |
| Q037 | Topological sort | Build order, dependency resolution |
| Q038 | O(n log n) sorts | Merge/Tim sort — default for in-memory |
| Q039 | External sort | Billion records — chunk + k-way merge |
| Q040 | Space-time tradeoff | Cache/memory vs recompute |

---

## Q041–Q046: Expert Scenarios

## Q041: Hot Partition in Cosmos/DynamoDB

### Question
Users report throttling on one tenant with 10K writes/sec. Others fine. Root cause?

### Short Answer
Bad partition key — all writes share one partition. Fix: composite key `tenantId#shardId` with random shard suffix for hot tenants.

---

## Q042: Report Job Killing OLTP

### Question
Nightly report scans 50M rows, OLTP p99 spikes during run. Fix?

### Short Answer
Move report to read replica, materialized view, or columnstore index. Schedule off-peak. Stream to warehouse (Synapse/Redshift) for analytics.

---

## Q043: Choose DB for E-Commerce

### Question
SQL Server, PostgreSQL, or Cosmos for 5M user e-commerce?

### Short Answer
Azure SQL or PostgreSQL for orders/payments (ACID). Redis for cart. Cosmos optional for product catalog if schema varies wildly. Search: AI Search/Elasticsearch.

---

## Q044: DSA in System Design Interview

### Question
"Design a leaderboard for 10M users with real-time score updates."

### Short Answer
Redis Sorted Set (ZSET) — O(log N) insert, O(1) rank query. `ZADD leaderboard score userId`. Shard by game/season if needed.

---

## Q045: Index Over-Engineering

### Question
Table has 15 indexes, writes are slow. Architect response?

### Short Answer
Audit index usage with DMVs. Drop unused. Consolidate overlapping indexes. Every index slows INSERT/UPDATE/DELETE.

---

## Q046: Migration SQL Server to PostgreSQL

### Question
Business wants PostgreSQL for cost. 200 stored procedures. Approach?

### Short Answer
Assess with migration tool (DMA, pgloader). Rewrite T-SQL procedures — major effort. Consider phased: new services on PostgreSQL, legacy stays SQL Server.

---

## Q047–Q050: Capstone Scenarios

## Q047: Capacity — Can This Query Scale?

**Scenario:** `SELECT * FROM Orders WHERE Status = 'Pending'` — 50M rows, 500 RPS.

**Answer:** Table scan disaster. Index on `Status` (low cardinality — maybe filtered index `WHERE Status = 'Pending'`). Better: status queue table or partition by status.

## Q048: FinOps — Database Cost

**Answer:** Right-size DTU/vCore, reserved capacity, archive cold data, elastic pool for multi-tenant, delete unused replicas.

## Q049: Interview Whiteboard — Design URL Shortener Data Layer

**Answer:** Base62 encoded counter or random 7-char string. Redis cache hot URLs. SQL/NoSQL persistence. 301 redirect. ~36^7 = 78 billion URLs.

## Q050: Month 2 Integration Question

**Question:** "You're architect for new .NET platform. Choose data stack."

**Structured answer (FARCS):**
- **Requirements:** ACID orders, flexible catalog, 100K users year 1
- **Scale:** 500 RPS peak, 50GB data year 1
- **Reliability:** 99.9%, RPO 15 min
- **Cost:** Startup budget
- **Skills:** Team knows SQL Server

**Recommendation:** Azure SQL (primary) + Redis (cache/cart) + Blob (images). PostgreSQL valid alternative. Add search index at 100K+ products. Document ADR.

---

## Master Index

| Q# | Topic | Week |
|----|-------|------|
| Q001-Q006 | DSA fundamentals | 5-6 |
| Q007-Q010 | SQL Server core | 7 |
| Q011-Q017 | PostgreSQL + polyglot | 8 |
| Q018-Q030 | SQL advanced | 7-8 |
| Q031-Q040 | Algorithms reference | 6 |
| Q041-Q050 | Expert scenarios | 5-8 |
