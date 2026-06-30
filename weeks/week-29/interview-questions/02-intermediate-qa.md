# Week 29 — Intermediate Q&A

> Q031–Q070: Premium format (Week 1 quality).

---


## Q031: DORA Four Key Metrics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DORA Metrics |
| **Frequency** | Very Common |

### Question

What are the four DORA metrics and how do elite performers benchmark against low performers?

### Short Answer (30 seconds)

Deployment Frequency, Lead Time for Changes, Change Failure Rate, and MTTR. Elite teams deploy multiple times daily with <15% CFR and <1 hour MTTR. I baseline all four before recommending any tooling investment.

### Detailed Answer (3–5 minutes)

The Accelerate/DORA research defines four metrics that predict organizational performance. **Deployment Frequency** measures how often you ship to production. **Lead Time** is commit to production — includes CI, review, and deploy time. **Change Failure Rate** is the percentage of deploys causing failure. **MTTR** is recovery time after incidents.

For a .NET team I assess: monthly deploys + 30% CFR = start with CI and automated tests on every PR. Daily deploys + high CFR = feature flags and canary deploys before adding more services.

I present DORA to executives as a balanced scorecard — optimizing deploy frequency alone while CFR spikes is a warning sign.

### Architecture Perspective

Interviewers want diagnostics, not buzzwords. Tie each metric to an architectural lever: smaller services improve frequency, automated rollback improves MTTR, contract tests reduce CFR.

### Follow-up Questions

1. **1. Lead time vs cycle time? — Cycle time ends at merge; lead time ends in production.**
2. **2. How measure in Azure DevOps? — Deployment records linked to commit SHA and environment.**

### Common Mistakes in Interviews

- Listing metrics without elite benchmarks
- Proposing tools without identifying which metric they improve
- Confusing lead time with cycle time

---

## Q032: Trunk-Based vs GitFlow

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Branching Strategy |
| **Frequency** | Very Common |

### Question

When would you recommend trunk-based development over GitFlow for a .NET enterprise?

### Short Answer (30 seconds)

Trunk-based with feature flags for most .NET microservice teams — short-lived branches merged to main within 1–2 days. GitFlow only for versioned libraries or strict regulatory release branches.

### Detailed Answer (3–5 minutes)

**Trunk-based:** `main` always deployable, branches live hours not weeks, incomplete work behind feature flags. Correlates with elite DORA.

**GitFlow:** long-lived develop, release branches, suited to semver NuGet packages and mobile store releases.

For 5 product teams on microservices, I mandate trunk-based per repo. For a shared domain library consumed by 20 services, GitFlow with semver tags prevents breaking consumers.

Feature flags are non-negotiable for trunk-based — without them you cannot merge incomplete checkout redesigns safely.

### Architecture Perspective

Branching is an architecture decision affecting release coupling and incident response speed.

### Follow-up Questions

1. **1. Can large PRs work with trunk-based? — No. Enforce <400 line PRs or split work.**
2. **2. Monorepo? — Trunk-based still applies; use path filters in CI.**

### Common Mistakes in Interviews

- Calling GitFlow enterprise best practice without trade-offs
- Omitting feature flags as prerequisite
- Ignoring monorepo vs polyrepo impact

---

## Q033: Feature Flags for Safe CD

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Feature Flags |
| **Frequency** | Common |

### Question

How do feature flags decouple deployment from release in a regulated .NET environment?

### Short Answer (30 seconds)

Code deploys to production with flags off; business release happens when compliance approves flag enable. CAB reviews flag rollout, not every binary deploy. Azure App Configuration provides audit history.

### Detailed Answer (3–5 minutes)

Three flag types: **release** (short-lived, new checkout), **ops** (permanent kill switch for payment provider), **experiment** (A/B test).

Regulated flow: automated deploy to prod (standard change) → CAB approves enabling `CheckoutV2` for 5% of users → monitor CFR and conversion → expand.

.NET: `Microsoft.FeatureManagement` + `TargetingFilter` for internal testers first, then `PercentageFilter`.

Flag hygiene: backlog ticket to remove flag and dead code within 2 sprints after 100% rollout.

### Architecture Perspective

This is how architects sell CD to compliance — deploy is low risk when code path is dark.

### Follow-up Questions

1. **1. Flags vs slots? — Slots swap versions; flags control logic within a version.**
2. **2. Test matrix? — CI runs tests with flag on and off.**

### Common Mistakes in Interviews

- Permanent flags becoming spaghetti
- Using flags for security boundaries
- No monitoring during percentage rollout

---

## Q034: Platform Engineering

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Platform Engineering |
| **Frequency** | Common |

### Question

What is an Internal Developer Platform and what would you include for .NET teams?

### Short Answer (30 seconds)

Self-service golden paths: .NET 8 API template, reusable GitHub Actions workflow with OIDC, Bicep modules, App Insights wired, feature flags ready. Platform team measures time-to-first-deploy and developer satisfaction.

### Detailed Answer (3–5 minutes)

IDP layers: **templates** (scaffold), **pipelines** (reusable workflows), **environments** (ephemeral PR envs), **docs** (Backstage catalog).

For 10 teams without IDP, each reinvents CI/CD — inconsistent security, 2-week onboarding. With IDP, clone to deployed hello-world in <1 day.

Platform team owns the paved road; product teams own services. Teams may go off-road but assume operational burden.

### Architecture Perspective

IDP scales architect influence — encodes Managed Identity, no secrets in config, OTel mandatory.

### Follow-up Questions

1. **1. Platform team size? — Roughly 1 platform engineer per 5–8 product teams at maturity.**
2. **2. Build vs buy? — Backstage + custom templates is common.**

### Common Mistakes in Interviews

- Platform team approving every deploy (bottleneck)
- No adoption metrics
- Over-engineering Kubernetes for App Service workloads

---

## Q035: Blameless Postmortems

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Incident Culture |
| **Frequency** | Common |

### Question

How do you facilitate a blameless postmortem after a production incident?

### Short Answer (30 seconds)

Focus on systems not individuals. Timeline, root cause, contributing factors, action items with owners. Architect owns actions for observability gaps, missing failure modes, and ADR updates.

### Detailed Answer (3–5 minutes)

Structure: impact summary → UTC timeline → root cause (technical) → contributing factors (missing alert, no runbook) → what went well → SMART actions.

After payment API outage from connection pool exhaustion: actions included SQL pool metric alert, load test at 2x peak in CI, ADR for read replica.

