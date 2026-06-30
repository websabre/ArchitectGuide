# Week 45 — Advanced Q&A

> Q071–Q100: Premium format (Week 1 quality).

---


## Q071: SOLID in Microservice Boundaries

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | SOLID |
| **Frequency** | Very Common |

### Question

How do SOLID principles inform microservice boundary decisions?

### Short Answer (30 seconds)

Each service should have one reason to change (SRP), expose stable contracts (OCP), honor published interfaces (LSP), small API surface (ISP), depend on events/contracts not concrete services (DIP).

### Detailed Answer (3–5 minutes)

**SRP:** Order service owns order lifecycle — not payments.

**DIP:** Depend on `OrderPlaced` event schema, not `PaymentServiceClient` concrete types in domain.

**OCP:** Add fulfillment provider via new consumer — don't modify order core.

**Architect:** SOLID at service level prevents distributed monolith.

### Architecture Perspective

Maps OOP principles to deployment boundaries — senior interview angle.

### Follow-up Questions

1. **Bounded context vs microservice? — Context may be multiple services — align teams.**
2. **Shared kernel risk? — Shared library couples services — minimize.**

### Common Mistakes in Interviews

- One database table per service as SRP
- Shared mutable library across all services
- SOLID cited without boundary examples

---

## Q072: Keyed DI Services

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Dependency Injection |
| **Frequency** | Common |

### Question

How use keyed services in .NET 8 for multi-tenant providers?

### Short Answer (30 seconds)

`AddKeyedScoped<IPaymentGateway, StripeGateway>("stripe")` — resolve with `[FromKeyedServices("stripe")]` or `GetRequiredKeyedService`.

### Detailed Answer (3–5 minutes)

```csharp
services.AddKeyedScoped<IPaymentGateway, StripeGateway>(TenantPayment.Stripe);

public class CheckoutService(
  [FromKeyedServices(TenantPayment.Stripe)] IPaymentGateway gateway) { }
```

**Architect:** Key from tenant config at runtime via factory when key dynamic per request.

### Architecture Perspective

Keyed services reduce factory boilerplate for variant implementations.

### Follow-up Questions

1. **Factory vs keyed? — Dynamic key from DB → factory wrapping keyed resolve.**
2. **Scope of keyed service? — Same lifetime rules as non-keyed.**

### Common Mistakes in Interviews

- Stringly typed keys without constants
- Keyed singleton holding scoped dependency
- Ten different factories doing same thing

---

## Q073: EF Compiled Queries

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | EF Core |
| **Frequency** | Common |

### Question

When use compiled queries in EF Core?

### Short Answer (30 seconds)

Hot path queries executed millions of times — `EF.CompileAsyncQuery` amortizes query compilation cost.

### Detailed Answer (3–5 minutes)

```csharp
private static readonly Func<AppDbContext, Guid, Task<Order?>> GetOrderById =
  EF.CompileAsyncQuery((AppDbContext db, Guid id) =>
    db.Orders.FirstOrDefault(o => o.Id == id));
```

**Measure first** — compilation savings matter at high QPS.

**Architect:** Platform provides compiled queries for top 10 hot paths.

### Architecture Perspective

Performance optimization with evidence — not premature.

### Follow-up Questions

1. **EF.Compile vs normal? — First call compiles once — reuse Func.**
2. **Interceptors? — Different concern — auditing, soft delete.**

### Common Mistakes in Interviews

- Compiled query for one-off admin report
- No benchmark before optimizing
- Compiled query with uncached SQL injection

---

## Q074: EF Split Query Cartesian

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | EF Core |
| **Frequency** | Common |

### Question

When use `AsSplitQuery()` in EF Core?

### Short Answer (30 seconds)

Multiple `Include` collections cause cartesian explosion — split into separate SQL queries joined in memory.

### Detailed Answer (3–5 minutes)

**Problem:** Include Orders + Items + Payments → huge result set with duplicated order rows.

**Fix:** `.AsSplitQuery()` — multiple queries, one round trip batch.

**Alternative:** Projection with `.Select()` — often better than Include for APIs.

**Architect:** Default split for multi-collection includes in read APIs.

### Architecture Perspective

Cartesian explosion is silent EF perf killer at scale.

### Follow-up Questions

1. **Single query when? — Small graphs — one collection include.**
2. **Filtered include? — EF 5+ filtered Include reduces data.**

