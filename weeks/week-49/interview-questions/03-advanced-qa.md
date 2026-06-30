# Week 49 — Advanced Q&A

> Q071–Q100: Premium format (Week 1 quality).

---


## Q071: API Gateway Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

45-min mock: design API gateway architecture for 200 partner integrations.

### Short Answer (30 seconds)

APIM/Kong front door: auth (OAuth, mTLS), rate limits, versioning, developer portal, analytics, WAF integration.

### Detailed Answer (3–5 minutes)

**Architecture:**
```
Partner → WAF → APIM → [Routing to internal services]
              ↓
        Developer Portal + OAuth
```

**Per partner:** Client ID, tier (gold/silver), rate limit, IP allowlist optional.

**Versioning:** `/v1/` path + 12-month deprecation policy.

**Observability:** Per-partner metrics, 429 tracking, latency SLO.

**Security:** mTLS for banks; JWT for SaaS partners; secrets in Key Vault.

**Scale:** APIM premium units multi-region; backend pool health probes.

### Architecture Perspective

API gateway mock is bread-and-butter architect interview — cover partner lifecycle.

### Follow-up Questions

1. **Gateway vs service mesh? — Gateway = north-south; mesh = east-west.**
2. **GraphQL at gateway? — Federation gateway pattern for BFF consolidation.**

### Common Mistakes in Interviews

- Single API key for all partners
- No versioning strategy
- Gateway does business logic — fat gateway anti-pattern

---

## Q072: Data Mesh Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

Whiteboard: apply data mesh principles to enterprise with 8 domain teams.

### Short Answer (30 seconds)

Domain-oriented data products, self-serve platform, federated governance. Not every team needs a lake — start with 2 pilot data products.

### Detailed Answer (3–5 minutes)

**Principles applied:**
1. **Domain ownership** — Checkout team owns `OrderCompleted` data product
2. **Data as product** — SLA, schema, SLO on freshness
3. **Self-serve platform** — Databricks/ADF templates, catalog in Purview
4. **Federated governance** — Global standards; domain implements

**Pilot:** Orders + Customer domains; publish to catalog with contracts.

**Anti-pattern:** Central data team owns all pipelines — that's a lake not mesh.

**Prerequisites:** Domain boundaries clear; platform team invests in tooling.

### Architecture Perspective

Data mesh mock tests federated thinking — avoid buzzword without product mindset.

### Follow-up Questions

1. **Mesh vs fabric? — Mesh = org pattern; Microsoft Fabric = product — don't conflate.**
2. **When not mesh? — Immature domains, no platform — central team first.**

### Common Mistakes in Interviews

- Rename data lake 'data mesh' without domain ownership
- No data product SLAs
- 8 domains day one without pilots

---

## Q073: Event Storming Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

Facilitate event storming session mock for new loyalty program domain.

### Short Answer (30 seconds)

Domain events orange, commands blue, aggregates yellow, policies lilac. Discover bounded contexts and integration events in 2-hour workshop.

### Detailed Answer (3–5 minutes)

**Flow:**
1. **Big picture** — `PointsEarned`, `RewardRedeemed`, `TierUpgraded`, `AccountMerged`
2. **Commands** — `EarnPoints`, `RedeemReward` → aggregate `LoyaltyAccount`
3. **Policies** — 'When TierUpgraded notify CRM'
4. **Bounded contexts** — Loyalty vs Payments vs Catalog — `OrderCompleted` integration event

**Outputs:** Context map, candidate microservices, event catalog for Kafka.

**Facilitation:** Domain expert + PM + engineers; timebox arguments.

**Follow-up:** ADR on context boundaries; spike on idempotent consumers.

### Architecture Perspective

Event storming mock shows collaborative discovery skill — not solo diagramming.

### Follow-up Questions

1. **Remote event storming? — Miro + video; shorter sessions 90 min.**
2. **Process manager vs event choreography? — Identify saga needs from policies.**

### Common Mistakes in Interviews

- Skip domain experts in session
- Events without aggregate ownership
- No output artifact after workshop

---

## Q074: Architecture Principles Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Draft and defend 8 architecture principles for 500-person engineering org.