Blameless does not mean no accountability — malicious acts are HR matters, but still fix the system.

### Architecture Perspective

Postmortems are architecture feedback loops — interviewers want leaders who improve systems.

### Follow-up Questions

1. **1. Near-misses? — Run postmortems for near-misses too — cheaper learning.**
2. **2. Repeat incidents? — Track action item completion rate.**

### Common Mistakes in Interviews

- Root cause = human error
- No measurable action items
- Postmortem only for major outages

---

## Q036: DevOps Culture for Architects

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DevOps Culture |
| **Frequency** | Common |

### Question

What is the architect role in building DevOps culture in a traditional enterprise?

### Short Answer (30 seconds)

Design for deployability and observability, partner with ops early, embed quality gates in golden paths, celebrate learning from incidents. Remove structural barriers — not mandate Kubernetes.

### Detailed Answer (3–5 minutes)

CALMS: Culture, Automation, Lean, Measurement, Sharing.

Architect actions: involve ops in design reviews; include runbooks in sign-off; measure DORA after platform investments; admit when designs fail.

Anti-pattern: tool mandates without cultural readiness — Jenkins installed, nobody trusts automated deploy.

### Architecture Perspective

Behavioral interviews probe influence without authority — DevOps transformation is a strong STAR story.

### Follow-up Questions

1. **1. DevOps vs SRE? — SRE applies software engineering to ops; DevOps is broader cultural movement.**
2. **2. Fund platform team? — Quantify lead time reduction and incident cost savings.**

### Common Mistakes in Interviews

- Equating DevOps with developers doing all ops alone
- Tool-first answers without cultural elements
- Ignoring organizational change management

---

## Q037: CAB vs Continuous Delivery

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

How do you reconcile Change Advisory Board processes with continuous delivery?

### Short Answer (30 seconds)

Automate deploy continuously; CAB approves production flag enable or standard change catalog. Pipeline generates audit evidence — test results, scans, commit SHA, approver identity.

### Detailed Answer (3–5 minutes)

Hybrid model: PR → CI → auto staging → integration tests → artifact signed → CAB reviews automated packet for normal changes → prod promotion.

Standard changes (template microservice deploy) pre-approved. Normal changes get weekly CAB with machine-generated evidence.

SOC 2 CC8 satisfied by environment protection rules and deployment audit logs — not meeting minutes per deploy.

### Architecture Perspective

Real stakeholder tension — show you understand compliance AND modern delivery.

### Follow-up Questions

1. **1. Manual prod deploys? — Start with automated deploy + manual approval gate; narrow scope over time.**
2. **2. Auditor concerns? — Demo immutable pipeline logs and segregation of duties.**

### Common Mistakes in Interviews

- CAB is always wrong
- No hybrid model
- Manual evidence collection per release

---

## Q038: Measuring Platform Success

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Platform Engineering |
| **Frequency** | Occasional |

### Question

What metrics prove an Internal Developer Platform is working?

### Short Answer (30 seconds)

Time from clone to first production deploy, platform adoption rate (% repos on golden path), DORA metrics per team, developer satisfaction survey, and platform support ticket volume trending down.

### Detailed Answer (3–5 minutes)

Leading indicators: template adoption, PRs to platform repos. Lagging: deployment frequency increase, CFR decrease, MTTR decrease.

If adoption is low, platform failed — investigate friction, not mandate harder.

Target: 80% of new services use golden path within 6 months of IDP launch.

### Architecture Perspective

Platform engineering must prove ROI — architects speak business and engineering metrics.

### Follow-up Questions

1. **1. Vanity metrics? — Number of pipelines created means nothing if teams don't use them.**
2. **2. Team opts out? — Allowed with documented operational burden.**

### Common Mistakes in Interviews

- No metrics on platform team success
- Measuring only infrastructure uptime
- Mandating platform without developer input

---

## Q039: Reducing Change Failure Rate

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DORA Metrics |
| **Frequency** | Common |

### Question

A team has daily deploys but 25% change failure rate. What architectural changes do you recommend?

### Short Answer (30 seconds)

Canary deploys with automatic rollback on error spike, feature flags to limit blast radius, contract tests in CI, deployment slots with health checks including DB, and expand-contract database migrations.

### Detailed Answer (3–5 minutes)

High CFR with high frequency means you're moving fast and breaking things. Fixes:
1. **Blast radius** — smaller services, flags off by default
2. **Detection** — synthetic tests post-deploy
3. **Rollback** — one-click slot swap, pipeline auto-rollback on 5xx > 1%
4. **Prevention** — integration + contract tests block merge

Measure CFR per service — one bad service drags team average.

### Architecture Perspective

CFR is the metric that proves whether speed is sustainable.

### Follow-up Questions

1. **1. Freeze deploys? — Worst response — slows learning. Fix quality gates instead.**
2. **2. Who owns CFR? — Service owner, visible on team dashboard.**

### Common Mistakes in Interviews

- Blaming developers without systemic fixes
- Removing deploy frequency to improve CFR
- No per-service CFR breakdown

---

## Q040: Reducing Lead Time

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DORA Metrics |
| **Frequency** | Common |

### Question

Lead time from commit to production is 3 weeks. What do you investigate first?

### Short Answer (30 seconds)

Map the value stream: PR review wait time, CI duration, manual QA queue, CAB schedule, manual deploy steps. Attack the longest wait first — often manual gates or monolith deploy coupling.

### Detailed Answer (3–5 minutes)

Value stream mapping example:
- PR review: 2 days (acceptable)
- CI: 45 min (optimize caching)
- QA queue: 5 days (add automated integration tests)
- CAB: weekly meeting (move to standard changes)
- Deploy: 4 hours manual (automate with slots)

Architectural fix: extract independently deployable microservice so order team isn't blocked by billing team's release train.

### Architecture Perspective

Lead time exposes organizational and architectural coupling — architects see both.

### Follow-up Questions

1. **1. CI too slow? — Parallel jobs, affected-only builds, NuGet cache.**
2. **2. Monolith? — Strangler extraction reduces coupling.**

### Common Mistakes in Interviews

- Only optimizing CI while QA/CAB waits remain
- No value stream measurement
- Ignoring cross-team release train coupling

---

## Q041: Value Stream Mapping for DevOps

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Value Stream |
| **Frequency** | Very Common |

### Question

How do you run a value stream mapping workshop for a .NET team with 3-week lead time?

### Short Answer (30 seconds)

