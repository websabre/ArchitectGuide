# Week 41 — Expert Scenario Q&A

> Q101–Q120: Premium format (Week 1 quality).

---


## Q101: ADR Deadlock in Merger Program

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Two merged companies have conflicting API gateway standards and both CTOs demand their own pattern. You own architecture governance. What do you do in 30 days?

### Short Answer (30 seconds)

Run a decision program with objective criteria, dual-track pilot evidence, and executive tie-break rules.

### Detailed Answer

**Week 1:** define decision criteria (latency, security controls, operability, migration cost).

**Week 2-3:** run constrained pilots on both standards with same workload profile.

**Week 4:** publish ADR with recommendation, transition strategy, and exception process.

Include a clear sunset timeline for the non-selected standard.

### Architecture Perspective

In high-politics scenarios, evidence-backed process design is as important as technical depth.

### Follow-up Questions

1. **How avoid team split after decision? -> Preserve limited exception path and provide migration support.**
2. **What if pilots are inconclusive? -> Choose based on strategic constraints and set re-evaluation checkpoint.**

### Common Mistakes in Interviews

- Choosing by hierarchy without criteria
- No migration support for losing platform
- Letting both standards proliferate indefinitely

---

## Q102: C4 Drift During Rapid Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Your org doubled microservices in six months and architecture diagrams are now untrusted. Incident reviews cite outdated dependencies. How do you restore confidence?

### Short Answer (30 seconds)

Establish source-controlled C4 baseline plus automated dependency extraction and ownership validation.

### Detailed Answer

Create a canonical system catalog and require each service owner to validate container-level dependencies.

Automate graph extraction from runtime/service mesh metadata where available.

Set architecture freshness SLO for critical domains and enforce via release checklist.

### Architecture Perspective

You are rebuilding architecture as an operational asset, not cosmetic documentation.

### Follow-up Questions

1. **How fast can this be done? -> Prioritize incident-prone domains first, then broaden coverage.**
2. **What metric proves success? -> Reduced incident triage time and dependency ambiguity findings.**

### Common Mistakes in Interviews

- Big-bang redraw with no ownership
- Manual one-time cleanup without automation
- No freshness target or accountability

---

## Q103: Security vs Product Launch Date

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

A strategic launch requires exposing new partner APIs in 4 weeks. Security mandates additional controls that likely add 8 weeks. Leadership asks for compromise. What is your recommendation?

### Short Answer (30 seconds)

Propose phased launch with strict exposure limits, compensating controls, and board-approved residual risk.

### Detailed Answer

Split launch into trusted-partner pilot and general availability.

Add immediate controls: mTLS, strict allowlists, rate limiting, enhanced monitoring, and incident playbook.

Document residual risks in ADR/risk register with hard deadline for full control completion.

### Architecture Perspective

You must preserve launch value while preventing uncontrolled security debt.

### Follow-up Questions

1. **Who signs residual risk? -> Business sponsor with security concurrence.**
2. **How ensure phase 2 happens? -> Tie expansion to gate criteria and executive checkpoint.**

### Common Mistakes in Interviews

- Ship fully open APIs with verbal risk acceptance
- Security asks for all-or-nothing without prioritization
- No measurable gate between phases

---

## Q104: Architecture Board Credibility Crisis

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Teams claim architecture board reviews are inconsistent and political. Delivery leads are bypassing process. How do you repair governance trust?

### Short Answer (30 seconds)

Standardize decision criteria, publish review rubric, and measure fairness and lead-time.

### Detailed Answer

Introduce transparent scoring template and publish anonymized decision examples.

Train reviewers on rubric calibration and conflict-of-interest handling.

Track governance KPIs and run retrospective with engineering managers monthly.

### Architecture Perspective

Trust comes from procedural fairness plus predictable outcomes.

### Follow-up Questions

1. **How handle legacy exceptions? -> Re-baseline them with explicit status and expiry.**
2. **What if board resists transparency? -> Escalate governance charter to executive sponsor.**

