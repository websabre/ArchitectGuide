# Week 49 — Intermediate Q&A

> Q031–Q070: Premium format (Week 1 quality).

---


## Q031: Multi-tenant SaaS Mock Intro

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

How do you open and structure a whiteboard mock for multi-tenant SaaS architecture?

### Short Answer (30 seconds)

Clarify tenant count, isolation tier, compliance, and scale first. Narrate a three-layer diagram (edge → app → data), state tenant model options, and reserve deep dive for one isolation path. Time-box: 5 min clarify, 10 min high-level, 20 min deep dive, 5 min trade-offs.

### Detailed Answer (3–5 minutes)

**Opening script (first 2 minutes):**
'Before I draw, I want to confirm: B2B or B2C tenants? Rough tenant count and whether any enterprise customers need dedicated isolation? Any compliance tier — SOC2, HIPAA? Peak RPS and data residency constraints?'

**Structure template:**
```
Minute 0–5   Requirements + assumptions on board
Minute 5–15  High-level: Tenant → APIM → App tier → Data tier
Minute 15–30 Deep dive: tenant model + auth + noisy-neighbor controls
Minute 30–40 NFRs: backup, DR, audit, observability by tenantId
Minute 40–45 Trade-offs + migration path for enterprise upsell
```

**Tenant model options to present:**
| Model | Isolation | Ops cost | When |
|-------|-----------|----------|------|
| Shared DB + tenantId + RLS | Logical | Low | Standard tier |
| Schema per tenant | Medium | Medium | Mid-market |
| DB/silo per tenant | Strong | High | Enterprise/HIPAA |

**Must mention:** JWT `tenant_id` claim, row-level security, per-tenant rate limits, tenant dimension in logs/metrics.

**Intro goal:** Show structured thinking before drawing boxes — interviewers score process, not perfect diagram.

### Architecture Perspective

Multi-tenant mock intro proves you clarify before designing — the #1 whiteboard failure mode is premature drawing.

### Follow-up Questions

1. **When default to RLS vs silo? — RLS for <100 enterprise; silo when contract or audit mandates physical separation.**
2. **Noisy neighbor on intro? — Name per-tenant rate limits and fair queue scheduling — even in opening.**

### Common Mistakes in Interviews

- Drawing microservices before stating tenant model
- Skipping compliance question in B2B SaaS mock
- No tenantId in observability discussion

---

## Q032: Acquisition Integration Mock Intro

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

How introduce an acquisition integration whiteboard mock before diving into integration patterns?

### Short Answer (30 seconds)

Start with discovery framing: systems of record, timeline, risk appetite, and governance. Present phased target state — never big-bang. Draw current vs target with integration hub as explicit boundary.

### Detailed Answer (3–5 minutes)

**Opening clarifiers:**
- What does acquired company own today (OMS, CRM, billing)?
- 12-month deadline hard or aspirational?
- Customer overlap — migrate all or new customers only?
- Team retention and skill mix on acquired side?

**Intro narrative structure:**
```
Phase 0: Discovery (inventory, data quality, SLAs)
Phase 1: Identity + read-only mirror
Phase 2: Event-driven sync + strangler for new traffic
Phase 3: Write path migration + decommission
```

**First diagram (simple):**
```
Acquired Stack ←→ Integration Hub ←→ Your Platform
                      ↓
               Customer ID Golden Record
```

**Name risks early:** Duplicate orders, currency/tax rules, dual ops cost, cultural resistance.

**Governance:** Joint integration squad with sunset date; executive milestone map at month 3, 6, 12.

**Intro goal:** Signal program thinking — acquisition mocks test integration strategy and stakeholder awareness, not API syntax.

### Architecture Perspective

Acquisition mock intro separates architects who plan phased integration from those who draw point-to-point REST.

### Follow-up Questions

1. **Strangler vs big-bang intro? — State strangler as default; big-bang only if EOL imminent — shows judgment.**
2. **Who owns integration hub? — Name platform/integration team — avoid orphan middleware.**

### Common Mistakes in Interviews

- Jumping to API design without systems-of-record map
- Ignoring data quality in legacy inventory
- No rollback or feature-flag cohort strategy mentioned

---

## Q033: Migration Strategy Mock Intro

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

How frame a large-scale migration whiteboard mock before detailing waves and landing zone?

### Short Answer (30 seconds)

Open with assess → plan → pilot → scale. State dependency mapping, wave criteria, landing zone prerequisites, and per-wave rollback. Quantify scope (service count, stateful vs stateless) before drawing Azure boxes.

### Detailed Answer (3–5 minutes)

**Opening clarifiers:**
- Source environment (on-prem K8s, VMs, mainframe)?
- Timeline and blackout windows?
- Stateful services count and data gravity?
- Team K8s/cloud maturity?
- Compliance constraints on data movement?

**Intro framework (write on board):**
```
1. ASSESS  — CMDB, dependency graph, risk scoring
2. LANDING ZONE — network, identity, policy guardrails
3. PILOT    — 5–10 low-risk services, learn run rate
4. WAVES    — dependency-ordered batches
5. VALIDATE — metrics per wave; rollback window
```

**Wave criteria to name upfront:**
| Wave | Selection rule |
|------|----------------|
| Pilot | Stateless, low revenue risk |
| Platform | Shared services others depend on |
| Core | Revenue path |
| Long tail | Legacy deps, manual steps |

**Per-service pattern:** Containerize → deploy target → traffic shift (DNS/APIM) → decommission source → 30-day rollback warm.

**Parallel track:** Data migration often separate program — call it out in intro.

**Intro goal:** Interviewers want wave planning discipline — not 'lift-and-shift everything weekend 1.'

### Architecture Perspective

Migration mock intro rewards sequencing language — assess and waves before technology choices.

### Follow-up Questions

1. **Replatform vs refactor intro? — Replatform containers first; refactor in cloud incrementally — set expectation early.**
2. **Landing zone before pilot? — Yes — identity and network policy before first production workload.**

### Common Mistakes in Interviews

- Big-bang cutover as opening recommendation
- No dependency-ordered wave criteria
- Ignoring team training and runbook updates

---

## Q034: Risk Register Mock Intro

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

How open a risk register whiteboard mock for a major architecture program?

### Short Answer (30 seconds)

State risk categories, scoring model (likelihood × impact), owner assignment, and review cadence before listing risks. Link risks to ADRs and executive escalation path.

### Detailed Answer (3–5 minutes)

**Opening clarifiers:**
- Program scope (greenfield, migration, launch)?
- Risk appetite — regulated vs startup tolerance?
- Audience — arch guild or risk committee?
- Time horizon — 90-day launch or 3-year program?

**Intro template (draw table header first):**
```
| Risk | Category | L | I | Score | Mitigation | Owner | Residual |
```