Map commit-to-production flow on a wall: wait times vs process times. Attack the longest wait first — often manual QA queue or CAB scheduling, not compile time.

### Detailed Answer (3–5 minutes)

**Workshop steps:**
1. Identify start (commit merged) and end (running in prod)
2. List every step: PR review, CI, security scan, QA, CAB, deploy, smoke test
3. Measure **wait time** (work sitting idle) vs **process time** (active work)
4. Calculate **process efficiency** = process / (process + wait)

**Example finding:** CI 45 min (process), QA queue 5 days (wait), CAB weekly (wait). Fix: automated integration tests eliminate QA queue; standard changes eliminate CAB wait.

**Architect role:** Facilitate cross-functional map — dev, QA, ops, security. Present business case: 5-day QA wait blocks revenue features.

### Architecture Perspective

Value stream mapping connects DORA lead time to organizational bottlenecks — not just tooling.

### Follow-up Questions

1. **VSM vs process mapping? — VSM adds wait/processing time and % complete-and-accurate.**
2. **Remote teams? — Miro board with sticky notes — same methodology.**

### Common Mistakes in Interviews

- Optimizing CI while 5-day QA wait remains
- No wait time measurement — only process time
- VSM without follow-up action owners

---

## Q042: Team Topologies Stream-Aligned Teams

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Team Topologies |
| **Frequency** | Very Common |

### Question

What is a stream-aligned team in Team Topologies and how does it change architecture?

### Short Answer (30 seconds)

Stream-aligned team owns a business capability end-to-end — order checkout from API to deploy to on-call. Platform and enabling teams reduce their cognitive load.

### Detailed Answer (3–5 minutes)

**Four team types:**
- **Stream-aligned** — delivers customer value (Order Team)
- **Platform** — internal product (CI/CD golden path, IDP)
- **Enabling** — temporary coaching (observability rollout)
- **Complicated-subsystem** — deep specialty (fraud ML)

**Architecture impact:** Bounded context maps to stream-aligned team. Conway's Law: design services team can own independently.

**Anti-pattern:** Stream team depends on 4 other teams to deploy — not truly stream-aligned.

### Architecture Perspective

Team Topologies is org design for DevOps — architects align service boundaries to team ownership.

### Follow-up Questions

1. **Platform team as gatekeeper? — Platform provides paved road; stream teams choose adoption.**
2. **Two-pizza team vs stream-aligned? — Overlap — stream-aligned is capability scope, not just size.**

### Common Mistakes in Interviews

- Component teams owning layers (UI team, API team)
- Platform team approving every production deploy
- Stream-aligned team spanning 12 microservices they cannot deploy alone

---

## Q043: Cognitive Load in Platform Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Team Topologies |
| **Frequency** | Common |

### Question

How do you reduce cognitive load on product teams through platform engineering?

### Short Answer (30 seconds)

Hide infrastructure complexity behind golden-path templates: .NET 8 API scaffold, OIDC pipeline, Bicep modules, App Insights wired. Product teams focus on domain logic only.

### Detailed Answer (3–5 minutes)

**Three cognitive load types (Team Topologies):**
1. **Intrinsic** — domain complexity (unavoidable)
2. **Extraneous** — tooling friction (platform removes)
3. **Germane** — learning new patterns (enabling team helps)

**Tactics:**
- Abstract Kubernetes behind Container Apps or App Service
- Reusable GitHub Actions workflow — teams pass `serviceName` only
- Standard observability — no per-team dashboard DIY

**Measure:** Developer survey + time-to-first-deploy. High extraneous load → low adoption of good practices.

### Architecture Perspective

Cognitive load explains why teams bypass security — make secure path the easy path.

### Follow-up Questions

1. **When expose complexity? — Power users may need escape hatches — document off-road burden.**
2. **Thinnest viable platform? — Start minimal golden path; expand on demand.**

### Common Mistakes in Interviews

- Mandating raw Terraform for all product developers
- Platform with 47 configuration options per service
- No feedback loop on developer friction

---

## Q044: Westrum Organizational Culture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DevOps Culture |
| **Frequency** | Common |

### Question

What is Westrum's organizational culture typology and why does DORA research cite it?

### Short Answer (30 seconds)

Westrum: Pathological (blame), Bureaucratic (rules), Generative (learning). Elite DORA performers correlate with generative culture — information flows freely, failures are learning opportunities.

### Detailed Answer (3–5 minutes)

**Generative signals:**
- Cross-functional collaboration is rewarded
- Messengers not shot — bad news travels fast
- Failures lead to inquiry not punishment
- New ideas welcomed

**Architect influence:** Design blameless postmortems, visible incident learning, psychological safety in architecture reviews.

**Assessment:** Westrum survey (7 questions) baseline before DevOps transformation — retest quarterly.

### Architecture Perspective

Culture predicts delivery performance — tools alone on pathological culture fail.

### Follow-up Questions

1. **Westrum vs CALMS? — Westrum measures culture type; CALMS is DevOps capability framework.**
2. **Can architects change culture? — Influence via systems: postmortems, metrics transparency, golden paths.**

### Common Mistakes in Interviews

- Declaring DevOps culture without measuring Westrum baseline
- Blameful incident reviews while claiming generative culture
- Tool rollout as culture change strategy

---

## Q045: SRE Error Budgets in Practice

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SRE |
| **Frequency** | Very Common |

### Question

How do error budgets change prioritization when a .NET API exhausts its monthly SLO budget?

### Short Answer (30 seconds)

Error budget = 1 − SLO. At 99.9% SLO, 43 min/month downtime allowed. Budget exhausted → freeze feature work, reliability sprint, exec escalation.

### Detailed Answer (3–5 minutes)

**Policy tiers:**
- **>50% budget remaining** — normal feature velocity
- **20–50%** — caution; no risky deploys Friday
- **<20%** — reliability work prioritized
- **Exhausted** — feature freeze until budget resets

**Example:** Order API burned budget on 3 incidents from connection pool exhaustion. Actions: pool metrics alert, load test in CI, circuit breaker on payment dependency.

**Architect:** Error budget is negotiation tool between product and SRE — data-driven not opinion.

### Architecture Perspective

Error budgets make reliability trade-offs explicit — interviewers want policy not just definition.

### Follow-up Questions

1. **100% SLO? — Impossible; creates paralysis and hides real trade-offs.**
2. **Budget per service or team? — Per user-facing service with distinct SLO.**

### Common Mistakes in Interviews

