# Week 16 — Intermediate Q&A

> Q001–Q050: Premium format (Week 1 quality).  
> **Topic:** Azure Production Capstone | **Count:** 50

---


## Q001: Production Architecture Review Checklist

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Very Common |

### Question

Lead architecture review for Azure production SaaS — checklist?

### Short Answer (30 seconds)

WAF all pillars, threat model, HA/DR RPO/RTO, identity MI+CA, network hub-spoke+PE, observability SLOs, FinOps tags+budgets, IaC deployment, runbooks.

### Detailed Answer (3–5 minutes)

**Deliverable:** findings ranked Critical/High/Medium with owners and dates.

**Architect:** Review is collaborative — not gatekeeping without alternatives.

### Architecture Perspective

Review checklist is capstone synthesis.

### Follow-up Questions

1. **Sign-off criteria? — No Critical open, High has mitigation plan.**
2. **Re-review trigger? — Major design change or quarterly.**

### Common Mistakes in Interviews

- Checklist only security
- No documented findings
- Review without workload owners

---

## Q002: Multi-Region Production SLA Math

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reliability |
| **Frequency** | Very Common |

### Question

Calculate composite SLA for Front Door + App Service + SQL geo-replica.

### Short Answer (30 seconds)

Multiply independent SLAs: 99.99% × 99.95% × 99.99% ≈ 99.93%. Weakest link dominates — document dependency chain.

### Detailed Answer (3–5 minutes)

**Improve:** redundant paths, circuit breakers, graceful degradation when dependency down.

**Architect:** Don't promise 99.99% if chain multiplies to 99.9% without mitigation.

### Architecture Perspective

SLA math is executive-facing architect skill.

### Follow-up Questions

1. **Parallel vs series dependencies? — Series multiplies; parallel improves.**
2. **Error budget? — 99.9% = 43 min/month downtime budget.**

### Common Mistakes in Interviews

- Sum SLAs instead of multiply
- Ignore dependency chain
- 100% SLA promise

---

## Q003: DR Runbook Essentials

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DR |
| **Frequency** | Very Common |

### Question

DR runbook outline for Azure SQL failover group?

### Short Answer (30 seconds)

Detection (alerts), decision criteria (RTO threshold), failover execution (manual/auto), validation (synthetic tests), communication (status page), rollback criteria.

### Detailed Answer (3–5 minutes)

**Test:** game day quarterly — measure actual RTO/RPO.

**Architect:** Runbook in wiki + automated scripts where possible — not panic documentation.

### Architecture Perspective

DR without tested runbook is wishful thinking.

### Follow-up Questions

1. **Failback plan? — Reverse replication after primary healthy.**
2. **Data loss acceptance? — Document RPO business sign-off.**

### Common Mistakes in Interviews

- Runbook untested since creation
- No communication templates
- Failover without app connection string plan

---

## Q004: C4 Diagram for Azure Capstone

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Documentation |
| **Frequency** | Very Common |

### Question

What to include in C4 Container diagram for Azure capstone?

### Short Answer (30 seconds)

Users, SPA, APIM, microservices (App Service/AKS), Service Bus, SQL, Cosmos, Redis, Key Vault, Entra ID, App Insights, Front Door.

### Detailed Answer (3–5 minutes)

**Per container:** technology choice, responsibilities, sync/async links.

**Level 1 Context:** system boundary and external actors only.

### Architecture Perspective

C4 is architect documentation standard.

### Follow-up Questions

1. **Dynamic diagram? — Show request flow for checkout scenario.**
2. **Deployment diagram? — Map containers to Azure resources.**

### Common Mistakes in Interviews

- Deployment diagram only no C4
- Missing external systems
- No legend or technology labels

---

## Q005: ADR for Azure Service Choices

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Very Common |

### Question

Write ADR: App Service vs AKS for order API.

### Short Answer (30 seconds)

Context: team skill, scale, 3 services. Decision: App Service P1v3. Consequences: faster ops, less K8s portability. Rejected: AKS — ops overhead unjustified.

### Detailed Answer (3–5 minutes)

**ADR template:** status, date, deciders, context, decision, consequences, alternatives.

**Architect:** ADRs in git next to Bicep — living documents.

### Architecture Perspective

ADR quality demonstrates architect thinking.

### Follow-up Questions

1. **Supersede ADR when? — Trigger metrics hit — document revision.**
2. **Link ADR to cost estimate? — Strengthens business case.**

### Common Mistakes in Interviews

- Decision without alternatives section
- ADR never revisited
- Verbal decision only

---

## Q006: Security Controls Mapping

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Map WAF security pillar to controls in capstone?

### Short Answer (30 seconds)

Entra auth, CA MFA, Private Link SQL, Key Vault secrets, WAF OWASP, NSG segmentation, Defender enabled, audit logs to Sentinel.

### Detailed Answer (3–5 minutes)

**Traceability matrix:** SOC2 control → Azure implementation → evidence (policy assignment ID, screenshot, IaC reference).

### Architecture Perspective

Compliance mapping is enterprise architect work.

### Follow-up Questions

1. **Pen test before launch? — External validation of controls.**
2. **Threat model STRIDE? — Link threats to mitigations.**

### Common Mistakes in Interviews

- Controls list without implementation
- No evidence collection plan
- Security bolted on last week

---

## Q007: Cost Estimate Order of Magnitude

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

Estimate monthly Azure cost for capstone architecture?

### Short Answer (30 seconds)

Pricing calculator: App Service P1v3×2, SQL S3, Redis C1, Service Bus standard, Front Door, Log Analytics ingestion GB/day.

### Detailed Answer (3–5 minutes)