### Short Answer (30 seconds)

Principles must be memorable, testable, and trade-off aware. Examples: API-first, security by design, prefer managed services, observable by default.

### Detailed Answer (3–5 minutes)

**Sample principles:**
1. **API-first** — Contracts before UI; OpenAPI in CI
2. **Security by design** — Threat model for tier-1 changes
3. **Managed over self-hosted** — Unless compliance blocks
4. **Observable by default** — Logs, metrics, traces on all services
5. **Stateless services** — Session externalized
6. **Backward compatible** — Version APIs; expand-contract migrations
7. **Data ownership** — One writer per aggregate
8. **Simplicity** — YAGNI; simplest architecture meeting NFRs

**Governance:** Architecture review checks principles; exceptions need ADR.

**Anti-principle:** 'Microservices everywhere' — context-dependent.

### Architecture Perspective

Principles mock tests leadership philosophy — defend trade-offs when principles conflict.

### Follow-up Questions

1. **Principle vs standard? — Principle guides; standard mandates (e.g., TLS 1.2+).**
2. **Exception process? — ADR with expiry — prevents shadow IT.**

### Common Mistakes in Interviews

- Poster principles never referenced in reviews
- Too many principles (>12)
- Untestable platitudes ('quality first')

---

## Q075: Board Presentation Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Mock board presentation: 3-year technology strategy for digital bank.

### Short Answer (30 seconds)

10 slides max: market context, strategic pillars, investment, risk, metrics. Board cares about risk, ROI, regulatory — not microservices.

### Detailed Answer (3–5 minutes)

**Agenda (20 min + Q&A):**
1. Market & regulatory context (open banking, DORA)
2. Strategic pillars: customer experience, resilience, cost efficiency
3. Architecture north star diagram (simplified)
4. Investment: $12M over 3 years — chart by pillar
5. Key risks & mitigations (cyber, vendor, talent)
6. Success metrics: NPS, uptime, cost/income ratio
7. Ask: Approve Phase 2 funding $4M

**Tone:** Confident, transparent on risks.

**Prep:** Anticipate audit committee questions on cyber and third-party risk.

### Architecture Perspective

Board mock is highest-stakes communication — risk and governance foreground.

### Follow-up Questions

1. **CTO vs architect presenter? — CTO leads; architect backs deep dives if asked.**
2. **Deep dive trap? — Offer appendix — don't drown board in detail.**

### Common Mistakes in Interviews

- Technical deep dive to non-technical board
- No risk slide
- Strategy without measurable outcomes

---

## Q076: SOC2 Control Mapping

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Map SOC2 Type II controls to architecture for a new customer data API in a compliance gap mock.

### Short Answer (30 seconds)

CC6 access, CC6.7 encryption, CC7 monitoring, CC8 change mgmt — gap per control, remediation owner, 90-day plan before audit.

### Detailed Answer (3–5 minutes)

**Gap table:**
| CC | Current | Gap | Remediation |
|----|---------|-----|-------------|
| CC6.1 | Partial RBAC | No ABAC for PII | Q2 IAM |
| CC6.7 | TLS | At-rest blob gaps | CMK enable |
| CC7.2 | Logs | No SIEM alerts | Sentinel rules |
| CC8.1 | Informal | No prod gate | GitOps policy |

**Evidence for auditor:** Diagrams, access reviews, pen test.

**Shared responsibility:** Azure vs your controls matrix documented.

### Architecture Perspective

Compliance gap mock bridges controls and architecture decisions.

### Follow-up Questions

1. **SOC2 vs ISO 27001? — Map once, certify twice if needed.**
2. **Continuous control monitoring? — Avoid audit surprise.**

### Common Mistakes in Interviews

- Checkbox security without architecture changes
- Gaps without owners and dates
- No shared responsibility matrix

---

## Q077: Payment DR Game Day

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Present tier-1 payment DR to risk committee — what must you include beyond topology?

### Short Answer (30 seconds)

RTO/RPO, failover automation, failback approval, last game day results, secrets replication gaps, cost vs outage model.

