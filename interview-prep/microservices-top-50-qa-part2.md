# Microservices Top 50 — Part 2 (Q009–Q030)

> **Resilience, Data, DDD, API Gateway** | Weeks 21–24 | [Part 1](microservices-top-50-qa-part1.md) | [Part 3](microservices-top-50-qa-part3.md) | [Index](microservices-top-50-index.md)

---


## Q009: Saga — Orchestration vs Choreography

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Distributed Transactions |
| **Week** | 24 |

### Question

Compare saga orchestration and choreography for order checkout. When do you choose each?

### Short Answer (30 seconds)

Choreography — services react to domain events without a central coordinator. Orchestration — a saga coordinator drives each step and compensation. Choreography for 2–4 simple steps; orchestration when you need visibility, timeouts, and complex compensation across 5+ steps.

### Detailed Answer (3–5 minutes)

**Choreography:** Order service publishes `OrderPlaced` → Inventory reserves → Payment charges → Shipping creates label. No central brain — flow emerges from event handlers.

**Pros:** loose coupling, no orchestrator SPOF, natural fit for event-driven teams.
**Cons:** implicit flow (hard to read), debugging requires distributed tracing, compensation logic scattered.

**Orchestration:** Durable Functions / custom saga service calls Inventory → Payment → Shipping; on failure runs compensations in reverse order.

**Pros:** explicit state machine, centralized timeout/retry, easier audit for regulated checkout.
**Cons:** orchestrator is a dependency; can become a mini-monolith if it holds domain logic.

| Factor | Choreography | Orchestration |
|--------|--------------|---------------|
| Steps | ≤4, linear | 5+, branching |
| Visibility | Low | High |
| Team maturity | Strong event culture | Mixed |
| Compliance audit | Harder | Easier |

**Architect:** Start choreography for notifications; orchestrate payment + inventory + fraud because money is involved.

### Follow-up Questions

1. **Can you mix both? — Yes — orchestrate payment path, choreograph downstream fulfillment events.**
2. **How test sagas? — State-machine unit tests + contract tests per step + chaos on compensation paths.**

### Common Mistakes

- Choosing orchestration for 3-step happy path only
- No saga log or correlation ID across steps

---

## Q010: Transactional Outbox Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Messaging |
| **Week** | 24 |

### Question

Why use the transactional outbox instead of publishing events immediately after SaveChanges?

### Short Answer (30 seconds)

Dual-write problem — DB commits but broker publish fails (or the reverse). Outbox writes the event in the same DB transaction as business data; a relay publishes reliably with at-least-once delivery.

### Detailed Answer (3–5 minutes)

**Anti-pattern:**
```csharp
await _db.Orders.AddAsync(order);
await _db.SaveChangesAsync();
await _bus.PublishAsync(new OrderPlaced(order)); // can fail after commit
```

**Outbox fix:**
1. INSERT order + INSERT outbox row in one transaction
2. Relay polls or CDC reads outbox → publishes to Service Bus / Kafka
3. Mark row processed (or delete with retention policy)

**Relay options:**
- **Polling** with `FOR UPDATE SKIP LOCKED` — simple, slight lag
- **CDC (Debezium)** — scales, captures all changes, more ops
- **Azure SQL trigger → Service Bus** — managed middle ground

**Architect checklist:** index on unprocessed rows, partition key = aggregate ID for ordering, consumer idempotency mandatory, monitor relay lag SLO.

### Follow-up Questions

1. **Outbox vs inbox? — Outbox is publisher-side guarantee; inbox deduplicates on consumer.**
2. **Exactly-once end-to-end? — Effectively-once: outbox + idempotent consumer + inbox.**

### Common Mistakes

- Publishing before DB commit
- Outbox table without index on unprocessed rows

---

## Q011: Strangler Fig Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Decomposition |
| **Week** | 23 |

### Question

Describe the strangler fig pattern for extracting a module from a .NET monolith.

### Short Answer (30 seconds)

Route increasing traffic through a proxy/gateway to the new microservice while the legacy monolith handles the remainder. Extract highest-value module first; retire legacy paths when metrics show 100% migration.

