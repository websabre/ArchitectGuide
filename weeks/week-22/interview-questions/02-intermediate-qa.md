# Week 22 — Intermediate Q&A

> Q031–Q070: Premium format (Week 1 quality).

---


## Q031: Service Decomposition

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Decomposition |
| **Frequency** | Very Common |

### Question

How do you decompose a monolith into microservices?

### Short Answer (30 seconds)

Identify bounded contexts via domain events and team structure. Extract highest-value, lowest-coupling module first. Strangler fig routing. Avoid big-bang.

### Detailed Answer (3–5 minutes)

Use Event Storming or domain workshops. Score candidates: deployment frequency pain, scale mismatch, team boundary alignment.

First extraction often: notification, catalog, or payment — clear boundaries.

Keep monolith data accessible via API during transition — don't big-bang database split.

### Architecture Perspective

Decomposition strategy is top microservices interview question.

### Follow-up Questions

1. **Monolith first? — Modular monolith validates domain before distributed ops complexity.**
2. **Shared library vs service? — Share domain types cautiously — prefer API contracts.**

### Common Mistakes in Interviews

- Split by technical layer (API service, DB service)
- Microservices day one for 3 developers
- No strangler — big bang rewrite

---

## Q032: API Gateway Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Gateway |
| **Frequency** | Very Common |

### Question

What belongs in API gateway vs microservices?

### Short Answer (30 seconds)

Gateway: TLS, auth, rate limit, routing, request ID, CORS. Services: domain logic, validation, data access.

### Detailed Answer (3–5 minutes)

Azure APIM policies: validate JWT, throttle, cache GET responses, route `/api/orders/*`.

Don't put business rules in gateway — drifts from services, untestable domain logic at edge.

### Architecture Perspective

Gateway is cross-cutting edge — not second business layer.

### Follow-up Questions

1. **Gateway aggregation? — GraphQL or BFF sometimes better than fat gateway.**
2. **mTLS at gateway? — Terminate TLS at gateway or pass-through — compliance decision.**

### Common Mistakes in Interviews

- Business validation in APIM policy
- Gateway becomes god object
- No rate limiting on public endpoints

---

## Q033: Database Per Service

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Data |
| **Frequency** | Very Common |

### Question

Explain database-per-service and reporting challenge.

### Short Answer (30 seconds)

Each service owns schema — no cross-DB FK. Reporting via data warehouse fed by events or CDC.

### Detailed Answer (3–5 minutes)

Order service: Order DB. Inventory: Inventory DB. Join in application via API or denormalized read model.

Analytics: Azure Synapse / Snowflake ingests domain events nightly.

### Architecture Perspective

Data ownership enables independent deploy.

### Follow-up Questions

1. **Shared database antipattern? — Hidden monolith — coupling at schema level.**
2. **CDC for reporting? — Debezium streams changes to warehouse.**

### Common Mistakes in Interviews

- Distributed JOIN across service DBs
- Reporting queries on OLTP primary
- Shared tables between teams

---

## Q034: Sync vs Async Communication

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Communication |
| **Frequency** | Very Common |

### Question

When HTTP sync vs message async between services?

### Short Answer (30 seconds)

Sync when user waits (get order total). Async for side effects (email, analytics). Max 2-3 sync hops.

### Detailed Answer (3–5 minutes)

Checkout: sync payment authorization. Post-order: async notification, inventory sync, search index update.

Circuit breaker + timeout on every sync call.

### Architecture Perspective

Communication choice defines latency and resilience.

### Follow-up Questions

1. **Request-response over Kafka? — Anti-pattern — use HTTP or true async events.**
2. **Timeout values? — Shorter than client timeout — fail fast with fallback.**

### Common Mistakes in Interviews

- 6-service sync chain for page load
- Async without dead letter queue
- No timeout on HttpClient

---

## Q035: Circuit Breaker

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Resilience |
| **Frequency** | Very Common |

### Question

Implement circuit breaker for inventory service calls.

### Short Answer (30 seconds)

After failure threshold, open circuit — fail fast. Half-open test request. Polly in .NET HttpClient factory.

### Detailed Answer (3–5 minutes)

Configure per dependency — payment stricter than recommendations.

Pair with fallback: cached catalog, degraded mode banner.

Monitor circuit state metric — alert when open.

### Architecture Perspective

Resilience patterns are architect checklist items.

### Follow-up Questions

1. **Bulkhead with circuit breaker? — Isolate thread pools per downstream.**
2. **Retry with circuit open? — Don't retry when open — wastes resources.**

### Common Mistakes in Interviews

- Circuit breaker without monitoring
- Infinite retry on 500 errors
- Same policy for all dependencies

---

## Q036: BFF Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | API Design |
| **Frequency** | Common |

### Question

Mobile app needs aggregated homepage. BFF or generic API?

### Short Answer (30 seconds)

BFF per client type — MobileBFF aggregates 3 calls into one payload shaped for mobile screens.

### Detailed Answer (3–5 minutes)

Web BFF and Mobile BFF separate — different data needs. BFF calls microservices server-side — reduces client chattiness.

Don't let BFF become monolith — thin orchestration only.

### Architecture Perspective

BFF solves client-specific API shape problem.

### Follow-up Questions

1. **GraphQL vs BFF? — GraphQL flexible queries; BFF explicit endpoints — team skill trade-off.**
2. **BFF auth? — BFF holds service-to-service tokens — not exposed to mobile.**

