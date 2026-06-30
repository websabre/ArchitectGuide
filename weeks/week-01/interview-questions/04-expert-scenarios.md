# Week 01 — Expert Scenario Interview Q&A (Q101–Q120)

> 20 scenario-based questions — premium format

---


## Q101: Go Rewrite Decision

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Architecture |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Team wants Go rewrite for performance. 500 RPS .NET API, p99 80ms.

### Short Answer (30 seconds)

Profile first — likely DB or network. FARCS: rewrite 6-12 months, retraining, dual maintenance. Optimize .NET: indexes, caching, async I/O, Native AOT if startup. Rewrite only if proven insufficient.

### Detailed Answer

**Response structure:** Acknowledge concern → propose 2-week profiling sprint → decision gate with metrics.

**Stakeholder:** 'Rewrite delays features 2 quarters — data will tell us if runtime is bottleneck.'

### Architecture Perspective

Shows judgment under pressure to chase trends.

### Follow-up Questions

1. **What metrics prove runtime bottleneck? — CPU <30% but high latency → not CPU language issue.**
2. **When Go makes sense? — Small binary edge workers, team already expert.**

### Common Mistakes in Interviews

- Blind rewrite approval
- No profiling data
- Ignoring organizational cost

---

## Q102: GC Pause Trading System

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Performance |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

p99 latency spikes correlate with Gen2 GC in trading-adjacent system.

### Short Answer (30 seconds)

Reduce allocations in hot path, `ArrayPool`, struct-based tick data, object pooling for orders, consider LOH compaction settings, isolate critical path to dedicated hardware if needed.

### Detailed Answer

**Investigation:** dotMemory during spike, allocation stack traces, LOH size.

**Extreme:** separate process for matching engine with tuned GC settings (`DOTNET_GCName` workstation vs server).

### Architecture Perspective

Latency-sensitive .NET requires GC-aware architecture.

### Follow-up Questions

1. **Server vs workstation GC? — Server default for ASP.NET — throughput vs latency trade-off.**
2. **Native AOT for matching? — Evaluate if reflection-free feasible.**

### Common Mistakes in Interviews

- Ignore GC in latency SLA
- Allocate per tick in hot loop
- Full GC during market hours untuned

---

## Q103: Monolith Extraction Deadline

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

CEO mandates microservices in 6 months. 500K LOC monolith, 30 developers.

### Short Answer (30 seconds)

Push back with phased strangler plan: Month 1-2 observability + CI, 3-4 extract one bounded context, 5-6 second context. Full decomposition 18-24 months realistic.

### Detailed Answer

Deliver: context map, risk register, what 'microservices' achieves by month 6 (2 services + platform foundations).

**Executive comms:** Tie to business outcomes — deploy frequency, not buzzword.

### Architecture Perspective

Architect must negotiate scope with leadership.

### Follow-up Questions

1. **What ship in 6 months? — Extracted payment service + API gateway + tracing.**
2. **Risk if big bang? — Production outage, team burnout.**

### Common Mistakes in Interviews

- Promise full decomposition in 6 months
- No incremental value milestones
- Skip platform prerequisites

---

## Q104: Null Reference Production Outage

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

NullReferenceException top crash in mobile API after release. Architect response?

### Short Answer (30 seconds)

Immediate: rollback or hotfix. Week: enable NRT on service, warnings as errors in CI, add null checks at API boundaries, review crash telemetry top stacks.

### Detailed Answer

Root cause: nullable disabled + new DTO field. Prevention: NRT + contract tests + staged rollout with feature flag.

### Architecture Perspective

Shows incident + systemic fix thinking.

### Follow-up Questions

1. **Blame developer? — Focus on system gates missing.**
2. **Feature flag rollback? — Faster than redeploy if integrated.**

### Common Mistakes in Interviews

- Fix null check only — no systemic gate
- Disable nullable to ship faster
- No staged rollout

---

## Q105: EF Core N+1 Production

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Order API p99 2s after feature launch. dotTrace shows 200 SQL queries per request.

### Short Answer (30 seconds)

N+1 from lazy loading or loop with `Include` missing. Fix: projection query, `AsNoTracking` for reads, split query, or explicit batch load.

### Detailed Answer

