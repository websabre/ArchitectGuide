# Week 45 — Expert Scenario Q&A

> Q101–Q120: Premium format (Week 1 quality).

---


## Q101: Distributed Monolith Detection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Architecture |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

How detect and remediate a distributed monolith in .NET microservices?

### Short Answer (30 seconds)

Symptoms: synchronous chatty HTTP chains, shared database, coordinated deployments, circular dependencies. Remediate with async events, database-per-service, and strangler extraction.

### Detailed Answer

**Detection:** Dependency graph shows Order→Payment→Inventory→Order sync loop. One team's change requires three service deploys.

**Remediation:**
1. Introduce async `OrderPlaced` event
2. Split shared DB — bounded context schemas
3. Saga for cross-aggregate consistency

**Architect:** ADR with measurable exit criteria — deploy independence score.

### Architecture Perspective

Expert scenario — pattern names insufficient without remediation plan.

### Follow-up Questions

1. **Saga vs 2PC? — Saga with compensations — not distributed SQL transaction.**
2. **When reunify? — Rare — merge services if boundaries wrong.**

### Common Mistakes in Interviews

- More microservices without async boundary
- Shared EF DbContext across services
- Ignore deployment coupling metric

---

## Q102: EF N+1 at Scale Incident

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | EF Core |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

API latency doubled after feature release — how diagnose EF N+1?

### Short Answer (30 seconds)

Compare App Insights dependency count per request, enable EF sensitive logging in staging, find 1+N SQL pattern, fix with projection or Include, verify logical reads dropped.

### Detailed Answer

**Incident flow:**
1. p99 latency alert post-release
2. Dependency telemetry: 50 SQL calls per GET
3. Locate lazy load or loop query in new code path
4. Hotfix: `.Select()` projection deploy
5. Postmortem: CI query count assertion

**Architect:** ORM guardrails — max queries per request middleware in staging.

### Architecture Perspective

Production war story format — structured diagnosis.

### Follow-up Questions

1. **Query tags? — Tag EF queries with request route for tracing.**
2. **Permanent fix? — Read model or denormalized view.**

### Common Mistakes in Interviews

- Add Redis without fixing query count
- Disable lazy load in prod only without code fix
- No regression test on SQL count

---

## Q103: Async All the Way Refactor

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Async |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Legacy .NET library exposes sync API over async — refactor strategy?

### Short Answer (30 seconds)

Avoid `Task.Run` wrappers exposing fake sync. Add true async API, obsolete sync with analyzer warning, migrate callers incrementally.

### Detailed Answer

**Anti-pattern:**
```csharp
public void Save(Order o) => SaveAsync(o).GetAwaiter().GetResult();
```

**Strategy:** Dual API period — `SaveAsync` primary, sync deprecated.

**Architect:** Block new sync-over-async in CI analyzer rule.

### Architecture Perspective

Sync-over-async causes thread-pool starvation under load.

### Follow-up Questions

1. ** IAsyncEnumerable adoption? — Part of async modernization.**
2. **Library breaking change policy? — Semver major for sync removal.**

### Common Mistakes in Interviews

- Task.Run wrap every sync public API
- GetResult in ASP.NET request thread
- Remove sync without migration period

---

## Q104: Payment API Idempotent Retry

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Resilience |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Design idempotent payment POST with Polly retry for staff interview.

### Short Answer (30 seconds)

Client sends `Idempotency-Key` header; server stores key→response; retry returns same result without double charge; Polly retries only on transport/5xx before response received.

### Detailed Answer

**Server:**
```sql
CREATE UNIQUE INDEX ON IdempotencyKeys (Key, ClientId);
```

**Flow:**
1. Begin transaction, insert key if absent
2. Process payment
3. Store response payload with key
4. Commit

**Conflict:** Duplicate key same body → return cached 200; different body → 409.

**Architect:** Payment gateway webhook dedup uses same pattern.

### Architecture Perspective

