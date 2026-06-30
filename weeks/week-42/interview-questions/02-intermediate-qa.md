# Week 42 — Intermediate Q&A

> Q031–Q070: Premium format (Week 1 quality).

---


## Q031: FinOps Framework

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Very Common |

### Question

Explain the FinOps framework phases and architect's role in each.

### Short Answer (30 seconds)

Inform (visibility), Optimize (rate/usage), Operate (governance). Architect designs for cost observability, right-sizing, tagging, and unit economics — partners with FinOps team, doesn't own invoices alone.

### Detailed Answer (3–5 minutes)

**Three phases (FinOps Foundation):**
1. **Inform** — Allocation, showback/chargeback, anomaly detection, cost per team/product
2. **Optimize** — RI/Savings Plans, spot, storage tiering, architecture efficiency
3. **Operate** — Policies, budgets, guardrails, continuous improvement culture

**Architect responsibilities:**
- Tagging strategy in IaC (mandatory tags: costCenter, env, service)
- Cost estimates in ADRs
- Design patterns that scale cost linearly not exponentially
- Review autoscale and multi-region cost traps

**Principle:** Everyone takes ownership — engineering changes drive 80% of cloud bill.

### Architecture Perspective

FinOps is architecture concern — design choices become monthly invoices.

### Follow-up Questions

1. **Showback vs chargeback? — Showback reports; chargeback bills internal teams — political sensitivity.**
2. **Unit economics? — Cost per transaction/order/API call — architects define measurable denominator.**

### Common Mistakes in Interviews

- FinOps only finance team problem
- No cost estimate in architecture review
- Optimizing RI before tagging and visibility

---

## Q032: Cost Allocation Tags

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Very Common |

### Question

Design a cloud cost allocation tagging strategy for enterprise.

### Short Answer (30 seconds)

Mandatory tags: environment, costCenter, application, owner, dataClassification. Enforce via Azure Policy/AWS SCP — untagged resources blocked or flagged. Map tags to FinOps dashboards and chargeback.

### Detailed Answer (3–5 minutes)

**Tag schema:**
| Tag | Example | Purpose |
|-----|---------|--------|
| env | prod/staging/dev | Separate prod spend |
| costCenter | CC-4521 | Finance allocation |
| service | order-api | Microservice granularity |
| owner | team-checkout | Accountability |

**Enforcement:**
- IaC linter fails PR missing tags
- Weekly report via Azure Policy `requireTag`
- Exception process with expiry

**Architect:** Tags must exist before first deploy — retrofitting 10K resources is painful.

### Architecture Perspective

Untagged cloud spend is ungovernable spend.

### Follow-up Questions

1. **Tag cardinality explosion? — Limit free-text — use catalog values.**
2. **Shared services allocation? — Apportion APIM, AKS cluster by usage metric or fixed split ADR.**

### Common Mistakes in Interviews

- Optional tags ignored by all teams
- Different tag keys per cloud/account
- Tags on compute but not storage or egress

---

## Q033: Reserved Instances Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Very Common |

### Question

When and how use reserved instances or savings plans in cloud architecture?

### Short Answer (30 seconds)

Commit 1–3 year reservations for steady-state baseline (70–80% of min capacity). Keep burst on-demand/spot. Architect documents baseline in capacity plan; FinOps purchases; review quarterly.

### Detailed Answer (3–5 minutes)

**Decision framework:**
1. Measure 30–90 day steady utilization
2. Baseline = p10 usage or committed minimum
3. RI/Savings Plan covers baseline; on-demand above
4. Avoid 100% RI — elasticity lost

**Azure:** Reserved VM instances, SQL RI, Cosmos reserved capacity. **Exchange/split** if workload changes.

**Architect:** Stateless autoscale tiers shouldn't be 100% RI — mix RI app pool + on-demand burst pool.

### Architecture Perspective

RI strategy is architecture + finance joint decision — wrong RI locks wrong shape.

### Follow-up Questions

1. **Savings Plan vs RI? — Savings Plan flexible across VM families; RI deeper discount specific SKU.**
2. **3-year vs 1-year? — 3-year only for proven stable workloads.**

### Common Mistakes in Interviews

- Buy RI before 90-day utilization analysis
- RI on dev/test ephemeral environments
- No process to exchange RI when architecture pivots

---

## Q034: Spot and Preemptible Workloads

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Very Common |

### Question

Design workloads suitable for spot/preemptible instances.

### Short Answer (30 seconds)

Fault-tolerant, interruptible batch: CI runners, ML training, render farms, stateless workers with queue retry. Not for synchronous user-facing Tier-0 without checkpointing.

### Detailed Answer (3–5 minutes)

**Patterns:**
- **Worker pool** — K8s spot node pool + on-demand system pool
- **Checkpoint** — ML training saves every N minutes to blob
- **Spot-friendly queue** — Message visibility timeout handles eviction
- **Diversification** — Multiple instance types/AZs reduce capacity crunch

**Azure:** Spot VMs, AKS spot node pools with eviction handler.

**Architect:** Design for `SIGTERM` — graceful drain within 30s notice.

### Architecture Perspective

Spot cuts compute 60–90% — architecture must tolerate interruption.

### Follow-up Questions

1. **Spot for stateful database? — Never primary DB — batch only.**
2. **Fallback on spot unavailable? — On-demand node pool autoscaler.**

### Common Mistakes in Interviews

- Spot nodes without PodDisruptionBudget
- Long single-node job with no checkpoint
- Tier-0 API on spot pool only