**Document assumptions:** DAU, requests/day, log volume, retention.

**Sensitivity:** 2x traffic = ~1.5x cost if autoscale — not linear.

### Architecture Perspective

Order-of-magnitude cost expected in capstone.

### Follow-up Questions

1. **Reserved instance savings? — Note 1-year RI option in estimate.**
2. **Dev vs prod cost split? — Separate subscriptions — show both.**

### Common Mistakes in Interviews

- No cost section in architecture
- Copy-paste calculator without assumptions
- Ignore Log Analytics cost

---

## Q008: Integration Architecture Synthesis

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Integration |
| **Frequency** | Common |

### Question

Show async flows in capstone e-commerce.

### Short Answer (30 seconds)

OrderPlaced → Service Bus topic → [Inventory, Notification, Analytics subscribers]. Outbox from order service. APIM sync for client-facing API.

### Detailed Answer (3–5 minutes)

**Sync path:** checkout API only. **Async:** everything post-confirm.

**Diagram:** numbered steps with failure compensation.

### Architecture Perspective

Integration synthesis ties week 15 to capstone.

### Follow-up Questions

1. **Event catalog? — List events, schema version, publisher, subscribers.**
2. **Correlation ID? — Propagate through Service Bus application properties.**

### Common Mistakes in Interviews

- All sync microservice calls
- No outbox on order write
- Missing DLQ strategy

---

## Q009: Operational Excellence Capstone

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Common |

### Question

Observability stack for capstone?

### Short Answer (30 seconds)

OpenTelemetry SDK → App Insights, Log Analytics workspace, workbooks dashboards, SLO alerts, action groups to on-call, runbooks linked in alerts.

### Detailed Answer (3–5 minutes)

**Golden signals:** latency, traffic, errors, saturation per service.

**Architect:** Same observability template for all services in platform.

### Architecture Perspective

Operability proves production readiness.

### Follow-up Questions

1. **Synthetic tests? — Availability tests from 3 regions.**
2. **Alert fatigue? — Actionable alerts only — SLO burn rate.**

### Common Mistakes in Interviews

- Logs only no distributed tracing
- Alerts to unused email
- No runbook links in alerts

---

## Q010: Capstone Presentation Defense

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Communication |
| **Frequency** | Very Common |

### Question

Defend capstone when interviewer challenges over-engineering.

### Short Answer (30 seconds)

Acknowledge trade-off, cite requirement (SLA, compliance, scale), offer phased simplification MVP vs target state, quantify cost/complexity of alternative.

### Detailed Answer (3–5 minutes)

**Structure:** 'You're right that X adds complexity. We accepted it because Y requirement. Phase 1 could defer Z until metric M hit.'

**Architect:** Intellectual honesty > defending every box.

### Architecture Perspective

Defense communication is interview skill.

### Follow-up Questions

1. **What would you cut for MVP? — Have answer ready — scope triage.**
2. **Metrics to validate design? — SLOs, cost per order, deploy frequency.**

### Common Mistakes in Interviews

- Defensive or dismissive tone
- Cannot simplify design when asked
- No phased roadmap

---

## Q011: Production Architecture Review

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Very Common |

### Question

Lead production architecture review for Azure SaaS — scope and deliverables?

### Short Answer (30 seconds)

Review WAF five pillars, threat model, data flows, HA/DR, identity, network, observability, FinOps, IaC maturity. Deliverable: ranked findings with owners, dates, and accepted risks.

### Detailed Answer (3–5 minutes)

**Process:** pre-read architecture docs → 2-hour session with app + platform + security → written report within 5 days.

**Architect:** Collaborative not gatekeeping — every Critical finding needs mitigation option or explicit risk acceptance by product owner.

### Architecture Perspective

Production review synthesizes entire architect curriculum.

### Follow-up Questions

1. **Review cadence? — Major release + annual prod health check.**
2. **Sign-off blockers? — Open Critical; High must have dated plan.**

### Common Mistakes in Interviews

- Checklist without workload context
- Verbal findings only no traceability
- Security-only lens ignoring cost and ops

---

## Q012: Multi-Region SLA Math

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reliability |
| **Frequency** | Very Common |

### Question

Calculate end-to-end SLA: Front Door 99.99%, App Service 99.95%, SQL geo 99.99%?

### Short Answer (30 seconds)

Series dependencies multiply: 0.9999 × 0.9995 × 0.9999 ≈ 99.93%. Parallel redundant paths improve composite — document weakest link.

### Detailed Answer (3–5 minutes)

**Presentation:** show math to executives; propose mitigation (cache, fallback read-only mode) if below target.

**Architect:** Don't contract SLA below calculated composite without architectural change.

### Architecture Perspective

SLA math is executive-facing architect deliverable.

### Follow-up Questions

1. **Independent vs dependent failures? — Model realistically — shared region outage hits all.**
2. **Error budget at 99.9%? — ~43 minutes downtime/month allowed.**

### Common Mistakes in Interviews

- Add SLAs instead of multiply
- Promise 99.99% without chain analysis
- Ignore third-party SaaS in chain

---

## Q013: DR Drill Execution

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DR |
| **Frequency** | Very Common |

### Question

Execute quarterly DR drill for Azure SQL failover group — steps?

### Short Answer (30 seconds)

Announce window → simulate primary failure → trigger failover → validate app connectivity synthetic tests → measure RTO → document gaps → failback in lower environment next sprint.

### Detailed Answer (3–5 minutes)

**Success criteria:** RTO < target, RPO within business tolerance, runbook steps complete without improvisation.

**Architect:** Rotate drill scenarios — region down, corruption, key compromise.

### Architecture Perspective

Untested DR is wishful thinking — drills prove RTO.