### Common Mistakes in Interviews

- One API for web and mobile forever
- Mobile calls 15 microservices directly
- Fat BFF with domain logic

---

## Q037: Contract Testing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Testing |
| **Frequency** | Common |

### Question

How ensure payment service change doesn't break order service?

### Short Answer (30 seconds)

Consumer-driven contracts (Pact): order service defines expected payment API contract; CI verifies payment provider satisfies it.

### Detailed Answer (3–5 minutes)

Complement with smoke E2E — don't rely on E2E alone — slow and flaky at scale.

Version APIs — breaking changes require contract major version bump.

### Architecture Perspective

Contract tests enable independent deploy.

### Follow-up Questions

1. **Pact broker? — Central contract repository — CI gate on publish.**
2. **Backward compatibility rule? — Additive changes only in minor version.**

### Common Mistakes in Interviews

- E2E only integration testing
- Breaking API without version bump
- No consumer notification on contract change

---

## Q038: Service Mesh When

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Infrastructure |
| **Frequency** | Occasional |

### Question

When adopt Istio/Linkerd service mesh?

### Short Answer (30 seconds)

15+ services needing uniform mTLS, traffic splitting, observability without library instrumentation in every app.

### Detailed Answer (3–5 minutes)

Cost: sidecar memory, operational complexity. Start with Polly + centralized logging for <10 services.

Mesh wins: polyglot services, canary by percentage, zero-trust east-west.

### Architecture Perspective

Mesh is infrastructure decision with ops cost.

### Follow-up Questions

1. **Sidecar latency? — ~1-2ms per hop — measure at your scale.**
2. **Mesh without observability backend? — Telemetry needs destination.**

### Common Mistakes in Interviews

- Mesh for 3-service system
- No team to operate Istio
- Ignoring sidecar resource cost

---

## Q039: Strangler Fig Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Migration |
| **Frequency** | Very Common |

### Question

Migrate order module from .NET monolith to microservice.

### Short Answer (30 seconds)

Proxy routes `/api/orders/*` to new service; monolith handles rest. Gradually move endpoints. Shared DB initially OK — then split schema.

### Detailed Answer (3–5 minutes)

Phase 1: new service wraps same DB tables (pragmatic). Phase 2: split schema. Phase 3: retire monolith path.

Feature flags control traffic percentage to new service.

### Architecture Perspective

Strangler reduces migration risk.

### Follow-up Questions

1. **Anti-corruption layer? — Translate monolith models to new domain model at boundary.**
2. **Rollback plan? — Route 100% back to monolith via proxy config.**

### Common Mistakes in Interviews

- Big bang cutover on Friday
- No traffic shadowing before cutover
- Delete monolith before parity verified

---

## Q040: Microservices Anti-Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Anti-Patterns |
| **Frequency** | Common |

### Question

Name three microservices anti-patterns you've seen.

### Short Answer (30 seconds)

Distributed monolith (deploy together, shared DB). Chatty microservices (20 calls per page). Nano-services (network overhead dominates).

### Detailed Answer (3–5 minutes)

**Detection:** Cannot deploy service alone; integration tests need all services; p99 dominated by network not work.

**Fix:** Merge services, add BFF aggregation, or consolidate boundaries.

### Architecture Perspective

Naming anti-patterns shows production experience.

### Follow-up Questions

1. **Gold plating? — Kubernetes for team of 3.**
2. **Smart endpoints dumb pipes? — Domain logic in services not ESB.**

### Common Mistakes in Interviews

- Microservices for resume
- No correlation ID across calls
- Shared ORM models across services

---

## Q041: Service Boundary Discovery

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Decomposition |
| **Frequency** | Very Common |

### Question

How do you discover microservice boundaries in a brownfield e-commerce monolith?

### Short Answer (30 seconds)

Event Storming workshops, dependency graph analysis, change coupling metrics, and team Conway alignment. Extract where business capability, data, and deployment pain intersect.

### Detailed Answer (3–5 minutes)

**Workshop output:** Domain events on timeline — `OrderPlaced`, `PaymentCaptured`, `ShipmentDispatched`. Cluster events into bounded contexts.

**Metrics:** Services that change together (git co-change) shouldn't split yet.

**First candidate:** Notification or catalog — clear API, low cross-context transactions.

**Architect:** Validate boundary with 'can this team deploy independently without coordinating schema migration?'

### Architecture Perspective

Boundary discovery is collaborative domain work not just drawing boxes.

### Follow-up Questions

1. **Transaction boundary test? — If two modules need same DB transaction often — maybe same service.**
2. **Conway's Law? — Service boundaries should align with team communication structure.**

### Common Mistakes in Interviews

- Split by technical layer (API service, DB service)
- Boundaries from org chart without domain analysis
- Ignore data coupling in dependency graph

---

## Q042: API Gateway Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Gateway |
| **Frequency** | Very Common |

### Question

Compare single gateway, per-domain gateway, and mesh ingress. When each?

### Short Answer (30 seconds)

Single gateway: small fleet, one team. Per-domain: multiple gateways by business area. Mesh ingress: K8s with Istio/Contour per cluster — gateway at platform layer.

### Detailed Answer (3–5 minutes)

**Single (APIM):** `/api/*` routes to services — good <15 services.

**Per-domain:** `orders-api.company.com`, `catalog-api.company.com` — separate rate limits, WAF rules, teams own routing.

