# Week 11 — Intermediate Q&A

> Q001–Q050: Premium format (Week 1 quality).  
> **Topic:** Azure Data Platform | **Count:** 50

---


## Q001: Azure SQL Database vs Cosmos DB

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Data |
| **Frequency** | Very Common |

### Question

Choose Azure SQL or Cosmos DB for multi-tenant SaaS orders and catalog?

### Short Answer (30 seconds)

SQL for orders — ACID, transactions, complex queries. Cosmos for catalog — global distribution, flexible schema, high read scale with partition key design.

### Detailed Answer (3–5 minutes)

**Orders:** relational integrity, foreign keys (within service), T-SQL reporting.

**Catalog:** `tenantId` + `productId` partition key, session consistency, multi-region reads.

**Architect:** Polyglot persistence per bounded context — not one database for everything.

### Architecture Perspective

Data store per workload is architect interview staple.

### Follow-up Questions

1. **Hyperscale SQL when? — Large OLTP >4TB, fast scale requirements.**
2. **Cosmos serverless? — Dev/test and unpredictable traffic.**

### Common Mistakes in Interviews

- Cosmos for financial transactions needing ACID
- SQL for global 1M RPS reads without design
- No partition key design before Cosmos

---

## Q002: Cosmos DB Partition Key Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Cosmos DB |
| **Frequency** | Very Common |

### Question

Design partition key for multi-tenant SaaS in Cosmos DB.

### Short Answer (30 seconds)

`tenantId` — co-locate tenant data, efficient tenant-scoped queries. Avoid low-cardinality keys (`status`) — hot partitions.

### Detailed Answer (3–5 minutes)

**Rules:**
- High cardinality
- Include in most queries
- Even distribution — watch for large tenants (dedicated partition or sub-shard)

**RU/s:** Hot partition causes 429 throttling on single partition limit (20GB, 10K RU/s max per partition).

### Architecture Perspective

Bad partition key causes unfixable scale ceiling.

### Follow-up Questions

1. **Synthetic partition key? — `tenantId + hash bucket` for mega-tenants.**
2. **Cross-partition query cost? — Expensive — design to avoid.**

### Common Mistakes in Interviews

- Partition key you cannot query by
- /id as partition key on high volume
- No 429 monitoring

---

## Q003: Azure SQL HA and DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SQL |
| **Frequency** | Very Common |

### Question

RPO/RTO for Azure SQL production?

### Short Answer (30 seconds)

Active geo-replication: readable secondaries, manual failover RPO ~5s. Auto-failover groups: RPO ~5s automated. Zone-redundant for HA within region.

### Detailed Answer (3–5 minutes)

**Architect documents:**
- HA: zone redundant or geo-secondary same region pair
- DR: failover group to paired region
- App: retry transient errors, `MultiSubnetFailover=True`

Test failover quarterly.

### Architecture Perspective

SQL HA options map directly to SLA promises.

### Follow-up Questions

1. **Hyperscale HA? — Different architecture — read replicas, fast scale.**
2. **Backup retention? — LTR for compliance — 7-10 years some industries.**

### Common Mistakes in Interviews

- Single database no geo-replica prod
- Never tested failover
- Assume geo-replica RPO=0

---

## Q004: Blob Storage Tiers and Lifecycle

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Storage |
| **Frequency** | Common |

### Question

Design blob lifecycle for 7-year audit log retention.

### Short Answer (30 seconds)

Hot 30 days → Cool 90 days → Cold 1 year → Archive 7 years. Lifecycle management policy automated. Immutable storage for compliance if required.

### Detailed Answer (3–5 minutes)

**Cost:** Archive cheapest, retrieval cost high — right for audit rarely accessed.

**Architect:** Lifecycle policies in IaC — Bicep `Microsoft.Storage/storageAccounts/blobServices`.

Immutable blob storage (WORM) for regulatory immutability.

### Architecture Perspective

Storage tiering is FinOps architecture.

### Follow-up Questions

1. **Versioning enabled? — Protect against overwrite — cost consideration.**
2. **Soft delete? — Recover accidental deletion — enable prod.**

### Common Mistakes in Interviews

- All data Hot tier forever
- No lifecycle policy automation
- Archive for frequently accessed reports

---

## Q005: DTU vs vCore SQL Model

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SQL |
| **Frequency** | Common |

### Question

DTU vs vCore for Azure SQL?

### Short Answer (30 seconds)

vCore: production — predictable CPU/memory, Hyperscale, reserved capacity. DTU: simple bundled model, dev/test, small databases.

### Detailed Answer (3–5 minutes)

**Architect:** Standardize on vCore for prod in enterprise. DTU acceptable dev.

**Elastic pool:** Many small databases share resources — SaaS with many tenant DBs.

### Architecture Perspective

Model choice affects scaling and cost transparency.

### Follow-up Questions

1. **Serverless SQL? — Intermittent workloads — auto-pause dev.**
2. **Reserved vCore? — 1-3 year for baseline production.**

### Common Mistakes in Interviews

- DTU prod without cost analysis
- Wrong pool eDTU sizing
- No performance baseline before purchase

---

## Q006: Synapse vs SQL for Analytics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Analytics |
| **Frequency** | Common |

### Question

Operational reporting: SQL read replica or Synapse?

### Short Answer (30 seconds)

Read replica or columnstore on SQL for moderate reporting. Synapse dedicated pool for large-scale DW, complex aggregations, data lake integration.

### Detailed Answer (3–5 minutes)

**Architect:** Don't run heavy analytics on OLTP primary — replica or separate DW path.

**Modern:** Export to Data Lake (Parquet) → Synapse serverless SQL or Fabric.

### Architecture Perspective

Analytics path protects OLTP.

### Follow-up Questions

1. **CDC to data lake? — Near real-time analytics pipeline.**
2. **Power BI DirectQuery vs Import? — Scale and freshness trade-off.**

### Common Mistakes in Interviews

- Heavy reports on primary OLTP
- Synapse for simple 10GB reporting
- No data pipeline ownership

---

## Q007: Event Hubs vs Service Bus for Ingestion

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Streaming |
| **Frequency** | Common |

### Question

10M telemetry events/day — Event Hubs or Service Bus?

### Short Answer (30 seconds)

Event Hubs for high-volume streaming ingest (Kafka protocol). Service Bus for business messages, transactions, lower volume, sessions.

### Detailed Answer (3–5 minutes)

**Event Hubs:** partitions, retention, stream analytics, Kafka ecosystem.

**Service Bus:** queues/topics, dead letter, duplicate detection, lower latency messaging patterns.

### Architecture Perspective

Right messaging tech prevents re-platforming.

### Follow-up Questions

