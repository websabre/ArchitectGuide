# Week 41 — Advanced Q&A

> Q071–Q100: Premium format (Week 1 quality).

---


## Q071: ADR Scope and Lifecycle

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | ADRs |
| **Frequency** | Common |

### Question

How do you define ADR scope so decisions are durable without becoming bureaucratic?

### Short Answer (30 seconds)

Keep ADRs at architecture-boundary decisions, not every code choice, and add an explicit review cadence.

### Detailed Answer (3–5 minutes)

**Scope rule:** write ADRs for decisions that change team autonomy, platform cost, security posture, or integration contracts.

**Lifecycle:** proposed -> accepted -> superseded/deprecated.

**Practice:** add owner, trigger for re-evaluation, and measurable fitness checks so the ADR is testable after adoption.

### Architecture Perspective

Strong architects keep ADR velocity high while preserving decision traceability.

### Follow-up Questions

1. **How many ADRs are too many? -> If engineers avoid reading them, your granularity is too fine.**
2. **Who approves ADRs? -> Decision owner plus affected domain owners, not everyone in the org.**

### Common Mistakes in Interviews

- Writing ADRs for trivial library upgrades
- Treating ADRs as immutable forever
- No status transitions or supersede links

---

## Q072: Conflicting ADR Stakeholders

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | ADRs |
| **Frequency** | Common |

### Question

What do you do when security wants strict controls but product wants faster release in an ADR?

### Short Answer (30 seconds)

Model options with risk and time impact, then choose a phased control set with explicit guardrails.

### Detailed Answer (3–5 minutes)

**Approach:** document two valid paths, quantify risk exposure, and propose staged controls (MVP controls now, advanced controls by milestone).

**Governance:** capture compensating controls and deadline in the ADR acceptance criteria.

This reframes conflict into time-bound risk ownership.

### Architecture Perspective

Trade-offs must be explicit, not hidden under vague wording.

### Follow-up Questions

1. **Who signs residual risk? -> Business owner with security concurrence.**
2. **How avoid infinite debate? -> Use decision deadline and escalation matrix.**

### Common Mistakes in Interviews

- Letting the loudest stakeholder win
- No quantified risk or timeline
- Accepting 'temporary' exceptions with no expiry

---

## Q073: ADR Quality Gates

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | ADRs |
| **Frequency** | Uncommon |

### Question

How would you enforce ADR quality in a growing architecture team?

### Short Answer (30 seconds)

Use a lightweight template plus PR checks for required sections and measurable consequences.

### Detailed Answer (3–5 minutes)

**Minimum template:** context, options considered, decision, consequences, rollback trigger.

**Automation:** CI lint verifies status, date, owner, and links to impacted systems.

**Review:** architecture guild samples recent ADRs monthly for clarity and outcome tracking.

### Architecture Perspective

Good governance is mostly consistency and discoverability.

### Follow-up Questions

1. **Should ADRs block deploys? -> Only for pre-defined high-impact change classes.**
2. **How measure ADR usefulness? -> Count supersede quality and post-decision incident correlation.**

### Common Mistakes in Interviews

- Overloading template with 20 mandatory fields
- No discoverability strategy (tags/index)
- No feedback loop after decisions land

---

## Q074: C4 Context Boundaries

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | C4 Model |
| **Frequency** | Very Common |

### Question

In C4 level 1 and 2, how do you avoid unclear system boundaries in a platform with shared services?

### Short Answer (30 seconds)

Name ownership and trust boundaries first, then map integrations by contract not team chart.

### Detailed Answer (3–5 minutes)

**Context view:** show external actors and upstream/downstream systems.

**Container view:** show runtime units with data and trust boundaries.

For shared services, annotate ownership and SLA tier to avoid fake cohesion.

### Architecture Perspective

C4 quality depends on clear ownership signals as much as diagrams.

### Follow-up Questions

1. **When to split a system in C4? -> When release cadence or risk profile diverges materially.**
2. **How show vendor SaaS? -> External system with integration and data classification notes.**

### Common Mistakes in Interviews