### Follow-up Questions

1. **Tabletop vs full drill? — Tabletop quarterly; full failover semi-annual.**
2. **Blast radius containment? — Drill in isolated subscription first.**

### Common Mistakes in Interviews

- DR plan never exercised
- Failover first time during real outage
- No failback procedure documented

---

## Q014: RTO RPO Validation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DR |
| **Frequency** | Very Common |

### Question

Business requires RPO 15 min, RTO 1 hour — validate Azure design delivers?

### Short Answer (30 seconds)

RPO: SQL geo-replica/async replication lag monitoring < 15m. RTO: automated failover group + runbook + App Service multi-instance warm secondary — drill measured time.

### Detailed Answer (3–5 minutes)

**Evidence:** drill logs, replication lag dashboards, written attestation for auditors.

**Architect:** RPO/RTO are business terms — map to technical controls and test results, not SKU names alone.

### Architecture Perspective

RTO/RPO validation closes gap between design and proof.

### Follow-up Questions

1. **RPO zero requirement? — Sync replication latency/cost trade-off — geographic limits.**
2. **RTO vs MTTR? — RTO business-facing; MTTR ops metric — align both.**

### Common Mistakes in Interviews

- Claim RPO 0 with async replication
- No lag monitoring on replica
- RTO estimate never measured in drill

---

## Q015: FinOps Production Budget

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Very Common |

### Question

Set production Azure budget with alerts and escalation?

### Short Answer (30 seconds)

Budget at subscription/MG scoped to prod; alerts 50/80/100/120% to FinOps + engineering lead; Cost Management action group; monthly review with tag-based chargeback.

### Detailed Answer (3–5 minutes)

**Architect:** Budget tied to unit economics ($/order) not just total — anomaly when unit cost spikes.

**Include:** Log Analytics ingestion, Service Bus ops, egress — hidden drivers.

### Architecture Perspective

Production FinOps is ongoing not launch-only.

### Follow-up Questions

1. **Budget vs reservation? — Budget alerts spend; RI/SP reduces rate — separate tracking.**
2. **Chargeback tags? — Required tags policy `CostCenter`, `Product`.**

### Common Mistakes in Interviews

- No budget on prod subscription
- Alert only at 100% — too late
- Untagged 30% spend unallocated

---

## Q016: Cost Anomaly Response

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

Production spend jumped 40% overnight — triage process?

### Short Answer (30 seconds)

Cost Management anomaly detection alert → identify resource/service spike in Cost Analysis → check recent deploys, autoscale runaway, Log Analytics ingestion, DDoS egress → contain (scale down, cap) → postmortem.

### Detailed Answer (3–5 minutes)

**Common culprits:** verbose logging, forgotten load test, misconfigured autoscale max, public blob egress abuse.

**Architect:** FinOps runbook parallel to incident runbook.

### Architecture Perspective

Cost incidents deserve same urgency as availability.

### Follow-up Questions

1. **Azure Advisor cost alerts? — Supplement anomaly detection.**
2. **Prevent recurrence? — Policy max SKUs; budget hard actions.**

### Common Mistakes in Interviews

- Ignore cost alert until month end
- No owner for cost anomalies
- Load test in prod without budget guardrails

---

## Q017: Incident Command in Production

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Very Common |

### Question

You are incident commander for Sev1 Azure outage — first 15 minutes?

### Short Answer (30 seconds)

Declare Sev1, open bridge, assign roles (IC, comms, ops, scribe), confirm customer impact, stop risky changes, gather timeline, engage Azure support if platform, 15-min status cadence.

### Detailed Answer (3–5 minutes)

**Azure-specific:** check Service Health, Resource Health, recent deployments, Front Door backend health.

**Architect:** IC coordinates — doesn't solo-debug. Single source of truth doc.

### Architecture Perspective

Incident command proves operational maturity.

### Follow-up Questions

1. **Sev1 vs Sev2? — Pre-defined severity matrix by revenue/users affected.**
2. **When engage Microsoft? — Platform SLA impact — support ticket priority.**

### Common Mistakes in Interviews

- Everyone debugs without coordination
- No scribe — lost timeline
- Deploy fix during unclear root cause

---

## Q018: Blameless Post-Incident Review

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Very Common |

### Question

Facilitate blameless PIR after prod outage — structure?

### Short Answer (30 seconds)

Timeline facts → impact metrics → root cause (5 whys) → contributing factors → action items (detect, prevent, mitigate) with owners — no individual blame.

### Detailed Answer (3–5 minutes)

**Output:** published internally, linked from ADR if architectural gap. Track action item closure in sprint.

**Architect:** System fixes over person fixes — missing runbook, bad alert, no canary.

### Architecture Perspective

PIR culture distinguishes senior organizations.

### Follow-up Questions

1. **PIR within 48 hours? — Fresh memory; before narrative solidifies wrong.**
2. **Customer-facing summary? — Separate comms doc without internal jargon.**

### Common Mistakes in Interviews

- Name engineer who caused outage
- PIR with no action items
- Same root cause third time no systemic fix

---

## Q019: SLO Error Budget Policy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reliability |
| **Frequency** | Very Common |

### Question

Define error budget policy when SLO burn exceeds 50% mid-month?

### Short Answer (30 seconds)

At 50% burn: freeze non-critical releases, focus reliability. At 100%: halt feature work until budget reset; exec notification. Burn rate alerts multi-window.

### Detailed Answer (3–5 minutes)

**SLO example:** 99.9% availability = 43m/month budget. **Tooling:** App Insights + alert on burn rate.

**Architect:** Error budget connects reliability to product velocity — engineering decision not ops alone.

### Architecture Perspective

