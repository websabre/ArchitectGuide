# Week 46 — Advanced Q&A

> Q071–Q100: Premium format (Week 1 quality).

---


## Q071: Index Maintenance Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | SQL Indexing |
| **Frequency** | Very Common |

### Question

Design index maintenance for high-write OLTP database.

### Short Answer (30 seconds)

Monitor fragmentation, rebuild/reorganize schedule, avoid redundant indexes, use online rebuild where edition supports, align fill factor with insert pattern.

### Detailed Answer (3–5 minutes)

**Process:**
- Weekly DMV: `sys.dm_db_index_physical_stats`
- Reorganize >10%, rebuild >30% fragmentation
- Drop unused indexes from missing index DMV false positives

**Architect:** Index changes through migration pipeline — not manual prod clicks.

### Architecture Perspective

Index maintenance is operational architecture responsibility.

### Follow-up Questions

1. **Auto rebuild cloud? — Azure SQL automatic tuning — verify scope.**
2. **Partition sliding window? — Archive old partitions — reduce rebuild scope.**

### Common Mistakes in Interviews

- Never maintain indexes
- Rebuild everything nightly blindly
- Duplicate overlapping indexes

---

## Q072: Parameter Sniffing Fix

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | SQL Indexing |
| **Frequency** | Common |

### Question

What is parameter sniffing and mitigation options?

### Short Answer (30 seconds)

SQL caches plan for first parameter values — bad plan for different parameters. Fix: OPTIMIZE FOR UNKNOWN, RECOMPILE hint, plan guides, or rewrite query.

### Detailed Answer (3–5 minutes)

**Example:** `@Status=Active` first — seeks; `@Status=Archived` later — scan wrong plan cached.

**Mitigations:**
- `OPTION (RECOMPILE)` for skewed reports
- Local variable trick (less ideal)
- Query Store force plan

**Architect:** EF raw SQL reports may need recompile hint.

### Architecture Perspective

Parameter sniffing is production SQL perf mystery.

### Follow-up Questions

1. **Query Store? — Identify regressed plans post-deploy.**
2. **Adaptive query processing? — SQL Server automatic mitigations.**

### Common Mistakes in Interviews

- Ignore plan regression after deploy
- One plan fits all without testing skew
- Hint every query RECOMPILE unnecessarily

---

## Q073: Columnstore for Analytics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | SQL Indexing |
| **Frequency** | Common |

### Question

When use columnstore indexes in SQL Server?

### Short Answer (30 seconds)

Analytics, aggregations, warehouse-style scans — not OLTP point lookups. Clustered columnstore for fact tables; nonclustered columnstore on warehouse tables.

### Detailed Answer (3–5 minutes)

**Benefits:** 10x compression, batch mode execution.

**OLTP caution:** Columnstore on hot OLTP table hurts inserts.

**Architect:** Separate OLTP and OLAP — ETL to columnstore warehouse.

### Architecture Perspective

Right index technology for workload shape.

### Follow-up Questions

1. **CCI maintenance? — Tuple mover, reorganize delta rowgroups.**
2. **Synapse dedicated SQL pool? — Columnstore native.**

### Common Mistakes in Interviews

- Columnstore on transactional order lines
- No separate analytics path
- Ignore rowgroup quality DMV

---

## Q074: Azure Well-Architected Pillars

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Azure |
| **Frequency** | Very Common |

### Question

Name Azure Well-Architected Framework pillars and one control each.

### Short Answer (30 seconds)

Reliability (health probes), Security (Private Link), Cost Optimization (reserved capacity), Operational Excellence (IaC), Performance Efficiency (right-size), Sustainability (region selection).

### Detailed Answer (3–5 minutes)

**Interview use:** Map design decision to pillar — 'We chose geo-redundant storage for Reliability RPO.'

**Review:** WAF assessment workbook per release for tier-1 apps.

**Architect:** WAF review in architecture board gate.

### Architecture Perspective

WAF provides vocabulary for design reviews.

### Follow-up Questions

1. **Sustainability pillar? — Carbon-aware region scheduling emerging.**
2. **Trade-off between pillars? — Cost vs reliability explicit.**