**Categories to announce:**
- Technical (performance, integration failure)
- Security (key compromise, data breach)
- Operational (skill gap, runbook gaps)
- Compliance (residency, audit)
- Vendor (PSP outage, cloud dependency)

**Scoring:** L/M/H × L/M/H → heat map; top-right items get steering committee visibility.

**Process:** Biweekly arch guild review; red items escalated with mitigation options not just alerts.

**Link to design:** Each high risk maps to ADR, spike, or accepted residual with exec sign-off.

**Intro goal:** Show governance maturity — risk register is living artifact, not one-time slide.

### Architecture Perspective

Risk register mock intro tests whether you quantify and assign — 'we'll monitor it' is not mitigation.

### Follow-up Questions

1. **Risk vs issue? — Risk = may happen; issue = occurred — separate logs in intro.**
2. **Heat map for exec? — Mention 5×5 grid translation for non-technical audience.**

### Common Mistakes in Interviews

- Generic risks without domain specificity
- No owners or review cadence on register
- Mitigation column says 'monitor' without action

---

## Q035: Executive Communication Mock Intro

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

How structure the opening of an executive communication mock for a non-technical audience?

### Short Answer (30 seconds)

Lead with business outcome (BLUF), not technology. One diagram, three milestones, cost/benefit, clear ask. Practice hard time limit — 5 minutes means 5 minutes.

### Detailed Answer (3–5 minutes)

**Opening clarifiers (even in mock):**
- Who is audience — CEO, CFO, board?
- Decision needed today or informational?
- Prior context — first briefing or progress update?

**5-minute structure (write outline first):**
```
1. Why now     — Business pain in dollars or risk
2. What        — Scope in plain language (not 'Kubernetes')
3. How         — Phased; customer impact = none/minimal
4. When        — 3 milestones with dates
5. Cost/benefit — Invest vs save; break-even
6. Ask         — Budget, headcount, or decision
```

**Language rules:**
- No acronyms without expansion
- 'Faster checkout' not 'microservices decomposition'
- '$2M annual savings by year 2' not 'improved scalability'

**One diagram:** Old brittle chain → new resilient flow — max 5 boxes.

**Anticipate one objection:** Prepare 'Why not buy SaaS?' or 'Why now vs next year?'

**Intro goal:** Executive comms mock tests translation — architects who cannot speak business fail regardless of technical depth.

### Architecture Perspective

Executive comms intro is BLUF discipline — headline outcome before any architecture vocabulary.

### Follow-up Questions

1. **CEO vs board depth? — CEO: outcomes and ask; board: risk, audit, material cost.**
2. **Yellow status in exec update? — Early yellow preferred over surprise red — mention in intro.**

### Common Mistakes in Interviews

- Opening with technology stack names
- No dollar figures or timeline in first minute
- Ending without explicit ask

---

## Q036: Multi-tenant SaaS Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

45-minute whiteboard mock: design multi-tenant SaaS for 5,000 B2B customers with data isolation, per-tenant config, and noisy-neighbor protection.

### Short Answer (30 seconds)

Start with requirements: tenant model (shared DB + tenantId vs schema-per-tenant vs DB-per-tenant), isolation tier, SLAs. Draw APIM → app tier → data tier. Cover auth (OIDC + tenant claim), row-level security, rate limits per tenant, and observability by tenantId.

### Detailed Answer (3–5 minutes)

**Minute 0–5 — Clarify:** B2B, 5K tenants, 50 enterprise (dedicated), rest shared. Compliance: SOC2, some HIPAA. Peak 10K RPS aggregate.

**Minute 5–15 — High-level:**
```
Tenant → APIM (rate limit key=tenantId) → App Service/AKS → PostgreSQL (RLS) + Redis (tenant-scoped cache)
```
Tiered isolation: Standard = shared pool + RLS; Enterprise = dedicated schema or silo.

**Minute 15–30 — Deep dive:**
- **Identity:** JWT with `tenant_id` claim; no cross-tenant queries without super-admin role
- **Data:** Shared DB with RLS policies; hot enterprise on dedicated flexible server
- **Config:** Feature flags per tenant (LaunchDarkly or app table)
- **Noisy neighbor:** Per-tenant rate limits, connection pool caps, queue fair scheduling

**Minute 30–40 — NFRs:** Backup per tenant export, DR RPO 1h, audit log immutable.

**Minute 40–45 — Trade-offs:** Schema-per-tenant ops cost vs RLS simplicity — document migration path for enterprise upsell.

### Architecture Perspective

Whiteboard mocks test structured thinking under time — narrate trade-offs aloud.

### Follow-up Questions

1. **When move tenant to dedicated silo? — Revenue tier, compliance, or performance SLO breach.**
2. **Cross-tenant analytics? — Aggregated warehouse with PII stripped — never prod DB.**

### Common Mistakes in Interviews

- Jumping to microservices per tenant
- No tenant in observability dimensions
- Ignoring enterprise dedicated tier in design

---

## Q037: Acquisition Integration Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Whiteboard mock: integrate acquired company's order system into your platform within 12 months.

### Short Answer (30 seconds)

Phase 0 discovery → strangler fig → unified customer identity → order sync → cutover. Draw current/target state, integration patterns (event bus vs API), data mapping, and decommission timeline.

### Detailed Answer (3–5 minutes)

**Discovery (Month 1–2):** Inventory APIs, data model, volume, SLAs, team skills. Identify system of record per domain.

**Target architecture:**
```
Acquired OMS ←→ Integration Hub (Event Hub + Logic Apps) ←→ Your Order Service
                    ↓
              Master Data (Customer ID map)
```

**Patterns:**
- **Customer identity:** Golden record + `legacy_acme_id` mapping table
- **Orders:** Event-driven sync; your platform read-only mirror first, then write path
- **Strangler:** New customers on your stack; legacy tenants migrated in waves

**Risks:** Duplicate orders, currency/tax rules, 2× ops during transition.

**Cutover:** Feature flag per tenant cohort; rollback = revert flag + replay events.

### Architecture Perspective

Acquisition mocks test integration strategy and political awareness — mention program governance.

### Follow-up Questions

1. **Big-bang vs strangler? — Strangler default unless acquired system end-of-life imminent.**
2. **Who owns integration team? — Joint squad with sunset date for acquired stack.**

### Common Mistakes in Interviews

- Big-bang cutover weekend without rollback
- Ignore data quality in legacy system
- No executive milestone map for 12 months

---

## Q038: Migration Strategy Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Present migration strategy mock: move 200 microservices from on-prem Kubernetes to AKS over 18 months.

### Short Answer (30 seconds)

Assess → wave plan → landing zone → pilot → scale. Cover CI/CD parity, networking (ExpressRoute), identity, data gravity, and rollback per wave.

### Detailed Answer (3–5 minutes)