---

## Q035: DR Tier 0–3

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DR |
| **Frequency** | Very Common |

### Question

Explain DR tiers 0–3 and map workloads to each.

### Short Answer (30 seconds)

Tier 0: no DR (dev). Tier 1: backup restore hours–days RTO. Tier 2: warm standby region minutes–hours. Tier 3: active-active near-zero RTO. Match tier to business impact analysis.

### Detailed Answer (3–5 minutes)

| Tier | RTO | RPO | Pattern | Example |
|------|-----|-----|---------|--------|
| 0 | N/A | N/A | None | Dev sandboxes |
| 1 | 24h+ | 24h | Backup/restore | Internal wiki |
| 2 | 1–4h | 15m–1h | Warm standby, ASR | Order API |
| 3 | <15m | ~0 | Active-active multi-region | Payment auth |

**Architect:** BIA assigns tier per capability — not one tier for whole company.

**Cost:** Tier 3 costs 1.5–2.5× Tier 2 — justify with revenue at risk.

### Architecture Perspective

DR tier drives architecture and budget — document in NFR matrix.

### Follow-up Questions

1. **Tier 2 vs 3 decision? — Revenue/minute + regulatory RTO drives tier.**
2. **Tier inflation? — Everything labeled Tier 3 — FinOps pushback required.**

### Common Mistakes in Interviews

- Production payment on Tier 0
- Same DR tier for batch reporting and checkout
- DR tier in spreadsheet not linked to infra design

---

## Q036: RTO and RPO Tradeoffs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DR |
| **Frequency** | Very Common |

### Question

Explain RTO/RPO tradeoffs and how they drive architecture.

### Short Answer (30 seconds)

RPO = max acceptable data loss (time). RTO = max acceptable downtime. Lower each = more replication, redundancy, cost. Architect captures business input and designs to measurable targets.

### Detailed Answer (3–5 minutes)

**Tradeoff examples:**
- RPO 0 → synchronous replication, dual-write complexity, latency cost
- RPO 15 min → async replication acceptable
- RTO 5 min → warm standby + automated failover
- RTO 4 hours → backup restore + runbook may suffice

**Formula for stakeholders:** `Cost ∝ 1/RTO + 1/RPO` approximately.

**Architect:** Document assumptions — 'RPO 15 min assumes replication lag monitored with alert at 5 min.'

### Architecture Perspective

RTO/RPO are business numbers that become replication topology.

### Follow-up Questions

1. **RPO 0 across regions? — Sync replication — watch cross-region latency impact.**
2. **RTO without tested runbook? — Fantasy — drill proves real RTO.**

### Common Mistakes in Interviews

- Confusing RTO with RPO in interview
- Promising RTO 5 min with cold backup only
- No monitoring of replication lag vs RPO

---

## Q037: Backup vs Replication

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DR |
| **Frequency** | Very Common |

### Question

When choose backup/restore vs continuous replication for DR?

### Short Answer (30 seconds)

Backup: point-in-time snapshots, lower cost, higher RTO/RPO — good Tier 1. Replication: near-real-time copy, lower RPO, higher cost — Tier 2/3. Often both — replication for fast failover, backup for corruption protection.

### Detailed Answer (3–5 minutes)

**Backup strengths:**
- Protects against logical corruption/ransomware (immutable vault)
- Cheaper for large cold data
- Long retention compliance

**Replication strengths:**
- Low RPO for outage not corruption
- Faster RTO failover

**Architect pattern:** Geo-replicated DB + daily backup to immutable storage. Failover to replica; restore backup if bad data propagated.

### Architecture Perspective

Backup and replication solve different failure modes — need both for Tier-2+.

### Follow-up Questions

1. **Immutable backup? — Azure Backup vault soft-delete + immutability — ransomware defense.**
2. **Replication lag test? — Failover drill measures effective RPO.**

### Common Mistakes in Interviews

- Replication only — no backup for oops DELETE
- Backup never restored in drill
- Backup same region as primary only

---

## Q038: Azure Site Recovery

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DR |
| **Frequency** | Very Common |

### Question

Design DR using Azure Site Recovery for hybrid or Azure workloads.

### Short Answer (30 seconds)

ASR replicates VMs, physical servers, or Azure VMs to secondary region. Orchestrated failover runbooks, non-disruptive test failover, RPO ~5 min for Azure-to-Azure.

### Detailed Answer (3–5 minutes)

**Architecture:**
- Source: Azure VM in East US → Target: West US replica
- Replication policy: crash-consistent vs app-consistent (VSS/SQL)
- Failover runbook: NSG, DNS Traffic Manager flip, SQL availability
- Test failover: isolated network — no production impact

**Integration:** Traffic Manager or Front Door health probe triggers user traffic shift post-failover.

**Architect:** ASR is Tier-2 enabler — still need application-level idempotency and DNS TTL planning.

### Architecture Perspective

ASR handles VM replication — app must handle regional failover semantics.

### Follow-up Questions

1. **App-consistent snapshot? — Required for SQL/AD — brief quiesce.**
2. **Failback plan? — Reverse replication after primary restored — document steps.**

### Common Mistakes in Interviews

- Failover without DNS plan — users hit dead region
- Never tested failover — unknown RTO
- ASR for pet VM with manual config drift

---

## Q039: Chaos Engineering

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Resilience |
| **Frequency** | Very Common |

### Question

Introduce chaos engineering in enterprise architecture responsibly.