**Patterns in gateway:** TLS termination, JWT validation, rate limit, request ID, routing — not business rules.

**Architect:** Gateway sprawl risk — platform team owns standards; domain teams own route config via GitOps.

### Architecture Perspective

Gateway topology scales with org structure.

### Follow-up Questions

1. **Gateway aggregation vs BFF? — BFF when client-specific shaping; gateway stays thin.**
2. **mTLS passthrough? — Compliance may require end-to-end encryption past gateway.**

### Common Mistakes in Interviews

- Business validation in gateway policies
- God gateway with 200 routes one team
- No rate limiting on public endpoints

---

## Q043: BFF Per Client

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | API Design |
| **Frequency** | Common |

### Question

Web and mobile need different order payloads. Design BFF layer.

### Short Answer (30 seconds)

MobileBFF: compact JSON, fewer round trips, image URLs sized for device. WebBFF: richer data, SEO metadata. Each BFF orchestrates microservice calls server-side.

### Detailed Answer (3–5 minutes)

**Structure:**
- `MobileBff` → OrderService + CatalogService → single `/mobile/home`
- `WebBff` → same services → `/web/home` with more fields

**Auth:** BFF holds service-to-service tokens; mobile never calls 5 microservices directly.

**Architect:** Keep BFF thin — orchestration and shaping only. Domain logic stays in services.

### Architecture Perspective

BFF solves client-specific API ergonomics.

### Follow-up Questions

1. **GraphQL vs BFF? — GraphQL flexible queries; BFF explicit endpoints — team skill trade-off.**
2. **One BFF forever? — Add new BFF per major client type (partner API, admin portal).**

### Common Mistakes in Interviews

- Mobile app calls 12 microservices directly
- Fat BFF with business rules and EF Core
- Shared BFF for web and mobile with compromise payload

---

## Q044: Database Per Service Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Data |
| **Frequency** | Very Common |

### Question

Extract order service from monolith DB — phased migration plan?

### Short Answer (30 seconds)

Phase 1: service owns API, reads/writes monolith tables (pragmatic). Phase 2: dual-write or CDC sync to new schema. Phase 3: cut read traffic. Phase 4: retire monolith writes.

### Detailed Answer (3–5 minutes)

**Patterns:**
- **Strangler on schema:** views and triggers bridge during transition
- **CDC:** Debezium captures monolith changes → new Order DB
- **Anti-corruption layer:** translate legacy row shape to domain model

**Reporting:** Warehouse ingests events — no cross-DB JOINs in prod.

**Architect:** Never big-bang schema split on Friday. Rollback = route traffic back, not reverse migration.

### Architecture Perspective

DB migration is highest-risk microservices step.

### Follow-up Questions

1. **Shared tables interim OK? — Time-boxed with explicit exit criteria.**
2. **Saga for cross-service data? — Eventual consistency during split.**

### Common Mistakes in Interviews

- Big-bang schema cutover
- Distributed JOIN across service DBs in prod
- No CDC validation before cutover

---

## Q045: Sync vs Async Communication

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Communication |
| **Frequency** | Very Common |

### Question

Checkout flow — classify each step as sync HTTP or async messaging.

### Short Answer (30 seconds)

Sync (user waits): validate cart, authorize payment, return confirmation. Async: send email, update search index, analytics, loyalty points.

### Detailed Answer (3–5 minutes)

**Rules:**
- User-facing path: max 2–3 sync hops with timeout budgets
- Side effects: always async with outbox
- Sync failure blocks UX; async failure retries with DLQ

**Example:** `POST /checkout` syncs payment; publishes `OrderPlaced` → inventory, email, warehouse consume async.

**Architect:** Document communication matrix in service catalog — prevents ad-hoc HTTP chains.

### Architecture Perspective

Sync/async choice defines latency and resilience.

### Follow-up Questions

1. **Request-reply over Kafka? — Anti-pattern — use HTTP or true fire-and-forget events.**
2. **Choreography default? — Prefer events for side effects; sync only when user needs answer now.**

### Common Mistakes in Interviews

- 6-service sync chain for page load
- Email send blocks checkout response
- Async without dead letter queue

---

## Q046: Circuit Breaker Polly

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Resilience |
| **Frequency** | Very Common |

### Question

Configure Polly circuit breaker in .NET HttpClientFactory for inventory client.

### Short Answer (30 seconds)

```csharp
services.AddHttpClient<IInventoryClient, InventoryClient>()
    .AddStandardResilienceHandler(options => {
        options.CircuitBreaker.SamplingDuration = TimeSpan.FromSeconds(30);
        options.CircuitBreaker.FailureRatio = 0.5;
        options.CircuitBreaker.MinimumThroughput = 10;
        options.CircuitBreaker.BreakDuration = TimeSpan.FromSeconds(30);
    });
```
Open after 50% failures in 30s window (min 10 requests). Break 30s then half-open.

### Detailed Answer (3–5 minutes)

**Architect standards:**
- Named client per dependency
- Fallback policy returns cached stock or 'availability unknown'
- Log circuit state transitions

**.NET 8+:** `Microsoft.Extensions.Http.Resilience` replaces ad-hoc Polly wiring.

### Architecture Perspective

Polly configuration is hands-on architect skill for .NET shops.

### Follow-up Questions

1. **Half-open behavior? — Trial request — success closes circuit.**
2. **Combine with retry? — Retry transient before breaker counts failure — configure pipeline order.**

