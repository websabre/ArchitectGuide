# Week 49 — Expert Scenario Q&A

> Q101–Q120: Premium format (Week 1 quality).

---


## Q101: Panel Multi-tenant Defense

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

45-min panel: defend shared-DB multi-tenant design to security architect skeptical of RLS.

### Short Answer (30 seconds)

Acknowledge risks, cite RLS policies, pen test results, tenant isolation tests in CI, enterprise silo upsell path, accepted residual with controls.

### Detailed Answer

**Defense structure:**
1. Validate concern — cross-tenant breach is catastrophic
2. Controls — RLS, app-layer checks, JWT scoping, audit
3. Evidence — pen test, negative CI tests, SOC2 CC6
4. Trade-off — ops cost vs silo at 5K tenants
5. Enterprise tier — physical isolation available
6. Residual — documented with review cadence

**Tone:** Collaboration not combat.

### Architecture Perspective

Panel defense is staff interview simulation for whiteboard topics.

### Follow-up Questions

1. **When insist silo? — HIPAA contract, performance SLO breach.**
2. **RLS bypass risk? — Super-admin break-glass audited.**

### Common Mistakes in Interviews

- Dismiss security concerns
- No test evidence for isolation
- Cannot articulate enterprise tier path

---

## Q102: Acquisition Big-Bang Challenge

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

CEO demands 90-day big-bang acquisition cutover — how respond in mock?

### Short Answer (30 seconds)

Present risk matrix: outage, data loss, rollback impossibility; offer phased strangler with 90-day read-only milestone; exec risk acceptance if override.

### Detailed Answer

**Response:**
1. Acknowledge urgency — validate business driver
2. Risk table — big-bang vs phased on outage, cost, rollback
3. Alternative — 90-day: identity + read sync live; write cutover month 6
4. If override — written risk acceptance, war room, rollback criteria

**Architect duty:** Document dissent; commit after decision.

### Architecture Perspective

Expert scenario tests courage with diplomacy under exec pressure.

### Follow-up Questions

1. **War room plan? — Joint command structure both companies.**
2. **Rollback criteria? — Feature flags per cohort mandatory.**

### Common Mistakes in Interviews

- Refuse without alternatives
- Capitulate without risk acceptance
- No rollback plan documented

---

## Q103: Migration Wave Failure Gate

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Wave 2 migration caused 4-hour outage — what gate criteria before wave 3?

### Short Answer (30 seconds)

Postmortem complete, runbook updated, dress rehearsal passed, rollback tested, steering approval, enhanced monitoring wave 3.

### Detailed Answer

**Gate checklist:**
- Blameless postmortem published
- Root cause fix verified (DNS, pool, firewall)
- Full dress rehearsal on wave 3 subset
- Rollback drill <30 min proven
- Steering sign-off
- 24hr war room for wave 3

**Architect leads:** Technical gate; exec owns go/no-go.

### Architecture Perspective

Wave failure gate shows program leadership maturity.

### Follow-up Questions

1. **Pause program? — Option if systemic not local failure.**
2. **Blame engineer? — Never — system fix focus.**

### Common Mistakes in Interviews

- Proceed wave 3 same runbook
- No dress rehearsal requirement
- Hide outage from steering

---

## Q104: Risk Heat Map Exec Translation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Translate 5×5 risk heat map for CFO in expert risk register scenario.

### Short Answer (30 seconds)

Dollarize top risks where possible, show mitigation spend vs exposure, residual risk after spend, insurance/regulatory context.

### Detailed Answer

**CFO translation:**
| Risk | Exposure | Mitigation cost | Residual |
|------|----------|-----------------|----------|
| PSP outage | $2M/yr revenue | $200K multi-PSP | $400K |
| Key breach | $10M+ regulatory | $150K HSM | Medium |

**Visual:** Top-right 3 risks only — not full 25-cell grid.

**Ask:** Approve $350K mitigation budget.

### Architecture Perspective

Expert comms translates heat map to money — CFO engagement.