- Drawing by org chart instead of contracts
- Mixing deployment details into level 1
- Omitting trust boundaries in security-sensitive systems

---

## Q075: C4 and Runtime Reality

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | C4 Model |
| **Frequency** | Common |

### Question

How do you keep C4 diagrams honest when runtime topology changes frequently?

### Short Answer (30 seconds)

Generate from source metadata where possible and review diagrams in release checkpoints.

### Detailed Answer (3–5 minutes)

Use diagram-as-code for stable structure and overlay dynamic runtime snapshots for drift checks.

Include version stamp and last validated date.

Treat stale diagrams as defects in architecture governance, not documentation debt.

### Architecture Perspective

Architecture communication fails when diagrams are aspirational instead of operational.

### Follow-up Questions

1. **What can be auto-generated? -> Service dependencies, deployment nodes, interface catalogs.**
2. **How handle ephemeral infra? -> Model patterns/classes of nodes, not every ephemeral instance.**

### Common Mistakes in Interviews

- Manual diagrams updated quarterly at best
- No ownership for diagram upkeep
- Using one mega-diagram for all audiences

---

## Q076: Architecture Review Depth

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Reviews |
| **Frequency** | Very Common |

### Question

What separates a superficial architecture review from a decision-grade one?

### Short Answer (30 seconds)

Decision-grade reviews test alternatives, risks, and non-functional evidence, not just slide quality.

### Detailed Answer (3–5 minutes)

**Checklist:** option comparison, NFR impact, threat model touchpoint, operational readiness, rollback plan.

Require evidence artifacts (load test, threat assumptions, cost estimate).

Outcome should be a decision with conditions, not a vague endorsement.

### Architecture Perspective

Review rigor is about evidence quality and decision clarity.

### Follow-up Questions

1. **Who must attend? -> Decision owner, domain reps, security, operations, and cost owner as needed.**
2. **How long should it take? -> Timebox prep and review; depth scales with blast radius.**

### Common Mistakes in Interviews

- Reviewing only happy-path architecture
- No explicit accept/reject criteria
- No follow-up tracking on review conditions

---

## Q077: Review Board Anti-Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Governance |
| **Frequency** | Common |

### Question

How can architecture review boards become delivery bottlenecks, and how do you fix it?

### Short Answer (30 seconds)

Move from central approval theater to risk-tiered reviews with delegated authority.

### Detailed Answer (3–5 minutes)

Define change tiers (low/medium/high risk) and route only high-risk items to full board.

Publish standards and pre-approved patterns so most teams self-serve.

Measure lead time added by governance and cap it with SLOs.

### Architecture Perspective

Governance should reduce enterprise risk without centralizing all decisions.

### Follow-up Questions

1. **What metrics prove improvement? -> Review cycle time, exception count, incident correlation.**
2. **How keep standards current? -> Quarterly ratification with platform and product input.**

### Common Mistakes in Interviews

- Board reviews every PR-like change
- Standards with no ownership
- No service-level objective for governance itself

---

## Q078: STRIDE at System Boundaries

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Security |
| **Frequency** | Common |

### Question

How do you apply STRIDE effectively to a distributed architecture?

### Short Answer (30 seconds)

Run STRIDE per trust boundary and high-risk data flow, not as a generic brainstorm.

### Detailed Answer (3–5 minutes)

For each boundary, map spoofing/tampering/repudiation/info disclosure/DoS/elevation risks and controls.

Prioritize by exploitability and impact.

Tie outcomes to backlog items and residual risk register entries.

### Architecture Perspective

Threat modeling becomes valuable only when tied to implementable controls.

### Follow-up Questions

1. **How often repeat STRIDE? -> At major design changes and pre-release of sensitive features.**
2. **Who owns mitigations? -> Service owner with security partner review.**

### Common Mistakes in Interviews

- Running STRIDE once then shelving it
- No control ownership after workshop
- Ignoring operational abuse cases (rate limits, alerting)

---

## Q079: Fitness Functions for Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Governance |
| **Frequency** | Common |

### Question