SLO policy is modern production governance.

### Follow-up Questions

1. **SLI selection? — User-facing success rate latency tail not CPU.**
2. **Partial SLO? — Critical paths stricter SLO than admin UI.**

### Common Mistakes in Interviews

- SLO defined but no enforcement
- 100% availability target impossible
- Alert on mean only ignoring p99 latency SLO

---

## Q020: Canary Production Deploy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Deployment |
| **Frequency** | Very Common |

### Question

Canary deploy new order API on App Service with 5% traffic?

### Short Answer (30 seconds)

Front Door or APIM weighted routing 5% canary / 95% stable; compare error rate latency 30 min; auto-rollback on SLO breach; gradual 25/50/100.

### Detailed Answer (3–5 minutes)

**Metrics:** golden signals canary vs baseline; business KPI checkout success.

**Architect:** Canary needs representative traffic — feature flags for internal-only canary first if needed.

### Architecture Perspective

Canary reduces blast radius of bad deploys.

### Follow-up Questions

1. **App Service slot vs Front Door canary? — Slots swap binary; Front Door % gradual.**
2. **Automated rollback? — Pipeline gate on App Insights alert.**

### Common Mistakes in Interviews

- Big bang deploy Friday 4pm
- Canary without comparable traffic volume
- No rollback runbook

---

## Q021: Blue-Green App Service Production

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Deployment |
| **Frequency** | Very Common |

### Question

Blue-green deployment on App Service production with minimal downtime?

### Short Answer (30 seconds)

Production slot (blue) live; deploy to staging (green); warm-up `/health/ready`; slot swap with preview; validate; complete swap; keep previous slot for instant rollback swap back.

### Detailed Answer (3–5 minutes)

**Database:** backward-compatible schema only — expand-contract. **Sessions:** sticky issues — prefer stateless or shared Redis.

**Architect:** Auto-swap only after integration tests pass on staging slot.

### Architecture Perspective

Blue-green is App Service native strength.

### Follow-up Questions

1. **Swap with VIP? — Instant DNS swap within App Service plan.**
2. **Green never receives prod traffic before swap? — Use slot setting sticky for preview test.**

### Common Mistakes in Interviews

- Deploy directly to production slot
- Breaking DB migration with swap
- Delete old slot immediately after swap

---

## Q022: Feature Flags in Production

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Deployment |
| **Frequency** | Common |

### Question

Roll out risky checkout feature to 10% tenants with Azure App Configuration?

### Short Answer (30 seconds)

Feature flag `checkout-v2` with percentage filter + tenant allowlist; telemetry compares conversion; kill switch instant off without redeploy.

### Detailed Answer (3–5 minutes)

**Architect:** Flags for release control not long-term config — retire flags. Audit flag changes. Combine with canary routing.

### Architecture Perspective

Feature flags decouple deploy from release.

### Follow-up Questions

1. **App Configuration vs LaunchDarkly? — App Config native Azure; LD advanced targeting.**
2. **Flag debt? — Quarterly flag cleanup sprint.**

### Common Mistakes in Interviews

- Long-lived branch instead of flag
- No kill switch during holiday peak
- Flag change without audit trail

---

## Q023: Chaos Engineering on Azure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reliability |
| **Frequency** | Common |

### Question

Introduce chaos experiments safely in Azure production?

### Short Answer (30 seconds)

Start in staging prod-like; then controlled prod (business hours low traffic): kill one pod, simulate Service Bus lag, deny Key Vault access — hypothesize steady state, abort if SLO breach.

### Detailed Answer (3–5 minutes)

**Tools:** Azure Chaos Studio faults (VM, AKS, Network). **Governance:** game day approval, blast radius limits, automated stop.

**Architect:** Chaos proves resilience claims — not chaos monkey random in prod day one.

### Architecture Perspective

Chaos validates architecture under failure.

### Follow-up Questions

1. **First experiment? — Verify monitoring detects injected failure.**
2. **Frequency? — Monthly game day after maturity.**

### Common Mistakes in Interviews

- Chaos in prod without hypothesis
- No abort criteria during experiment
- Chaos before basic monitoring exists

---

## Q024: Load Test Production-Like

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Very Common |

### Question

Design load test mirroring production before Black Friday?

### Short Answer (30 seconds)

Azure Load Testing or JMeter against staging prod-parity environment; realistic mix, think time, auth; ramp to 2× peak; monitor App Insights, SQL DTU, Service Bus depth.

### Detailed Answer (3–5 minutes)

**Never** surprise prod unless dedicated load sub with isolation. **Architect:** Define pass criteria (p99 < 500ms, error < 0.1%) before test.

### Architecture Perspective

Load test validates capacity plans with evidence.

### Follow-up Questions

1. **Production synthetic load? — Only isolated scale test with approval.**
2. **Soak test duration? — 4-24h catches memory leaks.**

### Common Mistakes in Interviews

- Load test dev SKU expecting prod numbers
- No pass/fail criteria defined
- Ignore messaging tier in load model

---

## Q025: Capacity Planning Production

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Common |

### Question

Annual capacity review for Azure production estate?

### Short Answer (30 seconds)

Trend CPU, memory, DTU, queue depth, TU consumption 12 months; forecast growth; quota checks; reservation renewals; scale ceiling documentation per service.

### Detailed Answer (3–5 minutes)

**Deliverable:** capacity plan spreadsheet + quota increase requests 90 days before need.

**Architect:** Connect business growth forecast (users, orders) to infrastructure headroom.

### Architecture Perspective

Capacity planning prevents emergency scale failures.

### Follow-up Questions

1. **Azure quota limits? — Pre-request vCPU Service Bus TU before launch.**
2. **Headroom target? — 30-40% below max autoscale under peak.**

