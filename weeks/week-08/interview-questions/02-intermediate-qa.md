# Week 08 — Intermediate Q&A

> Q031–Q070: Premium format (Week 1 quality).

---


## Q031: MVCC Vacuum Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Concurrency |
| **Frequency** | Very Common |

### Question

How do you tune autovacuum for a high-update PostgreSQL table?

### Short Answer (30 seconds)

Lower `autovacuum_vacuum_scale_factor` per table, raise `autovacuum_vacuum_cost_limit`, monitor `n_dead_tup`, set `idle_in_transaction_session_timeout`.

### Detailed Answer (3–5 minutes)

**Per-table settings:**
```sql
ALTER TABLE orders SET (
  autovacuum_vacuum_scale_factor = 0.02,
  autovacuum_analyze_scale_factor = 0.01,
  autovacuum_vacuum_cost_delay = 2
);
```

**Why:** Default scale 0.2 means vacuum after 20% dead tuples — on 100M row table that's 20M dead rows before cleanup.

**Architect monitoring:**
```sql
SELECT relname, n_dead_tup, last_autovacuum
FROM pg_stat_user_tables ORDER BY n_dead_tup DESC;
```

**Blockers:** Long transactions hold xmin — vacuum can't remove dead tuples — causes bloat.

**PgBouncer:** transaction pooling reduces idle-in-txn sessions holding snapshots.

### Architecture Perspective

Vacuum tuning is production architecture for Postgres — not optional DBA trivia.

### Follow-up Questions

1. **autovacuum_max_workers? — Increase on large instances with many tables.**
2. **Manual VACUUM ANALYZE when? — After bulk load before critical query window.**

### Common Mistakes in Interviews

- Default autovacuum on 500M row hot table
- ETL job idle in transaction 8 hours
- No alert on n_dead_tup threshold

---

## Q032: JSONB GIN Indexing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Indexing |
| **Frequency** | Very Common |

### Question

Index JSONB columns for containment queries. Which operators and index type?

### Short Answer (30 seconds)

GIN index with `jsonb_ops` (default) or `jsonb_path_ops` (smaller, `@>` only). Query with `@>`, `?`, `?&`, `?|` operators — B-tree cannot help.

### Detailed Answer (3–5 minutes)

**Create:**
```sql
CREATE INDEX idx_product_attrs ON products
USING GIN (attributes jsonb_path_ops);

-- Query uses index:
SELECT * FROM products
WHERE attributes @> '{"category": "electronics"}';
```

**jsonb_path_ops vs jsonb_ops:**
- `path_ops` — smaller index, only `@>` containment
- `jsonb_ops` — supports `?` key existence too — larger

**Architect:** Index only queried paths — not whole blob if subset hot.

**Expression index alternative:** `(attributes->>'sku')` B-tree for equality on single field.

### Architecture Perspective

JSONB indexing strategy determines whether hybrid schema scales.

### Follow-up Questions

1. **GIN pending list? — Fast insert batch — merge with vacuum.**
2. **jsonb vs JSON type? — Always JSONB for indexing and storage.**

### Common Mistakes in Interviews

- No index on hot @> queries
- jsonb_ops when only @> used — wasted size
- Huge JSONB document in every row indexed wholly

---

## Q033: GiST vs GIN Choice

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Indexing |
| **Frequency** | Common |

### Question

When choose GiST vs GIN index in PostgreSQL?

### Short Answer (30 seconds)

GIN: exact containment, arrays, full-text, JSONB — larger, slower build, fast lookup. GiST: geometric, range types, full-text (slower build, smaller), nearest-neighbor queries.

### Detailed Answer (3–5 minutes)

| Use Case | Index |
|----------|-------|
| JSONB `@>` | GIN |
| `tsvector` full-text | GIN (default) or GiST |
| PostGIS geometry | GiST |
| IP range, int4range overlap | GiST |
| Array `@>` | GIN |

**Rule of thumb:** GIN for 'contains' on static data; GiST for overlap/nearest-neighbor spatial.

**Architect:** Run `EXPLAIN ANALYZE` both ways on production-like volume — GIN build can lock writes during CREATE INDEX — use `CONCURRENTLY`.

### Architecture Perspective

Wrong index type means seq scan on million-row tables.

### Follow-up Questions

1. **BRIN vs GiST for geo? — BRIN not for point queries — GiST/SP-GiST.**
2. **SP-GiST? — Partitioned search trees — phone routing, some geo.**

### Common Mistakes in Interviews

- GiST for JSONB containment
- GIN for nearest-neighbor geo
- CREATE INDEX without CONCURRENTLY on prod

---

## Q034: Streaming Replication Slots

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | HA/DR |
| **Frequency** | Common |

### Question

What are replication slots and what happens if a replica stops consuming?

### Short Answer (30 seconds)

Slots track WAL position per consumer — prevent WAL deletion until consumed. Stopped replica with slot → WAL accumulates → disk full on primary.

### Detailed Answer (3–5 minutes)

**Physical replication slot:**
```sql
SELECT slot_name, active, pg_wal_lsn_diff(pg_current_wal_lsn(), restart_lsn) AS lag_bytes
FROM pg_replication_slots;
```

**Architect rules:**
- Monitor `lag_bytes` and `active=false`
- Drop orphaned slots after replica decommission
- `max_slot_wal_keep_size` (PG13+) — limit WAL retention
- Logical slots for logical replication — same disk risk