What are architecture fitness functions and where do they fit in governance?

### Short Answer (30 seconds)

They are automated or reviewable checks that continuously validate architecture characteristics.

### Detailed Answer (3–5 minutes)

Examples: p95 latency budget, dependency rule checks, mandatory encryption checks, and blast-radius constraints.

Integrate in CI/CD and scorecard dashboards.

Fitness functions convert architecture principles into enforceable outcomes.

### Architecture Perspective

Modern architecture governance is test-driven, not meeting-driven.

### Follow-up Questions

1. **Can all fitness functions be automated? -> No; combine automated checks with scheduled review gates.**
2. **Who defines thresholds? -> Architects with SRE/security/product owners based on SLOs and risk appetite.**

### Common Mistakes in Interviews

- Defining principles with no measurable criteria
- Unrealistic thresholds teams cannot meet
- No exception path for temporary deviations

---

## Q080: Tech Radar Adoption Model

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Governance |
| **Frequency** | Uncommon |

### Question

How should an architecture tech radar influence engineering choices without becoming rigid policy?

### Short Answer (30 seconds)

Use it as directional guidance with rationale and expiry dates, not as an absolute ban list.

### Detailed Answer (3–5 minutes)

Classify items into adopt/trial/assess/hold.

Each entry should include business context, observed outcomes, and re-review window.

Link radar updates to architecture incidents and migration learnings to stay credible.

### Architecture Perspective

A useful radar is transparent, evidence-backed, and revisited often.

### Follow-up Questions

1. **Who curates radar entries? -> Cross-functional guild with rotating practitioners.**
2. **How enforce 'hold' items? -> Through review gates for high-risk use, not blanket policing.**

### Common Mistakes in Interviews

- Publishing radar with no rationale
- Never retiring stale entries
- Treating radar as static enterprise law

---

## Q081: Decision Logs vs ADRs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Documentation |
| **Frequency** | Common |

### Question

When do you use decision logs versus full ADRs?

### Short Answer (30 seconds)

Use logs for low-impact tactical choices and ADRs for strategic or cross-team architecture commitments.

### Detailed Answer (3–5 minutes)

Decision logs capture quick context and owner in a lightweight registry.

Escalate to ADR when impact crosses team boundaries, budget, security posture, or long-term maintainability.

This keeps documentation proportional to decision risk.

### Architecture Perspective

Right-sized documentation is key to sustained adoption.

### Follow-up Questions

1. **How promote log entry to ADR? -> Define trigger criteria and link records bidirectionally.**
2. **Can logs replace ADRs? -> Not for high-stakes decisions needing alternatives analysis.**

### Common Mistakes in Interviews

- Everything as ADR causing process fatigue
- Unstructured logs with no searchability
- No linkage between logs and implementation artifacts

---

## Q082: Architecture Principles in Conflict

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Governance |
| **Frequency** | Common |

### Question

What do you do when architecture principles conflict, like 'buy over build' versus data sovereignty needs?

### Short Answer (30 seconds)

Treat principles as weighted heuristics, then document exception rationale with expiry and owner.

### Detailed Answer (3–5 minutes)

Create a principle hierarchy per domain and identify non-negotiables (e.g., legal/regulatory).

For conflicts, run a trade-off matrix and capture exception terms in ADR.

Schedule post-decision review to validate whether the exception should persist.

### Architecture Perspective

Principles guide decisions; they should not prevent context-sensitive judgment.

### Follow-up Questions

1. **How avoid principle sprawl? -> Keep a curated set with practical examples.**
2. **Who approves principle exceptions? -> Domain architect plus risk/compliance owner.**

### Common Mistakes in Interviews

- Treating all principles as equally absolute
- No expiry on principle exceptions
- Principles written without operational examples

---

## Q083: NFR Prioritization Under Budget

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | NFRs |
| **Frequency** | Very Common |

### Question

How do you prioritize NFRs when budget allows only partial implementation?

### Short Answer (30 seconds)

Translate NFRs into business risk and sequence controls by impact reduction per cost.

### Detailed Answer (3–5 minutes)

