# Week 46 — Intermediate Q&A

> Q031–Q070: Premium format (Week 1 quality).

---


## Q031: Clustered vs Nonclustered Index

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SQL Indexing |
| **Frequency** | Very Common |

### Question

Difference between clustered and nonclustered indexes in SQL Server?

### Short Answer (30 seconds)

Clustered index defines table row order — one per table (usually PK). Nonclustered index is separate structure with pointer to row — many allowed.

### Detailed Answer (3–5 minutes)

**Clustered:** Table data is B+ tree sorted by key — range scans efficient.

**Nonclustered:** Leaf contains key + row locator (bookmark or clustered key).

**Covering index:** Nonclustered includes all query columns — no key lookup.

**Architect:** Choose clustered key on common range filter — often identity or time-series insert pattern.

### Architecture Perspective

Index types drive SQL performance fundamentals.

### Follow-up Questions

1. **Heap table? — No clustered — nonclustered uses RID lookup.**
2. **GUID clustered key? — Random insert fragmentation — consider sequential GUID.**

### Common Mistakes in Interviews

- Multiple clustered indexes
- Clustered on low-cardinality column alone
- Ignore fill factor on heavy insert tables

---

## Q032: Composite Index Column Order

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SQL Indexing |
| **Frequency** | Very Common |

### Question

How does column order matter in composite indexes?

### Short Answer (30 seconds)

Leftmost prefix rule — index (A, B, C) helps `WHERE A=?`, `WHERE A=? AND B=?`, not `WHERE B=?` alone.

### Detailed Answer (3–5 minutes)

**Example:** `WHERE CustomerId = @id ORDER BY Created DESC`
→ Index `(CustomerId, Created DESC)`.

**Selectivity:** Most selective leading column often best — but consider equality before range columns.

**Architect:** Review top 10 slow queries quarterly — index order follows query patterns.

### Architecture Perspective

Composite index design is practical DBA architect skill.

### Follow-up Questions

1. **Include columns? — Covering index — INCLUDE clause non-key columns.**
2. **Filtered index? — `WHERE Status = 'Active'` — smaller index.**

### Common Mistakes in Interviews

- Wrong column order in composite
- Index every column individually instead
- Index without query workload analysis

---

## Q033: Covering Index Interview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SQL Indexing |
| **Frequency** | Common |

### Question

What is a covering index and when use INCLUDE columns?

### Short Answer (30 seconds)

Covering index contains all columns needed by query — SQL satisfies query from index alone without key lookup to table.

### Detailed Answer (3–5 minutes)

```sql
CREATE INDEX IX_Orders_Customer
ON Orders (CustomerId)
INCLUDE (Total, Status, Created);
```

**Benefit:** Eliminates nested loop key lookup — big read reduction.

**Cost:** Wider index — more write overhead.

**Architect:** Cover hot read queries identified in execution plans.

### Architecture Perspective

Covering indexes are high-impact read optimization.

### Follow-up Questions

1. **Key lookup in plan? — Signal missing INCLUDE or wrong index.**
2. **Over-covering? — Too wide indexes slow writes.**

### Common Mistakes in Interviews

- SELECT * preventing cover
- INCLUDE on huge varchar columns wastefully
- No plan analysis before adding INCLUDE

---

## Q034: Index Sargability

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SQL Indexing |
| **Frequency** | Very Common |

### Question

What makes a SQL predicate non-sargable?

### Short Answer (30 seconds)

Functions on indexed column prevent seek — `WHERE YEAR(OrderDate)=2024` scans. Use range: `OrderDate >= '2024-01-01' AND OrderDate < '2025-01-01'`.

### Detailed Answer (3–5 minutes)

**Non-sargable examples:**
- `LIKE '%abc'` leading wildcard
- `Column + 1 = 5`
- `CONVERT(date, Column)`

**Fix:** Computed persisted column indexed separately if needed.

**Architect:** ORM-generated SQL review — EF can produce non-sargable expressions.

### Architecture Perspective

Sargability is silent index killer in ORM apps.

### Follow-up Questions

1. **Implicit conversion? — nvarchar vs varchar — scan.**
2. **Collation mismatch? — Index not used — plan shows CONVERT.**

### Common Mistakes in Interviews

- Functions on indexed columns in WHERE
- Leading wildcard LIKE
- Ignore ORM SQL in reviews

---

## Q035: Azure Compute Service Map

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Azure |
| **Frequency** | Very Common |

### Question

Map Azure compute options to workload types.

### Short Answer (30 seconds)

VMs for full control, App Service for web APIs, AKS for container orchestration, Functions for event-driven, Container Apps for simpler K8s-less containers.

### Detailed Answer (3–5 minutes)

| Workload | Azure |
|----------|-------|
| Legacy monolith | VM / App Service |
| Microservices K8s | AKS |
| HTTP API scale-to-zero | Functions / Container Apps |
| Batch | VMSS / AKS jobs |

