# Week 46 — Fundamentals Interview Q&A

> Q001–Q030: Premium format (Week 1 quality).  
> See also: [Interview prep hub](../../../interview-prep/README.md)

---


## Q001: SQL Interview Architecture Angle

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Database |
| **Frequency** | Very Common |

### Question

How do solution architects approach SQL questions differently from DBA trivia interviews?

### Short Answer (30 seconds)

Lead with workload classification (OLTP vs analytics), consistency requirements, scale path (indexes → read replicas → sharding), and operational governance — not just 'add an index.' Show execution-plan methodology and business impact.

### Detailed Answer (3–5 minutes)

**Architect answer framework:**
1. **Classify workload** — transactional, reporting, mixed
2. **State SLAs** — p99 latency, RPO/RTO, consistency
3. **Diagnose** — execution plan, logical reads, waits
4. **Remediate** — sargable predicates, composite indexes, partition, cache
5. **Govern** — index review cadence, migration strategy, connection pooling

**High-value topics:**
| Topic | Architecture hook |
|-------|-------------------|
| Index design | Leading column selectivity; covering indexes; write overhead |
| Query tuning | Filter early; avoid functions on indexed columns |
| Replication lag | Classify reads: payment balance → primary; catalog → replica |
| Sharding | Shard key = tenantId; avoid cross-shard joins in OLTP |
| Connection pools | Pods × pool size vs DB max connections |

**Example opener:** 'For a 5:1 read/write ratio and 30s stale tolerance, I'd route analytics to a read replica and keep financial reads on the primary.'

**Tools to mention:** Azure SQL Query Store, missing index DMVs, EF Core SQL logging in staging.

**Avoid:** Index every column; optimize without baseline metrics.

### Architecture Perspective

SQL architecture interviews test data scale path and consistency trade-offs — architects own the decision, DBAs often own the tuning.

### Follow-up Questions

1. **Columnstore vs rowstore? — Analytics vs OLTP — different index models.**
2. **Hyperscale / Citus? — When vertical scale exhausts — mention shard router.**

### Common Mistakes in Interviews

- Jump to sharding on day one with 100 users
- Assume read replica is always current
- SELECT * on hot API paths

---

## Q002: Azure Services Interview Map

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Azure |
| **Frequency** | Very Common |

### Question

How map Azure services quickly in a cloud architect interview?

### Short Answer (30 seconds)

Organize by capability layers — identity, networking, compute, data, messaging, observability, security — not alphabetical service lists. Map each requirement to a managed service with trade-off (PaaS vs IaaS vs serverless).

### Detailed Answer (3–5 minutes)

**Capability map (interview whiteboard):**
| Layer | Azure services |
|-------|----------------|
| Edge | Front Door, CDN, WAF |
| API | API Management, App Service, AKS ingress |
| Compute | App Service, Functions, AKS, Container Apps |
| Data | Azure SQL, Cosmos DB, Blob, Redis Cache |
| Messaging | Service Bus, Event Hubs, Event Grid |
| Identity | Entra ID, managed identity, Key Vault |
| Ops | Monitor, Log Analytics, App Insights, Policy |
| Integration | Logic Apps, Data Factory |

**Answer technique:**
1. Restate requirement (global web app, 10K RPS, PCI)
2. Pick entry (Front Door + WAF)
3. Compute (App Service vs AKS — team skill decides)
4. Data (SQL + Redis cache-aside)
5. Identity (managed identity to Key Vault — no secrets in config)

**Frameworks to cite:** Well-Architected pillars, CAF landing zones, subscription segmentation.

**Differentiator:** Name what you would NOT use — 'Not AKS here because team has no platform engineers and traffic is steady.'

### Architecture Perspective

Azure interviews reward capability thinking — interviewers want justified service selection, not certification recall.

### Follow-up Questions

1. **Cosmos vs SQL? — Multi-region write vs relational transactions — consistency model drives choice.**
2. **Event Hubs vs Service Bus? — Streaming telemetry scale vs enterprise messaging features.**

### Common Mistakes in Interviews

- Naming services without requirement context
- Single subscription for all environments
- Public endpoints on PaaS without Private Link discussion

---

## Q003: AWS Fundamentals Interview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | AWS |
| **Frequency** | Very Common |

### Question

What AWS fundamentals must a multi-cloud architect demonstrate in interviews?

### Short Answer (30 seconds)

Cover shared responsibility model, core services (EC2, S3, IAM, VPC, RDS, Lambda, SQS/SNS), region/AZ design, and IAM least privilege — framed with Azure equivalents when asked for comparison.

### Detailed Answer (3–5 minutes)

**Foundational concepts:**
1. **Shared responsibility** — AWS secures cloud; you secure data, IAM, network config
2. **Regions & AZs** — multi-AZ for HA; data residency by region choice
3. **IAM** — users, roles, policies; instance profiles; no long-lived keys in apps
4. **VPC** — subnets public/private, security groups, NACLs, NAT gateway