Use a risk-cost matrix with clear thresholds for availability, security, performance, and compliance.

Classify must-have vs deferred enhancements.

Document deferred NFR debt with trigger events that force revisit.

### Architecture Perspective

Architects must make NFR trade-offs explicit and auditable.

### Follow-up Questions

1. **How communicate deferred NFR risk? -> Executive summary with quantified blast radius and mitigation timeline.**
2. **What if product pushes back? -> Negotiate scope with formal risk acceptance path.**

### Common Mistakes in Interviews

- Treating all NFRs as equally critical
- Deferring NFRs with no mitigation plan
- No stakeholder sign-off on accepted risk

---

## Q084: Risk Register Design Quality

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Risk Management |
| **Frequency** | Common |

### Question

What makes an architecture risk register actually useful?

### Short Answer (30 seconds)

Clear risk statements, owner, probability-impact score, mitigation, contingency, and review date.

### Detailed Answer (3–5 minutes)

Use concise 'if-then' risk phrasing and tie each item to architecture decisions.

Track trend over time, not just static status.

Close risks only when control evidence exists, not when attention shifts.

### Architecture Perspective

Risk registers fail when they become compliance theater instead of decision tools.

### Follow-up Questions

1. **How often review? -> Monthly for active programs; more often for critical releases.**
2. **Should risks map to incidents? -> Yes, to validate scoring quality and blind spots.**

### Common Mistakes in Interviews

- Generic risks with no owner
- No link between risk and decisions
- Marking risks closed without validation evidence

---

## Q085: Post-Decision Architecture Review

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Reviews |
| **Frequency** | Uncommon |

### Question

Why run post-decision reviews after an ADR is implemented?

### Short Answer (30 seconds)

To verify assumptions, detect side effects, and improve future decision quality.

### Detailed Answer (3–5 minutes)

Run 30-90 days after rollout.

Compare predicted vs actual metrics: latency, incidents, change failure rate, and cost.

Capture lessons and update ADR status (confirmed, amended, or superseded).

### Architecture Perspective

Feedback loops are what turn architecture into a learning system.

### Follow-up Questions

1. **Who attends post-review? -> Decision owner, affected teams, ops, and business sponsor.**
2. **What if outcome is mixed? -> Keep decision with compensating actions or plan phased supersession.**

### Common Mistakes in Interviews

- Never checking if decision assumptions held
- Treating review as blame session
- No metric baseline before rollout

---

## Q086: Executive Architecture Summary

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Communication |
| **Frequency** | Common |

### Question

How do you present architecture decisions to executives without losing technical truth?

### Short Answer (30 seconds)

Lead with business outcome, key risks, options considered, and decision confidence.

### Detailed Answer (3–5 minutes)

Use one-page structure: objective, options, recommendation, cost/risk timeline, and ask.

Keep technical appendix separate for engineering depth.

State residual risk plainly and who owns it.

### Architecture Perspective

Executive communication is a core architecture skill, not optional polish.

### Follow-up Questions

1. **How much technical detail is enough? -> Enough to justify risk and investment choices.**
2. **How show uncertainty? -> Include confidence level and decision checkpoints.**

### Common Mistakes in Interviews

- Dumping deep diagrams without business framing
- Hiding residual risks to gain quick approval
- No explicit decision request at the end

---

## Q087: Architecture Sign-off Criteria

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Governance |
| **Frequency** | Common |

### Question

What should be true before architecture sign-off on a critical program?

### Short Answer (30 seconds)

Decision artifacts, threat/risk review, NFR evidence plan, and operational ownership must be complete.

### Detailed Answer (3–5 minutes)

Minimum gate: ADRs accepted, key risks owned, threat model reviewed, SLO/SLI defined, rollback strategy tested, and cost envelope approved.

Sign-off should include explicit assumptions and validity period.

### Architecture Perspective

Sign-off is a risk transfer event; criteria must be objective.

### Follow-up Questions

1. **Who signs? -> Architecture owner plus delegated security/ops/compliance stakeholders.**
2. **How avoid sign-off delays? -> Publish gate checklist early and track readiness continuously.**