Money + retry = idempotency mandatory — expert money question.

### Follow-up Questions

1. **Stripe idempotency? — Industry reference implementation.**
2. **Outbox for webhook? — At-least-once delivery requires dedup.**

### Common Mistakes in Interviews

- Retry POST without key
- Store idempotency only in memory
- Different response for duplicate key

---

## Q105: Cache Invalidation Multi-Instance

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Caching |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Design cache invalidation across 12 AKS pods without stale reads.

### Short Answer (30 seconds)

Redis pub/sub or Redis key delete on write + short L1 TTL; or HybridCache tags; never rely on in-memory only.

### Detailed Answer

**Pattern:**
1. Write to DB
2. Delete Redis key `product:{id}`
3. Publish `invalidate:product:{id}` — pods evict L1

**Alternative:** No L1 — Redis only — simpler consistency.

**Architect:** Measure stale read SLA — catalog may tolerate 5s; pricing cannot.

### Architecture Perspective

Multi-instance cache is classic distributed systems trap.

### Follow-up Questions

1. **Eventual consistency UX? — Version number in response.**
2. **CDN cache purge? — Separate layer — API invalidation + CDN purge API.**

### Common Mistakes in Interviews

- IMemoryCache only on 12 pods
- Invalidate without pub/sub
- Infinite TTL on price data

---

## Q106: MediatR Pipeline Transaction

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | MediatR |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Implement transaction boundary in MediatR pipeline — pitfalls?

### Short Answer (30 seconds)

Wrap command handlers in transaction behavior — but exclude queries; nested transactions and external HTTP inside transaction are pitfalls.

### Detailed Answer

```csharp
public async Task<T> Handle(TRequest req, ...) {
  await using var tx = await _db.Database.BeginTransactionAsync();
  var result = await next();
  await tx.CommitAsync();
  return result;
}
```

**Pitfalls:** HTTP call inside transaction holds locks; retry entire transaction on transient failure.

**Architect:** Commands only; read handlers skip; keep transactions short.

### Architecture Perspective

Transaction behavior is expert MediatR topic with failure modes.

### Follow-up Questions

1. **Outbox same transaction? — Include outbox insert in same tx.**
2. **Isolation level? — Serializable rarely needed — default READ COMMITTED.**

### Common Mistakes in Interviews

- Transaction on query handler
- External API inside SQL transaction
- Long-running transaction minutes

---

## Q107: API Version Migration Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | API Design |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Migrate 200 enterprise clients from v1 to v2 without outage.

### Short Answer (30 seconds)

Run v1 and v2 parallel, sunset headers, client outreach, usage dashboard, v1 read-only phase, contract tests ensuring v2 superset, rate limit v1 eventually.

### Detailed Answer

**Phases:**
1. v2 release — feature parity checklist
2. 6-month dual run — metrics on v1 traffic
3. v1 freeze — security patches only
4. v1 shutdown — 410 Gone with link to v2

**Architect:** Partner SDK update cadence coordinated with PM.

### Architecture Perspective

API migration is program management plus engineering.

### Follow-up Questions

1. **Adapter layer? — v1 controller translates to v2 handlers internally.**
2. **Breaking field rename? — v2 new field, v1 maps deprecated.**

### Common Mistakes in Interviews

- Big-bang v1 off without usage data
- Breaking change without major version
- No adapter — force all clients same day

---

## Q108: Testing Pyramid Microservices

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Testing |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Design test strategy for 40-microservice .NET platform.

### Short Answer (30 seconds)

Unit per service, contract tests between pairs, integration per service with Testcontainers, few E2E journeys, chaos in staging, synthetic prod monitoring.

### Detailed Answer

**Contract:** Pact — consumer-driven — CI fails breaking provider change.

**E2E:** Checkout happy path only — not 40-service graph every commit.

**Architect:** Test ownership — provider verifies contracts; platform supplies fixtures.

### Architecture Perspective

Expert testing is economics — confidence per minute of CI.

