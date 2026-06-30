# Week 42 — Expert Scenario Q&A

> Q101–Q120: Premium format (Week 1 quality).

---


## Q101: Runaway Cloud Bill Overnight

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

At 7 AM, finance reports cloud spend spiked 4x overnight due to autoscaling and cross-region traffic. Product traffic is only up 20%. You lead architecture response. What are your first 48-hour actions?

### Short Answer (30 seconds)

Stabilize spend safely, isolate root cause, and implement temporary guardrails before deeper redesign.

### Detailed Answer

**First 6 hours:** freeze non-critical scale policies, apply spend guardrails, validate customer impact.

**Day 1:** trace anomaly by service/region/data flow; identify trigger (misconfigured autoscale, retry storm, data replication loop).

**Day 2:** deploy mitigations, publish incident review, and define architecture changes with owners.

### Architecture Perspective

In crisis, balance cost containment with reliability protection; avoid blunt shutdowns.

### Follow-up Questions

1. **How communicate to executives? -> Hourly status with spend trend, customer impact, and mitigation confidence.**
2. **What post-incident artifact? -> FinOps/architecture ADR and preventive controls checklist.**

### Common Mistakes in Interviews

- Immediate blanket scale-down causing outages
- Assuming cost spike equals external attack without data
- No follow-up governance changes after mitigation

---

## Q102: DR Failover Missed RTO

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

A regional outage occurs; failover succeeds technically but business transactions resume after 7 hours against 2-hour RTO. Leadership asks why DR 'worked' but still failed. How do you explain and fix?

### Short Answer (30 seconds)

Differentiate infrastructure recovery from business capability recovery and redesign recovery workflow.

### Detailed Answer

Postmortem should map timeline across infra, data, identity, dependencies, and operational decisions.

Identify critical path delays and update recovery plans, automation, and runbooks.

Set capability-level drill objectives, not infrastructure-only checks.

### Architecture Perspective

RTO commitments are about user outcomes, not resource status.

### Follow-up Questions

1. **How prevent recurrence? -> Capability-centric drills with measured checkpoints.**
2. **Who owns action plan? -> Joint ownership across platform, app teams, and incident command.**

### Common Mistakes in Interviews

- Calling event a success because VMs were up
- No dependency sequencing in recovery plan
- No governance accountability for missed contractual RTO

---

## Q103: Reserved Commitment Backfire

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

FinOps pushed aggressive 3-year commitments. Six months later product architecture changed and utilization dropped sharply. CFO blames engineering. How do you resolve and redesign process?

### Short Answer (30 seconds)

Create shared accountability model and restructure commitment governance with scenario planning.

### Detailed Answer

Quantify stranded commitment exposure and near-term mitigation options.

Establish commitment approval requiring architecture roadmap inputs and downside scenarios.

Adopt laddered commitments and periodic rebalance checkpoints.

### Architecture Perspective

Commitments are cross-functional bets; blame games hide process design flaws.

### Follow-up Questions

1. **How communicate to CFO? -> Recovery plan plus governance controls to prevent repeat losses.**
2. **How restore trust with engineering? -> Include architecture sign-off in future commitment decisions.**

### Common Mistakes in Interviews

- Treating commitments as finance-only procurement action
- No architecture roadmap input into purchase
- No downside-case modeling

---

## Q104: Latency SLO Burn Crisis

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Your p99 latency SLO has burned 60% of budget in 5 days after a major release. Product wants to continue rollout. SRE wants immediate freeze. What decision framework do you use?

### Short Answer (30 seconds)

Apply pre-agreed error-budget policy with staged rollout controls and risk-based exception path.

### Detailed Answer

Use burn-rate thresholds to determine policy action.

If threshold exceeded, pause broad rollout, retain limited canary, and prioritize remediation.

Any exception requires explicit business risk acceptance and timeframe.

### Architecture Perspective

Crisis decisions should follow policy to avoid ad hoc conflict.

### Follow-up Questions