### Common Mistakes in Interviews

- Cannot name pillars
- Security only pillar considered
- No periodic WAF assessment

---

## Q075: Multi-Region Active Active

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Azure |
| **Frequency** | Common |

### Question

Design active-active multi-region Azure application.

### Short Answer (30 seconds)

Both regions serve traffic via Front Door; data layer hardest — Cosmos multi-write, or SQL async with conflict resolution, session affinity avoided where possible.

### Detailed Answer (3–5 minutes)

**Challenges:**
- Data conflicts — last-write-wins vs application merge
- Cache coherence across regions
- Deployment coordination

**Architect:** Active-active only when RTO/RPO and traffic justify complexity.

### Architecture Perspective

Multi-region is data problem first — compute is easier.

### Follow-up Questions

1. **Traffic Manager vs Front Door? — Front Door modern global HTTP.**
2. **Regional pair? — Azure paired regions for platform DR.**

### Common Mistakes in Interviews

- Active-active without conflict strategy
- Sync SQL both regions writes blindly
- Ignore cross-region egress cost

---

## Q076: AWS Landing Zone Control Tower

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Cloud Comparison |
| **Frequency** | Common |

### Question

Compare Azure Landing Zone and AWS Control Tower.

### Short Answer (30 seconds)

Both automate multi-account/subscription setup with guardrails — Control Tower uses AWS Organizations + SCPs; Azure uses management groups + Azure Policy.

### Detailed Answer (3–5 minutes)

**AWS:** Account vending, OU structure, Config rules.

**Azure:** ALZ, subscription aliases, policy initiatives.

**Architect:** Multi-cloud enterprises align OU/MG naming and tag standards conceptually.

### Architecture Perspective

Landing zone parity across clouds for enterprise architects.

### Follow-up Questions

1. **SCP vs Azure Policy deny? — Similar guardrail — different syntax.**
2. **Terraform both? — Separate modules — shared tag module.**

### Common Mistakes in Interviews

- Conflate account and subscription count planning
- No guardrails on sandbox accounts
- Identical network CIDR overlap across clouds

---

## Q077: EKS vs AKS Comparison

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Cloud Comparison |
| **Frequency** | Common |

### Question

Compare EKS and AKS for Kubernetes workloads.

### Short Answer (30 seconds)

Both managed K8s — EKS deeper AWS integration; AKS Azure integration (Entra, Monitor, Key Vault CSI). Node management: AKS Automatic vs EKS Fargate profiles.

### Detailed Answer (3–5 minutes)

**Consider:** Team cloud estate, identity, existing DevOps pipelines.

**Portability:** Kubernetes API portable — managed services differ in add-ons.

**Architect:** Don't choose K8s cloud for console preference — integration path matters.

### Architecture Perspective

K8s comparison is pragmatic not religious.

### Follow-up Questions

1. **Istio both? — Service mesh portable — ops burden same.**
2. **Cluster autoscaler? — Both support — node pool config differs.**

### Common Mistakes in Interviews

- K8s for 3 static containers
- Ignore identity integration differences
- Assume YAML identical all features

---

## Q078: Retire and Retain 6Rs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Migration |
| **Frequency** | Common |

### Question

Explain Retire and Retain in 6 Rs portfolio assessment.

### Short Answer (30 seconds)

Retire: decommission unused apps — save cost and attack surface. Retain: keep on-prem due to compliance, latency, or licensing — cloud not always answer.

### Detailed Answer (3–5 minutes)

**Discovery:** CMDB + dependency mapping — 30% apps often retire candidates.

**Retain example:** Mainframe settlement system — cloud refactor ROI negative.

**Architect:** Migration portfolio dashboard — counts per R with savings estimate.

### Architecture Perspective

6 Rs includes intentional no-migration decisions.

### Follow-up Questions

1. **Archive data before retire? — Legal hold check.**
2. **Zombie SaaS subscriptions? — Retire includes license cleanup.**

### Common Mistakes in Interviews

- Migrate everything mandate
- No dependency discovery
- Retain without documented justification

---

## Q079: Azure Migrate Assessment

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Migration |
| **Frequency** | Very Common |

### Question