**Never** leave inactive slot on production without alert — classic Postgres outage cause.

### Architecture Perspective

Replication slots are durability contracts — architects monitor them like disk space.

### Follow-up Questions

1. **Temporary vs permanent slot? — Temp dies with session — prefer named permanent with monitoring.**
2. **pg_receivewal slot? — Third-party backup tools use slots.**

### Common Mistakes in Interviews

- Drop replica VM but not slot
- No alert on inactive slot
- Unlimited WAL keep with dead replica

---

## Q035: PgBouncer Transaction Mode

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Very Common |

### Question

Explain PgBouncer transaction pooling mode and ORM compatibility.

### Short Answer (30 seconds)

Transaction mode: server connection returned to pool after each transaction. Thousands of clients, tens of server connections. Breaks session-level features (prepared statements, temp tables, LISTEN).

### Detailed Answer (3–5 minutes)

**Modes:**
- **Session** — 1:1 until disconnect — compatible, less multiplexing
- **Transaction** — pool per txn — best for stateless web APIs
- **Statement** — pool per statement — rare, breaks multi-statement txn

**Npgsql + EF Core:**
- Disable prepared statements or use session mode if issues
- `Maximum Pool Size` on client still applies above PgBouncer

**Architect sizing:**
```
pgbouncer max_client_conn = 2000
pgbouncer default_pool_size = 50
postgres max_connections = 100 (reserved superuser)
```

### Architecture Perspective

Transaction pooling is mandatory architecture for Postgres at hundreds of app instances.

### Follow-up Questions

1. **Prepared statement error? — Switch session mode or `PrepareThreshold=0`.**
2. **SET search_path in transaction mode? — Must SET each transaction — or use connect query.**

### Common Mistakes in Interviews

- Session mode with 5000 app connections
- Temp tables in transaction pooling
- max_connections 500 on Postgres directly

---

## Q036: BRIN for Time-Series

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Indexing |
| **Frequency** | Common |

### Question

When use BRIN indexes for time-series data in PostgreSQL?

### Short Answer (30 seconds)

BRIN on naturally ordered column (timestamp, serial ID) — tiny index size, block-range min/max summary. Ideal append-only logs, metrics, events billions of rows.

### Detailed Answer (3–5 minutes)

**Create:**
```sql
CREATE INDEX idx_events_created ON events
USING BRIN (created_at) WITH (pages_per_range = 128);
```

**Query:**
```sql
WHERE created_at BETWEEN '2024-01-01' AND '2024-01-31'
```

**Works when:** Physical row order correlates with time (insert order). **Fails when:** Random insert order — reorder or use B-tree.

**Architect:** BRIN + declarative partitioning by month — partition pruning + BRIN per partition.

**Size:** BRIN index MB vs B-tree GB on billion-row table.

### Architecture Perspective

BRIN is the architect's secret for cheap time-range scans at scale.

### Follow-up Questions

1. **pages_per_range tuning? — Smaller = more precise, larger index.**
2. **CLUSTER on time column? — Improves BRIN correlation after bulk load.**

### Common Mistakes in Interviews

- BRIN on random UUID insert order
- B-tree on billion-row log table
- No partition + BRIN on single huge table only

---

## Q037: Expand-Contract Migrations

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Migrations |
| **Frequency** | Very Common |

### Question

Walk through expand-contract for renaming a column with zero downtime.

### Short Answer (30 seconds)

Add new column (expand) → dual-write both → backfill → switch reads → stop old writes → drop old (contract). Never rename in single deploy.

### Detailed Answer (3–5 minutes)

**Phases:**
1. **Expand:** `ADD COLUMN new_email TEXT` nullable
2. **Deploy app v2:** write both `email` and `new_email`
3. **Backfill:** `UPDATE ... SET new_email = email WHERE new_email IS NULL` batched
4. **Deploy app v3:** read `new_email`
5. **Contract:** drop `email` after all instances on v3

**Postgres:** `ADD COLUMN` with volatile default locks table — add nullable, backfill, then `SET DEFAULT`.

**Architect:** Migration pipeline blocks destructive DDL without expand-contract review.

### Architecture Perspective

Expand-contract is how architects enable continuous deployment on Postgres.

### Follow-up Questions

1. **CONCURRENTLY for indexes? — `CREATE INDEX CONCURRENTLY` during expand phase.**
2. **Flyway vs Liquibase? — Tool agnostic — process matters.**

### Common Mistakes in Interviews

- RENAME COLUMN in Friday deploy
- NOT NULL without backfill complete
- Single-phase breaking migration

---

## Q038: Partial Indexes

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Indexing |
| **Frequency** | Common |

### Question

Design partial indexes for PostgreSQL. When do they win?

### Short Answer (30 seconds)

Index subset with WHERE clause — smaller, faster, less write overhead. Ideal sparse predicates: active rows, unpaid orders, non-null subset.

### Detailed Answer (3–5 minutes)

**Example:**
```sql
CREATE INDEX idx_orders_open ON orders (customer_id)
WHERE status IN ('pending', 'processing');
```

**Wins when:**
- Query always includes same filter
- Small fraction of rows match (5–20%)
- Hot path queries only touch active subset

**Planner requirement:** Query WHERE must imply index predicate — `status = 'pending'` uses index; `status = 'shipped'` does not.