1. **Capture to Data Lake? — Event Hubs archive feature.**
2. **Partition count Event Hubs? — Throughput units — plan upfront.**

### Common Mistakes in Interviews

- Service Bus for million events/sec
- Event Hubs for order payment commands
- No consumer scaling plan

---

## Q008: Elastic Pools for SaaS

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SQL |
| **Frequency** | Common |

### Question

1000 small tenant databases — elastic pool strategy?

### Short Answer (30 seconds)

Elastic pool shares eDTU/vCore across DBs — cost efficient when tenants don't peak simultaneously. Monitor pool DTU utilization.

### Detailed Answer (3–5 minutes)

**Per-tenant DB:** isolation, easy export/delete tenant. **Shared DB with RLS:** fewer DBs, harder isolation.

**Architect:** Per-tenant DB in pool for B2B SaaS with compliance per tenant.

### Architecture Perspective

SaaS data architecture common scenario.

### Follow-up Questions

1. **Pool exhaustion? — Move hot tenant to own pool or single DB.**
2. **Geo-replication elastic pool? — Secondary pool in DR region.**

### Common Mistakes in Interviews

- 1000 separate servers
- Single shared table without RLS
- No pool utilization monitoring

---

## Q009: Data Encryption on Azure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

TDE vs customer-managed keys for healthcare data?

### Short Answer (30 seconds)

TDE with Microsoft-managed keys default. CMK (Key Vault) when compliance requires customer key control, key rotation audit, crypto-officer separation.

### Detailed Answer (3–5 minutes)

**Layer:** encryption at rest (TDE), in transit (TLS), column-level Always Encrypted for sensitive fields (SSN).

**Architect:** CMK adds ops — Key Vault availability becomes data availability.

### Architecture Perspective

Encryption choices are compliance architecture.

### Follow-up Questions

1. **Always Encrypted? — Client-side encryption — DBA cannot read.**
2. **Double encryption? — Infrastructure + CMK — defense in depth.**

### Common Mistakes in Interviews

- CMK without HA Key Vault plan
- No TLS on internal connections
- PII in plain text columns

---

## Q010: Polyglot Data on Azure Reference

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Architecture |
| **Frequency** | Common |

### Question

Draw data stores for e-commerce on Azure.

### Short Answer (30 seconds)

SQL: orders/payments. Cosmos: product catalog global. Redis: cart/sessions. Blob: images. Event Hubs: clickstream. Synapse: analytics.

### Detailed Answer (3–5 minutes)

Each store owns bounded context. Sync via events — not distributed JOINs.

**Integration:** Service Bus domain events, CDC to warehouse.

### Architecture Perspective

Reference architecture synthesis question.

### Follow-up Questions

1. **Cache aside Redis? — Product pages — TTL + invalidation on update event.**
2. **Search? — Azure AI Search index from catalog events.**

### Common Mistakes in Interviews

- One SQL database for everything
- Cosmos and SQL joined in app
- No event-driven sync

---

## Q011: Azure SQL Tier Selection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SQL |
| **Frequency** | Very Common |

### Question

How do you select the right Azure SQL tier for a new production OLTP workload?

### Short Answer (30 seconds)

Start with vCore General Purpose for most OLTP. Move to Business Critical for low-latency IO and built-in read scale-out. Hyperscale when database exceeds ~4 TB or needs rapid storage growth.

### Detailed Answer (3–5 minutes)

**Decision matrix:**
- **General Purpose (GP):** cost-effective, remote storage, 99.99% SLA with zone redundancy
- **Business Critical (BC):** local SSD, read replicas on same instance, 99.995% SLA — finance/trading latency
- **Hyperscale:** auto-growing storage to 100 TB+, fast backup/restore, read replicas

**Architect process:** Baseline DTU/vCore from load test, right-size compute, use reserved capacity for steady baseline. Serverless vCore for intermittent dev/test only.

**SaaS pattern:** Many small DBs → elastic pool on GP vCore rather than individual tiers.

### Architecture Perspective

Tier selection ties directly to SLA, cost, and scale ceiling.

### Follow-up Questions

1. **When GP vs BC read scale? — BC has free readable secondaries on same node; GP needs active geo-replication for read scale.**
2. **Serverless for production? — Rarely — auto-pause and cold start unacceptable for steady OLTP.**

### Common Mistakes in Interviews

- Choosing DTU prod without vCore analysis
- Hyperscale for 50 GB database — overkill
- No reserved capacity on predictable baseline

---

## Q012: Cosmos DB Consistency Levels

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Cosmos DB |
| **Frequency** | Very Common |

### Question

Explain Cosmos DB consistency levels and when to use each.

### Short Answer (30 seconds)

Five levels from strong to eventual: Strong, Bounded Staleness, Session, Consistent Prefix, Eventual. Session is default — best balance for most apps.

### Detailed Answer (3–5 minutes)

**Strong:** linearizability — single region only, highest RU cost. Use financial ledger within region.

**Bounded Staleness:** max lag in K versions or T seconds — global reads with predictable staleness.

**Session:** reads see own writes — ideal for user-scoped data (cart, profile).

**Consistent Prefix / Eventual:** lowest RU, highest throughput — analytics counters, social feeds.

**Architect:** Default Session; document per-container consistency in ADR. Multi-region writes require Session or weaker — Strong only single-region writer.

### Architecture Perspective

Consistency level is a cost, latency, and correctness trade-off.

### Follow-up Questions

1. **Can you mix consistency per request? — Yes — override at request level within account default.**
2. **Strong multi-region? — Not supported for multi-writer — use Session + conflict resolution.**

### Common Mistakes in Interviews

- Strong everywhere for cost savings
- Eventual for inventory without business acceptance
- No consistency documented in API contracts

---

## Q013: Blob Storage Access Tiers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Storage |
| **Frequency** | Very Common |

### Question

Compare Hot, Cool, Cold, and Archive blob tiers for a document archive platform.

### Short Answer (30 seconds)

Hot: frequent access, highest storage cost, lowest access cost. Cool: 30+ day retention, infrequent access. Cold: 90+ days, cheaper storage. Archive: 180+ days, lowest storage, highest retrieval latency (hours).

### Detailed Answer (3–5 minutes)

**Minimum retention:** Cool 30 days, Cold 90 days, Archive 180 days — early deletion penalty.

**Architect design:** Lifecycle policy automates tier transitions. Archive for compliance docs accessed once a year.

**Example:** Invoices Hot 7 days → Cool 1 year → Archive 7 years.

**Premium block blobs:** sub-ms latency for Hot tier hot paths — separate from tier choice.

### Architecture Perspective

Tier selection is FinOps architecture — wrong tier doubles storage bill.