How use Azure Migrate for datacenter exit planning?

### Short Answer (30 seconds)

Install appliance, discover VMs, assess readiness, right-size Azure target, dependency visualization, export TCO report.

### Detailed Answer (3–5 minutes)

**Outputs:**
- Azure VM SKU recommendation
- SQL to PaaS suitability
- Network dependency map

**Architect:** Assessment feeds wave planning — identity and DNS wave 0.

### Architecture Perspective

Assessment before migration prevents cost surprises.

### Follow-up Questions

1. **Dependency map? — Identifies chatty neighbors — migrate together.**
2. **Business case? — TCO + operational savings quantified.**

### Common Mistakes in Interviews

- Lift without assess — oversized VMs
- Ignore SQL compatibility report
- Skip network dependency analysis

---

## Q080: Consistency Models Cosmos

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Distributed Systems |
| **Frequency** | Very Common |

### Question

Explain Cosmos DB consistency levels for global app.

### Short Answer (30 seconds)

Strong, Bounded Staleness, Session, Consistent Prefix, Eventual — trade latency and RU cost vs consistency guarantees.

### Detailed Answer (3–5 minutes)

**Session:** Default sweet spot — read-your-writes in session.

**Strong:** Global linearizable — 2x latency/cost roughly.

**Architect:** Per-operation consistency override — checkout Strong, catalog Eventual.

### Architecture Perspective

Cosmos tunable consistency is practical CAP discussion.

### Follow-up Questions

1. **Conflict resolution? — Last-writer-wins or custom merge procedure.**
2. **Partition key? — Related — hot partition kills performance.**

### Common Mistakes in Interviews

- Strong everywhere globally
- Ignore RU cost of strong reads
- Wrong partition key design

---

## Q081: Vitess Sharding Layer

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Sharding |
| **Frequency** | Occasional |

### Question

What problem does Vitess solve for MySQL sharding?

### Short Answer (30 seconds)

Vitess provides VTGate query router, connection pooling, and resharding tooling — reduces custom shard router code.

### Detailed Answer (3–5 minutes)

**Components:**
- VTGate — routes SQL by shard key
- Topology service — shard map
- Resharding workflows

**Azure analog:** Consider Cosmos or Citus for PostgreSQL — similar routing abstraction.

**Architect:** Buy vs build shard router — Vitess when staying on MySQL at scale.

### Architecture Perspective

Managed sharding layers reduce custom middleware risk.

### Follow-up Questions

1. **Citus PostgreSQL? — Distributed PostgreSQL — shard-aware queries.**
2. **Application-level router? — Maintenance burden — justify carefully.**

### Common Mistakes in Interviews

- Custom router without resharding plan
- Cross-shard JOIN in app OLTP
- Ignore connection pool per shard

---

## Q082: Global Database Failover

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Database |
| **Frequency** | Common |

### Question

Design global SQL failover with minimum RPO.

### Short Answer (30 seconds)

Async geo-replication for RPO >0; sync replication for RPO 0 with latency cost; automated failover with grace period to prevent flapping.

### Detailed Answer (3–5 minutes)

**Azure SQL:** Auto-failover groups — secondary readable.

**Split brain:** Witness or cloud-managed quorum prevents dual primary.

**Architect:** Failover runbook includes connection string swap and cache invalidation.

### Architecture Perspective

Global SQL failover is RPO/RTO engineering.

### Follow-up Questions

1. **Manual failover testing? — Quarterly game day.**
2. **Read-only secondary routing? — Weighted during normal ops.**

### Common Mistakes in Interviews

- Async replica claim RPO zero
- Failover untested 2 years
- App not handling brief dual-write window

---

## Q083: Subscription Vending Machine

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Cloud Architecture |
| **Frequency** | Common |

### Question

Automate Azure subscription provisioning for app teams.

### Short Answer (30 seconds)

Pipeline creates subscription (or uses alias), assigns to MG, applies policies, deploys spoke network, grants team Contributor scoped, registers in catalog.

### Detailed Answer (3–5 minutes)

**Tools:** Terraform, Bicep, Azure Deployment Environments, Backstage template.

**Architect:** Self-service with guardrails — not ticket to ops for 2 weeks.