### Detailed Answer (3–5 minutes)

**Steps:**
1. **Facade** — APIM / YARP / nginx in front of monolith
2. **Identify seam** — order placement API is a clean boundary
3. **Build new service** — owns Order DB, implements same contract (or versioned)
4. **Route by path/header** — `/api/v2/orders` → new service; legacy → monolith
5. **Migrate data** — dual-write or CDC sync until cutover
6. **Retire** — delete monolith order module when error rate and traffic = 0

**Example routing:**
```
if (featureFlag "OrderServiceV2" && path.StartsWith("/orders"))
    proxy to order-service
else
    proxy to monolith
```

**Architect:** Never big-bang. Measure extraction with traffic %, error parity, and latency delta. Document ADR per extracted context.

### Follow-up Questions

1. **Which module first? — Highest pain: deploy frequency blocker, scale bottleneck, or team boundary.**
2. **Data migration strategy? — CDC + reconciliation job; avoid stop-the-world dump.**

### Common Mistakes

- Big-bang rewrite instead of incremental routing
- No rollback path when new service error rate spikes

---

## Q012: Backend-for-Frontend (BFF)

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | API Design |
| **Week** | 22 |

### Question

When should you add a Backend-for-Frontend layer in a microservices architecture?

### Short Answer (30 seconds)

When mobile, web, and partner clients need different aggregation shapes and latency budgets. Separate BFFs prevent a lowest-common-denominator API that over-fetches for mobile and under-serves web dashboards.

### Detailed Answer (3–5 minutes)

**Without BFF:** Mobile app calls 8 services for homepage — battery drain, fragile on 3G.

**With BFF:**
- `mobile-bff` — 1 aggregated `/home` response, image URLs resized
- `web-bff` — richer payload, server-driven pagination
- `partner-bff` — strict rate limits, API-key auth, stable v1 contract

**BFF responsibilities:** aggregation, protocol translation (GraphQL optional), auth token exchange, response shaping — **not** domain business rules.

**Placement:** BFF sits behind API gateway; calls domain services via internal network.

| Anti-pattern | Fix |
|--------------|-----|
| BFF owns order business logic | Move rules to Order service |
| One BFF for all clients | Split by client persona |
| BFF writes to multiple DBs | BFF orchestrates via APIs only |

### Follow-up Questions

1. **BFF vs API gateway? — Gateway = cross-cutting edge (TLS, rate limit); BFF = client-specific composition.**
2. **Can BFF call BFF? — Avoid chains; flatten to domain services.**

### Common Mistakes

- Putting domain validation only in BFF
- Single BFF becoming a new monolith with shared DB access

---

## Q013: Database Per Service

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Data |
| **Week** | 22 |

### Question

Explain database-per-service. How do you handle cross-service queries and reporting?

### Short Answer (30 seconds)

Each microservice owns its schema and storage — no foreign keys across service boundaries. Cross-service data via APIs, cached snapshots, events, or read models. Analytics uses a warehouse fed by domain events.

### Detailed Answer (3–5 minutes)

**Principle:** Order service has `Orders` DB; Catalog has `Products` DB. Order line stores `productId` + denormalized `productName` snapshot — never JOIN across DBs at runtime.

**Cross-service read patterns:**
1. **API composition** — BFF calls Catalog for product details (acceptable for low volume)
2. **Cache** — Redis materialized product card keyed by `productId`
3. **Event-driven projection** — `ProductUpdated` event updates read model in Order service
4. **CQRS read store** — dedicated query DB fed by event stream
5. **Data warehouse** — nightly / streaming ETL for BI

**Architect:** Choose consistency per use case — checkout needs strong order write; product name on receipt can be eventually consistent snapshot.

### Follow-up Questions

1. **Polyglot persistence? — Order = SQL, Search = Elasticsearch, Cart = Redis — each fits the access pattern.**
2. **Shared read replica? — Still violates ownership if services write to same tables.**

### Common Mistakes

- Shared database antipattern (hidden monolith)
- Distributed JOIN attempts across service databases

---

## Q014: Sync vs Async Communication

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Communication |
| **Week** | 22 |