**Assess:** CMDB dependency map, stateful vs stateless, compliance, team readiness.

**Waves:**
| Wave | Criteria | Count |
|------|----------|-------|
| 1 Pilot | Stateless, low risk | 10 |
| 2 Platform | Shared services | 30 |
| 3 Core | Revenue path | 80 |
| 4 Long tail | Legacy deps | 80 |

**Landing zone:** Hub-spoke VNet, AAD workload identity, ACR, policy guardrails.

**Per service:** Containerize → deploy to AKS → traffic shift via DNS/APIM → decommission on-prem.

**Data:** Stay on-prem initially with Private Link; migrate DBs in parallel track.

**Success metrics:** % services migrated, incident rate, cost delta, deploy frequency.

### Architecture Perspective

Migration mocks reward wave planning and risk sequencing — not lift-and-shift fantasy.

### Follow-up Questions

1. **Replatform vs refactor? — Replatform containers first; refactor in Azure incrementally.**
2. **Rollback per wave? — Keep on-prem warm 30 days — DNS flip back.**

### Common Mistakes in Interviews

- Big-bang 200 services one weekend
- No dependency-ordered waves
- Ignore team training and runbook updates

---

## Q039: Risk Register Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Whiteboard: build architecture risk register for cloud-native payments platform launch.

### Short Answer (30 seconds)

List risks: likelihood × impact, owner, mitigation, residual risk. Categories: technical, security, operational, compliance, vendor.

### Detailed Answer (3–5 minutes)

**Sample register:**
| Risk | L | I | Mitigation | Owner |
|------|---|---|------------|-------|
| PSP outage | M | H | Multi-PSP routing + circuit breaker | Platform |
| Key compromise | L | H | HSM, key rotation, break-glass | Security |
| Data residency breach | L | H | Region lock, policy-as-code | Architect |
| Team skill gap on K8s | H | M | Training, vendor SRE 6mo | Eng Mgr |
| Cost overrun | M | M | FinOps alerts, autoscale caps | FinOps |

**Process:** Review biweekly in arch guild; escalate red items to steering committee.

**Link to ADRs:** Each high risk maps to design decision or spike.

**Residual risk:** Document accepted risks with exec sign-off.

### Architecture Perspective

Risk register mock tests governance maturity — quantify and assign owners.

### Follow-up Questions

1. **Risk vs issue? — Risk = future; issue = happened — separate logs.**
2. **Heat map presentation? — 5×5 grid for exec — top-right focus.**

### Common Mistakes in Interviews

- Generic risks without payment-specific items
- No owners or review cadence
- Mitigation='monitor' without action

---

## Q040: Executive Comms Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Mock: explain 6-month platform modernization to non-technical CEO in 5 minutes.

### Short Answer (30 seconds)

Lead with business outcome, one diagram, three milestones, cost/benefit, ask. No jargon — 'faster features, lower outage risk, $2M annual savings by year 2.'

### Detailed Answer (3–5 minutes)

**Structure (5 min):**
1. **Why now** — Legacy blocking new product line; 3 outages last year cost $4M
2. **What** — Modernize checkout and inventory platform (not everything)
3. **How** — Phased; customers see no downtime
4. **When** — M1 foundation, M3 first product on new stack, M6 legacy decommission 80%
5. **Cost** — $3M invest, $2M/yr save, break-even month 18
6. **Ask** — Approve $800K Q3 budget and dedicated squad

**One slide diagram:** Old brittle chain → new resilient services.

**Anticipate:** 'Why not buy SaaS?' — Prepared answer on customization and data control.

### Architecture Perspective

Executive comms mock tests translation — business metrics first, technology second.

### Follow-up Questions

1. **What if CEO asks about AI? — Tie to roadmap phase 2 — don't derail core message.**
2. **Board vs CEO depth? — CEO: outcomes; board: risk and audit.**

### Common Mistakes in Interviews

- Opening with Kubernetes and microservices
- No dollar figures or timeline
- No clear ask at end

---

## Q041: Stakeholder Map Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Create stakeholder map for enterprise data platform initiative affecting 12 teams.

### Short Answer (30 seconds)

Map power vs interest grid; identify champions, blockers, neutrals. Plan engagement: weekly tech leads, biweekly sponsors, monthly steering.

### Detailed Answer (3–5 minutes)

**Stakeholders:**
- **High power, high interest:** CTO, VP Data — manage closely
- **High power, low interest:** CFO — keep satisfied (cost dashboard)
- **Low power, high interest:** Team leads — consult, involve in design
- **Blockers:** Legacy DW team fearing obsolescence — co-opt as migration leads

**Engagement plan:**
| Stakeholder | Message | Cadence |
|-------------|---------|--------|
| CTO | Strategic alignment, risk | Biweekly |
| Team leads | API contracts, timeline | Weekly |
| Security | Compliance gates | Per milestone |

**RACI on key decisions:** Who approves schema standards, budget, vendor.

**Political risk:** Competing VP fiefdoms — executive sponsor resolves escalations.

### Architecture Perspective

Stakeholder maps show you ship architecture through people — not diagrams alone.

### Follow-up Questions

1. **Sponsor vs champion? — Sponsor has budget; champion drives day-to-day.**
2. **Missing stakeholder discovered late? — Update map live — common in mocks.**

### Common Mistakes in Interviews

- Treating all stakeholders identical
- No plan for blockers
- Map without engagement cadence

---

## Q042: Build vs Buy Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Whiteboard mock: build vs buy decision for enterprise API management layer.

### Short Answer (30 seconds)

Evaluate: requirements, TCO 3-year, time-to-market, customization, team skills, exit strategy. Score matrix; recommend with ADR.

### Detailed Answer (3–5 minutes)

**Requirements:** OAuth, rate limiting, developer portal, multi-region, $50M revenue API monetization.

**Options:**
| | Azure APIM | Kong Enterprise | Build (YARP + custom) |
|---|------------|-----------------|----------------------|
| TTM | Weeks | Weeks | 12+ months |
| TCO 3yr | $400K | $500K | $1.2M eng |
| Custom policies | Good | Excellent | Unlimited |
| Ops burden | Low | Medium | High |

**Decision:** Azure APIM — already on Azure, adequate policies, lowest ops.

**Rejected build:** Team 8 engineers — opportunity cost on product.

**Exit:** OpenAPI standard; export policies; avoid proprietary lock where possible.

### Architecture Perspective

Build vs buy mocks need numbers and rejected alternatives — not ideology.

### Follow-up Questions

1. **When build wins? — Unique protocol, regulatory constraint, strategic differentiator.**
2. **Hybrid? — APIM front door + custom auth plugin — document boundary.**

### Common Mistakes in Interviews

- Build because 'we're special' without requirements
- SaaS TCO missing headcount
- No exit strategy for vendor lock-in

---