**Architect:** Document partial index predicates in data dictionary — devs must know query shape.

### Architecture Perspective

Partial indexes are free performance when workload is skewed.

### Follow-up Questions

1. **Unique partial index? — `WHERE deleted_at IS NULL` for soft-delete uniqueness.**
2. **Multiple partial indexes? — Different status values — evaluate write cost.**

### Common Mistakes in Interviews

- Partial index predicate not in queries
- Full index when 95% rows filtered out
- Forget UNIQUE constraint needs partial for soft delete

---

## Q039: Expression Indexes

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Indexing |
| **Frequency** | Common |

### Question

When create expression indexes in PostgreSQL?

### Short Answer (30 seconds)

Index on expression or function result — when queries use `LOWER(email)`, date truncation, or computed JSON path — not column directly.

### Detailed Answer (3–5 minutes)

**Examples:**
```sql
CREATE INDEX idx_users_email_lower ON users (LOWER(email));

CREATE INDEX idx_orders_month ON orders (date_trunc('month', created_at));
```

**Query must match expression exactly:**
```sql
WHERE LOWER(email) = LOWER(@input)  -- uses index
WHERE email = @input                 -- does not
```

**Architect:** Prefer generated stored column (PG12+) + B-tree if expression reused — clearer than opaque function index.

**Immutable functions only** in index — `LOWER` yes; `now()` no.

### Architecture Perspective

Expression indexes bridge app normalization and query patterns.

### Follow-up Questions

1. **Functional dependency? — PG14+ infer uniqueness on dependent cols sometimes.**
2. **jsonb path expression index? — `(data->>'type')` B-tree for equality.**

### Common Mistakes in Interviews

- Index column but query uses LOWER()
- Mutable function in index expression
- Expression mismatch — planner can't use index

---

## Q040: Declarative Table Partitioning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Scale |
| **Frequency** | Common |

### Question

Design declarative partitioning in PostgreSQL for a multi-tenant events table.

### Short Answer (30 seconds)

RANGE or LIST partition on `created_at` or `tenant_id`. PG10+ declarative — attach/detach partitions for archive. Unique constraints must include partition key.

### Detailed Answer (3–5 minutes)

**Monthly range:**
```sql
CREATE TABLE events (
  id BIGSERIAL, tenant_id INT, created_at TIMESTAMPTZ, payload JSONB,
  PRIMARY KEY (id, created_at)
) PARTITION BY RANGE (created_at);

CREATE TABLE events_2024_01 PARTITION OF events
  FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');
```

**Architect:**
- Partition key in PK and unique constraints
- `DETACH PARTITION` for archive — instant
- Default partition catches overflow — monitor
- Prune with `WHERE created_at >= ...` in every query

**pg_partman** extension automates partition creation.

### Architecture Perspective

Declarative partitioning is Postgres answer to SQL Server SWITCH — different mechanics, same lifecycle goal.

### Follow-up Questions

1. **HASH partition tenants? — Even distribution — cross-partition queries expensive.**
2. **Sub-partitioning? — RANGE then HASH — advanced multi-tenant.**

### Common Mistakes in Interviews

- PK without partition key
- No default partition — INSERT fails new month
- Queries missing partition key filter

---

## Q041: Connection Limits Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Common |

### Question

How size `max_connections` vs PgBouncer pool for PostgreSQL?

### Short Answer (30 seconds)

Postgres `max_connections` low (100–200) — process-per-connection expensive. PgBouncer multiplexes thousands of clients. Reserve `superuser_reserved_connections`.

### Detailed Answer (3–5 minutes)

**Sizing:**
```
postgres max_connections = pgbouncer default_pool_size + admin_headroom
```

**Memory:** Each connection ~5–10 MB work_mem dependent — 500 connections ≠ free.

**Architect:**
- PgBouncer between app and Postgres (or Azure Flexible Server built-in pooler)
- App connection string points to PgBouncer port 6432
- Monitor `pg_stat_activity` count vs `max_connections`
- `idle_in_transaction_session_timeout = 60s`

**Serverless burst:** Pooler essential — Lambda/container scale connections faster than Postgres accepts.

### Architecture Perspective

Connection limits are hard caps — architects design pooler-first.

### Follow-up Questions

1. **RDS/Azure connection limits? — Tier-based — upgrade or pool.**
2. **Connection leak detection? — `pg_stat_activity` state idle age.**

### Common Mistakes in Interviews

- max_connections 1000 no pooler
- Each microservice instance 100 direct connections
- No idle_in_transaction timeout

---

## Q042: EXPLAIN ANALYZE

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Very Common |

### Question

How do architects use EXPLAIN ANALYZE safely in production troubleshooting?

### Short Answer (30 seconds)

Run on representative query with ANALYZE in staging first. Production: use `EXPLAIN (ANALYZE, BUFFERS)` on isolated replica or limited window — executes query, adds overhead.

### Detailed Answer (3–5 minutes)

**Read plan:**
```sql
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
SELECT ...;
```

**Key nodes:**
- **Seq Scan** on large table — index opportunity
- **Index Only Scan** — covering index win
- **Nested Loop** with high loops — bad estimate or missing index
- **Hash Join** — build side should be smaller
- **Buffers: shared hit/read** — cache vs disk

**Architect workflow:**
1. Capture from `pg_stat_statements` top queries
2. EXPLAIN on read replica
3. Compare estimates vs actual rows
4. Fix index, stats (`ANALYZE`), or rewrite