### Follow-up Questions

1. **Insurance? — Cyber policy may affect residual acceptance.**
2. **Quantify low likelihood? — Use expected value honestly.**

### Common Mistakes in Interviews

- Show full grid without narrative
- No dollar exposure ranges
- Mitigation without cost

---

## Q105: Board Deep Dive Trap

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Board member asks 20-minute microservices deep dive — how handle?

### Short Answer (30 seconds)

Offer appendix or follow-up session with CTO; provide 2-minute plain-language answer; redirect to risk and investment slide; don't derail agenda.

### Detailed Answer

**Script:**
'That's important — I'll give a 2-minute version now and propose CTO and I brief the technology committee next week with depth you need.'

**2-min version:** Modernize for faster features and fewer outages — not technology for its own sake.

**After meeting:** Send 1-page appendix.

### Architecture Perspective

Board expert skill is boundary management on depth.

### Follow-up Questions

1. **Technology committee? — Standing body for deep dives.**
2. **Record follow-up? — Action item with owner and date.**

### Common Mistakes in Interviews

- 45-minute technical lecture to board
- Dismiss question as too basic
- No follow-up offered

---

## Q106: Enterprise Tenant Silo Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Design zero-downtime migration of enterprise tenant from shared RLS to dedicated silo.

### Short Answer (30 seconds)

Dual-write period, replication sync, DNS/connection string cutover, validation window, rollback to shared pool warm.

### Detailed Answer

**Steps:**
1. Provision dedicated DB/schema
2. Initial bulk copy + CDC sync
3. Dual-write both pools — compare counts
4. Read traffic shift to silo
5. Write cutover maintenance window (minutes)
6. Decommission shared rows after 30 days

**Customer comms:** Maintenance window SLA.

**Rollback:** Revert connection string to shared.

### Architecture Perspective

Silo migration expert scenario tests operational detail.

### Follow-up Questions

1. **Minimal downtime? — Sub-minute cutover with connection pool drain.**
2. **Contract SLA? — Enterprise tier promises documented.**

### Common Mistakes in Interviews

- Big-bang copy without CDC
- No validation compare period
- No rollback to shared

---

## Q107: Integration Hub Ownership

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Who owns integration hub in acquisition — debate platform vs integration squad?

### Short Answer (30 seconds)

Joint integration squad owns hub with sunset date; platform provides infrastructure patterns; acquired team embedded; executive mandate prevents orphan middleware.

### Detailed Answer

**Model:**
- **Squad:** Product owner from platform + leads from both companies
- **Sunset:** 12-month decommission acquired stack
- **Standards:** Event schema registry, idempotency, DLQ
- **Anti-pattern:** Neither team owns — integration spaghetti

**Escalation:** CTO resolves if turf war.

### Architecture Perspective

Hub ownership is political architecture — expert mocks probe this.

### Follow-up Questions

1. **iPaaS vs custom hub? — iPaaS faster; custom more control — ADR.**
2. **Knowledge transfer? — Acquired engineers on rotation 6 months.**

### Common Mistakes in Interviews

- Orphan middleware no owner
- Platform team ignores domain semantics
- No sunset date for acquired stack

---

## Q108: 6R Strategy Selection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Apply 6Rs to 200-service migration — assign strategy per service type in expert mock.

### Short Answer (30 seconds)

Rehost stateless, replatform containers, refactor tangled deps, retire unused, retain mainframe temporarily, repurchase SaaS where fit.

### Detailed Answer

**Assignment examples:**
| Service | 6R | Rationale |
|---------|-----|------------|
| Static web | Rehost | Low risk |
| Java monolith | Replatform | Container first |
| Reporting | Repurchase | Power BI vs custom |
| Cron orphan | Retire | Unused 2 years |
| Mainframe bridge | Retain | Wrap phase 2 |

**Portfolio view:** % by 6R for steering.

### Architecture Perspective

6R expert mock shows portfolio thinking not one strategy.

### Follow-up Questions