### Follow-up Questions

1. **Ephemeral environments? — Preview env per PR with subset services.**
2. **Test data management? — Anonymized fixtures — not prod copy.**

### Common Mistakes in Interviews

- Only manual QA across 40 services
- E2E every PR full graph
- No contract tests — breaking consumers monthly

---

## Q109: HttpClient Factory Platform Standard

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | HTTP |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Define organization-wide HttpClient factory standard.

### Short Answer (30 seconds)

Typed clients, 2-min PooledConnectionLifetime, standard resilience handler, correlation ID handler, mTLS where required — template in shared `ServiceDefaults` project.

### Detailed Answer

**ServiceDefaults (.NET Aspire pattern):**
- AddServiceDiscovery
- AddStandardResilienceHandler
- ConfigureHttpClientDefaults

**Governance:** Arch unit tests ban `new HttpClient()`.

**Architect:** Platform team ships package — apps add one line.

### Architecture Perspective

Platform standards scale reliability across dozens of teams.

### Follow-up Questions

1. **mTLS between services? — Cert rotation via cert-manager.**
2. **Service discovery? — K8s DNS vs Aspire service discovery.**

### Common Mistakes in Interviews

- Each team custom HttpClient hacks
- No standard resilience
- Ban not enforced in analyzers

---

## Q110: Repository CQRS Split

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Data Access |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Split command repository and query handlers in CQRS — design review.

### Short Answer (30 seconds)

Commands: aggregate repository, tracked entities, domain events. Queries: Dapper/EF no-tracking projections, skip repository abstraction, optimized SQL per screen.

### Detailed Answer

**Command side:**
`IOrderRepository.Save(Order aggregate)`

**Query side:**
`GetOrderSummaryQueryHandler` uses raw SQL or `FromSql` read model.

**Architect:** Don't force repository on read side — different optimization needs.

### Architecture Perspective

CQRS split is expert data access architecture.

### Follow-up Questions

1. **Shared model anti-pattern? — Separate read/write schemas.**
2. **Event sourcing read side? — Projections from event log.**

### Common Mistakes in Interviews

- Same EF entity for command and complex read
- Repository with 40 query methods
- CQRS on 5-table CRUD app unnecessarily

---

## Q111: Minimal API Monolith Growth

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | ASP.NET Core |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Minimal API service grew to 80 endpoints — refactor plan?

### Short Answer (30 seconds)

Extract endpoint modules per feature, introduce MediatR handlers, Carter modules or `IEndpointRouteBuilder` extension methods, separate assemblies per bounded context.

### Detailed Answer

```csharp
public static class OrderEndpoints {
  public static void MapOrders(this IEndpointRouteBuilder app) { ... }
}
```

**Program.cs:** Only composition — `app.MapOrderEndpoints()`.

**Architect:** Strangler to controllers optional — structure matters not pattern swap.

### Architecture Perspective

Growth path for Minimal APIs without rewrite.

### Follow-up Questions

1. **Carter library? — Convention-based module discovery.**
2. **OpenAPI per module? — Tags group endpoints.**

### Common Mistakes in Interviews

- Keep growing Program.cs
- Rewrite to MVC big-bang
- No feature folders at 80 endpoints

---

## Q112: Exception Taxonomy Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | ASP.NET Core |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Design exception hierarchy for multi-team .NET platform.

### Short Answer (30 seconds)

Base `AppException` with ErrorCode; derived `NotFoundException`, `ConflictException`, `ValidationException`; global handler maps to HTTP; never throw for expected business failures where Result fits.

### Detailed Answer

**Error codes:** `ORDER_NOT_FOUND` stable for clients — not exception type names.

**Teams:** Extend taxonomy in namespace — `Payments.InsufficientFundsException`.

**Architect:** Published error catalog for API consumers.

### Architecture Perspective

Exception taxonomy is API contract governance.

### Follow-up Questions

1. **Result vs exception? — Result for expected; exception for exceptional.**
2. **ProblemDetails type field? — URI to error documentation.**

