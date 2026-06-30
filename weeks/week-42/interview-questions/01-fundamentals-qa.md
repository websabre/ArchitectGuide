# Week 42 — Fundamentals Interview Q&A

> Q001–Q030: Premium format (Week 1 quality).  
> See also: [Interview prep hub](../../../interview-prep/README.md)

---


## Q001: FinOps Principles Overview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | FinOps |
| **Frequency** | Very Common |

### Question

What are the core FinOps principles and how do architects participate?

### Short Answer (30 seconds)

FinOps = cultural practice where engineering, finance, and business share cloud cost accountability. Core principles: teams need visibility; everyone takes ownership; central team enables (not controls); decisions driven by business value. Architects embed cost into design — tagging, right-sizing, and unit economics.

### Detailed Answer (3–5 minutes)

**FinOps Foundation principles:**
1. **Teams need to collaborate** — Finance alone cannot optimize; engineers change 80% of spend
2. **Everyone takes ownership** — Cost per team visible via tags and showback
3. **Central team enables** — FinOps provides tooling, standards, and education — not gatekeeping
4. **Reports should be accessible** — Engineers see daily cost, not quarterly surprise
5. **Decisions driven by business value** — Optimize unit economics, not just total bill

**Architect responsibilities:**
- Mandatory cost tags in IaC (costCenter, env, service, owner)
- Cost estimate section in every Tier-0/1 ADR
- Design for linear cost scaling — avoid exponential surprises (unbounded logs, cross-AZ chatter)
- Partner with FinOps on capacity plans and RI baseline

**Three phases (Inform → Optimize → Operate):** Visibility first, then rate/usage optimization, then governance policies.

**Interview framing:** FinOps is not 'finance tells engineering to cut' — it's engineering accountability with finance partnership.

### Architecture Perspective

Architects who ignore FinOps design invoices they cannot explain to executives.

### Follow-up Questions

1. **Showback vs chargeback? — Showback reports cost; chargeback bills internal teams — political sensitivity.**
2. **Unit economics? — Cost per order/API call/tenant — architects define measurable denominator.**

### Common Mistakes in Interviews

- FinOps treated as finance-only problem
- No cost estimate in architecture review package
- Optimizing reserved instances before tagging and visibility exist

---

## Q002: DR Tier Classification

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DR |
| **Frequency** | Very Common |

### Question

How do you classify workloads into DR tiers and what drives tier assignment?

### Short Answer (30 seconds)

DR tiers map business impact to recovery patterns: Tier 0 (no DR, dev only), Tier 1 (backup/restore, hours–days RTO), Tier 2 (warm standby, minutes–hours), Tier 3 (active-active, near-zero RTO/RPO). Assignment comes from Business Impact Analysis — not engineer preference.

### Detailed Answer (3–5 minutes)

**Standard tier model:**
| Tier | RTO | RPO | Pattern | Example |
|------|-----|-----|---------|--------|
| 0 | N/A | N/A | None | Dev sandboxes, POC |
| 1 | 24h+ | 24h | Backup restore | Internal wiki, reporting |
| 2 | 1–4h | 15m–1h | Warm standby, ASR | Order API, CRM |
| 3 | <15m | ~0 | Active-active multi-region | Payment auth, core banking |

**Assignment process:**
1. Business Impact Analysis (BIA) — revenue/hour, regulatory penalty, reputational harm
2. Map capability to tier — per workload, not per company
3. Document in NFR matrix linked to ADR
4. FinOps validates tier cost against business case

**Architect guardrails:**
- Resist tier inflation — everything labeled Tier 3 doubles cloud spend
- Tier 3 requires proven failover drills, not aspiration
- Tier 0 acceptable for non-production only

**Cost signal:** Tier 3 typically costs 1.5–2.5× Tier 2 — justify with revenue at risk.

### Architecture Perspective

DR tier is business classification that becomes infrastructure topology — architects facilitate BIA, not guess.

### Follow-up Questions

1. **Tier 2 vs 3 decision? — Revenue per minute of outage + regulatory RTO mandate drives tier.**
2. **Tier documented where? — NFR matrix + ADR + CMDB — not orphaned spreadsheet.**

### Common Mistakes in Interviews

- Production payment path on Tier 0
- Same DR tier applied to batch reporting and checkout
- DR tier in spreadsheet not linked to infrastructure design

---

## Q003: RTO and RPO Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DR |
| **Frequency** | Very Common |

### Question

Define RTO and RPO and explain how they drive architectural decisions.

### Short Answer (30 seconds)

RPO (Recovery Point Objective) = maximum acceptable data loss measured in time. RTO (Recovery Time Objective) = maximum acceptable downtime. Lower targets require more replication, redundancy, automation, and cost — architects translate business tolerance into infrastructure design.

### Detailed Answer (3–5 minutes)

**Definitions:**
- **RPO 15 minutes** — At worst, lose 15 minutes of data since last durable copy
- **RTO 1 hour** — Service must be restored within 1 hour of outage declaration

**How targets drive architecture:**
| Target | Typical pattern |
|--------|----------------|
| RPO 24h | Nightly backup sufficient |
| RPO 15m | Async geo-replication + lag monitoring |
| RPO ~0 | Sync replication, dual-write complexity, latency trade-off |
| RTO 4h | Backup restore + documented runbook |
| RTO 15m | Warm standby with automated failover (ASR, DNS flip) |
| RTO <5m | Active-active, health-checked traffic shift |