**Never** EXPLAIN ANALYZE destructive UPDATE on prod primary without transaction rollback test.

### Architecture Perspective

EXPLAIN ANALYZE is the architect's microscope — use on replica when possible.

### Follow-up Questions

1. **auto_explain extension? — Log slow plans automatically.**
2. **Generic vs custom plan? — Prepared statement plans — use `EXPLAIN GENERIC_PLAN`.**

### Common Mistakes in Interviews

- EXPLAIN without ANALYZE and guess
- ANALYZE heavy query on primary peak
- Ignore actual vs estimated row mismatch

---

## Q043: Autovacuum Freeze

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Common |

### Question

What is transaction ID wraparound and how does autovacuum freeze prevent it?

### Short Answer (30 seconds)

Postgres 32-bit transaction IDs wrap ~2 billion. Dead tuples must be frozen to mark all-visible — autovacuum freeze reclaims XID space. Failure → database shutdown to prevent corruption.

### Detailed Answer (3–5 minutes)

**Monitor:**
```sql
SELECT datname, age(datfrozenxid) FROM pg_database;
-- Alert if age > 200M (default autovacuum_freeze_max_age 200M)
```

**Causes of freeze lag:**
- Long transactions block vacuum
- `autovacuum_freeze_max_age` too high on busy DB
- Tables never vacuumed — `n_mod_since_analyze` stale

**Architect:**
- Alert `age(datfrozenxid) > 150M`
- `idle_in_transaction_session_timeout`
- Schedule manual `VACUUM FREEZE` on catalog-heavy tables if needed

**Emergency:** `VACUUM FREEZE VERBOSE` — not `VACUUM FULL` unless bloat crisis.

### Architecture Perspective

XID wraparound is existential Postgres risk — architects monitor age, not just disk.

### Follow-up Questions

1. **multixact wraparound? — Similar risk for row locks — `pg_multixact` age.**
2. **vacuum_defer_cleanup_age? — Usually leave default — deferring increases wrap risk.**

### Common Mistakes in Interviews

- Ignore datfrozenxid age alerts
- Weekend ETL idle in transaction
- Disable autovacuum on any production table

---

## Q044: Logical Replication

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | HA/DR |
| **Frequency** | Common |

### Question

When use logical vs physical replication in PostgreSQL?

### Short Answer (30 seconds)

Physical: byte-for-byte WAL, full cluster, low lag, replica read-only. Logical: row-level, selective tables, version upgrades, CDC to external systems — more overhead.

### Detailed Answer (3–5 minutes)

**Logical replication use cases:**
- PG major version upgrade (17 → 18) with minimal downtime
- Replicate subset of tables to analytics DB
- CDC to Kafka/Debezium
- Multi-master conflict scenarios (advanced — avoid without expertise)

**Setup:**
```sql
CREATE PUBLICATION orders_pub FOR TABLE orders;
CREATE SUBSCRIPTION orders_sub CONNECTION '...' PUBLICATION orders_pub;
```

**Architect:** Logical replication slot holds WAL — monitor like physical slot. Initial sync locks source table briefly.

**Not for:** Sub-millisecond HA failover — use physical + Patroni/cloud HA.

### Architecture Perspective

Logical replication is migration and CDC architecture — not primary HA.

### Follow-up Questions

1. **Replica identity FULL? — Needed for UPDATE/DELETE without PK on all columns.**
2. **Conflict resolution? — Logical multi-master needs strategy — last-write-wins dangerous.**

### Common Mistakes in Interviews

- Logical replication for HA failover only
- No monitoring on replication lag
- Upgrade without logical replication test

---

## Q045: Citus Extension Sharding

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Scale |
| **Frequency** | Occasional |

### Question

When recommend Citus for PostgreSQL sharding?

### Short Answer (30 seconds)

Citus when single Postgres node exceeds vertical scale (CPU, storage, write throughput) and workload shards by tenant_id or distribution key — multi-tenant SaaS, real-time analytics.

### Detailed Answer (3–5 minutes)

**Distribution:**
```sql
SELECT create_distributed_table('events', 'tenant_id');
```

**Good fit:**
- Queries filter by distribution column (`tenant_id`)
- Tenant count >> single node capacity
- Azure Cosmos DB for PostgreSQL (Citus managed)

**Bad fit:**
- Cross-shard JOINs dominate
- No natural distribution key
- Small DB that fits one Flexible Server

**Architect:** Shard key is permanent architecture decision — resharding is painful. Co-locate related tables same distribution key.

### Architecture Perspective

Citus is horizontal scale when partition-on-one-node is exhausted.

### Follow-up Questions

1. **Reference tables? — Small lookup tables replicated to all nodes.**
2. **Coordinator bottleneck? — Query routing — scale coordinator tier.**

### Common Mistakes in Interviews

- Citus without tenant isolation in key
- Cross-shard JOIN heavy reporting
- Citus for 50GB database

---

## Q046: PostGIS When

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Extensions |
| **Frequency** | Occasional |

### Question

When add PostGIS to PostgreSQL vs store lat/long in app or use external geo service?

### Short Answer (30 seconds)

PostGIS when queries need distance, containment, spatial joins, geofencing in SQL — not just display markers. GiST index on geometry.

### Detailed Answer (3–5 minutes)

