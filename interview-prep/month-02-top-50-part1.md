# Month 2 Top 50 — Part 1 (Q001–Q017)

> **DSA & Algorithms** | Weeks 5–6 | [Part 2](month-02-top-50-part2.md) | [Index](month-02-top-50-index.md)

---

## Q001: Hash Table for System Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Data Structures |
| **Week** | 05 |

### Question
Why are hash tables fundamental to system design? Give three production examples.

### Short Answer (30 seconds)
O(1) average lookup enables caching, sharding, and routing. Examples: Redis key-value store, CDN edge routing, database hash partitioning.

### Detailed Answer (3–5 minutes)
Hash tables map keys to values via hash function → bucket index. Average O(1) insert/lookup/delete. Collisions handled by chaining or open addressing.

**Production examples:**
1. **Distributed cache (Redis):** Key `user:session:abc123` → session JSON. Entire caching layer is hash-based.
2. **Database sharding:** `shard = hash(userId) % N` distributes users across N database nodes.
3. **Consistent hashing:** CDN and distributed caches use hash rings so adding/removing nodes minimizes key remapping.

**Architect decisions:**
- Choose shard key with high cardinality (userId, not countryCode)
- Understand worst-case O(n) when collisions cluster
- Consistent hashing when nodes dynamically join/leave

### Follow-up Questions
1. **Hash collision attack?** Adversarial keys causing O(n) — use secure hash, bounded chains.
2. **Consistent hashing vs modulo?** Modulo remaps most keys when N changes; consistent hashing remaps ~K/N keys.

### Common Mistakes in Interviews
- Only mentioning "fast lookup" without distributed systems connection
- Using low-cardinality shard keys (hot partitions)

---

## Q002: B+ Tree and Database Indexes

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Data Structures / SQL |
| **Week** | 05, 07 |

### Question
How does understanding B+ trees help you design database indexes?

### Short Answer
SQL Server and PostgreSQL indexes are B+ trees. Queries using indexed columns do O(log n) seeks instead of O(n) scans. Composite index leftmost prefix rule determines which queries benefit.

### Detailed Answer
B+ tree: balanced tree, high branching factor, optimized for disk I/O. Leaf nodes linked for range scans. Internal nodes only store keys (not data).

**Architect impact:**
- **Index seek** = B+ tree traversal → fast
- **Index scan** = read all leaf pages → slower
- **Table scan** = no useful index → O(n)

**Composite index `(tenantId, createdAt)`:**
- Fast: `WHERE tenantId = X AND createdAt > Y`
- Fast: `WHERE tenantId = X`
- Slow: `WHERE createdAt > Y` alone (no leftmost prefix)

**Design session:** For every high-traffic query, ask "does an index support this as a seek?"

### Common Mistakes
- Creating indexes without analyzing query patterns
- Too many indexes slowing writes

---

## Q003: When to Use Graph vs Relational

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Data Architecture |
| **Week** | 05 |

### Question
When would you choose a graph database over relational SQL?

### Short Answer
Deep relationship traversal (social graphs, fraud rings, knowledge graphs) where SQL requires expensive recursive joins. Use SQL for transactions; graph for relationship-heavy queries.

### Detailed Answer
| Factor | SQL | Graph (Neo4j, Cosmos Gremlin) |
|--------|-----|-------------------------------|
| Transactions | ACID excellent | Varies |
| Deep traversals | Recursive CTEs, slow at depth | Native, fast |
| Schema | Fixed | Flexible |
| Team familiarity | High (.NET shops) | Lower |

**Example:** "Friends of friends within 3 degrees" — graph DB natural. "Process order payment" — SQL.

**Architect:** Don't use graph DB because "relationships" — use when traversal performance at depth > 3 is proven bottleneck.

---

## Q004: Big-O for Architects — When It Matters

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Algorithms |
| **Week** | 06 |

### Question
As an architect, when does algorithmic complexity actually matter?

### Short Answer
When n is large at peak: millions of records, thousands of RPS, batch jobs on full datasets. Doesn't matter for typical CRUD with proper indexes. Matters for search, recommendations, routing, and capacity planning.

### Detailed Answer
**Matters:**
- Designing search (inverted index O(1) lookup vs scan O(n))
- Batch ETL on 100M rows (O(n log n) sort vs O(n²))
- Rate limiter algorithm choice
- Estimating if solution works at 10x scale

**Doesn't matter (usually):**
- Business logic with EF Core on indexed queries
- API with < 1000 items per request

**Interview framework:** "What's n at peak?" If n < 10K, optimize for maintainability. If n > 1M, analyze complexity.

### Common Mistakes
- Optimizing algorithm before profiling
- Ignoring O(n²) in nested loops over large collections in hot paths

---

## Q005: N+1 Query Problem

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | .NET / SQL |
| **Week** | 06, 07 |

### Question
Explain the N+1 query problem and how architects prevent it.

### Short Answer
Loading N parent records then 1 query per child = N+1 database round trips. Fix with eager loading (`Include`), projection, or denormalized read models.