### Common Mistakes in Interviews

- Late checklist surprises right before release
- Sign-off based on verbal confidence only
- No expiry or revalidation trigger

---

## Q088: Diagram Tooling Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Documentation |
| **Frequency** | Uncommon |

### Question

How do you choose diagram tooling across a large engineering organization?

### Short Answer (30 seconds)

Prioritize version control, automation compatibility, and audience accessibility over aesthetics.

### Detailed Answer (3–5 minutes)

Use diagram-as-code for architecture and workflow artifacts that must evolve with code.

Allow visual tools for workshops but require source-controlled exports.

Standardize metadata tags for ownership and last validation date.

### Architecture Perspective

Tool sprawl hurts consistency more than it helps creativity.

### Follow-up Questions

1. **Should one tool be mandatory? -> Usually one default plus approved exceptions works best.**
2. **How prevent stale diagrams? -> CI reminders and release readiness checks for critical assets.**

### Common Mistakes in Interviews

- Tool decisions based only on preference
- No source-controlled architecture artifacts
- No conventions for naming and metadata

---

## Q089: Architecture Checklist Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Governance |
| **Frequency** | Common |

### Question

What makes an architecture checklist effective rather than bureaucratic?

### Short Answer (30 seconds)

Short, risk-focused checks with evidence links and clear pass/fail intent.

### Detailed Answer (3–5 minutes)

Limit checklist to high-signal questions covering security, reliability, data governance, and operability.

Every item should map to a real incident pattern or policy requirement.

Review and prune quarterly to avoid checklist bloat.

### Architecture Perspective

Good checklists accelerate judgment; bad ones replace it.

### Follow-up Questions

1. **How many items is ideal? -> Enough to catch common failures without killing momentum.**
2. **Who owns updates? -> Architecture governance group with SRE and security input.**

### Common Mistakes in Interviews

- Checklist with vague yes/no prompts
- No evidence required to pass items
- Growing checklist never retired

---

## Q090: Multi-Team Decision Rights

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Governance |
| **Frequency** | Common |

### Question

How do you avoid decision paralysis when multiple platform and product teams are affected?

### Short Answer (30 seconds)

Define decision rights up front with RAPID/RACI and escalation deadlines.

### Detailed Answer (3–5 minutes)

Assign decision-maker, recommenders, and consulted parties before design spikes start.

Use decision deadlines and tie-break escalation to avoid endless async loops.

Record dissent and rationale in decision logs for future context.

### Architecture Perspective

Clarity of decision rights is often more valuable than perfect consensus.

### Follow-up Questions

1. **How to handle unresolved dissent? -> Capture it explicitly and proceed with accountable owner decision.**
2. **When escalate to executive level? -> Cross-domain budget/legal risk without local resolution.**

### Common Mistakes in Interviews

- Assuming consensus will emerge organically
- No documented owner for final call
- Escalating every disagreement immediately

---

## Q091: Architecture Debt Governance

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Risk Management |
| **Frequency** | Uncommon |

### Question

How would you govern architecture debt so it stays visible and actionable?

### Short Answer (30 seconds)

Track debt as risk-bearing work items with impact metrics and retirement targets.

### Detailed Answer (3–5 minutes)

Classify debt into reliability, security, scalability, and maintainability categories.

Attach carrying cost estimates (incident load, lead time drag, cloud waste).

Reserve recurring capacity for debt retirement and report trend monthly.

### Architecture Perspective

Debt without economics becomes invisible; economics makes it prioritizable.

### Follow-up Questions

1. **How estimate debt cost? -> Use proxy metrics like incidents, MTTR, and engineering effort overhead.**
2. **Who owns debt? -> System owner with architecture oversight and portfolio visibility.**

### Common Mistakes in Interviews

- Debt tracked as vague backlog notes
- No retirement targets or dates
- Treating debt as optional forever

---

## Q092: Security Review in Architecture Board

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Security |
| **Frequency** | Common |

### Question

How should security participate in architecture reviews without becoming a blocker?