**Use PostGIS:**
- Find stores within 5 km of user
- Polygon containment (delivery zones)
- Route-adjacent spatial joins

**Skip PostGIS:**
- Store coordinates for map pin display only
- Simple bounding box in app code at low volume
- Azure Maps / Google Maps API handles geo logic externally

**Example:**
```sql
SELECT * FROM stores
WHERE ST_DWithin(location::geography, ST_MakePoint(@lon,@lat)::geography, 5000);
```

**Architect:** PostGIS adds operational complexity — extension upgrades tied to PG version. Bounded context owns spatial data.

### Architecture Perspective

PostGIS is for spatial queries in SQL — not coordinates in a JSON blob.

### Follow-up Questions

1. **geometry vs geography? — Geography for lat/lon meters; geometry for projected CRS.**
2. **Spatial index? — `CREATE INDEX ON stores USING GIST (location);`**

### Common Mistakes in Interviews

- PostGIS for lat/long display only
- No GiST index on geometry column
- Haversine in app on 10M rows

---

## Q047: TimescaleDB

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Extensions |
| **Frequency** | Common |

### Question

When choose TimescaleDB over native Postgres partitioning for metrics?

### Short Answer (30 seconds)

TimescaleDB for high-ingest time-series (metrics, IoT, logs) needing automatic chunking, compression, retention policies, continuous aggregates — reduces ops vs hand-rolled partitions.

### Detailed Answer (3–5 minutes)

**Hypertable:**
```sql
SELECT create_hypertable('metrics', 'time');
```

**Features architects use:**
- **Compression** — older chunks compressed 90%+
- **Retention policies** — drop chunks older than N days
- **Continuous aggregates** — materialized rollups refresh incrementally

**Native partitioning enough when:**
- Low ingest, monthly manual partitions OK
- Team knows pg_partman

**TimescaleDB when:**
- Millions inserts/min
- Standard Prometheus/Grafana stack on SQL

**Azure:** Timescale on Flexible Server or self-managed.

### Architecture Perspective

TimescaleDB is architect shortcut for time-series ops Postgres can do manually.

### Follow-up Questions

1. **Chunk interval tuning? — 1 day vs 1 week — match query window.**
2. **Hypercore columnstore? — Recent Timescale compression evolution — evaluate version.**

### Common Mistakes in Interviews

- Hand-rolled partitions at IoT ingest scale
- No retention policy on metrics table
- Timescale for relational OLTP core

---

## Q048: Row-Level Security Policies

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Implement multi-tenant isolation with PostgreSQL RLS.

### Short Answer (30 seconds)

Enable RLS on table, create policy filtering `tenant_id = current_setting('app.tenant_id')::int`. App sets tenant per connection/transaction.

### Detailed Answer (3–5 minutes)

**Setup:**
```sql
ALTER TABLE orders ENABLE ROW LEVEL SECURITY;

CREATE POLICY tenant_isolation ON orders
  USING (tenant_id = current_tenant_id());
```

**App (Npgsql):**
```csharp
await cmd.ExecuteNonQueryAsync("SET app.tenant_id = '42'");
```

**Architect:**
- RLS is defense in depth — not replacement for app filtering
- Superuser bypasses RLS — no superuser in app role
- Test policies with integration tests per tenant
- **Bypass risk:** SQL injection setting wrong tenant — parameterize everything

**Performance:** Index on `tenant_id` — policy adds filter every query.

### Architecture Perspective

RLS encodes tenant isolation in database — architects layer with app auth.

### Follow-up Questions

1. **FORCE ROW LEVEL SECURITY? — Applies to table owner too — stricter.**
2. **BYPASSRLS role attribute? — Migration admin only — not app.**

### Common Mistakes in Interviews

- RLS without index on tenant_id
- App uses superuser connection
- Forget SET tenant on pooled connection

---

## Q049: pg_stat_statements

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Observability |
| **Frequency** | Very Common |

### Question

How use pg_stat_statements for performance architecture?

### Short Answer (30 seconds)

Extension tracks normalized query text, calls, total_time, mean_time, rows — identify top CPU/IO queries without full query logging.

### Detailed Answer (3–5 minutes)

**Enable:**
```sql
CREATE EXTENSION pg_stat_statements;
SELECT query, calls, mean_exec_time, total_exec_time
FROM pg_stat_statements ORDER BY total_exec_time DESC LIMIT 20;
```

**Architect workflow:**
1. Weekly review top 10 by `total_exec_time` and `mean_exec_time`
2. Correlate with `EXPLAIN ANALYZE` on replica
3. Reset stats after major release for clean baseline: `pg_stat_statements_reset()`

**Azure Flexible Server:** extension available — enable in server parameters.

**Pair with:** `pg_stat_user_tables` (seq scans), auto_explain for slow plans.

### Architecture Perspective

pg_stat_statements is Postgres Query Store equivalent — architects mandate it on prod.

### Follow-up Questions

1. **track_io_timing? — `shared_preload_libraries` — I/O per query.**
2. **Query normalization? — Literals replaced — group similar queries.**

### Common Mistakes in Interviews

- No extension on production Postgres
- Tune queries never ranked by total_time
- Never reset stats after major migration

---

## Q050: Postgres on Azure Flexible HA

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Cloud |
| **Frequency** | Very Common |

### Question

Design HA and DR for Azure Database for PostgreSQL Flexible Server.