- Error budget with no enforcement mechanism
- Exhausted budget but features still ship unchecked
- SLO defined but never measured

---

## Q046: Toil Reduction for SRE

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SRE |
| **Frequency** | Common |

### Question

What is toil in SRE and how do you measure and reduce it?

### Short Answer (30 seconds)

Toil is manual, repetitive, automatable ops work that scales linearly with service growth. Target <50% of SRE time on toil; automate or eliminate the rest.

### Detailed Answer (3–5 minutes)

**Toil examples:**
- Manual certificate renewal checks
- Clicking through portal to scale instances
- Copy-pasting deployment commands
- Manually correlating logs across 15 services

**Reduction playbook:**
1. Measure toil hours/week per on-call rotation
2. Prioritize highest-frequency tasks
3. Automate with runbooks → scripts → pipelines
4. Track toil ratio quarterly

**Architect:** Design self-healing patterns — auto-scale, auto-restart, automated rollback — to prevent toil at source.

### Architecture Perspective

Toil reduction is how SRE teams buy time for engineering — architects enable automation.

### Follow-up Questions

1. **Toil vs overhead? — Overhead (meetings) is not automatable; toil is.**
2. **When toil is acceptable? — Brief manual intervention during novel incidents — then automate.**

### Common Mistakes in Interviews

- Hero culture rewarding manual firefighting
- Automating without measuring toil baseline
- SRE team spending 80% on ticket queue

---

## Q047: Continuous Learning Culture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DevOps Culture |
| **Frequency** | Common |

### Question

How do architects embed continuous learning into a DevOps transformation?

### Short Answer (30 seconds)

Learning loops: blameless postmortems, game days, internal tech talks, ADR library, chaos experiments with documented outcomes. Celebrate learning from failures publicly.

### Detailed Answer (3–5 minutes)

**Practices:**
- **Postmortem library** — searchable incident learnings
- **Game days** — quarterly failure injection (kill AZ, corrupt cache)
- **Brown bags** — teams demo what they learned from outages
- **Guilds** — .NET, security, observability communities of practice

**Architect actions:** Present ADR decisions including rejected options — models learning. Fund conference attendance tied to internal presentation.

**Anti-pattern:** Postmortem actions never completed — learning theater without improvement.

### Architecture Perspective

Continuous learning is CALMS 'Sharing' — architects institutionalize knowledge transfer.

### Follow-up Questions

1. **Learning vs blame? — Blameless does not mean no accountability for malicious acts.**
2. **Measure learning? — Postmortem action completion rate, repeat incident rate.**

### Common Mistakes in Interviews

- Incidents closed without postmortem
- Same root cause incident three times
- Knowledge locked in senior engineers' heads

---

## Q048: DevSecOps Shift Left

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DevSecOps |
| **Frequency** | Very Common |

### Question

What does shift left mean in DevSecOps for a .NET microservices platform?

### Short Answer (30 seconds)

Security earlier in SDLC: threat modeling at design, SAST/dependency scan in PR, secrets in Key Vault, container scan before deploy — not penetration test after launch.

### Detailed Answer (3–5 minutes)

**Shift-left layers:**
1. **Design** — STRIDE threat model in architecture review
2. **Code** — CodeQL, SonarQube on every PR
3. **Build** — Dependabot, NuGet CVE gate
4. **Pipeline** — Trivy image scan, SBOM generation
5. **Runtime** — WAF, Defender for Cloud

**Gate policy:** Block critical/high new issues; baseline legacy debt. Parallelize scans with tests.

**Architect:** Golden path templates include security by default — OIDC not secrets, Managed Identity mandatory.

### Architecture Perspective

Shift left is architectural — security gates encoded in platform not optional checklist.

### Follow-up Questions

1. **Shift left vs shift everywhere? — Runtime detection still needed — defense in depth.**
2. **DAST placement? — Staging nightly — not blocking every PR.**

### Common Mistakes in Interviews

- Security review only before production launch
- Blocking all PRs on medium SonarQube findings in legacy code
- Developers responsible for manual security checklist per deploy

---

## Q049: Change Failure Root Cause Analysis

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DORA Metrics |
| **Frequency** | Common |

### Question

A team has 20% change failure rate. How do you perform root cause analysis?

### Short Answer (30 seconds)

Classify failures: code defect, config drift, dependency break, schema incompatibility, infrastructure. Measure CFR per service and per change type — one bad service skews average.

### Detailed Answer (3–5 minutes)

**RCA process:**
1. Tag every failed deploy in deployment system
2. Categorize: test gap, missing contract test, bad migration, env config diff
3. Pareto chart — top 3 categories get architectural fixes

**Example findings:**
- 40% failures from breaking EF migrations → expand-contract policy
- 30% from missing payment contract test → Pact in CI
- 20% from staging/prod config drift → IaC for all env config

**Architect:** CFR is lagging indicator — fix systemic gates not individual developers.

### Architecture Perspective

CFR RCA connects metrics to architectural quality gates.

### Follow-up Questions

1. **CFR vs incident rate? — CFR is deploy-triggered failure; incidents include non-deploy causes.**
2. **Target CFR? — Elite <15%; start by halving current rate.**

### Common Mistakes in Interviews

- Reacting to CFR with deploy freeze
- No per-service CFR breakdown
- Root cause = human error without systemic fix

---

## Q050: Deployment Freeze Anti-Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Release Management |
| **Frequency** | Common |

### Question

Why are deployment freezes before holidays a DevOps anti-pattern and what do you do instead?

### Short Answer (30 seconds)

Freezes stop learning, accumulate big-bang releases, and often fail anyway — outages spike when frozen code finally deploys. Replace with smaller changes, feature flags, and heightened monitoring.

### Detailed Answer (3–5 minutes)

**Problems with freeze:**
- Risk concentrates in post-freeze mega-deploy
- Security patches delayed
- Team velocity drops; morale suffers
- False sense of safety — prod still drifts

**Alternatives:**
- Feature flags — dark deploy risky code
- Canary with tighter thresholds during peak
- On-call staffing increase
- Automated rollback on SLO burn

**Exception:** Regulated blackout windows — negotiate automated low-risk changes still allowed.

### Architecture Perspective

Architects argue against freeze with risk math — smaller batches beat big-bang.

### Follow-up Questions

1. **Black Friday? — Freeze new features via flags; allow hotfixes and security patches.**
2. **Stakeholder fear? — Show CFR data for big-bang vs continuous deploy.**

### Common Mistakes in Interviews