**Core service map:**
| Need | AWS | Quick note |
|------|-----|------------|
| VM | EC2 | ASG for scale |
| Object storage | S3 | Lifecycle tiers, versioning |
| Relational DB | RDS / Aurora | Multi-AZ failover |
| Serverless | Lambda | Cold start, 15 min limit |
| Queue | SQS | Visibility timeout, DLQ |
| Identity | IAM + Cognito | Federation with Entra possible |
| K8s | EKS | Control plane managed |

**Interview structure:** Define → production example → Azure parallel → operational concern (cost, monitoring CloudWatch).

**Architect angle:** Landing zone (Control Tower), Organizations, SCPs — enterprise guardrails.

**Honest stance:** 'Primary on Azure; AWS fluent for DR, acquisition, or multi-cloud ADR.'

### Architecture Perspective

AWS fundamentals prove multi-cloud literacy — architects compare capabilities, not logo loyalty.

### Follow-up Questions

1. **Well-Architected Framework? — Six pillars parallel Azure WAF — good bridge answer.**
2. **RDS Proxy? — Connection pooling at scale — pairs with Lambda/RDS discussion.**

### Common Mistakes in Interviews

- Assume IAM is same as Entra ID RBAC
- S3 bucket public by default acceptable
- Ignore egress cost between AZs and regions

---

## Q004: Multi-Cloud Strategy Interview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Cloud Strategy |
| **Frequency** | Very Common |

### Question

How answer multi-cloud strategy questions with architectural maturity?

### Short Answer (30 seconds)

Distinguish multi-cloud by accident, DR backup, vs active-active. Acknowledge abstraction tax, egress costs, duplicated ops, and IAM sprawl. Recommend deliberate strategy: primary cloud + portable interfaces + tested exit — not lowest-common-denominator everywhere.

### Detailed Answer (3–5 minutes)

**Multi-cloud patterns:**
| Pattern | Description | Common? |
|---------|-------------|--------|
| Primary + DR | Prod Azure, DR failover AWS | Moderate |
| Acquisition blend | Integrate purchased company's cloud | Common |
| Active-active dual | Same workload both clouds | Rare, expensive |
| Portable K8s | EKS + AKS same manifests | Ops-heavy |

**Pitfalls to articulate:**
- Lowest-common-denominator services (self-managed everything)
- 2× operational expertise (Terraform multi-provider still ops burden)
- Cross-cloud egress fees
- Inconsistent security baselines
- 'Multi-cloud' without tested failover

**Mitigation strategies:**
1. Open formats — Parquet, OAuth, Postgres, Kubernetes
2. Abstraction at boundaries — S3-compatible API wrapper
3. Identity federation — Entra as IdP across clouds
4. DR runbooks tested quarterly

**Strong interview close:** 'We optimize for Azure time-to-market; DR objects in S3 with quarterly restore test; revisit if regulatory or contract requires active dual.'

### Architecture Perspective

Multi-cloud maturity is skepticism with valid exceptions — architects quantify cost and ops before endorsing dual active.

### Follow-up Questions

1. **Terraform multi-cloud? — Modules per provider — doesn't eliminate operational duplication.**
2. **Vendor negotiation? — Credible exit strategy improves pricing — pragmatic reason for portability.**

### Common Mistakes in Interviews

- Multi-cloud for buzzword compliance
- Active-active dual cloud without budget 2×
- No shared identity or observability plane

---

## Q005: Cloud Migration Interview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Migration |
| **Frequency** | Very Common |

### Question

How structure cloud migration answers using architect frameworks?

### Short Answer (30 seconds)

Use 6 Rs portfolio (rehost, replatform, refactor, repurchase, retire, retain), wave planning, dependency ordering, and explicit phase 2 modernization. Always state RTO/RPO, identity first, and landing zone prerequisites.

### Detailed Answer (3–5 minutes)

**6 Rs quick reference:**
| Strategy | When | Example |
|----------|------|--------|
| Rehost | Fast deadline, low change | VM → Azure VM (ASR) |
| Replatform | Managed wins | SQL Server → Azure SQL |
| Refactor | Strategic apps | Monolith → App Service + Functions |
| Repurchase | SaaS replaces custom | CRM → Dynamics 365 |
| Retire | Decommission zombie | Turn off unused LOB |
| Retain | Compliance/latency | Mainframe stays |

**Migration architecture sequence:**
1. **Assess** — Azure Migrate, dependency map, 6 R classification
2. **Foundation** — landing zone, identity, networking hub
3. **Wave 1** — low-risk rehost + retire quick wins
4. **Wave 2** — replatform databases, replatform middleware
5. **Wave 3** — refactor strategic workloads
6. **Operate** — FinOps, monitoring, security baseline

**Risks to mention:** Lift-shift cost surprise, license BYOL audit, latency assumptions, no rollback.

**Architect deliverable:** Migration ADR per app — R choice, cutover plan, rollback, phase 2 roadmap.

**Interview tip:** Give portfolio percentages — '70% rehost/replatform wave 1; 15% refactor over 18 months.'

### Architecture Perspective

Migration interviews test portfolio thinking — architects sequence waves and retain honesty about lift-shift limits.

### Follow-up Questions