### Detailed Answer (3–5 minutes)

**Targets:** RTO 15 min, RPO 5 min.

**Topology:** Primary ↔ geo-replica; Traffic Manager health probes.

**Failover:** Auto DNS flip; manual failback approval.

**Testing:** Quarterly game day; last drill 94% — gap on secrets fixed.

**Cost:** 1.4× single region vs $50K/min outage model.

**Distinction:** Backup for corruption; DR for region loss.

### Architecture Perspective

DR mock must include test evidence — when did you last drill?

### Follow-up Questions

1. **Active-active payments? — Split-brain risk — active-passive often safer.**
2. **Runbook walkthrough? — Risk committee may ask step-by-step.**

### Common Mistakes in Interviews

- DR never tested
- RPO/RTO undefined
- Manual failover without runbook

---

## Q078: Flash Sale Triage

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Checkout p99 jumps 200ms → 3s during flash sale — walk through first 15 minutes.

### Short Answer (30 seconds)

Confirm scope, traces → DB pool exhaustion, mitigate cache/scale/shed load, comms every 15 min, root cause index + pool sizing.

### Detailed Answer (3–5 minutes)

**0–5 min:** Checkout only; PSP green; DB CPU 98%.

**5–15 min:** Traces show inventory SQL 2.8s; Hikari pool maxed.

**Mitigate:** Read cache TTL 30s; cautious pool increase; shed non-critical steps.

**Root cause:** Missing index + undersized pool.

**Comms:** Degraded status + ETA.

**Post:** Index, pool formula, load test before next sale.

### Architecture Perspective

Performance crisis mock tests measure-before-optimize discipline.

### Follow-up Questions

1. **Load shed vs scale? — Scale if capacity exists; shed if downstream saturated.**
2. **Blameless postmortem? — Mention after stabilization.**

### Common Mistakes in Interviews

- Restart everything without data
- Skip dependency graph
- No stakeholder comms

---

## Q079: Order API 10x Phases

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Evolution plan for order API 1K → 10K orders/sec — what changes at each phase?

### Short Answer (30 seconds)

1K→3K: vertical + replicas + cache. 3K→6K: async accept, pooling, autoscale. 6K→10K: shard by customerId, CQRS light, edge rate limits.

### Detailed Answer (3–5 minutes)

**Phases:**
- **1K→3K:** Redis catalog cache, read replicas
- **3K→6K:** Queue 202+webhook, connection pooling, stateless autoscale
- **6K→10K:** Sharding, read/write split, tenant rate limits

**Validation:** Staging load test at 12K; chaos on replica lag.

**Cost:** Linear until shard; step at 6K ops complexity.

### Architecture Perspective

10x mock rewards incremental narrative — not day-one over-engineering.

### Follow-up Questions

1. **When shard? — Writer DB >70% sustained before hard ceiling.**
2. **Global 10x? — Multi-region after single-region 10x proven.**

### Common Mistakes in Interviews

- Microservices day one for 1K RPS
- Skip load test validation
- Cache without invalidation

---

## Q080: Data Product SLAs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

Define data mesh data product SLAs in an 8-domain enterprise mock.

### Short Answer (30 seconds)

Owner domain, schema contract, freshness SLO, quality checks, catalog entry, consumer onboarding path — pilot 2 domains first.

### Detailed Answer (3–5 minutes)

**Data product card:**
- **Owner:** Checkout team
- **Dataset:** OrderCompleted events
- **SLO:** 99% events <5 min lag
- **Schema:** Versioned Avro/Protobuf
- **Quality:** Null rate <0.1%
- **Catalog:** Purview entry with sample queries

**Pilot:** Orders + Customer only.

**Anti-pattern:** Central team owns all pipelines — that's a lake.

### Architecture Perspective

Data mesh mock needs product mindset — SLAs not just lakes.

### Follow-up Questions

1. **Mesh vs Fabric? — Mesh = org pattern; Fabric = product.**
2. **When not mesh? — Immature domains — central team first.**

### Common Mistakes in Interviews

- Rename lake data mesh without ownership
- No data product SLAs
- 8 domains day one