**Architect:** Default .NET API to App Service or Container Apps unless K8s features required.

### Architecture Perspective

Compute selection is first cloud architecture decision.

### Follow-up Questions

1. **App Service vs AKS? — Ops burden vs control trade-off.**
2. **Azure Spring Apps? — Java-focused — mention if polyglot.**

### Common Mistakes in Interviews

- VM for every microservice
- AKS for two static containers
- Functions for long-running sync API

---

## Q036: Azure Data Service Map

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Azure |
| **Frequency** | Very Common |

### Question

Choose between Azure SQL, Cosmos DB, and PostgreSQL.

### Short Answer (30 seconds)

Azure SQL for relational ACID OLTP. Cosmos for global low-latency NoSQL with SLAs. PostgreSQL for open-source relational + extensions.

### Detailed Answer (3–5 minutes)

**Azure SQL:** Familiar T-SQL, geo-replication, managed patches.

**Cosmos:** Partition key design critical — multi-model APIs.

**PostgreSQL:** Flexible extensions (PostGIS), AKS sidecar patterns.

**Architect:** Match consistency model and query pattern — not resume familiarity only.

### Architecture Perspective

Data store selection drives application architecture.

### Follow-up Questions

1. **Synapse? — Analytics warehouse — not OLTP.**
2. **Table Storage? — Simple key-value — not SQL replacement.**

### Common Mistakes in Interviews

- Cosmos for relational joins heavy workload
- SQL Server on VM when Azure SQL fits
- One database technology for everything

---

## Q037: Azure Messaging Map

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Azure |
| **Frequency** | Common |

### Question

When Service Bus vs Event Hubs vs Event Grid?

### Short Answer (30 seconds)

Service Bus: enterprise messaging, queues, topics, transactions. Event Hubs: high-throughput streaming ingestion. Event Grid: reactive event routing and fan-out.

### Detailed Answer (3–5 minutes)

**Service Bus:** Order processing, competing consumers, dead-letter.

**Event Hubs:** Telemetry, Kafka-compatible streaming.

**Event Grid:** Blob created, resource events — push notification model.

**Architect:** Choreography with Event Grid + Service Bus; streaming analytics with Event Hubs.

### Architecture Perspective

Messaging product choice affects ordering and scale.

### Follow-up Questions

1. **Queue vs topic? — Single consumer vs pub/sub.**
2. **Sessions? — Service Bus ordered delivery per session key.**

### Common Mistakes in Interviews

- Event Hubs for task queue workload
- Service Bus for billion event telemetry
- No dead-letter on Service Bus subscription

---

## Q038: AWS EC2 vs Azure VM

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Cloud Comparison |
| **Frequency** | Common |

### Question

Compare AWS EC2 and Azure Virtual Machines for architects.

### Short Answer (30 seconds)

Both IaaS VMs with similar concepts — instance types, scale sets/VMSS, disks, NICs. Differences in marketplace, hybrid (Arc/SSM), licensing (AHUB), and regional footprint.

### Detailed Answer (3–5 minutes)

**Azure advantage:** Hybrid benefit, Entra integration, Arc hybrid management.

**AWS advantage:** Broader service catalog maturity in some regions, Graviton price/perf.

**Architect:** Map instance families to workload — compute optimized vs memory optimized.

### Architecture Perspective

IaaS comparison is migration and multi-cloud literacy.

### Follow-up Questions

1. **Spot vs Azure Spot? — Interruptible cheap capacity — batch jobs.**
2. **Reserved instances both clouds? — Commitment discounts.**

### Common Mistakes in Interviews

- Assume identical pricing
- Ignore hybrid licensing
- Pick VM size without profiling

---

## Q039: AWS S3 vs Azure Blob

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Cloud Comparison |
| **Frequency** | Very Common |

### Question

Compare S3 and Azure Blob Storage capabilities.

### Short Answer (30 seconds)

Both object storage — REST API, tiers (hot/cool/archive), lifecycle policies, versioning, encryption. S3 has wider ecosystem tooling; Blob integrates Entra RBAC and Private Link.

### Detailed Answer (3–5 minutes)

| Feature | S3 | Blob |
|---------|----|----- |
| Tiers | Standard/IA/Glacier | Hot/Cool/Archive |
| ACL vs RBAC | ACL + IAM | Entra RBAC preferred |
| Events | S3 Event Notifications | Event Grid |

**Architect:** Abstraction via S3-compatible SDK patterns if portability required.

### Architecture Perspective

Object storage comparison appears in multi-cloud interviews.

### Follow-up Questions

1. **ADLS Gen2? — Hierarchical namespace on blob — analytics.**
2. **MinIO on-prem? — S3 API compatible — hybrid.**

### Common Mistakes in Interviews

- Blob when POSIX SMB needed
- Public container anonymous by default
- Ignore lifecycle tiering cost