### Follow-up Questions

1. **Archive rehydrate priority? — High (minutes-hours) vs Standard ( hours) — cost vs urgency.**
2. **Cool vs Cold break-even? — Model access frequency — Cold wins below ~1 read/month per blob.**

### Common Mistakes in Interviews

- All blobs Hot forever
- Archive for monthly payroll reports
- No lifecycle policy in IaC

---

## Q014: Azure Data Factory Pipelines

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Data Integration |
| **Frequency** | Common |

### Question

Design an ADF pipeline for nightly SQL-to-Data-Lake ETL.

### Short Answer (30 seconds)

Linked services for SQL and ADLS Gen2. Copy activity with incremental watermark column. Trigger schedule or tumbling window. Staging in ADLS as Parquet partitioned by date.

### Detailed Answer (3–5 minutes)

**Pattern:**
1. Lookup last watermark from metadata table
2. Copy activity `query` with `WHERE modified > @{watermark}`
3. Update watermark on success
4. Failure alert via Logic App / Azure Monitor

**Architect:** Use managed VNet integration + private endpoints for SQL. Git integration for ARM/Bicep-deployed ADF. Self-hosted IR only for on-prem sources.

### Architecture Perspective

ADF is orchestration — not transformation engine for complex logic.

### Follow-up Questions

1. **Mapping data flows vs Copy? — Data flows for transforms; Copy for bulk movement.**
2. **Parameterize environments? — ARM template parameters or Bicep — separate dev/prod linked services.**

### Common Mistakes in Interviews

- Full load nightly on 500 GB table
- No watermark — duplicates or missed rows
- Credentials in pipeline not Key Vault

---

## Q015: Synapse Analytics Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Analytics |
| **Frequency** | Very Common |

### Question

When use Synapse dedicated SQL pool vs serverless vs Spark pool?

### Short Answer (30 seconds)

Dedicated pool: provisioned DW, predictable performance, large aggregations. Serverless: ad-hoc queries on Data Lake files, pay per TB scanned. Spark pool: ETL, ML, complex transforms on big data.

### Detailed Answer (3–5 minutes)

**Modern lakehouse:** Ingest to ADLS (Parquet/Delta) → Spark for curation → Serverless SQL for analysts → Dedicated pool for heavy BI if needed.

**Architect:** Don't duplicate data — medallion layers in ADLS, Synapse workspaces query in place.

**Cost:** Pause dedicated pool off-hours. Serverless — partition Parquet and use column pruning to reduce scan cost.

### Architecture Perspective

Synapse is a workspace orchestrating multiple compute engines on shared storage.

### Follow-up Questions

1. **Synapse Link for Cosmos? — Near real-time analytics without ETL batch.**
2. **Dedicated vs Fabric warehouse? — Fabric convergence — know both for interviews.**

### Common Mistakes in Interviews

- Dedicated pool for 10 GB monthly report
- Serverless full table scan on CSV
- No pause schedule on dedicated pool

---

## Q016: PostgreSQL Flexible Server

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Databases |
| **Frequency** | Common |

### Question

Azure Database for PostgreSQL Flexible Server vs Single Server — why Flexible?

### Short Answer (30 seconds)

Flexible Server is current platform: zone redundancy, better VNet integration, custom maintenance window, burstable and general-purpose compute. Single Server is retired — migrate to Flexible.

### Detailed Answer (3–5 minutes)

**Architect choices:**
- **Burstable:** dev/test, low CPU average
- **General Purpose:** production OLTP
- **Memory Optimized:** analytics on Postgres, large cache

**HA:** zone-redundant HA with automatic failover. Read replicas for read scale.

**Extensions:** pgvector, PostGIS — verify allowlist for AI/search workloads.

### Architecture Perspective

Flexible Server is default Postgres choice on Azure.

### Follow-up Questions

1. **Private access? — Private endpoint or VNet injection — no public endpoint prod.**
2. **Migration from Single Server? — Azure migration tooling — plan downtime or DMS.**

### Common Mistakes in Interviews

- New projects on Single Server
- Public endpoint production
- No HA on business-critical Postgres

---

## Q017: Azure Cache for Redis Tiers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Caching |
| **Frequency** | Common |

### Question

Compare Basic, Standard, Premium Redis tiers for session cache.

### Short Answer (30 seconds)

Basic: single node, no SLA — dev only. Standard: two-node replica, 99.9% SLA. Premium: clustering, persistence, VNet injection, geo-replication.

### Detailed Answer (3–5 minutes)

**Production session cache:** Standard C1 minimum. **Premium when:** >53 GB data, shard cluster, persistence (AOF/RDB), private VNet, active geo-replication for DR.

**Architect:** Cache-aside pattern, TTL on sessions, handle Redis failure gracefully (re-login acceptable vs data loss).

**Enterprise:** Azure Managed Redis (new) vs legacy Cache for Redis — know rebranding direction.

### Architecture Perspective

Redis tier maps to HA, scale, and network isolation needs.

### Follow-up Questions

1. **Clustering when? — Memory exceeds single node max or need horizontal shard.**
2. **Redis vs SQL session state? — Redis for scale and speed; SQL when durability mandatory.**

### Common Mistakes in Interviews

- Basic tier production
- No TTL — memory eviction surprises
- Cache as source of truth for orders

---

## Q018: Table Storage vs Cosmos DB Table API

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Storage |
| **Frequency** | Common |

### Question

Table Storage vs Cosmos DB Table API — when each?

### Short Answer (30 seconds)

Table Storage: legacy, cheap, single region, Key/Value within partition. Cosmos Table API: global distribution, SLA, throughput control, same SDK surface.

### Detailed Answer (3–5 minutes)

**Choose Table Storage:** simple internal tooling, single region, lowest cost, no SLA requirement.

**Choose Cosmos Table API:** need multi-region, RU scaling, consistency options, enterprise SLA.

**Architect:** Greenfield tabular NoSQL → prefer Cosmos native API (SQL/NoSQL) over Table API unless SDK compatibility required.

### Architecture Perspective

Table API is migration path — not default for new global apps.

### Follow-up Questions

1. **Partition key Table Storage? — `PartitionKey` + `RowKey` — same hot partition rules as Cosmos.**
2. **Azure Tables SDK? — New `Azure.Data.Tables` works with both — connection string differs.**

### Common Mistakes in Interviews

- Table Storage for global user-facing app
- Cosmos Table API without RU planning
- Cross-partition scan on large table

---

## Q019: Data Lake Storage Gen2 Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Storage |
| **Frequency** | Very Common |

### Question

Design ADLS Gen2 folder structure for enterprise analytics.

### Short Answer (30 seconds)