---

## Q081: Board Cyber Slide

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

What must a board technology strategy deck include for a digital bank?

### Short Answer (30 seconds)

Market/regulatory context, strategic pillars, investment chart, top risks with mitigations, success metrics, explicit funding ask.

### Detailed Answer (3–5 minutes)

**10 slides max:**
1. Market (open banking, DORA)
2. Pillars: experience, resilience, efficiency
3. North star diagram (simple)
4. $12M/3yr by pillar
5. Cyber, vendor, talent risks
6. NPS, uptime, cost/income ratio
7. Ask: Phase 2 $4M

**Tone:** Confident, transparent risks.

**Prep:** Audit committee cyber and third-party questions.

### Architecture Perspective

Board mock foregrounds risk and governance — not microservices.

### Follow-up Questions

1. **CTO vs architect presenter? — CTO leads; architect backs deep dives.**
2. **Deep dive trap? — Appendix offer — don't drown board.**

### Common Mistakes in Interviews

- Technical deep dive to board
- No risk slide
- Strategy without metrics

---

## Q082: Multi-tenant Auth Deep Dive

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Deep dive multi-tenant auth in whiteboard mock — what must you cover in 10 minutes?

### Short Answer (30 seconds)

OIDC, tenant claim in JWT, no cross-tenant queries, super-admin break-glass with audit, per-tenant API keys optional for B2B.

### Detailed Answer (3–5 minutes)

**Flow:**
```
User → IdP → JWT(tenant_id, roles) → APIM validate → App RLS
```

**Rules:**
- Every query scoped by tenantId
- RLS policies in PostgreSQL
- Super-admin cross-tenant: break-glass + immutable audit
- B2B: optional per-tenant API keys + mTLS

**Test:** Negative test cross-tenant access in CI.

### Architecture Perspective

Auth deep dive is where multi-tenant mocks are won or lost.

### Follow-up Questions

1. **Tenant in cache keys? — Prefix all Redis keys with tenantId.**
2. **Tenant offboarding? — Crypto-shred or export then delete.**

### Common Mistakes in Interviews

- TenantId only in UI not DB
- Shared cache keys across tenants
- No cross-tenant negative tests

---

## Q083: Acquisition Event Sync

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Design event-driven sync for acquired OMS in integration mock.

### Short Answer (30 seconds)

Change data capture or domain events to integration hub, idempotent consumers, customer ID golden record, feature-flag cohort cutover.

### Detailed Answer (3–5 minutes)

**Pattern:**
```
Acquired OMS → CDC/Events → Hub → Your Order Service read model
```

**Identity:** `legacy_acme_id` mapping table.

**Phases:** Read-only mirror → dual write with compare → cutover per cohort.

**Idempotency:** EventId dedup store.

**Rollback:** Revert feature flag + replay from offset.

### Architecture Perspective

Event sync shows integration maturity beyond point-to-point REST.

### Follow-up Questions

1. **Ordering guarantees? — Partition by customerId for per-customer order.**
2. **Poison messages? — DLQ + alert + manual replay tool.**

### Common Mistakes in Interviews

- Synchronous poll acquired API for every read
- No idempotency on consumers
- Big-bang cutover without cohort flags

---

## Q084: Landing Zone Prerequisites

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

What landing zone prerequisites before first AKS migration wave?

### Short Answer (30 seconds)

Hub-spoke VNet, Entra workload identity, ACR, policy guardrails, Private Link to data, ExpressRoute, centralized logging.

### Detailed Answer (3–5 minutes)

**Checklist:**
- Hub-spoke networking + firewall
- Entra ID + workload identity
- ACR with retention policy
- Azure Policy: allowed regions, tags, no public storage
- Log Analytics + Defender
- Private Link to SQL/on-prem
- ExpressRoute or VPN validated

**Pilot gate:** Deploy hello-world with full guardrails before wave 1.

### Architecture Perspective

Landing zone before pilot prevents retrofitting security under pressure.

### Follow-up Questions

1. **Policy exceptions? — ADR with expiry — not permanent waivers.**
2. **Multi-subscription strategy? — Prod vs non-prod separation.**