## Q043: Technical Debt Presentation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Present technical debt portfolio to engineering leadership for 20% capacity allocation.

### Short Answer (30 seconds)

Quantify debt: incident correlation, velocity drag, security CVEs. Prioritize by risk × effort; show 90-day paydown plan with measurable outcomes.

### Detailed Answer (3–5 minutes)

**Debt categories:**
1. **Reliability** — Monolith deploy 4hr → 3 outages/quarter
2. **Security** — 47 critical CVEs in legacy Java 8
3. **Velocity** — 3-day feature in payments vs 3-week due to tangled deps
4. **Cost** — Overprovisioned VMs $180K/yr

**Prioritization:** ICE score or risk matrix.

**Ask:** 20% sprint capacity + 2 dedicated platform engineers for Q3.

**Metrics:** Deploy frequency, MTTR, CVE count, lead time — baseline now, target 90 days.

**Visual:** Debt quadrant — quick wins (migrate logging) vs strategic (extract payment service).

### Architecture Perspective

Tech debt presentations must speak executive — tie to incidents and dollars.

### Follow-up Questions

1. **Interest vs principal? — Interest = ongoing cost; principal = paydown effort.**
2. **Stop-the-line debt? — Security CVEs may preempt feature work.**

### Common Mistakes in Interviews

- Complaint list without prioritization
- No metrics to prove improvement
- Asking 100% capacity for debt

---

## Q044: Architecture Roadmap Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Draw 3-year architecture roadmap aligning platform maturity with business goals.

### Short Answer (30 seconds)

Horizon 1 (0–12mo) stabilize, H2 (12–24mo) scale, H3 (24–36mo) innovate. Link initiatives to capabilities: observability, self-service, multi-region.

### Detailed Answer (3–5 minutes)

**Year 1 — Foundation:**
- Observability baseline (SLIs, tracing)
- CI/CD golden path
- Identity standardization

**Year 2 — Scale:**
- Multi-region active-passive
- Event-driven integration hub
- Platform team self-service portal

**Year 3 — Optimize:**
- FinOps automation
- AI-assisted ops
- Cell-based architecture for blast radius

**Mapping:** Each initiative → business OKR (time-to-market, uptime 99.95%).

**Dependencies:** Identity before zero-trust; observability before SLO-based scaling.

**Now/Next/Later** board for stakeholder communication.

### Architecture Perspective

Roadmap mocks test strategic sequencing — dependencies and business linkage.

### Follow-up Questions

1. **Theme vs project roadmap? — Themes for flexibility; projects for committed quarters.**
2. **Re-baseline when? — Quarterly — pivot on acquisition or market shift.**

### Common Mistakes in Interviews

- Technology laundry list without outcomes
- Everything in year 1
- No dependency arrows between initiatives

---

## Q045: Vendor Evaluation Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Mock vendor evaluation: select observability platform for 500-service estate.

### Short Answer (30 seconds)

Define weighted criteria, POC scope, reference calls, security review, TCO. Score Datadog vs Dynatrace vs Azure Monitor.

### Detailed Answer (3–5 minutes)

**Criteria (weight):** Azure integration (20%), K8s APM (20%), cost at scale (20%), SIEM export (15%), UX (10%), support (15%).

**POC:** 20 representative services, 2 weeks, success = trace 99% requests, <5min alert latency.

**TCO model:** Ingest GB/day × 365 × $/GB + seats.

**Security:** Data residency, SSO, pen test results.

**Scorecard:** Weighted total; recommendation with conditions (e.g., negotiate ingest cap).

### Architecture Perspective

Vendor eval mocks prove structured procurement — not brand preference.

### Follow-up Questions

1. **Build vs buy observability? — Rarely build at 500 services.**
2. **Lock-in mitigation? — OpenTelemetry instrumentation — portable telemetry.**

### Common Mistakes in Interviews

- POC on toy app only
- Ignore egress/ingest cost at scale
- Single vendor quote without negotiation leverage

---

## Q046: SLA Negotiation Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Mock: negotiate internal SLA between platform team and product squads for Kubernetes platform.

### Short Answer (30 seconds)

Define SLI/SLO, error budget, escalation, exclusions. Platform commits uptime; squads commit migration standards and incident cooperation.

### Detailed Answer (3–5 minutes)

**Platform SLOs:**
- Control plane API 99.9%
- Node pool availability 99.95%
- P1 incident ack 15 min

**Squad obligations:**
- Use golden path templates
- Resource limits on all pods
- Runbooks for owned services

**Error budget:** 43 min/month downtime — if burned, freeze platform changes, focus reliability.

**Exclusions:** Customer DNS, misconfigured squad manifests.

**Review:** Quarterly SLA review with metrics dashboard.

### Architecture Perspective

SLA negotiation mock tests bilateral accountability — not one-sided guarantees.

### Follow-up Questions

1. **Internal vs customer SLA? — Internal enables customer SLA — cascade requirements.**
2. **Penalty without error budget? — Blame culture — pair SLO with budget policy.**

### Common Mistakes in Interviews

- Vague 'best effort' platform commitment
- No squad responsibilities
- SLA without measurement method

---

## Q047: Team Topology Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Design team topology for platform engineering supporting 15 product streams.

### Short Answer (30 seconds)

Team Topologies: platform team, enabling team, complicated-subsystem, stream-aligned. Map interaction modes: X-as-a-Service, facilitation, collaboration.

### Detailed Answer (3–5 minutes)

**Structure:**
- **Platform (8):** K8s, CI/CD, observability — X-as-a-Service
- **Enabling (3):** Rotates to streams for upskilling — facilitation
- **Complicated subsystem (4):** Payments, identity — collaboration with streams
- **Streams (15×6):** Own features end-to-end

**Interfaces:** Internal developer portal, ticket SLAs for platform requests.

**Anti-pattern:** Platform as ticket queue bottleneck — embed enabling team instead.

**Conway alignment:** Service boundaries match team boundaries where possible.

### Architecture Perspective

Team topology mock connects org design to architecture deliverability.

### Follow-up Questions

1. **Platform as product? — Treat internal devs as customers — roadmap, NPS.**
2. **Too many platform teams? — Consolidate golden paths — avoid 5 K8s teams.**

### Common Mistakes in Interviews

- Central platform ticket queue with 2-week wait
- Stream teams own K8s cluster upgrades
- Topology diagram without interaction modes

---

## Q048: Conway's Law Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

Explain Conway's Law impact on proposed microservices split and recommend org changes.

### Short Answer (30 seconds)

Organizations ship architectures mirroring communication structures. Misaligned splits cause integration pain — align service boundaries to team ownership or fund collaboration tax.

### Detailed Answer (3–5 minutes)

**Scenario:** 4 teams, monolith splitting into 12 services but teams still organized by layer (UI, API, DB).