### Common Mistakes in Interviews

- Triple Include without split or projection
- AsSplitQuery on simple two-table join unnecessarily
- No SQL logging to detect explosion

---

## Q075: Async Streaming IAsyncEnumerable

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Async |
| **Frequency** | Common |

### Question

When return `IAsyncEnumerable<T>` from ASP.NET Core endpoints?

### Short Answer (30 seconds)

Large result streams — logs export, CSV download, SSE — avoid buffering entire collection in memory.

### Detailed Answer (3–5 minutes)

```csharp
[HttpGet("stream")]
public async IAsyncEnumerable<LogEntry> GetLogs() {
  await foreach (var entry in _repo.StreamAsync())
    yield return entry;
}
```

**Architect:** Set timeout and backpressure — client slow read shouldn't hold DB connection forever.

### Architecture Perspective

Streaming responses reduce memory for large payloads.

### Follow-up Questions

1. **Minimal API streaming? — Supports IAsyncEnumerable results.**
2. **CancellationToken? — Pass to async enumerable cancellation.**

### Common Mistakes in Interviews

- ToListAsync on million rows then return
- No timeout on long streams
- Holding DB connection entire stream without paging

---

## Q076: CancellationToken Propagation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Async |
| **Frequency** | Very Common |

### Question

Why propagate CancellationToken through all async layers?

### Short Answer (30 seconds)

Client disconnect or timeout should cancel DB and HTTP work — saves resources and prevents wasted writes.

### Detailed Answer (3–5 minutes)

```csharp
public async Task<Order> GetAsync(Guid id, CancellationToken ct)
  => await _db.Orders.FirstOrDefaultAsync(o => o.Id == id, ct);
```

**Hosted services:** Honor `stoppingToken` in loops.

**Architect:** Analyzer rule — CancellationToken last parameter on all async public APIs.

### Architecture Perspective

Cancellation is reliability and cost control under load.

### Follow-up Questions

1. **Linked token sources? — Combine timeout + user cancel.**
2. **Fire-and-forget Task? — Dangerous — no cancel, unobserved exceptions.**

### Common Mistakes in Interviews

- Ignoring CancellationToken in repository
- Long-running loop without stoppingToken check
- CancellationToken.None hardcoded

---

## Q077: Middleware vs Filters Performance

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | ASP.NET Core |
| **Frequency** | Common |

### Question

Performance implications of middleware vs action filters?

### Short Answer (30 seconds)

Middleware runs for every request matching pipeline — keep fast. Filters run for MVC actions only — can access action context.

### Detailed Answer (3–5 minutes)

**Middleware:** Correlation ID, exception handling — microseconds.

**Avoid:** Heavy DB calls in middleware for all routes.

**Filter:** Authorization on specific controller.

**Architect:** Performance-critical path audit — middleware chain length and allocations.

### Architecture Perspective

Pipeline depth adds latency — minimize middleware count.

### Follow-up Questions

1. **Conditional middleware? — MapWhen for branch pipelines.**
2. **Response compression middleware? — Enable for JSON APIs over threshold.**

### Common Mistakes in Interviews

- DB lookup in middleware every request
- 20 middleware components
- Synchronous IO in middleware

---

## Q078: Minimal API Authorization Policies

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | ASP.NET Core |
| **Frequency** | Common |

### Question

Apply fine-grained authorization in Minimal APIs.

### Short Answer (30 seconds)

Use `RequireAuthorization(policy)` on groups, `AddAuthorizationBuilder` policies, and claims-based handlers.

### Detailed Answer (3–5 minutes)

```csharp
var admin = app.MapGroup("/admin").RequireAuthorization("AdminOnly");
admin.MapDelete("/users/{id}", DeleteUser).RequireAuthorization(p => p.RequireRole("Admin"));
```

**Architect:** Policy names in constants — same policies in integration tests.

### Architecture Perspective

AuthZ on Minimal APIs equals controller `[Authorize]`.

### Follow-up Questions

1. **IAuthorizationMiddlewareResultHandler? — Custom 403 responses.**
2. **Resource-based auth? — `IAuthorizationHandler` with resource.**

### Common Mistakes in Interviews

- Only authentication no authorization
- Role checks hardcoded in handler body
- Different auth rules Minimal vs controllers same service

---

## Q079: Record vs Class DTOs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | API Design |
| **Frequency** | Common |