---

## Q040: AWS IAM vs Azure RBAC

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Cloud Comparison |
| **Frequency** | Very Common |

### Question

Compare AWS IAM and Azure RBAC models.

### Short Answer (30 seconds)

AWS IAM: users, roles, policies JSON attached to identities/resources. Azure RBAC: role definitions at management group/subscription/RG/resource scope with deny assignments and PIM.

### Detailed Answer (3–5 minutes)

**AWS:** Role assumed by EC2/Lambda instance profile.

**Azure:** Managed identity + role assignment on resource scope.

**Both:** Least privilege, no long-lived keys, audit logs (CloudTrail / Activity Log).

**Architect:** Map workload identity pattern — role per service not shared admin.

### Architecture Perspective

Identity models differ — architects learn both for interviews.

### Follow-up Questions

1. **ABAC? — AWS attribute-based; Azure ABAC preview conditions.**
2. **Break-glass account? — Both clouds need emergency access procedure.**

### Common Mistakes in Interviews

- Root account daily use AWS
- Contributor subscription-wide for app
- Shared access keys in code

---

## Q041: Rehost Migration Step

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Migration |
| **Frequency** | Very Common |

### Question

What is rehost in the 6 Rs and when use it?

### Short Answer (30 seconds)

Rehost (lift-and-shift): move VM/app to cloud unchanged — Azure Migrate, ASR replication. Fastest migration, least cloud optimization.

### Detailed Answer (3–5 minutes)

**When:** Deadline driven, legacy app stable, phase 1 of journey.

**Tooling:** Azure Migrate assessment → ASR replication → cutover.

**Architect:** Pair with phase 2 modernization roadmap — rehost is not end state.

### Architecture Perspective

6 Rs vocabulary structures migration conversations.

### Follow-up Questions

1. **Rehost vs replatform? — Rehost unchanged; replatform managed service swap.**
2. **Mainframe rehost? — Emulation or refactor — different timeline.**

### Common Mistakes in Interviews

- Rehost without assessment sizing
- Assume auto-scale after lift unchanged
- No phase 2 plan

---

## Q042: Replatform Example

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Migration |
| **Frequency** | Common |

### Question

Give replatform example for .NET SQL Server workload.

### Short Answer (30 seconds)

Move SQL Server on VM to Azure SQL Database or SQL Managed Instance — same app, managed database patches and backups.

### Detailed Answer (3–5 minutes)

**Steps:**
1. DMA/SQL assessment compatibility
2. Choose PaaS tier (vCore, DTU)
3. Migrate schema + data (DMS)
4. Update connection string
5. Retire VM SQL

**Benefits:** Patch automation, geo-restore, reduced ops.

**Architect:** MI when need SQL Agent near-full compatibility.

### Architecture Perspective

Replatform is common .NET migration sweet spot.

### Follow-up Questions

1. **Elastic pool? — Multi-tenant DB cost optimization.**
2. **Managed Instance vs Azure SQL? — Feature compatibility vs simplicity.**

### Common Mistakes in Interviews

- Replatform app without DB assessment
- Wrong tier oversized forever
- Ignore connection pool limits change

---

## Q043: Refactor Cloud Native

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Migration |
| **Frequency** | Common |

### Question

What does refactor mean in 6 Rs for a .NET monolith?

### Short Answer (30 seconds)

Decompose to microservices, adopt managed services (Service Bus, Key Vault), containers, CI/CD, observability — maximize cloud value.

### Detailed Answer (3–5 minutes)

**Signals to refactor:** Deploy bottleneck, scale one module only, team scaling.

**Approach:** Strangler fig — extract payment service first.

**Architect:** Refactor highest ROI bounded context — not entire monolith at once.

### Architecture Perspective

Refactor is strategic — timeline and skill dependent.

### Follow-up Questions

1. **Repurchase? — SaaS replace custom — different R.**
2. **Retire? — Decommission unused — portfolio cleanup.**

### Common Mistakes in Interviews

- Big-bang rewrite as refactor
- Microservices without async boundaries
- Refactor without observability first

---

## Q044: CAP During Partition

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Distributed Systems |
| **Frequency** | Very Common |

### Question

During network partition, what does choosing CP vs AP mean?

### Short Answer (30 seconds)

CP: sacrifice availability — minority partition may reject writes. AP: sacrifice consistency — both sides accept writes, reconcile later.

### Detailed Answer (3–5 minutes)

**CP example:** SQL primary with sync replica — minority read-only during split.

**AP example:** DynamoDB eventual consistency, shopping cart merge.

**Note:** CAP applies during partition — normal operation has tunable consistency/latency (PACELC).

### Architecture Perspective

CAP is partition behavior — common interview trap.

### Follow-up Questions

1. **Cosmos consistency levels? — Strong to Eventual — tunable per request.**
2. **Kafka CAP? — AP per partition with ordering.**