### Short Answer (30 seconds)

Zone-redundant HA: standby in another AZ, automatic failover ~60–120s. Read replicas up to 5 for read scale. Geo-redundant backup for DR — not synchronous geo replica by default.

### Detailed Answer (3–5 minutes)

**HA modes:**
- **Same zone** — single AZ, lower cost, AZ outage risk
- **Zone redundant** — production default for tier-1

**Architect checklist:**
- Private endpoint + VNet integration
- Connection string retry on failover (Npgsql `KeepAlive`, Polly)
- Read replica for reporting — monitor replication lag
- PITR backup retention per compliance (7–35 days)
- **Built-in PgBouncer** — enable for connection pooling

**RPO/RTO:**
- HA failover RPO=0 within region, RTO ~2 min
- Geo-DR: restore from geo backup — RPO = backup interval, RTO hours — document acceptance

**vs SQL Server AG:** Postgres Flexible uses different failover semantics — test app behavior.

### Architecture Perspective

Azure Flexible HA is managed Patroni — architects still own app retry and replica lag routing.

### Follow-up Questions

1. **Accelerated logs? — IO optimization for write-heavy — enable for OLTP.**
2. **Burstable vs General Purpose? — Burstable dev only — prod GP or Memory Optimized.**

### Common Mistakes in Interviews

- Single zone for production payments
- No retry logic on Npgsql connection
- Assume read replica zero lag

---

## Q051: HOT Updates Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Very Common |

### Question

What must architects know about HOT Updates?

### Short Answer (30 seconds)

Heap-Only Tuple updates avoiding index maintenance when indexed columns unchanged

### Detailed Answer (3–5 minutes)

**Topic:** HOT Updates
**Focus:** Heap-Only Tuple updates avoiding index maintenance when indexed columns unchanged

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 8 context:** What must architects know about HOT Updates?

### Architecture Perspective

HOT Updates is essential Week 8 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of HOT Updates?**
2. **Common production mistake with HOT Updates?**

### Common Mistakes in Interviews

- Confusing HOT Updates with adjacent service
- Console-only knowledge without design rationale
- No monitoring for HOT Updates failures

---

## Q052: HOT Updates Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Very Common |

### Question

How deploy HOT Updates in production enterprise workloads?

### Short Answer (30 seconds)

Heap-Only Tuple updates avoiding index maintenance when indexed columns unchanged

### Detailed Answer (3–5 minutes)

**Topic:** HOT Updates
**Focus:** Heap-Only Tuple updates avoiding index maintenance when indexed columns unchanged

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 8 context:** How deploy HOT Updates in production enterprise workloads?

### Architecture Perspective

HOT Updates is essential Week 8 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of HOT Updates?**
2. **Common production mistake with HOT Updates?**

### Common Mistakes in Interviews

- Confusing HOT Updates with adjacent service
- Console-only knowledge without design rationale
- No monitoring for HOT Updates failures

---

## Q053: HOT Updates Advanced Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Common |

### Question

Advanced HOT Updates tuning and edge cases?

### Short Answer (30 seconds)

Heap-Only Tuple updates avoiding index maintenance when indexed columns unchanged

### Detailed Answer (3–5 minutes)

**Topic:** HOT Updates
**Focus:** Heap-Only Tuple updates avoiding index maintenance when indexed columns unchanged

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 8 context:** Advanced HOT Updates tuning and edge cases?

### Architecture Perspective

HOT Updates is essential Week 8 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of HOT Updates?**
2. **Common production mistake with HOT Updates?**

### Common Mistakes in Interviews

- Confusing HOT Updates with adjacent service
- Console-only knowledge without design rationale
- No monitoring for HOT Updates failures

---

## Q054: HOT Updates Architecture Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Common |

### Question

Architecture trade-offs for HOT Updates?

### Short Answer (30 seconds)

Heap-Only Tuple updates avoiding index maintenance when indexed columns unchanged

### Detailed Answer (3–5 minutes)

**Topic:** HOT Updates
**Focus:** Heap-Only Tuple updates avoiding index maintenance when indexed columns unchanged

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 8 context:** Architecture trade-offs for HOT Updates?

### Architecture Perspective

HOT Updates is essential Week 8 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of HOT Updates?**
2. **Common production mistake with HOT Updates?**

### Common Mistakes in Interviews

- Confusing HOT Updates with adjacent service
- Console-only knowledge without design rationale
- No monitoring for HOT Updates failures

---

## Q055: Fillfactor Tuning Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Very Common |

### Question

What must architects know about Fillfactor Tuning?

### Short Answer (30 seconds)

Page free space reserved for HOT updates on high-churn tables

### Detailed Answer (3–5 minutes)

**Topic:** Fillfactor Tuning
**Focus:** Page free space reserved for HOT updates on high-churn tables

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 8 context:** What must architects know about Fillfactor Tuning?

### Architecture Perspective

Fillfactor Tuning is essential Week 8 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Fillfactor Tuning?**
2. **Common production mistake with Fillfactor Tuning?**

### Common Mistakes in Interviews

- Confusing Fillfactor Tuning with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Fillfactor Tuning failures

---

## Q056: Fillfactor Tuning Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Very Common |

### Question

How deploy Fillfactor Tuning in production enterprise workloads?

### Short Answer (30 seconds)

Page free space reserved for HOT updates on high-churn tables