### Question

When do you use synchronous HTTP vs asynchronous messaging between microservices?

### Short Answer (30 seconds)

Sync when the caller needs an immediate result for the user (checkout total, fraud check). Async for fire-and-forget, long-running work, or decoupling peak load (email, analytics, report generation). Avoid sync chains deeper than 2–3 hops.

### Detailed Answer (3–5 minutes)

**Synchronous (HTTP/gRPC):**
- User waits for response
- Simpler mental model and debugging
- Couples availability in time — downstream outage blocks caller
- Requires timeout + circuit breaker + bulkhead

**Asynchronous (events/queues):**
- Temporal decoupling — producer doesn't wait
- Natural load leveling and retry
- Complexity: ordering, idempotency, poison messages, eventual consistency UX

**Decision matrix:**
| Scenario | Choice |
|----------|--------|
| Get order status for user | Sync (or sync + cache) |
| Send confirmation email | Async |
| Payment authorization | Sync with 3s timeout |
| Update search index | Async |

**Architect rule:** If failure must be shown to the user immediately → sync with resilience patterns. Otherwise → prefer events.

### Follow-up Questions

1. **gRPC vs REST? — gRPC for internal east-west, low latency, strong contracts; REST at edge for browser clients.**
2. **Request-reply over queue? — Valid pattern when you need async but still need a response (correlation ID + reply queue).**

### Common Mistakes

- Six-service sync chain for page load
- Async for user-facing status query without polling or WebSocket

---

## Q015: Circuit Breaker Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Resilience |
| **Week** | 21 |

### Question

How does a circuit breaker protect a microservices system? How do you tune it per dependency?

### Short Answer (30 seconds)

After a failure threshold, stop calling the failing dependency — fail fast instead of hanging. Half-open sends probe requests to detect recovery. Prevents thread pool exhaustion and cascading failures.

### Detailed Answer (3–5 minutes)

**States:** Closed (normal) → Open (fail fast) → Half-open (test probe) → Closed or re-Open.

**Polly / .NET resilience pipeline example:**
- Payment: 30% failures in 20s window, minimum 10 requests → open 60s
- Recommendations: 50% failures, open 10s, fallback to cached defaults

**Pair with:**
- **Timeout** — shorter than client SLA
- **Fallback** — cached response, degraded mode, empty list
- **Bulkhead** — isolate thread pools per dependency

**Monitor:** `circuit_state` metric; alert if open > 2 minutes.

**Architect:** Document fallback behavior in ADR — users see empty recommendations, not a 500 homepage.

### Follow-up Questions

1. **Circuit breaker vs retry? — Don't retry when circuit is open; retry only on transient errors when closed.**
2. **Hedging requests? — Send duplicate to backup after delay — use sparingly, doubles load.**

### Common Mistakes

- Same breaker settings for payment and recommendations
- Circuit open with no fallback UX or cached response

---

## Q016: Bulkhead Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Resilience |
| **Week** | 21 |

### Question

How does the bulkhead pattern prevent one slow dependency from starving others?

### Short Answer (30 seconds)

Isolate resources (thread pools, connections, semaphores) per downstream dependency — email slowness cannot exhaust the pool used for payment calls.

### Detailed Answer (3–5 minutes)

**Without bulkhead:** Shared `HttpClient` pool of 100 threads — slow email service blocks all 100 → payment requests queue → checkout times out.

**With bulkhead:**
```csharp
// Separate pipelines per downstream
services.AddHttpClient("Payment").AddStandardResilienceHandler(...);
services.AddHttpClient("Email").AddStandardResilienceHandler(...);
// Polly bulkhead: max 10 parallel, queue 20 for email only
```

**K8s variant:** Separate deployments for critical vs batch workloads; different node pools.

**Sizing:** Load test at 2× peak — payment pool sized for Black Friday checkout, email pool sized for async notification backlog.

**Defense in depth:** Bulkhead + circuit breaker + timeout = three independent failure containment layers.

### Follow-up Questions