1. **Azure Migrate / AWS MGN? — Discovery and replication tools — mention assessment phase.**
2. **Data migration cutover? — Minimal downtime strategies — DMS, transactional replication.**

### Common Mistakes in Interviews

- Refactor everything in wave one
- Migrate without landing zone or identity plan
- No retire — carry all technical debt to cloud

---

## Q006: Azure vs AWS Service Map

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Cloud |
| **Frequency** | Very Common |

### Question

Map equivalent Azure and AWS services for compute, storage, identity, and messaging.

### Short Answer (30 seconds)

Compute: App Service/AKS ↔ Elastic Beanstalk/EKS/ECS. Storage: Blob ↔ S3. Identity: Entra ID ↔ IAM/Cognito. Messaging: Service Bus/Event Hubs ↔ SQS/SNS/Kinesis.

### Detailed Answer (3–5 minutes)

| Capability | Azure | AWS |
|------------|-------|-----|
| VM | Virtual Machines | EC2 |
| PaaS web | App Service | Elastic Beanstalk |
| Kubernetes | AKS | EKS |
| Object storage | Blob Storage | S3 |
| SQL | Azure SQL | RDS |
| NoSQL | Cosmos DB | DynamoDB |
| IAM | Entra ID + RBAC | IAM |
| Queue | Service Bus | SQS |
| Events | Event Grid | EventBridge |
| Secrets | Key Vault | Secrets Manager |

**Architect:** Map by capability not name — migration and multi-cloud ADRs use this table. Note semantic gaps (Cosmos multi-model vs Dynamo key-value).

### Architecture Perspective

Service mapping proves cloud fluency beyond single-vendor cert trivia.

### Follow-up Questions

1. **Networking? — VNet/VNet peering ↔ VPC/VPC peering.**
2. **Serverless? — Functions ↔ Lambda.**

### Common Mistakes in Interviews

- Assuming 1:1 feature parity
- Ignoring identity model differences
- Choosing cloud by console familiarity only

---

## Q007: SQL Index Interview Question

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Database |
| **Frequency** | Very Common |

### Question

How do you decide what indexes to add on a slow SQL query?

### Short Answer (30 seconds)

Analyze execution plan, identify seek vs scan, high logical reads, missing index DMV hints. Index WHERE/JOIN/ORDER BY columns — leading column most selective. Balance write overhead.

### Detailed Answer (3–5 minutes)

**Steps:**
1. Capture slow query + actual execution plan
2. Check clustered vs nonclustered — PK clustered default
3. Covering index includes SELECT columns — avoid key lookups
4. Avoid over-indexing — each index slows INSERT/UPDATE

**Example:** `WHERE CustomerId = @id ORDER BY Created DESC` → composite index `(CustomerId, Created DESC)`.

**Architect:** Index strategy in capacity planning — review quarterly with workload changes.

### Architecture Perspective

Index interview wants methodology — plan analysis not 'add index on id'.

### Follow-up Questions

1. **Filtered index? — `WHERE Status = 'Active'` partial — smaller, faster.**
2. **Columnstore? — Analytics workloads — different indexing model.**

### Common Mistakes in Interviews

- Index every column
- Hint without measuring plan
- Ignoring index maintenance fragmentation

---

## Q008: Query Optimization Steps

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Database |
| **Frequency** | Very Common |

### Question

Walk through systematic SQL query optimization.

### Short Answer (30 seconds)

Measure baseline → examine plan → reduce rows early (filters, sargable predicates) → fix joins → add/revise indexes → consider partitioning → cache or materialize if read-heavy.

### Detailed Answer (3–5 minutes)

**Checklist:**
1. **Baseline** — duration, CPU, logical reads
2. **Sargability** — no `WHERE YEAR(Date)=2024` — use range
3. **Join order** — filter driving table first
4. **Statistics** — update stats if stale
5. **Parameter sniffing** — OPTION RECOMPILE or optimize for unknown
6. **Locking** — READ COMMITTED SNAPSHOT for read/write contention

**Architect:** 80% fix without hardware — document before/after metrics in perf ADR.

### Architecture Perspective

Structured optimization beats random index adding — show measurement discipline.

### Follow-up Questions

1. **N+1 at ORM layer? — Fix in app before DB tuning.**
2. **Read replica for reports? — Offload heavy analytics.**

### Common Mistakes in Interviews

- Optimize without baseline metrics
- SELECT * in hot paths
- Functions on indexed columns in WHERE

---

## Q009: Replication Lag Handling

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Database |
| **Frequency** | Very Common |

### Question

How handle read replica lag in production applications?

### Short Answer (30 seconds)

Route critical reads to primary, eventual reads to replica with stale tolerance UI, session stickiness after write (read-your-writes), or version tokens to detect stale data.

### Detailed Answer (3–5 minutes)

**Patterns:**
1. **Read-your-writes** — After POST, read from primary for 2s or by cookie
2. **Lag-aware routing** — If lag > threshold, fall back to primary
3. **UI honesty** — 'Data may take a minute to update'
4. **CQRS** — Projections async — user expects delay