### Common Mistakes in Interviews

- Circuit breaker without HttpClientFactory
- Same resilience pipeline all dependencies
- No fallback when circuit open

---

## Q047: Bulkhead Thread Pools

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Resilience |
| **Frequency** | Common |

### Question

Isolate thread pools for payment and analytics HTTP calls in ASP.NET Core.

### Short Answer (30 seconds)

Separate `IHttpClientFactory` named clients with Polly bulkhead — payment max 20 parallel, analytics max 5. Analytics backlog cannot starve payment threads.

### Detailed Answer (3–5 minutes)

**Implementation:**
```csharp
.AddResilienceHandler("payment-bulkhead", b =>
    b.AddBulkhead(new BulkheadStrategyOptions {
        MaxParallelization = 20,
        MaxQueuedActions = 40
    }));
```

**K8s complement:** Separate deployments for batch vs API if bulkhead insufficient.

**Architect:** Size from load test — payment pool = peak concurrent checkouts × downstream calls.

### Architecture Perspective

Thread pool bulkhead protects critical path.

### Follow-up Questions

1. **Bulkhead rejection? — Return 503 fast — better than slow timeout.**
2. **Sync-over-async breaks bulkhead? — Fix root cause — async all the way.**

### Common Mistakes in Interviews

- Single pool for all outbound HTTP
- Unbounded bulkhead queue
- No monitoring on bulkhead rejections

---

## Q048: Strangler Fig Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Migration |
| **Frequency** | Very Common |

### Question

Strangler fig routing for `/api/orders` — design proxy rules and validation gates.

### Short Answer (30 seconds)

Reverse proxy (YARP, APIM, nginx) routes by path prefix. Start 0% new service, shadow traffic, then 10% → 50% → 100% with feature flag.

### Detailed Answer (3–5 minutes)

**Phases:**
1. Proxy all `/api/orders/*` to monolith (baseline)
2. Implement new service — route `GET /orders/{id}` only
3. Shadow: duplicate requests, compare responses
4. Canary: route percentage by header or flag
5. Retire monolith handler

**Architect:** Parity checklist — response schema, error codes, latency SLO before each traffic shift.

### Architecture Perspective

Strangler fig is standard brownfield microservices pattern.

### Follow-up Questions

1. **Anti-corruption layer at boundary? — Translate monolith DTOs to new domain model.**
2. **Rollback? — Single config change routes 100% back to monolith.**

### Common Mistakes in Interviews

- Big bang cutover without shadow
- No automated response diff in shadow phase
- Delete monolith code before parity verified

---

## Q049: Service Mesh Istio When

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Infrastructure |
| **Frequency** | Occasional |

### Question

15 microservices, mixed .NET and Python — when justify Istio adoption?

### Short Answer (30 seconds)

Justify when: uniform mTLS east-west, canary by percentage, observability without per-language SDK, 15+ services with platform team to operate mesh.

### Detailed Answer (3–5 minutes)

**Cost:** Sidecar ~50–100MB RAM per pod, ~1–2ms latency per hop, Istio control plane ops.

**Start without mesh:** Polly + centralized OTel + APIM for <10 services.

**Mesh wins:** Polyglot, zero-trust network, traffic shifting without app changes.

**Architect:** Pilot on non-critical service; measure p99 overhead before fleet-wide.

### Architecture Perspective

Mesh is infrastructure bet with real ops cost.

### Follow-up Questions

1. **Sidecar vs ambient mesh? — Istio ambient reduces per-pod sidecar — evaluate maturity.**
2. **Mesh without observability backend? — Telemetry needs Jaeger/Prometheus destination.**

### Common Mistakes in Interviews

- Istio for 3-service team
- No platform team for mesh upgrades
- Ignore sidecar memory in node sizing

---

## Q050: Contract Testing Pact

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Testing |
| **Frequency** | Common |

### Question

Set up Pact between order service (consumer) and payment service (provider).

### Short Answer (30 seconds)

Consumer writes pact defining expected `POST /payments` request/response. Provider CI verifies against published pacts. Pact Broker gates deploy.

### Detailed Answer (3–5 minutes)

**Flow:**
1. Order service tests define interaction expectations
2. Pact file published to broker
3. Payment service `verify-pacts` job in CI
4. `can-i-deploy` checks compatibility before prod

**Architect:** Consumer-driven — order team defines what they need; payment must not break contract without negotiation.

### Architecture Perspective

Pact enables independent deploy with confidence.

### Follow-up Questions

1. **Pact vs OpenAPI? — OpenAPI is provider schema; Pact is consumer expectations verified.**
2. **Breaking change process? — Major pact version bump + consumer update before provider deploy.**

### Common Mistakes in Interviews

- E2E only integration testing
- Provider changes API without pact verification
- No broker — pacts lost on developer laptops

---

## Q051: Consumer-Driven Contracts

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Testing |
| **Frequency** | Common |

### Question

Why consumer-driven contracts vs provider-published OpenAPI only?

### Short Answer (30 seconds)

Provider OpenAPI documents what exists; consumer-driven captures what is actually used — prevents unused breaking changes and catches provider drift on consumed fields.

### Detailed Answer (3–5 minutes)

**Scenario:** Payment adds required field — OpenAPI updated — but order service didn't need it. Consumer-driven pact only tests order's subset.

**Org process:** Consumer PRs publish pacts; provider CI blocks on verification failure.