### Short Answer (30 seconds)

Start in non-prod, expand to controlled prod experiments with blast radius limits. Inject failures (kill pod, latency, AZ loss) to validate assumptions in ADRs and runbooks.

### Detailed Answer (3–5 minutes)

**Maturity path:**
1. Game days in staging — manual failure injection
2. Automated chaos in staging CI (Chaos Mesh, Azure Chaos Studio)
3. Prod experiments: small blast, business hours, rollback ready

**Hypothesis format:** 'If AZ-B fails, checkout maintains 99.95% — error budget OK.'

**Architect:** Chaos findings update risk register and ADRs — closed loop.

### Architecture Perspective

Chaos proves DR/architecture claims — not just documentation.

### Follow-up Questions

1. **Azure Chaos Studio? — Managed fault injection for Azure resources — start here on Azure.**
2. **Blast radius? — One namespace/customer shard — not whole cluster day one.**

### Common Mistakes in Interviews

- Chaos in prod day one without staging practice
- Experiments without hypothesis or success criteria
- Findings not fed back to architecture review

---

## Q040: Load Testing with k6

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Very Common |

### Question

How use k6 for architecture validation and performance gates?

### Short Answer (30 seconds)

k6 scripts define VUs, duration, thresholds (p95<300ms, error<1%). Run in CI against staging, compare to performance budget, block deploy on regression.

### Detailed Answer (3–5 minutes)

**Architecture integration:**
```javascript
export const options = { thresholds: { http_req_duration: ['p(95)<300'] } };
```
- Pre-release: load test against prod-like staging
- Synthetic prod: small constant k6 cloud run against canary
- Results → Grafana/dashboard + CI artifact

**Scenarios:** Smoke (10 VU), load (expected peak), stress (2× peak), soak (24h).

**Architect:** Performance NFRs must map to k6 thresholds — not 'we load tested once.'

### Architecture Perspective

k6 connects NFR documentation to CI gates.

### Follow-up Questions

1. **k6 vs JMeter? — k6 script-as-code, CI-native — preferred for modern pipelines.**
2. **Test data realism? — Synthetic users with production-like payload sizes.**

### Common Mistakes in Interviews

- Load test only localhost dev machine
- No thresholds — manual eyeball latency
- Skip soak test before Black Friday

---

## Q041: Performance Budgets

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Very Common |

### Question

Define and enforce frontend/backend performance budgets.

### Short Answer (30 seconds)

Budget caps per resource: JS bundle 200KB, LCP <2.5s, API p99 <500ms. Track in CI (Lighthouse, k6); exceed budget = fix or ADR exception.

### Detailed Answer (3–5 minutes)

**Example budgets:**
| Layer | Metric | Budget |
|-------|--------|--------|
| Web | LCP | 2.5s |
| Web | Total JS | 250KB gzip |
| API | p99 latency | 300ms |
| DB | Query p95 | 50ms |

**Enforcement:** Bundle analyzer in PR; Lighthouse CI; k6 thresholds.

**Architect:** Budgets negotiated with product — trade features vs speed explicitly.

### Architecture Perspective

Performance budgets prevent death by a thousand optimizations deferred.

### Follow-up Questions

1. **Budget regression who fixes? — Team owning PR that exceeded — same as test failure.**
2. **Mobile vs desktop budgets? — Separate — mobile stricter on JS weight.**

### Common Mistakes in Interviews

- Budgets defined but not in CI
- One global budget for all APIs
- Waivers without expiry date

---

## Q042: Latency SLO

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SLO |
| **Frequency** | Very Common |

### Question

Define latency SLO for a customer-facing API architecture.

### Short Answer (30 seconds)

SLO example: 99% of requests <300ms over 30-day window excluding client errors. SLI measured at load balancer; error budget policy gates risky releases.

### Detailed Answer (3–5 minutes)

**Components:**
- **SLI** — Histogram from APM (Application Insights)
- **SLO** — 99% < 300ms monthly
- **Error budget** — 1% slow requests allowed — ~7.2h equivalent slow time/month

**Architecture implications:**
- Cache, CDN, read replicas consume budget for writes
- Async patterns for non-latency-critical work

**Architect:** SLO in ADR; dashboards linked from service catalog.

### Architecture Perspective

Latency SLO drives caching, sync vs async, and regional placement.

### Follow-up Questions

1. **SLO vs SLA? — SLA customer contract; SLO internal target stricter than SLA.**
2. **Tail latency? — p99/p999 SLO separately from p50 — user experience at tail.**

### Common Mistakes in Interviews

- SLO measured only in dev
- No error budget policy
- Latency SLO ignores dependency chain

---

## Q043: Capacity Planning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Very Common |

### Question

Describe capacity planning process for cloud-native architecture.

### Short Answer (30 seconds)

Forecast from business growth + seasonality, model CPU/memory/QPS per service, load test validation, headroom 30%, plan scale events (Black Friday), review quarterly.

### Detailed Answer (3–5 minutes)

**Steps:**
1. **Demand forecast** — Product growth %, marketing events
2. **Current utilization** — p95 CPU, DB DTU, queue depth
3. **Model** — `peak QPS × payload × instances needed`
4. **Validate** — k6 stress test
5. **Plan** — Scale limits, pre-warm, RI baseline

**Architect:** Capacity plan linked to FinOps — scaling isn't infinite money.

### Architecture Perspective

Capacity planning bridges business forecast and infra scale.