### Detailed Answer (3–5 minutes)

**Topic:** Fillfactor Tuning
**Focus:** Page free space reserved for HOT updates on high-churn tables

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 8 context:** How deploy Fillfactor Tuning in production enterprise workloads?

### Architecture Perspective

Fillfactor Tuning is essential Week 8 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Fillfactor Tuning?**
2. **Common production mistake with Fillfactor Tuning?**

### Common Mistakes in Interviews

- Confusing Fillfactor Tuning with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Fillfactor Tuning failures

---

## Q057: Fillfactor Tuning Advanced Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Common |

### Question

Advanced Fillfactor Tuning tuning and edge cases?

### Short Answer (30 seconds)

Page free space reserved for HOT updates on high-churn tables

### Detailed Answer (3–5 minutes)

**Topic:** Fillfactor Tuning
**Focus:** Page free space reserved for HOT updates on high-churn tables

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 8 context:** Advanced Fillfactor Tuning tuning and edge cases?

### Architecture Perspective

Fillfactor Tuning is essential Week 8 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Fillfactor Tuning?**
2. **Common production mistake with Fillfactor Tuning?**

### Common Mistakes in Interviews

- Confusing Fillfactor Tuning with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Fillfactor Tuning failures

---

## Q058: Fillfactor Tuning Architecture Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Common |

### Question

Architecture trade-offs for Fillfactor Tuning?

### Short Answer (30 seconds)

Page free space reserved for HOT updates on high-churn tables

### Detailed Answer (3–5 minutes)

**Topic:** Fillfactor Tuning
**Focus:** Page free space reserved for HOT updates on high-churn tables

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 8 context:** Architecture trade-offs for Fillfactor Tuning?

### Architecture Perspective

Fillfactor Tuning is essential Week 8 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Fillfactor Tuning?**
2. **Common production mistake with Fillfactor Tuning?**

### Common Mistakes in Interviews

- Confusing Fillfactor Tuning with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Fillfactor Tuning failures

---

## Q059: TOAST Storage Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Storage |
| **Frequency** | Very Common |

### Question

What must architects know about TOAST Storage?

### Short Answer (30 seconds)

Out-of-line storage for oversized JSONB and text values

### Detailed Answer (3–5 minutes)

**Topic:** TOAST Storage
**Focus:** Out-of-line storage for oversized JSONB and text values

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 8 context:** What must architects know about TOAST Storage?

### Architecture Perspective

TOAST Storage is essential Week 8 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of TOAST Storage?**
2. **Common production mistake with TOAST Storage?**

### Common Mistakes in Interviews

- Confusing TOAST Storage with adjacent service
- Console-only knowledge without design rationale
- No monitoring for TOAST Storage failures

---

## Q060: TOAST Storage Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Storage |
| **Frequency** | Very Common |

### Question

How deploy TOAST Storage in production enterprise workloads?

### Short Answer (30 seconds)

Out-of-line storage for oversized JSONB and text values

### Detailed Answer (3–5 minutes)

**Topic:** TOAST Storage
**Focus:** Out-of-line storage for oversized JSONB and text values

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 8 context:** How deploy TOAST Storage in production enterprise workloads?

### Architecture Perspective

TOAST Storage is essential Week 8 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of TOAST Storage?**
2. **Common production mistake with TOAST Storage?**

### Common Mistakes in Interviews

- Confusing TOAST Storage with adjacent service
- Console-only knowledge without design rationale
- No monitoring for TOAST Storage failures

---

## Q061: TOAST Storage Advanced Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Storage |
| **Frequency** | Common |

### Question

Advanced TOAST Storage tuning and edge cases?

### Short Answer (30 seconds)

Out-of-line storage for oversized JSONB and text values

### Detailed Answer (3–5 minutes)

**Topic:** TOAST Storage
**Focus:** Out-of-line storage for oversized JSONB and text values

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 8 context:** Advanced TOAST Storage tuning and edge cases?

### Architecture Perspective

TOAST Storage is essential Week 8 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of TOAST Storage?**
2. **Common production mistake with TOAST Storage?**

### Common Mistakes in Interviews

- Confusing TOAST Storage with adjacent service
- Console-only knowledge without design rationale
- No monitoring for TOAST Storage failures

---

## Q062: TOAST Storage Architecture Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Storage |
| **Frequency** | Common |

### Question

Architecture trade-offs for TOAST Storage?

### Short Answer (30 seconds)

Out-of-line storage for oversized JSONB and text values

### Detailed Answer (3–5 minutes)

**Topic:** TOAST Storage
**Focus:** Out-of-line storage for oversized JSONB and text values

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 8 context:** Architecture trade-offs for TOAST Storage?

### Architecture Perspective

TOAST Storage is essential Week 8 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of TOAST Storage?**
2. **Common production mistake with TOAST Storage?**

### Common Mistakes in Interviews

- Confusing TOAST Storage with adjacent service
- Console-only knowledge without design rationale
- No monitoring for TOAST Storage failures

---

## Q063: Generated Columns Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | JSONB |
| **Frequency** | Very Common |

### Question

What must architects know about Generated Columns?

### Short Answer (30 seconds)

Stored generated columns extracting hot JSONB paths to B-tree indexable columns

### Detailed Answer (3–5 minutes)

**Topic:** Generated Columns
**Focus:** Stored generated columns extracting hot JSONB paths to B-tree indexable columns

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 8 context:** What must architects know about Generated Columns?