**Problem:** Every feature touches 3 teams → slow releases, blame loops.

**Recommendation:** Reorganize to stream-aligned teams owning vertical slices (Checkout, Catalog, Fulfillment). Each owns 3–4 services.

**Alternative:** If reorg impossible — assign **service owners** with DRI per service, weekly cross-team sync, API versioning contract.

**Architect role:** Flag Conway misalignment in ADR; quantify collaboration tax (lead time data).

### Architecture Perspective

Conway mock tests whether you see org-technical feedback loops.

### Follow-up Questions

1. **Inverse Conway? — Design org to desired architecture — deliberate reorg.**
2. **Melvin Conway 1968? — Historical credibility in senior interviews.**

### Common Mistakes in Interviews

- 12 services 4 teams no interaction plan
- Ignore communication overhead in estimates
- Propose reorg without change management plan

---

## Q049: Platform Team Pitch

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Pitch new internal developer platform to CTO for headcount and budget.

### Short Answer (30 seconds)

Problem: 45min deploy times, 15 duplicate CI templates. Vision: golden path, self-service, measurable developer productivity. ROI: 200 engineers × 2hr/week saved.

### Detailed Answer (3–5 minutes)

**Pitch structure:**
1. **Pain** — DORA metrics below industry; survey NPS 32
2. **Vision** — 'Deploy in 15 min with guardrails'
3. **Product** — Portal, templates, env provisioning, docs
4. **Team** — 6 platform engineers + 1 PM
5. **ROI** — 200 × 2hr × $75/hr × 50 weeks = $1.5M/yr
6. **Milestones** — Q1 portal MVP, Q2 50% adoption

**Metrics:** Deployment frequency, lead time, platform adoption %.

**Risk:** Adoption — embed enabling team in pilot squads.

### Architecture Perspective

Platform pitch mock is sales to internal executives — quantify developer time.

### Follow-up Questions

1. **Thinnest viable platform? — One golden path language first — .NET or Java.**
2. **Platform PM needed? — Yes at 200+ engineers — roadmap and adoption.**

### Common Mistakes in Interviews

- Build everything before pilot users
- ROI without baseline DORA metrics
- Platform team disconnected from stream pain

---

## Q050: Cost-Benefit Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Whiteboard: cost-benefit analysis for migrating data warehouse to cloud.

### Short Answer (30 seconds)

CAPEX vs OPEX shift, 3-year TCO, soft benefits (agility), risks. Include egress, reserved instances, staffing change.

### Detailed Answer (3–5 minutes)

**Costs:**
- Migration project: $600K (12 FTE-months)
- Cloud run rate: $35K/mo (compute + storage + network)
- Training: $80K

**Benefits:**
- Decommission on-prem HW: $200K/yr maintenance saved
- Elastic analytics — pause dev clusters nights: $120K/yr
- Faster insights — revenue enablement $500K/yr (assumption stated)

**NPV 3yr:** Positive if revenue assumption ≥50% credible.

**Sensitivity:** ±30% on cloud run rate.

**Recommendation:** Proceed phase 1 — dev/test migrate; validate run rate before prod.

### Architecture Perspective

Cost-benefit mock requires explicit assumptions and sensitivity — finance respects honesty.

### Follow-up Questions

1. **Stranded on-prem cost? — Include datacenter contract exit penalties.**
2. **Real options? — Phase 1 buys learning — value of deferring full commit.**

### Common Mistakes in Interviews

- Cloud always cheaper claim
- Ignore egress and support staffing
- Benefits without credible attribution

---

## Q051: Compliance Gap Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Assess compliance gaps for SOC2 Type II on new customer data API.

### Short Answer (30 seconds)

Map controls to architecture: access control, encryption, logging, change mgmt, vendor risk. Gap analysis → remediation plan with owners and dates.

### Detailed Answer (3–5 minutes)

**Control domains:**
| SOC2 CC | Current | Gap | Remediation |
|---------|---------|-----|-------------|
| CC6.1 Logical access | Partial RBAC | No ABAC for PII | Q2 IAM project |
| CC6.7 Encryption | TLS yes | At-rest gaps in blob | Enable CMK |
| CC7.2 Monitoring | Logs exist | No SIEM alerts | Sentinel rules |
| CC8.1 Change mgmt | Informal | No prod approval gate | GitOps + policy |

**Timeline:** 90-day remediation before audit window.

**Evidence:** Architecture diagrams, access reviews, pen test for auditor.

### Architecture Perspective

Compliance gap mock bridges security controls and architecture decisions.

### Follow-up Questions

1. **SOC2 vs ISO 27001? — Overlap — map once, certify twice if needed.**
2. **Shared responsibility cloud? — Document Azure vs your controls matrix.**

### Common Mistakes in Interviews

- Checkbox security without architecture changes
- Gaps without owners and dates
- Audit surprise — no continuous control monitoring

---

## Q052: DR Presentation Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Present disaster recovery architecture for tier-1 payment service to risk committee.

### Short Answer (30 seconds)

RTO/RPO targets, active-passive topology, failover runbook, test cadence, last drill results.

### Detailed Answer (3–5 minutes)

**Targets:** RTO 15 min, RPO 5 min (sync repl lag bounded).

**Topology:**
```
Primary Region (East) ──async repl──► Secondary (West)
APIM health probe → Traffic Manager failover
```

**Failover:** Automated DNS flip when health <2/3 checks fail 3 min. Manual approval for failback.

**Data:** SQL geo-replica; Cosmos multi-region.

**Testing:** Game day quarterly; last drill 94% success — gap on secrets replication fixed.

**Cost:** 1.4× single region — justified by $50K/min outage cost model.

### Architecture Perspective

DR mock must include test evidence — risk committee asks 'when did you last drill?'

### Follow-up Questions

1. **Active-active vs active-passive? — Active-active harder for payments — split-brain risk.**
2. **Backup vs DR? — Backup for corruption; DR for region loss — both needed.**

### Common Mistakes in Interviews

- DR never tested
- RPO/RTO undefined
- Failover depends on manual steps without runbook

---

## Q053: Performance Crisis Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Live mock: checkout p99 latency jumped from 200ms to 3s during flash sale. Walk through diagnosis and mitigation.

### Short Answer (30 seconds)

Triage: metrics → traces → logs. Hypothesis: DB connection pool exhaustion. Mitigate: scale, cache, queue, circuit breaker. Communicate status every 15 min.

### Detailed Answer (3–5 minutes)

**Minute 0–5:** Confirm scope — checkout only; payment PSP green; DB CPU 98%.

**Minute 5–15:** Traces show 2.8s in inventory SQL; connection pool maxed (Hikari 50).