1. **What data matters most? -> User-impact slices, not aggregate latency alone.**
2. **How avoid future conflict? -> Align release policy and SLO governance before launches.**

### Common Mistakes in Interviews

- Continuing rollout on hope
- Full freeze without impact analysis
- No documented exception mechanism

---

## Q105: ASR Drill Reveals Data Gaps

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Uncommon |
| **Type** | Scenario |

### Question

During a planned ASR drill, failover works but restored order data is inconsistent across services. Business confidence drops. What architecture response do you lead?

### Short Answer (30 seconds)

Treat as data recovery architecture issue: consistency model, reconciliation workflows, and runbook redesign.

### Detailed Answer

Map write paths and replication guarantees per datastore.

Define authoritative records and reconciliation procedures.

Update DR design with integrity checkpoints and application-level recovery sequencing.

### Architecture Perspective

DR credibility depends on data correctness, not just uptime.

### Follow-up Questions

1. **Who validates corrected design? -> Data platform, app owners, and business process stakeholders.**
2. **How communicate impact? -> Explain integrity risk plainly and staged remediation timeline.**

### Common Mistakes in Interviews

- Declaring drill passed due to infra metrics
- No reconciliation strategy for distributed state
- Ignoring business data validation in drills

---

## Q106: Chaos Test Triggers Incident

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

A chaos experiment unexpectedly degrades customer traffic and leadership questions the entire resilience program. How do you recover credibility?

### Short Answer (30 seconds)

Run transparent incident review, tighten experiment governance, and restart with safer maturity model.

### Detailed Answer

Acknowledge control gaps and publish corrective actions (blast-radius rules, approval tiers, abort automation).

Link future experiments to explicit hypotheses and customer-protection controls.

Demonstrate value via low-risk high-signal experiments first.

### Architecture Perspective

Program trust is restored through accountability and visible governance improvements.

### Follow-up Questions

1. **Should chaos pause entirely? -> Pause high-risk experiments, continue safe controlled validations.**
2. **How reassure product teams? -> Share guardrail framework and experiment calendar.**

### Common Mistakes in Interviews

- Defending incident as acceptable collateral damage
- Restarting chaos without governance changes
- No customer impact thresholds for experiment abort

---

## Q107: Capacity Forecast Misses Launch

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

A product launch drives 3x expected traffic; autoscaling lags and user latency spikes. Finance rejects permanent overprovisioning. What architecture and FinOps plan do you propose?

### Short Answer (30 seconds)

Implement surge-aware capacity strategy with forecast improvements and temporary cost controls.

### Detailed Answer

Create launch surge playbook: pre-warm critical tiers, predictive scaling signals, and dependency capacity checks.

Use temporary spend authorization window with clear rollback.

Update forecasting model with product funnel and marketing pipeline inputs.

### Architecture Perspective

Coordinating product, capacity, and cost decisions is core architecture leadership.

### Follow-up Questions

1. **How prevent repeated misses? -> Add launch readiness gates with capacity sign-off.**
2. **How keep cost in check? -> Time-bound surge allocations and post-launch right-sizing.**

### Common Mistakes in Interviews

- Permanent overprovisioning as only answer
- No launch-specific scaling preparation
- No dependency-level readiness checks

---

## Q108: Multi-Region Costs Out of Control

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Your active-active deployment meets reliability goals but inter-region data transfer costs now exceed compute costs. Business wants 30% reduction without reducing availability targets. What do you change?

### Short Answer (30 seconds)

Re-architect data flows for locality and selective replication while preserving failover capability.

### Detailed Answer

Identify hot data paths and shift to region-local processing.

Replicate only required state classes, compress telemetry, and convert chatty sync calls to async/event patterns.

Validate new design against failover and latency SLOs.

### Architecture Perspective

Availability architecture must include data movement economics.

### Follow-up Questions

1. **How prove no reliability regression? -> Simulate failover with new replication policies.**
2. **Who approves replication reductions? -> Architecture, reliability, and compliance stakeholders.**

