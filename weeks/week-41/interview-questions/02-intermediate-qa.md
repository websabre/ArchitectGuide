# Week 41 — Intermediate Q&A

> Q031–Q070: Premium format (Week 1 quality).

---


## Q031: ADR Template Structure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | ADRs |
| **Frequency** | Very Common |

### Question

What sections belong in an enterprise ADR template and why?

### Short Answer (30 seconds)

Status, date, deciders, context, drivers, options, decision, rationale, consequences (positive/negative/risks), compliance, cost, related ADRs. Template ensures every decision is searchable and reviewable.

### Detailed Answer (3–5 minutes)

**Core sections (Michael Nygard + enterprise extensions):**
1. **Metadata** — Status (Proposed/Accepted/Deprecated/Superseded), date, deciders, week/module tag
2. **Context** — Problem forcing the decision
3. **Decision drivers** — NFRs, budget, skills, compliance
4. **Considered options** — Minimum two viable alternatives
5. **Decision** — Chosen option stated plainly
6. **Rationale** — Why this option; explicit trade-offs
7. **Consequences** — Positive, negative, risks + mitigations
8. **Compliance / security** — Data classification, threat notes
9. **Cost implications** — Monthly estimate, FinOps tags
10. **Related ADRs** — Links to superseded or dependent records

**Architect:** Store ADRs in Git (`docs/adr/NNNN-title.md`) with PR review — same rigor as code. Template in repo README prevents blank-slate inconsistency.

### Architecture Perspective

Interviewers test whether you treat ADRs as governance artifacts — not meeting notes.

### Follow-up Questions

1. **ADR vs RFC? — RFC proposes and gathers feedback; ADR records final decision after consensus.**
2. **Numbering scheme? — Sequential ADR-0042 — never reuse numbers when superseding.**

### Common Mistakes in Interviews

- ADR that's one line with no alternatives considered
- Missing status field — can't tell if decision is still valid
- No link to architecture diagrams or cost estimate

---

## Q032: ADR Lifecycle

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | ADRs |
| **Frequency** | Very Common |

### Question

Describe the ADR lifecycle from proposal to deprecation.

### Short Answer (30 seconds)

Proposed → review/comment → Accepted → (optional) Amended → Deprecated or Superseded. Lifecycle is tracked in Git history and decision log; never delete — supersede with new ADR.

### Detailed Answer (3–5 minutes)

**Lifecycle states:**
- **Proposed** — Draft PR open; architecture review scheduled
- **Accepted** — Merged after sign-off; implementation may proceed
- **Deprecated** — Decision no longer recommended but not replaced
- **Superseded by ADR-NNNN** — New ADR replaces old; old remains for audit

**Workflow:**
```
Spike/RFC → Draft ADR PR → Review board → Merge Accepted → Implement → Monitor
                                    ↓
                            Supersede if context changes
```

**Architect:** Set SLA — critical decisions ADR within 5 business days of review. Quarterly ADR health check — flag Accepted ADRs where implementation diverged.

### Architecture Perspective

ADR lifecycle prevents 'ghost decisions' that nobody follows.

### Follow-up Questions

1. **Amend vs supersede? — Supersede preserves history; amend only for clarifications not decision changes.**
2. **Who can accept? — Named deciders in template — usually architect + product + security delegate.**

### Common Mistakes in Interviews

- Deleting old ADRs when decisions change
- Accepted ADR never referenced in implementation tickets
- Proposed ADRs left open for months

---

## Q033: When to Write an ADR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | ADRs |
| **Frequency** | Very Common |

### Question

When should a team write an ADR versus updating a wiki page?

### Short Answer (30 seconds)

Write ADR for significant, hard-to-reverse decisions: technology choice, integration pattern, data ownership, security boundary, multi-year cost commitment. Skip ADR for trivial config or easily reversible choices.

### Detailed Answer (3–5 minutes)

**Write ADR when:**
- Reversing later costs >2 sprints or migration risk
- Multiple teams affected or need alignment
- Compliance/audit trail required
- Options had meaningful trade-offs (build vs buy, sync vs async)
- Decision will be questioned in 12 months

**Skip ADR when:**
- Library patch version bump
- Reversible feature flag default
- Local team coding standard already documented

**Heuristic:** 'Would a new architect ask why we did this?' — yes → ADR.

**Architect:** Publish decision tree in engineering handbook — reduces debate every sprint.

### Architecture Perspective

Knowing when to ADR separates architects from document-everything bureaucrats.

### Follow-up Questions

1. **ADR for NFR targets? — Yes when SLO/error budget policy affects all services.**
2. **Batch ADRs? — Acceptable for related micro-decisions in one ADR with numbered sub-decisions.**

### Common Mistakes in Interviews

- ADR for every npm dependency
- No ADR for database engine choice affecting 5 teams
- Wiki page edited silently without decision record

---

## Q034: ADR vs Design Doc

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Documentation |
| **Frequency** | Very Common |

### Question

Compare ADR vs design doc. When use each?

### Short Answer (30 seconds)

ADR: immutable decision record — what and why, short, permanent. Design doc: working document — how, detailed flows, diagrams, evolves during build. ADR references design doc; design doc links to ADR.

### Detailed Answer (3–5 minutes)

| Artifact | Purpose | Audience | Lifespan |
|----------|---------|----------|----------|
| ADR | Record decision | All engineers, audit | Permanent |
| Design doc | Explain implementation | Build team | Evolves then archived |
| RFC | Gather input pre-decision | Stakeholders | Closes when ADR written |

**Flow:** RFC discussion → ADR Accepted → Design doc for build → Update design doc during sprint; ADR unchanged unless decision reverses.

**Architect:** One ADR may spawn one design doc per service. Don't put decision rationale only in design doc — it gets stale.

### Architecture Perspective

Confusing ADR and design doc causes lost rationale when docs rot.

### Follow-up Questions

1. **C4 in design doc? — Yes — context/container in design doc; ADR links to diagram commit SHA.**
2. **One doc for both? — Anti-pattern — decisions buried in 40-page doc.**

### Common Mistakes in Interviews

- 40-page design doc with no ADR for key fork
- ADR that includes sequence diagrams for every API
- Design doc updated but ADR never superseded when decision changed