### Common Mistakes in Interviews

- Wait until throttling to plan
- No forecast from business growth
- Ignore messaging partition limits

---

## Q026: On-Call Runbook Quality

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Very Common |

### Question

Evaluate runbook quality for Service Bus DLQ alert?

### Short Answer (30 seconds)

Good runbook: symptom, severity, prerequisites, step-by-step diagnosis, rollback, escalation contact, last-tested date. Linked directly from alert.

### Detailed Answer (3–5 minutes)

**Quality bar:** new engineer resolves 80% incidents without tribal knowledge. **Review:** quarterly runbook drill.

**Architect:** Runbook lives in wiki/Git near IaC — version controlled.

### Architecture Perspective

Runbook quality defines on-call experience.

### Follow-up Questions

1. **Runbook vs playbook? — Runbook technical steps; playbook incident process.**
2. **Stale runbook? — Auto-ticket if last-tested > 6 months.**

### Common Mistakes in Interviews

- Alert says page someone
- Runbook references retired portal blades
- No escalation section

---

## Q027: Escalation Paths

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Common |

### Question

Define escalation path for unresolved Sev1 after 30 minutes?

### Short Answer (30 seconds)

L1 on-call → L2 platform engineer (15m) → engineering manager (30m) → director + Azure support Sev A (45m) → exec comms if customer-facing > 1h.

### Detailed Answer (3–5 minutes)

**Document:** phone tree, backup on-call, timezone coverage, vendor contacts (Microsoft, Datadog).

**Architect:** Escalation is pre-negotiated — not invented during outage.

### Architecture Perspective

Clear escalation prevents incident stagnation.

### Follow-up Questions

1. **Azure support severity? — Sev A for production down platform suspected.**
2. **Customer escalation parallel? — Support lead owns external while IC owns technical.**

### Common Mistakes in Interviews

- Single on-call no backup
- Escalation path unknown to team
- Wait 4 hours before manager engaged

---

## Q028: Customer Communication During Outage

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Very Common |

### Question

Draft customer communication approach for multi-tenant SaaS outage?

### Short Answer (30 seconds)

Status page update within 15m: impact scope, workaround if any, next update time. Post-resolution: summary, root cause high-level, prevention steps — no sensitive internals.

### Detailed Answer (3–5 minutes)

**Templates:** pre-written status.io/Azure status integration. **Roles:** comms lead separate from IC.

**Architect:** B2B SLA may mandate notification windows — contract drives timeline.

### Architecture Perspective

Customer comms is architect awareness for SaaS.

### Follow-up Questions

1. **When notify? — When customer-visible impact confirmed — not every internal blip.**
2. **Regulatory notification? — GDPR breach diff from availability outage.**

### Common Mistakes in Interviews

- Silence until outage over
- Blame Azure publicly without verification
- Share internal postmortem draft externally

---

## Q029: Regulatory Audit Production

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compliance |
| **Frequency** | Common |

### Question

Prepare Azure production environment for SOC 2 Type II audit?

### Short Answer (30 seconds)

Evidence: IAM access reviews, change management tickets, encryption configs, backup logs, vulnerability scans, incident PIRs, policy assignments, penetration test remediation.

### Detailed Answer (3–5 minutes)

**Architect:** Traceability matrix control → Azure implementation → evidence artifact location.

**Tools:** Microsoft Purview compliance manager, Defender for Cloud regulatory dashboard.

### Architecture Perspective

Audit readiness is continuous not scramble.

### Follow-up Questions

1. **Auditor Azure access? — Read-only scoped RBAC not Owner.**
2. **Gap remediation timeline? — Prioritize Critical before audit window.**

### Common Mistakes in Interviews

- Scramble evidence week before audit
- No change management for prod
- Controls documented but not implemented

---

## Q030: Pen Test Remediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Prioritize penetration test findings for production Azure workload?

### Short Answer (30 seconds)

Critical (exploit RCE/data breach) fix 7 days; High 30 days; Medium next quarter; Low backlog. Retest after Critical/High fix.

### Detailed Answer (3–5 minutes)

**Common findings:** misconfigured storage public, excessive RBAC, missing WAF rules, SQL injection in custom code.

**Architect:** Track in same system as prod defects — visible to leadership.

### Architecture Perspective

Pen test without remediation is theater.

### Follow-up Questions

1. **Azure penetration testing rules? — Notify Microsoft for certain services — follow policy.**
2. **Third-party vs internal? — External annual + internal continuous.**

### Common Mistakes in Interviews

- Ignore Medium findings forever
- No retest verification
- Findings in PDF only not ticketed

---

## Q031: Backup Restore Drill

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DR |
| **Frequency** | Very Common |

### Question

Validate Azure Backup restore quarterly — procedure?

### Short Answer (30 seconds)

Select random VM/SQL/file backup → restore to isolated network → verify data integrity app login → document RTO actual → delete restore resources.

### Detailed Answer (3–5 minutes)

**SQL:** point-in-time restore to alternate server. **Architect:** Immutable backup vault protects against ransomware.

### Architecture Perspective

Restore drill proves backup not just backup job success.

### Follow-up Questions

1. **Backup vault immutability? — Enable for prod vaults.**
2. **Cross-region backup? — GRS vault for regional disaster.**

### Common Mistakes in Interviews

- Backup succeeds restore never tested
- Restore over production database
- No isolated network for restore test

---

## Q032: Key Compromise Response

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Azure Storage account key leaked in GitHub — response?

### Short Answer (30 seconds)

Rotate keys immediately (regenerate key2 then key1), audit access logs for abuse, migrate to managed identity, enable Key Vault references, scan repos for secrets, incident PIR.