### Common Mistakes in Interviews

- Blindly reducing replication everywhere
- No classification of critical vs non-critical data
- No failover validation after optimization

---

## Q109: Perf CI Gate Revolt

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Teams are bypassing performance regression CI gates because they are flaky and slow. Latency incidents are rising. How do you redesign the control model?

### Short Answer (30 seconds)

Introduce tiered, reliable perf gates with statistical thresholds and canary reinforcement.

### Detailed Answer

Separate fast PR smoke tests from deeper scheduled suites.

Stabilize environment and use variance-aware thresholds to reduce false positives.

Pair CI checks with release canary SLO monitoring to catch context-specific regressions.

### Architecture Perspective

Controls must be trustworthy to be adopted; otherwise teams route around them.

### Follow-up Questions

1. **How rebuild trust quickly? -> Publish gate reliability metrics and iterate with team feedback.**
2. **What policy for bypasses? -> Time-limited override plus mandatory follow-up verification.**

### Common Mistakes in Interviews

- Enforcing broken gates with no improvement plan
- Removing all gates due to developer complaints
- No visibility into gate false-positive rates

---

## Q110: Backup Restore Failure During Incident

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

A ransomware event forces restore, but backup images are incomplete for one critical service. What architecture governance changes do you implement after containment?

### Short Answer (30 seconds)

Shift from backup existence checks to restore-readiness governance with evidence.

### Detailed Answer

Mandate periodic restore validation across critical services.

Add backup integrity checks, immutable storage strategy, and dependency-aware restoration runbooks.

Tie recovery readiness to executive risk reporting.

### Architecture Perspective

Backup strategy is only real when restore outcomes are proven.

### Follow-up Questions

1. **How prioritize remediation? -> Critical services first based on business continuity impact.**
2. **How ensure sustained compliance? -> Automated controls plus drill evidence audits.**

### Common Mistakes in Interviews

- Assuming successful backup jobs mean recoverability
- No service-level restore accountability
- No immutable backup controls for ransomware threat

---

## Q111: FinOps Team Lacks Authority

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Uncommon |
| **Type** | Scenario |

### Question

Your new FinOps team can report cost waste but cannot influence architecture decisions. Savings plateau. What operating model change do you recommend?

### Short Answer (30 seconds)

Embed FinOps in architecture governance and roadmap decisions with defined decision rights.

### Detailed Answer

Give FinOps formal role in design reviews, commitment approvals, and quarterly planning.

Create domain cost champions with optimization OKRs.

Tie savings opportunities to product and engineering accountability structures.

### Architecture Perspective

Influence requires governance integration, not better dashboards alone.

### Follow-up Questions

1. **How avoid perceived policing? -> Frame FinOps as enablement with shared value targets.**
2. **What initial KPI? -> Actioned recommendations rate and unit cost trend.**

### Common Mistakes in Interviews

- Reporting-only FinOps function
- No engineering ownership for cost outcomes
- No formal governance seat for FinOps

---

## Q112: DR Contract Penalty Threat

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

A key customer contract has strict downtime penalties. Recent drills show your architecture cannot meet commitments consistently. Sales asks to keep contract language unchanged. What is your response?

### Short Answer (30 seconds)

Escalate contract-risk mismatch and define either architecture uplift plan or renegotiated terms.

### Detailed Answer

Present evidence of current capability versus contractual obligation.

Offer phased reliability uplift with funded milestones and interim controls.

If timeline infeasible, recommend commercial renegotiation to avoid unmanaged liability.

### Architecture Perspective

Architecture leadership must surface commercial risk truth, not hide it.

### Follow-up Questions

1. **Who should decide final path? -> Executive leadership with legal, product, and architecture input.**
2. **How keep customer trust? -> Transparent roadmap and demonstrable progress checkpoints.**

### Common Mistakes in Interviews

- Quietly hoping commitments are never tested
- Engineering absorbs unbounded contractual risk silently
- No funded plan for target reliability

---