---

## Q035: C4 Context Diagram

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | C4 Model |
| **Frequency** | Very Common |

### Question

Explain the C4 context diagram and what belongs on it.

### Short Answer (30 seconds)

Context diagram (Level 1): system as one box, users and external systems as neighbors, relationships labeled with purpose/technology. Shows scope boundary — what you build vs what you integrate.

### Detailed Answer (3–5 minutes)

**Elements:**
- **Your system** — single box (e.g., 'Order Platform')
- **Personas** — Customer, Admin, Support agent
- **External systems** — Payment gateway, ERP, Identity provider
- **Relationships** — 'Places orders via HTTPS', 'Syncs inventory nightly SFTP'

**Rules:**
- No internal databases or microservices — too much detail
- Every external dependency explicit — interviewers probe integration risk
- Include trust direction (inbound/outbound data)

**Architect:** Context diagram is slide 1 for executives and security review — 5–7 boxes max.

### Architecture Perspective

Context diagram answers 'what world does this system live in?'

### Follow-up Questions

1. **Multiple systems on one diagram? — One primary system per diagram; dashed box for enterprise boundary.**
2. **Trust boundaries? — Annotate PCI, PHI, PII flows at context level.**

### Common Mistakes in Interviews

- Microservices shown on context diagram
- Missing external identity provider
- Unlabeled arrows ('uses API')

---

## Q036: C4 Container Diagram

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | C4 Model |
| **Frequency** | Very Common |

### Question

What is a C4 container diagram and how does it differ from context?

### Short Answer (30 seconds)

Container diagram (Level 2): decomposes system into deployable/runtime units — web app, API, database, queue, worker. Shows technology choices and inter-container protocols.

### Detailed Answer (3–5 minutes)

**Containers (C4 sense = deployable units):**
- SPA (React on CDN)
- API Gateway (Azure APIM)
- Order Service (.NET on AKS)
- PostgreSQL (Azure Flexible Server)
- Service Bus (topics/subscriptions)

**Show:** Protocol (HTTPS, AMQP, JDBC), sync vs async, auth mechanism at boundary.

**Not shown yet:** Classes, modules inside container — that's component level.

**Architect:** Container diagram drives team boundaries and deployment pipelines — one container often maps to one repo or one K8s deployment.

### Architecture Perspective

Container diagram is the workhorse for architecture reviews.

### Follow-up Questions

1. **Container vs microservice? — Not 1:1 — one service may be multiple containers (app + sidecar).**
2. **Shared database anti-pattern? — Visible immediately on container diagram — call out in review.**

### Common Mistakes in Interviews

- Class diagrams labeled as C4 container
- Single 'backend' blob hiding 12 services
- No data store on diagram

---

## Q037: C4 Component Diagram — When to Use

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | C4 Model |
| **Frequency** | Common |

### Question

When do you produce C4 component diagrams versus stopping at containers?

### Short Answer (30 seconds)

Component diagram (Level 3) when internal structure affects risk, onboarding, or refactor — complex service, unclear ownership, performance hotspot, or security-critical module boundaries.

### Detailed Answer (3–5 minutes)

**Use component diagram when:**
- Single container >50K LOC or multiple teams inside
- Explaining payment routing, plugin architecture, pipeline stages
- Reviewing coupling before extract-to-service
- Onboarding senior devs to critical domain service

**Skip when:**
- CRUD service with standard controller/service/repository
- POC with 2-week lifetime
- Container is single-purpose lambda

**Components:** Controllers, domain services, repositories, adapters — not every class.

**Architect:** Component diagram is optional in enterprise standards — require only for Tier-1 services.

### Architecture Perspective

Component level is zoom-in for complexity — not mandatory wallpaper.

### Follow-up Questions

1. **Code diagram (Level 4)? — Rare in architecture reviews — auto-gen from IDE if needed.**
2. **UML vs C4 component? — C4 emphasizes runtime dependencies over inheritance.**

### Common Mistakes in Interviews

- Component diagram for every microservice by policy
- 50 classes on one diagram
- Component diagram without linking to container parent

---

## Q038: Architecture Review Checklist

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reviews |
| **Frequency** | Very Common |

### Question

What belongs on an architecture review checklist before production approval?

### Short Answer (30 seconds)

NFRs (availability, latency, RTO/RPO), security (authN/Z, encryption, threat model), scalability, observability, DR, cost estimate, operability, compliance, ADRs complete, runbooks, migration/rollback plan.

### Detailed Answer (3–5 minutes)

**Checklist categories:**
1. **Requirements traceability** — Functional + NFR signed off
2. **Security** — STRIDE summary, secrets management, network segmentation
3. **Data** — Classification, retention, residency, backup
4. **Reliability** — HA pattern, idempotency, retry, circuit breakers
5. **Observability** — Logs, metrics, traces, SLOs, alerts
6. **Operations** — Deploy strategy, feature flags, rollback tested
7. **Cost** — FinOps tags, scale assumptions, budget owner
8. **Governance** — ADRs, RFC comments resolved, legal/privacy review

**Architect:** Tiered checklist — Tier-0 payment path full review; internal tool lightweight subset.

### Architecture Perspective

Checklist makes review repeatable — not ad hoc memory.

### Follow-up Questions

1. **Pre-review vs full review? — Pre-review at RFC; full at production gate.**
2. **Waivers? — Documented exception with expiry and compensating controls.**

### Common Mistakes in Interviews

- Checkbox review without reading diagrams
- Same checklist for POC and payment system
- No security section for external-facing API

---

## Q039: Legacy System Architecture Review

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reviews |
| **Frequency** | Very Common |

### Question

How approach to you review architecture of a legacy system you didn't build?

### Short Answer (30 seconds)

Discovery: stakeholder interviews, production metrics, dependency map, code/repo archaeology, runbooks, incident history. Document as-is C4, risk register, strangler opportunities — no big-bang rewrite recommendation without data.

### Detailed Answer (3–5 minutes)

**Review process:**
1. **Context** — Business criticality, change frequency, incident rate
2. **Discovery** — CMDB, APM traces, DB schemas, batch schedules, tribal knowledge
3. **As-is documentation** — Context + container (even if approximate)
4. **Risk scoring** — Security debt, bus factor, unsupported runtime
5. **Recommendations** — Prioritized: contain, replace, wrap, retire