**Immediate:** hotfix with `.Include()` or DTO projection. **Long-term:** ban lazy loading in API layer, arch test, query review in PR for data access.

### Architecture Perspective

Classic production issue architects must diagnose fast.

### Follow-up Questions

1. **Split query EF? — `.AsSplitQuery()` — multiple SQL vs cartesian explosion.**
2. **Compiled queries? — Hot path micro-optimization after N+1 fixed.**

### Common Mistakes in Interviews

- Lazy loading enabled in web API
- No query logging in staging
- Ignore SQL count in PR review

---

## Q106: Memory Leak in Production

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

App Service memory grows 8GB over 48 hours until restart.

### Short Answer (30 seconds)

Capture dump, analyze with dotMemory — static event handlers, undisposed `HttpClient` (pre-IHttpClientFactory), cache without eviction, DI singleton holding scoped services.

### Detailed Answer

**Common .NET leak:** singleton capturing scoped `DbContext`. Fix lifetimes, `IDisposable` audit, memory alert at 70%.

### Architecture Perspective

Memory leak triage is operational architect skill.

### Follow-up Questions

1. **Dump capture in Azure? — Diagnostic settings memory dump on threshold.**
2. **HttpClient anti-pattern? — `new HttpClient()` per request — socket exhaustion.**

### Common Mistakes in Interviews

- Ignore slow memory growth
- Restart without root cause
- Singleton DbContext

---

## Q107: Breaking API Change Crisis

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Mobile team broken by API field rename — 2M users affected.

### Short Answer (30 seconds)

Immediate: revert or dual-field compatibility period. Process: API versioning policy, contract tests in CI, deprecation timeline, consumer notification.

### Detailed Answer

Add `Obsolete` field period — return both `customerId` and `clientId` for 2 releases.

Architect owns API governance policy.

### Architecture Perspective

API compatibility is architecture governance.

### Follow-up Questions

1. **Consumer-driven contracts? — Pact would catch before prod.**
2. **Breaking change in patch version? — Semantic versioning violation.**

### Common Mistakes in Interviews

- Rename without version bump
- No mobile app lag consideration
- No contract tests

---

## Q108: Thread Pool Starvation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

ASP.NET API hangs under load — thread pool starvation from sync-over-async.

### Short Answer (30 seconds)

`Task.Result`, `.Wait()`, blocking I/O on thread pool threads. Fix: async all the way, `Task.Run` only for CPU offload with care, diagnose with thread pool starvation events.

### Detailed Answer

.NET 6+ detects starvation — logs warning. Audit codebase for `.Result` in request path.

**Architect:** CI analyzer bans sync-over-async in API projects.

### Architecture Perspective

Async discipline prevents mysterious outages.

### Follow-up Questions

1. **Min threads config? — Emergency relief — not root fix.**
2. **Dedicated thread for CPU work? — `BackgroundService` queue.**

### Common Mistakes in Interviews

- Task.Result in controller
- sync I/O in async method
- Ignore thread pool starvation warnings

---

## Q109: Choose SQL vs Cosmos for New Service

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Product wants global low-latency reads, flexible schema, 50K writes/sec. SQL or Cosmos?

### Short Answer (30 seconds)

Cosmos if partition key clear, global distribution needed, document model fits. SQL if strong transactions, complex joins, team skill, cost at moderate scale.

### Detailed Answer

Decision matrix presentation to stakeholders with cost estimate. Hybrid: SQL for orders, Cosmos for product catalog.

**Document:** partition key design before Cosmos commitment.

### Architecture Perspective

Data store decision is architect signature moment.

### Follow-up Questions

1. **Cosmos hot partition? — Validate key cardinality with load test.**
2. **SQL scale limits? — Hyperscale or sharding path.**

### Common Mistakes in Interviews

- Cosmos because 'NoSQL faster'
- SQL without index plan at scale
- No partition key design for Cosmos

---

## Q110: Regulatory Audit Data Residency

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

EU regulator audits — customer data stored in US region.

### Short Answer (30 seconds)

Document data flows, migrate EU tenants to EU region, encryption in transit/at rest, DPA compliance, access logs for cross-border access.

### Detailed Answer

Architecture: geo-routing by tenant residency, separate DB per region, no replication across border without legal basis.