### Common Mistakes in Interviews

- CAP means pick two always
- Same choice for payments and analytics
- Ignore partition in design

---

## Q045: PACELC Extension

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Distributed Systems |
| **Frequency** | Common |

### Question

What does PACELC add to CAP theorem?

### Short Answer (30 seconds)

If Partition then A or C; Else Latency or Consistency — normal operation trade-off too.

### Detailed Answer (3–5 minutes)

**Example:** Cosmos Session consistency — lower latency than Strong globally.

**CDN:** AP with stale cache — latency vs freshness.

**Architect:** Classify operations — checkout Strong; product catalog Eventual OK.

### Architecture Perspective

PACELC is more practical than CAP alone for architects.

### Follow-up Questions

1. **Linearizability? — Strongest consistency — expensive globally.**
2. **Read-your-writes? — Session consistency pattern.**

### Common Mistakes in Interviews

- Only discuss CAP never latency
- Strong consistency everywhere globally
- No consistency level per operation

---

## Q046: Shard Key Selection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Sharding |
| **Frequency** | Very Common |

### Question

How choose shard key for multi-tenant SaaS?

### Short Answer (30 seconds)

High cardinality, even distribution, query locality — usually `tenantId`. Avoid monotonic hot shard unless salted.

### Detailed Answer (3–5 minutes)

**Patterns:**
- Tenant-per-shard for enterprise whales
- Hash(tenantId) for even spread
- Geo shard for data residency

**Anti-pattern:** `shard by month` — hot current month.

**Architect:** Shard when single DB limits hit — not day one default.

### Architecture Perspective

Shard key is hardest sharding decision.

### Follow-up Questions

1. **Lookup service? — tenantId → shard map table.**
2. **Resharding? — Dual-write migration plan required.**

### Common Mistakes in Interviews

- Low cardinality shard key
- Cross-shard joins in OLTP
- No plan for hot tenant

---

## Q047: Cross-Shard Query Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Sharding |
| **Frequency** | Common |

### Question

How run reports across sharded databases?

### Short Answer (30 seconds)

Don't cross-shard JOIN in OLTP — aggregate via map-reduce, ETL to warehouse, or federated query engine (Citus, Synapse link).

### Detailed Answer (3–5 minutes)

**Patterns:**
1. Nightly ETL each shard → Snowflake/Synapse
2. Scatter-gather API queries all shards — timeout risk
3. Global search index (Elasticsearch)

**Architect:** Accept eventual consistency on cross-shard analytics.

### Architecture Perspective

Cross-shard queries are architectural pain point.

### Follow-up Questions

1. **Elastic query Azure SQL? — Cross-database queries limited.**
2. **Vitess? — VTGate routes queries — reduces custom router.**

### Common Mistakes in Interviews

- Realtime cross-shard JOIN at scale
- Scatter-gather on user-facing sync API
- No warehouse for BI

---

## Q048: Read Replica Lag

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Database |
| **Frequency** | Very Common |

### Question

What is replication lag and why does it matter?

### Short Answer (30 seconds)

Delay between primary commit and replica visibility. Readers see stale data — breaks read-your-writes if not handled.

### Detailed Answer (3–5 minutes)

**Causes:** Network, replica load, sync vs async mode.

**Monitor:** `replica_lag_seconds` alert.

**Mitigation:** Critical reads to primary after write; stale UI messaging.

**Architect:** Classify endpoints by staleness tolerance.

### Architecture Perspective

Replication lag is consistency architecture topic.

### Follow-up Questions

1. **Sync replica? — Lower lag — higher write latency.**
2. **Azure SQL geo-secondary? — Named replica lag metrics.**

### Common Mistakes in Interviews

- Assume replica always current
- Financial balance from lagging replica
- No lag monitoring

---

## Q049: Read Your Writes Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Database |
| **Frequency** | Common |

### Question

Implement read-your-writes after user creates order.

### Short Answer (30 seconds)

Route reads to primary for session after write, or stickiness token, or client passes `readConsistency=strong` for 2 seconds.

### Detailed Answer (3–5 minutes)

**Cookie approach:** Set `primary-read=1` for 2s post POST.

**Token:** Return `version` — client sends — server routes if version newer than replica.

**Architect:** Document per API — mobile offline complicates further.

### Architecture Perspective

Session consistency is UX expectation on writes.

### Follow-up Questions

1. **Cosmos session token? — Built-in session consistency.**
2. **Global users? — Multi-region write conflicts — different problem.**

### Common Mistakes in Interviews

- Always read replica after POST
- No stickiness mechanism
- Ignore mobile cache

---

## Q050: Landing Zone Definition

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Cloud Architecture |
| **Frequency** | Very Common |

### Question

What is an Azure landing zone?

### Short Answer (30 seconds)

Governed subscription foundation before workloads deploy — management groups, identity, networking hub, policy, logging, security baseline.