Hierarchical namespace enabled on storage account. Zones: raw/bronze, curated/silver, analytics/gold. Partition by `year/month/day/`. RBAC at container/folder level.

### Detailed Answer (3–5 minutes)

**Features:** ACLs + RBAC, atomic directory operations, POSIX-like semantics for Spark/Hadoop.

**Architect:**
- Separate storage accounts per environment (dev/prod)
- Managed identity for Synapse/Databricks access
- Lifecycle to Cool/Archive on raw after N days

**Security:** No public access, private endpoints, Entra ID only — avoid shared keys.

### Architecture Perspective

ADLS Gen2 is analytics landing zone foundation.

### Follow-up Questions

1. **ABFS driver? — `abfss://` URI — always use OAuth not key.**
2. **One account vs many? — Domain-separated accounts (finance, marketing) for blast radius.**

### Common Mistakes in Interviews

- Flat blob storage without hierarchical namespace
- Shared key in Spark config
- No partition strategy — full scans

---

## Q020: Private Endpoint for Azure SQL

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

Configure Azure SQL with Private Endpoint — what breaks if misconfigured?

### Short Answer (30 seconds)

SQL gets private IP in subnet. Requires private DNS zone `privatelink.database.windows.net` linked to VNet. Without DNS, apps still resolve public IP — connection fails or bypasses private path.

### Detailed Answer (3–5 minutes)

**Checklist:**
1. Disable public network access (prod)
2. Create private endpoint in app subnet
3. Private DNS zone group on endpoint
4. Link DNS zone to all VNets that need access (hub-spoke)

**Architect:** Test with `nslookup sqlserver.database.windows.net` from VM — must return 10.x private IP.

**Cross-region:** Private endpoint same region as SQL; consumers in other regions via peered VNet.

### Architecture Perspective

Private Link for SQL is production security baseline.

### Follow-up Questions

1. **Dual endpoint public+private? — Transitional only — disable public after validation.**
2. **Managed identity through PE? — Yes — `Authentication=Active Directory Default`.**

### Common Mistakes in Interviews

- Private endpoint without DNS zone
- Public access still enabled prod
- Hardcode private IP in connection string

---

## Q021: Azure SQL Active Geo-Replication

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SQL |
| **Frequency** | Very Common |

### Question

Design active geo-replication for read scale and DR.

### Short Answer (30 seconds)

Up to four readable secondaries in any region. Async replication — typical RPO ~5 seconds. Manual failover for DR; secondaries for read offload.

### Detailed Answer (3–5 minutes)

**Read routing:** `ApplicationIntent=ReadOnly` in connection string with `Server=tcp:secondary.database.windows.net`.

**Architect:** Secondary in paired region for DR; additional secondaries near users for read scale.

**Limitations:** Same service tier family, no cross-tier. User tables replicate — some system objects differ.

### Architecture Perspective

Geo-replication is async — plan for seconds of data loss on failover.

### Follow-up Questions

1. **Auto-failover groups vs geo-replication? — Failover groups add automatic endpoint management.**
2. **Hyperscale geo? — Different model — named replicas.**

### Common Mistakes in Interviews

- Assume RPO zero with geo-replication
- Write to secondary
- No read connection string separation

---

## Q022: Azure SQL Backup Retention

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SQL |
| **Frequency** | Common |

### Question

Backup retention strategy for compliance-heavy Azure SQL?

### Short Answer (30 seconds)

PITR: 7–35 days default configurable. LTR (Long-Term Retention): weekly/monthly/yearly up to 10 years in blob storage.

### Detailed Answer (3–5 minutes)

**Architect documents:**
- PITR window for operational recovery (35 days typical prod)
- LTR for regulatory (SOX 7 years)
- Test restore quarterly to verify LTR

**Geo-redundant backup storage:** ON for DR — backups survive region loss.

**Hyperscale:** Continuous backup model — different restore semantics.

### Architecture Perspective

Backup retention is compliance architecture not DBA checkbox.

### Follow-up Questions

1. **Restore time PITR? — Depends on size — communicate RTO in DR plan.**
2. **Deleted database retention? — 7 days recoverable — extend awareness.**

### Common Mistakes in Interviews

- Minimum 7-day PITR for prod financial
- LTR never tested restore
- Geo-redundant backup disabled

---

## Q023: Elastic Pool Sizing Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SQL |
| **Frequency** | Common |

### Question

Size an elastic pool for 500 tenant databases with variable load.

### Short Answer (30 seconds)

Monitor aggregate DTU/vCore and per-DB peaks. Pool eDTU must exceed sum of average usage with headroom for uncorrelated peaks.

### Detailed Answer (3–5 minutes)

**Signals:**
- `elastic_pool_resource_stats` — pool utilization
- Per-DB `avg_cpu_percent` — identify noisy neighbors

**Architect:** Set per-database min/max eDTU caps — prevent one tenant consuming entire pool. Move hot tenant to standalone DB.

**Alternative:** Hyperscale per tenant if one tenant exceeds pool economics.

### Architecture Perspective

Elastic pools assume load diversity — correlated peaks breakupsize pool.

### Follow-up Questions

1. **Pool vs many singles cost? — Break-even ~20–30 small DBs — model with calculator.**
2. **Zone redundancy pool? — Supported — add HA at pool level.**

### Common Mistakes in Interviews

- Max eDTU per DB unlimited — one tenant starves others
- No per-DB cap configuration
- Never eject hot tenant from pool

---

## Q024: Cosmos DB Partition Key Deep Dive

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Cosmos DB |
| **Frequency** | Very Common |

### Question

A tenant has 10× traffic of others — partition key strategy?

### Short Answer (30 seconds)

Synthetic partition key: `tenantId + bucket` where bucket = hash(userId) % N. Distributes mega-tenant across N logical partitions while keeping queries scoped.

### Detailed Answer (3–5 minutes)

**Physical limit:** 20 GB and 10K RU/s per physical partition — hot tenant hits ceiling with `tenantId` alone.

**Architect:** Monitor `PartitionKeyRangeId` metrics for skew. Dedicated container for mega-tenant if isolation required.

**Hierarchical keys:** `/tenantId/orders` — preview feature for multi-level — know conceptually.

### Architecture Perspective

Partition key mistakes are expensive to fix — requires container rebuild.

### Follow-up Questions

1. **Change partition key? — Live container migration feature — plan downtime/cost.**
2. **GUID as partition key? — High cardinality but random — cross-partition queries on every read.**

### Common Mistakes in Interviews

- Low cardinality status field as key
- Ignore 429 throttling on single partition
- No tenant size monitoring

---

## Q025: Cosmos DB Change Feed

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Cosmos DB |
| **Frequency** | Common |