### Common Mistakes in Interviews

- Defending process without evidence of consistency
- No published criteria for acceptance
- Ignoring feedback from delivery leadership

---

## Q105: Fitness Functions Not Meeting Reality

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Your architecture fitness checks show green, but production has repeated latency incidents. What likely went wrong and how do you fix governance?

### Short Answer (30 seconds)

Your checks measure proxies, not actual user-path risk; redesign checks around service-level objectives.

### Detailed Answer

Trace incidents to user journeys and identify blind spots (queue contention, dependency timeout chains, regional failovers).

Add synthetic critical-path tests and p95/p99 guardrails tied to real traffic patterns.

Retire vanity checks with low predictive value.

### Architecture Perspective

Fitness functions should correlate with failure modes, not tool convenience.

### Follow-up Questions

1. **How validate improved checks? -> Back-test against recent incident dataset.**
2. **Who owns updates? -> Jointly architecture + SRE + domain teams.**

### Common Mistakes in Interviews

- Adding more checks without relevance analysis
- Ignoring incident postmortems in governance updates
- Thresholds detached from SLO commitments

---

## Q106: Tech Radar Rebellion

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Uncommon |
| **Type** | Scenario |

### Question

A high-performing team wants to adopt a 'hold' technology and claims radar is outdated. Their prototype outperforms current stack by 25%. How do you respond?

### Short Answer (30 seconds)

Run controlled exception trial with explicit metrics and a radar review cycle.

### Detailed Answer

Approve a bounded trial under production guardrails.

Capture evaluation data on performance, operability, hiring impact, and security controls.

If validated, move item to trial/adopt with migration guidance; if not, close exception with rationale.

### Architecture Perspective

Governance must absorb legitimate innovation signals without losing control.

### Follow-up Questions

1. **How avoid exception flood? -> Require evidence plan and sponsor for each request.**
2. **What if radar owner blocks change? -> Use governance charter and escalation path.**

### Common Mistakes in Interviews

- Rejecting data because policy says hold
- Allowing unbounded adoption before evaluation
- No institutional learning after trial outcome

---

## Q107: Regulatory Audit in Six Weeks

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

A regulator requests proof of architecture decision traceability and risk handling in six weeks. Documentation is fragmented. What is your triage plan?

### Short Answer (30 seconds)

Build a control-evidence map from critical systems first, then close highest-risk traceability gaps.

### Detailed Answer

Identify top regulatory scope systems and map: ADR -> control -> implementation evidence.

Create missing links via concise decision records and risk ownership updates.

Run mock audit walkthroughs to surface narrative gaps before formal review.

### Architecture Perspective

Audit readiness is about traceability chain quality under time constraints.

### Follow-up Questions

1. **What gets deprioritized? -> Low-risk systems outside immediate regulatory scope.**
2. **How prevent future scramble? -> Implement ongoing evidence capture workflow post-audit.**

### Common Mistakes in Interviews

- Trying to document everything equally
- No ownership assigned for evidence gaps
- Submitting raw artifacts without coherent narrative

---

## Q108: Data Residency Conflict

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

A global analytics initiative proposes centralizing customer data in one region, but legal flags residency restrictions in key markets. Product says decentralization hurts insight speed. What architecture direction do you choose?

### Short Answer (30 seconds)

Adopt regional data domains with federated analytics and lawful aggregation patterns.

### Detailed Answer

Keep regulated raw data in-region and publish anonymized/aggregated datasets to global analytics plane.

Use policy-tagged pipelines and jurisdiction-aware access controls.

Document constraints and accepted trade-offs in ADR and risk register.

### Architecture Perspective

Balanced architecture protects compliance while preserving analytics value.

### Follow-up Questions

1. **How handle model training centrally? -> Train on de-identified features or federated methods.**
2. **What if insights latency increases? -> Set product expectations and optimize federation pipeline.**

### Common Mistakes in Interviews