### Detailed Answer (3–5 minutes)

**CAF alignment:** Platform team owns; app teams deploy to spoke subscriptions.

**Components:** Entra, hub VNet, Log Analytics, Azure Policy, Key Vault.

**Architect:** Landing zone is prerequisite — not optional for enterprise scale.

### Architecture Perspective

Landing zone separates platform from application delivery.

### Follow-up Questions

1. **ALZ accelerator? — Terraform/Bicep reference implementation.**
2. **Subscription vending? — Automated spoke provisioning.**

### Common Mistakes in Interviews

- App teams create subscriptions ad hoc
- No centralized logging
- Skip policy guardrails

---

## Q051: Management Group Hierarchy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Cloud Architecture |
| **Frequency** | Common |

### Question

Design Azure management group hierarchy for enterprise.

### Short Answer (30 seconds)

Root → Platform / Landing Zones / Sandbox / Decommissioned — policies inherit down — production policies stricter than sandbox.

### Detailed Answer (3–5 minutes)

**Example:**
- MG-Prod: deny public IP, require tags
- MG-Dev: relaxed, auto-shutdown schedules

**Architect:** Policy exceptions via ADR — not silent subscription-level disables.

### Architecture Perspective

Hierarchy enables scalable governance.

### Follow-up Questions

1. **Blueprint vs ALZ? — ALZ is current enterprise-scale approach.**
2. **Deny vs audit policy? — Audit first rollout — deny enforce later.**

### Common Mistakes in Interviews

- Flat subscription sprawl
- Prod and sandbox same policies
- No decommissioned MG quarantine

---

## Q052: Azure Policy Interview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Cloud Architecture |
| **Frequency** | Common |

### Question

Give examples of Azure Policy for guardrails.

### Short Answer (30 seconds)

Deny public IP on NIC, require `Environment` tag, enforce allowed regions, require Private Link on storage.

### Detailed Answer (3–5 minutes)

```json
"effect": "deny",
"policyRule": { "if": { "field": "type", "equals": "Microsoft.Network/publicIPAddresses" } }
```

**Initiatives:** Group policies as CIS benchmark bundle.

**Architect:** Policy as code in repo — PR review like application code.

### Architecture Perspective

Policy automates compliance at scale.

### Follow-up Questions

1. **Remediation task? — DeployIfNotExists — auto-fix drift.**
2. **Exemption workflow? — Time-bound with approval.**

### Common Mistakes in Interviews

- Manual compliance spreadsheets
- Deny policies without audit phase
- Permanent exemptions untracked

---

## Q053: FinOps Tagging Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Very Common |

### Question

Why are resource tags critical for FinOps?

### Short Answer (30 seconds)

Tags allocate cost to team, product, environment — enable chargeback, budget alerts, and waste identification.

### Detailed Answer (3–5 minutes)

**Required tags:** `CostCenter`, `Environment`, `Owner`, `Application`.

**Enforcement:** Azure Policy deny deploy without tags.

**Architect:** Untagged resources = ungoverned spend — monthly cleanup report.

### Architecture Perspective

Tags are foundation of cloud financial accountability.

### Follow-up Questions

1. **Showback vs chargeback? — Visibility vs billing internal teams.**
2. **Tag inheritance? — Not automatic — enforce at deploy.**

### Common Mistakes in Interviews

- Optional tags in prod
- No budget alerts per team
- Cannot explain $50K unattributed spend

---

## Q054: Reserved Capacity FinOps

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

When buy Azure Reserved Instances or Savings Plans?

### Short Answer (30 seconds)

After 30–60 days stable baseline utilization — 1–3 year commit for 30–70% discount — not before workload steady.

### Detailed Answer (3–5 minutes)

**Process:**
1. Advisor recommendations
2. Right-size first
3. Buy RI for stable cores
4. Savings Plan for flexible compute

**Architect:** FinOps reviews quarterly — avoid buying RI for migrating-away workloads.

### Architecture Perspective

Commitment discounts require utilization discipline.

### Follow-up Questions

1. **Exchange RI? — Azure allows exchange with penalty rules.**
2. **Spot for batch? — Complement RI — not replace OLTP.**

### Common Mistakes in Interviews

- RI day one before baseline
- Oversized RI for 'growth'
- No right-sizing before commit

---

## Q055: Cost Anomaly Response

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

Sudden 3× Azure bill increase — triage steps?

### Short Answer (30 seconds)

Cost Management anomaly alert → identify resource/service spike → check new deployments, misconfigured autoscale, data egress, orphaned resources.

### Detailed Answer (3–5 minutes)

**Common causes:**
- Forgotten GPU VM left running
- Log Analytics ingestion explosion
- Cross-region egress
- Premium tier selected by mistake

**Architect:** Budget alerts at 80/100% — weekly cost review dashboard per team.