### Question

When use record vs class for API DTOs in C#?

### Short Answer (30 seconds)

Records for immutable request/response with value equality — ideal for commands and API contracts. Classes when mutable mapping targets or ORM-shaped objects needed.

### Detailed Answer (3–5 minutes)

```csharp
public record CreateOrderRequest(Guid CustomerId, List<LineItemDto> Items);
```

**Records:** Concise, init-only, good for Minimal API binding.

**Architect:** Consistent DTO style per solution — analyzers enforce.

### Architecture Perspective

DTO immutability reduces accidental mutation bugs.

### Follow-up Questions

1. **record class vs record struct? — Reference vs value semantics.**
2. **Required members C# 11? — Compiler-enforced init.**

### Common Mistakes in Interviews

- Mutable DTOs passed through pipeline
- Entity classes as API contracts
- record with mutable List properties unguarded

---

## Q080: Validation ProblemDetails Shape

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Validation |
| **Frequency** | Common |

### Question

Return field-level validation errors in ProblemDetails format.

### Short Answer (30 seconds)

RFC 7807 ProblemDetails with `errors` extension dictionary mapping field → messages.

### Detailed Answer (3–5 minutes)

```json
{
  "type": "validation_error",
  "title": "Validation failed",
  "status": 400,
  "errors": { "Email": ["Invalid format"] }
}
```

**FluentValidation:** `ValidationProblemDetails` integration in ASP.NET.

**Architect:** Consistent error contract across all services for client SDK generation.

### Architecture Perspective

Standard error shape improves client developer experience.

### Follow-up Questions

1. **traceId in ProblemDetails? — Link support tickets to logs.**
2. **Localization? — Title/message localized — codes stable.**

### Common Mistakes in Interviews

- Plain text error body
- Different error formats per endpoint
- 500 on validation failure

---

## Q081: Polly Hedging Policy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Resilience |
| **Frequency** | Occasional |

### Question

What is hedging in resilience policies and when risky?

### Short Answer (30 seconds)

Send duplicate request if first slow — reduce tail latency. Risky on non-idempotent operations — can double-charge.

### Detailed Answer (3–5 minutes)

**Hedging:** After delay T, fire second request; take first success.

**Safe:** Read-only GET to idempotent search.

**Unsafe:** POST payment without idempotency key.

**Architect:** Hedging only with explicit ADR and downstream dedup.

### Architecture Perspective

Hedging is advanced latency tactic with duplication risk.

### Follow-up Questions

1. **.NET 8 resilience? — Experimental hedging in HTTP extensions.**
2. **AWS SDK hedging? — Some clients built-in — understand semantics.**

### Common Mistakes in Interviews

- Hedge POST mutations
- No idempotency key with hedging
- Hedge amplifies outage load

---

## Q082: HybridCache Two Tier

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Caching |
| **Frequency** | Common |

### Question

How does .NET 9 HybridCache combine L1 and L2 caching?

### Short Answer (30 seconds)

HybridCache checks in-memory L1 then distributed L2 — stampede protection and tag-based invalidation built-in.

### Detailed Answer (3–5 minutes)

```csharp
await hybridCache.GetOrCreateAsync($"product:{id}", async ct => await LoadFromDb(id));
```

**Architect:** Platform default for read-heavy catalog — replaces hand-rolled cache-aside + lock.

### Architecture Perspective

HybridCache simplifies enterprise caching patterns.

### Follow-up Questions

1. **Tags for invalidation? — Invalidate all products in category.**
2. **Stampede protection? — Built-in — compare manual mutex.**

### Common Mistakes in Interviews

- Hand-rolled cache-aside when HybridCache fits
- L1 stale after L2 invalidation without tags
- Cache user-specific data globally keyed wrong

---

## Q083: Chain of Responsibility HTTP

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Design Patterns |
| **Frequency** | Common |

### Question

Implement Chain of Responsibility with HttpClient DelegatingHandlers.

### Short Answer (30 seconds)

Each handler processes request/response — logging, auth header, retry — calls `base.SendAsync` for next.

### Detailed Answer (3–5 minutes)

```csharp
public class CorrelationIdHandler : DelegatingHandler {
  protected override async Task<HttpResponseMessage> SendAsync(...) {
    request.Headers.Add("X-Correlation-ID", id);
    return await base.SendAsync(request, ct);
  }
}
```