1. **Bulkhead vs rate limiting? — Bulkhead limits concurrent calls to one dependency; rate limit caps requests per time window (often per client).**
2. **Thread pool vs connection pool? — Both can be bulkheaded; HttpClient handler isolation is the .NET pattern.**

### Common Mistakes

- Single shared HttpClient for all downstreams
- Unbounded queue on bulkhead — still risks memory pressure

---

## Q017: Service Mesh — When to Adopt

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Infrastructure |
| **Week** | 23 |

### Question

At what scale and maturity should you adopt a service mesh (Istio, Linkerd, Dapr)?

### Short Answer (30 seconds)

Typically 15+ services needing uniform mTLS, traffic splitting, and observability without library sprawl. Overkill for 3–5 services — use Polly, OpenTelemetry SDK, and APIM first.

### Detailed Answer (3–5 minutes)

**Service mesh provides:**
- **mTLS** east-west without app code changes
- **Traffic management** — canary, A/B, fault injection
- **Observability** — automatic metrics, traces per hop
- **Policy** — rate limits, authz at L7

**Cost:** Operational complexity, sidecar CPU/memory overhead (~50–100MB per pod), steep learning curve.

**Decision framework:**
| Signal | Action |
|--------|--------|
| <10 services, one team | Libraries + gateway |
| 15+ services, polyglot | Evaluate mesh |
| Strict zero-trust east-west | Mesh or service-level mTLS |
| AKS + GitOps mature | Istio/Linkerd viable |

**Dapr alternative:** Portable building blocks (pub/sub, state, secrets) without full mesh — good for .NET teams on Azure.

### Follow-up Questions

1. **Sidecar vs node agent? — Sidecar per pod is standard; node agent reduces overhead but weaker isolation.**
2. **Mesh vs API gateway? — Gateway = north-south; mesh = east-west between services.**

### Common Mistakes

- Adopting Istio before CI/CD and observability baselines exist
- Mesh for 3 services — operational tax exceeds benefit

---

## Q018: Contract Testing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Testing |
| **Week** | 24 |

### Question

How do contract tests avoid the integration test grid explosion in microservices?

### Short Answer (30 seconds)

Consumer-driven contracts (Pact) define expected API shapes; provider verifies against published contracts in CI — no need to spin up all 20 services for every PR.

### Detailed Answer (3–5 minutes)

**Problem:** 15 services × 15 consumers = 225 integration combinations — E2E suite takes hours, flakes constantly.

**Contract testing flow:**
1. Order service (consumer) defines: `POST /payments` expects `{ amount, currency }` → `{ transactionId }`
2. Pact file published to broker
3. Payment service (provider) CI runs `verify pact` — fails if response shape changes
4. Deploy independently with confidence

**Scope:** HTTP request/response, message schemas (asyncAPI), event payloads.

**Not a replacement for:** A thin smoke E2E suite (5 critical journeys) and production synthetic monitoring.

**Architect:** Mandate contract tests in platform golden path template; broker (Pactflow) for cross-team visibility.

### Follow-up Questions

1. **Contract vs schema registry? — Schema registry (Avro/Protobuf) for events; Pact for behavioral HTTP contracts.**
2. **Who owns breaking changes? — Provider notifies consumers; run v1/v2 parallel during deprecation window.**

### Common Mistakes

- Replacing all E2E with contracts — miss wiring bugs
- Contracts that test implementation details instead of public interface

---

## Q019: API Versioning Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | API Design |
| **Week** | 22 |

### Question

A payment API needs a breaking change. What versioning strategy do you recommend?

### Short Answer (30 seconds)

Run v1 and v2 in parallel with a published deprecation timeline. Prefer URL path versioning (`/v2/payments`) for clarity; header versioning for internal services. Never break consumers without 90-day notice.

### Detailed Answer (3–5 minutes)

**Strategies:**
| Approach | Pros | Cons |
|----------|------|------|
| URL `/v2/` | Explicit, cacheable | URL proliferation |
| Header `Api-Version: 2` | Clean URLs | Harder to test in browser |
| Query `?version=2` | Easy | Easy to forget |