**Immediate:**
- Scale app instances (doesn't fix DB)
- Enable inventory read cache TTL 30s
- Increase pool cautiously — risks DB overwhelm
- Shed load: queue non-critical steps

**Root cause:** Missing index on hot query + pool undersized for new traffic.

**Post:** Add index, pool sizing formula, load test before next sale.

**Comms:** 'Checkout degraded — workaround: retry — ETA 45 min fix.'

### Architecture Perspective

Performance crisis mock tests structured incident thinking — measure before optimize.

### Follow-up Questions

1. **Load shed vs scale? — Scale if capacity exists; shed if downstream saturated.**
2. **Blameless postmortem? — Mention after stabilization — culture signal.**

### Common Mistakes in Interviews

- Restart everything without data
- Skip dependency graph check
- No stakeholder comms during incident

---

## Q054: Scale 10x Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Design evolution plan to scale order API from 1K to 10K orders/sec.

### Short Answer (30 seconds)

Identify bottlenecks at each order of magnitude. Caching, read replicas, async writes, sharding, CDN, autoscale policies.

### Detailed Answer (3–5 minutes)

**1K → 3K:** Vertical scale + read replicas + Redis cache for catalog

**3K → 6K:**
- Async order acceptance (queue) — 202 + poll/webhook
- DB connection pooling per service
- Stateless app autoscale on CPU/RPS

**6K → 10K:**
- Shard orders by `customerId` hash
- Separate read/write DB paths (CQRS light)
- Rate limit abusive tenants at edge

**Observability:** Load test in staging at 12K/sec; chaos on DB replica lag.

**Cost:** Linear until shard; step function at 6K for ops complexity.

### Architecture Perspective

10x mock tests incremental scaling narrative — not day-one over-engineering.

### Follow-up Questions

1. **When shard? — Single writer DB >70% sustained — before hard ceiling.**
2. **Global 10x? — Add multi-region after single-region 10x proven.**

### Common Mistakes in Interviews

- Microservices day one for 1K RPS
- Skip load test validation
- Cache without invalidation strategy

---

## Q055: Legacy Wrap Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Whiteboard: strangler fig pattern to wrap 20-year-old COBOL billing system.

### Short Answer (30 seconds)

Anti-corruption layer, event extraction, parallel run, gradual traffic shift. Don't rewrite — wrap and replace module by module.

### Detailed Answer (3–5 minutes)

**Wrap layer:**
```
New Billing API → ACL (translate REST ↔ COBOL copybook) → MQ → Mainframe
```

**Extraction:** Change data capture from mainframe DB → event bus → new billing read model.

**Parallel run:** Compare invoices new vs legacy 90 days; 99.99% match threshold.

**Modules:** Start with inquiry (read-only), then adjustments, finally rating engine last.

**Team:** Mainframe SMEs + modern squad pair programming.

### Architecture Perspective

Legacy wrap mock rewards pragmatism — strangler over big-bang rewrite.

### Follow-up Questions

1. **ACL pattern? — Isolate legacy model from domain model — DDD boundary.**
2. **When rewrite? — Never default; only if wrap cost exceeds rewrite NPV.**

### Common Mistakes in Interviews

- Big-bang COBOL rewrite
- No mainframe SME access plan
- Skip parallel run validation

---

## Q056: Tenant Isolation Tiers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

What tenant isolation tiers should you present in a multi-tenant SaaS whiteboard?

### Short Answer (30 seconds)

Standard (shared + RLS), professional (schema-per-tenant), enterprise (dedicated silo). Match tier to compliance, revenue, and noisy-neighbor risk.

### Detailed Answer (3–5 minutes)

**Tier model:**
| Tier | Isolation | Ops | When |
|------|-----------|-----|------|
| Standard | Shared DB + tenantId + RLS | Low | SMB |
| Professional | Schema per tenant | Medium | Mid-market |
| Enterprise | Dedicated DB/cluster | High | HIPAA/regulated |

**Must cover:** JWT `tenant_id`, per-tenant rate limits, observability dimension, backup/export per tenant.

**Upsell path:** Migration runbook from RLS → schema → silo without rewrite.

### Architecture Perspective

Isolation tiers show commercial and technical alignment — not one-size-fits-all.

### Follow-up Questions

1. **Noisy neighbor controls per tier? — Rate limits, pool caps, fair queue scheduling.**
2. **Cross-tenant admin? — Break-glass role with audit — never default query.**

### Common Mistakes in Interviews

- Microservice per tenant by default
- No enterprise dedicated option
- Tenant missing from logs and metrics

---

## Q057: Acquisition Discovery Checklist

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

What discovery checklist opens an acquisition integration architecture mock?

### Short Answer (30 seconds)

Systems of record, data quality, volume/SLAs, team skills, customer overlap, regulatory constraints, and decommission timeline before drawing integration.

### Detailed Answer (3–5 minutes)

**Discovery checklist:**
1. Inventory APIs, batch jobs, data stores
2. Identify system of record per domain (orders, customers, billing)
3. Data quality score — duplicates, null keys, currency rules
4. Transaction volume and peak patterns
5. Acquired team retention and skill map
6. Customer overlap — migrate all or new-only?
7. Contractual/regulatory constraints
8. Hard decommission date or flexible?

**Output:** Current-state context diagram + integration risk list before target state.

**Governance:** Joint integration squad with executive milestone map.

### Architecture Perspective

Acquisition mocks fail when integration is drawn before inventory.

### Follow-up Questions

1. **Strangler default? — Yes unless EOL forces big-bang — state in opening.**
2. **Golden customer record? — Identity mapping table is first-class artifact.**

### Common Mistakes in Interviews

- API design before systems-of-record map
- Ignoring legacy data quality
- No rollback cohort strategy

---

## Q058: Migration Wave Criteria

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

How define migration wave criteria in a whiteboard migration strategy mock?

### Short Answer (30 seconds)

Order waves by dependency graph, risk, and business criticality — pilot stateless first, platform next, revenue path third, long tail last.

### Detailed Answer (3–5 minutes)

**Wave selection matrix:**
| Wave | Criteria | Example count |
|------|----------|---------------|
| Pilot | Stateless, low revenue risk | 5–10 |
| Platform | Shared dependencies | 20–30 |
| Core | Revenue path | 40–80 |
| Long tail | Legacy deps, manual steps | Remainder |

**Per wave:** Rollback window (DNS warm 30 days), success metrics, runbook updates.

**Parallel track:** Data migration often separate program — call out explicitly.

**Anti-pattern:** Big-bang weekend cutover for 200 services.

### Architecture Perspective

Wave criteria prove sequencing discipline — assess before Azure boxes.

### Follow-up Questions

1. **Replatform vs refactor? — Containerize first; refactor incrementally in cloud.**
2. **Landing zone before pilot? — Identity and network policy before prod workload.**

### Common Mistakes in Interviews

- Lift-and-shift everything wave 1
- No dependency-ordered batches
- Ignore team training and runbooks

---

## Q059: Risk Scoring Model

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

How score risks in an architecture risk register whiteboard mock?

### Short Answer (30 seconds)

Likelihood × impact heat map, categories (technical, security, ops, compliance, vendor), owner per risk, mitigation with residual risk and review cadence.

### Detailed Answer (3–5 minutes)

**Scoring:** L/M/H × L/M/H → heat map; top-right escalates to steering.

**Categories:** Technical, security, operational, compliance, vendor.

**Table columns:** Risk | L | I | Score | Mitigation | Owner | Residual | Review date

**Process:** Biweekly arch guild; red items with options not alerts only.

**Link:** High risks map to ADR, spike, or accepted residual with exec sign-off.

**Distinction:** Risk (may happen) vs issue (occurred) — separate logs.

### Architecture Perspective

Risk register mock tests governance — 'monitor' is not mitigation.

### Follow-up Questions

1. **Heat map for exec? — 5×5 grid translation for non-technical audience.**
2. **Residual risk acceptance? — Document with exec sign-off and expiry.**

### Common Mistakes in Interviews

- Generic risks without domain specificity
- No owners or review cadence
- Mitigation column says monitor only

---

## Q060: Executive BLUF Structure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

What BLUF structure should architects use in executive communication mocks?

### Short Answer (30 seconds)

Bottom line up front: business outcome, scope in plain language, phased how, three milestones, cost/benefit, explicit ask — no jargon in first minute.

### Detailed Answer (3–5 minutes)

**5-minute BLUF:**
1. Why now — pain in dollars or risk
2. What — scope plain language
3. How — phased; customer impact minimal
4. When — 3 milestones with dates
5. Cost/benefit — invest vs save; break-even
6. Ask — budget, headcount, or decision

**Rules:** No acronyms without expansion; one diagram max; rehearse hard time limit.

**Anticipate:** 'Why not buy SaaS?' 'Why now vs next year?'

### Architecture Perspective

Executive comms intro is BLUF discipline — headline before architecture vocabulary.

### Follow-up Questions

1. **Yellow status? — Early yellow preferred over surprise red.**
2. **CEO vs board depth? — CEO outcomes; board risk, audit, materiality.**

### Common Mistakes in Interviews

- Opening with Kubernetes and microservices
- No dollar figures or timeline
- Ending without explicit ask

---

## Q061: Power Interest Grid

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

How use a power/interest stakeholder map in architecture whiteboard mocks?

### Short Answer (30 seconds)

Plot stakeholders on power vs interest; strategies: manage closely, keep satisfied, consult, monitor. Add engagement cadence and RACI for key decisions.

### Detailed Answer (3–5 minutes)

**Quadrants:**
- High power, high interest → manage closely (CTO, sponsor)
- High power, low interest → keep satisfied (CFO — cost dashboard)
- Low power, high interest → consult (team leads)
- Low power, low interest → monitor

**Add:** Engagement cadence table, RACI on schema/budget/vendor decisions.

**Political risk:** Competing VP fiefdoms — exec sponsor resolves escalations.

**Update live:** Missing stakeholder discovered late — revise map in mock.

### Architecture Perspective

Stakeholder maps show architecture ships through people.

### Follow-up Questions

1. **Sponsor vs champion? — Sponsor has budget; champion drives adoption.**
2. **Blocker strategy? — Co-opt as migration leads — not ignore.**

### Common Mistakes in Interviews

- All stakeholders same cadence
- Map without engagement plan
- No plan for identified blockers

---

## Q062: Build vs Buy Scorecard

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

What belongs on a build vs buy scorecard in a whiteboard mock?

### Short Answer (30 seconds)

Requirements, 3-year TCO, time-to-market, customization need, team skills, ops burden, exit strategy. Score matrix with rejected alternative documented in ADR.

### Detailed Answer (3–5 minutes)

**Criteria weights example (APIM):**
| Criterion | Weight |
|-----------|--------|
| TTM | 25% |
| TCO 3yr | 25% |
| Customization | 20% |
| Ops burden | 15% |
| Team skills | 15% |

**Options:** Buy (APIM/Kong), build (YARP+custom), hybrid.

**Document:** Rejected option with honest trade-off — not ideology.

**Exit:** OpenAPI, portable policies — conscious lock-in ADR.

### Architecture Perspective

Build vs buy mocks need numbers and rejected alternatives.

### Follow-up Questions

1. **When build wins? — Unique protocol, regulatory constraint, strategic differentiator.**
2. **Hybrid boundary? — APIM front + custom auth plugin — document line.**

### Common Mistakes in Interviews

- Build because we are special
- SaaS TCO missing headcount
- No exit strategy for vendor lock-in

---

## Q063: Tech Debt ICE Score

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

How prioritize technical debt in an executive presentation mock?

### Short Answer (30 seconds)

Categorize (reliability, security, velocity, cost); ICE or risk×effort; tie to incidents and dollars; ask for bounded capacity (e.g., 20%) with 90-day measurable outcomes.

### Detailed Answer (3–5 minutes)

**Categories:**
1. Reliability — deploy time, outage correlation
2. Security — CVE count, unsupported runtime
3. Velocity — lead time drag from coupling
4. Cost — overprovisioned infra

**Prioritization:** ICE or risk matrix; quick wins + strategic items.

**Ask:** 20% sprint capacity + platform engineers for Q3.

**Metrics:** Deploy frequency, MTTR, CVE count — baseline and 90-day target.

### Architecture Perspective

Tech debt presentations must speak executive — incidents and dollars.

### Follow-up Questions

1. **Interest vs principal? — Interest = ongoing cost; principal = paydown effort.**
2. **Stop-the-line debt? — Critical CVEs may preempt features.**

### Common Mistakes in Interviews

- Complaint list without prioritization
- No metrics to prove improvement
- Asking 100% capacity for debt

---

## Q064: Now Next Later Roadmap

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

How structure a 3-year architecture roadmap for whiteboard mocks?

### Short Answer (30 seconds)

Horizon 1 stabilize (0–12mo), H2 scale (12–24mo), H3 innovate (24–36mo). Link capabilities to business OKRs; show dependencies between initiatives.

### Detailed Answer (3–5 minutes)

**Year 1 — Foundation:** Observability, CI/CD golden path, identity standardization.

**Year 2 — Scale:** Multi-region, event hub, self-service portal.

**Year 3 — Optimize:** FinOps automation, cell-based blast radius.

**Mapping:** Each initiative → OKR (time-to-market, uptime 99.95%).

**Dependencies:** Identity before zero-trust; observability before SLO scaling.

**Communication:** Now/Next/Later board for stakeholders.

### Architecture Perspective

Roadmap mocks test strategic sequencing — not technology laundry lists.

### Follow-up Questions

1. **Theme vs project? — Themes for flexibility; committed projects for near term.**
2. **Re-baseline when? — Quarterly on acquisition or market shift.**

### Common Mistakes in Interviews

- Everything in year 1
- No dependency arrows
- No business outcome linkage

---

## Q065: Vendor POC Scope

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

How scope a vendor evaluation POC in an observability platform mock?

### Short Answer (30 seconds)

20 representative services, 2 weeks, weighted criteria scorecard, security review, TCO at scale, reference calls — success metrics defined before POC starts.

### Detailed Answer (3–5 minutes)

**Criteria (example weights):** Cloud integration 20%, K8s APM 20%, cost at scale 20%, SIEM export 15%, UX 10%, support 15%.

**POC success:** 99% trace coverage, <5min alert latency, ingest cost model validated.

**Security:** Data residency, SSO, pen test results.

**Portable telemetry:** OpenTelemetry instrumentation regardless of vendor choice.

### Architecture Perspective

Vendor eval mocks prove structured procurement — not brand preference.

### Follow-up Questions

1. **Build vs buy observability? — Rarely build at 500+ services.**
2. **Negotiation leverage? — Competitive quote even if staying incumbent.**

### Common Mistakes in Interviews

- POC on toy app only
- Ignore ingest cost at scale
- Single quote without comparison

---

## Q066: Internal SLA Error Budget

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

How negotiate internal platform SLA with error budget in a mock?

### Short Answer (30 seconds)

Platform commits SLO (uptime, ack time); product squads commit standards (golden path, limits, runbooks). Error budget policy when burned — freeze changes, focus reliability.

### Detailed Answer (3–5 minutes)

**Platform SLOs:** Control plane 99.9%, node pool 99.95%, P1 ack 15 min.

**Squad obligations:** Golden path templates, pod limits, incident cooperation.

**Error budget:** ~43 min/month at 99.9% — if burned, reliability sprint.

**Exclusions:** Customer DNS, misconfigured manifests — documented.

**Review:** Quarterly with metrics dashboard.

### Architecture Perspective

SLA negotiation tests bilateral accountability — not one-sided guarantees.

### Follow-up Questions

1. **Internal vs customer SLA? — Internal enables customer SLA — cascade requirements.**
2. **Penalty without error budget? — Blame culture — pair SLO with budget policy.**

### Common Mistakes in Interviews

- Vague best-effort commitment
- No squad responsibilities
- SLA without measurement method

---

## Q067: Team Topologies Modes

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

What Team Topologies interaction modes apply in a platform org mock?

### Short Answer (30 seconds)

Platform as X-as-a-Service, enabling team facilitation, complicated-subsystem collaboration, stream-aligned ownership. Avoid platform ticket-queue bottleneck.

### Detailed Answer (3–5 minutes)

**Modes:**
- **X-as-a-Service** — Platform provides self-service APIs/portal
- **Facilitation** — Enabling team rotates to upskill streams
- **Collaboration** — Complex subsystem (payments, identity) pairs with streams

**Structure example:** Platform 8, Enabling 3, Complicated subsystem 4, Streams 15×6.

**Anti-pattern:** 2-week platform ticket queue — embed enablers instead.

### Architecture Perspective

Team topology mock connects org design to deliverability.

### Follow-up Questions

1. **Platform as product? — Internal devs are customers — NPS, roadmap.**
2. **Conway alignment? — Service boundaries match team ownership where possible.**

### Common Mistakes in Interviews

- Central ticket queue bottleneck
- Stream teams own cluster upgrades
- Topology without interaction modes

---

## Q068: Inverse Conway Maneuver

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

What is the inverse Conway maneuver and when recommend it?

### Short Answer (30 seconds)

Deliberately reshape team structure to match desired architecture boundaries — reorg to stream-aligned teams before or alongside service extraction.

### Detailed Answer (3–5 minutes)

**Problem:** 12 services, 4 layer-based teams → every feature crosses 3 teams.

**Inverse Conway:** Reorganize to Checkout, Catalog, Fulfillment streams owning vertical slices.

**If reorg impossible:** Service owner DRI per service, weekly cross-team sync, API contracts.

**Quantify:** Collaboration tax via lead time data in ADR.

**Change management:** Executive sponsor, phased reorg, communication plan.

### Architecture Perspective

Conway mock tests org-technical feedback loop awareness.

### Follow-up Questions

1. **Melvin Conway 1968? — Organizations design systems mirroring communication structure.**
2. **Service owner without team change? — Interim pattern with explicit collaboration tax.**

### Common Mistakes in Interviews

- 12 services 4 teams no interaction plan
- Reorg proposal without change management
- Ignore communication overhead in estimates

---

## Q069: Platform ROI Model

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

How model ROI for an internal developer platform pitch mock?

### Short Answer (30 seconds)

Pain (DORA, survey NPS), vision (golden path), team size, engineer-hours saved × loaded rate, adoption milestones, risk of low adoption with enabling team mitigation.

### Detailed Answer (3–5 minutes)

**ROI example:**
- 200 engineers × 2 hr/week saved × $75/hr × 50 weeks = $1.5M/yr
- Team: 6 platform engineers + 1 PM
- Milestones: Q1 portal MVP, Q2 50% adoption

**Metrics:** Deployment frequency, lead time, platform adoption %.

**Risk:** Adoption — embed enabling team in pilot squads.

**Thin start:** One golden path language first.

### Architecture Perspective

Platform pitch is internal sales — quantify developer time.

### Follow-up Questions

1. **Platform PM needed? — Yes at 200+ engineers.**
2. **Thinnest viable platform? — One path done well beats five half-built.**

### Common Mistakes in Interviews

- Build everything before pilot
- ROI without baseline DORA
- Platform disconnected from stream pain

---

## Q070: NPV Sensitivity Analysis

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

How present cost-benefit with sensitivity in a cloud migration mock?

### Short Answer (30 seconds)

3-year TCO, CAPEX→OPEX shift, stated assumptions, ±30% sensitivity on run rate, phased proceed (dev/test first), include egress and staffing.

### Detailed Answer (3–5 minutes)

**Costs:** Migration project, cloud run rate, training, contract exit penalties.

**Benefits:** HW maintenance saved, elastic dev clusters, revenue enablement (assumption stated).

**NPV:** Positive if key assumptions ≥50% credible.

**Sensitivity:** ±30% cloud run rate; document real options value of phased commit.

**Honesty:** Cloud not always cheaper — show math.

### Architecture Perspective

Cost-benefit mock requires explicit assumptions and sensitivity.

### Follow-up Questions

1. **Stranded on-prem cost? — Datacenter exit penalties in model.**
2. **Real options? — Phase 1 buys learning — defer full commit.**

### Common Mistakes in Interviews

- Cloud always cheaper claim
- Ignore egress and support staffing
- Benefits without credible attribution

---