**Order:** Outermost handler registered last — understand chain direction.

**Architect:** Platform registers standard handler pack on all outbound clients.

### Architecture Perspective

CoR is HttpClient middleware — practical .NET pattern.

### Follow-up Questions

1. **Handler vs Polly policy? — Often combined — handler wraps policy.**
2. **Too many handlers? — Consolidate observability handlers.**

### Common Mistakes in Interviews

- Wrong handler registration order
- Handler doing business logic
- No correlation propagation handler

---

## Q084: Unit of Work Explicit

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Data Access |
| **Frequency** | Common |

### Question

When wrap EF DbContext in explicit IUnitOfWork interface?

### Short Answer (30 seconds)

When domain services shouldn't reference EF types but need transaction boundary — `Commit()`/`Rollback()` abstracts SaveChanges.

### Detailed Answer (3–5 minutes)

```csharp
public interface IUnitOfWork {
  Task CommitAsync(CancellationToken ct);
}
```

**Scoped per request:** One UoW per HTTP request aligns with DbContext scope.

**Architect:** MediatR transaction behavior calls UoW.Commit after successful handler.

### Architecture Perspective

Explicit UoW clarifies transaction intent in application layer.

### Follow-up Questions

1. **Multiple DbContexts? — Distributed transaction or saga — not one UoW.**
2. **SaveChanges in repository every method? — Breaks atomic use case.**

### Common Mistakes in Interviews

- Commit after every repository call
- Singleton UoW
- UoW across microservice HTTP calls

---

## Q085: Testcontainers EF Integration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Testing |
| **Frequency** | Common |

### Question

Use Testcontainers for EF Core integration tests in CI.

### Short Answer (30 seconds)

Spin real SQL Server/Postgres container per test run — apply migrations, exercise real SQL, dispose container.

### Detailed Answer (3–5 minutes)

```csharp
var container = new PostgreSqlBuilder().Build();
await container.StartAsync();
// configure DbContext with container connection string
```

**Architect:** Standard test fixture in platform template — consistent across teams.

### Architecture Perspective

Testcontainers bridges unit and production fidelity.

### Follow-up Questions

1. **Reuse container across tests? — Fixture pattern — faster CI.**
2. **Azurite for blob tests? — Emulator container for storage integration.**

### Common Mistakes in Interviews

- In-memory EF provider for SQL-specific tests
- Prod database for CI tests
- No migration apply in fixture setup

---

## Q086: WebApplicationFactory Customize

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Testing |
| **Frequency** | Common |

### Question

Override services in WebApplicationFactory for tests.

### Short Answer (30 seconds)

`ConfigureWebHost` with `services.Replace` or `RemoveAll` + mock — swap external HTTP with WireMock.

### Detailed Answer (3–5 minutes)

```csharp
protected override void ConfigureWebHost(IWebHostBuilder builder) {
  builder.ConfigureTestServices(services => {
    services.RemoveAll<IPaymentGateway>();
    services.AddSingleton<IPaymentGateway, FakePaymentGateway>();
  });
}
```

**Architect:** Fakes over mocks for complex gateways — real behavior subset.

### Architecture Perspective

Test host customization is integration test core skill.

### Follow-up Questions

1. **Environment=test? — Separate config — no prod Key Vault.**
2. **Authentication in tests? — `AddAuthentication("Test").AddScheme` fake user.**

### Common Mistakes in Interviews

- Testing against real payment API
- Not isolating external dependencies
- Shared mutable fake singleton between tests

---

## Q087: HttpClient DNS and K8s

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | HTTP |
| **Frequency** | Very Common |

### Question

Why does HttpClient DNS matter in Kubernetes deployments?

### Short Answer (30 seconds)

Pod IPs change on rollout — singleton HttpClient caches DNS — requests hit dead pods until process restart.

### Detailed Answer (3–5 minutes)

**Fix:** `PooledConnectionLifetime = TimeSpan.FromMinutes(2)` on SocketsHttpHandler.

**K8s:** Service ClusterIP stable but endpoint pods rotate.

**Architect:** Platform HttpClient factory template enforces PooledConnectionLifetime.

### Architecture Perspective

DNS staleness causes mysterious partial outages after deploy.

### Follow-up Questions

1. **Service mesh? — Sidecar may affect connection handling.**
2. **Headless service? — Direct pod DNS — more churn.**

### Common Mistakes in Interviews