### Follow-up Questions

1. **Vertical vs horizontal headroom? — Prefer horizontal with autoscale ceiling defined.**
2. **Pre-warming? — AKS cluster autoscaler + scheduled scale-up before known peak.**

### Common Mistakes in Interviews

- Capacity = max autoscale with no limit
- No seasonal planning for retail
- DB capacity ignored until connection exhaustion

---

## Q044: Right-Sizing Reviews

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Very Common |

### Question

Run right-sizing reviews for cloud resources.

### Short Answer (30 seconds)

Monthly/quarterly: identify CPU<20% p95 VMs, oversized DB tiers, unused disks/IP. Recommend downsize, consolidate, or serverless. Track savings in FinOps dashboard.

### Detailed Answer (3–5 minutes)

**Review sources:**
- Azure Advisor, AWS Compute Optimizer
- Custom: 30-day max CPU <30% → candidate
- Database: DTU/vCore utilization vs tier

**Process:**
1. Generate report by owner tag
2. Owner accepts or documents why oversized (burst, compliance)
3. Change window execution
4. Measure 30-day post-change performance

**Architect:** Right-size in architecture review — don't default to largest SKU 'to be safe'.

### Architecture Perspective

Right-sizing is continuous — cloud makes oversizing easy.

### Follow-up Questions

1. **Rightsize production without load test? — Downsize staging first — validate p99.**
2. **Rightsizing vs performance SLO? — Never save cost breaking SLO — rollback.**

### Common Mistakes in Interviews

- One-time exercise then forgotten
- Downsize DB breaking burst headroom
- No owner notification — surprise ticket to ops

---

## Q045: Idle Resource Cleanup

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Very Common |

### Question

Architect policies for idle cloud resource cleanup.

### Short Answer (30 seconds)

Automated detection: unattached disks, old snapshots, stopped VMs >30 days, unused load balancers, orphaned IPs. Policy: notify → auto-delete after grace with exceptions.

### Detailed Answer (3–5 minutes)

**Architecture policies:**
- Dev env TTL — auto-shutdown nights/weekends (Azure Automation)
- Tag `expiresOn` for POC resources
- Weekly FinOps report to engineering managers
- Azure Policy: delete unattached disks after 7 days (non-prod)

**Architect:** Sandbox subscriptions with budget caps and mandatory expiry — innovation without waste.

### Architecture Perspective

Idle resources are recurring leak — automate cleanup not quarterly heroics.

### Follow-up Questions

1. **Zombie resources? — VM stopped but disk/IP/LB billing — holistic scan.**
2. **Exception process? — Legal hold, long-running migration — tagged `noCleanup`.**

### Common Mistakes in Interviews

- Production cleanup automation without safeguard tags
- Ignore object storage lifecycle policies
- No FinOps visibility into idle spend

---

## Q046: Multi-Region DR Cost

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Very Common |

### Question

Analyze cost of multi-region DR architecture.

### Short Answer (30 seconds)

Multi-region adds: duplicate compute/storage baseline, cross-region replication egress, Traffic Manager, operational complexity. Model Tier-2 vs Tier-3 TCO in ADR — often 40–100% premium over single region.

### Detailed Answer (3–5 minutes)

**Cost components:**
- **Compute** — Warm standby 50–100% of primary or active-active 200%
- **Data** — Geo-redundant storage, SQL geo-replication
- **Egress** — Replication traffic between regions
- **Ops** — Dual runbooks, dual on-call familiarity

**Optimization:**
- Tier-2: scale-to-minimum in DR region until failover
- Async replication vs sync for RPO tradeoff
- Shared global services (CDN, DNS) amortized

**Architect:** Present $/month delta in ADR — executives approve cost not diagrams alone.

### Architecture Perspective

Multi-region DR is insurance premium — quantify it.

### Follow-up Questions

1. **Active-passive savings? — DR region min instances — scale on failover — slower RTO.**
2. **Licensing in DR region? — Include SQL replica cores in TCO.**

### Common Mistakes in Interviews

- Active-active everywhere without business case
- Ignore cross-region egress in estimate
- DR region untested — paying for false confidence

---

## Q047: DR Drill Frequency

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DR |
| **Frequency** | Very Common |

### Question

How often run DR drills and what should they prove?

### Short Answer (30 seconds)

Tier-3: quarterly partial + annual full failover. Tier-2: semi-annual failover test. Tier-1: annual restore test. Drill proves RTO/RPO, runbook accuracy, and communication chain.

### Detailed Answer (3–5 minutes)

**Drill types:**
- **Tabletop** — Walk runbook verbally — quarterly
- **Test failover** — ASR isolated network — semi-annual
- **Full failover** — Production traffic shift — annual with exec approval

**Success criteria:**
- Measured RTO within NFR
- Data integrity checks pass
- All integrations accounted for (payments, identity)

**Architect:** Drill findings are ADR inputs — update design if RTO missed.

### Architecture Perspective

Untested DR is wishful thinking — drills are architecture validation.

### Follow-up Questions

1. **Game day vs DR drill? — Game day chaos broader; DR drill focused on region loss.**
2. **Communications drill? — Include status page and support scripts.**

### Common Mistakes in Interviews

- Last drill 3 years ago
- Test failover never run — only PowerPoint
- Drill success not measured against RTO

---

## Q048: Performance Regression in CI

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Very Common |

### Question

Detect performance regression in CI/CD pipeline.

### Short Answer (30 seconds)