- Annual freeze becoming permanent risk management
- No exception process for critical security patches
- Freeze without reducing change size after thaw

---

## Q051: MTTR Reduction via Runbook Automation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SRE |
| **Frequency** | Common |

### Question

How do runbook automation and Azure Automation reduce MTTR?

### Short Answer (30 seconds)

Codify incident response: diagnostic queries, scale-out scripts, slot swap rollback, cache flush — triggered from alert or runbook button. MTTR drops when L1 executes automation instead of paging senior engineer.

### Detailed Answer (3–5 minutes)

**Automation tiers:**
1. **Diagnostic** — auto-run KQL query, attach results to incident ticket
2. **Remediation** — restart app, scale SQL DTU, swap deployment slot
3. **Escalation** — auto-page if automation fails

**Example:** Payment API 5xx alert → runbook checks SQL DTU saturation → auto-scale + notify on-call → if unresolved in 10 min, page SRE.

**Architect:** Design services for operability — health endpoints checking dependencies, graceful degradation paths documented in runbooks.

### Architecture Perspective

MTTR is a DORA metric architects improve through operability design.

### Follow-up Questions

1. **Runbook vs playbook? — Runbook is technical steps; playbook includes comms and escalation.**
2. **Azure Automation vs GitHub Actions? — Automation for hybrid/runbook response; Actions for deploy.**

### Common Mistakes in Interviews

- Runbooks as Word docs nobody reads during incidents
- Automation without idempotency testing
- MTTR measured but no runbook linked to alerts

---

## Q052: Incident Commander Role

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Incident Management |
| **Frequency** | Common |

### Question

What does an incident commander do during a Sev1 outage?

### Short Answer (30 seconds)

IC coordinates response — not the person fixing. Owns timeline, communication, decision log, resource allocation. Ensures parallel workstreams don't conflict.

### Detailed Answer (3–5 minutes)

**IC responsibilities:**
- Declare incident severity and channel
- Assign roles: ops lead (technical), comms lead (status page), scribe (timeline)
- Regular status cadence every 15 min
- Decision authority: rollback vs fix-forward
- End incident when SLO restored; schedule postmortem

**Architect as IC:** Technical depth helps prioritize — payment down beats cosmetic CSS bug. Defer root cause to postmortem during incident.

**Training:** Rotate IC role in game days — not only managers.

### Architecture Perspective

IC role shows operational leadership — senior architects expected to lead Sev1.

### Follow-up Questions

1. **IC vs ops lead? — IC coordinates; ops lead executes technical investigation.**
2. **When no IC? — Small teams — on-call lead assumes IC informally.**

### Common Mistakes in Interviews

- Everyone debugging with no coordination
- IC also deep-diving logs — role confusion
- No external communication during customer-impacting outage

---

## Q053: SRE vs DevOps Organizational Models

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Org Design |
| **Frequency** | Common |

### Question

Compare embedding SREs in product teams vs centralized SRE platform team.

### Short Answer (30 seconds)

Embedded SRE: deep product knowledge, faster trust. Centralized: consistent practices, tooling standards. Hybrid common: platform SRE builds tools, embedded SRE partners with 2–3 product teams.

### Detailed Answer (3–5 minutes)

**Models:**
| Model | Pros | Cons |
|-------|------|------|
| Embedded | Context, ownership | Inconsistent practices |
| Centralized | Standards, career path | Ticket queue bottleneck |
| Hybrid | Balance | Coordination overhead |

**DevOps vs SRE:** DevOps is cultural movement; SRE is concrete implementation with error budgets and toil metrics.

**Architect:** Define SRE engagement model in platform ADR — when embedded SRE joins new product team.

### Architecture Perspective

Org model affects reliability outcomes — architects influence structure.

### Follow-up Questions

1. **SRE team as ops rename? — SRE must do engineering work — automation, not ticket routing.**
2. **DevOps engineer title? — Often platform engineering — clarify expectations.**

### Common Mistakes in Interviews

- SRE team that only pages and escalates
- No engagement model — SRE pulled into every project ad hoc
- Confusing DevOps culture with eliminating ops entirely

---

## Q054: Conway's Law in Microservices

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Architecture |
| **Frequency** | Very Common |

### Question

How does Conway's Law affect microservice decomposition decisions?

### Short Answer (30 seconds)

Organizations produce systems mirroring communication structure. Split services along team boundaries — if two teams must coordinate daily, don't split their services without API contract discipline.

### Detailed Answer (3–5 minutes)

**Implications:**
- 4 teams → aim for ~4–8 services with clear ownership
- Split by bounded context matching team cognitive load
- **Inverse Conway maneuver:** Restructure teams to desired architecture (risky but intentional)

**Anti-pattern:** 50 microservices, 5 developers — coordination overhead kills velocity.

**Architect:** Present org chart alongside architecture diagram in reviews — misalignment predicts integration pain.

### Architecture Perspective

Conway's Law is why architects need org design literacy.

### Follow-up Questions

1. **Monorepo effect? — Teams can still own directories — Conway applies to ownership.**
2. **Outsourced integration? — Vendor boundary becomes service boundary — plan ACL.**

### Common Mistakes in Interviews

- 50 services for 8 developers
- Service split without team ownership assignment
- Ignoring communication overhead in integration design

---

## Q055: Technical Debt vs Delivery Velocity

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Engineering Culture |
| **Frequency** | Common |

### Question

How do you balance technical debt paydown with feature velocity for executives?

### Short Answer (30 seconds)

Reserve 15–20% capacity for debt; quantify debt cost in DORA metrics (CFR, lead time). Present debt as risk with business impact — not engineering wish list.

### Detailed Answer (3–5 minutes)

**Framework:**
- **Interest payments** — incidents, slow deploys, developer attrition from frustration
- **Principal** — refactoring cost to fix
- **Prioritize** debt touching revenue path (checkout) over cosmetic modules

**Metrics:** Track CFR and lead time before/after debt sprints. Show 25% CFR drop after test coverage investment.

**Architect:** ADR documents accepted debt with expiration — 'shared DB acceptable for 6 months during strangler.'

### Architecture Perspective

Debt negotiation is executive communication — architects quantify risk.

### Follow-up Questions

1. **Boy scout rule? — Incremental improvement each PR — complements dedicated debt sprints.**
2. **Debt register? — Visible backlog with business impact scores.**

### Common Mistakes in Interviews

- Big-bang rewrite as only debt strategy
- Zero debt capacity — velocity illusion until outage
- Debt items without business impact articulation