### Detailed Answer (3–5 minutes)

**Contain:** deny public access review; Defender alert. **Prevent:** GitHub secret scanning, no keys in appsettings in prod.

**Architect:** Eliminate long-lived keys — RBAC + MI default pattern.

### Architecture Perspective

Key compromise runbook is security architect must-know.

### Follow-up Questions

1. **Key Vault soft delete? — Protects against accidental/malicious delete during incident.**
2. **Customer impact communication? — If data exfil suspected — legal/comms engaged.**

### Common Mistakes in Interviews

- Only delete Git commit without rotation
- Shared key across environments
- No access log review after leak

---

## Q033: Certificate Expiry Monitoring

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Monitor TLS certificate expiry across App Service APIM Front Door?

### Short Answer (30 seconds)

Key Vault cert lifetime alerts 30/14/7 days; App Service managed cert auto-renew track failures; Azure Monitor metric alerts; external synthetic check TLS handshake.

### Detailed Answer (3–5 minutes)

**Architect:** Central inventory of all certs — custom domains easy to orphan. Automate renewal via ACME or Key Vault integration.

### Architecture Perspective

Cert expiry outages are preventable — embarrassing prod incidents.

### Follow-up Questions

1. **Managed cert failure? — Alert on renewal failed state.**
2. **Wildcard vs single? — Wildcard convenience vs blast radius if compromised.**

### Common Mistakes in Interviews

- Calendar reminder only no automation
- Expired cert takes down checkout silently undetected
- Manual cert install on 40 App Services

---

## Q034: Dependency Mapping CMDB

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Common |

### Question

Maintain service dependency map for Azure production CMDB?

### Short Answer (30 seconds)

Map: app → APIM → backends → SQL/Cosmos/Service Bus/Key Vault/third-party SaaS. Tag resources in Azure Resource Graph; link to Service Map/App Insights application map.

### Detailed Answer (3–5 minutes)

**Use:** impact analysis for changes and outages. **Architect:** Update on every architecture review — stale CMDB useless.

### Architecture Perspective

Dependency map accelerates incident triage.

### Follow-up Questions

1. **App Insights app map? — Auto-discovered if instrumentation consistent.**
2. **Third-party dependencies? — Include Stripe, SendGrid SLA in composite.**

### Common Mistakes in Interviews

- No dependency map during change review
- CMDB spreadsheet never updated
- Missing messaging dependencies in map

---

## Q035: Architecture Decision Log Production

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Very Common |

### Question

Maintain ADR log for production system — what belongs?

### Short Answer (30 seconds)

ADRs for significant prod decisions: database choice, messaging product, auth model, multi-region strategy. Status: proposed/accepted/deprecated/superseded with date and consequences.

### Detailed Answer (3–5 minutes)

**Location:** git `/docs/adr/` next to Bicep. **Review:** new ADR in PR template for architectural changes.

**Architect:** ADR explains why — diagram shows what.

### Architecture Perspective

Production ADRs prevent re-litigating settled decisions.

### Follow-up Questions

1. **ADR vs design doc? — ADR single decision; design doc full system.**
2. **Supersede example? — App Service → AKS when scale threshold hit.**

### Common Mistakes in Interviews

- Verbal decisions only
- ADR never updated when reversed
- No consequences section

---

## Q036: Technical Debt Budget

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

Allocate 20% sprint capacity to production technical debt — enforce how?

### Short Answer (30 seconds)

Platform roadmap includes debt epics: upgrade .NET, retire flags, fix DLQ root causes, IaC drift. Track debt ratio in quarterly review; block all-feature sprints after outage from debt.

### Detailed Answer (3–5 minutes)

**Architect:** Quantify debt impact — 'missing index costs $2K/month and 200ms p99'. Makes prioritization objective.

### Architecture Perspective

Debt budget prevents slow production rot.

### Follow-up Questions

1. **Debt register? — Shared backlog tagged `tech-debt` visible to product.**
2. **When defer debt? — Never entirely — minimum 10% even in crunch.**

### Common Mistakes in Interviews

- Zero debt sprints until emergency rewrite
- Debt invisible to product owner
- No link debt to incidents

---

## Q037: Platform Team SLA

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Organization |
| **Frequency** | Common |

### Question

Define internal SLA platform team provides app teams?

### Short Answer (30 seconds)

Examples: new subscription provisioned 2 business days; AKS cluster upgrade communicated 30 days ahead; break-fix P1 platform 1h response; golden path template updates monthly.

### Detailed Answer (3–5 minutes)

**Measure:** ticket metrics, deployment frequency of platform modules.

**Architect:** Platform SLA enables-label enables app team planning — not ad hoc Slack requests.

### Architecture Perspective

Platform SLAs professionalize internal cloud enablement.

### Follow-up Questions

1. **X-as-a-service maturity? — Platform evolves from ticket to self-service portal.**
2. **SLA breach escalation? — App team VP to platform lead.**

### Common Mistakes in Interviews

- Platform team no published SLA
- Unlimited custom requests no queue
- Breaking change without notice window

---

## Q038: App Team Autonomy Guardrails

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

Balance app team autonomy with Azure guardrails?

### Short Answer (30 seconds)

Autonomy: choose app architecture within approved services; deploy via pipeline. Guardrails: Azure Policy deny public IP, required tags, allowed SKUs, network hub-spoke, security baseline.

### Detailed Answer (3–5 minutes)

**Exception process:** RFC to architecture board with time-bound exemption.

**Architect:** Guardrails enable speed — teams don't fear breaking prod security.

### Architecture Perspective

Autonomy + guardrails is enterprise platform pattern.