### Question

Use Cosmos DB change feed for event-driven sync to Azure Search.

### Short Answer (30 seconds)

Change feed processor reads ordered changes per partition. Push product updates to Azure AI Search indexer or custom worker.

### Detailed Answer (3–5 minutes)

**Pattern:**
1. Container with change feed enabled (default)
2. Azure Function or Container Apps processor with lease container
3. Idempotent upsert to Search index

**Architect:** At-least-once delivery — handle duplicates. Lease container manages processor scale-out.

**Alternative:** Synapse Link for analytics path; change feed for operational sync.

### Architecture Perspective

Change feed is CDC for Cosmos — foundation for event-driven architecture.

### Follow-up Questions

1. **All versions and deletes? — Configure feed mode — know delete handling.**
2. **Multiple processors? — Partition lease distribution — scale horizontally.**

### Common Mistakes in Interviews

- Poll container manually for changes
- No idempotent downstream writes
- Single processor no lease container

---

## Q026: Azure AI Search Indexing Pipeline

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Search |
| **Frequency** | Common |

### Question

Design Azure AI Search index refresh from SQL and blob documents.

### Short Answer (30 seconds)

Indexer pulls from SQL with high-watermark column or Cosmos change feed. Skillset for OCR (blob), language detection, enrichment. Schedule or push model.

### Detailed Answer (3–5 minutes)

**Architect:**
- Separate index per environment
- Semantic ranker for relevance
- Private endpoint for Search service prod

**Scale:** Replicas for query QPS, partitions for index size >25 GB.

### Architecture Perspective

Search indexing is part of polyglot persistence reference architecture.

### Follow-up Questions

1. **Push vs pull? — Indexer scheduled pull; push API for real-time from app events.**
2. **Skillset cost? — Cognitive Services billing per document — batch wisely.**

### Common Mistakes in Interviews

- Search without index partitioning plan
- Indexer full scan hourly on large table
- No soft delete handling in index

---

## Q027: Event Hubs Capture to Data Lake

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Streaming |
| **Frequency** | Common |

### Question

Configure Event Hubs Capture for raw event archival.

### Short Answer (30 seconds)

Enable Capture on Event Hub — writes Avro files to Storage account or ADLS on time/size window (e.g., 5 min / 300 MB).

### Detailed Answer (3–5 minutes)

**Downstream:** Spark/Synapse reads Avro for batch analytics. Stream Analytics separate path for real-time.

**Architect:** Capture is fire-and-forget archive — consumers use separate consumer groups for live processing.

**Retention:** Event Hubs retention (1–7 days) vs Capture ( indefinite cheap storage ).

### Architecture Perspective

Capture decouples long-term storage from stream retention limits.

### Follow-up Questions

1. **Avro vs Parquet capture? — Event Hubs Capture is Avro; convert in Spark to Parquet.**
2. **Capture storage account security? — Private endpoint, MI access from Synapse.**

### Common Mistakes in Interviews

- Only 1-day retention no Capture — data loss for replay
- Same consumer group for analytics and live
- Capture to Hot tier forever without lifecycle

---

## Q028: Schema Migration Strategy Cloud

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DevOps |
| **Frequency** | Very Common |

### Question

Zero-downtime schema migration for Azure SQL in CI/CD?

### Short Answer (30 seconds)

Expand-contract pattern: add nullable column (expand) → dual-write or backfill → switch reads → remove old (contract). Flyway/Liquibase/DbUp in pipeline with review gate.

### Detailed Answer (3–5 minutes)

**Tools:** Flyway in Azure DevOps/GitHub Actions against staging slot DB. Use `-outOfOrder` carefully.

**Architect:** Backward-compatible migrations only in release N; breaking changes in N+1 after code deployed.

**Lock avoidance:** Online index rebuild, avoid table rewrites in peak hours.

### Architecture Perspective

Cloud DB migrations require expand-contract not big-bang ALTER.

### Follow-up Questions

1. **Blue-green database? — Copy failover group secondary as test — advanced.**
2. **Rollback? — Forward-only migrations with feature flags safer than down scripts prod.**

### Common Mistakes in Interviews

- Breaking schema change same release as code
- Manual SSMS prod without script review
- Long-running migration without online option

---

## Q029: Connection Pooling in Cloud

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Very Common |

### Question

Connection pooling best practices for Azure SQL with App Service?

### Short Answer (30 seconds)

Enable pooling in ADO.NET (default). Right-size pool `Max Pool Size` — too high exhausts SQL `max_connections`. Use gateway/proxy (PgBouncer pattern) for serverless functions with many instances.

### Detailed Answer (3–5 minutes)

**Azure specifics:**
- **App Service:** pooling per instance — 10 instances × 100 pool = 1000 SQL connections
- **Functions:** use `Microsoft.Data.SqlClient` pooling; consider Azure SQL serverless min vCores to avoid cold start + connection storm

**Architect:** Monitor `connection_failed` and `blocked_process` metrics. Elastic pool many apps — aggregate connection math.

### Architecture Perspective

Connection storms are common cloud outage cause.

### Follow-up Questions

1. **Disable pooling? — Almost never — latency and resource waste.**
2. **SqlClient vs ODBC pool? — Per-process separate pools.**

### Common Mistakes in Interviews

- Max Pool Size 500 on 20 App Service instances
- New connection per request in Functions
- No connection count monitoring

---

## Q030: Read Replica Routing Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SQL |
| **Frequency** | Common |

### Question

Implement read replica routing in .NET microservices.

### Short Answer (30 seconds)

Primary connection string for writes. Secondary with `ApplicationIntent=ReadOnly` for reports. Or separate `IReadDbConnection` injected via DI.

### Detailed Answer (3–5 minutes)

**Architect:**
- Eventual consistency on replica — UI labels 'near real-time'
- Retry on replica lag for critical read-after-write — read primary

**Cosmos:** Session consistency gives read-your-writes without routing complexity.

**Postgres Flexible:** Read replica FQDN separate — reader endpoint load balances.

### Architecture Perspective

Explicit read/write split protects OLTP primary.

### Follow-up Questions

1. **EF Core read replica? — Interceptor or dual DbContext — no built-in auto routing.**
2. **Replica for all reads including just-written order? — Bug — use primary or wait.**

### Common Mistakes in Interviews

- Random round-robin to replica for writes
- Ignore replication lag in UX
- Single connection string for everything

---

## Q031: Azure SQL Geo-Restore

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DR |
| **Frequency** | Common |

### Question

Geo-restore vs failover group — when geo-restore?

### Short Answer (30 seconds)