---

## Q056: Developer Experience Metrics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Platform Engineering |
| **Frequency** | Common |

### Question

What metrics measure Internal Developer Platform developer experience?

### Short Answer (30 seconds)

Time-to-first-deploy, PR build time p50/p95, platform NPS survey, golden path adoption %, support ticket volume, and DORA metrics per team using platform.

### Detailed Answer (3–5 minutes)

**Leading indicators:**
- Template clone-to-running-hello-world < 1 day
- % repos on golden path workflow
- Developer satisfaction quarterly survey (5 questions)

**Lagging indicators:**
- Deployment frequency increase after IDP launch
- MTTR decrease
- Onboarding time new hire → first prod commit

**Red flag:** Low adoption despite mandate — platform failed; interview users don't enforce harder.

### Architecture Perspective

DX metrics prove platform ROI — architects speak product metrics for internal products.

### Follow-up Questions

1. **SPACE framework? — Satisfaction, Performance, Activity, Communication, Efficiency — broader than DORA.**
2. **Vanity metric trap? — Pipelines created count meaningless without adoption.**

### Common Mistakes in Interviews

- Platform success measured only by uptime
- No developer survey feedback loop
- Mandating platform without measuring friction

---

## Q057: Release Train vs Continuous Delivery

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Release Management |
| **Frequency** | Very Common |

### Question

When is a release train appropriate vs continuous delivery for .NET microservices?

### Short Answer (30 seconds)

Release train for coordinated multi-service releases (shared schema, mobile app store). Continuous delivery for independently deployable microservices with contract tests.

### Detailed Answer (3–5 minutes)

**Release train:** Fixed schedule (e.g., Thursday 2pm), all services board together, integration window, higher coordination cost.

**Continuous:** Each service deploys on green main — Pact/contract tests prevent integration breaks.

**Hybrid:** Most services continuous; quarterly train for major versioned API breaking changes.

**Architect:** Release train often signals architectural coupling — goal is reduce train frequency by decoupling.

### Architecture Perspective

Release model reflects architecture coupling — trains are symptom of tight coupling.

### Follow-up Questions

1. **SAFe release train? — Agile at scale — architect knows when overhead justified.**
2. **Mobile constraint? — App store review forces train for client; server can still CD.**

### Common Mistakes in Interviews

- Release train for 3 independent microservices
- Train as excuse to skip automated integration tests
- Continuous deploy without contract tests on shared APIs

---

## Q058: SOC 2 Compliance Automation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compliance |
| **Frequency** | Common |

### Question

How do you automate SOC 2 evidence collection in CI/CD pipelines?

### Short Answer (30 seconds)

Pipeline generates audit artifacts: test results, security scan reports, deployment approvals, access logs, change tickets linked to commit SHA — stored immutably in blob storage.

### Detailed Answer (3–5 minutes)

**CC8 change management automation:**
- Branch protection rules enforced via API audit
- Production deploy requires environment approval — logged
- SAST/dependency scan results archived per build
- Infrastructure changes via IaC PR with plan diff

**Tools:** Vanta/Drata integrate with GitHub and Azure; custom scripts export deployment records.

**Architect:** Design golden path so compliant path is default — manual prod deploy impossible.

### Architecture Perspective

Compliance automation is architecture — auditors trust systems not screenshots.

### Follow-up Questions

1. **SOC 2 vs ISO 27001? — Overlapping controls; pipeline evidence serves both.**
2. **Manual evidence before audit? — Automate continuous — audit is sampling not scramble.**

### Common Mistakes in Interviews

- Scrambling screenshots week before audit
- Compliance as separate team bolt-on
- No linkage between deploy and change ticket

---

## Q059: Audit Trail in CI/CD Pipelines

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

What audit trail must a production CI/CD pipeline maintain for regulated .NET workloads?

### Short Answer (30 seconds)

Immutable record: who approved, what commit SHA, what artifact digest, what tests passed, what scans ran, when deployed, to which environment — retained 7 years typical.

### Detailed Answer (3–5 minutes)

**Audit fields:**
- `commitSha`, `artifactDigest`, `buildId`
- Approver identity and timestamp
- Test and scan result artifacts
- Environment promotion history
- Rollback events with reason

**Implementation:** GitHub deployment API, Azure DevOps deployment records, append-only blob storage. OIDC subject identifies pipeline identity.

**Architect:** Segregation of duties — developer cannot approve own prod deploy.

### Architecture Perspective

Audit trail enables forensic investigation and regulatory compliance.

### Follow-up Questions

1. **Mutable logs? — Ship to SIEM with WORM storage — pipeline logs tamper-evident.**
2. **Artifact provenance? — Sigstore/cosign signature in audit record.**

### Common Mistakes in Interviews

- Deployment with no commit SHA traceability
- Developer self-approves production
- Audit logs in ephemeral CI runner disk only

---

## Q060: DORA Benchmarking Cadence

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DORA Metrics |
| **Frequency** | Common |

### Question

How often should teams benchmark DORA metrics and against whom?

### Short Answer (30 seconds)

Measure weekly automated, review monthly with team, benchmark quarterly against industry (DORA/Accelerate report) and own historical trend. Compare similar teams internally not across unlike contexts.

### Detailed Answer (3–5 minutes)

**Cadence:**
- **Weekly:** Automated dashboard — deployment frequency, lead time, CFR, MTTR
- **Monthly:** Team retrospective — one metric improvement goal
- **Quarterly:** Compare to DORA elite/high/medium/low tiers; present to leadership

**Benchmarking pitfalls:**
- Vanity deploy counts without CFR context
- Comparing mobile team to API team without normalization

**Architect:** Use DORA to prioritize investments — if lead time high, value stream map before buying new CI tool.

### Architecture Perspective

Benchmarking cadence turns DORA from poster to management system.

### Follow-up Questions

1. **DORA vs SPACE? — Complementary — DORA delivery, SPACE developer wellbeing.**
2. **Industry benchmark source? — DORA State of DevOps report annually.**

### Common Mistakes in Interviews

- Annual DORA glance with no action
- Benchmarking against Google when 50-person fintech
- Improving deploy count while CFR spikes

---

## Q061: CALMS Framework DevOps

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DevOps Culture |
| **Frequency** | Very Common |

### Question

Explain the CALMS framework and how it guides a DevOps transformation.

### Short Answer (30 seconds)