### Short Answer (30 seconds)

Embed security early with threat-informed checklists and risk-tiered review depth.

### Detailed Answer (3–5 minutes)

Security should review design alternatives and controls, not just final diagrams.

For high-risk flows, require threat model evidence and compensating control plan.

Use pre-approved patterns to reduce repetitive review cycles.

### Architecture Perspective

Shift-left security is collaboration with standards, not late-stage gatekeeping.

### Follow-up Questions

1. **When require dedicated security sign-off? -> Regulated data, external exposure, or high privilege scope.**
2. **How reduce review load? -> Reuse approved reference architectures.**

### Common Mistakes in Interviews

- Security invited only at final release gate
- No documented threat assumptions
- Treating every service with same review depth

---

## Q093: Documentation Operating Model

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Documentation |
| **Frequency** | Uncommon |

### Question

What documentation operating model scales architecture knowledge across many teams?

### Short Answer (30 seconds)

Use layered docs: principle docs, reference architectures, ADRs, and system runbooks with clear ownership.

### Detailed Answer (3–5 minutes)

Define ownership per artifact and review cadence.

Create an architecture index with tagging by domain, compliance scope, and lifecycle status.

Tie documentation freshness to quarterly architecture health checks.

### Architecture Perspective

Scalable architecture docs rely on ownership and discoverability more than writing volume.

### Follow-up Questions

1. **How avoid duplicate docs? -> Set canonical source rules and cross-linking conventions.**
2. **What gets archived? -> Superseded references and retired system artifacts with historical links.**

### Common Mistakes in Interviews

- Single wiki page for entire architecture estate
- No owners for critical docs
- Duplicated guidance across tools without canonical source

---

## Q094: Governance KPIs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Governance |
| **Frequency** | Uncommon |

### Question

Which KPIs indicate architecture governance is working?

### Short Answer (30 seconds)

Use both flow and outcome metrics: decision lead time, exception rate, incident trend, and NFR attainment.

### Detailed Answer (3–5 minutes)

Recommended set: median review turnaround, % changes using approved patterns, high-risk exception closure time, production incidents tied to architecture gaps, and architecture debt trend.

Balance speed and risk, not one or the other.

### Architecture Perspective

If you only measure compliance, teams optimize paperwork not architecture quality.

### Follow-up Questions

1. **How present to leadership? -> Quarterly scorecard with trend and major interventions.**
2. **What metric is dangerous alone? -> Number of reviews completed without outcome quality context.**

### Common Mistakes in Interviews

- No baseline before governance rollout
- Vanity metrics detached from incidents
- No action loop from KPI signals

---

## Q095: Decision Supersession Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | ADRs |
| **Frequency** | Common |

### Question

How do you supersede an old ADR without destabilizing active teams?

### Short Answer (30 seconds)

Publish supersession ADR, migration path, and sunset milestones with compatibility period.

### Detailed Answer (3–5 minutes)

New ADR should explain why prior assumptions changed.

Define coexistence window, backward-compatibility requirements, and support timeline.

Track adoption with explicit migration checkpoints.

### Architecture Perspective

Supersession is change management, not just documentation cleanup.

### Follow-up Questions

1. **Should old ADR be deleted? -> Never; mark status and link superseding decision.**
2. **How enforce migration? -> Tie deadlines to platform support policy and review gates.**

### Common Mistakes in Interviews

- Silent policy changes with no transition plan
- Immediate cutoff with no compatibility window
- No owner assigned for migration progress

---

## Q096: Architecture Narrative for Audits

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Communication |
| **Frequency** | Common |

### Question

How do you prepare architecture evidence for audits without derailing engineering?

### Short Answer (30 seconds)

Continuously capture decision and control evidence so audits become extraction, not reconstruction.

### Detailed Answer (3–5 minutes)

Map architecture artifacts to control objectives (security, availability, data handling).

Automate evidence links from CI/CD, policy checks, and risk register updates.

Keep concise narratives that explain intent plus implementation proof.

### Architecture Perspective

Audit readiness is strongest when built into engineering flow.