- Ignoring legal constraints for speed
- Full data duplication without classification controls
- No cross-functional sign-off

---

## Q109: Executive Wants 'One Diagram'

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

The CEO asks for one architecture diagram for board reporting; engineering needs detailed operational views. How do you satisfy both without conflicting truths?

### Short Answer (30 seconds)

Create layered narrative: executive context view plus linked operational views with shared glossary.

### Detailed Answer

Provide a single board-level map focused on business capabilities, risk posture, and major dependencies.

Link to C4 container/component details for engineering audiences.

Ensure all views derive from same source model to prevent contradictory messaging.

### Architecture Perspective

Different audiences need different abstractions, not different realities.

### Follow-up Questions

1. **How avoid drift between views? -> Generate from shared architecture metadata model.**
2. **How much detail on board slide? -> Risk and investment relevant detail only.**

### Common Mistakes in Interviews

- Using engineering detail dump for executives
- Maintaining separate disconnected diagram sets
- No shared terminology across audience layers

---

## Q110: Post-Decision Failure Spike

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

After adopting a service mesh via ADR, failure rates and latency increased. Team morale is low and leadership questions architecture governance. What do you do?

### Short Answer (30 seconds)

Run structured post-decision review, isolate causal factors, and decide amend vs rollback with objective criteria.

### Detailed Answer

Compare expected benefits versus actual metrics and incident patterns.

Identify whether issues are configuration maturity, platform fit, or organizational readiness.

Publish corrective plan with staged rollback criteria and updated decision record.

### Architecture Perspective

Governance credibility grows when it can course-correct quickly and transparently.

### Follow-up Questions

1. **When rollback? -> If risk exceeds tolerance and remediation path is uncertain in required timeline.**
2. **How communicate to executives? -> Clear accountability, timeline, and risk reduction milestones.**

### Common Mistakes in Interviews

- Defending original decision despite contrary evidence
- Blaming teams without system-level analysis
- No updated ADR after major correction

---

## Q111: Architecture Sign-off Gridlock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Uncommon |
| **Type** | Scenario |

### Question

A release train is blocked because ops, security, and product each insist on different sign-off criteria. Deadline is fixed by contractual obligation. What governance mechanism do you apply?

### Short Answer (30 seconds)

Activate pre-agreed risk-tier sign-off matrix and executive escalation for unresolved high-impact conflicts.

### Detailed Answer

Consolidate criteria into must-have vs deferred with explicit risk ownership.

Timebox dispute resolution and escalate unresolved blockers through chartered decision path.

Record outcome and update sign-off playbook to avoid repeat conflict.

### Architecture Perspective

You need principled escalation, not ad hoc negotiation under pressure.

### Follow-up Questions

1. **How prevent recurrence? -> Publish unified sign-off baseline by risk class.**
2. **What if contract penalties are severe? -> Evaluate controlled release scope reduction over unsafe full launch.**

### Common Mistakes in Interviews

- Trying to satisfy all parties fully under impossible timeline
- No documented tie-break authority
- Reusing unclear criteria next release

---

## Q112: Architecture Debt Bankruptcy Threat

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Uncommon |
| **Type** | Scenario |

### Question

A portfolio review shows architecture debt consuming 35% of capacity and rising. CFO demands immediate reduction in spend while CTO fears reliability collapse. How do you respond?

### Short Answer (30 seconds)

Segment debt by risk and economics, then execute a targeted retirement and containment strategy.

### Detailed Answer

Classify debt into critical-risk, productivity drag, and cosmetic.

Protect critical-risk remediation while reducing low-value feature churn.

Set debt burn-down targets tied to incident reduction and delivery predictability metrics.

### Architecture Perspective

Debt governance succeeds when translated into business economics and reliability outcomes.

### Follow-up Questions

1. **How communicate to CFO? -> Show debt carrying cost and ROI of remediation slices.**
2. **How reassure CTO? -> Preserve reliability-critical investments with explicit guardrails.**