**Stakeholder conversation:**
```
'How much data can we afford to lose?' → RPO
'How long can customers wait?' → RTO
```

**Architect:** Document assumptions — 'RPO 15 min assumes replication lag alert at 5 min.' Untested runbooks mean fantasy RTO.

### Architecture Perspective

RTO/RPO are business numbers that become replication topology — confuse them in interviews at your peril.

### Follow-up Questions

1. **RPO 0 across regions? — Synchronous replication — watch cross-region write latency impact.**
2. **RTO without tested runbook? — Drill proves real RTO; paper target is worthless.**

### Common Mistakes in Interviews

- Confusing RTO with RPO in interview answers
- Promising RTO 5 min with cold backup-only architecture
- No replication lag monitoring despite 15-minute RPO claim

---

## Q004: Load Testing Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Performance |
| **Frequency** | Very Common |

### Question

Design a load testing strategy for an enterprise system approaching production.

### Short Answer (30 seconds)

Load testing strategy defines scenarios (smoke, load, stress, soak), environments (prod-like staging), tools (k6, JMeter), thresholds tied to NFRs, CI integration, and go/no-go gates. Architects ensure tests validate realistic user journeys — not just health-check endpoints.

### Detailed Answer (3–5 minutes)

**Test scenario pyramid:**
| Scenario | Purpose | Scale |
|----------|---------|-------|
| Smoke | Pipeline sanity | 10 VU, 2 min |
| Load | Expected peak | 1× peak QPS, 30 min |
| Stress | Breaking point | 2–3× peak until failure |
| Soak | Memory leak, drift | 1× load, 12–24h |

**Architecture integration:**
```
NFR matrix → k6 thresholds → CI gate on staging → pre-release sign-off
```

**Environment requirements:**
- Prod-like data volume (anonymized), network topology, and dependency mocks where unsafe
- Isolated from production — never load test prod without explicit chaos program
- Results stored as CI artifacts + Grafana dashboard

**Go/no-go criteria:**
- p95 latency within performance budget
- Error rate <0.1% under expected peak
- No resource exhaustion (connection pool, thread leak) in soak test

**Architect:** Map every performance NFR to a named test scenario — 'we load tested once' is not a strategy.

### Architecture Perspective

Load testing strategy connects NFRs to release confidence — architects define thresholds, not just ops.

### Follow-up Questions

1. **Synthetic prod monitoring? — Small constant k6 run against canary post-deploy catches regression.**
2. **When skip stress test? — Never for Tier-0; acceptable for internal tools with documented risk.**

### Common Mistakes in Interviews

- Load test only localhost dev machine
- Health-check endpoint only — misses real user journey latency
- No CI integration — load test run manually once before launch

---

## Q005: Performance Budgets Definition

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Performance |
| **Frequency** | Very Common |

### Question

What are performance budgets and how do architects define them for web applications?

### Short Answer (30 seconds)

Performance budgets are measurable limits on latency, bundle size, and resource consumption — e.g., p95 API <300ms, JS bundle <200KB, LCP <2.5s. Defined per user journey, enforced in CI, and owned by product + engineering — not optional nice-to-haves.

### Detailed Answer (3–5 minutes)

**Budget categories:**
| Layer | Example budget | Enforcement |
|-------|----------------|-------------|
| Frontend | LCP <2.5s, JS <200KB gzipped | Lighthouse CI, bundle analyzer |
| API | Checkout p95 <300ms | k6 thresholds in pipeline |
| Database | Query p95 <50ms | APM + slow query alerts |
| Third-party | Payment SDK <500ms | Synthetic monitoring |

**Definition process:**
1. Identify critical user journeys (checkout, search, login)
2. Set budgets from NFR matrix and UX research (53% abandon >3s load)
3. Allocate budget across layers — BFF 100ms, DB 50ms, network 50ms = 200ms headroom
4. Add CI gates — PR fails if bundle grows >5% without approval

**Architect:** Performance budget ADR documents trade-offs — 'rich personalization costs 80KB JS; accepted with lazy load.'

**Regression response:** Budget breach blocks deploy or triggers optimization sprint — same rigor as security CVE.

### Architecture Perspective

Performance budgets make NFRs enforceable — architects define them before optimization debates start.

### Follow-up Questions

1. **Budget per journey vs global? — Per journey — homepage and checkout have different tolerance.**
2. **Mobile vs desktop budgets? — Separate budgets — mobile networks need stricter targets.**

### Common Mistakes in Interviews

- Budgets defined but never enforced in CI
- Single global latency number for all APIs
- Frontend bundle grows unbounded — no analyzer in pipeline

---

## Q006: FinOps Framework

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q007: Cost Allocation Tags

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q008: Reserved Instances Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q009: Spot and Preemptible Workloads

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q010: DR Tier 0–3

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q011: RTO and RPO Tradeoffs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q012: Backup vs Replication

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q013: Azure Site Recovery

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q014: Chaos Engineering

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q015: Load Testing with k6

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q016: Performance Budgets

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q017: Latency SLO

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q018: Capacity Planning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q019: Right-Sizing Reviews

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q020: Idle Resource Cleanup

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q021: Multi-Region DR Cost

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q022: DR Drill Frequency

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q023: Performance Regression in CI

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q024: Flame Graphs for Performance

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q025: Database Performance Baseline

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q026: CDN Cost Optimization

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q027: Autoscale Cost Traps

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q028: FinOps Team Structure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q029: Unit Economics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q030: Cost Anomaly Response

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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