- Static HttpClient in long-running pods
- No connection lifetime config
- Blame app code not DNS on rollout failures

---

## Q088: API Deprecation Policy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | API Design |
| **Frequency** | Common |

### Question

Design API deprecation communication for enterprise clients.

### Short Answer (30 seconds)

Sunset header, Release-Notes, version timeline, metrics on v1 traffic, breaking change only in new major version.

### Detailed Answer (3–5 minutes)

**Headers:**
- `Deprecation: true`
- `Sunset: Sat, 01 Jan 2027 00:00:00 GMT`
- `Link: </v2/orders>; rel="successor-version"`

**Architect:** 6–12 month migration window — track adoption dashboard.

### Architecture Perspective

API lifecycle management is architect responsibility.

### Follow-up Questions

1. **Telemetry on version? — Log Api-Version header per request.**
2. **Forced migration? — Communicate early — partner SLAs.**

### Common Mistakes in Interviews

- Silent breaking change in patch release
- Deprecate without sunset date
- No metrics on old version usage

---

## Q089: IExceptionHandler Chain

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | ASP.NET Core |
| **Frequency** | Common |

### Question

Use multiple IExceptionHandler implementations in .NET 8.

### Short Answer (30 seconds)

Register handlers that return `true` when handled — chain tries each until one handles.

### Detailed Answer (3–5 minutes)

```csharp
builder.Services.AddExceptionHandler<ValidationExceptionHandler>();
builder.Services.AddExceptionHandler<GlobalExceptionHandler>();
builder.Services.AddProblemDetails();
```

**Order:** Specific handlers before catch-all.

**Architect:** One handler per bounded context exception family.

### Architecture Perspective

.NET 8 exception handling modernizes middleware approach.

### Follow-up Questions

1. **ProblemDetails customization? — `CustomizeProblemDetails` event.**
2. **Developer exception page? — Dev only — never prod.**

### Common Mistakes in Interviews

- Single giant switch handler
- Handler order wrong — catch-all swallows specific
- No ProblemDetails registration

---

## Q090: MediatR vs Direct Service

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | MediatR |
| **Frequency** | Common |

### Question

When is MediatR overkill for a small API?

### Short Answer (30 seconds)

Under ~10 endpoints with no shared pipelines — direct application service may be simpler. MediatR pays off with validation/logging behaviors and growing endpoint count.

### Detailed Answer (3–5 minutes)

**Skip MediatR:** Internal tool, CRUD prototype.

**Use MediatR:** 30+ endpoints, multiple teams, pipeline behaviors needed.

**Architect:** Revisit when service grows — strangler inject MediatR incrementally.

### Architecture Perspective

Pragmatic pattern adoption — not mandatory everywhere.

### Follow-up Questions

1. **Wolverine/Marten alternatives? — Higher throughput pipelines — evaluate.**
2. **Mediator as god service? — Handlers stay small — one use case each.**

### Common Mistakes in Interviews

- MediatR on 5-endpoint service unnecessarily
- God handler doing everything
- No pipeline behaviors — MediatR as pointless indirection

---

## Q091: Outbox with MediatR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | MediatR |
| **Frequency** | Common |

### Question

Publish integration events reliably with transactional outbox.

### Short Answer (30 seconds)

Save domain changes and outbox row in same DB transaction; background worker publishes to Service Bus and marks sent.

### Detailed Answer (3–5 minutes)

**Flow:**
1. Handler saves order + OutboxMessage in one transaction
2. `OutboxProcessor` polls unpublished rows
3. Publish to topic → mark processed

**Avoid:** Publish to bus then save DB — dual-write failure.

**Architect:** Outbox library (MassTransit, custom) standard on platform.

### Architecture Perspective

Reliable messaging requires outbox or inbox pattern.

### Follow-up Questions

1. **Idempotent consumer? — Bus messageId dedup table.**
2. **Polling vs CDC? — Debezium/CDC lower latency than poll.**

### Common Mistakes in Interviews

- await bus.Publish before SaveChanges
- No idempotency on consumer
- Outbox without dead-letter on publish failure

---

## Q092: Specification Pattern EF

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Data Access |
| **Frequency** | Common |

### Question

Implement Specification pattern for reusable EF queries.

### Short Answer (30 seconds)

Encapsulate query criteria in `ISpecification<T>` — composable And/Or — repository applies to IQueryable.