## Q113: Unit Economics Degrading Fast

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

User growth is strong, but cost per transaction has doubled in three months. Leadership fears scaling is becoming unprofitable. How do you run architecture triage?

### Short Answer (30 seconds)

Diagnose cost-per-unit drivers by architecture layer and prioritize high-leverage fixes.

### Detailed Answer

Break down unit cost into compute, storage, data transfer, and third-party dependencies.

Identify hotspots from inefficient data paths, over-resilience, or poor scaling behavior.

Launch focused remediation plan with measurable unit-cost targets.

### Architecture Perspective

Growth without efficiency can destroy business model; unit economics must be architecture signal.

### Follow-up Questions

1. **How fast to show results? -> Quick wins in 2-4 weeks plus longer structural changes roadmap.**
2. **How align teams? -> Shared unit-cost KPI per domain with governance review.**

### Common Mistakes in Interviews

- Looking only at total spend
- No attribution by workload/business path
- No target-driven remediation plan

---

## Q114: Global Outage Simulation Political Pushback

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Uncommon |
| **Type** | Scenario |

### Question

You propose full-region outage simulation, but business stakeholders reject it as too risky and disruptive. Regulators still expect resilience evidence. What compromise architecture strategy works?

### Short Answer (30 seconds)

Use progressive validation ladder: controlled partial tests, synthetic drills, and evidence-backed tabletop escalation.

### Detailed Answer

Start with isolated component failover and synthetic traffic validation.

Advance to limited-scope production simulations with strict guardrails.

Build regulator-ready evidence trail showing increasing confidence and remaining risk.

### Architecture Perspective

Resilience assurance can be staged without reckless full-blast tests.

### Follow-up Questions

1. **How avoid endless partial testing? -> Define maturity milestones and decision gates upfront.**
2. **What evidence matters to regulators? -> Achieved recovery metrics, governance controls, and remediation closure.**

### Common Mistakes in Interviews

- Canceling all meaningful drills due to fear
- Jumping directly to high-blast experiments
- No documented progression strategy

---

## Q115: Autoscale Cost Spiral in Event Storm

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

A retry storm from downstream failures causes autoscaling to explode cost while user success stays low. What architecture control plan do you implement?

### Short Answer (30 seconds)

Control retries, apply backpressure, and align scale signals to useful work completion.

### Detailed Answer

Introduce bounded retries with jitter and circuit breakers.

Scale on queue health and success throughput, not raw request volume.

Add load shedding and graceful degradation paths to protect core transactions.

### Architecture Perspective

Scaling failure traffic is expensive chaos; architecture must favor successful work.

### Follow-up Questions

1. **How prove fix effectiveness? -> Compare success rate, latency, and cost during controlled fault injection.**
2. **Who owns changes? -> Service owners with platform/SRE coordination.**

### Common Mistakes in Interviews

- Unbounded retries plus autoscale
- Scaling on incoming error traffic only
- No fault-mode performance testing

---

## Q116: Cost Allocation War Between Teams

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Shared platform costs are disputed by product teams; each claims unfair allocation and resists optimization actions. Delivery relationships are degrading. How do you fix it?

### Short Answer (30 seconds)

Define transparent allocation policy, independent governance, and appeal process with data.

### Detailed Answer

Document cost drivers and allocation formulas.

Publish showback dashboards with drill-down.

Create governance forum to resolve disputes and evolve model quarterly.

### Architecture Perspective

Fairness perception in allocation is as important as mathematical precision.

### Follow-up Questions

1. **How start when data quality is poor? -> Improve tagging first, then phase in refined allocation.**
2. **How prevent gaming behavior? -> Use stable policy windows and exception auditing.**

### Common Mistakes in Interviews

- Changing formulas ad hoc each month
- No dispute resolution mechanism
- Using opaque spreadsheet-only allocations

---

## Q117: Performance Budget Breach by New Feature

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

A strategic feature improves conversion but pushes checkout latency beyond budget. Product wants to keep it; SRE warns of long-term reliability impact. What architecture decision path do you use?