**Monitor:** `replica_lag_seconds` alert > 30s.

**Architect:** Payment balance always primary — product catalog OK on 30s stale replica.

### Architecture Perspective

Replication lag is consistency trade-off — architects classify reads by tolerance.

### Follow-up Questions

1. **Global replication? — Cosmos/AWS Global Tables — conflict resolution rules.**
2. **Automatic failover? — Promote replica — RPO/RTO implications.**

### Common Mistakes in Interviews

- Assume replica is always current
- No lag monitoring
- Financial reads from async replica always

---

## Q010: Sharding Interview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Database |
| **Frequency** | Very Common |

### Question

How would you shard a multi-tenant SaaS database?

### Short Answer (30 seconds)

Choose shard key (tenantId), route via lookup service or consistent hash, avoid cross-shard joins, plan resharding, replicate per shard for HA.

### Detailed Answer (3–5 minutes)

**Strategies:**
- **Tenant-per-shard** — enterprise tenants isolated
- **Hash(tenantId) % N** — even spread — hot tenant risk
- **Geo shard** — EU tenants EU shard — compliance

**Components:**
- Router middleware adds shard context
- Global index for email → tenantId lookup
- Cross-shard reports via map-reduce or warehouse

**Architect:** Start single DB until >1TB or noisy neighbor — premature sharding hurts.

### Architecture Perspective

Sharding interview tests shard key choice and operational pain awareness.

### Follow-up Questions

1. **Vitess/Citus? — Managed sharding layers reduce custom router code.**
2. **Hot shard? — Split tenant or salting keys.**

### Common Mistakes in Interviews

- Cross-shard JOIN in OLTP
- Shard key changes later without plan
- No single place for routing logic

---

## Q011: CAP Theorem Interview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Distributed Systems |
| **Frequency** | Very Common |

### Question

Explain CAP theorem and give a real cloud trade-off example.

### Short Answer (30 seconds)

In partition, choose Consistency or Availability (not both). AP: DynamoDB eventual, DNS. CP: etcd, Zookeeper, strong SQL primary during split. Most systems are PA with tunable C.

### Detailed Answer (3–5 minutes)

**During network partition:**
- **CP** — refuse writes or minority partition read-only (bank ledger)
- **AP** — accept writes both sides, reconcile later (shopping cart merge)

**PACELC:** Else latency vs consistency — normal operation trade-off too.

**Azure example:** Cosmos DB consistency levels — Strong vs Session vs Eventual.

**Architect:** Document per bounded context — payments CP, analytics AP.

### Architecture Perspective

CAP is about partition behavior — not 'pick two of three always'.

### Follow-up Questions

1. **Kafka CAP? — AP with ordering per partition — nuanced.**
2. **Multi-region SQL? — CP with failover — availability hit on partition.**

### Common Mistakes in Interviews

- CAP means ignore consistency
- Same CAP choice for all services
- No partition failure in design discussion

---

## Q012: Multi-Cloud Pitfalls

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Cloud Strategy |
| **Frequency** | Common |

### Question

What are common pitfalls of multi-cloud architecture?

### Short Answer (30 seconds)

Lowest-common-denominator services, duplicated ops expertise, complex networking, inconsistent security, data egress costs, and no single observability — often 2× cost for portability rarely exercised.

### Detailed Answer (3–5 minutes)

**Pitfalls:**
- Abstraction tax (custom K8s on both vs managed PaaS)
- Split brain DR untested
- Different IAM models — role sprawl
- Egress between clouds expensive

**When justified:** Regulatory, acquisition integration, negotiate vendor pricing.

**Architect:** Multi-cloud by design vs accident — active-active multi-cloud is rare; backup DR in second cloud more common.

### Architecture Perspective

Multi-cloud skepticism with valid use cases shows maturity.

### Follow-up Questions

1. **Terraform multi-provider? — Modules per cloud — still ops burden.**
2. **Exit strategy vs multi-cloud active? — Exit ≠ run equally on two.**

### Common Mistakes in Interviews

- Multi-cloud for buzzword compliance
- No shared identity plane
- Untested failover between clouds

---

## Q013: Cloud Migration 6 Rs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Migration |
| **Frequency** | Very Common |

### Question

Explain the 6 Rs of cloud migration with examples.

### Short Answer (30 seconds)

Rehost (lift-shift), Replatform (managed DB), Repurchase (SaaS), Refactor (cloud-native), Retire (decommission), Retain (keep on-prem).

### Detailed Answer (3–5 minutes)

| R | Action | Example |
|---|--------|--------|
| Rehost | VM to Azure VM | Fast, least benefit |
| Replatform | SQL Server to Azure SQL | Managed patches |
| Repurchase | CRM to Dynamics 365 | SaaS replace custom |
| Refactor | Monolith to microservices | Max cloud value |
| Retire | Turn off unused app | Cost save |
| Retain | Mainframe stays | Compliance/latency |

**Architect:** Portfolio assessment — 70% rehost/replatform wave 1, refactor strategic apps wave 2.

### Architecture Perspective

6 Rs framework structures migration portfolio conversations.