### Detailed Answer (3–5 minutes)

```csharp
public class ActiveOrdersSpec : Specification<Order> {
  public override Expression<Func<Order, bool>> Criteria => o => o.Status == Active;
}
```

**Architect:** Specifications live in application/domain — infrastructure translates to EF.

### Architecture Perspective

Specification reduces duplicated LINQ across handlers.

### Follow-up Questions

1. **Ardalis Specification library? — Popular — includes repository base.**
2. **Over-specification? — Simple one-off Where doesn't need spec class.**

### Common Mistakes in Interviews

- Specification returning IQueryable to controller
- Un composable copy-paste LINQ
- Spec with Include leaking to API layer

---

## Q093: Value Objects EF Core

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | EF Core |
| **Frequency** | Common |

### Question

Map value objects in EF Core 8 owned entities.

### Short Answer (30 seconds)

Use `OwnsOne` for Address, Money — value object columns grouped, no identity.

### Detailed Answer (3–5 minutes)

```csharp
modelBuilder.Entity<Order>().OwnsOne(o => o.ShippingAddress);
```

**DDD:** Value objects immutable — equality by value.

**Architect:** Owned types keep domain rich without separate tables for every value object.

### Architecture Perspective

Value objects in EF support DDD modeling.

### Follow-up Questions

1. **Complex type mapping? — EF 8+ improved complex types.**
2. **Value object collections? — OwnsMany for line item value types.**

### Common Mistakes in Interviews

- Primitive obsession strings for Address
- Mutable value objects
- Separate table for every value object unnecessarily

---

## Q094: Interceptors Auditing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | EF Core |
| **Frequency** | Common |

### Question

Use EF Core interceptors for audit fields.

### Short Answer (30 seconds)

`SaveChangesInterceptor` sets `CreatedAt`, `UpdatedBy` from ICurrentUserService before save.

### Detailed Answer (3–5 minutes)

```csharp
public override InterceptionResult<int> SavingChanges(
  DbContextEventData eventData, InterceptionResult<int> result) {
  foreach (var entry in eventData.Context.ChangeTracker.Entries<IAuditable>())
    if (entry.State == Added) entry.Entity.CreatedAt = _clock.UtcNow;
  return result;
}
```

**Architect:** Central audit — not copy-paste in every repository method.

### Architecture Perspective

Interceptors DRY cross-cutting persistence concerns.

### Follow-up Questions

1. **Soft delete interceptor? — Convert Delete to Update IsDeleted.**
2. **Slow query interceptor? — Log commands exceeding threshold.**

### Common Mistakes in Interviews

- Audit logic in every handler
- Interceptor accessing HttpContext incorrectly in background
- Missing audit on raw SQL bypass

---

## Q095: API Rate Limiting .NET 7

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | ASP.NET Core |
| **Frequency** | Common |

### Question

Configure built-in rate limiting in ASP.NET Core.

### Short Answer (30 seconds)

`AddRateLimiter` with fixed window or token bucket; `RequireRateLimiting` on endpoints.

### Detailed Answer (3–5 minutes)

```csharp
builder.Services.AddRateLimiter(o => o.AddFixedWindowLimiter("api", opt => {
  opt.PermitLimit = 100; opt.Window = TimeSpan.FromMinutes(1);
}));
app.MapGet("/orders").RequireRateLimiting("api");
```

**Architect:** Per-tenant limits via partition resolver on API key.

### Architecture Perspective

Rate limiting protects APIs at edge or app layer.

### Follow-up Questions

1. **APIM vs in-app? — APIM for multi-service; in-app for single service.**
2. **429 response? — Retry-After header — clients backoff.**

### Common Mistakes in Interviews

- No rate limit on public API
- Global limit without per-tenant fairness
- Rate limit only in documentation

---

## Q096: Health Checks Liveness Readiness

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | ASP.NET Core |
| **Frequency** | Common |

### Question

Design separate liveness and readiness health endpoints.

### Short Answer (30 seconds)

Liveness: process alive — restart if fails. Readiness: can serve traffic — exclude from load balancer if DB down.

### Detailed Answer (3–5 minutes)

```csharp
services.AddHealthChecks()
  .AddCheck("self", () => Healthy())
  .AddSqlServer(conn, name: "db", tags: new[] { "ready" });

app.MapHealthChecks("/health/live", new() { Predicate = _ => false });
app.MapHealthChecks("/health/ready", new() { Predicate = c => c.Tags.Contains("ready") });
```