### Common Mistakes in Interviews

- Migrate before identity standard exists
- No policy guardrails on subscriptions
- Public endpoints for internal APIs

---

## Q085: Risk Register Living Artifact

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

How keep architecture risk register alive after initial mock?

### Short Answer (30 seconds)

Biweekly guild review, link to ADRs, escalate red items with mitigation options, retire mitigated risks, version in Git.

### Detailed Answer (3–5 minutes)

**Cadence:**
- Biweekly arch guild — top 10 risks
- Steering monthly — red heat map
- Per release — new risks from threat model

**Integration:** Risk ID in ADR references.

**Retire:** When mitigation verified — don't infinite list.

**Version control:** `risks/register.md` in Git with history.

### Architecture Perspective

Living register beats one-time slide for governance maturity.

### Follow-up Questions

1. **Risk appetite statement? — Align scoring to org tolerance.**
2. **Issue log link? — Convert occurred risks to issues with RCA.**

### Common Mistakes in Interviews

- Register in slide deck only
- Never retire mitigated risks
- No link from ADRs to risks

---

## Q086: Exec Objection Handling

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

How handle 'why not buy SaaS?' objection in executive comms mock?

### Short Answer (30 seconds)

Acknowledge valid cases, compare TCO 3yr, customization/data control, integration cost, hybrid option, recommend with conditions.

### Detailed Answer (3–5 minutes)

**Response structure:**
1. Validate — SaaS right for commodity functions
2. Criteria — Custom workflows, data residency, integration depth
3. TCO — Build/maintain vs SaaS + integration tax
4. Hybrid — SaaS for CRM, custom for core IP
5. Recommend — With phased proof

**Avoid:** Dismissing SaaS dogmatically.

**Ask:** Pilot budget to validate assumption.

### Architecture Perspective

Objection handling shows business judgment not technology religion.

### Follow-up Questions

1. **Build trap? — Opportunity cost of engineering on commodity.**
2. **SaaS trap? — Integration and data egress costs hidden.**

### Common Mistakes in Interviews

- No TCO comparison prepared
- Dismiss SaaS without criteria
- Cannot articulate hybrid path

---

## Q087: Stakeholder Escalation Path

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

Design escalation path when stakeholders deadlock on migration priority.

### Short Answer (30 seconds)

Document options with cost/risk, align to OKRs, timebox decision, escalate to exec sponsor with recommendation — not opinion.

### Detailed Answer (3–5 minutes)

**Escalation pack:**
| Option | Cost | Risk | OKR fit |
|--------|------|------|--------|
| CRM first | $X | Low | Revenue |
| Inventory first | $Y | Medium | Ops |

**Process:** 2-week negotiation → steering with data → exec tie-break.

**Document:** Decision log + dissenting view.

**Relationship:** 1:1 with both VPs before group escalation.

### Architecture Perspective

Escalation with data preserves architect credibility.

### Follow-up Questions

1. **Pre-wire exec? — Share pack 48h before steering.**
2. **Revisit trigger? — ADR condition if wrong choice.**

### Common Mistakes in Interviews

- Pick favorite VP's priority
- Escalate without options matrix
- Surprise exec in public forum

---

## Q088: Custom Build TCO

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

Calculate 3-year TCO when build option wins in build vs buy mock.

### Short Answer (30 seconds)

Engineering headcount × loaded rate × months, maintenance 20%/yr, opportunity cost, infra, vs vendor license + integration.

### Detailed Answer (3–5 minutes)

**Build TCO example:**
- 8 engineers × 12 months × $150K loaded = $1.2M build
- Maintenance 2 FTE ongoing = $300K/yr
- 3yr total ≈ $2.1M

**Compare:** Vendor $400K/yr license + 2 FTE integration = $1.8M

**Opportunity cost:** 8 engineers not on product roadmap — state explicitly.

**Decision:** Buy unless strategic differentiator justifies premium.

### Architecture Perspective

Build TCO must include opportunity cost — CFO asks this.

### Follow-up Questions