**Breaking change playbook:**
1. Announce deprecation in changelog + email
2. Deploy v2 alongside v1 (separate controllers or route maps)
3. Monitor v1 traffic — alert when >5% remains at day 60
4. Sunset v1 after 90 days (or contractual SLA)

**.NET:** `[ApiVersion("2.0")]` + `AddApiVersioning()` with default version reporting.

**Architect:** Prefer additive changes (new optional fields) over breaking — event schema evolution uses same discipline.

### Follow-up Questions

1. **GraphQL versioning? — Avoid — deprecate fields with `@deprecated` directive instead.**
2. **Internal vs public API versioning? — Internal can move faster; public needs longer deprecation.**

### Common Mistakes

- Breaking change without parallel version running
- Version in URL for events — use schema version in payload instead

---

## Q020: Event Choreography

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Event-Driven |
| **Week** | 24 |

### Question

Explain event choreography and its trade-offs compared to orchestrated sagas.

### Short Answer (30 seconds)

Choreography coordinates workflows through domain events — each service knows only what to do when it sees an event. No central coordinator. Works for simple flows; becomes hard to reason about at scale.

### Detailed Answer (3–5 minutes)

**Example — order fulfillment:**
```
OrderPlaced → Inventory: ReserveStock
StockReserved → Payment: Charge
PaymentCompleted → Shipping: CreateLabel
LabelCreated → Notification: SendEmail
```

Each handler is independent — adding FraudCheck means subscribing to `OrderPlaced`, not editing orchestrator code.

**Risks:**
- **Implicit process** — new engineer can't read one state machine
- **Cyclic events** — A triggers B triggers A without guard
- **Compensation scatter** — refund logic in 3 services
- **Debugging** — need correlation ID + distributed trace

**Mitigation:** Event catalog documenting publishers/subscribers; process manager only for compensation; saga log table per aggregate.

### Follow-up Questions

1. **Event notification vs event-carried state transfer? — Notification carries ID only (extra API call); ECST carries data (larger messages, fewer calls).**
2. **How avoid infinite loops? — Idempotent handlers + processed-event inbox + version checks.**

### Common Mistakes

- Choreography for 8-step payment saga with compliance audit
- No event catalog or ownership matrix

---

## Q021: Shared Database Anti-Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Data |
| **Week** | 22 |

### Question

Why is a shared database among microservices considered an anti-pattern?

### Short Answer (30 seconds)

Shared DB creates a hidden monolith — services couple through schema, deploy together for migrations, and fight over indexes. You lose independent deployment, team autonomy, and clear ownership.

### Detailed Answer (3–5 minutes)

**Symptoms:**
- Three services `UPDATE` the same `Orders` table
- Schema migration requires coordinating 5 deploys
- No one owns the `Customers` table — everyone adds columns
- Foreign keys across logical service boundaries

**Why teams do it:** Faster initial extraction, fear of distributed queries, legacy inertia.

**Escape path:**
1. Assign table ownership per bounded context
2. Other services access via API or events only
3. Database views as temporary ACL (read-only) during migration
4. Strangler extracts write ownership first

**Architect:** Shared DB is acceptable as a **temporary** migration state with a dated exit ADR — not a target architecture.

### Follow-up Questions

1. **Shared read replica OK? — Read-only replica of owned data is fine; shared writable tables are not.**
2. **Database-per-service with shared server? — Acceptable isolation step — separate schemas, no cross-schema FKs.**

### Common Mistakes

- Calling it microservices while sharing one SQL instance with cross-service FKs
- No migration plan off shared schema

---

## Q022: Distributed Tracing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Observability |
| **Week** | 21 |

### Question

How do you trace a single user request across 8 microservices in production?

### Short Answer (30 seconds)

Propagate W3C `traceparent` on every HTTP call and message metadata. OpenTelemetry SDK in each service exports spans to App Insights, Jaeger, or Grafana Tempo — one trace ID ties the full journey.

### Detailed Answer (3–5 minutes)

**Implementation:**
1. Edge gateway creates or forwards `traceparent`
2. Each service: `ActivitySource` → span per operation
3. Outbound HTTP: inject trace context headers
4. Message bus: add `traceparent` to message properties
5. Correlate with `correlation-id` for business logs