### Architecture Perspective

Generated Columns is essential Week 8 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Generated Columns?**
2. **Common production mistake with Generated Columns?**

### Common Mistakes in Interviews

- Confusing Generated Columns with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Generated Columns failures

---

## Q064: Generated Columns Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | JSONB |
| **Frequency** | Very Common |

### Question

How deploy Generated Columns in production enterprise workloads?

### Short Answer (30 seconds)

Stored generated columns extracting hot JSONB paths to B-tree indexable columns

### Detailed Answer (3–5 minutes)

**Topic:** Generated Columns
**Focus:** Stored generated columns extracting hot JSONB paths to B-tree indexable columns

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 8 context:** How deploy Generated Columns in production enterprise workloads?

### Architecture Perspective

Generated Columns is essential Week 8 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Generated Columns?**
2. **Common production mistake with Generated Columns?**

### Common Mistakes in Interviews

- Confusing Generated Columns with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Generated Columns failures

---

## Q065: Generated Columns Advanced Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | JSONB |
| **Frequency** | Common |

### Question

Advanced Generated Columns tuning and edge cases?

### Short Answer (30 seconds)

Stored generated columns extracting hot JSONB paths to B-tree indexable columns

### Detailed Answer (3–5 minutes)

**Topic:** Generated Columns
**Focus:** Stored generated columns extracting hot JSONB paths to B-tree indexable columns

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 8 context:** Advanced Generated Columns tuning and edge cases?

### Architecture Perspective

Generated Columns is essential Week 8 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Generated Columns?**
2. **Common production mistake with Generated Columns?**

### Common Mistakes in Interviews

- Confusing Generated Columns with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Generated Columns failures

---

## Q066: Generated Columns Architecture Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | JSONB |
| **Frequency** | Common |

### Question

Architecture trade-offs for Generated Columns?

### Short Answer (30 seconds)

Stored generated columns extracting hot JSONB paths to B-tree indexable columns

### Detailed Answer (3–5 minutes)

**Topic:** Generated Columns
**Focus:** Stored generated columns extracting hot JSONB paths to B-tree indexable columns

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 8 context:** Architecture trade-offs for Generated Columns?

### Architecture Perspective

Generated Columns is essential Week 8 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Generated Columns?**
2. **Common production mistake with Generated Columns?**

### Common Mistakes in Interviews

- Confusing Generated Columns with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Generated Columns failures

---

## Q067: Synchronous Replication Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | HA/DR |
| **Frequency** | Very Common |

### Question

What must architects know about Synchronous Replication?

### Short Answer (30 seconds)

synchronous_commit and synchronous_standby_names for RPO=0

### Detailed Answer (3–5 minutes)

**Topic:** Synchronous Replication
**Focus:** synchronous_commit and synchronous_standby_names for RPO=0

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 8 context:** What must architects know about Synchronous Replication?

### Architecture Perspective

Synchronous Replication is essential Week 8 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Synchronous Replication?**
2. **Common production mistake with Synchronous Replication?**

### Common Mistakes in Interviews

- Confusing Synchronous Replication with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Synchronous Replication failures

---

## Q068: Synchronous Replication Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | HA/DR |
| **Frequency** | Very Common |

### Question

How deploy Synchronous Replication in production enterprise workloads?

### Short Answer (30 seconds)

synchronous_commit and synchronous_standby_names for RPO=0

### Detailed Answer (3–5 minutes)

**Topic:** Synchronous Replication
**Focus:** synchronous_commit and synchronous_standby_names for RPO=0

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 8 context:** How deploy Synchronous Replication in production enterprise workloads?

### Architecture Perspective

Synchronous Replication is essential Week 8 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Synchronous Replication?**
2. **Common production mistake with Synchronous Replication?**

### Common Mistakes in Interviews

- Confusing Synchronous Replication with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Synchronous Replication failures

---

## Q069: Synchronous Replication Advanced Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | HA/DR |
| **Frequency** | Common |

### Question

Advanced Synchronous Replication tuning and edge cases?

### Short Answer (30 seconds)

synchronous_commit and synchronous_standby_names for RPO=0

### Detailed Answer (3–5 minutes)

**Topic:** Synchronous Replication
**Focus:** synchronous_commit and synchronous_standby_names for RPO=0

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 8 context:** Advanced Synchronous Replication tuning and edge cases?

### Architecture Perspective

Synchronous Replication is essential Week 8 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Synchronous Replication?**
2. **Common production mistake with Synchronous Replication?**

### Common Mistakes in Interviews

- Confusing Synchronous Replication with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Synchronous Replication failures

---

## Q070: Synchronous Replication Architecture Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | HA/DR |
| **Frequency** | Common |

### Question

Architecture trade-offs for Synchronous Replication?

### Short Answer (30 seconds)

synchronous_commit and synchronous_standby_names for RPO=0

### Detailed Answer (3–5 minutes)

**Topic:** Synchronous Replication
**Focus:** synchronous_commit and synchronous_standby_names for RPO=0

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 8 context:** Architecture trade-offs for Synchronous Replication?

### Architecture Perspective

Synchronous Replication is essential Week 8 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Synchronous Replication?**
2. **Common production mistake with Synchronous Replication?**

### Common Mistakes in Interviews

- Confusing Synchronous Replication with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Synchronous Replication failures

---