### Follow-up Questions

1. **7th R — Relocate? — VMware to AVS — sometimes added.**
2. **Wave planning? — Dependency order — identity first.**

### Common Mistakes in Interviews

- Refactor everything day one
- No retire — migration without decommission
- Ignore retain compliance constraints

---

## Q014: Lift and Shift Risks

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Migration |
| **Frequency** | Very Common |

### Question

What risks come with lift-and-shift migration to cloud?

### Short Answer (30 seconds)

Bringing datacenter inefficiency to cloud OpEx, no auto-scale, license mismatch, wrong VM sizing, latent dependencies on LAN, and security groups misconfigured for internet exposure.

### Detailed Answer (3–5 minutes)

**Risks:**
- **Cost surprise** — oversized VMs 24/7 vs right-sized PaaS
- **HA illusion** — single VM in cloud still SPOF
- **Latency** — app assumes local SQL sub-ms
- **Licensing** — BYOL vs pay-as-you-go audit
- **Ops model** — no patch automation

**Mitigation:** Assess with Azure Migrate, pilot non-prod, implement monitoring before cutover.

**Architect:** Lift-shift is valid phase 1 with explicit phase 2 modernization roadmap.

### Architecture Perspective

Lift-shift risk awareness prevents 'cloud is more expensive' backlash.

### Follow-up Questions

1. **ASR replication? — Test failover quarterly.**
2. **Network latency profiling? — Measure before move.**

### Common Mistakes in Interviews

- Assume cloud magically scales legacy app
- Public RDP on migrated VM
- No rollback plan

---

## Q015: Refactor vs Rehost

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Migration |
| **Frequency** | Common |

### Question

When recommend refactor vs rehost for a legacy .NET monolith?

### Short Answer (30 seconds)

Rehost when deadline tight, app stable, team lacks microservices skill. Refactor when scalability blocked, release cadence slow, or cloud services (managed identity, Service Bus) unlock major value.

### Detailed Answer (3–5 minutes)

**Decision matrix:**
| Factor | Rehost | Refactor |
|--------|--------|----------|
| Timeline | Months | 12–24 months |
| Business change rate | Low | High |
| Scale pain | Moderate | Severe |
| Team maturity | Ops-focused | Platform team ready |

**Strangler fig:** Rehost first, extract hot paths to microservices incrementally.

**Architect:** ADR per application — not one strategy for entire portfolio.

### Architecture Perspective

Refactor vs rehost is business timeline question — not technical purity.

### Follow-up Questions

1. **Containerize without refactor? — Replatform middle ground.**
2. **ROI proof for refactor? — Release frequency, incident cost.**

### Common Mistakes in Interviews

- Big-bang rewrite
- Rehost without monitoring baseline
- Refactor without domain boundaries identified

---

## Q016: Data Migration Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Migration |
| **Frequency** | Very Common |

### Question

Design data migration strategy with minimal downtime.

### Short Answer (30 seconds)

Dual-write or CDC replication, migrate historical batch, verify checksums, cutover with DNS/connection switch, rollback window, freeze writes briefly if needed.

### Detailed Answer (3–5 minutes)

**Phases:**
1. **Schema sync** — target schema ready
2. **Initial load** — bulk copy off-peak
3. **CDC** — DMS/ADF catch-up replication
4. **Verify** — row counts, hash samples, reconciliation reports
5. **Cutover** — read-only window, final sync, flip connection strings
6. **Rollback** — keep source read-only 48h

**Architect:** Test migration dry-run monthly — measure lag and duration.

### Architecture Perspective

Data migration is highest-risk migration phase — detail cutover and verify.

### Follow-up Questions

1. **Azure DMS? — Online migration SQL to Azure SQL.**
2. **Large BLOB data? — AzCopy parallel — separate from DB.**

### Common Mistakes in Interviews

- Big-bang copy production day one
- No reconciliation counts
- Cutover without tested rollback

---

## Q017: Blue-Green Database

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Migration |
| **Frequency** | Common |

### Question

How apply blue-green deployment to database changes?

### Short Answer (30 seconds)

Blue runs old schema, green new — expand-contract pattern: deploy backward-compatible schema first, dual-write, backfill, switch app to green, remove old columns later.

### Detailed Answer (3–5 minutes)

**Expand-contract:**
1. Add new column (nullable)
2. Deploy app writing both
3. Backfill job
4. Deploy app reading new
5. Drop old column

**Not:** Two full DB copies for every release — expensive. Blue-green DB means schema compatibility strategy.

**Architect:** Flyway/Liquibase versioned migrations in CI — no manual prod DDL.

### Architecture Perspective

Blue-green DB is expand-contract — not literal duplicate databases every deploy.

### Follow-up Questions

1. **Feature flags with schema? — Flag reads new column when ready.**
2. **Breaking rename? — View layer compatibility shim.**

### Common Mistakes in Interviews

- Renaming column in one deploy
- Long transaction blocking cutover
- No backward compatible migrations

---

## Q018: Connection Pooling Cloud

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Database |
| **Frequency** | Very Common |

### Question