**Remediation plan** with timeline to auditor.

### Architecture Perspective

Compliance architecture is increasingly common.

### Follow-up Questions

1. **Schrems II implications? — Legal + architect collaboration.**
2. **Pseudonymization? — Reduce PII scope — architect enables.**

### Common Mistakes in Interviews

- Ignore tenant residency at design
- Global single DB for simplicity
- No audit trail for data access

---

## Q111: Black Friday Scale Plan

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

10x traffic in 2 weeks — architect checklist?

### Short Answer (30 seconds)

Load test 12x, scale out app tier, pre-warm cache, CDN, DB connection pool review, rate limit non-critical endpoints, freeze deploys 48h before, war room runbook.

### Detailed Answer

Identify bottleneck from load test — scale that tier. Queue non-critical work. Feature flag disable heavy features if needed.

**Rollback:** one-click scale down + feature flags.

### Architecture Perspective

Seasonal scale is planning not improvisation.

### Follow-up Questions

1. **Synthetic load shape? — Match previous year traffic curve.**
2. **Cost ceiling? — Pre-approve auto-scale max instances.**

### Common Mistakes in Interviews

- First load test on Black Friday
- Scale DB without app tier
- Deploy new feature week before

---

## Q112: Developer Wants Microservices

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Junior architect proposes 12 microservices for 5-person startup MVP.

### Short Answer (30 seconds)

Coach: modular monolith, single deploy, extract when pain real. Document Conway's Law — 5 people can't operate 12 services.

### Detailed Answer

Offer compromise: solution structure with clear modules, one database, API boundaries internal — prepare for future extraction.

**Mentoring** not dictating — explain ops cost.

### Architecture Perspective

Shows leadership without ego.

### Follow-up Questions

1. **Resume-driven architecture? — Name it gently — focus on outcomes.**
2. **When agree? — If 5 teams already assigned — different story.**

### Common Mistakes in Interviews

- Approve 12 services for MVP
- Dismiss without alternative
- No mentoring documentation

---

## Q113: Legacy .NET Framework Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

400K LOC .NET Framework 4.8 — migrate to .NET 8 strategy?

### Short Answer (30 seconds)

Assessment: Windows dependencies, ASP.NET WebForms/MVC version, third-party libs. Strangler: new features on .NET 8, bridge via API, migrate module by module. 2-3 year plan typical.

### Detailed Answer

Use .NET Upgrade Assistant for analysis. Not big bang unless small app.

**Interop:** host .NET Framework and .NET 8 side by side during transition.

### Architecture Perspective

Migration strategy is bread-and-butter architect work.

### Follow-up Questions

1. **Containerize Framework? — Windows containers — ops cost — bridge only.**
2. **Entity Framework version jump? — Major effort — plan per module.**

### Common Mistakes in Interviews

- Big bang rewrite
- Ignore third-party lib blockers
- No parallel run period

---

## Q114: Observability Gap Post-Incident

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

4-hour outage — cannot trace request across services. Post-incident architect actions?

### Short Answer (30 seconds)

Mandate OpenTelemetry, correlation ID middleware, structured logging, distributed tracing dashboard, SLO alerts. Blameless postmortem with action items.

### Detailed Answer

Week 1: trace ID in all logs. Month 1: OTel rollout. Quarter: SLO dashboards per service.

**Prevent:** synthetic monitoring on critical journeys.

### Architecture Perspective

Incidents drive observability investment — architect leads.

### Follow-up Questions

1. **Log aggregation? — Central ELK/App Insights — query by traceId.**
2. **MTTR improvement metric? — Track post-OTel deployment.**

### Common Mistakes in Interviews

- Add println debugging only
- No postmortem action tracking
- Same blind spot next incident

---

## Q115: Cost Overrun Azure Bill

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Azure bill 3x forecast — CTO escalation.

### Short Answer (30 seconds)

Cost Explorer: top resources, untagged sprawl, over-provisioned SKUs, verbose logging to Log Analytics, egress, forgotten dev environments.

### Detailed Answer

Quick wins: shutdown dev nights, right-size VMs, log sampling, reserved instances for baseline, budget alerts.

**Architect:** FinOps review in every design going forward.

### Architecture Perspective

Cost crisis requires immediate + preventive response.