Culture, Automation, Lean, Measurement, Sharing — culture and sharing first; automation without trust fails.

### Detailed Answer (3–5 minutes)

**CALMS pillars:**
- **Culture** — blameless learning, cross-functional ownership
- **Automation** — CI/CD, IaC, repeatable releases
- **Lean** — value stream, WIP limits, eliminate wait time
- **Measurement** — DORA metrics, flow metrics, SLOs
- **Sharing** — internal conferences, shared runbooks, open postmortems

**Azure/.NET example:** Platform team publishes golden-path GitHub Actions templates; stream teams adopt without ticket queue.

**Architect:** CALMS is diagnostic — score each pillar before buying more Jenkins agents.

### Architecture Perspective

CALMS shows maturity is cultural before tooling — interviewers probe whether you lead with culture.

### Follow-up Questions

1. **CALMS vs DORA? — CALMS is philosophy; DORA quantifies outcomes.**
2. **Where start? — Value stream map + one bottleneck automation win.**

### Common Mistakes in Interviews

- CALMS as checklist without culture change
- Buy tools before measuring baseline
- Ignore Sharing pillar entirely

---

## Q062: DORA Four Key Metrics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DORA |
| **Frequency** | Very Common |

### Question

What are the four DORA metrics and what do Elite performers achieve?

### Short Answer (30 seconds)

Deployment frequency, lead time for changes, change failure rate, MTTR — Elite: on-demand deploys, <1hr lead time, <15% CFR, <1hr restore.

### Detailed Answer (3–5 minutes)

**DORA four keys:**
| Metric | Elite (indicative) | What it measures |
|--------|-------------------|------------------|
| Deployment frequency | On-demand / multiple/day | Delivery throughput |
| Lead time for changes | <1 hour | Flow efficiency |
| Change failure rate | 0–15% | Quality of change |
| MTTR | <1 hour | Recovery capability |

**Collect in Azure DevOps:** Deployment records + work item cycle time + incident linkage.

```csharp
// Tag releases in Application Insights for CFR correlation
telemetry.TrackEvent("Deployment", new Dictionary<string,string> {
    ["version"] = buildId, ["environment"] = "prod"
});
```

**Architect:** Never optimize one metric in isolation — faster deploys with rising CFR is regressing.

### Architecture Perspective

DORA metrics are the lingua franca of engineering leadership conversations.

### Follow-up Questions

1. **Accelerate book? — Forsgren et al. — research backing, not vendor marketing.**
2. **Low performers? — Monthly deploys, >1 month lead time — baseline before goals.**

### Common Mistakes in Interviews

- Cherry-pick deployment frequency only
- No baseline before transformation
- Claim Elite without measurement method

---

## Q063: Team Topologies Overview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Team Topologies |
| **Frequency** | Very Common |

### Question

Describe the four Team Topologies team types and their interaction modes.

### Short Answer (30 seconds)

Stream-aligned, platform, enabling, complicated-subsystem — modes: collaboration, X-as-a-Service, facilitation.

### Detailed Answer (3–5 minutes)

**Team types:**
1. **Stream-aligned** — owns feature flow end-to-end (Checkout squad)
2. **Platform** — internal APIs, golden paths, self-service (Azure landing zone portal)
3. **Enabling** — temporary coaching (observability adoption sprint)
4. **Complicated-subsystem** — deep specialty (payments PCI, ML ranking)

**Interaction modes:**
- **X-as-a-Service** — platform provides documented APIs
- **Facilitation** — enabler pairs with stream temporarily
- **Collaboration** — joint work on complex integration

**Architect:** Platform as ticket queue violates X-as-a-Service — embed enablers instead.

### Architecture Perspective

Team Topologies connects Conway's Law to deliberate org design.

### Follow-up Questions

1. **Thinnest viable platform? — One golden path (.NET 8 + AKS) done well.**
2. **Reverse Conway? — Reorg streams before extracting microservices.**

### Common Mistakes in Interviews

- Platform team as approval gate
- Every team owns Kubernetes upgrades
- No interaction mode documented

---

## Q064: SRE vs DevOps Role

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SRE |
| **Frequency** | Very Common |

### Question

How does Site Reliability Engineering differ from traditional DevOps?

### Short Answer (30 seconds)

SRE applies software engineering to operations with error budgets and SLOs; DevOps is broader cultural movement — SRE is one implementation pattern.

### Detailed Answer (3–5 minutes)

**SRE principles (Google):**
- **SLIs/SLOs** — measurable reliability targets
- **Error budgets** — balance velocity vs stability
- **Toil reduction** — automate repetitive ops (<50% toil target)
- **Blameless postmortems** — learn from incidents

**DevOps broader:** CALMS, whole-team ownership, value stream.

**.NET on AKS example:** SRE team owns cluster SLOs + golden Helm charts; stream teams own app SLOs within budget.

**Architect:** SRE is not 'ops with a new title' — it requires engineering investment in automation.

### Architecture Perspective

Clarifying SRE vs DevOps shows you understand industry nuance beyond buzzwords.

### Follow-up Questions

1. **SRE team size? — Rule of thumb: 5–8 SREs per 100 devs at scale.**
2. **DevOps engineer title? — Often platform/SRE hybrid — define scope explicitly.**

### Common Mistakes in Interviews

- SRE as gatekeeper approving all deploys
- 100% reliability goal — no error budget
- SRE team disconnected from development

---

## Q065: Platform Engineering Basics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Platform Engineering |
| **Frequency** | Very Common |

### Question

What is platform engineering and how does it differ from a traditional ops team?

### Short Answer (30 seconds)

Platform engineering builds internal developer platforms (IDP) as products — self-service golden paths reduce cognitive load for stream teams.

### Detailed Answer (3–5 minutes)

**IDP components:**
- Developer portal (Backstage, Azure Dev Center)
- Golden path templates (Bicep + GitHub Actions + AKS)
- Shared observability, secrets, identity
- Service catalog with ownership metadata

**Difference from ops:**
| Ops | Platform Engineering |
|-----|---------------------|
| Ticket queue | Self-service APIs |
| Snowflake servers | Standardized modules |
| Reactive | Product roadmap + NPS |

**Architect:** Measure platform success via adoption % and DORA improvement of consuming teams.

### Architecture Perspective

Platform engineering is hot because it operationalizes Team Topologies at scale.

### Follow-up Questions

1. **Build vs buy IDP? — Backstage + Azure primitives common hybrid.**
2. **Platform PM? — Needed at 150+ engineers for roadmap prioritization.**