1. **Maintenance tail? — Often underestimated in build cases.**
2. **Exit cost? — Custom code has higher switching cost.**

### Common Mistakes in Interviews

- Build cost = sprint estimate only
- Ignore ongoing maintenance FTE
- No opportunity cost stated

---

## Q089: Debt Quadrant Presentation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

Use debt quadrant in tech debt presentation mock — how structure?

### Short Answer (30 seconds)

Quick wins (high value, low effort) first; strategic (high/high) planned; thankless (low/low) defer; hard slog (low value, high effort) avoid.

### Detailed Answer (3–5 minutes)

**Quadrant examples:**
- **Quick win:** Centralize logging library
- **Strategic:** Extract payment service
- **Thankless:** Rename packages
- **Hard slog:** Rewrite working module for style

**Narrative:** 90-day plan mixes quick wins + one strategic.

**Metrics per item:** MTTR, deploy time, CVE count.

### Architecture Perspective

Quadrant visual helps execs grasp prioritization instantly.

### Follow-up Questions

1. **Strategic debt sequencing? — Don't do three strategic items parallel.**
2. **Stop-the-line? — Security quadrant items may preempt.**

### Common Mistakes in Interviews

- Random debt list unordered
- Only quick wins — no strategic
- No metrics per quadrant item

---

## Q090: Roadmap Dependency Chain

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

Show dependency chain in architecture roadmap mock — example chain?

### Short Answer (30 seconds)

Identity standardization → zero-trust → service mesh mTLS; observability → SLO-based autoscale → error budgets.

### Detailed Answer (3–5 minutes)

**Chains:**
```
Identity → Zero-trust → mTLS mesh
Observability → SLOs → Autoscale policies
Data catalog → Data mesh pilots → Federated governance
```

**Visual:** Gantt or dependency arrows on roadmap.

**Anti-pattern:** Parallel initiatives that secretly depend on identity not ready.

### Architecture Perspective

Dependency chains show you won't promise SLOs without observability first.

### Follow-up Questions

1. **Critical path? — Highlight blockers for business milestones.**
2. **Slack in chain? — Buffer for pilot learning.**

### Common Mistakes in Interviews

- Independent parallel tracks with hidden deps
- SLO initiative before metrics exist
- No critical path identified

---

## Q091: Observability Vendor TCO

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

Model observability vendor TCO at 500-service scale in evaluation mock.

### Short Answer (30 seconds)

Ingest GB/day × $/GB × 365 + seats + retention tiers + egress to SIEM.

### Detailed Answer (3–5 minutes)

**Model:**
- 2 TB/day ingest × $0.10/GB × 365 = $73K/yr ingest alone
- 50 power user seats × $40 = $24K/yr
- 13-month retention premium
- SIEM export egress

**Sensitivity:** ±40% ingest growth.

**Negotiate:** Ingest cap, committed use discount.

### Architecture Perspective

Observability TCO surprises at scale — model ingest honestly.

### Follow-up Questions

1. **OpenTelemetry portability? — Reduces switching cost.**
2. **Sampling strategy? — Head-based vs tail — cost vs debuggability.**

### Common Mistakes in Interviews

- Per-host pricing on 500 K8s pods
- Ignore log volume growth
- No sampling plan

---

## Q092: Platform Squad SLA Breach

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

Platform SLO breached — how present accountability in SLA mock follow-up?

### Short Answer (30 seconds)

Blameless RCA, error budget policy triggered, freeze non-critical changes, comms to squads, corrective actions with dates.

### Detailed Answer (3–5 minutes)

**Response:**
1. Acknowledge breach transparently
2. RCA — root cause not blame
3. Error budget policy — reliability sprint
4. Comms — status to all squads
5. Actions — SMART with owners
6. Review SLA targets if unrealistic

**Bilateral:** Squad misconfigurations excluded — evidence-based.

### Architecture Perspective

SLA breach response tests mature SRE partnership.

### Follow-up Questions

1. **Renegotiate SLO? — If target was never achievable — data-driven.**
2. **Penalty credits internal? — Optional gamification — careful culture.**

### Common Mistakes in Interviews