Geo-restore: restore DB from geo-redundant backup to any region — RPO up to 1 hour, RTO hours. Use region-wide outage when failover group not configured or full region loss.

### Detailed Answer (3–5 minutes)

**Failover group:** Managed DR with seconds RPO. **Geo-restore:** Backup-based recovery last resort.

**Architect DR runbook:**
1. Attempt failover group automatic/manual
2. If backup region intact, geo-restore to target region
3. Update DNS/connection strings
4. Communicate data loss window

### Architecture Perspective

Geo-restore is safety net not primary DR strategy.

### Follow-up Questions

1. **Geo-restore Hyperscale? — Different — point-in-time restore within region first.**
2. **Test geo-restore annually? — Required for compliance evidence.**

### Common Mistakes in Interviews

- Geo-restore as only DR plan
- No runbook for connection string update
- Assume zero data loss geo-restore

---

## Q032: Transparent Data Encryption SQL

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Explain TDE for Azure SQL and customer-managed keys.

### Short Answer (30 seconds)

TDE encrypts data at rest automatically — data files, backups, tempdb. Microsoft-managed keys default. CMK via Azure Key Vault for customer control and audit.

### Detailed Answer (3–5 minutes)

**Architect:** Enable TDE on all prod databases (default on new). CMK when compliance mandates key ownership.

**Ops:** Key Vault soft delete + purge protection mandatory with CMK. Key unavailable = database offline.

**Double encryption:** Infrastructure encryption + TDE for defense in depth.

### Architecture Perspective

TDE is baseline — interviewers want CMK trade-offs too.

### Follow-up Questions

1. **TDE performance impact? — Minimal on Azure SQL — hardware accelerated.**
2. **Bring your own key (BYOK)? — CMK from HSM-backed Key Vault.**

### Common Mistakes in Interviews

- CMK without Key Vault HA
- Assume TDE covers in-transit — need TLS too
- Disable TDE for performance myth

---

## Q033: Dynamic Data Masking

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Implement Dynamic Data Masking for support staff SQL access.

### Short Answer (30 seconds)

DDM masks column values in query results — email shows `aXXX@XXXX.com`. Does not encrypt — users with UNMASK privilege see plain text.

### Detailed Answer (3–5 minutes)

**Architect:** Layer defense — DDM for casual access, Always Encrypted for true protection, audit UNMASK grants.

**Limitations:** Deterministic masking for joins; random for display-only. Not replacement for encryption.

### Architecture Perspective

DDM reduces accidental exposure — not cryptographic control.

### Follow-up Questions

1. **Mask admin accounts? — Exclude with UNMASK only break-glass audited.**
2. **DDM on API layer? — Database-level — apps using same DB user still masked.**

### Common Mistakes in Interviews

- DDM instead of Always Encrypted for PCI
- Grant UNMASK broadly
- Masking without auditing privileged access

---

## Q034: Always Encrypted SQL

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

When use Always Encrypted vs TDE?

### Short Answer (30 seconds)

Always Encrypted: client-side encryption — DBA and cloud admin cannot read column values. TDE: at-rest only — DBAs see plain text in memory.

### Detailed Answer (3–5 minutes)

**Use Always Encrypted for:** SSN, PCI PAN, highly sensitive PII.

**Modes:** Deterministic (equality search) vs Randomized (max security, no search).

**Architect:** Key in Key Vault or Windows Certificate Store. Column Master Key rotation plan. Performance overhead on encrypted columns.

### Architecture Perspective

Always Encrypted protects against privileged insider and cloud operator.

### Follow-up Questions

1. **Enclave enabled? — Secure enclaves allow range queries on encrypted data — complexity trade-off.**
2. **.NET integration? — `Column Encryption Setting=Enabled` in connection string.**

### Common Mistakes in Interviews

- Always Encrypted for all columns — unnecessary overhead
- Store CMK in app config
- Randomized encryption then filter WHERE — fails

---

## Q035: Azure SQL Failover Groups

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SQL |
| **Frequency** | Very Common |

### Question

Design failover group for multi-region Azure SQL.

### Short Answer (30 seconds)

Failover group: one primary, one secondary (or more readable), shared `failover-group-name.database.windows.net` listener. Automatic or manual failover, RPO ~5s.

### Detailed Answer (3–5 minutes)

**Architect checklist:**
- Same subscription recommended
- App uses listener connection string
- `MultipleActiveResultSets` and retry logic for transient faults
- Graceful failover: planned maintenance

**Readable secondaries:** Include in failover group — DR + read scale unified.

### Architecture Perspective

Failover group simplifies DR connection management.

### Follow-up Questions

1. **Failover group elastic pool? — Pools must match region pairing strategy.**
2. **Split-brain? — Azure prevents dual primary — listener follows primary.**

### Common Mistakes in Interviews

- Hardcode regional server name not listener
- No application retry on 40613 errors
- Failover untested in production

---

## Q036: Cosmos DB RU Autoscale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Cosmos DB |
| **Frequency** | Common |

### Question

Provisioned RU vs autoscale vs serverless for Cosmos?

### Short Answer (30 seconds)

Provisioned: steady predictable load, cost at max RU. Autoscale: 10–100% of max RU, scales to zero floor at 10% max — variable workloads. Serverless: dev/test, sporadic traffic, no minimum.

### Detailed Answer (3–5 minutes)

**Architect:** Start autoscale for unknown patterns — max RU = peak × 1.5. Move to provisioned when baseline stable for cost.

**Monitor:** 429 rate, normalized RU consumption. Partition max 10K RU/s — autoscale per partition.

### Architecture Perspective

RU model choice is primary Cosmos cost lever.

### Follow-up Questions

1. **Autoscale max RU change? — Can adjust — billing on highest max in hour.**
2. **Serverless limits? — 1M RU/month free tier; not for sustained prod load.**

### Common Mistakes in Interviews

- Provisioned 50K RU on idle dev database
- Ignore 429 throttling alerts
- Autoscale max set to peak without headroom

---

## Q037: Blob Immutability WORM

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compliance |
| **Frequency** | Common |

### Question

Configure immutable blob storage for SEC 17a-4 compliance.

### Short Answer (30 seconds)

Time-based retention policy on container — blobs cannot be deleted or overwritten until period expires. Legal hold for litigation.

### Detailed Answer (3–5 minutes)

**Governance mode:** admins can extend retention. **Compliance mode:** no one shortens — including subscription owner.

**Architect:** Separate storage account for audit logs. Versioning + immutability together. Document retention in compliance register.

### Architecture Perspective

Immutability is regulatory architecture for WORM requirements.

### Follow-up Questions

1. **Immutable vs soft delete? — Complementary — immutability prevents overwrite; soft delete recovery window.**
2. **Lifecycle delete conflict? — Lifecycle cannot delete before immutability expiry.**

