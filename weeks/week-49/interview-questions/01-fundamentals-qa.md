# Week 49 — Fundamentals Interview Q&A

> Q001–Q030: Premium format (Week 1 quality).  
> See also: [Interview prep hub](../../../interview-prep/README.md)

---


## Q001: Multi-tenant SaaS Mock Intro

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q002: Acquisition Integration Mock Intro

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q003: Migration Strategy Mock Intro

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q004: Risk Register Mock Intro

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q005: Executive Communication Mock Intro

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q006: Multi-tenant SaaS Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q007: Acquisition Integration Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q008: Migration Strategy Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q009: Risk Register Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q010: Executive Comms Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q011: Stakeholder Map Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q012: Build vs Buy Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q013: Technical Debt Presentation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q014: Architecture Roadmap Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q015: Vendor Evaluation Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q016: SLA Negotiation Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q017: Team Topology Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q018: Conway's Law Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q019: Platform Team Pitch

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q020: Cost-Benefit Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q021: Compliance Gap Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q022: DR Presentation Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q023: Performance Crisis Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q024: Scale 10x Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q025: Legacy Wrap Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q026: API Gateway Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q027: Data Mesh Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q028: Event Storming Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q029: Architecture Principles Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q030: Board Presentation Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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