### Architecture Perspective

Subscription vending scales platform team.

### Follow-up Questions

1. **Quota increase? — Automate request in pipeline.**
2. **Sandbox TTL? — Auto-delete sandbox subscriptions after 30 days.**

### Common Mistakes in Interviews

- Manual subscription creation each team
- No policy on new subscriptions
- Over-permissioned Contributor subscription-wide

---

## Q084: FinOps Unit Economics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | FinOps |
| **Frequency** | Very Common |

### Question

Calculate unit economics for cloud-hosted API.

### Short Answer (30 seconds)

Cost per 1000 API requests = (monthly infra cost) / (monthly requests in thousands). Track trend as efficiency metric.

### Detailed Answer (3–5 minutes)

**Example:** $20K/month, 100M requests → $0.20 per 1K requests.

**Optimize:** Right-size, cache, reduce egress, serverless for spiky.

**Architect:** Tie scale decisions to unit cost — not absolute bill only.

### Architecture Perspective

Unit economics connects engineering to finance.

### Follow-up Questions

1. **Marginal cost of feature? — Estimate new service $/transaction.**
2. **Chargeback model? — Teams incentivized to optimize.**

### Common Mistakes in Interviews

- Only total bill monitoring
- Unit cost rising unnoticed
- No allocation to product teams

---

## Q085: Azure Advisor Operational

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

How use Azure Advisor in architecture governance?

### Short Answer (30 seconds)

Review reliability, security, performance, cost recommendations weekly; assign owners; track remediation in backlog; block prod deploy on critical security open items.

### Detailed Answer (3–5 minutes)

**Categories:** Cost — right-size VMs; Security — MFA gaps; Reliability — no geo-redundancy.

**Architect:** Advisor findings feed architecture review KPI dashboard.

### Architecture Perspective

Advisor is free architectural second opinion.

### Follow-up Questions

1. **Exemptions? — Document risk acceptance for false positives.**
2. **Defender integration? — Deeper security than Advisor alone.**

### Common Mistakes in Interviews

- Ignore Advisor recommendations
- No owner assignment on findings
- Cost recommendations without implementing

---

## Q086: Hub Spoke Peering Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Hybrid Cloud |
| **Frequency** | Very Common |

### Question

Design hub-spoke VNet topology with on-prem connectivity.

### Short Answer (30 seconds)

Hub: firewall, VPN/ER gateway, DNS, shared services. Spokes: app workloads peer to hub only — not spoke-to-spoke mesh. UDR routes internet via firewall.

### Detailed Answer (3–5 minutes)

**Security:** All egress inspected — NVA or Azure Firewall.

**Scale:** Multiple spokes per subscription pattern.

**Architect:** Peering is non-transitive — hub required for spoke-to-spoke via hub.

### Architecture Perspective

Hub-spoke is enterprise Azure networking default.

### Follow-up Questions

1. **VWAN? — Virtual WAN simplifies large hub-spoke at scale.**
2. **Spoke peer spoke directly? — Bypasses firewall — avoid.**

### Common Mistakes in Interviews

- Flat VNet mesh 50 spokes
- No UDR to firewall
- Overlapping CIDR with on-prem

---

## Q087: DNS Hybrid Resolution

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Hybrid Cloud |
| **Frequency** | Common |

### Question

Solve DNS resolution between on-prem and Azure private endpoints.

### Short Answer (30 seconds)

Azure Private DNS zones linked to VNets; conditional forwarders on-prem to Azure DNS resolver; avoid split-brain with consistent naming.

### Detailed Answer (3–5 minutes)

**Private endpoint:** `storage.privatelink.blob.core.windows.net` resolves private IP in VNet.

**On-prem:** DNS forwarder to Azure inbound endpoint.

**Architect:** DNS design before mass Private Link rollout.

### Architecture Perspective

DNS breaks hybrid deployments silently.

### Follow-up Questions

1. **Azure DNS Private Resolver? — Central hybrid DNS service.**
2. **Hosts file hack? — Not scalable.**

### Common Mistakes in Interviews

- Public DNS for private endpoints
- No forwarder from on-prem
- Conflicting internal zone names