- Hide breach from squads
- Blame squad without evidence
- No corrective actions

---

## Q093: Stream-Aligned Reorg Plan

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

Present stream-aligned reorg plan alongside microservices split in Conway mock.

### Short Answer (30 seconds)

Phase 1 service owners, phase 2 team moves, phase 3 decommission old structure, executive sponsor, 6-month transition metrics.

### Detailed Answer (3–5 minutes)

**Phases:**
1. **0–3 mo:** Name service DRIs within current structure
2. **3–6 mo:** Form stream teams with migrated people
3. **6–12 mo:** Decommission layer-based team charters

**Metrics:** Lead time per stream, cross-team tickets down.

**Risk:** Talent loss — retention plan for reorg.

**Comms:** Weekly all-hands updates.

### Architecture Perspective

Reorg plan shows Conway awareness beyond diagram.

### Follow-up Questions

1. **Interim DRI model? — When reorg politically blocked.**
2. **Team topology book? — Reference Team Topologies credibly.**

### Common Mistakes in Interviews

- Reorg surprise announcement
- Services split without ownership
- No transition metrics

---

## Q094: Platform Adoption Metrics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

What adoption metrics support platform pitch in whiteboard mock?

### Short Answer (30 seconds)

Golden path usage %, deploy frequency delta, lead time, developer NPS, ticket volume to platform team.

### Detailed Answer (3–5 minutes)

**Dashboard:**
| Metric | Baseline | Target Q2 |
|--------|----------|----------|
| Golden path adoption | 12% | 50% |
| Deploy frequency | 2/wk | 8/wk |
| Lead time | 5 days | 1 day |
| Platform NPS | 32 | 50 |

**Pilot first:** Show delta from 2 pilot squads before scaling ask.

### Architecture Perspective

Adoption metrics prevent platform team building unused tooling.

### Follow-up Questions

1. **Forced adoption? — Required for new services only — phased.**
2. **NPS survey cadence? — Quarterly — act on feedback.**

### Common Mistakes in Interviews

- Build portal nobody uses
- No baseline before pitch
- Adoption not measured

---

## Q095: Compliance Remediation Timeline

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Present 90-day compliance remediation timeline in gap analysis mock.

### Short Answer (30 seconds)

Week 1–2 assessment, 3–6 quick wins (CMK, SIEM rules), 7–10 ABAC/IAM, 11–12 evidence pack for auditor.

### Detailed Answer (3–5 minutes)

**Timeline:**
| Week | Deliverable |
|------|-------------|
| 1–2 | Gap assessment sign-off |
| 3–4 | Encryption at-rest CMK |
| 5–6 | SIEM alert rules live |
| 7–8 | ABAC for PII paths |
| 9–10 | GitOps prod approval gate |
| 11–12 | Auditor evidence package |

**Owners:** Named per workstream.

**Risk buffer:** 2-week slip on IAM.

### Architecture Perspective

Remediation timeline shows execution not just gap list.

### Follow-up Questions

1. **Parallel tracks? — Security + app changes coordinated.**
2. **Auditor dry run? — Week 10 internal mock audit.**

### Common Mistakes in Interviews

- Gaps listed without timeline
- All remediation week 12
- No owners per workstream

---

## Q096: DR Failback Procedure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

Explain DR failback procedure in payment service DR mock.

### Short Answer (30 seconds)

Validate primary healthy, reverse replication caught up, manual approval, DNS flip, monitor 24hr, post-failback verification checklist.

### Detailed Answer (3–5 minutes)

**Failback steps:**
1. Confirm primary region health checks green
2. Replication lag < RPO threshold
3. Change advisory board approval
4. DNS/traffic manager flip to primary
5. 24hr enhanced monitoring
6. Verification: transaction sample compare

**Risk:** Split-brain — prevent dual-write during transition.

**Document:** Failback runbook separate from failover.

### Architecture Perspective

Failback often harder than failover — mention explicitly in DR mocks.

### Follow-up Questions

1. **Game day failback? — Test both directions annually.**
2. **Data reconciliation? — Sample financial transactions post-failback.**

### Common Mistakes in Interviews