**Architect:** Complement with contract tests + smoke E2E — not replace all integration tests.

### Architecture Perspective

CDC puts consumers in the contract driver's seat.

### Follow-up Questions

1. **Provider states? — Pact supports staging pacts per environment.**
2. **Bi-directional contracts? — Emerging pattern — both sides verify.**

### Common Mistakes in Interviews

- Provider dictates API without consumer input
- Breaking field removal without consumer notification
- Contract tests skipped in CI

---

## Q052: API Versioning Microservices

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | API Design |
| **Frequency** | Common |

### Question

Version `/orders` API across three microservices consumed by mobile app.

### Short Answer (30 seconds)

URL path versioning (`/v1/orders`, `/v2/orders`) for public APIs. Deprecation headers (`Sunset`, `Link`). Support N-1 version minimum 6–12 months.

### Detailed Answer (3–5 minutes)

**Rules:**
- Additive changes in minor — new optional fields OK
- Breaking: new major version, parallel deploy
- Mobile: force upgrade policy for ancient versions

**Internal gRPC:** package versioning in proto (`v1`, `v2` services).

**Architect:** API gateway routes version to correct service deployment — v1 and v2 may run simultaneously during migration.

### Architecture Perspective

Versioning prevents mobile client breakage.

### Follow-up Questions

1. **Header vs URL versioning? — URL more visible for support and caching.**
2. **GraphQL versioning? — Avoid — evolve schema additively with deprecation.**

### Common Mistakes in Interviews

- Breaking change without version bump
- Three versions supported forever
- No Sunset header communication

---

## Q053: Choreography vs Orchestration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Integration |
| **Frequency** | Very Common |

### Question

Order saga — when event choreography vs orchestrator (Durable Functions)?

### Short Answer (30 seconds)

Choreography: few steps, clear events, teams own services — `OrderPlaced` → inventory reacts. Orchestration: 6+ steps, complex compensation, visibility needed — central coordinator.

### Detailed Answer (3–5 minutes)

**Choreography pros:** loose coupling, no single point. **Cons:** hard to trace, implicit flow.

**Orchestration pros:** visible state machine, easier debug. **Cons:** coordinator HA, coupling to orchestrator.

**Hybrid:** Orchestrate checkout; choreograph post-order side effects.

**Architect:** Choose orchestration when support asks 'where is my order in the pipeline?' daily.

### Architecture Perspective

Saga style choice affects operability.

### Follow-up Questions

1. **Event notification vs event-carried state? — Carried state reduces chattiness.**
2. **Orchestration language? — Durable Functions, Temporal, Camunda — team skill matters.**

### Common Mistakes in Interviews

- Choreography with 12 events nobody documents
- Orchestrator for simple two-step flow
- No correlation ID across choreography

---

## Q054: Domain Events Integration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Integration |
| **Frequency** | Common |

### Question

Publish `OrderPlaced` domain event — design schema, versioning, and consumers.

### Short Answer (30 seconds)

CloudEvents envelope: `type`, `source`, `id`, `time`, `data`. Schema registry (Avro/JSON Schema). Version in `type` suffix or `dataschema` URI.

### Detailed Answer (3–5 minutes)

**Event payload:** orderId, customerId, line items, total — not full entity graph.

**Consumers:** inventory, email, analytics, warehouse — each idempotent on `event.id`.

**Outbox:** publish from same transaction as order insert.

**Architect:** Event contract is public API — review like REST breaking changes.

### Architecture Perspective

Domain events are integration backbone.

### Follow-up Questions

1. **Event versioning? — Add optional fields; never remove — upcast old events in consumers.**
2. **Integration event vs domain event? — Domain is business language; integration may translate at boundary.**

### Common Mistakes in Interviews

- Fat events with entire database row
- No schema registry
- Consumers mutate event payload

---

## Q055: Shared Database Anti-Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Anti-Patterns |
| **Frequency** | Very Common |

### Question

Two microservices share Orders table — why anti-pattern and remediation?

### Short Answer (30 seconds)

Hidden distributed monolith — schema changes require coordinated deploy, no true service ownership, coupling at data layer defeats independent scaling.

### Detailed Answer (3–5 minutes)

**Symptoms:** Both services run migrations on same DB; integration tests need both schemas; neither team can deploy alone.

**Remediation:**
1. Assign table ownership to one service
2. Other service accesses via API or replicated read model
3. Events for state changes

**Architect:** Shared DB acceptable as time-boxed migration phase — not end state.

### Architecture Perspective

Shared DB is #1 microservices anti-pattern.

### Follow-up Questions

1. **View-based sharing? — Still coupling — views break on schema change.**
2. **Reporting on shared DB? — CDC to warehouse instead of cross-service queries.**

### Common Mistakes in Interviews

- Distributed JOIN in application layer
- Both services write same table
- No exit plan from shared schema

---

## Q056: Distributed Tracing Correlation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Observability |
| **Frequency** | Common |

### Question

Standardize trace correlation across gateway, BFF, and five microservices.

### Short Answer (30 seconds)

W3C `traceparent` header propagated on every hop. Structured logs include `traceId`, `spanId`. Business `correlationId` in baggage for support tickets.

### Detailed Answer (3–5 minutes)

**Implementation:**
- OpenTelemetry auto-instrument ASP.NET, HttpClient
- APIM injects trace context if missing
- Service Bus messages carry trace context in application properties