**.NET:**
```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(t => t.AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation()
        .AddAzureMonitorTraceExporter());
```

**Architect SLO:** 100% of production services export traces; sampling at 10% for cost, 100% on errors. Dashboard: p95 per hop to find slow service in chain.

### Follow-up Questions

1. **Trace vs log correlation? — Trace shows span tree; logs attach `trace_id` for drill-down.**
2. **Sampling strategy? — Head-based for volume; tail-based (always keep slow/error traces) for debugging.**

### Common Mistakes

- Different trace IDs per hop — broken propagation
- Tracing only at gateway — blind to internal service latency

---

## Q023: Health Checks — Liveness vs Readiness

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Operations |
| **Week** | 21 |

### Question

Explain liveness and readiness probes in Kubernetes for .NET microservices.

### Short Answer (30 seconds)

Liveness — is the process alive? Restart if deadlocked. Readiness — can this instance accept traffic? Remove from load balancer during startup, migration, or dependency outage.

### Detailed Answer (3–5 minutes)

**Liveness probe:** `GET /health/live` — returns 200 if app process responds. Fails → K8s restarts pod.
- Keep lightweight — no DB calls
- Detect deadlocks and infinite loops

**Readiness probe:** `GET /health/ready` — checks DB connection, cache, critical downstream.
- Fails → pod removed from Service endpoints
- Use during: EF migration on startup, warming cache, dependency temporarily down

**.NET:**
```csharp
builder.Services.AddHealthChecks()
    .AddSqlServer(conn)
    .AddCheck("downstream", () => _paymentHealth.IsHealthy());
app.MapHealthChecks("/health/ready", new() { Predicate = r => r.Tags.Contains("ready") });
```

**Architect:** Never put slow external calls in liveness — cascading restart storm. Startup probe for slow .NET cold start.

### Follow-up Questions

1. **Startup probe? — K8s 1.16+ — allows long startup before liveness kills the pod.**
2. **Health check in load balancer vs K8s? — Same endpoints; ALB/App Gateway can use `/health/ready`.**

### Common Mistakes

- DB check in liveness probe — restart loop when SQL blips
- Readiness always 200 — traffic sent to instance still starting

---

## Q024: Configuration Externalization

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Week** | 23 |

### Question

How should microservices externalize configuration per the twelve-factor app methodology?

### Short Answer (30 seconds)

Store config in environment — Azure App Configuration, Key Vault, K8s ConfigMaps/Secrets. No secrets in source control. Validate at startup; support reload without redeploy for non-secret toggles.

### Detailed Answer (3–5 minutes)

**Hierarchy (lowest → highest precedence):**
1. `appsettings.json` (defaults only)
2. `appsettings.{Environment}.json`
3. Environment variables
4. Azure App Configuration (with Key Vault references)
5. Feature flags (dynamic)

**.NET pattern:**
```csharp
builder.Configuration.AddAzureAppConfiguration(options =>
    options.Connect(conn).ConfigureKeyVault(kv => kv.SetCredential(credential)));
builder.Services.Configure<PaymentOptions>(builder.Configuration.GetSection("Payment"));
```

**Per-service config:** Each service owns its config namespace — `OrderService:Database`, not one giant shared file.

**Architect:** `IOptionsMonitor<T>` for hot reload; `IValidateOptions<T>` fail fast on invalid config; audit who changed production config.

### Follow-up Questions

1. **ConfigMap vs Secret in K8s? — ConfigMap for non-sensitive; Secret (encrypted at rest) for connection strings.**
2. **GitOps for config? — Store non-secret config in repo; secrets via External Secrets Operator → Key Vault.**

### Common Mistakes

- Connection strings committed to Git
- One global config file shared across all services — coupling and blast radius

---

## Q025: Feature Flags in Microservices

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Release Engineering |
| **Week** | 23 |

### Question

How do feature flags enable independent deployment and safe rollout per microservice?

### Short Answer (30 seconds)

Deploy code to production with features dark; enable per service, per tenant, or per user percentage without redeploy. Decouples deployment from release — critical for trunk-based development across teams.