### Architecture Perspective

FinOps incident response is architect operational skill.

### Follow-up Questions

1. **Advisor cost? — Right-size recommendations.**
2. **KQL cost query? — CostManagementResources table.**

### Common Mistakes in Interviews

- Wait until month-end invoice
- No budgets or alerts
- Ignore egress in architecture

---

## Q056: ExpressRoute vs VPN

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hybrid Cloud |
| **Frequency** | Very Common |

### Question

ExpressRoute vs Site-to-Site VPN for hybrid connectivity?

### Short Answer (30 seconds)

ExpressRoute: private dedicated connection, predictable latency, SLA, higher cost. VPN: IPsec over internet, cheaper, good for dev/smaller bandwidth.

### Detailed Answer (3–5 minutes)

**ExpressRoute when:** Production hybrid, compliance no internet transit, high throughput.

**VPN when:** Pilot, backup path, low bandwidth.

**Architect:** Often both — ER primary, VPN backup.

### Architecture Perspective

Hybrid connectivity choice affects latency and security.

### Follow-up Questions

1. **ExpressRoute Gateway? — Required for VNet integration.**
2. **Azure Arc? — Manage on-prem from Azure control plane.**

### Common Mistakes in Interviews

- VPN only for tier-1 prod at scale
- No redundant path
- Hairpin traffic through on-prem unnecessarily

---

## Q057: Azure Arc Hybrid

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hybrid Cloud |
| **Frequency** | Common |

### Question

What does Azure Arc enable for hybrid cloud?

### Short Answer (30 seconds)

Project on-prem, AWS, GCP, edge Kubernetes and SQL into Azure Resource Manager — unified policy, monitoring, and governance.

### Detailed Answer (3–5 minutes)

**Use cases:**
- Arc-enabled Kubernetes — GitOps, policy
- Arc SQL — inventory and best practices
- Run Azure services anywhere (Arc data services)

**Architect:** Arc is management plane extension — not migration by itself.

### Architecture Perspective

Arc addresses multi-environment governance.

### Follow-up Questions

1. **Arc vs AVS? — VMware lift to Azure — different migration path.**
2. **Disconnected mode? — Limited features — plan connectivity.**

### Common Mistakes in Interviews

- Arc as magic migration tool
- No on-prem network to Arc agents
- Ignore agent update lifecycle

---

## Q058: RTO Definition Interview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Disaster Recovery |
| **Frequency** | Very Common |

### Question

Define RTO and what architectural choices it drives.

### Short Answer (30 seconds)

Recovery Time Objective — max acceptable downtime. Lower RTO → hot standby, automated failover, multi-region active.

### Detailed Answer (3–5 minutes)

**Examples:**
- RTO 15 min → warm standby, Traffic Manager health probe failover
- RTO 8 hours → cold backup restore runbook

**Cost:** RTO 0 minutes nearly impossible — negotiate realistic with business.

**Architect:** RTO documented per application tier.

### Architecture Perspective

RTO drives standby architecture cost.

### Follow-up Questions

1. **RTO vs MTTR? — Objective vs measured recovery.**
2. **Runbook automation? — IaC rebuild reduces RTO.**

### Common Mistakes in Interviews

- Same RTO all apps
- RTO without tested runbook
- Confuse backup with DR

---

## Q059: RPO Definition Interview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Disaster Recovery |
| **Frequency** | Very Common |

### Question

Define RPO and how backup frequency relates.

### Short Answer (30 seconds)

Recovery Point Objective — max acceptable data loss measured in time. RPO 1 hour → backups or replication at least hourly.

### Detailed Answer (3–5 minutes)

**RPO 0:** Synchronous replication — higher cost and latency.

**RPO 24h:** Nightly backup — 24h data loss possible.

**Architect:** RPO drives replication mode — async vs sync.

### Architecture Perspective

RPO links business tolerance to replication technology.

### Follow-up Questions

1. **Log shipping RPO? — Depends on log backup interval.**
2. **Immutable backup? — Ransomware protection — separate concern.**

### Common Mistakes in Interviews

- Daily backup for RPO zero claim
- No backup restore test
- RPO undefined in SLA

---

## Q060: Active Passive DR Azure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Disaster Recovery |
| **Frequency** | Common |

### Question

Design active-passive DR with Azure Front Door.

### Short Answer (30 seconds)

Primary region serves traffic; secondary warm standby; Front Door health probes fail over DNS/routing on primary failure.

### Detailed Answer (3–5 minutes)

**Components:**
- Primary App Service / AKS
- Secondary scaled-down or ready capacity
- SQL geo-replication async
- Front Door priority routing

**Test:** Quarterly failover drill — measure actual RTO.

**Architect:** Automate scale-up secondary on failover.

### Architecture Perspective

Active-passive is common cost-balanced DR.

### Follow-up Questions