Why connection pooling matters in cloud PaaS databases and what breaks it?

### Short Answer (30 seconds)

Pools reuse TCP+auth handshakes — critical at scale. Broken by: too many app instances each opening max pool, long idle timeouts, opening connection per request without dispose, serverless scale-out explosion.

### Detailed Answer (3–5 minutes)

**Azure SQL:** Gateway connection pooling, app-side `Max Pool Size` tuning. **PgBouncer** for PostgreSQL.

**Anti-patterns:**
- 50 AKS pods × 100 pool = 5000 connections — exceeds DTU limit
- `Pooling=false` in connection string
- Serverless Functions default pool per instance — use RDS proxy/Azure SQL middle tier

**Architect:** Central pooler or limit pod max connections — monitor `connection_failed` metrics.

### Architecture Perspective

Cloud DB connection limits bite at scale — pooling math is interview gold.

### Follow-up Questions

1. **EF Core DbContext pooling? — Reuse context internals — not same as ADO pool.**
2. **Connection string per request? — Always from config — rotate via Key Vault.**

### Common Mistakes in Interviews

- Exhaust DTU with connection storm
- New connection string per tenant uncapped
- Ignore pool metrics in AKS scale events

---

## Q019: Serverless Cold Start

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Serverless |
| **Frequency** | Very Common |

### Question

What causes serverless cold start and how mitigate for latency-sensitive APIs?

### Short Answer (30 seconds)

Cold start: provision runtime, load dependencies, JIT (.NET), VPC attach. Mitigate: always-on instances, smaller packages, managed identity, premium plan, warmup pings, avoid huge DI graph.

### Detailed Answer (3–5 minutes)

**.NET Azure Functions:**
- **Premium plan** — pre-warmed instances
- **ReadyToRun** compilation
- Trim dependencies
- Avoid VPC unless needed — ENI attach adds seconds

**Lambda:** Provisioned concurrency, ARM Graviton, smaller handler.

**Architect:** If p99 < 200ms SLA — serverless may need premium tier or container always-on.

### Architecture Perspective

Cold start is architecture constraint — not just 'use serverless'.

### Follow-up Questions

1. **Consumption plan when? — Sporadic batch — cold OK.**
2. **.NET isolated worker? — Faster startup than in-process sometimes.**

### Common Mistakes in Interviews

- Serverless for synchronous user-facing without premium
- 500MB deployment package
- Cold start surprise in load test

---

## Q020: IAM Least Privilege

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

How implement least privilege IAM in Azure and AWS?

### Short Answer (30 seconds)

Grant minimum roles per workload identity — managed identity for app, scoped RBAC (Storage Blob Data Contributor on one container), deny assignments at subscription, regular access reviews, no long-lived keys.

### Detailed Answer (3–5 minutes)

**Azure:**
- Workload uses **managed identity**
- `azurerm_role_assignment` scoped to resource group
- PIM for human admin just-in-time

**AWS:**
- IAM role per Lambda/EC2 instance profile
- Policy with specific `arn:aws:s3:::bucket/prefix/*`

**Architect:** Break-glass account separate — audit quarterly. CI validates Terraform IAM policies.

### Architecture Perspective

Least privilege is identity architecture — default deny, scope resources.

### Follow-up Questions

1. **Permission boundaries? — AWS cap max permissions delegate.**
2. **Entra Conditional Access? — Human access layer.**

### Common Mistakes in Interviews

- Contributor at subscription for app identity
- Shared service principal all environments
- Access keys in app settings

---

## Q021: Landing Zone Interview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Cloud Architecture |
| **Frequency** | Very Common |

### Question

What is a cloud landing zone and what pillars does it include?

### Short Answer (30 seconds)

Landing zone: governed multi-account/subscription foundation — identity, networking hub-spoke, security baseline, logging, policy guardrails, before workloads land.

### Detailed Answer (3–5 minutes)

**Pillars (CAF/ALZ):**
1. **Identity** — Entra tenant, RBAC, PIM
2. **Networking** — Hub VNet, firewall, DNS
3. **Security** — Defender, Policy, Key Vault
4. **Governance** — Management groups, tags, budgets
5. **Operations** — Log Analytics, alert routing

**Azure Landing Zone** — Enterprise-scale reference architecture.

**Architect:** Platform team owns landing zone — app teams deploy into spoke subscriptions.

### Architecture Perspective

Landing zone separates platform engineering from app delivery — enterprise interview staple.

### Follow-up Questions

1. **Policy as code? — Azure Policy deny public IP on NIC.**
2. **Subscription vending? — Automated spoke per team via Terraform.**

### Common Mistakes in Interviews

- App teams define own networking ad hoc
- No centralized logging subscription
- Skip policy guardrails for speed

---

## Q022: Cost Optimization Interview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | FinOps |
| **Frequency** | Very Common |

### Question

Name cloud cost optimization strategies beyond 'turn off VMs'.

### Short Answer (30 seconds)

Right-sizing, reserved instances/savings plans, spot for batch, storage tiering, autoscale schedules, tagging/chargeback, eliminate zombie resources, serverless for spiky, CDN egress reduction.