### Detailed Answer (3–5 minutes)

**Flag types:**
- **Release** — short-lived (`CheckoutV2`), remove after 100%
- **Ops** — permanent kill switch (`UseBackupPaymentProvider`)
- **Experiment** — A/B test with metrics

**Per-service independence:** Order service ships `ExpressCheckout` flag; Payment service unaffected. Shared platform: Azure App Configuration Feature Manager or LaunchDarkly.

**.NET:**
```csharp
if (await _featureManager.IsEnabledAsync("CheckoutV2"))
    return await _checkoutV2.ProcessAsync(order);
```

**Architect:** Flag hygiene — ticket to remove flag + dead code within 2 sprints after full rollout. Monitor error rate per flag variant.

### Follow-up Questions

1. **Flags vs API versioning? — Flags toggle behavior within a version; versioning for contract breaks.**
2. **Test matrix? — CI runs integration tests with flag on AND off.**

### Common Mistakes

- Permanent flags becoming spaghetti conditionals
- Using flags as security boundary instead of proper auth

---

## Q026: Testing Pyramid for Microservices

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Testing |
| **Week** | 24 |

### Question

Describe the test pyramid for microservices. What belongs at each layer?

### Short Answer (30 seconds)

Many fast unit tests, fewer integration tests, contract tests between services, minimal E2E. Unit tests domain logic; contract tests API boundaries; E2E only for critical revenue paths.

### Detailed Answer (3–5 minutes)

**Pyramid layers:**
```
        /  E2E  \        ← 5–10 critical journeys
       / Contract \      ← every service boundary
      / Integration \    ← DB, message bus, one service
     /     Unit      \   ← domain, handlers, policies
```

| Layer | Scope | Speed | Example |
|-------|-------|-------|--------|
| Unit | Pure logic | ms | Saga compensation rules |
| Integration | Service + DB | sec | Order repo with Testcontainers |
| Contract | Consumer ↔ Provider | sec | Pact verify payment API |
| E2E | Full stack | min | Place order smoke in staging |

**Architect:** If E2E suite > 30 min, teams stop running it — invest in contracts. Testcontainers for SQL/Redis in CI without shared staging env.

### Follow-up Questions

1. **Component tests? — Test one service with mocked external HTTP — between integration and contract.**
2. **Chaos testing layer? — Production/staging fault injection — not daily CI, scheduled game days.**

### Common Mistakes

- E2E-only strategy — slow, flaky, blocks deploys
- No contract tests — breaking changes discovered in production

---

## Q027: Domain Events

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DDD |
| **Week** | 23 |

### Question

What are domain events and how do they differ from integration events in microservices?

### Short Answer (30 seconds)

Domain events represent something that happened in the domain (`OrderPlaced`, `PaymentFailed`) — past tense, immutable. Integration events are the cross-service message format; domain events may be translated before publishing.

### Detailed Answer (3–5 minutes)

**Domain event (in-process):**
```csharp
public record OrderPlaced(Guid OrderId, decimal Total) : IDomainEvent;
// Raised inside aggregate, handled by same bounded context handlers
```

**Integration event (cross-service):**
```json
{ "type": "orders.placed.v1", "orderId": "...", "total": 99.99 }
```

**Flow:** Aggregate raises domain event → handler persists to outbox → relay publishes integration event → other services consume.

**Rules:**
- Name in past tense
- Carry minimal data (ID + changed fields)
- Version schema (`v1`, `v2` additive)
- One publisher per event type (clear ownership)

**Architect:** Event storming workshop produces the catalog before writing code.

### Follow-up Questions

1. **Domain event vs command? — Command is intent (`PlaceOrder`); event is fact (`OrderPlaced`).**
2. **Event sourcing? — Store events as source of truth — domain events are the persistence model.**

### Common Mistakes

- Publishing domain model entities directly as integration events
- Events named as commands (`PlaceOrder` on the bus)

---

## Q028: Deployment Independence

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Week** | 22 |

### Question

What does deployment independence mean for microservices and how do you achieve it?

### Short Answer (30 seconds)