Baseline k6/Lighthouse on main branch; PR runs same suite against ephemeral env; compare p95 latency and bundle size; fail if >10% regression unless waiver.

### Detailed Answer (3–5 minutes)

**Pipeline design:**
```
PR → deploy staging → k6 smoke + benchmark → compare to main baseline → pass/fail
```

**Tools:** k6 thresholds, Lighthouse CI, .NET BenchmarkDotNet for hot paths.

**Flaky perf tests:** Fixed seed data, warm-up requests, statistical comparison over 3 runs.

**Architect:** Perf regression gate as important as unit test gate for Tier-0 services.

### Architecture Perspective

CI perf gates catch degradation before customers do.

### Follow-up Questions

1. **Micro-benchmark vs load test? — Unit micro for hot function; k6 for integration path.**
2. **Baseline storage? — Store main branch metrics in blob — PR compares delta.**

### Common Mistakes in Interviews

- Perf tests run locally only before release
- Flaky thresholds cause team to disable gate
- No warm-up — cold start false regression

---

## Q049: Flame Graphs for Performance

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Common |

### Question

Use flame graphs to diagnose performance issues in production architecture.

### Short Answer (30 seconds)

Flame graph stacks CPU samples — wide bar = hot path. Collect via dotnet-trace, perf, Azure Profiler; identify synchronous blocking, allocation hotspots, unexpected library cost.

### Detailed Answer (3–5 minutes)

**Workflow:**
1. APM shows elevated p99 on OrderService
2. Capture trace under load (Continuous Profiler or manual sample)
3. Flame graph reveals 40% time in JSON serialization
4. Fix: source-generated serializer or cache

**Architect:** Enable always-on lightweight profiler in prod (sample 1%) — not only during incidents.

### Architecture Perspective

Flame graphs turn 'it's slow' into actionable hot functions.

### Follow-up Questions

1. **.NET tool? — dotnet-trace + Speedscope flame graph export.**
2. **Production safety? — Sampling profiler low overhead — avoid always-on full trace.**

### Common Mistakes in Interviews

- Optimize without profiling — guess wrong layer
- Profile dev laptop not production-like load
- Ignore async blocked thread stacks

---

## Q050: Database Performance Baseline

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Very Common |

### Question

Establish database performance baseline for architecture reviews.

### Short Answer (30 seconds)

Capture top 20 queries by CPU/duration, p95 latency, connection count, IOPS, lock waits at peak. Document in performance appendix; re-baseline after schema major change.

### Detailed Answer (3–5 minutes)

**Baseline artifact:**
| Query/SP | p95 ms | Exec/min | Plan type |

**Sources:** Query Store, pg_stat_statements, Azure SQL Insights.

**Review triggers:**
- New microservice DB access pattern
- 10× data growth projection
- Read replica decision

**Architect:** Baseline prevents 'works in dev' — prod cardinality differs.

### Architecture Perspective

DB baseline is evidence for indexing, sharding, and cache ADRs.

### Follow-up Questions

1. **Baseline drift alert? — Query Store regression alert on plan change.**
2. **Connection pool baseline? — Include pool exhaustion threshold.**

### Common Mistakes in Interviews

- No Query Store enabled in prod
- Baseline taken at 3am low traffic only
- Ignore lock/deadlock metrics in baseline

---

## Q051: CDN Cost Optimization

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

Optimize CDN costs without hurting performance.

### Short Answer (30 seconds)

Cache hit ratio optimization, correct TTL tiers, compress images (WebP/AVIF), origin shield, eliminate cache busting abuse, geo-tier pricing awareness, log sampling.

### Detailed Answer (3–5 minutes)

**Tactics:**
- Long TTL static assets with fingerprinted filenames
- Shorter TTL only for HTML shell
- Origin minimize — BFF aggregation reduces origin trips
- Monitor **egress** vs **request** billing dimensions

**Azure Front Door / CDN:** Caching rules by path; disable cache on authenticated API paths.

**Architect:** CDN is not free at scale — model $/TB in FinOps review.

### Architecture Perspective

CDN cost grows with poor cache strategy — architecture controls hit ratio.

### Follow-up Questions

1. **Cache key design? — Vary by Accept-Language not UserId — avoid cache fragmentation.**
2. **Purging strategy? — Versioned assets minimize full purge events.**

### Common Mistakes in Interviews

- Cache-Control: no-store on all static assets
- Huge uncached video through expensive tier
- Ignore CDN bill — only origin cost tracked

---

## Q052: Autoscale Cost Traps

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Very Common |

### Question

Identify autoscaling configurations that cause cost surprises.

### Short Answer (30 seconds)

Min instances too high, scale-out without scale-in delay, CPU-only trigger ignoring memory, runaway scale from retry storm, missing max instance cap, scale during DDoS.

### Detailed Answer (3–5 minutes)

**Traps:**
1. **minReplicas=10 always** — Paying peak at off-peak
2. **No max** — Bug causes 500 instances overnight
3. **Aggressive scale-out** — +10 instances per 1% CPU spike
4. **Missing scale-in** — Instances never terminate
5. **Wrong metric** — Scale on queue depth without consumer count

**Mitigations:** Budget alerts, max replicas, scale-in stabilization window, scale on custom metric (requests/instance).

**Architect:** Autoscale rules in IaC reviewed like code — FinOps signs off max cap.

### Architecture Perspective

Autoscale without caps is unlimited budget liability.

### Follow-up Questions