1. **Pilot light? — Minimal secondary — slower RTO.**
2. **Warm standby? — Pre-scaled partial capacity.**

### Common Mistakes in Interviews

- Backup only no failover path
- Failover never tested
- DNS TTL blocks fast failover

---

## Q061: Functions Consumption Plan

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Serverless |
| **Frequency** | Very Common |

### Question

When is Azure Functions Consumption plan appropriate?

### Short Answer (30 seconds)

Sporadic workloads, event-driven processing, tolerance for cold start — pay per execution — not latency-critical synchronous APIs at scale.

### Detailed Answer (3–5 minutes)

**Good:** Blob trigger virus scan, nightly cleanup, webhooks.

**Bad:** User-facing API p99 < 100ms at steady traffic.

**Mitigate cold start:** Premium plan, always-ready instances, smaller package.

### Architecture Perspective

Serverless plan choice is architecture decision.

### Follow-up Questions

1. **Durable Functions? — Orchestration — long-running workflows.**
2. **Premium plan? — VNET, pre-warmed, longer timeout.**

### Common Mistakes in Interviews

- Consumption for steady high QPS API
- Huge dependency package cold start
- No premium plan for latency SLA

---

## Q062: Lambda vs Azure Functions

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Serverless |
| **Frequency** | Common |

### Question

Compare AWS Lambda and Azure Functions for architects.

### Short Answer (30 seconds)

Both event-driven FaaS — per-invocation billing, triggers from storage/queue/http. Differences: VPC config, deployment packages, durable orchestration, identity integration.

### Detailed Answer (3–5 minutes)

| | Lambda | Azure Functions |
|---|--------|-----------------|
| Triggers | Many AWS native | Azure + bindings |
| Identity | IAM role | Managed identity |
| Plan | Provisioned concurrency | Premium always-ready |

**Architect:** Choose based on cloud estate — not feature checklist trivia.

### Architecture Perspective

Serverless comparison in multi-cloud interviews.

### Follow-up Questions

1. **Lambda@Edge? — CDN edge functions — Azure Front Door Rules Engine different.**
2. **Container vs zip deploy? — Container image for complex deps.**

### Common Mistakes in Interviews

- Lambda for monolith replacement
- Ignore VPC cold start penalty AWS
- Serverless without idempotent design

---

## Q063: Managed Identity Azure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | IAM |
| **Frequency** | Very Common |

### Question

How use managed identity for App Service to access Key Vault?

### Short Answer (30 seconds)

Enable system-assigned or user-assigned managed identity on App Service; grant identity Key Vault Secrets User RBAC; access secrets without client secret in config.

### Detailed Answer (3–5 minutes)

```csharp
builder.Configuration.AddAzureKeyVault(
  new Uri(vaultUri),
  new DefaultAzureCredential());
```

**Architect:** No secrets in appsettings — identity-based access only.

### Architecture Perspective

Managed identity eliminates secret rotation pain.

### Follow-up Questions

1. **User-assigned vs system? — Shared identity across resources — user-assigned.**
2. **DefaultAzureCredential chain? — Local dev uses Azure CLI — prod managed identity.**

### Common Mistakes in Interviews

- Client secret in appsettings
- Key Vault access policy legacy without RBAC
- Same identity all environments

---

## Q064: Service Principal vs MI

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | IAM |
| **Frequency** | Common |

### Question

When service principal still needed vs managed identity?

### Short Answer (30 seconds)

External CI/CD to Azure, third-party SaaS integration, cross-tenant scenarios — managed identity for Azure-hosted workloads.

### Detailed Answer (3–5 minutes)

**Service principal:** Pipeline federated credential (OIDC) preferred over secret.

**Managed identity:** App Service, Functions, AKS pod identity.

**Architect:** Prefer workload identity federation — no rotating secrets.

### Architecture Perspective

Identity type follows where code runs.

### Follow-up Questions

1. **AKS workload identity? — Federated credential to K8s SA.**
2. **Expired SP secret outage? — Common incident — automate rotation.**

### Common Mistakes in Interviews

- SP secret in repo
- MI for external non-Azure caller
- Never rotate credentials

---

## Q065: Blob Access Tiers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Storage |
| **Frequency** | Very Common |

### Question

Explain Azure Blob access tiers hot, cool, cold, archive.

### Short Answer (30 seconds)

Hot: frequent access. Cool: 30+ day infrequent, lower storage higher access cost. Cold: 90+ day rare access. Archive: offline retrieval hours — cheapest storage.

### Detailed Answer (3–5 minutes)

**Lifecycle policy:** Auto-tier after 30 days to cool, 180 to archive.

**Architect:** Backup and logs → cool/archive quickly — save 50%+ storage cost.

### Architecture Perspective

Tiering is FinOps storage optimization.

### Follow-up Questions

1. **Rehydrate archive? — High latency — plan restore runbook.**
2. **Premium block blob? — Low latency hot tier variant.**