### Follow-up Questions

1. **Policy vs RBAC? — Policy restricts resource config; RBAC who can deploy.**
2. **Self-service subscription vending? — Automated with policy inheritance.**

### Common Mistakes in Interviews

- Central team approves every deploy
- No guardrails full Owner on prod sub
- Guardrails without exception path

---

## Q039: Golden Path Templates

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Platform |
| **Frequency** | Very Common |

### Question

Ship golden path Bicep template for standard .NET API on Azure?

### Short Answer (30 seconds)

Template: App Service P1v3 + MI + Key Vault + App Insights + Service Bus queue + SQL private endpoint + CI/CD pipeline stub + monitoring dashboard + runbook links.

### Detailed Answer (3–5 minutes)

**Documentation:** 'happy path' README — deviations need ADR. **Version:** semver template releases.

**Architect:** Golden path covers 80% teams — not every edge case.

### Architecture Perspective

Golden paths scale architect standards.

### Follow-up Questions

1. **Template vs module library? — Composable modules; golden path opinionated bundle.**
2. **Adoption metric? — % new apps from template vs snowflake.**

### Common Mistakes in Interviews

- Every team custom architecture snowflake
- Template outdated .NET 6 in 2026
- Golden path without security defaults

---

## Q040: Production Readiness Checklist

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Very Common |

### Question

Production readiness review (PRR) checklist before go-live?

### Short Answer (30 seconds)

HA validated, DR drill scheduled, monitoring/alerting complete, runbooks written, security scan passed, load test passed, FinOps budget set, on-call rotation staffed, rollback tested, docs updated.

### Detailed Answer (3–5 minutes)

**Gate:** no go-live with open Critical PRR items. **Sign-off:** engineering + ops + security + product.

**Architect:** PRR is quality gate — not checkbox theater if items verified.

### Architecture Perspective

PRR prevents preventable launch disasters.

### Follow-up Questions

1. **PRR vs go/no-go? — PRR input to business go/no-go meeting.**
2. **Hypercare planned? — Extended support post-launch in checklist.**

### Common Mistakes in Interviews

- Go-live without load test
- Monitoring added after launch
- PRR signed without evidence

---

## Q041: Go-Live Criteria

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Very Common |

### Question

Define objective go-live criteria for Azure platform migration?

### Short Answer (30 seconds)

Cutover when: parallel run 2 weeks <0.1% variance, rollback tested <30m, all integrations verified, training complete, support staffed, exec sign-off, maintenance window communicated.

### Detailed Answer (3–5 minutes)

**Rollback trigger:** error rate 2× baseline within 2h post-cutover.

**Architect:** Criteria documented before project starts — prevents moving goalposts.

### Architecture Perspective

Go-live criteria align business and technical readiness.

### Follow-up Questions

1. **Big bang vs phased? — Phased lower risk — criteria per phase.**
2. **Data validation? — Reconciliation counts financial parity.**

### Common Mistakes in Interviews

- Go-live on hope
- Rollback never tested
- Criteria changed day of cutover

---

## Q042: Hypercare Period

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Common |

### Question

Plan 2-week hypercare after major Azure production launch?

### Short Answer (30 seconds)

War room daily standup, extended on-call (24/7), senior engineers embedded, heightened monitoring dashboards, fast-track bug fixes, daily status to stakeholders, hypercare exit criteria defined.

### Detailed Answer (3–5 minutes)

**Exit:** error rate normal 7 days, no Sev1/2, runbooks handed to BAU ops.

**Architect:** Hypercare budgeted upfront — not volunteer overtime surprise.

### Architecture Perspective

Hypercare bridges launch to steady-state ops.

### Follow-up Questions

1. **Hypercare team composition? — Build team + ops + product analyst.**
2. **Deferred enhancements? — Log but don't destabilize during hypercare.**

### Common Mistakes in Interviews

- Launch Friday no hypercare
- Same on-call intensity forever post-launch
- No exit criteria from hypercare

---

## Q043: Handoff to Operations

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Very Common |

### Question

Hand off new Azure service from project team to BAU operations?

### Short Answer (30 seconds)

Deliver: runbooks, architecture diagrams, IaC repo access, monitoring dashboards, alert routing verified, on-call trained shadow shift, known issues list, SLAs documented, KT sessions recorded.

### Detailed Answer (3–5 minutes)

**Acceptance:** ops sign-off checklist — won't accept without runbooks.

**Architect:** Design for operability during build — not documentation scramble at end.

### Architecture Perspective

Clean handoff defines project success beyond go-live.

### Follow-up Questions

1. **Shadow on-call? — Project engineer pairs one week before solo.**
2. **Ops feedback loop? — Retro on handoff quality improve golden path.**

### Common Mistakes in Interviews

- Throw over wall Friday evening
- No ops in PRR
- Runbooks written by dev who never ops

---

## Q044: Monitoring Coverage Review

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Observability |
| **Frequency** | Very Common |

### Question

Audit monitoring coverage for production Azure app?

### Short Answer (30 seconds)

Checklist: golden signals all services, synthetic availability, dependency failures, business KPIs, Service Bus DLQ depth, SQL replica lag, cert expiry, quota usage — gaps prioritized.

### Detailed Answer (3–5 minutes)

**Tooling:** Azure Monitor workbook inventory; alert rules tagged `prod`.

**Architect:** Monitoring debt is technical debt — schedule quarterly coverage review.

### Architecture Perspective

Coverage review finds blind spots before customers do.

### Follow-up Questions

1. **Service Level Indicators? — Map each SLI to metric source.**
2. **Third-party SaaS monitoring? — Synthetic or webhook status integration.**