Each service deploys on its own schedule without coordinating other teams. Achieved via versioned APIs, backward-compatible events, contract tests, feature flags, and database-per-service.

### Detailed Answer (3–5 minutes)

**Enablers:**
1. **Database per service** — no shared schema migrations
2. **Contract tests** — detect breaking API changes in CI
3. **Additive event schemas** — new fields optional; consumers ignore unknown
4. **Feature flags** — dark deploy new behavior
5. **Independent CI/CD pipelines** — one repo per service or monorepo with path filters

**Blockers to fix:**
- Shared library version lockstep (treat as product with semver)
- Distributed monolith — must deploy A+B together
- Shared database foreign keys

**Metric:** Deployment frequency per service — elite teams deploy individual services multiple times daily.

**Architect:** If two services always deploy together, they are one service until you fix the coupling.

### Follow-up Questions

1. **Monorepo vs polyrepo? — Both work — key is independent pipeline per service artifact.**
2. **Shared NuGet domain package? — Version with semver; consumers upgrade on their schedule.**

### Common Mistakes

- Coordinated big-bang releases across all services
- Breaking API change without deprecation period

---

## Q029: Consumer-Driven Contracts

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Testing |
| **Week** | 24 |

### Question

Explain consumer-driven contract testing and how it shifts the testing responsibility.

### Short Answer (30 seconds)

Consumers define the API contract they need; providers verify they satisfy it. Shifts from provider-defined specs (often ignored) to consumer-defined expectations (enforced in CI).

### Detailed Answer (3–5 minutes)

**Traditional:** Payment team publishes OpenAPI → Order team hopes it's accurate.

**CDC:** Order team (consumer) writes Pact: "When I POST `{amount}`, I expect 201 + `{transactionId}`". Payment CI must pass `pact verify` before deploy.

**Workflow:**
1. Consumer PR generates pact JSON
2. Publish to Pact Broker
3. Provider `can-i-deploy` check before production
4. Breaking change → provider negotiates with consumers

**Benefits:** Independent deploy velocity, living documentation, fails in minutes not hours.

**Architect:** Platform provides Pact template in .NET service scaffold; broker is shared infrastructure.

### Follow-up Questions

1. **Provider-driven vs consumer-driven? — Provider-driven (OpenAPI) documents intent; CDC enforces what consumers actually use.**
2. **Message contracts? — Pact supports async — message pact for event payloads.**

### Common Mistakes

- Contracts testing unused endpoints
- No broker — contracts only on developer laptops

---

## Q030: API Gateway Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Gateway |
| **Week** | 22 |

### Question

What patterns belong in an API gateway vs individual microservices?

### Short Answer (30 seconds)

Gateway handles cross-cutting edge concerns: TLS, authentication, rate limiting, routing, WAF, request size limits. Services own business logic, domain validation, and data access.

### Detailed Answer (3–5 minutes)

**Gateway responsibilities:**
- TLS termination and certificate management
- JWT validation / OAuth token introspection
- Rate limiting per client/API key
- Path-based routing (`/orders` → order-service)
- Request/response transformation (header injection)
- API product management (APIM developer portal)

**Service responsibilities:**
- Business rules and domain invariants
- Authorization (can this user cancel this order?)
- Data persistence and transactions

**Patterns:**
| Pattern | Where |
|---------|-------|
| BFF aggregation | Behind gateway |
| Strangler routing | Gateway/YARP |
| mTLS east-west | Service mesh, not gateway |

**Azure:** APIM + App Gateway or AKS Ingress + internal services.

**Anti-pattern:** All validation in gateway — duplicates service logic, drifts, can't enforce on internal calls.

### Follow-up Questions

1. **Ocelot vs APIM? — Ocelot for OSS/K8s ingress; APIM for enterprise governance, monetization, developer portal.**
2. **GraphQL gateway? — Federation gateway routes to subgraph services — different from REST gateway.**

### Common Mistakes

- Domain business rules enforced only at gateway
- Gateway calling 10 services synchronously per request without BFF

---

**Next:** [Part 3](microservices-top-50-qa-part3.md) →