1. **Scheduled scale? — Pre-scale before peak cheaper than reactive over-provision stuck.**
2. **KEDA? — Scale to zero for sporadic workloads — save off-hours.**

### Common Mistakes in Interviews

- Autoscale max = unlimited
- Scale-out without diagnosing retry loop cause
- Production min instances = load test peak forever

---

## Q053: FinOps Team Structure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

Describe FinOps team structure and how architects collaborate.

### Short Answer (30 seconds)

Central FinOps practice (3–10 people) + embedded champions per tribe. FinOps owns process/dashboards; architects own design efficiency; finance owns allocation policy.

### Detailed Answer (3–5 minutes)

**Roles:**
- **FinOps lead** — Strategy, vendor negotiation, reporting
- **FinOps analyst** — Dashboards, anomaly response, RI planning
- **Engineering champions** — Tag compliance, right-sizing in squads
- **Architect liaison** — Cost in ADR review, unit economics

**Cadence:** Monthly cost review with engineering directors; quarterly executive summary.

**Architect:** Attend cost review for top 10 services — not optional optional meeting.

### Architecture Perspective

FinOps succeeds as partnership — not finance policing engineering.

### Follow-up Questions

1. **CFO dashboard? — Executive view of unit cost trend — architect supplies denominator.**
2. **Maturity L1→L3? — L1 visibility, L2 optimization, L3 continuous unit economics.**

### Common Mistakes in Interviews

- FinOps buys RI without engineering input
- No engineering representation in FinOps council
- Architect never sees cloud bill data

---

## Q054: Unit Economics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Very Common |

### Question

Apply unit economics to cloud architecture decisions.

### Short Answer (30 seconds)

Cost per business unit: $/order, $/MAU, $/API call, $/inference. Architects design telemetry to measure denominator; FinOps tracks numerator — together optimize margin.

### Detailed Answer (3–5 minutes)

**Example:**
- Checkout: $0.012 per order all-in infra
- Target: reduce to $0.009 via cache hit + right-size

**Architecture levers:**
- Reduce cross-AZ chatter
- Batch vs real-time inference
- Storage tier lifecycle

**Dashboard:** Grafana panel — unit cost 30-day trend by service tag.

**Architect:** Unit economics in ADR consequences — 'Option B saves $0.003/order at 10M orders/month.'

### Architecture Perspective

Unit economics connects architecture to P&L — executives understand this.

### Follow-up Questions

1. **Denominator definition? — Agree with finance — gross vs net orders.**
2. **Shared platform allocation? — Amortize K8s control plane across services by CPU share.**

### Common Mistakes in Interviews

- Only total cloud spend tracked
- Unit cost rising — no architectural response
- Compare options without normalizing per transaction

---

## Q055: Cost Anomaly Response

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Very Common |

### Question

Design cost anomaly detection and response runbook.

### Short Answer (30 seconds)

Alert on daily spend >20% vs 7-day baseline by subscription/service tag. Runbook: identify resource, owner, intentional vs leak, mitigate (scale down, kill resource), postmortem.

### Detailed Answer (3–5 minutes)

**Detection:**
- Azure Cost Management alerts
- Custom: anomaly ML on hourly grain
- Budget thresholds at 80/100/120%

**Response steps:**
1. Page FinOps champion + service owner (from tags)
2. Identify top delta resources in portal
3. Mitigate — disable runaway scale, delete crypto-mining VM
4. Communicate if customer impact
5. Postmortem — policy gap?

**Architect:** Design kill switches and max caps so anomaly can't 10× overnight bill.

### Architecture Perspective

Cost anomaly response is incident response — same urgency as outage.

### Follow-up Questions

1. **Cryptomining on compromised account? — Anomaly + GuardDuty — revoke keys.**
2. **False positive? — Marketing launch spike — whitelist event tag.**

### Common Mistakes in Interviews

- No tags — can't find owner during anomaly
- Budget alert only monthly — too late
- Anomaly fixed without root cause policy update

---

## Q056: FinOps Culture Basics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Very Common |

### Question

What does a healthy FinOps culture look like in an engineering organization?

### Short Answer (30 seconds)

Engineers, product, and finance share cost accountability with regular cost reviews and clear ownership.

### Detailed Answer (3–5 minutes)

**Key traits:** cost visibility by team, unit-economics mindset, and optimization built into delivery rituals.

FinOps is not a monthly finance report; it is continuous engineering behavior.

### Architecture Perspective

Interviewers look for collaboration model, not tool names only.

### Follow-up Questions

1. **Who owns cloud cost? -> Shared ownership: product + engineering + finance.**
2. **How often review costs? -> Weekly at team level, monthly at portfolio level.**

### Common Mistakes in Interviews

- Treating FinOps as finance-only function
- No tagging/ownership for spend
- Cost reviews with no action items

---

## Q057: Cost Allocation Foundations

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

How do you set up cost allocation so teams trust the numbers?

### Short Answer (30 seconds)

Use consistent tagging/account structure, shared cost rules, and transparent allocation logic.

### Detailed Answer (3–5 minutes)

Start with mandatory tags (team, product, environment, criticality).

Define clear rules for shared platform costs and document them.

Publish allocation methodology so disputes can be resolved objectively.

### Architecture Perspective

Trust in cost data is prerequisite for optimization.

### Follow-up Questions

1. **What if tags are missing? -> Enforce policy and quarantine unallocated spend in reports.**
2. **How allocate shared services? -> Driver-based split (traffic, tenants, usage units).**