**Architect:** 100% sampling in dev; head-based 1–10% in prod with tail sampling for errors.

**Support:** User provides order ID → lookup trace → see full waterfall.

### Architecture Perspective

Correlation is debugging microservices at scale.

### Follow-up Questions

1. **Baggage vs span attributes? — Baggage propagates; keep small — no PII.**
2. **Trace ID in ProblemDetails? — Return correlation ID to client for support.**

### Common Mistakes in Interviews

- No trace propagation on async messages
- Different trace format per service
- 100% sampling at 50K RPS

---

## Q057: Health Check Aggregation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Common |

### Question

Design `/health` for Kubernetes — liveness vs readiness vs dependency checks.

### Short Answer (30 seconds)

Liveness: process alive — restart if fails. Readiness: can accept traffic — exclude from LB. Dependency checks in readiness only for critical path — not every downstream.

### Detailed Answer (3–5 minutes)

**ASP.NET Core:**
```csharp
builder.Services.AddHealthChecks()
    .AddSqlServer(conn, name: "db", tags: ["ready"])
    .AddCheck("self", () => Healthy(), tags: ["live"]);
```

**Anti-pattern:** Liveness includes DB — DB blip kills all pods.

**Architect:** Aggregate health at deploy gate — `can-i-deploy` + smoke, not deep checks on liveness.

### Architecture Perspective

Health check design prevents cascading pod restarts.

### Follow-up Questions

1. **Startup probe? — Slow-init containers — prevent kill during warmup.**
2. **Health check aggregation API? — Gateway polls services — circuit on unhealthy dependency.**

### Common Mistakes in Interviews

- Liveness probe calls database
- Readiness always healthy — route to broken pods
- No differentiation live vs ready

---

## Q058: Config Externalization

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Common |

### Question

Move microservice config from appsettings.json to external store — design approach.

### Short Answer (30 seconds)

Azure App Configuration + Key Vault references. Feature flags, connection strings, tuning params. Refresh without redeploy via `IOptionsMonitor`.

### Detailed Answer (3–5 minutes)

**Layers:**
- **Static:** appsettings baseline defaults
- **Environment:** App Config label `Production`
- **Secrets:** Key Vault — never in App Config plaintext

**Architect:** Config change audit trail, RBAC on keys, staged rollout per service. GitOps for infra; App Config for runtime tuning.

### Architecture Perspective

External config enables safe runtime changes.

### Follow-up Questions

1. **Refresh interval? — Balance propagation speed vs API throttling.**
2. **Config vs secrets boundary? — Secrets always Key Vault; config may reference vault URI.**

### Common Mistakes in Interviews

- Secrets in appsettings committed to git
- No refresh — redeploy for timeout change
- Shared config key across services — coupling

---

## Q059: Feature Flags Per Service

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Common |

### Question

Canary new inventory service with 10% traffic — feature flag architecture.

### Short Answer (30 seconds)

LaunchDarkly / App Configuration feature flag `inventory-v2-routing`. Gateway or BFF evaluates flag by user ID percentage. Metrics compare error rate and latency v1 vs v2.

### Detailed Answer (3–5 minutes)

**Patterns:**
- **Percentage rollout:** hash(userId) % 100 < 10
- **Allowlist:** internal testers first
- **Kill switch:** instant 100% back to v1

**Architect:** Flag per service not global monolith flag. Automate flag cleanup after full rollout — tech debt otherwise.

### Architecture Perspective

Feature flags are microservices migration safety net.

### Follow-up Questions

1. **Flag evaluation at edge vs service? — Edge for routing; service for behavior toggles.**
2. **Long-lived flags? — Review quarterly — remove stale.**

### Common Mistakes in Interviews

- Hardcoded if-debug routing
- No metrics on flag cohorts
- Kill switch untested until incident

---

## Q060: Microservices Testing Pyramid

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Testing |
| **Frequency** | Common |

### Question

Define testing pyramid for microservices order domain.

### Short Answer (30 seconds)

Many unit tests (domain logic), contract tests (Pact), integration tests (Testcontainers per service), few E2E smoke (critical paths only).

### Detailed Answer (3–5 minutes)

**Layers:**
1. **Unit:** aggregate rules, pricing — fast, no IO
2. **Contract:** order ↔ payment, order ↔ inventory
3. **Integration:** API + real DB in container — one service boundary
4. **E2E:** checkout happy path staging — 5–10 scenarios max

**Architect:** E2E suite >30 min blocks CI — invest in contracts and integration. Service virtualization for rare third parties.

### Architecture Perspective

Right pyramid keeps microservices CI fast and reliable.

### Follow-up Questions

1. **Testcontainers? — Real Postgres/Redis in Docker for integration tests.**
2. **E2E environment parity? — Staging mirrors prod topology scaled down.**

### Common Mistakes in Interviews

- E2E only — 2 hour CI pipeline
- No contract tests between services
- Shared test database across parallel CI jobs

---

## Q061: Strangler Fig Routing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Migration |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: Strangler Fig Routing — what do you need to know and decide?

### Short Answer (30 seconds)

Strangler Fig Routing requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 22 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 22 — Migration):**
- Scenario: production system at scale needs a decision involving *Strangler Fig Routing*
- Constraints: reliability, security, cost, and team skill must be explicit

**Architect approach:**
1. Clarify requirements and NFRs (latency, RPO/RTO, compliance)
2. List two viable options with pros/cons
3. Choose with documented trade-offs in ADR
4. Define verification: metrics, alerts, game day, rollback