### Detailed Answer
```csharp
// N+1: 1 query for orders + N queries for each order's lines
var orders = await _db.Orders.ToListAsync();
foreach (var order in orders)
    var lines = order.Lines; // lazy load per order
```

**Fixes:**
1. `.Include(o => o.Lines)` — single join query
2. Projection: `.Select(o => new OrderDto(...))` — only needed columns
3. CQRS read model — pre-joined denormalized view
4. DataLoader pattern (GraphQL)

**Architect:** Mandate query review in PRs. App Insights dependency tracking shows N+1 as many small SQL calls.

---

## Q006: Sorting at Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Algorithms |
| **Week** | 06 |

### Question
How would you sort 1 billion records that don't fit in memory?

### Short Answer
External merge sort: sort chunks in memory, write to disk, merge sorted runs. MapReduce/Hadoop uses similar pattern. In databases: ORDER BY uses indexes or sort operator with spill to disk.

### Detailed Answer
**External sort:**
1. Read M records into memory (fit RAM)
2. Sort in memory (O(M log M))
3. Write sorted chunk to disk
4. Repeat until all data chunked
5. K-way merge of sorted chunks

**Architect relevance:** Batch reporting, ETL pipelines, log processing. Don't load 1B rows into .NET List.

**Database:** `ORDER BY` on unindexed column → sort operator → may spill to tempdb (SQL Server) — performance disaster at scale.

---

## Q007: SQL Server Clustered vs Non-Clustered Index

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | SQL Server |
| **Week** | 07 |

### Question
Difference between clustered and non-clustered indexes in SQL Server?

### Short Answer
Clustered index defines physical row order (one per table, usually PK). Non-clustered is separate structure with pointer to row. Clustered = table; non-clustered = lookup book with page references.

### Detailed Answer
**Clustered:** Data rows stored in index order. Range scans efficient. One per table.

**Non-clustered:** B+ tree with key + row locator (RID or clustered key). Covering index includes all queried columns — avoids key lookup.

**Architect decisions:**
- PK as clustered (default) — good for range queries on Id
- Large table range queries on `CreatedAt` — consider clustered on date (rare, evaluate carefully)
- Covering indexes for hot queries — trade write overhead

---

## Q008: SQL Server Always On Availability Groups

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | SQL Server HA |
| **Week** | 07 |

### Question
Design HA for SQL Server with RPO near zero and readable secondaries.

### Short Answer
Always On AG with synchronous commit within region (zero data loss), asynchronous secondary in DR region (small RPO). Readable secondaries for reporting queries.

### Detailed Answer
**Synchronous replica:** Transaction waits for secondary ack — RPO = 0, higher latency.

**Asynchronous replica:** No wait — RPO = replication lag (seconds), lower latency.

**Readable secondaries:** Route `ApplicationIntent=ReadOnly` to secondary for reports — offload primary.

**Azure equivalent:** Azure SQL failover group with geo-secondary.

**Failover:** Automatic or manual. Test quarterly.

---

## Q009: Index Fragmentation and Maintenance

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SQL Server |
| **Week** | 07 |

### Question
How do you handle index fragmentation in production SQL Server?

### Short Answer
Monitor `sys.dm_db_index_physical_stats`. Reorganize (online, light fragmentation) or rebuild (heavy fragmentation, more disruptive). Azure SQL automates some; on-prem needs maintenance plans.

### Detailed Answer
**Fragmentation causes:** Page splits from random inserts, deletes leaving gaps.

**Thresholds (rule of thumb):**
- < 10%: ignore
- 10-30%: `ALTER INDEX REORGANIZE`
- > 30%: `ALTER INDEX REBUILD` (online edition permitting)

**Architect:** Schedule maintenance windows. Monitor tempdb during rebuilds. Consider fill factor for insert-heavy indexes.

---

## Q010: Row-Level Security for Multi-Tenant SaaS

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | SQL Server Security |
| **Week** | 07 |

### Question
Implement tenant isolation in shared SQL Server database.

### Short Answer
`tenantId` column on all tables + Row-Level Security policy filtering by `SESSION_CONTEXT('tenantId')`. EF Core sets context on connection open.

### Detailed Answer
```sql
CREATE FUNCTION dbo.fn_tenantFilter(@tenantId uniqueidentifier)
RETURNS TABLE WITH SCHEMABINDING AS
RETURN SELECT 1 AS fn_result
WHERE @tenantId = CAST(SESSION_CONTEXT(N'tenantId') AS uniqueidentifier);

CREATE SECURITY POLICY TenantFilter
ADD FILTER PREDICATE dbo.fn_tenantFilter(tenantId) ON dbo.Orders;
```

**Pros:** DB-enforced isolation, one schema. **Cons:** All queries pay filter predicate. **Alternative:** schema-per-tenant or database-per-tenant for enterprise tier.

---

## Q011: PostgreSQL MVCC

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | PostgreSQL |
| **Week** | 08 |

### Question
What is MVCC in PostgreSQL and why do architects care?