### Short Answer (30 seconds)

Quantify business gain versus reliability cost, then choose optimize-or-isolate plan with time-bound guardrails.

### Detailed Answer

Run impact analysis on conversion uplift, latency degradation, and infrastructure cost.

Option A: optimize implementation quickly.

Option B: isolate feature path with controlled exposure while remediation proceeds.

Record decision with explicit review date.

### Architecture Perspective

Senior architects arbitrate value-vs-reliability trade-offs transparently.

### Follow-up Questions

1. **Who signs off? -> Product and reliability leadership with architecture recommendation.**
2. **How prevent permanent 'temporary' breaches? -> Hard expiry and release gate conditions.**

### Common Mistakes in Interviews

- Ignoring budget breach because business metric improved
- Blocking feature without option analysis
- No revisit timeline for exception

---

## Q118: DR Governance in M&A Transition

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Uncommon |
| **Type** | Scenario |

### Question

During post-acquisition integration, two DR standards conflict and neither system can meet combined contractual SLAs today. What 90-day architecture governance plan do you execute?

### Short Answer (30 seconds)

Prioritize contractual risk, establish interim unified control baseline, then converge standards.

### Detailed Answer

Weeks 1-3: map SLA gaps and critical-path dependencies.

Weeks 4-8: implement interim controls and harmonized recovery runbooks.

Weeks 9-12: publish target-state DR ADRs and migration plan with accountable owners.

### Architecture Perspective

Integration DR work should sequence by legal and customer risk first.

### Follow-up Questions

1. **How report to leadership? -> Weekly risk burndown with achieved recovery evidence.**
2. **What if standards cannot converge quickly? -> Maintain controlled dual-standard with sunset timeline.**

### Common Mistakes in Interviews

- Immediate full standard migration under instability
- No interim control baseline
- No SLA-gap transparency to leadership

---

## Q119: FinOps Pushback on Reliability Spend

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

FinOps recommends cutting observability and redundancy spend to hit quarterly targets. SRE argues this will increase incident cost. You mediate. What is your architecture recommendation?

### Short Answer (30 seconds)

Use risk-adjusted cost model and trim low-value spend while protecting high-leverage reliability controls.

### Detailed Answer

Differentiate spend that prevents high-impact outages from low-signal tooling bloat.

Optimize telemetry cardinality/storage policies and right-size redundancy by tier.

Track incident cost and reliability trend after changes.

### Architecture Perspective

Not all reliability spend is equal; optimization should be precision, not blunt reduction.

### Follow-up Questions

1. **How settle disagreement? -> Shared model comparing savings vs expected risk cost.**
2. **What governance artifact? -> ADR capturing chosen cuts and protected controls.**

### Common Mistakes in Interviews

- Across-the-board reliability budget cuts
- Preserving all spend without value scrutiny
- No post-change risk monitoring

---

## Q120: Executive Demands Immediate Savings

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

CEO mandates 15% cloud savings in one quarter with no customer impact. Teams are already overloaded. What realistic architecture execution plan do you present?

### Short Answer (30 seconds)

Deliver phased savings: rapid low-risk actions first, then structural optimizations with dedicated capacity.

### Detailed Answer

Phase 1 (30 days): rightsizing, idle cleanup, commitment tuning, storage lifecycle fixes.

Phase 2 (60-90 days): query/data-path optimization, autoscale tuning, architecture refactors with highest unit-cost impact.

Protect reliability SLOs with explicit guardrails and monitoring.

### Architecture Perspective

Credible plans combine quick wins and sustainable structural change.

### Follow-up Questions

1. **How secure execution capacity? -> Create funded optimization sprint allocation with leadership backing.**
2. **How track impact? -> Weekly savings dashboard tied to service quality metrics.**

### Common Mistakes in Interviews

- Promiseing savings without execution bandwidth
- Cutting services blindly for quick numbers
- No guardrails on customer impact

---