1. **Refactor in cloud? — After replatform stable.**
2. **Retire evidence? — Usage metrics prove unused.**

### Common Mistakes in Interviews

- Refactor everything before migrate
- Retain without wrap plan
- No retire candidates identified

---

## Q109: Vendor Lock-in ADR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Write vendor lock-in ADR for observability choice in expert evaluation mock.

### Short Answer (30 seconds)

Conscious lock-in acceptance, portable instrumentation (OTel), export APIs, contract exit terms, revisit trigger at renewal.

### Detailed Answer

**ADR sections:**
- Decision: Vendor X for 3 years
- Portable layer: OpenTelemetry SDK
- Exit: Export to S3, 90-day parallel run on alt
- Lock-in accepted: Dashboards, ML features
- Revisit: Renewal month 30

**Honest:** Some lock-in rational for velocity.

### Architecture Perspective

Conscious lock-in ADR is expert procurement maturity.

### Follow-up Questions

1. **Dual vendor? — Expensive — usually phased not parallel long-term.**
2. **Contract terms? — Data export, API access, notice period.**

### Common Mistakes in Interviews

- Deny any lock-in exists
- No portable instrumentation layer
- No revisit trigger at renewal

---

## Q110: Platform Build vs Buy Panel

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Panel challenges internal platform build — defend or concede with ADR?

### Short Answer (30 seconds)

Present adoption data, TCO vs vendor developer platform, opportunity cost, hybrid path; concede if data weak — credibility over ego.

### Detailed Answer

**Defense data:**
- 50% adoption, DORA improved 3×
- Vendor IDP TCO $800K/yr + less customization
- 6 FTE platform vs $800K — breakeven 18 mo

**If weak adoption:** Concede pivot — buy IDP, team focuses on golden path content.

**Expert signal:** Change mind with data.

### Architecture Perspective

Expert panel tests intellectual honesty not stubbornness.

### Follow-up Questions

1. **Backstage/Cortex? — Name alternatives evaluated.**
2. **Build trap duration? — 18-month review gate mandatory.**

### Common Mistakes in Interviews

- Defend build with zero adoption data
- Ignore vendor IDP alternatives
- Ego prevents pivot when data weak

---

## Q111: Regulatory Residency Conflict

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Whiteboard Mock |
| **Frequency** | Occasional |
| **Type** | Scenario |

### Question

EU customer requires residency; US DR region proposed — resolve in compliance expert mock.

### Short Answer (30 seconds)

EU-only replication pairs, policy deny US deploy, DPA review, support access logging, possibly EU-only DR within EU regions.

### Detailed Answer

**Options:**
A) EU primary + EU secondary only — no US replication
B) US DR with encrypted replica — legal review required
C) Delay US DR — accept RTO risk

**Document:** Legal sign-off on chosen residual.

**Policy-as-code:** Deny non-EU resource deploy.

### Architecture Perspective

Residency expert scenario requires legal partnership not solo architect call.

### Follow-up Questions

1. **Schrems II? — Transfer impact assessment.**
2. **Pseudonymization? — Reduce PII in cross-border flows.**

### Common Mistakes in Interviews

- US DR copies EU PII silently
- Architect decides without legal
- No policy deny non-EU deploy

---

## Q112: 10x Cost Inflection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

CFO asks cost inflection point at 10x scale mock — answer?

### Short Answer (30 seconds)

Linear until shard (6K), step function ops + infra at shard, human ops ceiling, FinOps autoscale caps, unit economics per order.

### Detailed Answer

**Cost narrative:**
- 1K→6K: mostly linear autoscale
- 6K→10K: +shard ops, +DB nodes, +SRE headcount
- Unit cost/order should decrease until cache hit plateau

**Chart:** Cost vs RPS with annotation at inflection.

**Ask:** Platform SRE hire at 6K gate.

### Architecture Perspective

10x expert includes economic inflection — not just technical.

### Follow-up Questions

1. **FinOps guardrails? — Budget alerts per environment.**
2. **Overprovision buffer? — State % headroom cost.**