**Production checklist:**
- Runbook entry exists
- Observability: metric + log + trace
- Security review for external exposure
- FinOps tag and cost estimate

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect Strangler Fig Routing to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove Strangler Fig Routing is healthy in production?**
2. **What is the rollback plan if Strangler Fig Routing change fails?**

### Common Mistakes in Interviews

- Treating Strangler Fig Routing as set-and-forget with no monitoring
- No ADR documenting trade-offs for Strangler Fig Routing
- Copying Strangler Fig Routing pattern from blog without context fit

---

## Q062: Sidecar Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Microservices |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: Sidecar Pattern — what do you need to know and decide?

### Short Answer (30 seconds)

Sidecar Pattern requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 22 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 22 — Microservices):**
- Scenario: production system at scale needs a decision involving *Sidecar Pattern*
- Constraints: reliability, security, cost, and team skill must be explicit

**Architect approach:**
1. Clarify requirements and NFRs (latency, RPO/RTO, compliance)
2. List two viable options with pros/cons
3. Choose with documented trade-offs in ADR
4. Define verification: metrics, alerts, game day, rollback

**Production checklist:**
- Runbook entry exists
- Observability: metric + log + trace
- Security review for external exposure
- FinOps tag and cost estimate

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect Sidecar Pattern to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove Sidecar Pattern is healthy in production?**
2. **What is the rollback plan if Sidecar Pattern change fails?**

### Common Mistakes in Interviews

- Treating Sidecar Pattern as set-and-forget with no monitoring
- No ADR documenting trade-offs for Sidecar Pattern
- Copying Sidecar Pattern pattern from blog without context fit

---

## Q063: Ambassador Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Microservices |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: Ambassador Pattern — what do you need to know and decide?

### Short Answer (30 seconds)

Ambassador Pattern requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 22 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 22 — Microservices):**
- Scenario: production system at scale needs a decision involving *Ambassador Pattern*
- Constraints: reliability, security, cost, and team skill must be explicit

**Architect approach:**
1. Clarify requirements and NFRs (latency, RPO/RTO, compliance)
2. List two viable options with pros/cons
3. Choose with documented trade-offs in ADR
4. Define verification: metrics, alerts, game day, rollback

**Production checklist:**
- Runbook entry exists
- Observability: metric + log + trace
- Security review for external exposure
- FinOps tag and cost estimate

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect Ambassador Pattern to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove Ambassador Pattern is healthy in production?**
2. **What is the rollback plan if Ambassador Pattern change fails?**

### Common Mistakes in Interviews

- Treating Ambassador Pattern as set-and-forget with no monitoring
- No ADR documenting trade-offs for Ambassador Pattern
- Copying Ambassador Pattern pattern from blog without context fit

---

## Q064: Anti-Corruption at Gateway

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Gateway |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: Anti-Corruption at Gateway — what do you need to know and decide?

### Short Answer (30 seconds)

Anti-Corruption at Gateway requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 22 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 22 — Gateway):**
- Scenario: production system at scale needs a decision involving *Anti-Corruption at Gateway*
- Constraints: reliability, security, cost, and team skill must be explicit

**Architect approach:**
1. Clarify requirements and NFRs (latency, RPO/RTO, compliance)
2. List two viable options with pros/cons
3. Choose with documented trade-offs in ADR
4. Define verification: metrics, alerts, game day, rollback

**Production checklist:**
- Runbook entry exists
- Observability: metric + log + trace
- Security review for external exposure
- FinOps tag and cost estimate

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect Anti-Corruption at Gateway to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove Anti-Corruption at Gateway is healthy in production?**
2. **What is the rollback plan if Anti-Corruption at Gateway change fails?**

### Common Mistakes in Interviews

- Treating Anti-Corruption at Gateway as set-and-forget with no monitoring
- No ADR documenting trade-offs for Anti-Corruption at Gateway
- Copying Anti-Corruption at Gateway pattern from blog without context fit

---

## Q065: Rate Limiting Per Tenant

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Gateway |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: Rate Limiting Per Tenant — what do you need to know and decide?

### Short Answer (30 seconds)

Rate Limiting Per Tenant requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 22 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 22 — Gateway):**
- Scenario: production system at scale needs a decision involving *Rate Limiting Per Tenant*
- Constraints: reliability, security, cost, and team skill must be explicit

**Architect approach:**
1. Clarify requirements and NFRs (latency, RPO/RTO, compliance)
2. List two viable options with pros/cons
3. Choose with documented trade-offs in ADR
4. Define verification: metrics, alerts, game day, rollback

**Production checklist:**
- Runbook entry exists
- Observability: metric + log + trace
- Security review for external exposure
- FinOps tag and cost estimate

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect Rate Limiting Per Tenant to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove Rate Limiting Per Tenant is healthy in production?**
2. **What is the rollback plan if Rate Limiting Per Tenant change fails?**

### Common Mistakes in Interviews

- Treating Rate Limiting Per Tenant as set-and-forget with no monitoring
- No ADR documenting trade-offs for Rate Limiting Per Tenant
- Copying Rate Limiting Per Tenant pattern from blog without context fit

---

## Q066: JWT Validation at Edge

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: JWT Validation at Edge — what do you need to know and decide?

### Short Answer (30 seconds)