### Common Mistakes in Interviews

- Monitor VM CPU only
- No alert on dependency failure
- Business KPIs absent from dashboards

---

## Q045: Alert Fatigue Reduction

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Observability |
| **Frequency** | Very Common |

### Question

Reduce alert fatigue — 200 alerts/week down to actionable set?

### Short Answer (30 seconds)

Audit alerts: delete noisy, tune thresholds, composite alerts, SLO burn rate only pages, route info to ticket not page, dedupe, weekly alert review meeting.

### Detailed Answer (3–5 minutes)

**Principle:** page human only when immediate action required.

**Architect:** Every alert links runbook — if no runbook, maybe shouldn't alert.

### Architecture Perspective

Alert hygiene is operational excellence pillar.

### Follow-up Questions

1. **Action groups? — Separate email vs SMS vs PagerDuty severity.**
2. **Alert on missing data? — Critical metrics treat no-data as breach.**

### Common Mistakes in Interviews

- Page on CPU 60%
- 200 alerts nobody reads
- Same alert fires every 5 min all night

---

## Q046: Executive Dashboards

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Observability |
| **Frequency** | Common |

### Question

Build executive Azure dashboard for CTO — what metrics?

### Short Answer (30 seconds)

Availability SLO trend, error budget remaining, monthly Azure spend vs budget, deployment frequency, open Critical vulnerabilities, major incident count, customer-facing latency p95.

### Detailed Answer (3–5 minutes)

**Avoid:** raw CPU graphs — executives need business-aligned KPIs.

**Architect:** Workbook shared read-only; auto-refresh weekly email snapshot.

### Architecture Perspective

Executive dashboards translate ops to business language.

### Follow-up Questions

1. **Power BI vs Monitor workbook? — Power BI for cross-cloud finance merge.**
2. **Drill-down path? — Exec dashboard links to ops detail.**

### Common Mistakes in Interviews

- Executive dashboard 50 technical graphs
- No financial view
- Stale manual PowerPoint monthly

---

## Q047: Tenant Isolation Production SaaS

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Architecture |
| **Frequency** | Very Common |

### Question

Multi-tenant SaaS isolation strategies on Azure?

### Short Answer (30 seconds)

Pool: shared DB tenantId column + RLS. Silo: database per tenant Premium tier. Hybrid: pool default, silo enterprise. Network: separate subscriptions for largest tenants.

### Detailed Answer (3–5 minutes)

**Security:** always filter by tenantId in code + DB RLS defense in depth. **Compliance:** silo for data residency requirements.

**Architect:** Isolation model drives cost model — document in ADR.

### Architecture Perspective

Tenant isolation is SaaS architect core decision.

### Follow-up Questions

1. **Cosmos partition key tenantId? — Natural isolation boundary.**
2. **Cross-tenant leak test? — Automated security test in CI.**

### Common Mistakes in Interviews

- TenantId optional query filter
- Shared Key Vault secrets all tenants
- No isolation testing

---

## Q048: Multi-Tenant Noisy Neighbor

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Very Common |

### Question

Large tenant batch job degrades others — mitigation?

### Short Answer (30 seconds)

Rate limit per tenant APIM; separate Service Bus queue for bulk vs interactive; compute quota per tenant; autoscale dedicated workers for premium tier; circuit breaker on shared SQL pool DTU exhaustion.

### Detailed Answer (3–5 minutes)

**Detection:** per-tenant metrics dashboards; anomaly on one tenant CPU/queue depth.

**Architect:** Fair scheduling — premium tenants get silo or reserved capacity.

### Architecture Perspective

Noisy neighbor handling separates SaaS maturity levels.

### Follow-up Questions

1. **Elastic pool vs single DB? — Pool shares DTU — noisy neighbor risk.**
2. **Bulkhead pattern? — Separate thread pools/queues per tenant class.**

### Common Mistakes in Interviews

- Unlimited batch for any tenant
- No per-tenant rate limits
- Single shared queue all priorities

---

## Q049: Performance Baseline

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Common |

### Question

Establish production performance baseline post-launch?

### Short Answer (30 seconds)

Capture 30 days normal traffic: p50/p95/p99 latency per endpoint, SQL query durations, Service Bus processing time, error rates — store in workbook; alert when 2× baseline deviation.

### Detailed Answer (3–5 minutes)

**Use:** capacity planning, regression detection after releases.

**Architect:** Baseline during representative load — not holiday peak as normal.

### Architecture Perspective

Baseline enables meaningful regression alerts.

### Follow-up Questions

1. **Continuous baseline update? — Rolling 30-day window adapts seasonality.**
2. **Load test baseline vs prod? — Prod baseline authoritative; load test validates headroom.**

### Common Mistakes in Interviews

- No baseline alert on 3× latency
- Baseline from dev environment
- One-time baseline never updated

---

## Q050: Continuous Improvement WAF

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Process |
| **Frequency** | Very Common |

### Question

Institutionalize WAF continuous improvement for production?

### Short Answer (30 seconds)

Quarterly WAF assessment per workload pillar score 1-5; improvement backlog; link incidents to pillar gaps; Azure Advisor + WAF review; annual compare scores trend.

### Detailed Answer (3–5 minutes)

**Architect:** WAF not one-time launch review — living discipline tied to OKRs.

### Architecture Perspective

Continuous WAF closes architect learning loop.

### Follow-up Questions

1. **WAF assessment tool? — Microsoft WAF self-assessment checklist.**
2. **Pillar trade-off example? — Cost vs reliability reserved capacity decision.**

### Common Mistakes in Interviews

- WAF review once at launch only
- Scores without improvement plan
- Ignore Advisor recommendations systematically

---