### Common Mistakes in Interviews

- Arbitrary monthly cost split
- No governance on tagging quality
- Changing allocation logic without communication

---

## Q058: Reserved Instances 101

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

When are reserved instances or savings plans a good fit?

### Short Answer (30 seconds)

Use them for stable baseline usage with predictable runtime patterns.

### Detailed Answer (3–5 minutes)

Analyze utilization history and commit only for durable baseline, not burst traffic.

Combine commitments with autoscaling for variability.

Monitor coverage and utilization monthly to avoid over-commitment waste.

### Architecture Perspective

Commitments are financial architecture decisions with operational assumptions.

### Follow-up Questions

1. **What is over-commitment risk? -> Paying for unused capacity when demand drops.**
2. **Can commitments and spot coexist? -> Yes, for baseline + opportunistic burst.**

### Common Mistakes in Interviews

- Committing based on one short data window
- Applying commitments to volatile workloads
- No periodic utilization review

---

## Q059: DR Tier Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Disaster Recovery |
| **Frequency** | Common |

### Question

What are common disaster recovery tiers and how do they differ?

### Short Answer (30 seconds)

Cold, warm, and hot strategies trade recovery speed for cost and operational complexity.

### Detailed Answer (3–5 minutes)

Cold: cheapest, longest recovery.

Warm: partial pre-provisioning, medium RTO.

Hot-active: near-immediate recovery, highest cost and operational discipline.

Choose tier per workload criticality and business tolerance.

### Architecture Perspective

DR architecture is business-risk budgeting.

### Follow-up Questions

1. **Can one app have mixed tiers? -> Yes, by component criticality.**
2. **Who defines tier? -> Business owner with architecture/SRE input.**

### Common Mistakes in Interviews

- Same DR tier for all workloads
- No documented assumptions for tier choice
- Ignoring operational runbook readiness

---

## Q060: RTO and RPO Basics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Disaster Recovery |
| **Frequency** | Very Common |

### Question

Explain RTO and RPO in practical terms.

### Short Answer (30 seconds)

RTO is max acceptable downtime; RPO is max acceptable data loss window.

### Detailed Answer (3–5 minutes)

If RTO is 1 hour, service must recover within 1 hour.

If RPO is 15 minutes, restored data can be at most 15 minutes behind.

These targets drive architecture and budget decisions.

### Architecture Perspective

Many teams confuse these; clarity is expected in interviews.

### Follow-up Questions

1. **Can low RTO have high RPO? -> Yes, depending on design and replication strategy.**
2. **Who signs targets? -> Business and risk owners, not engineers alone.**

### Common Mistakes in Interviews

- Using RTO/RPO terms without numeric targets
- Setting unrealistic targets without budget
- No validation drills against targets

---

## Q061: Azure Site Recovery Intro

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Disaster Recovery |
| **Frequency** | Common |

### Question

What role does Azure Site Recovery play in DR strategy?

### Short Answer (30 seconds)

It replicates workloads and orchestrates failover/failback for defined recovery plans.

### Detailed Answer (3–5 minutes)

ASR helps implement warm/hot DR patterns for supported workloads.

You still need tested runbooks, dependency ordering, and business validation.

Tooling supports strategy; it does not replace design.

### Architecture Perspective

Mentioning orchestration plus testing maturity shows practical depth.

### Follow-up Questions

1. **Does ASR guarantee business continuity alone? -> No, application dependencies still matter.**
2. **How often test failover? -> Scheduled non-disruptive drills plus periodic full exercises.**

### Common Mistakes in Interviews

- Buying ASR and assuming DR is done
- No application-level recovery testing
- No failback plan

---

## Q062: Chaos Engineering Purpose

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Common |

### Question

Why does chaos engineering matter for reliability programs?

### Short Answer (30 seconds)

It validates resilience assumptions by testing controlled failures before real incidents happen.

### Detailed Answer (3–5 minutes)

Start with low-blast-radius experiments aligned to known risks.

Define steady-state metrics and abort conditions.

Use findings to improve architecture, alerts, and runbooks.

### Architecture Perspective

Chaos is disciplined experimentation, not random outage simulation.

### Follow-up Questions

1. **Where start first? -> Dependency timeouts, pod/node failure, and regional loss assumptions.**
2. **Who should approve experiments? -> SRE/platform with service owners.**

### Common Mistakes in Interviews

- Running chaos in production without guardrails
- No measurable hypothesis before experiment
- No follow-through after findings

---

## Q063: k6 Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Common |

### Question

What is k6 commonly used for in performance engineering?

### Short Answer (30 seconds)

Scripted load and stress testing to validate latency, throughput, and error behavior.

### Detailed Answer (3–5 minutes)

k6 supports repeatable scenarios in CI/CD and pre-release testing.

Use realistic traffic models and assert thresholds tied to SLOs.

Performance tests should be versioned like code.

### Architecture Perspective

Interviewers value repeatability and threshold-driven testing.

### Follow-up Questions

1. **Can k6 run in CI? -> Yes, with budgeted test tiers.**
2. **What metrics matter most? -> p95/p99 latency, errors, saturation indicators.**

### Common Mistakes in Interviews

- Only running ad hoc local load tests
- No realistic test data/profile
- No pass/fail thresholds

---

## Q064: Performance Budgets Intro

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Common |

### Question

What is a performance budget for backend services?

### Short Answer (30 seconds)

A defined latency/resource envelope that changes must stay within.