### Common Mistakes in Interviews

- Compliance mode without legal review
- Mutable audit log container
- No versioning with immutability

---

## Q038: ADLS ACLs vs RBAC

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

When use POSIX ACLs vs RBAC on ADLS Gen2?

### Short Answer (30 seconds)

RBAC: Entra ID groups, coarse-grained container/folder via `Storage Blob Data Contributor`. ACLs: fine-grained file/folder POSIX permissions, execute bit for folders.

### Detailed Answer (3–5 minutes)

**Architect pattern:** RBAC for service principals and broad team access. ACLs when fine folder-level control needed (multi-tenant lake folders).

**Best practice:** Enable `storage blob owner` RBAC + ACLs for default ACL inheritance on new files.

**Avoid:** Shared keys — always OAuth/RBAC.

### Architecture Perspective

ADLS security combines RBAC and ACLs — not either/or.

### Follow-up Questions

1. **Default ACL? — New files inherit — critical for Spark jobs.**
2. **Access checker tool? — Validate effective permissions before prod cutover.**

### Common Mistakes in Interviews

- RBAC alone on deeply nested multi-tenant paths
- Shared key in Databricks cluster
- ACL changes not in IaC

---

## Q039: Azure Data Share

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Occasional |

### Question

Share dataset with partner without copying to their subscription?

### Short Answer (30 seconds)

Azure Data Share: provider shares snapshot or in-place from Storage, SQL, Synapse. Consumer maps to their subscription — governed, monitored transfers.

### Detailed Answer (3–5 minutes)

**Architect:** Prefer in-place share (provider pays egress rules apply) vs copy for freshness. Entra B2B guest for consumer access.

**Alternative:** Event-driven export to their storage with SAS — less governance.

### Architecture Perspective

Data Share is B2B data exchange pattern on Azure.

### Follow-up Questions

1. **Snapshot vs in-place? — Snapshot for point-in-time; in-place for live read with refresh triggers.**
2. **Purview integration? — Register shared assets in catalog.**

### Common Mistakes in Interviews

- Email CSV export to partner
- Full storage account key shared
- No data sharing agreement documented

---

## Q040: Microsoft Purview Data Map

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

Use Purview for data governance across Azure and on-prem.

### Short Answer (30 seconds)

Purview scans sources (SQL, ADLS, Power BI), builds data map, classifies sensitive data, lineage graph. Unified catalog for discovery.

### Detailed Answer (3–5 minutes)

**Architect:** Register collections per domain. Auto-classification for PII. Integrate with ADF/Synapse for lineage capture.

**Ops:** Scheduled scans, glossary for business terms, access policies (preview features evolving).

### Architecture Perspective

Purview is enterprise data catalog — not optional at scale.

### Follow-up Questions

1. **Scan scope? — Sample vs full — cost and time trade-off.**
2. **On-prem SQL scan? — Self-hosted integration runtime.**

### Common Mistakes in Interviews

- No catalog — analysts query unknown datasets
- Classification without owner assignment
- Scan prod without change window

---

## Q041: Lakehouse Medallion Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Analytics |
| **Frequency** | Very Common |

### Question

Explain bronze/silver/gold medallion layers on ADLS.

### Short Answer (30 seconds)

Bronze: raw ingest, schema-on-read, append-only. Silver: cleansed, deduplicated, conformed. Gold: business aggregates, star schema, BI-ready.

### Detailed Answer (3–5 minutes)

**Architect:**
- Delta/Iceberg on ADLS for ACID silver/gold
- Separate Spark jobs per layer
- Data quality checks at bronze→silver gate

**Ownership:** Domain teams own gold; platform team owns bronze ingestion standards.

### Architecture Perspective

Medallion is standard lakehouse pattern interviewers expect.

### Follow-up Questions

1. **One big folder? — Anti-pattern — layer separation enables reprocessing.**
2. **Real-time gold? — Streaming silver → materialized gold via Spark Structured Streaming.**

### Common Mistakes in Interviews

- Skip silver — dirty data in reports
- No idempotent bronze ingestion
- Gold tables writable by analysts

---

## Q042: Synapse Spark Pool Configuration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Analytics |
| **Frequency** | Common |

### Question

Size and configure Synapse Spark pool for daily ETL.

### Short Answer (30 seconds)

Node size (Small to XXLarge), auto-scale min/max nodes, auto-pause idle minutes. Spark 3.x with Delta Lake libraries.

### Detailed Answer (3–5 minutes)

**Architect:**
- Separate pools dev (small, short pause) vs prod (right-sized, longer pause delay)
- Managed VNet for private data access
- Pool packages for dependency consistency

**Cost:** Auto-pause after 15 min idle. Spot/Low priority nodes where fault-tolerant.

### Architecture Perspective

Spark pool sizing affects ETL window and bill directly.

### Follow-up Questions

1. **Dynamic allocation? — Enable for variable partition workloads.**
2. **Synapse vs Databricks? — Know both — Synapse unified workspace; Databricks broader ecosystem.**

### Common Mistakes in Interviews

- XXLarge pool for 1 GB daily job
- No auto-pause — pool runs 24/7
- Libraries installed ad hoc not pool package

---

## Q043: PolyBase in Synapse

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Analytics |
| **Frequency** | Occasional |

### Question

Use PolyBase to query external data in Synapse dedicated pool.

### Short Answer (30 seconds)

PolyBase creates external tables over ADLS/Blob/SQL ODBC sources. Query Data Lake with T-SQL without loading into warehouse.

### Detailed Answer (3–5 minutes)

**Architect:** External tables for exploratory queries; CETAS to materialize hot paths into internal tables.

**Serverless SQL:** Preferred for ad-hoc external queries — dedicated pool PolyBase for integrated DW workloads.

**Format:** Parquet/ORC/Delta supported — CSV for small only.

### Architecture Perspective

PolyBase bridges relational SQL and data lake.

### Follow-up Questions

1. **Statistics on external tables? — Create for cardinality estimates — performance.**
2. **Credential security? — DATABASE SCOPED CREDENTIAL with MI or SAS in Key Vault.**

### Common Mistakes in Interviews

- Load entire lake into DW unnecessarily
- External table on tiny CSV forever
- SAS key in credential plaintext

---

## Q044: Azure Stream Analytics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Streaming |
| **Frequency** | Common |

### Question

Design Stream Analytics job from Event Hubs to Power BI.

### Short Answer (30 seconds)

Input Event Hub, query with SQL-like language (windowing, JOIN reference data), output Power BI push dataset or ADLS for archive.

### Detailed Answer (3–5 minutes)