### Common Mistakes in Interviews

- string throw messages only
- Each team different HTTP mapping
- Exception for control flow everywhere

---

## Q113: DI Scope in Blazor Server

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Dependency Injection |
| **Frequency** | Occasional |
| **Type** | Scenario |

### Question

Explain scoped service pitfalls in Blazor Server vs Blazor WASM.

### Short Answer (30 seconds)

Blazor Server circuits can outlive HTTP request — scoped services live for circuit duration — DbContext held too long. Use `IDbContextFactory` or explicit scope per operation.

### Detailed Answer

**Circuit-scoped:** User state OK; DbContext dangerous.

**Fix:**
```csharp
await using var ctx = await _factory.CreateDbContextAsync();
```

**Architect:** Document Blazor lifetime differences in platform guide — WASM aligns with web request scope.

### Architecture Perspective

Blazor Server lifetime surprises senior .NET architects.

### Follow-up Questions

1. **Singleton state in Blazor Server? — User-specific data wrong.**
2. **Interactive Auto render? — .NET 8+ mixed — know scope.**

### Common Mistakes in Interviews

- Scoped DbContext entire circuit
- Assume Blazor same as MVC request scope
- No factory for long-lived components

---

## Q114: Polly Chaos Testing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Resilience |
| **Frequency** | Occasional |
| **Type** | Scenario |

### Question

Validate Polly policies with chaos testing.

### Short Answer (30 seconds)

Inject faulting handler in staging — random 503, latency spike — verify circuit opens, retries bounded, dashboards alert.

### Detailed Answer

**Tools:** Toxiproxy, Chaos Mesh, custom `DelegatingHandler` in test env.

**Assertions:** Circuit state metrics, no retry storm, fallback UI path works.

**Architect:** Game day quarterly — inject payment outage — verify order queue behavior.

### Architecture Perspective

Resilience policies untested are wishful thinking.

### Follow-up Questions

1. **Fault injection prod? — Only controlled tiny blast radius.**
2. **Retry budget? — Max retries per minute globally.**

### Common Mistakes in Interviews

- Policies never tested under failure
- Chaos only in unit tests with mocks
- No metrics on circuit state

---

## Q115: SOLID Refactor Legacy Monolith

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | SOLID |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Prioritize SOLID refactor on 500K-line .NET monolith.

### Short Answer (30 seconds)

Strangler: extract highest-churn module first, introduce interfaces at seam, don't boil ocean. Measure coupling with NDepend/architecture tests.

### Detailed Answer

**Priority:**
1. Payment calculation — highest business risk
2. Introduce `IPricingStrategy` at boundary
3. Tests around extracted module
4. Deploy in-process first — microservice later

**Architect:** Refactor for change velocity — not diagram purity.

### Architecture Perspective

Expert legacy answer — incremental with metrics.

### Follow-up Questions

1. **Architecture tests? — NetArchTest enforce layer dependencies.**
2. **Big bang rewrite? — Reject unless business mandates.**

### Common Mistakes in Interviews

- SOLID refactor entire codebase freeze
- Extract microservice before modular monolith
- No tests before seam extraction

---

## Q116: Design Pattern Overuse Review

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Design Patterns |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Architecture review flags pattern over-engineering — response?

### Short Answer (30 seconds)

Acknowledge YAGNI — remove unused abstractions, keep extension points only at proven variation boundaries, simplify to direct service if one implementation.

### Detailed Answer

**Review finding:** Factory + Abstract Factory + Builder for single PDF export.

**Response:** Collapse to `IInvoiceGenerator` one implementation until second format required.

**Architect:** Patterns earn their complexity — document trigger for reintroduction.

### Architecture Perspective

Expert judgment — when not to use patterns.

### Follow-up Questions

1. **Rule of three? — Third variant triggers abstraction.**
2. **ADR for simplification? — Record deliberate removal.**

### Common Mistakes in Interviews