### Follow-up Questions

1. **What artifact helps most? -> Traceable link chain from decision to control to runtime evidence.**
2. **How avoid scramble before audit? -> Quarterly mock evidence review.**

### Common Mistakes in Interviews

- Creating evidence only during audit week
- No mapping between controls and architecture artifacts
- Over-reliance on tribal knowledge

---

## Q097: Cross-Border Data Architecture Review

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Risk Management |
| **Frequency** | Uncommon |

### Question

How should architecture governance handle cross-border data constraints in global systems?

### Short Answer (30 seconds)

Model data residency by domain and enforce processing boundaries in design and platform policy.

### Detailed Answer (3–5 minutes)

Decisions should include data classification, region constraints, lawful transfer mechanisms, and incident response implications.

Require legal/compliance sign-off on high-risk data flows.

Track exceptions in risk register with expiration.

### Architecture Perspective

Data governance needs architecture and legal alignment from day one.

### Follow-up Questions

1. **How reflect in C4? -> Annotate trust zones, data stores, and transfer pathways by jurisdiction.**
2. **What if product needs global analytics? -> Use regional aggregation or anonymization strategies with legal review.**

### Common Mistakes in Interviews

- Assuming cloud region equals full compliance
- No explicit data classification ownership
- Unbounded data replication across jurisdictions

---

## Q098: Architecture RFC vs ADR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Documentation |
| **Frequency** | Common |

### Question

When should teams use an RFC before an ADR?

### Short Answer (30 seconds)

Use RFC for exploration and alignment when options are still open; ADR records the final decision.

### Detailed Answer (3–5 minutes)

RFC invites broad feedback and risk discovery.

ADR captures final choice, rationale, and consequences once decision authority is applied.

Link RFC and ADR so history is coherent and auditable.

### Architecture Perspective

Separating exploration from decision keeps records clean and actionable.

### Follow-up Questions

1. **Can RFC be skipped? -> Yes for low-complexity changes with clear precedent.**
2. **How prevent RFC limbo? -> Add decision deadline and owning authority.**

### Common Mistakes in Interviews

- Using ADR as discussion thread
- RFC with no closure criteria
- No linkage between exploratory and final artifacts

---

## Q099: Platform Principle Exceptions

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Governance |
| **Frequency** | Common |

### Question

How do you handle platform standards exceptions requested by a high-priority product team?

### Short Answer (30 seconds)

Allow time-bound exceptions with compensating controls and explicit migration obligations.

### Detailed Answer (3–5 minutes)

Create exception record with business rationale, risk impact, owner, review date, and rollback/migration plan.

Monitor exception drift to avoid de facto policy erosion.

Escalate repeated exceptions as signal to revisit platform standards.

### Architecture Perspective

Exceptions are data; they tell you whether standards are realistic.

### Follow-up Questions

1. **How long can exceptions live? -> Define strict maximum and renewal process.**
2. **Who pays exception cost? -> Requesting domain typically owns extra operational burden.**

### Common Mistakes in Interviews

- Permanent exceptions disguised as temporary
- No review cadence for active exceptions
- No measurement of exception-related incidents

---

## Q100: Architecture Review Readiness Package

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Reviews |
| **Frequency** | Common |

### Question

What should be in a readiness package before formal architecture review?

### Short Answer (30 seconds)

Include context, options, target state, NFR projections, risk register, and migration/rollback strategy.

### Detailed Answer (3–5 minutes)

A strong package includes C4 diagrams, key ADR drafts, dependency map, estimated cost profile, and unresolved decisions.

Call out known unknowns explicitly to focus review time.

This shifts review from discovery to judgment.

### Architecture Perspective

Preparation quality is the best predictor of review quality.

### Follow-up Questions

1. **How big should package be? -> As small as possible while preserving decision-critical evidence.**
2. **Who validates package completeness? -> Review coordinator or architecture PM function.**

### Common Mistakes in Interviews

- Review with only slide deck and no artifacts
- Hiding unknowns to look prepared
- No rollback strategy for risky migrations

---