### Common Mistakes in Interviews

- Platform team builds everything custom
- No developer feedback loop
- Golden path optional — most teams bypass

---

## Q066: Value Stream Mapping DevOps

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Value Stream |
| **Frequency** | Common |

### Question

How use value stream mapping in a DevOps transformation?

### Short Answer (30 seconds)

Map steps from commit to production customer value; measure wait time vs process time; attack biggest wait — often environment provisioning or approval gates.

### Detailed Answer (3–5 minutes)

**VSM exercise:**
1. Walk one feature from idea → prod
2. Time each state: coding, review, CI, staging, CAB, deploy
3. Calculate **process ratio** = value-add time / total lead time

**Typical finding:** 5 days total, 4 hours coding — 95% wait.

**Azure fix:** Ephemeral PR environments via Bicep + GitHub Actions; remove CAB for low-risk paths.

**Architect:** VSM data beats opinion in steering committee debates.

### Architecture Perspective

Value stream mapping grounds DevOps in measurable flow, not toolchain shopping.

### Follow-up Questions

1. **Kanban vs VSM? — VSM is one-time diagnostic; Kanban sustains flow.**
2. **Deployment pipeline as VSM? — Yes — visualize wait states in Azure DevOps.**

### Common Mistakes in Interviews

- Optimize compile time when CAB waits 2 weeks
- VSM without executive sponsor
- Ignore downstream ops wait states

---

## Q067: Westrum Organizational Culture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Culture |
| **Frequency** | Common |

### Question

What is Westrum's organizational culture typology and why does DORA research cite it?

### Short Answer (30 seconds)

Generative (high cooperation, shared risk), Bureaucratic (rules), Pathological (blame) — generative culture correlates with better software delivery performance.

### Detailed Answer (3–5 minutes)

**Three types:**
| Type | Information flow | Failure response |
|------|-----------------|------------------|
| Pathological | Hoarded | Blame individuals |
| Bureaucratic | Siloed by role | Cover up |
| Generative | Shared across teams | Learn collectively |

**Assessment:** Survey questions on collaboration and incident response.

**Intervention:** Blameless postmortems, cross-team guilds, leadership modeling.

**Architect:** Culture metrics belong in transformation dashboards alongside DORA.

### Architecture Perspective

Westrum links culture to delivery outcomes — architects influence culture via rituals.

### Follow-up Questions

1. **Measure culture? — Annual Westrum survey + incident response qualitative review.**
2. **Toxic culture fix? — Executive sponsorship required — grassroots alone fails.**

### Common Mistakes in Interviews

- Assume generative because you use Kubernetes
- Skip culture in transformation plan
- Blame individuals in incident reviews

---

## Q068: Error Budget Concept

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SRE |
| **Frequency** | Very Common |

### Question

Explain error budgets and how they resolve the velocity vs stability conflict.

### Short Answer (30 seconds)

Error budget = 1 − SLO (e.g., 99.9% SLO → 43 min/month downtime budget). While budget remains, ship features; when exhausted, freeze features and fix reliability.

### Detailed Answer (3–5 minutes)

**Policy example:**
```
SLO: 99.95% availability (21 min/month budget)
Burn rate alert: 14.4× → page immediately
Budget exhausted → reliability sprint, no feature deploys
```

**.NET API on App Service:** Track availability SLI via Application Insights availability tests + request success rate.

**Negotiation:** Product owns feature velocity within budget; SRE owns measurement.

**Architect:** Error budget policy must be pre-agreed in writing — not invented during outage.

### Architecture Perspective

Error budgets are the diplomatic bridge between product and reliability teams.

### Follow-up Questions

1. **Multi-window burn alerts? — Google SRE workbook — fast + slow burn.**
2. **Budget for dependencies? — Track internal platform SLO separately.**

### Common Mistakes in Interviews

- 100% uptime SLO — no budget for velocity
- Error budget without enforcement policy
- Ignore budget until major outage

---

## Q069: Blameless Postmortem Practice

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Incident Culture |
| **Frequency** | Very Common |

### Question

What makes a postmortem truly blameless and effective?

### Short Answer (30 seconds)

Focus on systems and processes that allowed failure; action items with owners and dates; publish widely; never name individuals as root cause.

### Detailed Answer (3–5 minutes)

**Blameless postmortem template:**
1. **Summary** — impact, duration, customer effect
2. **Timeline** — UTC timestamps from monitoring
3. **Root cause** — contributing factors (usually multiple)
4. **What went well** — effective mitigations
5. **Action items** — preventive, detective, process
6. **Lessons** — shareable patterns

**Azure example:** App Configuration flag rollback failed — action: add flag kill-switch integration test in CI.

**Architect:** Track action item completion rate — postmortems without follow-through breed cynicism.

### Architecture Perspective

Blameless culture is tested during the first major outage — rituals matter.

### Follow-up Questions

1. **Blameless vs no accountability? — Accountability for actions, not punishment for mistakes.**
2. **Customer-facing postmortem? — Status page summary without internal jargon.**

### Common Mistakes in Interviews

- Name engineer in root cause
- Postmortem without action items
- Incident closed before postmortem scheduled

---

## Q070: Trunk-Based Development

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DevOps Practices |
| **Frequency** | Very Common |

### Question

Explain trunk-based development and its relationship to CI/CD maturity.

### Short Answer (30 seconds)

All developers commit to main/trunk at least daily; short-lived branches (<1 day); feature flags hide incomplete work; requires strong CI and test automation.

### Detailed Answer (3–5 minutes)

**Practices:**
- Main branch always releasable
- Feature flags (LaunchDarkly, Azure App Configuration)
- Small commits — easier bisect on failure
- Branch by abstraction for large refactors

**vs GitFlow:** GitFlow suits release trains; trunk suits continuous delivery.

```csharp
if (await _featureFlags.IsEnabledAsync("NewCheckoutFlow", userId))
    return await _checkoutV2.ProcessAsync(order);
return await _checkoutV1.ProcessAsync(order);
```

**Architect:** Trunk without CI test gate causes main branch chaos — automate first.

### Architecture Perspective

Trunk-based development is prerequisite for elite deployment frequency.

### Follow-up Questions

1. **Release branches exception? — Short-lived for LTS products only.**
2. **Pair with code review? — Yes — small PRs reviewed within hours.**

### Common Mistakes in Interviews

- Long-lived feature branches months
- Trunk without feature flags
- Skip CI on main merges

---