JWT Validation at Edge requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 22 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 22 — Security):**
- Scenario: production system at scale needs a decision involving *JWT Validation at Edge*
- Constraints: reliability, security, cost, and team skill must be explicit

**Architect approach:**
1. Clarify requirements and NFRs (latency, RPO/RTO, compliance)
2. List two viable options with pros/cons
3. Choose with documented trade-offs in ADR
4. Define verification: metrics, alerts, game day, rollback

**Production checklist:**
- Runbook entry exists
- Observability: metric + log + trace
- Security review for external exposure
- FinOps tag and cost estimate

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect JWT Validation at Edge to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove JWT Validation at Edge is healthy in production?**
2. **What is the rollback plan if JWT Validation at Edge change fails?**

### Common Mistakes in Interviews

- Treating JWT Validation at Edge as set-and-forget with no monitoring
- No ADR documenting trade-offs for JWT Validation at Edge
- Copying JWT Validation at Edge pattern from blog without context fit

---

## Q067: Service Discovery Client

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Discovery |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: Service Discovery Client — what do you need to know and decide?

### Short Answer (30 seconds)

Service Discovery Client requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 22 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 22 — Discovery):**
- Scenario: production system at scale needs a decision involving *Service Discovery Client*
- Constraints: reliability, security, cost, and team skill must be explicit

**Architect approach:**
1. Clarify requirements and NFRs (latency, RPO/RTO, compliance)
2. List two viable options with pros/cons
3. Choose with documented trade-offs in ADR
4. Define verification: metrics, alerts, game day, rollback

**Production checklist:**
- Runbook entry exists
- Observability: metric + log + trace
- Security review for external exposure
- FinOps tag and cost estimate

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect Service Discovery Client to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove Service Discovery Client is healthy in production?**
2. **What is the rollback plan if Service Discovery Client change fails?**

### Common Mistakes in Interviews

- Treating Service Discovery Client as set-and-forget with no monitoring
- No ADR documenting trade-offs for Service Discovery Client
- Copying Service Discovery Client pattern from blog without context fit

---

## Q068: Client-Side Load Balancing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Resilience |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: Client-Side Load Balancing — what do you need to know and decide?

### Short Answer (30 seconds)

Client-Side Load Balancing requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 22 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 22 — Resilience):**
- Scenario: production system at scale needs a decision involving *Client-Side Load Balancing*
- Constraints: reliability, security, cost, and team skill must be explicit

**Architect approach:**
1. Clarify requirements and NFRs (latency, RPO/RTO, compliance)
2. List two viable options with pros/cons
3. Choose with documented trade-offs in ADR
4. Define verification: metrics, alerts, game day, rollback

**Production checklist:**
- Runbook entry exists
- Observability: metric + log + trace
- Security review for external exposure
- FinOps tag and cost estimate

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect Client-Side Load Balancing to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove Client-Side Load Balancing is healthy in production?**
2. **What is the rollback plan if Client-Side Load Balancing change fails?**

### Common Mistakes in Interviews

- Treating Client-Side Load Balancing as set-and-forget with no monitoring
- No ADR documenting trade-offs for Client-Side Load Balancing
- Copying Client-Side Load Balancing pattern from blog without context fit

---

## Q069: Server-Side Load Balancing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Resilience |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: Server-Side Load Balancing — what do you need to know and decide?

### Short Answer (30 seconds)

Server-Side Load Balancing requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 22 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 22 — Resilience):**
- Scenario: production system at scale needs a decision involving *Server-Side Load Balancing*
- Constraints: reliability, security, cost, and team skill must be explicit

**Architect approach:**
1. Clarify requirements and NFRs (latency, RPO/RTO, compliance)
2. List two viable options with pros/cons
3. Choose with documented trade-offs in ADR
4. Define verification: metrics, alerts, game day, rollback

**Production checklist:**
- Runbook entry exists
- Observability: metric + log + trace
- Security review for external exposure
- FinOps tag and cost estimate

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect Server-Side Load Balancing to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove Server-Side Load Balancing is healthy in production?**
2. **What is the rollback plan if Server-Side Load Balancing change fails?**

### Common Mistakes in Interviews

- Treating Server-Side Load Balancing as set-and-forget with no monitoring
- No ADR documenting trade-offs for Server-Side Load Balancing
- Copying Server-Side Load Balancing pattern from blog without context fit

---

## Q070: Health Probe Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: Health Probe Design — what do you need to know and decide?

### Short Answer (30 seconds)

Health Probe Design requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 22 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 22 — Operations):**
- Scenario: production system at scale needs a decision involving *Health Probe Design*
- Constraints: reliability, security, cost, and team skill must be explicit

**Architect approach:**
1. Clarify requirements and NFRs (latency, RPO/RTO, compliance)
2. List two viable options with pros/cons
3. Choose with documented trade-offs in ADR
4. Define verification: metrics, alerts, game day, rollback

**Production checklist:**
- Runbook entry exists
- Observability: metric + log + trace
- Security review for external exposure
- FinOps tag and cost estimate

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect Health Probe Design to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove Health Probe Design is healthy in production?**
2. **What is the rollback plan if Health Probe Design change fails?**

### Common Mistakes in Interviews

- Treating Health Probe Design as set-and-forget with no monitoring
- No ADR documenting trade-offs for Health Probe Design
- Copying Health Probe Design pattern from blog without context fit

---