---

## Q088: Game Day DR Drill

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Disaster Recovery |
| **Frequency** | Very Common |

### Question

Run effective DR game day for cloud application.

### Short Answer (30 seconds)

Predefined scenario (region down), execute runbook, measure actual RTO/RPO, involve ops and dev, document gaps, fix before next quarter.

### Detailed Answer (3–5 minutes)

**Scenarios:**
- Primary region unavailable
- SQL corruption restore
- Key Vault access failure

**Success:** Actual RTO within SLA; no undocumented manual steps.

**Architect:** Executive observer — proves DR investment value.

### Architecture Perspective

Untested DR is wishful thinking — game days prove it.

### Follow-up Questions

1. **Chaos Studio Azure? — Fault injection in controlled environment.**
2. **Tabletop vs technical? — Both needed — tabletop first.**

### Common Mistakes in Interviews

- DR drill never run
- Drill without success criteria
- Hide failures from leadership

---

## Q089: Immutable Backup Ransomware

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Disaster Recovery |
| **Frequency** | Common |

### Question

Protect backups from ransomware with immutability.

### Short Answer (30 seconds)

Azure Backup immutable vault, blob immutable storage policies, soft delete, separate subscription for backup estate, MFA on delete operations.

### Detailed Answer (3–5 minutes)

**3-2-1 rule:** 3 copies, 2 media, 1 offsite — immutability prevents attacker encrypting backups.

**Architect:** Backup subscription in separate MG with stricter RBAC.

### Architecture Perspective

Ransomware resilience is modern DR requirement.

### Follow-up Questions

1. **MARS agent? — Verify immutability scope per workload.**
2. **Restore test? — Verify backup not corrupted pre-incident.**

### Common Mistakes in Interviews

- Mutable backups only same tenant
- Single admin can delete all backups
- Never test restore

---

## Q090: Durable Functions Saga

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Serverless |
| **Frequency** | Common |

### Question

Implement saga pattern with Durable Functions orchestration.

### Short Answer (30 seconds)

Orchestrator function calls activities in sequence with compensation on failure — state persisted automatically — survives restarts.

### Detailed Answer (3–5 minutes)

```csharp
[Function(nameof(OrderSaga))]
public async Task OrderSaga([OrchestrationTrigger] TaskOrchestrationContext ctx) {
  try {
    await ctx.CallActivityAsync(nameof(ReserveInventory), order);
    await ctx.CallActivityAsync(nameof(ChargePayment), order);
  } catch {
    await ctx.CallActivityAsync(nameof(ReleaseInventory), order);
  }
}
```

**Architect:** Orchestration visibility beats hidden choreography for complex sagas.

### Architecture Perspective

Durable Functions is Azure saga tool — know compensation.

### Follow-up Questions

1. **Human interaction? — External events — approval steps.**
2. **Timeout handling? — Orchestration runtime timers.**

### Common Mistakes in Interviews

- Choreography for 8-step payment saga
- No compensation activities
- Long synchronous Logic App chain

---

## Q091: AKS Workload Identity

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | IAM |
| **Frequency** | Very Common |

### Question

Configure AKS workload identity to access Azure SQL without secrets.

### Short Answer (30 seconds)

Federated credential maps K8s service account to Entra app; pod uses DefaultAzureCredential; SQL grants Entra user access.

### Detailed Answer (3–5 minutes)

**Steps:**
1. Enable workload identity on AKS
2. Create UAMI + federated credential
3. Annotate service account
4. SQL: `CREATE USER [app-name] FROM EXTERNAL PROVIDER`

**Architect:** No connection string secrets in K8s secrets — identity only.

### Architecture Perspective

Workload identity is AKS security baseline.

### Follow-up Questions

1. **Legacy pod identity? — Deprecated — migrate to workload identity.**
2. **Key Vault CSI? — Secrets still needed for some third-party APIs.**

### Common Mistakes in Interviews

- SQL sa password in K8s secret
- Shared cluster identity all apps
- No federated credential rotation doc

---

## Q092: ABAC Azure Conditions

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | IAM |
| **Frequency** | Common |

### Question

Use attribute-based access control in Azure RBAC.