### Detailed Answer (3–5 minutes)

**Tactics:**
- **Azure Advisor** recommendations
- **Dev/test pricing** for non-prod
- **Auto-shutdown** schedules
- **Blob lifecycle** to cool/archive
- **Commitment discounts** 1–3 year after baseline stable

**Culture:** FinOps dashboard per team — accountability.

**Architect:** Cost is NFR — design review includes $/month estimate like latency.

### Architecture Perspective

Cost optimization shows operational maturity — specific levers not generic advice.

### Follow-up Questions

1. **Unit economics? — $ per transaction — tie scale to revenue.**
2. **Egress cost? — Same-region traffic, CDN, compress payloads.**

### Common Mistakes in Interviews

- Reserved instances day one before baseline
- No tags — cannot allocate spend
- Over-provision 'for safety' forever

---

## Q023: Hybrid Cloud Connectivity

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Networking |
| **Frequency** | Common |

### Question

Design hybrid connectivity between on-prem and Azure.

### Short Answer (30 seconds)

ExpressRoute (private dedicated) or VPN (IPsec) to hub VNet, DNS resolution for private endpoints, route tables, no hairpin through internet for DB traffic.

### Detailed Answer (3–5 minutes)

**Options:**
- **ExpressRoute** — predictable latency, SLA, no internet
- **Site-to-Site VPN** — cheaper, internet dependent
- **ExpressRoute + VPN** — backup path

**Services:** Azure Arc for on-prem K8s/SQL management plane.

**Architect:** Hub-spoke — on-prem connects to hub only — spokes peer through hub firewall policies.

### Architecture Perspective

Hybrid design tests networking and security zoning — not just 'VPN yes'.

### Follow-up Questions

1. **Private Link? — PaaS over private IP — no public endpoint.**
2. **DNS hybrid? — Conditional forwarders — split brain risk.**

### Common Mistakes in Interviews

- Flat network all on-prem and cloud
- RDP over public internet for admin
- No redundant VPN/ER path

---

## Q024: Blob vs File Storage

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Storage |
| **Frequency** | Common |

### Question

When choose blob storage vs file storage in Azure?

### Short Answer (30 seconds)

Blob: object storage for unstructured data — images, backups, data lake, static websites. Azure Files: SMB/NFS shared file system — lift-and-shift apps needing file share, legacy ISV.

### Detailed Answer (3–5 minutes)

| | Blob | Azure Files |
|---|------|-------------|
| Protocol | REST | SMB/NFS |
| Use | Objects, analytics | Shared drive |
| Scale | Massive | Moderate share |
| Cost | Lower per GB hot | Premium for low latency |

**Architect:** New cloud-native → blob. .NET app with `\\server\share` → Files or refactor to blob SDK.

### Architecture Perspective

Storage choice maps to access pattern — object vs POSIX file semantics.

### Follow-up Questions

1. **ADLS Gen2? — Blob with hierarchical namespace for Spark.**
2. **Lifecycle tiers? — Hot/cool/archive on blob.**

### Common Mistakes in Interviews

- Files for static website hosting
- Blob when app needs file locking SMB semantics
- Ignore egress on frequent small reads

---

## Q025: Event-Driven Cloud

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Architecture |
| **Frequency** | Very Common |

### Question

Design event-driven architecture on Azure.

### Short Answer (30 seconds)

Producers publish to Event Grid/Service Bus/Event Hubs, consumers idempotent, schema registry, dead-letter queues, outbox from transactional systems.

### Detailed Answer (3–5 minutes)

**Patterns:**
- **Event notification** — Blob created → Function processes
- **Event-carried state** — minimal payload + lookup
- **Choreography** — subscribers react — vs orchestration (Logic Apps)

**Components:** APIM → API → outbox table → publisher → Service Bus topic → multiple subscribers.

**Architect:** Define event contract versioning — additive schema changes only.

### Architecture Perspective

Event-driven is decoupling strategy — include failure and ordering semantics.

### Follow-up Questions

1. **Service Bus vs Event Hubs? — Messages vs streaming telemetry scale.**
2. **Idempotent consumer? — Dedup by eventId store.**

### Common Mistakes in Interviews

- Synchronous chain of 6 HTTP calls instead
- No dead-letter monitoring
- Breaking event schema without version

---

## Q026: Disaster Recovery Interview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Reliability |
| **Frequency** | Very Common |

### Question

Design disaster recovery for a tier-1 cloud application.

### Short Answer (30 seconds)

Define RTO/RPO, active-passive or active-active multi-region, automated failover (Traffic Manager/Front Door), regular game days, backup encryption, runbook tested quarterly.

### Detailed Answer (3–5 minutes)

**Tiers:**
- **Active-passive** — secondary warm standby — lower cost
- **Active-active** — both regions serve — data sync harder

**Data:** Geo-redundant storage, SQL geo-replication, Cosmos multi-region writes with conflict policy.

**Architect:** DR is tested procedure — backup without restore test is wishful thinking.

### Architecture Perspective

DR interview requires RTO/RPO numbers and failover mechanics.