### Follow-up Questions

1. **Log Analytics cost? — Often surprise — retention and ingestion volume.**
2. **Zombie resources? — Unattached disks, old snapshots.**

### Common Mistakes in Interviews

- Ignore until bill arrives
- Cut prod capacity blindly
- No tagging — cannot attribute

---

## Q116: AI Feature in Core Product

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

PM wants ChatGPT in checkout flow by next sprint.

### Short Answer (30 seconds)

Clarify: latency budget, PII handling, cost per request, fallback when API down, prompt injection risks. Propose RAG or API behind feature flag — not inline blocking call.

### Detailed Answer

Architecture: async suggestion service, cache common responses, content safety filter, no card data in prompts.

**ADR:** build vs Azure OpenAI vs third-party.

### Architecture Perspective

AI integration requires architect guardrails.

### Follow-up Questions

1. **Prompt injection? — Sanitize user input — separate system prompt.**
2. **Cost cap? — Token budget per session.**

### Common Mistakes in Interviews

- Sync OpenAI in payment path
- Send PII to model
- No fallback when AI unavailable

---

## Q117: Team Split Across Timezones

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Occasional |
| **Type** | Scenario |

### Question

US and India teams — async communication breaking architecture decisions?

### Short Answer (30 seconds)

ADR documents decisions, architecture decision records in Confluence, recorded design reviews, clear ownership per bounded context, overlap hours for sync decisions only.

### Detailed Answer

Reduce synchronous design meetings — written RFC with comment period. Escalation path for blocking disagreements.

### Architecture Perspective

Distributed team process is architect facilitation.

### Follow-up Questions

1. **RFC template? — Problem, options, recommendation, deadline.**
2. **Decision log? — Single source of truth — avoid Slack-only decisions.**

### Common Mistakes in Interviews

- Verbal decisions not documented
- No overlap for contentious choices
- Architecture by committee without owner

---

## Q118: Acquire Startup Integrate Stack

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Acquired startup on Node.js + Mongo — integrate with .NET Azure estate?

### Short Answer (30 seconds)

Assess: retain at boundary via API, strangler migrate high-value modules, or rewrite if tiny. Anti-corruption layer between stacks. Don't force immediate rewrite.

### Detailed Answer

6-month: API gateway routing, SSO integration, observability unified, security policy aligned.

18-month: migrate if business justifies — not ideology.

### Architecture Perspective

M&A integration is architect scenario.

### Follow-up Questions

1. **Team skill? — Retain Node team for their service initially.**
2. **Data sync? — Events between Mongo and SQL — eventual consistency.**

### Common Mistakes in Interviews

- Immediate full rewrite
- Two security models forever
- No ACL at boundary

---

## Q119: Principal Engineer Disagrees

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Principal proposes event sourcing everywhere. You disagree for CRUD admin module.

### Short Answer (30 seconds)

Engage with respect: document trade-offs, complexity cost, team skill, propose event sourcing for order aggregate only — CRUD stays simple EF.

### Detailed Answer

Written ADR with both options scored. Escalate to architecture review if stalemate. Data wins — pilot both if needed.

### Architecture Perspective

Conflict resolution without ego — architect soft skill.

### Follow-up Questions

1. **When principal right? — If audit replay legally required — reconsider.**
2. **Pilot scope? — One bounded context — measure complexity.**

### Common Mistakes in Interviews

- Acquiesce without discussion
- Public undermining
- No written trade-off analysis

---

## Q120: Graduation Readiness Self-Assessment

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Are you ready for Solution Architect interviews after Week 1?

### Short Answer (30 seconds)

Honest checklist: explain GC/async/value types with production examples, 5 ADRs written, week 1 assessment ≥70%, expert scenarios practiced aloud, identified 3 weak areas with plan.

### Detailed Answer

Week 1 is foundation — revisit weak topics in weeks 45-47 intensive. Record mock answers — compare to premium samples.

### Architecture Perspective

Self-assessment honesty expected.

### Follow-up Questions

1. **Weak area plan? — Log in progress tracker.**
2. **Next practice? — Month 1 Top 50 Q001-Q010.**

### Common Mistakes in Interviews

- Overconfidence without practice
- Skip expert scenarios
- No production examples in answers

---