### Common Mistakes in Interviews

- Uniform budget cuts across all debt classes
- No measurable outcome targets
- Treating debt purely as engineering preference

---

## Q113: Threat Model Ownership Gap

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

STRIDE workshop identified major risks, but six weeks later no mitigations are implemented because teams dispute ownership. What governance fix do you apply?

### Short Answer (30 seconds)

Bind risks to service ownership at decision time and enforce closure tracking in delivery governance.

### Detailed Answer

Each threat mitigation must map to accountable owner, due date, and verification evidence.

Integrate risk closure status into release readiness and leadership scorecards.

Escalate overdue high-risk controls with exception sign-off.

### Architecture Perspective

Threat modeling without ownership is theater; ownership makes it real.

### Follow-up Questions

1. **Who verifies closure quality? -> Security partner plus system owner.**
2. **How avoid overload? -> Prioritize by exploitability and blast radius.**

### Common Mistakes in Interviews

- Capturing threats without backlog linkage
- Shared ownership with no accountable owner
- No verification of implemented controls

---

## Q114: Platform Standard Migration Rebellion

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

You mandate a new logging and observability standard, but legacy teams claim migration will hurt delivery targets. Leadership wants both compliance and speed. What plan do you execute?

### Short Answer (30 seconds)

Adopt risk-tiered migration waves with automation support and temporary exception governance.

### Detailed Answer

Prioritize high-risk services first.

Provide migration accelerators (templates, tooling, office hours) and set realistic milestones.

Use temporary exceptions with expiry and measurable reduction plan.

### Architecture Perspective

Standards adoption is organizational change management, not a memo.

### Follow-up Questions

1. **How prove value early? -> Publish incident diagnostic improvements from early adopters.**
2. **What if a team misses deadlines? -> Trigger escalation and adjust support, not silent extension.**

### Common Mistakes in Interviews

- One deadline for all services regardless of risk
- No migration tooling investment
- Permanent exceptions without roadmap

---

## Q115: Board Requests Cost-Cut Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

The board asks for 20% cloud cost reduction while product insists no performance degradation. Existing architecture has idle headroom and over-provisioned DR. How do you govern decisions?

### Short Answer (30 seconds)

Create a cross-functional architecture-finops review with guardrail metrics and phased optimization ADRs.

### Detailed Answer

Define non-negotiable SLO/SLA guardrails.

Prioritize right-sizing, commitment optimization, and tiered DR adjustments with rollback plans.

Approve changes only with before/after metrics and risk acceptance for residual exposure.

### Architecture Perspective

Cost optimization must be architecture-governed to avoid hidden reliability regressions.

### Follow-up Questions

1. **Who owns guardrails? -> SRE, FinOps, and product jointly.**
2. **How report progress? -> Weekly savings vs risk scorecard with incident correlation.**

### Common Mistakes in Interviews

- Cutting spend by disabling resilience blindly
- No performance guardrails during optimization
- Savings claimed without validated baselines

---

## Q116: Executive Demands AI Tool Adoption

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Uncommon |
| **Type** | Scenario |

### Question

Executives mandate rapid adoption of an AI design-assistant tool, but security and legal have unresolved concerns. Teams already started using it informally. What governance response is practical?

### Short Answer (30 seconds)

Issue temporary controlled-use policy, run rapid risk assessment, and formalize approved usage boundaries.

### Detailed Answer

Define allowed data classes, retention policies, and prohibited workflows immediately.

Run a 2-4 week review with security/legal/architecture and publish permanent policy + reference patterns.

Add monitoring and training to reduce shadow usage.

### Architecture Perspective

Pragmatic governance channels inevitable adoption into manageable risk.

### Follow-up Questions

1. **How handle existing informal usage? -> Require disclosure and remediation where policy violated.**
2. **What if tool is banned? -> Provide sanctioned alternatives to avoid productivity collapse.**

### Common Mistakes in Interviews

- Ignoring shadow adoption realities
- All-or-nothing policy with no transition
- No clear communication to engineering teams