### Follow-up Questions

1. **Pilot light? — Minimal secondary — scale on failover.**
2. **Chaos engineering? — Inject region failure in staging.**

### Common Mistakes in Interviews

- Backup never restored in test
- Single region with 'we'll rebuild'
- Manual failover untested 18 months

---

## Q027: RTO RPO Calculation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Reliability |
| **Frequency** | Very Common |

### Question

How calculate and negotiate RTO and RPO with stakeholders?

### Short Answer (30 seconds)

RPO: max acceptable data loss (time between backups). RTO: max downtime. Derive from business impact $/hour, then map to architecture cost.

### Detailed Answer (3–5 minutes)

**Example:**
- E-commerce checkout: RPO 0, RTO 15 min → sync replication, hot standby
- Internal HR portal: RPO 24h, RTO 8h → nightly backup, rebuild VM

**Calculation:**
`RPO drives backup frequency`. `RTO drives hot/warm/cold standby`.

**Cost:** RPO 0 multi-region active-active costs 2×+ infra.

**Architect:** Document tier per application — not one SLA for entire estate.

### Architecture Perspective

RTO/RPO links business to engineering — quantify don't hand-wave.

### Follow-up Questions

1. **WRT RPO? — Work Recovery Time — process not just tech.**
2. **Compliance minimum? — HIPAA may mandate — floor not ceiling.**

### Common Mistakes in Interviews

- Same RTO for all apps
- RPO zero without budget discussion
- Confuse backup retention with RPO

---

## Q028: Compliance Cloud Interview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Compliance |
| **Frequency** | Common |

### Question

How address compliance (SOC2, HIPAA, GDPR) in cloud architecture?

### Short Answer (30 seconds)

Shared responsibility model, data residency region selection, encryption at rest/transit, audit logging, DPA with vendor, access controls, retention policies, breach notification process.

### Detailed Answer (3–5 minutes)

**Controls:**
- **SOC2** — change management, logging, access reviews
- **HIPAA** — BAA, PHI encryption, audit trails
- **GDPR** — lawful basis, right to erasure, DPO

**Azure:** Policy initiatives, Compliance Manager score, private endpoints.

**Architect:** Compliance by design in landing zone — app teams inherit baseline controls.

### Architecture Perspective

Compliance is shared responsibility — know what cloud provides vs you configure.

### Follow-up Questions

1. **Data residency? — EU data in EU region — no silent replication US.**
2. **Encryption customer-managed keys? — CMK in Key Vault for regulated.**

### Common Mistakes in Interviews

- Assume cloud cert means app compliant
- PII in logs unredacted
- No data processing agreement

---

## Q029: Vendor Lock-In Response

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Strategy |
| **Frequency** | Common |

### Question

How respond to vendor lock-in concerns in architecture review?

### Short Answer (30 seconds)

Acknowledge trade-off: managed services accelerate delivery but increase switch cost. Mitigate with portable interfaces (Kubernetes, Postgres), open formats (Parquet, OAuth), exit plan for tier-0 data, avoid proprietary DSL deep in core.

### Detailed Answer (3–5 minutes)

**Mitigation levels:**
1. **Accept lock-in** — Cosmos DB — document business value
2. **Abstraction** — S3-compatible API wrapper
3. **Multi-cloud** — only where regulatory demands

**Interview answer:** 'We optimize for time-to-market on Azure with open API contracts and data export quarterly tested.'

**Architect:** Lock-in risk register — severity × likelihood.

### Architecture Perspective

Balanced lock-in answer shows pragmatism — neither zealot portable nor blind native.

### Follow-up Questions

1. **Open source on cloud? — Still ops lock-in on managed K8s.**
2. **Data portability test? — Quarterly export to neutral format.**

### Common Mistakes in Interviews

- Fear of all managed services
- Proprietary format core business data no export
- Lock-in ignored in ADR

---

## Q030: Cloud Architecture Whiteboard

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Interview Skills |
| **Frequency** | Very Common |

### Question

How structure a cloud architecture whiteboard interview in 45 minutes?

### Short Answer (30 seconds)

Requirements 5 min → high-level diagram 10 min → deep dive critical path 15 min → security/ops 10 min → trade-offs and evolution 5 min. Label managed services, data flows, trust boundaries.

### Detailed Answer (3–5 minutes)

**Layers to draw:**
1. Users/CDN/WAF
2. API gateway
3. Compute (App Service/AKS)
4. Data (SQL, cache, blob)
5. Messaging
6. Identity, Key Vault
7. Observability

**Say aloud:** 'I'll use Azure Front Door for global entry...'

**Architect:** Call out single points of failure and how you'd eliminate them in phase 2.

### Architecture Perspective

Whiteboard pacing separates prepared candidates — practice timed mocks.

### Follow-up Questions

1. **C4 model? — Context then container — don't drill components too early.**
2. **Cost mention? — Rough monthly estimate impresses.**

### Common Mistakes in Interviews

- Jump to EC2 instances without requirements
- Single box 'database' unlabeled
- Ignore security and monitoring until asked

---