### Common Mistakes in Interviews

- Claim linear cost to infinity
- Ignore SRE headcount step
- No unit economics

---

## Q113: Data Mesh Anti-pattern Review

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Review proposal labeled 'data mesh' that's central ETL team owning all pipelines — expert response?

### Short Answer (30 seconds)

Call anti-pattern kindly, map to mesh principles, propose domain ownership pilot, platform enables self-serve not central build.

### Detailed Answer

**Review script:**
'I see strong central engineering — mesh requires domain-owned data products. Suggest: central team builds platform templates; Checkout owns OrderCompleted product as pilot.'

**Document:** Gap analysis vs four mesh principles.

**Politics:** Offer central team platform role — not elimination.

### Architecture Perspective

Expert mesh review requires principled correction with diplomacy.

### Follow-up Questions

1. **Central team fear? — Reframe as platform elevation.**
2. **Pilot success metrics? — 2 products in catalog Q2.**

### Common Mistakes in Interviews

- Approve mesh label on central ETL
- Humiliate central team publicly
- No pilot proposed

---

## Q114: DR Cost Justification

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

CFO challenges 1.4× DR cost — justify in expert payment DR scenario.

### Short Answer (30 seconds)

$50K/min outage × 15 min RTO avoided once = $750K; historical 2 SEV1; insurance doesn't cover revenue loss; regulatory uptime requirement.

### Detailed Answer

**Math:**
- 1.4× infra = $180K/yr extra
- One 15-min SEV1 avoided = $750K+ revenue protection
- Payback <1 quarter if risk materializes

**Sensitivity:** Outage cost assumption range.

**Alternative rejected:** Cold DR cheaper — RTO 4hr fails regulatory.

### Architecture Perspective

DR expert defense is financial not technical only.

### Follow-up Questions

1. **Insurance gap? — Business interruption limits.**
2. **DR test cost? — Include in TCO — game days.**

### Common Mistakes in Interviews

- Hand-wave resilience value
- Cannot state outage $/min model
- Cold DR without RTO analysis

---

## Q115: Whiteboard Synthesis Question

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Final expert prompt: synthesize multi-tenant, migration, and risk register into one program narrative.

### Short Answer (30 seconds)

Single program with shared steering, phased tenant tiers during migration, risk register links migration waves, exec comms unified storyline.

### Detailed Answer

**Narrative arc:**
1. **Program:** SaaS modernization + acquisition integration
2. **Wave 1:** Multi-tenant platform landing zone
3. **Wave 2:** Acquired customer cohort migration
4. **Risks:** Top 5 across both — single register
5. **Exec:** One steering deck — milestones month 3/6/12

**Expert signal:** Systems thinking across mock topics.

### Architecture Perspective

Synthesis questions separate principal candidates from topic silos.

### Follow-up Questions

1. **Dependency between workstreams? — Identity before tenant migration.**
2. **Single vs dual program? — Prefer unified steering if same sponsor.**

### Common Mistakes in Interviews

- Three disconnected diagrams
- Separate risk registers per workstream
- No unified exec narrative

---

## Q116: Mock Interviewer Redirect

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Interviewer redirects mock from migration to security mid-session — adapt?

### Short Answer (30 seconds)

Acknowledge pivot, snapshot migration state on board, apply security lens to current design, link back to migration constraints at end.

### Detailed Answer

**Adaptation:**
'Good point — let me layer threat model on this target state.'

**Don't:** Erase work defensively.

**Bridge back:** 'Security gates affect wave 2 timing — note on roadmap.'

**Shows:** Flexibility under pressure.

### Architecture Perspective

Redirect handling is meta skill tested in senior mocks.

### Follow-up Questions

1. **STRIDE quick pass? — 5 min on current diagram.**
2. **Ask clarifier? — 'Deep security or migration trade-off priority?'**

### Common Mistakes in Interviews

- Refuse pivot rigidly
- Erase board and restart
- Ignore original migration context

---