### Common Mistakes in Interviews

- Hot tier for all backup data
- Archive for data needed daily
- No lifecycle management

---

## Q066: Blob Private Endpoint

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Storage |
| **Frequency** | Common |

### Question

Secure blob access with Private Endpoint.

### Short Answer (30 seconds)

Disable public access; create Private Endpoint in spoke VNet; DNS private zone `privatelink.blob.core.windows.net`; access via private IP only.

### Detailed Answer (3–5 minutes)

**Pattern:** App in spoke → private endpoint → storage account.

**Exfiltration risk reduced:** No internet route to data plane.

**Architect:** Default deny public — exceptions via policy exemption ADR.

### Architecture Perspective

Private Link is enterprise storage security baseline.

### Follow-up Questions

1. **Storage firewall? — Selected networks + PE — defense in depth.**
2. **PE DNS in on-prem? — Conditional forwarder to Azure DNS.**

### Common Mistakes in Interviews

- Public blob container prod data
- Private endpoint without DNS config
- Bypass PE via SAS leaked publicly

---

## Q067: Event Grid vs Service Bus

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Event-Driven |
| **Frequency** | Very Common |

### Question

Event Grid vs Service Bus for order-placed notification?

### Short Answer (30 seconds)

Event Grid: lightweight reactive routing, fan-out, near real-time push — great for Azure resource events and micro-event notification. Service Bus: durable messaging, transactions, sessions, dead-letter.

### Detailed Answer (3–5 minutes)

**Hybrid:** API saves order → outbox → Service Bus (durable) → subscribers; optional Event Grid for external webhook fan-out.

**Architect:** Durability and ordering requirements pick product.

### Architecture Perspective

Event-driven product choice affects reliability semantics.

### Follow-up Questions

1. **At-least-once? — Both — consumers must be idempotent.**
2. **Ordering? — Service Bus sessions — Event Grid no global order.**

### Common Mistakes in Interviews

- Event Grid as only durable queue
- No idempotent consumer
- Synchronous HTTP chain instead

---

## Q068: Outbox Pattern Cloud

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Event-Driven |
| **Frequency** | Very Common |

### Question

Why transactional outbox for cloud event publishing?

### Short Answer (30 seconds)

Guarantees DB commit and message publish atomicity — avoid dual-write where DB succeeds and bus fails leaving inconsistent state.

### Detailed Answer (3–5 minutes)

**Flow:** Insert business row + outbox row same transaction → worker publishes → marks sent.

**Tools:** MassTransit EF outbox, Debezium CDC alternative.

**Architect:** Mandatory for money and inventory events.

### Architecture Perspective

Outbox is distributed consistency foundation.

### Follow-up Questions

1. **Inbox pattern? — Consumer dedup — pairs with outbox.**
2. **CDC vs outbox? — CDC decouples app code — ops complexity.**

### Common Mistakes in Interviews

- Publish before DB commit
- Fire-and-forget Task.Run publish
- No poison message handling

---

## Q069: Idempotent Event Consumer

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Event-Driven |
| **Frequency** | Common |

### Question

Design idempotent Service Bus message handler.

### Short Answer (30 seconds)

Store processed `messageId` in dedup table; begin transaction — if messageId exists skip; else process and insert messageId.

### Detailed Answer (3–5 minutes)

```sql
CREATE UNIQUE INDEX ON ProcessedMessages (MessageId);
```

**At-least-once delivery:** Duplicate delivery safe.

**Architect:** Business logic also idempotent — `Upsert` not blind `Insert`.

### Architecture Perspective

Idempotent consumers are event-driven requirement.

### Follow-up Questions

1. **Natural idempotency? — SET balance = X not balance = balance + X.**
2. **Dead-letter when? — Max delivery exceeded — alert and tool.**

### Common Mistakes in Interviews

- Assume exactly-once delivery
- Insert-only without unique constraint
- Ignore poison messages

---

## Q070: Choreography vs Orchestration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Event-Driven |
| **Frequency** | Common |

### Question

Choreography vs orchestration for order fulfillment?

### Short Answer (30 seconds)

Choreography: services react to events independently — loose coupling. Orchestration: central coordinator (Logic Apps, Durable Functions) controls flow — easier visibility.

### Detailed Answer (3–5 minutes)

**Choreography:** OrderPlaced → Inventory, Payment, Shipping subscribe.

**Orchestration:** Saga orchestrator calls each step with compensations.

**Architect:** Choreography for simple flows; orchestration when complex compensation needed.

### Architecture Perspective

Event-driven style choice affects debugging and coupling.

### Follow-up Questions

1. **Distributed tracing? — Required for choreography observability.**
2. **Temporal/Camunda? — Enterprise orchestration engines.**

### Common Mistakes in Interviews

- Choreography without correlation ID
- Orchestrator god service with all logic
- No compensation on failure

---