---

## Q117: Distributed Ownership Incident

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

A major outage spans three domains and no team agrees who owns the integration architecture. Leadership asks for a permanent governance fix. What do you propose?

### Short Answer (30 seconds)

Define end-to-end capability ownership model with explicit integration accountability.

### Detailed Answer

Map critical business capabilities to accountable architecture owners.

Create interface ownership contracts and shared reliability objectives across domains.

Require cross-domain design reviews for high-risk integration changes.

### Architecture Perspective

Complex systems fail at seams; governance must assign seam ownership.

### Follow-up Questions

1. **How enforce shared reliability objectives? -> Tie them to service-level reporting and leadership reviews.**
2. **What artifact updates are needed? -> C4 context/container maps and interface catalog ownership fields.**

### Common Mistakes in Interviews

- Assuming shared ownership means no owner
- No governance for cross-domain changes
- Incident review without structural accountability changes

---

## Q118: Review Board Scope Creep

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Uncommon |
| **Type** | Scenario |

### Question

Your architecture board now reviews hiring plans, sprint metrics, and coding style disputes. Critical design decisions are delayed. How do you reset the operating model?

### Short Answer (30 seconds)

Refocus charter on architecture risk decisions and delegate non-architecture concerns.

### Detailed Answer

Redefine board mandate and publish in governance handbook.

Create referral paths for engineering excellence and delivery management topics.

Track decision throughput and backlog age for architecture-critical items.

### Architecture Perspective

Clear scope boundaries protect governance effectiveness.

### Follow-up Questions

1. **How get buy-in for scope reset? -> Share delay impact data and executive sponsor alignment.**
2. **What to do with existing backlog? -> Re-triage and route non-architecture items immediately.**

### Common Mistakes in Interviews

- Trying to optimize all governance topics in one forum
- No measurable service level for board decisions
- Keeping low-value agenda items for 'visibility'

---

## Q119: Zero-Trust Program Stalls

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Zero-trust architecture program is behind schedule because teams argue controls are impractical for legacy systems. Regulators have set deadlines. What is your architecture governance strategy?

### Short Answer (30 seconds)

Apply risk-tiered control baselines with legacy transition architecture and compensating controls.

### Detailed Answer

Define minimum enforceable controls now (identity hardening, segmentation, logging) and staged controls for legacy modernization.

Track exceptions with expiry and regulator-facing evidence plan.

Use reference implementation teams to accelerate adoption patterns.

### Architecture Perspective

You need credible progress under regulatory pressure, not perfect-state paralysis.

### Follow-up Questions

1. **How communicate to regulators? -> Show control roadmap, current coverage, and exception governance.**
2. **What if a legacy app cannot comply in time? -> Implement compensating controls and formal risk acceptance.**

### Common Mistakes in Interviews

- Waiting for full modernization before any control rollout
- No exception expiry or transparency
- No regulator-ready evidence narrative

---

## Q120: Acquisition Architecture Integration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Uncommon |
| **Type** | Scenario |

### Question

Your company acquires a startup with different cloud stack, weak docs, and tribal architecture knowledge. You must define a 90-day governance integration plan. What do you do?

### Short Answer (30 seconds)

Stabilize risk first, then converge standards through targeted ADRs and capability mapping.

### Detailed Answer

First 30 days: document critical systems, dependencies, and top risks.

Days 30-60: decide boundary architecture and security baselines via ADRs.

Days 60-90: execute prioritized standardization/migration backlog with exception governance.

### Architecture Perspective

Integration succeeds when you sequence by risk and business continuity, not purity.

### Follow-up Questions

1. **What should not be rushed? -> Core customer workflows and compliance controls.**
2. **How avoid cultural rejection? -> Include acquired team leads in decision forums.**

### Common Mistakes in Interviews

- Immediate full-stack migration mandate
- Ignoring undocumented high-risk dependencies
- No interim governance while integration is underway

---