## Q117: Executive Sponsor Loss

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Whiteboard Mock |
| **Frequency** | Occasional |
| **Type** | Scenario |

### Question

Executive sponsor leaves mid-program — expert stakeholder scenario in mock?

### Short Answer (30 seconds)

Pause major decisions, map new power structure, re-brief successor within 2 weeks, document continuity risks in register, protect team morale.

### Detailed Answer

**Actions:**
1. Identify interim sponsor with budget authority
2. Re-present BLUF to new sponsor
3. Freeze non-critical architecture changes
4. Update stakeholder map
5. Escalate program risk to steering

**Comms:** Transparent to teams — no rumor vacuum.

### Architecture Perspective

Sponsor loss is realistic program risk — expert mocks may include it.

### Follow-up Questions

1. **Decision log? — Helps successor onboard fast.**
2. **Back-channel new sponsor? — Start with listening tour.**

### Common Mistakes in Interviews

- Assume program continues unchanged
- Hide sponsor loss from teams
- Major ADRs without new sponsor buy-in

---

## Q118: Architecture Roadmap Pivot

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Acquisition forces 3-year roadmap pivot in month 6 — expert response?

### Short Answer (30 seconds)

Re-baseline Now/Next/Later, defer H3 innovate, insert integration theme H1, communicate trade-offs, OKR realignment with steering.

### Detailed Answer

**Pivot:**
- **Now:** Integration hub + identity
- **Next:** Deferred multi-region → EU only for acquired entity
- **Later:** AI ops moved to H3+1

**Trade-off slide:** What we stop, start, continue.

**Document:** Roadmap version 2.0 ADR.

### Architecture Perspective

Roadmap pivot tests strategic agility not rigid plans.

### Follow-up Questions

1. **Sunk cost fallacy? — Acknowledge past investment; forward look.**
2. **Team morale? — Explain why — acquisition opportunity.**

### Common Mistakes in Interviews

- Pretend original roadmap unchanged
- Pivot without steering approval
- No communicated stop list

---

## Q119: SLA Cascade Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Design SLA cascade from customer 99.95% to internal platform SLOs in expert mock.

### Short Answer (30 seconds)

Customer SLA → product SLO → platform SLO with error budget math; each layer stricter internal targets; exclusions documented.

### Detailed Answer

**Cascade:**
- Customer: 99.95% (21 min/mo)
- Product API: 99.97% (13 min)
- Platform K8s: 99.99% (4 min)

**Math:** Budget allocation per layer.

**Exclusions:** Third-party PSP — customer comms separate.

**Review:** Quarterly alignment audit.

### Architecture Perspective

SLA cascade expert topic links customer promise to internal accountability.

### Follow-up Questions

1. **Error budget policy? — Burn triggers reliability sprint at each layer.**
2. **Composite SLA? — Multi-service customer journey — weakest link.**

### Common Mistakes in Interviews

- Customer SLA with no internal SLOs
- Platform weaker than product SLA
- No exclusion documentation

---

## Q120: Staff Mock Debrief

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

How debrief yourself after a staff-level whiteboard mock interview?

### Short Answer (30 seconds)

Score clarify/design/depth/comms/trade-offs 1-5, note filler words, diagram clarity, missed NFRs, practice weak area within 48 hours.

### Detailed Answer

**Debrief rubric:**
| Area | Score | Gap |
|------|-------|-----|
| Clarify | /5 | |
| High-level | /5 | |
| Deep dive | /5 | |
| Trade-offs | /5 | |
| Comms | /5 | |

**48hr drill:** One focused mock on lowest score.

**Log:** Spreadsheet of missed prompts — pattern over 5 mocks.

### Architecture Perspective

Self-debrief discipline accelerates mock interview improvement.

### Follow-up Questions

1. **Recording review? — Painful but high value.**
2. **Peer debrief? — Architect guild practice pairs.**

### Common Mistakes in Interviews

- No structured debrief after mock
- Repeat same weak area 5 mocks
- Only practice full 45-min mocks

---