### Short Answer
Multi-Version Concurrency Control — readers don't block writers. Each transaction sees snapshot. Requires VACUUM to reclaim dead tuples. Long transactions cause bloat and wraparound risk.

### Detailed Answer
**Implications:**
- `UPDATE` creates new row version, old becomes dead tuple
- `autovacuum` reclaims space (usually automatic)
- Long-running report transaction blocks vacuum → table bloat
- Monitor `pg_stat_user_tables.n_dead_tup`

**Architect:** Connection pooling (PgBouncer), avoid long transactions, monitor bloat on high-churn tables.

---

## Q012: JSONB vs Relational Columns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | PostgreSQL |
| **Week** | 08 |

### Question
When use PostgreSQL JSONB vs normalized relational columns?

### Short Answer
JSONB for semi-structured, evolving schemas (product attributes, config, metadata). Relational for queryable, constrained, join-heavy data (orders, users, payments).

### Detailed Answer
```sql
CREATE INDEX idx_attrs ON products USING GIN (attributes jsonb_path_ops);
SELECT * FROM products WHERE attributes @> '{"color": "red"}';
```

**JSONB pros:** Schema flexibility, fast containment queries with GIN index.
**JSONB cons:** No FK constraints on nested fields, harder validation, larger storage.

**Architect:** Hybrid — core fields relational, extensible attributes JSONB.

---

## Q013: Polyglot Persistence Decision

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Data Architecture |
| **Week** | 08 |

### Question
When would you add a second database technology to your architecture?

### Short Answer
When measurable pain: read scale (add Redis), flexible schema (JSONB/NoSQL), full-text search (Elasticsearch), analytics (warehouse), or specialized queries (graph). Not on day one.

### Detailed Answer
**Decision framework:**
1. Is single PostgreSQL/SQL Server insufficient? (Prove with metrics)
2. What's the specific access pattern mismatch?
3. What's the operational cost of second store?
4. How handle cross-store consistency? (Saga, eventual consistency)

**Start:** One RDBMS. Add stores incrementally with clear ownership boundaries.

---

## Q014: PostgreSQL vs SQL Server for .NET Shop

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Database Selection |
| **Week** | 08 |

### Question
As a .NET architect, when PostgreSQL vs SQL Server?

### Short Answer
SQL Server when Microsoft stack, Entra auth, team expertise, Azure SQL integration. PostgreSQL when open source mandate, cost sensitivity, JSONB/extensions (PostGIS, pgvector), or Linux-first.

### Detailed Answer
| Factor | SQL Server | PostgreSQL |
|--------|------------|------------|
| .NET/EF Core | Excellent | Excellent (Npgsql) |
| Azure integration | Native | Good (Flexible Server) |
| Licensing | Commercial | Open source |
| JSON | JSON (2016+) | JSONB (superior indexing) |
| AI embeddings | Azure SQL vector | pgvector extension |

**Interview:** No religious war — match to requirements and team.

---

## Q015: Bloom Filters in Production

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Data Structures |
| **Week** | 05 |

### Question
What is a Bloom filter and when would you use one?

### Short Answer
Probabilistic set membership — "definitely not in set" or "probably in set". No false negatives. Use to avoid expensive lookups for items likely absent (DB, S3, CDN).

### Detailed Answer
**Example:** Before querying database for `username` availability, check Bloom filter of taken names. If filter says "not present" — definitely available. If "maybe present" — query DB to confirm.

**Trade-off:** Configurable false positive rate vs memory size. Cannot delete (use counting Bloom filter).

---

## Q016: Consistent Hashing Deep Dive

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Distributed Systems |
| **Week** | 05 |

### Question
Explain consistent hashing. Why not `hash(key) % N`?

### Short Answer
Modulo remaps nearly all keys when N changes. Consistent hashing maps keys and nodes to a ring — adding/removing one node only affects adjacent key range (~K/N keys).

### Detailed Answer
**Virtual nodes:** Each physical node has 150+ virtual positions on ring for even distribution.

**Use cases:** Memcached, Redis Cluster, Cassandra, CDN request routing, database sharding rebalancing.

**Architect:** Understand when your managed service uses it (Cosmos DB, DynamoDB) even if you don't implement it.

---

## Q017: CAP Theorem for Data Store Selection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Distributed Systems |
| **Week** | 05, 21 |

### Question
How does CAP theorem guide database selection?

### Short Answer
During partition: choose consistency (CP) or availability (AP). SQL single-node is CA until clustered. Cosmos/Dynamo tunable. Architects match choice to business requirement per data type.

### Detailed Answer
| Data | CAP choice | Store |
|------|------------|-------|
| Bank balance | CP (strong) | SQL with sync replication |
| Product catalog | AP (eventual) | Cosmos Eventual, CDN |
| Shopping cart | AP + merge | Redis, custom merge |
| Session | AP | Redis with TTL |

**PACELC:** Else choose latency vs consistency — explains DynamoDB default.

---

*Continued in [Part 2 — Q018–Q050](month-02-top-50-part2.md)*