- Add patterns to satisfy checklist
- Reject all patterns always
- Keep unused interfaces 'for future'

---

## Q117: Staff Interview System Trade-off

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Interview Skills |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Staff interview: 'Use repository, MediatR, and microservices?' — respond.

### Short Answer (30 seconds)

Clarify scale, team size, and change rate. Propose modular monolith with MediatR optional, repository at aggregate boundary only, microservices when deploy independence proven necessary.

### Detailed Answer

**Framework:**
- 8 engineers, 2 deploys/week pain → modular monolith + vertical slices
- Repository on write model only
- MediatR if >20 endpoints
- Revisit microservices when bounded contexts stabilize

**Staff signal:** Trade-off narrative with triggers — not default buzzword stack.

### Architecture Perspective

Staff level — justify stack to context.

### Follow-up Questions

1. **What would change answer? — 50 engineers, independent scaling proof.**
2. **Document triggers in ADR? — Team size, QPS, compliance.**

### Common Mistakes in Interviews

- Yes to everything interviewer lists
- Reject patterns without context questions
- No measurable adoption triggers

---

## Q118: Production Middleware Incident

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | ASP.NET Core |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Auth broke after middleware reorder deploy — diagnosis?

### Short Answer (30 seconds)

Compare middleware pipeline diff, find authorization before authentication or endpoint before routing, fix order, add integration test asserting 401/403 behavior.

### Detailed Answer

**Timeline:** Deploy → spike 401 for valid users → rollback → diff `Program.cs` middleware order.

**Prevention:** `Program.cs` middleware extension with enforced order; architecture test.

**Architect:** Treat middleware order as contract — code review checklist.

### Architecture Perspective

Real incident pattern — middleware order regression.

### Follow-up Questions

1. **Pipeline snapshot test? — Integration test hits authorized endpoint.**
2. **Feature flag middleware? — Order changes behind flag — canary.**

### Common Mistakes in Interviews

- Manual order in every service divergent
- No auth integration tests
- Rollback without root cause doc

---

## Q119: Cross-Cutting Observability Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Observability |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Design observability for 25 .NET APIs — logging, metrics, traces.

### Short Answer (30 seconds)

OpenTelemetry SDK, OTLP export to Azure Monitor, standard ActivitySource per service, Serilog with traceId enrichment, RED metrics (rate, errors, duration) per endpoint.

### Detailed Answer

**Standards:**
- Correlation + trace ID propagation
- Structured JSON logs
- `http.server.request.duration` histogram
- Alerts on SLO burn rate

**Architect:** Shared `ServiceDefaults` package — one-line enable per service.

### Architecture Perspective

Observability platform decision — not per-team snowflake.

### Follow-up Questions

1. **Log vs trace? — Logs for events; traces for latency breakdown.**
2. **Cardinality explosion? — Limit custom metric labels.**

### Common Mistakes in Interviews

- Plain text logs no correlation
- 25 different observability stacks
- Metrics per internal method — cardinality blowup

---

## Q120: API Platform Governance

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Architecture |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Govern 30 teams building .NET APIs on shared platform.

### Short Answer (30 seconds)

Golden path template: ServiceDefaults, auth, ProblemDetails, versioning policy, arch unit tests, API review for public surfaces, Backstage catalog.

### Detailed Answer

**Enforcement:**
- CI arch tests fail wrong layer references
- APIM publishes approved OpenAPI only
- Exception taxonomy shared package

**Freedom:** Internal services less rigid than public partner APIs.

**Architect:** Govern outcomes (security, observability) not implementation details (Minimal vs MVC).

### Architecture Perspective

Platform governance is staff architect scope.

### Follow-up Questions

1. **Golden path vs guardrails? — Template optional but policy mandatory.**
2. **Escape hatch process? — ADR for exceptions.**

### Common Mistakes in Interviews

- No standards — 30 snowflake APIs
- Mandate identical domain model across teams
- Governance without template support

---