**Outputs:** Architecture assessment report, ADR for modernization approach, funding ask with ROI.

**Architect:** Treat unknown as risk — 'undocumented integration' is finding, not embarrassment.

### Architecture Perspective

Legacy review is forensic architecture — evidence over assumptions.

### Follow-up Questions

1. **Document as code for legacy? — Export discovered diagram to Git — baseline for drift detection.**
2. **When recommend rewrite? — Only when sustain cost > rewrite cost over 3-year TCO model.**

### Common Mistakes in Interviews

- Recommend cloud lift without understanding batch windows
- Ignore undeclared FTP integrations
- No interview with ops/on-call team

---

## Q040: RFC Process for Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Very Common |

### Question

Design an RFC process for significant architecture changes.

### Short Answer (30 seconds)

RFC template: problem, goals, non-goals, proposals, alternatives, migration, open questions. Time-boxed comment period (5–10 days), facilitator synthesizes, decision → ADR. Async-first with optional review meeting.

### Detailed Answer (3–5 minutes)

**RFC workflow:**
```
Author drafts RFC in Git/Markdown → Announce in #architecture → Comment period
→ Facilitator resolves threads → Decision meeting if needed → ADR merged
```

**Rules:**
- RFC number sequential (RFC-0042)
- Required reviewers by domain (security, data, platform)
- Explicit **non-goals** prevent scope creep
- **Open questions** must be resolved or deferred with owner before ADR

**Architect:** RFCs are proposals — no status 'Accepted' on RFC itself; acceptance lives in ADR.

### Architecture Perspective

RFC democratizes input; ADR records output — don't skip either.

### Follow-up Questions

1. **RFC vs design review meeting? — RFC async for distributed teams; meeting for conflict resolution.**
2. **Stale RFC? — Close as Withdrawn — don't leave ambiguous.**

### Common Mistakes in Interviews

- Decision in Slack never captured in ADR
- RFC with single option — no real decision process
- Unlimited comment period blocking delivery

---

## Q041: Stakeholder Sign-off

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Very Common |

### Question

Who must sign off on architecture decisions and how document sign-off?

### Short Answer (30 seconds)

Sign-off matrix by tier: product owner (scope), lead architect (design), security (threat/compliance), data owner (classification), FinOps (cost), ops (runability). Record in ADR deciders field + PR approvals.

### Detailed Answer (3–5 minutes)

**Tier-0 (customer payment, PHI):**
- Enterprise architect
- CISO delegate
- Product director
- Platform ops lead

**Tier-2 (internal tool):**
- Team architect + product owner

**Mechanism:**
- Git PR approvals = auditable sign-off
- Architecture review board minutes for org-wide decisions
- Exception/waiver form with executive sponsor

**Architect:** Sign-off is accountability — name roles not vague 'stakeholders'.

### Architecture Perspective

Sign-off without named roles creates blame vacuum in incidents.

### Follow-up Questions

1. **Sign-off after deploy? — Retroactive only for emergencies — ADR within 48h.**
2. **Delegated sign-off? — Document delegate in ADR when primary unavailable.**

### Common Mistakes in Interviews

- Verbal OK from VP never recorded
- Security not involved on external data export
- Same sign-off list for all tiers

---

## Q042: Architecture Decision Log

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | ADRs |
| **Frequency** | Very Common |

### Question

What is an architecture decision log and how maintain it?

### Short Answer (30 seconds)

Central index of all ADRs — searchable table with number, title, status, date, domain, owner. Lives in Git README or Backstage catalog; links to full ADR markdown.

### Detailed Answer (3–5 minutes)

**Log columns:**
| ADR | Title | Status | Date | Domain | Supersedes |