### Short Answer (30 seconds)

Role assignment conditions restrict by resource attributes — e.g., Blob Data Reader only if blob path prefix matches team.

### Detailed Answer (3–5 minutes)

**Example condition:** `@Resource[Microsoft.Storage/storageAccounts/blobServices/containers:name] StringEquals 'team-data'`

**Architect:** ABAC reduces role assignment sprawl — fine-grained data plane.

### Architecture Perspective

ABAC advances least privilege beyond RBAC scope.

### Follow-up Questions

1. **AWS ABAC? — IAM policy tags on resources — similar concept.**
2. **Testing conditions? — What-if simulator — verify deny.**

### Common Mistakes in Interviews

- Contributor plus manual ACLs everywhere
- ABAC conditions untested
- Overly broad storage access

---

## Q093: Data Lake vs Blob Analytics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Storage |
| **Frequency** | Common |

### Question

ADLS Gen2 vs standard blob for analytics pipeline?

### Short Answer (30 seconds)

ADLS Gen2 adds hierarchical namespace — efficient directory operations for Spark/Databricks; standard blob for simple object storage.

### Detailed Answer (3–5 minutes)

**Analytics:** Synapse, Databricks use abfss:// paths on ADLS.

**Architect:** Landing zone raw data on ADLS; curated parquet in gold layer.

### Architecture Perspective

Data lake storage choice affects analytics performance.

### Follow-up Questions

1. **Lifecycle on ADLS? — Tier cold/archive like blob.**
2. **Private endpoint ADLS? — Same Private Link pattern.**

### Common Mistakes in Interviews

- Flat blob millions prefixes slow
- Analytics on hot tier only
- No zone redundancy on critical lake

---

## Q094: Event Hubs Kafka Endpoint

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Event-Driven |
| **Frequency** | Common |

### Question

Use Event Hubs Kafka endpoint for event streaming migration.

### Short Answer (30 seconds)

Existing Kafka clients connect to Event Hubs with protocol head — migrate producers/consumers without full cluster ops.

### Detailed Answer (3–5 minutes)

**Benefits:** Managed scaling, Azure integration, capture to ADLS.

**Limits:** Not 100% Kafka feature parity — verify consumer groups, transactions.

**Architect:** Bridge pattern during Kafka-to-cloud migration.

### Architecture Perspective

Protocol compatibility eases streaming migration.

### Follow-up Questions

1. **Capture feature? — Auto-archive stream to data lake.**
2. **Throughput units? — Scale Event Hubs capacity planning.**

### Common Mistakes in Interviews

- Self-managed Kafka on VMs without ops team
- Assume full Kafka parity
- No consumer offset monitoring

---

## Q095: Schema Registry Events

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Event-Driven |
| **Frequency** | Common |

### Question

Manage event schema evolution in enterprise integration.

### Short Answer (30 seconds)

Schema registry (Event Hubs, Confluent) with backward-compatible additive changes; consumers tolerate unknown fields; version in event envelope.

### Detailed Answer (3–5 minutes)

**Rules:**
- Add optional fields only in minor version
- Breaking change → new topic `order.v2`

**Architect:** Contract tests on sample events in CI.

### Architecture Perspective

Schema governance prevents event-driven breakage.

### Follow-up Questions

1. **Avro vs JSON? — Avro compact with schema ID.**
2. **Protobuf? — gRPC internal — events often Avro/JSON.**

### Common Mistakes in Interviews

- Breaking rename without version bump
- No registry — free-form JSON
- Consumers fail on unknown fields

---

## Q096: Service Bus Sessions Ordering

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Event-Driven |
| **Frequency** | Common |

### Question

When use Service Bus sessions for ordered processing?

### Short Answer (30 seconds)

Messages with same SessionId processed FIFO by one consumer — use for order lifecycle per orderId — not global ordering.

### Detailed Answer (3–5 minutes)

**Pattern:** `SessionId = orderId` — all events for one order serialized.

**Scale:** Different sessions parallel across consumers.

**Architect:** Don't use sessions for global order — partition key in Event Hubs instead.

### Architecture Perspective

Ordering scope must be minimal for scale.