### Detailed Answer (3–5 minutes)

Example: p95 API latency < 250ms at target load and CPU < 70%.

Budgets make performance a planned constraint, not afterthought.

Use them in design and regression gates.

### Architecture Perspective

Budgets convert performance goals into enforceable engineering constraints.

### Follow-up Questions

1. **Who sets budgets? -> Product + architecture + SRE based on user expectations.**
2. **How enforce? -> CI perf checks and release gates.**

### Common Mistakes in Interviews

- Budgets defined but never measured
- No baseline before budgeting
- One budget for all endpoints equally

---

## Q065: Latency SLO Essentials

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Very Common |

### Question

How is a latency SLO different from a one-time performance target?

### Short Answer (30 seconds)

SLO is an ongoing reliability commitment measured over time, not a single benchmark run.

### Detailed Answer (3–5 minutes)

Define latency objective with window and error budget.

Track by user journey and percentile (often p95/p99).

Use burn-rate alerts to detect fast degradation.

### Architecture Perspective

SLOs align technical behavior with customer experience outcomes.

### Follow-up Questions

1. **Can every endpoint share same SLO? -> Usually no; critical paths differ.**
2. **Why percentile over average? -> Averages hide tail latency pain.**

### Common Mistakes in Interviews

- Only tracking average latency
- No time window or compliance rate
- No operational action tied to SLO breach

---

## Q066: Capacity Planning Basics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Common |

### Question

What inputs are needed for practical capacity planning?

### Short Answer (30 seconds)

Demand forecast, workload profile, growth assumptions, and saturation thresholds.

### Detailed Answer (3–5 minutes)

Use historical load plus business seasonality and launch events.

Model baseline, peak, and failure mode scenarios.

Revisit quarterly or after major architecture changes.

### Architecture Perspective

Capacity planning is a recurring practice, not annual paperwork.

### Follow-up Questions

1. **How include resilience? -> Model N-1 and zone/region failure capacity.**
2. **What if forecast confidence is low? -> Use scenario bands and adaptive scaling.**

### Common Mistakes in Interviews

- Planning from peak only
- No growth assumptions documented
- Ignoring failure scenarios

---

## Q067: Right-Sizing Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

What is right-sizing and why is it often missed?

### Short Answer (30 seconds)

Matching resource size to actual workload needs; often missed due to default overprovisioning and fear.

### Detailed Answer (3–5 minutes)

Analyze CPU, memory, IOPS, and queue depth trends.

Downsize gradually with guardrails and rollback.

Reassess after code/perf changes because ideal size shifts.

### Architecture Perspective

Right-sizing is low-risk, high-return FinOps when done with observability.

### Follow-up Questions

1. **How avoid outages while downsizing? -> Canary reductions and SLO monitoring.**
2. **How often revisit? -> Monthly for dynamic workloads, quarterly otherwise.**

### Common Mistakes in Interviews

- One-time right-sizing project then abandoned
- Downsizing without monitoring
- Ignoring memory/IO bottlenecks

---

## Q068: DR Drills and Readiness

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Disaster Recovery |
| **Frequency** | Common |

### Question

Why are DR drills mandatory even with automation tools?

### Short Answer (30 seconds)

They validate people, process, and dependency assumptions not covered by tooling.

### Detailed Answer (3–5 minutes)

Run scenario-based drills including communication paths and decision authority.

Capture actual recovery times and gaps.

Feed findings back into architecture and runbooks.

### Architecture Perspective

Recovery readiness is socio-technical, not tool-only.

### Follow-up Questions

1. **How frequent for critical systems? -> At least quarterly with varied scenarios.**
2. **What metric matters? -> Achieved vs target RTO/RPO and confidence trend.**

### Common Mistakes in Interviews

- Tabletop-only exercises forever
- No lessons learned tracking
- Drills skipped due to release pressure

---

## Q069: Perf Regression in CI

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Common |

### Question

How do you integrate performance regression checks into CI without slowing teams too much?

### Short Answer (30 seconds)

Use test tiers: fast smoke performance on PRs, deeper suites on schedule or pre-release.

### Detailed Answer (3–5 minutes)

Set endpoint-level thresholds and compare against baseline trends.

Fail builds only for meaningful regressions; warn on noise bands.

Keep test environment stable to reduce false positives.

### Architecture Perspective

Balanced CI performance strategy protects quality and developer flow.

### Follow-up Questions

1. **How avoid flaky perf gates? -> Standardize test env and use statistical thresholds.**
2. **What runs on PR? -> Narrow critical-path smoke profiles.**

### Common Mistakes in Interviews

- Running full load test on every commit
- No baseline versioning
- Ignoring regression alerts as 'test noise'

---

## Q070: Unit Economics Starter

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

What are unit economics in cloud architecture decisions?

### Short Answer (30 seconds)

They measure cost per business unit (order, tenant, API call) to guide scaling and optimization choices.

### Detailed Answer (3–5 minutes)

Map infrastructure and platform spend to business drivers.

Track trend over time and compare across architectures.

Use unit cost to prioritize optimization with highest business impact.

### Architecture Perspective

Unit economics connects architecture to business value language.

### Follow-up Questions

1. **Why better than total cloud spend? -> It normalizes growth and reveals efficiency.**
2. **What if allocation is imperfect? -> Start directional and improve granularity iteratively.**

### Common Mistakes in Interviews

- Optimizing total spend without usage context
- No shared definition of unit metric
- Ignoring feature-level cost impact

---