**Patterns:**
- Tumbling window aggregations (5-min counts)
- Reference data blob for dimension enrichment
- Multiple outputs — alert stream + archive

**Architect:** Scale SU for throughput. Handle late events with watermark policy.

### Architecture Perspective

Stream Analytics is managed stream processing without Spark ops.

### Follow-up Questions

1. **ASA vs Spark Streaming? — ASA simpler SQL; Spark for complex ML/transform.**
2. **Exactly-once? — At-least-once default — idempotent sinks.**

### Common Mistakes in Interviews

- Unbounded window on high volume
- No reference data version strategy
- Single SU production peak traffic

---

## Q045: Azure Time Series Insights

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | IoT |
| **Frequency** | Occasional |

### Question

Time Series Insights vs storing IoT telemetry in Cosmos/SQL?

### Short Answer (30 seconds)

TSI (legacy/evolving to Data Explorer): optimized time-series storage, downsampling, trend analysis. Cosmos/SQL: operational state, alerts, not long-term analytics at scale.

### Detailed Answer (3–5 minutes)

**Modern path:** IoT Hub → Event Hubs → ADX (Azure Data Explorer) for time-series analytics; TSI Gen2 migrated toward ADX.

**Architect:** Hot path operational in SQL/Cosmos; warm/cold analytics in ADX with retention policies.

### Architecture Perspective

Know TSI evolution to ADX for interviews.

### Follow-up Questions

1. **ADX vs Synapse? — ADX sub-second analytics on append-only telemetry; Synapse batch/BI.**
2. **Retention tiering ADX? — Cache vs extend vs archive.**

### Common Mistakes in Interviews

- SQL for billion-row telemetry
- No downsampling on 1-second sensor data
- Ignore TSI migration guidance

---

## Q046: Azure Database for MySQL Flexible

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Databases |
| **Frequency** | Common |

### Question

Choose Azure Database for MySQL Flexible Server for WordPress scale-out.

### Short Answer (30 seconds)

Flexible Server: zone HA, read replicas, burstable/GP/MO tiers, VNet integration. Better than Single Server (retired).

### Detailed Answer (3–5 minutes)

**Architect:** Read replicas for read-heavy WordPress; Premium storage IO for plugin-heavy DB. Connection pooling via ProxySQL sidecar if needed.

**Migration:** Azure Database Migration Service from on-prem or Single Server.

### Architecture Perspective

MySQL Flexible is standard Azure MySQL offering.

### Follow-up Questions

1. **MariaDB vs MySQL? — Separate Azure service — see selection criteria.**
2. **Private Link MySQL? — Supported Flexible — disable public.**

### Common Mistakes in Interviews

- Single Server new deployment
- No read replica for viral traffic
- max_connections default without pooling

---

## Q047: MariaDB vs MySQL on Azure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Databases |
| **Frequency** | Occasional |

### Question

Azure Database for MariaDB vs MySQL — selection?

### Short Answer (30 seconds)

MariaDB Flexible Server mirrors MySQL Flexible capabilities. Choose based on app compatibility (MariaDB fork features vs Oracle MySQL 8).

### Detailed Answer (3–5 minutes)

**MySQL when:** Oracle MySQL 8 features, InnoDB cluster compatibility. **MariaDB when:** existing MariaDB app, specific MariaDB extensions.

**Architect:** Standardize one engine org-wide unless legacy requires MariaDB. Both support HA, replicas, VNet.

### Architecture Perspective

Engine choice is compatibility not performance religion.

### Follow-up Questions

1. **Cross-migrate? — Dump/restore or DMS — test charset/collation.**
2. **Azure MariaDB Single Server? — Retired — Flexible only.**

### Common Mistakes in Interviews

- Pick MariaDB without app requirement
- Ignore version EOL schedule
- Wrong collation migration failure

---

## Q048: Data Encryption at Rest Azure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Map encryption at rest across Azure data services.

### Short Answer (30 seconds)

Storage: SSE with Microsoft or CMK. SQL: TDE. Cosmos: service-managed keys or CMK. ADLS: same as storage. Disks: SSE.

### Detailed Answer (3–5 minutes)

**Architect defense in depth:**
1. Platform encryption (default on)
2. CMK for regulated workloads
3. Client-side (Always Encrypted, app-level) for highest sensitivity

**Compliance:** Document key hierarchy in security architecture.

### Architecture Perspective

Encryption at rest is table stakes — CMK is the architect decision.

### Follow-up Questions

1. **Infrastructure encryption storage? — Extra AES layer on hardware.**
2. **Cosmos CMK? — Account level Key Vault key.**

### Common Mistakes in Interviews

- Assume default encryption satisfies all regulators without CMK review
- Keys and data same Key Vault no separation
- No encryption in transit complement

---

## Q049: SQL Key Rotation with CMK

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Rotate customer-managed TDE key without database outage?

### Short Answer (30 seconds)

Add new Key Vault key version; alter database encryption key to rewrap with new version. Azure SQL online reencryption — minimal impact.

### Detailed Answer (3–5 minutes)

**Architect runbook:**
1. Create new KV key version (or rotation policy auto)
2. `ALTER DATABASE ENCRYPTION KEY` or portal rotate
3. Verify `sys.dm_database_encryption_keys`
4. Audit Key Vault logs

**Avoid:** Disabling purge protection; deleting old key version before rewrap complete.

### Architecture Perspective

Key rotation proves crypto governance maturity.

### Follow-up Questions

1. **Automatic rotation Key Vault? — 90-day policy + SQL manual rewrap or automation runbook.**
2. **TDE protector vs column CMK? — Separate rotation schedules.**

### Common Mistakes in Interviews

- Delete old key version immediately
- CMK rotation untested in staging
- No alert on Key Vault access failure

---

## Q050: SQL Data Classification

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

Implement data discovery and classification in Azure SQL.

### Short Answer (30 seconds)

Built-in SQL Data Discovery & Classification scans columns, recommends labels (PII, financial). Integrates with Purview for enterprise catalog.

### Detailed Answer (3–5 minutes)

**Architect workflow:**
1. Enable classification scan
2. Review recommendations, apply labels
3. Export report for compliance
4. Feed Purview for lineage + policies

**Combine with:** DDM, Always Encrypted, audit sensitive column access.

### Architecture Perspective

Classification drives protection tier decisions.

### Follow-up Questions

1. **Auto-labeling sensitivity? — Information Protection integration for MIP labels.**
2. **Classification in CI? — Fail build if unlabeled columns in prod schema — advanced governance.**

### Common Mistakes in Interviews

- Manual spreadsheet of PII columns
- Classification without remediation plan
- Ignore recommendations quarterly

---