### Follow-up Questions

1. **Session lock lost? — Handler must be idempotent on redelivery.**
2. **Max delivery count? — Dead-letter poison session messages.**

### Common Mistakes in Interviews

- Global FIFO on single session
- Sessions on high-cardinality key — no parallelism
- Ignore dead-letter on session failures

---

## Q097: Multi-Cloud DR Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Disaster Recovery |
| **Frequency** | Common |

### Question

Design DR with secondary cloud provider.

### Short Answer (30 seconds)

Backup replication to S3 from Azure (or vice versa), infra as code portable modules, DNS failover, accept higher complexity and egress cost — rare except regulatory.

### Detailed Answer (3–5 minutes)

**Patterns:**
- Backup only secondary cloud (common)
- Active-passive DR in AWS for Azure primary (rare)

**Architect:** Document data residency and egress cost — DR test includes cross-cloud restore.

### Architecture Perspective

Multi-cloud DR is expensive — justify regulatory need.

### Follow-up Questions

1. **Velero cross-cloud? — K8s backup portability partial.**
2. **Terraform multi-provider? — Duplicate networking complexity.**

### Common Mistakes in Interviews

- Active-active multi-cloud without budget
- Untested cross-cloud restore
- Ignore egress on replication

---

## Q098: Carbon Aware Scheduling

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Sustainability |
| **Frequency** | Occasional |

### Question

Consider carbon-aware workload scheduling in cloud?

### Short Answer (30 seconds)

Run batch jobs in regions/time windows with lower carbon intensity grid — Azure sustainability APIs emerging — trade latency and data residency.

### Detailed Answer (3–5 minutes)

**Batch suitable:** ETL, ML training, report generation.

**Not suitable:** User-facing synchronous APIs with SLA.

**Architect:** Sustainability NFR for batch tier — document trade-off.

### Architecture Perspective

Sustainability pillar growing in enterprise architecture.

### Follow-up Questions

1. **Region selection FinOps? — Cost and carbon both factors.**
2. **On-prem renewable? — Hybrid scheduling complexity.**

### Common Mistakes in Interviews

- Carbon wash without measurement
- Move regulated data for green region illegally
- Ignore sustainability entirely in ADR

---

## Q099: Cloud Exit Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Strategy |
| **Frequency** | Common |

### Question

Document cloud exit strategy in architecture review.

### Short Answer (30 seconds)

Export data regular tested (Parquet, standard SQL dump), avoid proprietary-only formats in tier-0 data, portable compute (K8s, containers), contract terms, exit cost estimate.

### Detailed Answer (3–5 minutes)

**Mitigation levels:**
1. Accept managed service lock-in with export tested quarterly
2. Abstraction layer for portable subset
3. Full multi-cloud (rare)

**Architect:** Exit strategy is risk register item — not anti-cloud paranoia.

### Architecture Perspective

Pragmatic lock-in management impresses senior interviewers.

### Follow-up Questions

1. **Cosmos export? — Data migration toolkit — test size/time.**
2. **SaaS repurchase exit? — Data portability clauses in contract.**

### Common Mistakes in Interviews

- No export test ever
- Proprietary format critical archives
- Exit strategy taboo discussion

---

## Q100: Interview Whiteboard Azure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Interview Skills |
| **Frequency** | Very Common |

### Question

Draw Azure architecture for e-commerce checkout in 10 minutes.

### Short Answer (30 seconds)

Front Door → WAF → APIM → App Service/AKS → Azure SQL + Redis → Service Bus events → Functions consumers → App Insights.

### Detailed Answer (3–5 minutes)

**Label:** Identity (Entra), secrets (Key Vault), PCI zone segmentation.

**Mention:** RTO/RPO for payment DB, autoscale rules, rate limiting at APIM.

**Architect:** One deep dive area — e.g., idempotent payment handler.

### Architecture Perspective

Timed whiteboard practice is week 46 interview prep.

### Follow-up Questions

1. **Missing monitoring box? — Red flag in review.**
2. **Single region? — State DR assumption aloud.**

### Common Mistakes in Interviews

- Blob labeled 'database'
- No identity or secrets
- Cannot explain data flow arrows

---