**Architect:** K8s probes map to correct endpoints — don't kill pod on external dep blip in liveness.

### Architecture Perspective

Health check design prevents cascading wrong restarts.

### Follow-up Questions

1. **Startup probe? — Slow .NET cold start.**
2. **Health check auth? — Internal network only.**

### Common Mistakes in Interviews

- HTTP check external payment in liveness
- Single /health for everything
- Readiness includes optional non-critical deps

---

## Q097: Source Generated Regex Validation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Modern C# |
| **Frequency** | Occasional |

### Question

Use compile-time regex for input validation in .NET.

### Short Answer (30 seconds)

`[GeneratedRegex("^[a-zA-Z0-9]+$")] partial Regex SkuRegex()` — no runtime regex compile cost.

### Detailed Answer (3–5 minutes)

**Benefit:** Faster startup, trim-friendly, analyzer validates pattern at compile time.

**Use:** SKU format, postal code validation in FluentValidation or attributes.

**Architect:** Platform analyzers prefer GeneratedRegex over `new Regex()` in hot paths.

### Architecture Perspective

Modern .NET performance micro-optimizations show currency.

### Follow-up Questions

1. **RegexOptions? — Specify in attribute — Compiled unnecessary.**
2. **ReDoS risk? — Audit patterns — timeout where needed.**

### Common Mistakes in Interviews

- Complex regex compiled every request
- User-supplied regex patterns
- No timeout on dynamic regex

---

## Q098: Native AOT API Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Performance |
| **Frequency** | Occasional |

### Question

Trade-offs publishing ASP.NET API as Native AOT.

### Short Answer (30 seconds)

Faster cold start, smaller image, no JIT — but reflection limits, longer builds, some EF/features restricted.

### Detailed Answer (3–5 minutes)

**Good:** Edge functions, high-scale cold start sensitive.

**Bad:** Heavy EF, reflection serializers, dynamic plugins.

**Architect:** Measure cold start and build time before mandating AOT.

### Architecture Perspective

AOT is workload-specific — not default for all APIs.

### Follow-up Questions

1. **Trimming warnings? — Must resolve — silent breakage risk.**
2. **JSON source gen? — Required for AOT serialization.**

### Common Mistakes in Interviews

- AOT mandate without compatibility audit
- Ignore trim warnings
- Dynamic plugin load with AOT

---

## Q099: ProblemDetails Security

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | ASP.NET Core |
| **Frequency** | Common |

### Question

Balance informative ProblemDetails with security.

### Short Answer (30 seconds)

Return type, title, status, traceId to clients — log full exception server-side only. No stack trace, internal host names, or SQL in response.

### Detailed Answer (3–5 minutes)

**Extensions:** `errorCode` for client branching — not exception message from DB.

**409 Conflict:** Safe business message — 'Order already shipped'.

**500:** Generic title — details in logs with correlation ID.

**Architect:** Security review error responses like any API surface.

### Architecture Perspective

Error responses are information disclosure vector.

### Follow-up Questions

1. **Exception middleware dev vs prod? — Developer page dev only.**
2. **HSTS and security headers? — Separate from ProblemDetails.**

### Common Mistakes in Interviews

- SqlException message to client
- Stack trace in staging exposed publicly
- Same verbose errors all environments

---

## Q100: Vertical Slice Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Architecture |
| **Frequency** | Very Common |

### Question

Organize .NET API as vertical slices instead of layered folders.

### Short Answer (30 seconds)

Group by feature `Features/Orders/Create/` — handler, validator, endpoint together — not `Controllers/`, `Services/` by type.

### Detailed Answer (3–5 minutes)

**Benefits:** Cohesion, easier navigation, independent feature evolution.

**Shared:** Domain primitives, infrastructure extensions in separate folders.

**Architect:** Vertical slices pair well with MediatR and Minimal APIs.

### Architecture Perspective

Folder structure reflects change isolation — interview architecture topic.

### Follow-up Questions

1. **Shared kernel folder? — Cross-feature utilities — keep minimal.**
2. **ReSharper/rider structure? — Teams adapt tooling to slices.**

### Common Mistakes in Interviews

- Giant Services folder 80 classes
- Vertical slice with shared mutable static state
- Layers duplicated inside every slice unnecessarily

---