- Failback assumed trivial
- Never tested failback
- Dual-write during transition

---

## Q097: Shard Key Selection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

How choose shard key for 10K orders/sec scale mock?

### Short Answer (30 seconds)

customerId hash — even distribution, colocate customer orders, avoid cross-shard transactions where possible.

### Detailed Answer (3–5 minutes)

**Options:**
| Key | Pros | Cons |
|-----|------|------|
| customerId | Even, locality | Hot customer risk |
| orderId | Even | Cross-customer queries hard |
| region | Data residency | Hot region |

**Mitigation hot shard:** Sub-shard or isolate VIP customers.

**Router:** Consistent hash ring or lookup service.

**Cross-shard:** Saga or avoid — design bounded transactions.

### Architecture Perspective

Shard key choice is core 10x mock deep dive.

### Follow-up Questions

1. **Resharding plan? — Virtual shards / logical shards for growth.**
2. **Cross-shard joins? — Denormalize or CQRS read models.**

### Common Mistakes in Interviews

- Shard by month only — hot latest month
- Cross-shard ACID transactions
- No hot shard mitigation

---

## Q098: Federated Governance Council

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

Design federated data governance for data mesh mock.

### Short Answer (30 seconds)

Central standards council sets policies; domain teams implement; quarterly compliance review; exception ADR process.

### Detailed Answer (3–5 minutes)

**Council:** Data architect, security, legal, domain reps.

**Standards:** Schema registry rules, PII tagging, retention minimums.

**Domain implements:** Quality checks, catalog metadata.

**Exceptions:** ADR with expiry for domain-specific needs.

**Review:** Quarterly scorecard per domain data product.

### Architecture Perspective

Federated governance distinguishes mesh from anarchy.

### Follow-up Questions

1. **Central team role? — Platform tooling not all pipelines.**
2. **Data contract enforcement? — CI breaks on breaking schema change.**

### Common Mistakes in Interviews

- No central standards at all
- Central team owns all data pipelines
- Exceptions without expiry

---

## Q099: Audit Committee Prep

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Occasional |

### Question

Prep architect for audit committee questions after board strategy mock.

### Short Answer (30 seconds)

Third-party risk, cyber controls, material system changes, incident history, regulatory mapping (DORA, SOC2).

### Detailed Answer (3–5 minutes)

**Likely questions:**
- Top 3 cyber risks and mitigations?
- Material vendor dependencies?
- Incidents last 12 months — lessons?
- How architecture supports DORA resilience?

**Materials:** 1-page appendix — not main deck.

**Tone:** Factual, no overclaim on controls.

**Escalate unknowns:** 'We'll follow up with CISO detail.'

### Architecture Perspective

Audit committee prep shows board-level communication depth.

### Follow-up Questions

1. **Materiality threshold? — Align with finance on what's board-relevant.**
2. **Third-party concentration? — Cloud + PSP dependency risks.**

### Common Mistakes in Interviews

- Wing audit questions
- Overstate control maturity
- No incident lessons prepared

---

## Q100: Whiteboard Time Management

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

How time-box a 45-minute whiteboard mock across clarify, design, deep dive, trade-offs?

### Short Answer (30 seconds)

5 min clarify, 10 min high-level, 20 min deep dive, 5 min trade-offs, 5 min buffer — narrate clock aloud.

### Detailed Answer (3–5 minutes)

**Template:**
```
0–5   Requirements + assumptions on board
5–15  L1/L2 diagram — narrate as you draw
15–35 Deep dive one path (auth, data, or scale)
35–40 Trade-off table
40–45 Questions + migration/next steps
```

**Tips:** Leave white space; don't erase — add revision box.

**If stuck:** State assumption and proceed — shows judgment.

### Architecture Perspective

Time management is scored in mocks — practice with timer.

### Follow-up Questions

1. **Interviewer redirect? — Adapt — don't cling to script.**
2. **Too shallow breadth? — Pick one deep dive — they choose which.**

### Common Mistakes in Interviews

- Draw 40 boxes in 5 minutes
- Skip clarification entirely
- No trade-off summary at end

---