**Maintenance:**
- Auto-lint in CI — new ADR must update log index
- Quarterly review — mark Deprecated where code diverged
- Tag by domain (#data, #security, #integration)

**Discovery:** Engineers search log before proposing duplicate decisions.

**Architect:** Decision log is institutional memory — onboarding starts here.

### Architecture Perspective

Decision log turns ADR folder from file pile into navigable registry.

### Follow-up Questions

1. **Backstage integration? — ADR plugin renders log with ownership.**
2. **Cross-repo ADRs? — Central architecture repo with links from service repos.**

### Common Mistakes in Interviews

- ADRs scattered with no index
- Log not updated when status changes to Superseded
- Duplicate ADRs on same topic undetected

---

## Q043: Reversing an ADR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | ADRs |
| **Frequency** | Very Common |

### Question

How do you reverse or supersede an accepted ADR?

### Short Answer (30 seconds)

Never edit Accepted ADR in place for decision change. Write new ADR that supersedes old: explain context change, new options, migration plan. Mark old ADR Superseded with link. Track implementation rollback.

### Detailed Answer (3–5 minutes)

**Supersede process:**
1. New ADR-0050 references ADR-0031 status → Superseded
2. Migration plan: phased, feature flags, dual-write period
3. Update decision log
4. Communicate to affected teams
5. Archive deprecated patterns in linters/docs

**Triggers:** Cost overrun, security incident, scale limit hit, vendor EOL.

**Architect:** Reversal is normal — ADR captures why context changed, not ego protection.

### Architecture Perspective

Superseding preserves audit trail — regulators ask 'why did you change?'

### Follow-up Questions

1. **Deprecated vs superseded? — Deprecated = don't use; superseded = replaced by specific ADR.**
2. **Implementation lag? — ADR Accepted but code still on old pattern — track in tech debt register.**

### Common Mistakes in Interviews

- Silent rewrite of merged ADR file
- Delete ADR-0031 from Git history
- Supersede without migration plan

---

## Q044: NFR Documentation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | NFRs |
| **Frequency** | Very Common |

### Question

How document non-functional requirements in architecture artifacts?

### Short Answer (30 seconds)

NFR matrix: ID, category (performance, security, availability), requirement, metric, measurement method, owner, ADR link. Attach to architecture review package — testable not vague.

### Detailed Answer (3–5 minutes)

**Example NFR rows:**
| ID | Category | Requirement | Target | Verification |
| NFR-01 | Latency | Checkout p99 | <300ms | Load test k6 |
| NFR-02 | Availability | Order API | 99.95% | SLO dashboard |
| NFR-03 | RPO | Order DB | 5 min | DR drill |

**Categories:** Performance, scalability, reliability, security, maintainability, compliance, cost.

**Architect:** NFRs are contract with ops — ambiguous 'fast' fails reviews.

### Architecture Perspective

NFR documentation connects architecture to SLO dashboards and test gates.

### Follow-up Questions

1. **NFR in ADR vs separate doc? — Critical NFRs summarized in ADR; full matrix in review pack.**
2. **Who validates NFRs? — QA/perf engineer signs measurement method.**

### Common Mistakes in Interviews

- 'Highly available' without numeric target
- NFRs never revisited after launch
- No owner per NFR

---

## Q045: Risk Register for Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Risk Management |
| **Frequency** | Very Common |

### Question

Build and maintain an architecture risk register for a program.

### Short Answer (30 seconds)

Risk register: ID, description, likelihood, impact, score, mitigation, owner, status, review date. Link to ADRs, threat model, and compliance gaps. Review monthly in architecture governance.

### Detailed Answer (3–5 minutes)

**Architecture-specific risks:**
- Single point of failure undiscovered
- Vendor lock-in without exit plan
- Skill gap on chosen stack
- Data residency violation
- Underestimated integration failure modes

**Scoring:** 5×5 heat map — score ≥15 requires executive visibility.

**Architect:** Risk register feeds portfolio prioritization — not shelfware.

### Architecture Perspective

Risk register makes trade-offs visible before production incidents.

### Follow-up Questions

1. **Risk vs issue? — Risk = may happen; issue = happening — separate tabs.**
2. **Residual risk acceptance? — Named executive accepts with date.**

### Common Mistakes in Interviews

- Risk register copied from template never updated
- Mitigation 'monitor closely' without action
- No link between STRIDE findings and register

---

## Q046: Threat Modeling with STRIDE

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Apply STRIDE threat modeling in an architecture review.

### Short Answer (30 seconds)

STRIDE per trust boundary crossing: Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege. Data-flow diagram → enumerate threats → mitigations → residual risk.

### Detailed Answer (3–5 minutes)

**Process:**
1. Draw DFD with trust boundaries (Internet, DMZ, data tier)
2. For each element/flow, apply STRIDE checklist
3. Document threat, mitigation (control), verification (test/audit)
4. Feed high threats to risk register

**Example:** API gateway → service: Spoofing → mitigated by mTLS + JWT validation.

**Tools:** Microsoft Threat Modeling Tool, OWASP Threat Dragon.

**Architect:** STRIDE required for Tier-0 and external-facing changes — not optional security checkbox.

### Architecture Perspective

STRIDE connects diagrams to actionable controls.

### Follow-up Questions

1. **STRIDE vs PASTA? — STRIDE faster for component reviews; PASTA for attack-centric programs.**
2. **Repudiation in APIs? — Audit logs, signed transactions, immutable event store.**

### Common Mistakes in Interviews

- STRIDE doc created after production launch
- Generic 'use HTTPS' for every threat
- No verification column — mitigations untested

---

## Q047: Architecture Fitness Functions

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

What are architecture fitness functions and give examples?

### Short Answer (30 seconds)

Automated checks that measure architecture adherence — executable constraints. Examples: dependency rules (no UI→DB direct), cycle detection, API breaking change detector, latency budget in CI, allowed cloud region policy.

### Detailed Answer (3–5 minutes)

**Types:**
- **Static** — ArchUnit, NetArchTest: layer dependencies
- **Dynamic** — Synthetic canary: p99 <200ms after deploy
- **Compliance** — OPA/Rego: all storage encrypted, tags present
- **Evolutionary** — Complexity trend must not increase >5% per quarter

**Architect:** Start with 3–5 fitness functions on critical paths — expand as platform matures.

### Architecture Perspective

Fitness functions encode architecture principles into CI — drift fails build.

### Follow-up Questions

1. **Fitness function vs lint? — Fitness = architectural cross-cutting; lint = code style.**
2. **Who owns? — Platform team maintains; domain teams fix violations.**

### Common Mistakes in Interviews

- Manual architecture reviews only — no automation
- Fitness functions too brittle — teams disable them
- No fitness functions for cloud tag policy

---

## Q048: Technology Radar

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

How use a tech radar in enterprise architecture governance?

### Short Answer (30 seconds)

Radar quadrants (Adopt, Trial, Assess, Hold) per technology — curated quarterly by architecture guild. Guides standards, training budget, and ADR option filtering.

### Detailed Answer (3–5 minutes)

**Process:**
1. Teams nominate technologies with use cases
2. Architecture board evaluates: support, security, skill, TCO
3. Publish radar — visible to all engineering
4. ADRs should prefer Adopt/Trial unless exception documented

**Example:** Kafka = Adopt; New message broker X = Assess; ActiveMQ = Hold (migrate off).

**Architect:** Radar prevents 47 overlapping databases — not a ban list but strong default.

### Architecture Perspective

Tech radar aligns thousands of engineers without central approval bottlenecks.

### Follow-up Questions

1. **Radar vs standards doc? — Radar is directional; standards doc is mandatory rules.**
2. **Exception process? — ADR with Hold technology requires exec waiver.**

### Common Mistakes in Interviews

- Radar never updated — stuck on 2019 entries
- Trial without exit criteria
- Radar created in vacuum without practitioner input

---

## Q049: Architecture Principles

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Very Common |

### Question

Define enterprise architecture principles and how enforce them.

### Short Answer (30 seconds)

Principles: short, memorable, testable statements (e.g., 'API-first', 'Cloud-native by default', 'Privacy by design'). Enforced via standards, fitness functions, review checklist, and training — not posters.

### Detailed Answer (3–5 minutes)

**Example principles:**
1. **Business alignment** — Every system maps to capability model
2. **Reuse before buy before build**
3. **Loose coupling** — Async over sync when possible
4. **Security by default** — Zero trust network
5. **Observable** — No production without metrics/traces

**Enforcement:** Architecture review gates, golden paths, template repos.

**Architect:** 8–12 principles max — more = none remembered.

### Architecture Perspective

Principles guide decisions when ADR options seem equal.

### Follow-up Questions

1. **Principle vs pattern? — Principle is why; pattern is how.**
2. **Conflict between principles? — Document priority in governance (security > cost).**

### Common Mistakes in Interviews

- 40 principles nobody reads
- Principles with no review enforcement
- Principles contradicting actual executive incentives

---

## Q050: Architecture Governance Board

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Very Common |

### Question

Design an architecture governance board — charter, cadence, scope.

### Short Answer (30 seconds)

Cross-functional board: lead architects, security, data, platform, product reps. Weekly/biweekly triage RFCs, review Tier-0 designs, maintain principles/radar, resolve escalations — enable not block.

### Detailed Answer (3–5 minutes)

**Charter elements:**
- **Mission** — Consistency, risk reduction, speed through standards
- **Scope** — Tier-0/1 reviews, exceptions, standards updates
- **Out of scope** — Team-internal implementation details
- **SLA** — RFC response within 5 business days
- **Escalation** — Unresolved → CTO decision

**Anti-pattern:** Board as approval bottleneck for every deploy.

**Architect:** Delegate Tier-2 to domain architects — board handles portfolio-level decisions.

### Architecture Perspective

Governance board scales architecture quality without centralizing every decision.

### Follow-up Questions

1. **Board metrics? — Time to decision, exception rate, repeat findings.**
2. **Rotating membership? — Domain architects rotate — reduces silo.**

### Common Mistakes in Interviews

- Board reviews every microservice deploy
- No documented charter or SLA
- Board decisions not published to engineering

---

## Q051: Architecture Review Facilitation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reviews |
| **Frequency** | Common |

### Question

How facilitate a productive architecture review meeting?

### Short Answer (30 seconds)

Pre-read RFC/ADR 48h ahead, time-boxed agenda, focus on risks and NFRs not syntax, capture actions with owners, decision or explicit follow-up — no design-by-committee rewrites live.

### Detailed Answer (3–5 minutes)

**Facilitation checklist:**
1. Send pre-read + explicit decision ask
2. Assign note-taker and timekeeper
3. First 5 min: author presents problem and recommendation
4. Structured comments: security, data, ops round-robin
5. Parking lot for deep dives offline
6. Close with: Accepted / Revise / Defer + action items

**Architect as facilitator:** Ask 'what fails first under 10× load?' not 'why not use my favorite tool?'

### Architecture Perspective

Facilitation quality determines whether reviews are feared or valued.

### Follow-up Questions

1. **Review without pre-read? — Cancel or shorten — waste of senior time.**
2. **Silent participants? — Round-robin ensures security voice heard.**

### Common Mistakes in Interviews

- 12 architects whiteboarding replacement design live
- No written outcome after 90-minute meeting
- Personal attacks on author's technology choice

---

## Q052: Diagram Standards and Documentation as Code

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Documentation |
| **Frequency** | Very Common |

### Question

Define diagram standards and documentation-as-code practices for architecture.

### Short Answer (30 seconds)

Standard: C4 levels, naming conventions, color legend, Mermaid/PlantUML in Git, versioned with code, PR review for diagram changes, auto-render in docs site.

### Detailed Answer (3–5 minutes)

**Diagram standards:**
- Tool: Mermaid in repo (diffable) or Structurizr DSL
- Naming: `[Container] Order API` not `Box1`
- Legend required for non-obvious symbols
- One diagram per concern — avoid god diagram

**Docs as code:**
- ADRs, C4, runbooks in Git
- CI: link check, Mermaid render, ADR index lint
- Publish via MkDocs/Backstage/Docusaurus on merge

**Architect:** Diagram in wiki rots — diagram in Git next to service stays honest.

### Architecture Perspective

Documentation as code applies same quality gates as application code.

### Follow-up Questions

1. **Structurizr vs Mermaid? — Structurizr for C4 consistency; Mermaid for quick embed.**
2. **Diagram drift detection? — Compare deployed tags in CMDB to container diagram quarterly.**

### Common Mistakes in Interviews

- Visio files emailed outside version control
- Diagrams with no date or author
- Different teams using incompatible notation

---

## Q053: Architecture Communication

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Communication |
| **Frequency** | Very Common |

### Question

How communicate architecture decisions to diverse audiences?

### Short Answer (30 seconds)

Tailor message: executives (outcomes, risk, cost), developers (ADRs, diagrams, migration steps), ops (runbooks, SLOs), security (threat model, controls). Same decision — multiple formats, one source of truth in ADR.

### Detailed Answer (3–5 minutes)

**Communication matrix:**
| Audience | Format | Focus |
|----------|--------|-------|
| Executive | 1-pager | ROI, risk, timeline |
| Engineering | ADR + RFC | Trade-offs, APIs |
| Ops | Runbook delta | Alerts, capacity |
| Compliance | Control mapping | Audit evidence |

**Channels:** Architecture newsletter, recorded review summary, #architecture Slack with ADR links.

**Architect:** Over-communicate context change when superseding ADRs.

### Architecture Perspective

Communication failure causes 'architecture by rumor'.

### Follow-up Questions

1. **Architecture decision records newsletter? — Monthly digest of new ADRs.**
2. **Developer pushback? — Office hours after major decisions.**

### Common Mistakes in Interviews

- Only PowerPoint for complex migration
- ADR jargon sent to board unchanged
- No comms when ADR superseded — teams build on obsolete decision

---

## Q054: Executive Summary for ADR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Communication |
| **Frequency** | Very Common |

### Question

Write an executive summary section for a technical ADR.

### Short Answer (30 seconds)

Half-page max: problem in business terms, recommended option, cost/timeline impact, top 3 risks and mitigations, what happens if we don't decide. Link to full ADR for engineers.

### Detailed Answer (3–5 minutes)

**Template:**
- **Situation** — Market/regulatory/driver
- **Decision** — We will [X] by [date]
- **Benefit** — $ savings, risk reduction, speed
- **Cost** — $X/month, Y FTE months migration
- **Risks** — Vendor lock-in → mitigated by abstraction layer
- **Ask** — Approve ADR-0042 and fund Q3 migration

**Architect:** Exec summary at top of ADR or linked PDF — many leaders never read consequences section.

### Architecture Perspective

Executive summary unlocks funding and sign-off for technical decisions.

### Follow-up Questions

1. **When separate doc? — Tier-0 ADRs may attach board slide deck appendix.**
2. **Metrics in summary? — One chart beats three paragraphs.**

### Common Mistakes in Interviews

- 10-page ADR emailed to CEO
- No cost figure in executive summary
- Benefits claimed without measurement plan

---

## Q055: Post-Decision Review

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

Run a post-decision review after implementing an ADR. What do you evaluate?

### Short Answer (30 seconds)

3–6 months post-implement: compare outcomes to ADR predictions — cost, latency, operability, team velocity, incidents. Document lessons; supersede ADR if assumptions wrong.

### Detailed Answer (3–5 minutes)

**Review agenda:**
1. Did we implement what ADR stated?
2. Actual vs predicted cost and performance
3. Unexpected consequences
4. Would we decide same today?
5. Update decision log / supersede if needed

**Metrics:** Error budget burn, ops ticket volume, developer satisfaction survey.

**Architect:** Post-decision review closes learning loop — without it ADRs become fiction.

### Architecture Perspective

Post-decision review validates architect accountability.

### Follow-up Questions

1. **Failed decision? — Blameless postmortem — update radar and principles.**
2. **Cadence? — Tier-0 at 90 days; standard at 6 months.**

### Common Mistakes in Interviews

- Never revisiting Accepted ADRs
- Post-review notes not linked to ADR
- Only celebrating successes — ignoring cost overrun

---

## Q056: Michael Nygard ADR Format

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | ADRs |
| **Frequency** | Very Common |

### Question

What is the Michael Nygard ADR format and why is it widely adopted?

### Short Answer (30 seconds)

Title, status, context, decision, consequences — minimal sections that force explicit trade-off thinking and stay readable in Git diffs.

### Detailed Answer (3–5 minutes)

**Nygard template** is the de facto open-source ADR standard.

**Sections:** Context (forces), Decision (chosen path), Consequences (good/bad).

**Enterprise extensions:** Add deciders, options considered, compliance — but keep core short.

**Architect:** Publish org template derived from Nygard in `docs/adr/README.md` with examples.

### Architecture Perspective

Interviewers expect you to name Nygard and explain why brevity beats encyclopedic design docs for decisions.

### Follow-up Questions

1. **ADR tools supporting Nygard? — adr-tools CLI, Log4brains, Backstage ADR plugin.**
2. **Markdown vs YAML front matter? — YAML metadata aids search; body stays Markdown.**

### Common Mistakes in Interviews

- ADR without consequences section
- Copy-paste template without filling options
- Storing ADRs only in Confluence

---

## Q057: Structurizr for C4

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | C4 Model |
| **Frequency** | Common |

### Question

When recommend Structurizr over hand-drawn C4 diagrams?

### Short Answer (30 seconds)

Structurizr DSL gives consistent C4 notation, relationship validation, and diagram views generated from one model — ideal for enterprises with many systems.

### Detailed Answer (3–5 minutes)

**Structurizr workflow:**
1. Define software system, people, containers in DSL
2. Generate context, container, component views automatically
3. Export to PlantUML/Mermaid for docs site

**When yes:** 20+ services, architecture guild enforces notation.
**When no:** Single POC — Mermaid in README faster.

**Architect:** Structurizr workspace in Git — PR review on model changes.

### Architecture Perspective

Tool choice signals whether you scale architecture documentation beyond whiteboards.

### Follow-up Questions

1. **Structurizr Lite vs cloud? — Lite self-hosted; cloud for collaboration features.**
2. **IcePanel vs Structurizr? — IcePanel more UX; Structurizr purer C4 DSL.**

### Common Mistakes in Interviews

- Every architect must learn Structurizr day one
- DSL model diverges from deployed reality
- Generated diagrams never updated after first sprint

---

## Q058: PlantUML Architecture Diagrams

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Documentation |
| **Frequency** | Common |

### Question

Use PlantUML for architecture diagrams in a docs-as-code pipeline.

### Short Answer (30 seconds)

PlantUML text diagrams diff in Git, render in CI to SVG/PNG, embed in MkDocs — same review flow as code.

### Detailed Answer (3–5 minutes)

**Pipeline:**
```bash
plantuml -tsvg docs/architecture/*.puml
```

**Strengths:** Sequence, component, deployment diagrams; IDE plugins.

**C4 integration:** Structurizr exports PlantUML; or C4-PlantUML macros.

**Architect:** Standardize on one diagram-as-code tool per org — avoid Visio attachments.

### Architecture Perspective

Diagram-as-code is table stakes for senior architect interviews in 2026.

### Follow-up Questions

1. **Mermaid vs PlantUML? — Mermaid lighter for README; PlantUML richer for complex UML.**
2. **Render in PR preview? — CI bot posts diagram diff image on PR.**

### Common Mistakes in Interviews

- Binary Visio as source of truth
- PlantUML files not rendered in docs site
- No naming legend on diagrams

---

## Q059: ADR Numbering Convention

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | ADRs |
| **Frequency** | Common |

### Question

Define ADR numbering and file naming conventions for a monorepo.

### Short Answer (30 seconds)

Sequential `NNNN-short-title.md` — never reuse numbers; supersede links old number; pad to 4 digits for sort order.

### Detailed Answer (3–5 minutes)

**Convention:**
- `docs/adr/0042-event-sourcing-orders.md`
- Index table in `docs/adr/README.md`
- CI lint: new ADR must increment max number

**Monorepo:** Central `architecture/adr/` repo or per-service `adr/` with federated index.

**Architect:** Number is permanent identifier — title slug can change in front matter only before merge.

### Architecture Perspective

Numbering discipline prevents 'which ADR is current?' confusion during audits.

### Follow-up Questions

1. **Per-service vs central numbering? — Central sequential; service prefix if federated (`ORDER-0042`).**
2. **Auto-generate number in PR template? — Script suggests next ID.**

### Common Mistakes in Interviews

- Reuse ADR number after supersede
- Random UUID filenames — not human searchable
- No index README in adr folder

---

## Q060: Architecture Review Pre-Read Pack

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reviews |
| **Frequency** | Very Common |

### Question

What belongs in an architecture review pre-read pack sent 48 hours before the meeting?

### Short Answer (30 seconds)

RFC/ADR, C4 context+container, NFR matrix, threat model summary, cost estimate, open questions, explicit decision ask.

### Detailed Answer (3–5 minutes)

**Pack contents:**
1. Problem statement (1 paragraph)
2. Recommended option + alternatives table
3. Diagrams (linked, not 40-page embed)
4. NFR targets with verification plan
5. Risk register top 5
6. Migration/rollback outline

**Architect:** Pre-read mandatory — meeting cancelled if not distributed 48h ahead for Tier-0.

### Architecture Perspective

Pre-read quality predicts review meeting productivity.

### Follow-up Questions

1. **Who prepares pack? — Author owns; architect reviews completeness before scheduling.**
2. **Redact secrets in pre-read? — Use sample data; link to secure vault for creds.**

### Common Mistakes in Interviews

- Slide deck only — no written decision ask
- Diagrams attached as unreadable screenshots
- Open questions buried on slide 38

---

## Q061: Data-Flow Diagram for Threat Modeling

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Draw a data-flow diagram (DFD) for STRIDE threat modeling — what elements are required?

### Short Answer (30 seconds)

Processes, data stores, external entities, data flows, trust boundaries — DFD is prerequisite before STRIDE enumeration.

### Detailed Answer (3–5 minutes)

**DFD elements:**
- **External entity** — User, partner API
- **Process** — Order API, payment worker
- **Data store** — Order DB, cache
- **Flow** — labeled with data classification
- **Trust boundary** — dashed line (Internet/DMZ/internal)

**Architect:** DFD Level 1 for threat model; don't confuse with C4 container (related but different purpose).

### Architecture Perspective

DFD + STRIDE is the standard security review combo for external-facing designs.

### Follow-up Questions

1. **DFD vs C4? — C4 for structure; DFD for security data movement.**
2. **Microsoft Threat Modeling Tool? — Auto STRIDE from DFD elements.**

### Common Mistakes in Interviews

- STRIDE without DFD — threats guessed not systematic
- Missing trust boundaries on diagram
- Unlabeled data flows ('data')

---

## Q062: Architecture Review Tiering

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reviews |
| **Frequency** | Very Common |

### Question

Define architecture review tiers (Tier-0/1/2) and what depth each requires.

### Short Answer (30 seconds)

Tier-0: full checklist, STRIDE, DR, FinOps, board sign-off. Tier-1: standard checklist + ADR. Tier-2: lightweight self-certification with spot audits.

### Detailed Answer (3–5 minutes)

**Example matrix:**
| Tier | Examples | Review depth |
|------|----------|-------------|
| 0 | Payment, PHI | Full board + security |
| 1 | Customer-facing non-PII | Domain architect |
| 2 | Internal tools | Team checklist |

**Architect:** Tier assigned by data classification + revenue impact — not team preference.

### Architecture Perspective

Tiering prevents governance bottleneck while protecting critical paths.

### Follow-up Questions

1. **Who assigns tier? — Architecture guild + data classification auto-tag.**
2. **Tier escalation? — POC becomes Tier-0 when scope adds PII.**

### Common Mistakes in Interviews

- Everything Tier-0 — board exhaustion
- Payment path labeled Tier-2 to skip review
- Tiers undocumented — subjective every time

---

## Q063: Decision Record vs Meeting Minutes

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | ADRs |
| **Frequency** | Common |

### Question

Why are ADRs not substitutes for meeting minutes?

### Short Answer (30 seconds)

ADRs record decisions and rationale — immutable. Minutes capture discussion, attendees, actions — ephemeral. Link minutes to ADR PR but don't bury decision in minutes only.

### Detailed Answer (3–5 minutes)

**Distinction:**
- **Minutes:** Who said what, action items, next meeting
- **ADR:** What we decided, why, consequences

**Practice:** Review meeting minutes reference ADR PR number; decision merges as Accepted ADR.

**Architect:** Slack/Teams threads are not ADRs — export decision to Git.

### Architecture Perspective

Confusing minutes and ADRs loses audit trail for regulators.

### Follow-up Questions

1. **Notion meeting notes as ADR? — Must promote decision to Git ADR.**
2. **Recording videos? — Supplement, not replace written ADR.**

### Common Mistakes in Interviews

- Decision only in meeting minutes
- ADR listing attendees instead of deciders
- No link between RFC comment thread and ADR

---

## Q064: Architecture Review Outcomes

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reviews |
| **Frequency** | Common |

### Question

What are valid outcomes of an architecture review?

### Short Answer (30 seconds)

Accepted, Accepted with conditions, Revise and resubmit, Deferred (needs spike), Rejected — each with documented actions and owners.

### Detailed Answer (3–5 minutes)

**Outcome definitions:**
- **Accepted** — Proceed; conditions tracked as tickets
- **Revise** — Specific gaps (NFR, threat model) before re-review
- **Deferred** — Spike/time-boxed prototype required
- **Rejected** — Alternative approach mandated with rationale

**Architect:** 'Accepted verbally' without written record is not an outcome.

### Architecture Perspective

Clear outcomes prevent ambiguous 'we sort of approved it'.

### Follow-up Questions

1. **Conditions expiry? — Must complete before prod gate — tracked in Jira.**
2. **Re-review SLA? — 5 days after revision submitted.**

### Common Mistakes in Interviews

- Vague 'looks good' email
- Rejected design deployed anyway
- Conditions never tracked to completion

---

## Q065: Mermaid C4 in README

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Documentation |
| **Frequency** | Very Common |

### Question

Embed C4 container diagrams in Markdown using Mermaid — benefits and limits.

### Short Answer (30 seconds)

Mermaid in GitHub/GitLab/MkDocs renders C4-ish diagrams from text — great for PR review and quick updates; limited vs Structurizr for large models.

### Detailed Answer (3–5 minutes)

**Example:**
```mermaid
C4Container
title Order System
Person(customer)
Container(api, Order API, .NET)
```

**Benefits:** Zero tooling install for readers; diffs visible.

**Limits:** Large diagrams clutter; not all C4 macros in older renderers.

**Architect:** Mermaid for service README; Structurizr for enterprise landscape.

### Architecture Perspective

Mermaid lowers barrier to diagrams-as-code for every team.

### Follow-up Questions

1. **C4 extension support? — Verify renderer version in docs CI.**
2. **Auto-render in Backstage? — TechDocs plugin renders Mermaid.**

### Common Mistakes in Interviews

- Mermaid so complex it exceeds renderer limits
- Diagram in image only — not source
- C4 levels mixed on one unreadable diagram

---

## Q066: Architecture Risk Heat Map

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Risk Management |
| **Frequency** | Common |

### Question

Present architecture risks on a 5×5 heat map to executives.

### Short Answer (30 seconds)

Likelihood × impact matrix with color zones — scores ≥15 get mitigation plan and executive visibility; link each risk to ADR or STRIDE item.

### Detailed Answer (3–5 minutes)

**Heat map zones:**
- Green 1–6: monitor
- Yellow 7–14: mitigate this quarter
- Red 15–25: escalate / block release

**Executive view:** Top 10 red risks with owner, ETA, residual risk after mitigation.

**Architect:** Heat map in monthly architecture governance deck — not spreadsheet only.

### Architecture Perspective

Executives understand heat maps faster than technical threat lists.

### Follow-up Questions

1. **Qualitative vs quantitative scoring? — Start qualitative; refine with incident data.**
2. **Risk appetite statement? — Board defines acceptable red count.**

### Common Mistakes in Interviews

- All risks scored medium — useless
- Heat map never updated after launch
- Risks without named owners

---

## Q067: Architecture Standards Document

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Documentation |
| **Frequency** | Very Common |

### Question

What belongs in an enterprise architecture standards document vs principles?

### Short Answer (30 seconds)

Standards are mandatory rules (TLS 1.2+, approved regions, tagging schema). Principles are directional values (API-first). Standards enforced in CI; principles guide ADR trade-offs.

### Detailed Answer (3–5 minutes)

**Standards examples:**
- All external APIs behind API gateway
- No plaintext secrets in repos
- Mandatory cost allocation tags
- Approved auth pattern (OIDC + PKCE)

**Enforcement:** Azure Policy, OPA, fitness functions, review checklist.

**Architect:** Standards versioned in Git — change via RFC + ADR.

### Architecture Perspective

Standards vs principles confusion causes either chaos or paralysis.

### Follow-up Questions

1. **Exception process? — Time-boxed waiver with compensating controls.**
2. **Standards review cadence? — Quarterly — remove obsolete entries.**

### Common Mistakes in Interviews

- Standards doc 200 pages unread
- Standards with no enforcement mechanism
- Principles duplicated as mandatory standards

---

## Q068: Sign-off Workflow in Git

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Very Common |

### Question

Implement architecture sign-off using Git PR approvals.

### Short Answer (30 seconds)

ADR/RFC PR requires CODEOWNERS approvals from architect, security, FinOps delegates — merge = auditable sign-off; branch protection enforces.

### Detailed Answer (3–5 minutes)

**Setup:**
```
# CODEOWNERS
docs/adr/ @enterprise-architects @security-architecture
```

**Branch protection:** 2 approvals including security for Tier-0 paths.

**Evidence:** GitHub/GitLab audit log + ADR deciders field matches approvers.

**Architect:** Sign-off in email is supplement — Git is source of truth.

### Architecture Perspective

Git-based sign-off satisfies SOC2 change management evidence.

### Follow-up Questions

1. **Emergency break-glass? — Retroactive ADR PR within 48h with incident link.**
2. **Delegated approvers? — Document in ADR metadata when primary OOO.**

### Common Mistakes in Interviews

- Verbal approval without PR
- CODEOWNERS file empty
- Same person authors and sole approves Tier-0 ADR

---

## Q069: NFR Traceability Matrix

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | NFRs |
| **Frequency** | Common |

### Question

Link NFRs to test cases and monitoring in a traceability matrix.

### Short Answer (30 seconds)

Matrix columns: NFR ID, requirement, ADR, test (k6/QA), dashboard/alert, owner — proves each NFR is built, tested, and observed.

### Detailed Answer (3–5 minutes)

**Example row:**
NFR-07 | p99 <300ms | ADR-0042 | k6 threshold PR gate | App Insights workbook | Team Checkout

**Audit value:** Regulators ask 'how prove availability claim?' — matrix answers.

**Architect:** NFR matrix required in Tier-0 review pack appendix.

### Architecture Perspective

Traceability is how NFRs survive from slide to production.

### Follow-up Questions

1. **Bi-directional links? — ADR cites NFR IDs; tests cite NFR IDs.**
2. **Orphan NFRs? — Quarterly audit for NFRs with no test.**

### Common Mistakes in Interviews

- NFRs in Word doc disconnected from CI
- Tests exist but not mapped to NFR IDs
- Monitoring without alert linked to NFR

---

## Q070: Architecture Review Facilitation Agenda

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reviews |
| **Frequency** | Common |

### Question

Provide a 60-minute architecture review agenda template.

### Short Answer (30 seconds)

0–5 context, 5–20 author presentation, 20–45 structured feedback rounds, 45–55 decision, 5–60 actions — timeboxed with parking lot.

### Detailed Answer (3–5 minutes)

**Agenda template:**
1. **Context** (5m) — Decision ask stated
2. **Presentation** (15m) — Author only, no interruptions
3. **Round-robin** (25m) — Security, data, ops, FinOps
4. **Decision** (10m) — Accepted/Revise/Defer
5. **Actions** (5m) — Owners + dates

**Architect facilitator:** Cut tool debates — park for offline spike.

### Architecture Perspective

Agenda discipline respects senior reviewer time.

### Follow-up Questions

1. **Recording allowed? — Yes for absent stakeholders; not substitute for ADR.**
2. **Parking lot tracking? — Jira tickets from parking lot same day.**

### Common Mistakes in Interviews

- Unstructured 90-minute debate
- No decision in meeting — another meeting scheduled
- Author not presenting — architect presents for them

---
