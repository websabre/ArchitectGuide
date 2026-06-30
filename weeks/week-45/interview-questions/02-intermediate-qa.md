# Week 45 — Intermediate Q&A

> Q031–Q070: Premium format (Week 1 quality).

---


## Q031: SRP in .NET Services

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SOLID |
| **Frequency** | Very Common |

### Question

What does Single Responsibility Principle mean for a .NET service class?

### Short Answer (30 seconds)

One class, one reason to change. Split validation, persistence, and notification into separate collaborators instead of one god service.

### Detailed Answer (3–5 minutes)

**SRP:** A module should have only one axis of change — business rules, persistence, or integration — not all three.

**Violation:** `OrderService` validates, saves to SQL, sends email, and calls payment gateway.

**Fix:** `OrderValidator`, `IOrderRepository`, `INotificationService`, `IPaymentGateway` injected into a thin `PlaceOrderHandler`.

**Architect lens:** SRP at the service boundary mirrors microservice cohesion — one bounded context per deployable unit.

### Architecture Perspective

Interviewers want refactor instinct with a concrete before/after example.

### Follow-up Questions

1. **SRP vs one microservice per class? — Cohesion matters — don't over-split.**
2. **How detect SRP violation in review? — Multiple unrelated using statements and change-request sources.**

### Common Mistakes in Interviews

- Defining SRP as one public method per class
- Splitting into dozens of one-liner classes
- Ignoring stakeholder-driven reasons to change

---

## Q032: Open Closed in ASP.NET

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SOLID |
| **Frequency** | Very Common |

### Question

How apply Open/Closed Principle when adding new payment providers?

### Short Answer (30 seconds)

Add new `IPaymentGateway` implementation and DI registration — don't edit stable checkout code with another switch statement.

### Detailed Answer (3–5 minutes)

**OCP:** Open for extension (new types), closed for modification (stable core).

**Pattern:**
```csharp
services.AddKeyedScoped<IPaymentGateway, StripeGateway>(PaymentProvider.Stripe);
services.AddKeyedScoped<IPaymentGateway, AdyenGateway>(PaymentProvider.Adyen);
```

**Anti-pattern:** `switch(paymentType)` growing in `CheckoutService` every sprint.

**Architect:** Document extension points in ADR — which assemblies are stable vs pluggable.

### Architecture Perspective

OCP shows how platforms scale feature velocity without regression on core paths.

### Follow-up Questions

1. **OCP vs YAGNI? — Introduce extension point when second variant is certain.**
2. **Strategy pattern relation? — Strategy is the usual OCP implementation.**

### Common Mistakes in Interviews

- Editing shared library for every new provider
- Abstract factory before second use case exists
- Giant switch/if-else chains in domain services

---

## Q033: Liskov and Interfaces

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SOLID |
| **Frequency** | Common |

### Question

Give a Liskov Substitution Principle violation in .NET repository design.

### Short Answer (30 seconds)

A `ReadOnlyRepository` that throws `NotSupportedException` on `Delete` breaks callers expecting full `IRepository` behavior.

### Detailed Answer (3–5 minutes)

**LSP:** Subtypes must honor the contract of the base type without surprising callers.

**Violation:**
```csharp
public class ReadOnlyOrderRepo : IOrderRepository {
  public void Delete(Guid id) => throw new NotSupportedException();
}
```

**Fix:** Segregate `IOrderReader` and `IOrderWriter` — consumers depend only on what they use.

**Architect:** Contract tests on interface implementations catch LSP violations in CI.

### Architecture Perspective

LSP connects inheritance design to production bugs when mocks don't match real behavior.

### Follow-up Questions

1. **LSP vs ISP? — Smaller interfaces prevent unsupported operations.**
2. **Testing LSP? — Property-based tests across all implementations.**

### Common Mistakes in Interviews

- Subclass silently changing expected behavior
- Throwing NotSupportedException on half the interface
- Mock in tests that violates production contract

---

## Q034: Interface Segregation APIs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SOLID |
| **Frequency** | Common |

### Question

How does Interface Segregation apply to API client SDK design?

### Short Answer (30 seconds)

Split fat `IAdminApiClient` into `IOrderReader`, `IOrderWriter`, and `IReportExporter` — mobile BFF takes only reader interface.

### Detailed Answer (3–5 minutes)

**ISP:** Clients should not depend on methods they don't use.

**Fat interface smell:** Reporting service forced to reference bulk-delete methods.

**API parallel:** Don't expose 40-field admin DTO on public mobile endpoint — separate read contracts.

**Architect:** Segregation clarifies security boundaries — read-only service account gets `IReader` only.

### Architecture Perspective

ISP is dependency and permission minimization — critical for zero-trust service accounts.

### Follow-up Questions

1. **ISP vs too many interfaces? — Segregate by client role, not every method.**
2. **CQRS connection? — Command/query split is ISP at architecture level.**

### Common Mistakes in Interviews

- One IRepository<T> with 15 methods for all consumers
- Admin operations on same interface as public API
- Segregating into unusable one-method interfaces

---

## Q035: Dependency Inversion Basics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SOLID |
| **Frequency** | Very Common |

### Question

What is Dependency Inversion and why inject `IOrderRepository` not `SqlOrderRepository`?

### Short Answer (30 seconds)

High-level modules depend on abstractions. Domain defines ports; infrastructure implements adapters; DI wires at composition root.

### Detailed Answer (3–5 minutes)

**DIP layers:**
1. Domain defines `IOrderRepository`
2. Infrastructure implements `SqlOrderRepository`
3. `Program.cs`: `AddScoped<IOrderRepository, SqlOrderRepository>`

**Benefits:** Unit test with fakes, swap stores without domain change, clear module boundaries.

**Architect:** Domain never imports EF or HTTP — hexagonal architecture foundation.

### Architecture Perspective

DIP is the foundation of testable .NET microservices.

### Follow-up Questions

1. **DI vs service locator? — Constructor injection only — locator hides dependencies.**
2. **Composition root rule? — Only startup references concrete types.**

### Common Mistakes in Interviews

- Domain project references Entity Framework
- new SqlConnection() inside business logic
- Static singletons in domain layer

---

## Q036: DI Singleton vs Scoped

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Dependency Injection |
| **Frequency** | Very Common |

### Question

When register a service as Singleton vs Scoped in ASP.NET Core?

### Short Answer (30 seconds)

Singleton for stateless app-wide services (config, caches). Scoped for per-request state (DbContext, current user). Never inject Scoped into Singleton.

### Detailed Answer (3–5 minutes)

**Rules:**
- `DbContext` → Scoped
- Stateless helpers → Singleton or Transient
- `IHttpContextAccessor` → Singleton (accesses scoped via accessor)

**Captive dependency:** Singleton holding Scoped `DbContext` — stale data, thread bugs.

**Fix:** `IServiceScopeFactory` in background singleton work.

### Architecture Perspective

Lifetime mistakes cause production-only concurrency bugs.

### Follow-up Questions

1. **ValidateOnBuild? — Catches captive dependencies at startup.**
2. **Transient when? — Lightweight stateless per-resolve services.**

### Common Mistakes in Interviews

- Singleton injecting DbContext
- Transient DbContext per property resolve
- Background service without scope factory

---

## Q037: Constructor Injection Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Dependency Injection |
| **Frequency** | Very Common |

### Question

Why prefer constructor injection over property or method injection?

### Short Answer (30 seconds)

Constructor injection makes dependencies explicit, immutable, and required — class cannot be constructed in invalid state.

### Detailed Answer (3–5 minutes)

```csharp
public class OrderService(IOrderRepository repo, ILogger<OrderService> log) {
  // all deps visible, testable
}
```

**Avoid:** `[FromServices]` on action methods for core deps — hides class requirements.

**Architect:** Enforce via analyzers — no `new` for infrastructure in domain.

### Architecture Perspective

Explicit dependencies improve testability and code review clarity.

### Follow-up Questions

1. **Primary constructors C# 12? — Same semantics, less boilerplate.**
2. **Too many ctor params? — Class may violate SRP — split responsibilities.**

### Common Mistakes in Interviews

- Service locator in constructors
- Optional dependencies as nullables without design
- Property injection for required services

---

## Q038: EF Core Include vs Projection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | EF Core |
| **Frequency** | Very Common |

### Question

How fix N+1 queries when loading orders with line items?

### Short Answer (30 seconds)

Use `.Include(o => o.Items)` for eager load, or `.Select()` projection to fetch only needed columns in one query.

### Detailed Answer (3–5 minutes)

**N+1 problem:**
```csharp
var orders = await _db.Orders.ToListAsync();
foreach (var o in orders) { var x = o.Items; } // lazy load per order
```

**Fixes:**
1. `.Include(o => o.Items)`
2. Projection: `.Select(o => new OrderDto { ... })`
3. `.AsSplitQuery()` for multiple collections

**Detection:** EF SQL logging, MiniProfiler, App Insights dependency traces.

### Architecture Perspective

N+1 is the #1 EF production performance bug.

### Follow-up Questions

1. **AsNoTracking for read lists? — Reduces memory and tracking overhead.**
2. **When not to Include? — Large graphs — project instead.**

### Common Mistakes in Interviews

- Lazy loading enabled globally in APIs
- Include entire object graph by default
- Not profiling SQL in staging

---

## Q039: EF Core Tracking Modes

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | EF Core |
| **Frequency** | Common |

### Question

When use `AsNoTracking()` in EF Core queries?

### Short Answer (30 seconds)

Read-only queries that won't be updated — lists, reports, API GET responses. Reduces memory and CPU from change tracking.

### Detailed Answer (3–5 minutes)

```csharp
var orders = await _db.Orders.AsNoTracking()
  .Where(o => o.CustomerId == id)
  .ToListAsync();
```

**With updates:** Use tracked queries or explicit `Attach`/`Update`.

**Architect:** Default read repositories to no-tracking; command side uses tracked entities for aggregates.

### Architecture Perspective

Tracking mode choice affects API memory under load.

### Follow-up Questions

1. **AsNoTrackingWithIdentityResolution? — Graphs with shared references.**
2. **Global NoTracking? — Risk if writes expect tracking.**

### Common Mistakes in Interviews

- AsNoTracking on entities you then SaveChanges
- Tracking enabled on million-row exports
- No distinction read vs write queries

---

## Q040: async await ASP.NET

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Async |
| **Frequency** | Very Common |

### Question

Why use async/await in ASP.NET Core controllers and what happens if you block?

### Short Answer (30 seconds)

Async frees threads during I/O — higher throughput. Blocking with `.Result` or `.Wait()` risks thread-pool starvation and deadlocks.

### Detailed Answer (3–5 minutes)

**Correct:**
```csharp
public async Task<Order> Get(Guid id)
  => await _repo.GetAsync(id);
```

**Wrong:**
```csharp
return _repo.GetAsync(id).Result; // blocks thread pool
```

**Architect:** Async all the way through HTTP → DB → external APIs. Use `Task.Run` only for CPU-bound work offloaded intentionally.

### Architecture Perspective

Async throughput is a production scalability topic, not syntax trivia.

### Follow-up Questions

1. **ValueTask when? — Hot paths with frequent synchronous completion.**
2. **async void? — Only event handlers — never in services.**

### Common Mistakes in Interviews

- .Result or .GetAwaiter().GetResult() in request path
- async void service methods
- Fake async — Task.Run wrapping sync I/O unnecessarily

---

## Q041: ConfigureAwait in Libraries

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Async |
| **Frequency** | Common |

### Question

Should shared .NET library code use `ConfigureAwait(false)`?

### Short Answer (30 seconds)

Yes in library code to avoid capturing caller synchronization context. ASP.NET Core app code generally doesn't need it — no legacy sync context.

### Detailed Answer (3–5 minutes)

**Library:**
```csharp
await reader.ReadAsync().ConfigureAwait(false);
```

**ASP.NET Core:** HttpContext flows via `AsyncLocal` — ConfigureAwait(false) rarely required in controllers.

**Architect:** Coding standard — analyzers enforce ConfigureAwait(false) in shared packages.

### Architecture Perspective

Async context rules differ for library vs application code.

### Follow-up Questions

1. **Task.Run for CPU work? — Offloads thread pool — measure before defaulting.**
2. **CancellationToken propagation? — Pass from controller through all awaits.**

### Common Mistakes in Interviews

- ConfigureAwait(false) blindly in every ASP.NET line
- Ignoring CancellationToken in library APIs
- Blocking sync over async endpoints

---

## Q042: Middleware Pipeline Order

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | ASP.NET Core |
| **Frequency** | Very Common |

### Question

List the correct ASP.NET Core middleware order for a secured API.

### Short Answer (30 seconds)

Exception handler → HTTPS → routing → CORS → authentication → authorization → endpoints. Correlation ID early; auth before authz.

### Detailed Answer (3–5 minutes)

**Order matters:** Each middleware wraps the next.

1. Exception handling (outermost)
2. HTTPS redirection
3. Routing
4. CORS (before auth for preflight)
5. Authentication
6. Authorization
7. Endpoints

**Wrong order symptoms:** 401 on CORS preflight, unauthorized access slipping through.

### Architecture Perspective

Wrong middleware order causes 'works locally' auth and CORS bugs.

### Follow-up Questions

1. **Terminal middleware? — Map/Run short-circuit — nothing after runs.**
2. **Request buffering? — Enable early if body read multiple times.**

### Common Mistakes in Interviews

- Authorization before Authentication
- CORS after endpoints
- Exception handler innermost

---

## Q043: Custom Middleware Use Case

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | ASP.NET Core |
| **Frequency** | Common |

### Question

When write custom middleware vs endpoint filter in Minimal APIs?

### Short Answer (30 seconds)

Middleware for cross-cutting pipeline concerns (correlation ID, global logging). Endpoint filters for per-route validation and auth nuances.

### Detailed Answer (3–5 minutes)

**Middleware:**
```csharp
app.Use(async (ctx, next) => {
  var id = ctx.Request.Headers["X-Correlation-ID"].FirstOrDefault() ?? Guid.NewGuid().ToString();
  ctx.Items["CorrelationId"] = id;
  await next();
});
```

**Endpoint filter:** Validation on specific route group only.

**Architect:** Don't duplicate — one correlation middleware, not per-controller copy-paste.

### Architecture Perspective

Middleware vs filters is scope decision — pipeline-wide vs route-specific.

### Follow-up Questions

1. **IMiddleware vs convention middleware? — IMiddleware is DI-activated per request.**
2. **Short-circuiting middleware? — Don't call next() to stop pipeline.**

### Common Mistakes in Interviews

- Business logic in middleware
- Duplicate middleware registered twice
- Filter for correlation ID on every route separately

---

## Q044: Minimal API Structure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | ASP.NET Core |
| **Frequency** | Common |

### Question

How structure Minimal APIs for a production .NET microservice?

### Short Answer (30 seconds)

Use endpoint groups, separate handler classes, validation filters, OpenAPI, and auth policies — not 200-line lambdas in Program.cs.

### Detailed Answer (3–5 minutes)

```csharp
var orders = app.MapGroup("/orders").RequireAuthorization();
orders.MapPost("/", CreateOrder.Handle);
```

**Add:** Carter/vertical slices, ProblemDetails, API versioning, rate limiting.

**Architect:** Team consistency matters more than Minimal vs controllers religion.

### Architecture Perspective

Minimal APIs are production-ready with structure discipline.

### Follow-up Questions

1. **MapGroup benefits? — Shared prefix, filters, auth per group.**
2. **Testing? — WebApplicationFactory works same as controllers.**

### Common Mistakes in Interviews

- 500-line lambda in Program.cs
- No auth on 'internal' endpoints
- Skipping OpenAPI on public APIs

---

## Q045: Minimal API vs Controllers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | ASP.NET Core |
| **Frequency** | Common |

### Question

When choose Minimal APIs over MVC controllers?

### Short Answer (30 seconds)

Minimal APIs for small services, BFFs, and internal tools with few endpoints. Controllers when complex model binding, filters ecosystem, or team familiarity favors MVC.

### Detailed Answer (3–5 minutes)

| Factor | Minimal | Controllers |
|--------|---------|-------------|
| Ceremony | Low | Higher |
| Model binding | Good, simpler cases | Rich |
| Filters | Endpoint filters | Mature ecosystem |
| Team skill | Newer pattern | Familiar |

**Architect:** Pick one per service — mixing styles in one codebase hurts onboarding.

### Architecture Perspective

Choice is team and complexity fit — not performance myth.

### Follow-up Questions

1. **Minimal API versioning? — Asp.Versioning packages support both.**
2. **Razor Pages? — Different use case — server-rendered UI.**

### Common Mistakes in Interviews

- Controllers for 3-endpoint microservice unnecessarily
- Minimal APIs for complex form uploads without structure
- Mixing both patterns randomly in one service

---

## Q046: DTO Purpose

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | API Design |
| **Frequency** | Very Common |

### Question

Why use DTOs instead of returning EF entities from APIs?

### Short Answer (30 seconds)

Control exposed shape, prevent over-posting, avoid circular reference serialization, and decouple API contract from domain refactoring.

### Detailed Answer (3–5 minutes)

**Risks of exposing entities:**
- Lazy-load serialization triggers N+1
- Internal fields leaked (`PasswordHash`)
- Breaking API when domain changes

**Pattern:** Request/response records in application layer; map with Mapster or manual methods.

### Architecture Perspective

DTO boundary is API security and evolution.

### Follow-up Questions

1. **Record DTOs? — Immutable request types — great for Minimal APIs.**
2. **Separate read/write DTOs? — CQRS-friendly — different shapes.**

### Common Mistakes in Interviews

- Return EF entities with navigation properties
- Same DTO for create and complex read
- AutoMapper config untested — silent null mapping

---

## Q047: Over-Posting Prevention

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | API Design |
| **Frequency** | Common |

### Question

How prevent over-posting attacks in ASP.NET Core APIs?

### Short Answer (30 seconds)

Bind only intended input DTO fields — never entity directly. Use `[BindNever]` or separate create DTO without privileged fields like `IsAdmin`.

### Detailed Answer (3–5 minutes)

```csharp
public record CreateUserRequest(string Email, string Name);
// NOT: User entity with Role, IsVerified
```

**Mass assignment:** Attacker sends `{"isAdmin": true}` if entity bound.

**Architect:** Input DTOs are allow-lists — explicit fields only.

### Architecture Perspective

Over-posting is OWASP API risk — DTOs are the fix.

### Follow-up Questions

1. **FluentValidation on DTO? — Validate shape before mapping to command.**
2. **PATCH partial updates? — JsonPatch or dedicated patch DTO.**

### Common Mistakes in Interviews

- Bind entity directly from JSON body
- Same model for admin and public create
- Trust client-sent Id or audit fields

---

## Q048: FluentValidation Setup

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Validation |
| **Frequency** | Very Common |

### Question

How integrate FluentValidation in ASP.NET Core pipeline?

### Short Answer (30 seconds)

Register validators from assembly, use auto-validation or MediatR pipeline behavior, return ProblemDetails on failure.

### Detailed Answer (3–5 minutes)

```csharp
services.AddValidatorsFromAssemblyContaining<CreateOrderValidator>();
```

**Layers:**
1. Request validation — format, required fields
2. Domain validation — business invariants
3. DB constraints — last defense

**Architect:** Single validation path — not duplicated in controller and service.

### Architecture Perspective

Validation pipeline shows clean architecture layering.

### Follow-up Questions

1. **FluentValidation vs DataAnnotations? — Fluent for complex rules.**
2. **Client-side only? — Never sufficient — always server validate.**

### Common Mistakes in Interviews

- Validation only in UI
- Business rules in FluentValidation that belong in domain
- 500 instead of 400 on validation failure

---

## Q049: DataAnnotations vs Domain Rules

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Validation |
| **Frequency** | Common |

### Question

What validation belongs on DTOs vs in the domain layer?

### Short Answer (30 seconds)

DTO: format, length, required fields. Domain: invariants like 'order cannot exceed credit limit' requiring business context.

### Detailed Answer (3–5 minutes)

**DTO:** `[Required]`, `[EmailAddress]`, max length.

**Domain:**
```csharp
if (order.Total > customer.CreditLimit)
  throw new DomainException("Credit exceeded");
```

**Architect:** Duplicate format checks nowhere — domain doesn't validate email regex unless identity aggregate.

### Architecture Perspective

Validation layering prevents anemic domain and fat DTOs.

### Follow-up Questions

1. **IValidatableObject? — Cross-field DTO rules OK at boundary.**
2. **ValidationBehavior in MediatR? — Central pipeline before handler.**

### Common Mistakes in Interviews

- All validation in attributes only
- Domain entity with DataAnnotations
- Credit rules in controller

---

## Q050: Polly Retry Basics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Resilience |
| **Frequency** | Very Common |

### Question

When is HTTP retry with Polly appropriate?

### Short Answer (30 seconds)

Retry transient failures — 408, 429, 5xx — with backoff and max attempts on idempotent operations or with idempotency keys.

### Detailed Answer (3–5 minutes)

```csharp
Policy.Handle<HttpRequestException>()
  .OrResult(r => (int)r.StatusCode >= 500)
  .WaitAndRetryAsync(3, i => TimeSpan.FromSeconds(Math.Pow(2, i)));
```

**Never blind retry:** POST payment without dedup key.

**Architect:** Wrap retry outside circuit breaker; timeout innermost.

### Architecture Perspective

Polly interview tests idempotency awareness.

### Follow-up Questions

1. **Jitter? — Prevents thundering herd on recovery.**
2. **429 handling? — Respect Retry-After header.**

### Common Mistakes in Interviews

- Retry non-idempotent POST unlimited
- No jitter on exponential backoff
- Retry nested across every service layer

---

## Q051: Polly Circuit Breaker

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Resilience |
| **Frequency** | Common |

### Question

What does a Polly circuit breaker protect against?

### Short Answer (30 seconds)

After sustained failures, fail fast instead of hammering sick downstream — gives service time to recover.

### Detailed Answer (3–5 minutes)

**States:** Closed (normal) → Open (reject calls) → Half-open (test probe).

**Configure:** Failure threshold, break duration, on-break/on-reset callbacks for metrics.

**Architect:** Circuit breaker on external payment API — fallback to queued retry or graceful degradation message.

### Architecture Perspective

Circuit breaker is bulkhead pattern for dependency failures.

### Follow-up Questions

1. **Half-open probe? — Single trial request tests recovery.**
2. **Combine with retry? — Retry transient inside breaker-wrapped call carefully.**

### Common Mistakes in Interviews

- No circuit breaker on critical external deps
- Breaker never half-opens — stuck open forever
- Breaker without metrics/alerts

---

## Q052: Cache-Aside Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Caching |
| **Frequency** | Very Common |

### Question

Explain cache-aside pattern for a .NET product catalog API.

### Short Answer (30 seconds)

App checks Redis first; on miss loads SQL, populates cache with TTL, returns. On write, update DB then invalidate cache key.

### Detailed Answer (3–5 minutes)

```csharp
var cached = await _cache.GetAsync<Product>(key);
if (cached != null) return cached;
var product = await _db.Products.FindAsync(id);
await _cache.SetAsync(key, product, TimeSpan.FromMinutes(10));
```

**Risks:** Stampede on expiry — use lock or HybridCache.

**Architect:** TTL + explicit invalidation on update — never infinite cache.

### Architecture Perspective

Cache-aside is default distributed caching pattern.

### Follow-up Questions

1. **IDistributedCache? — Redis backing in .NET.**
2. **Stampede mitigation? — Mutex per key or stale-while-revalidate.**

### Common Mistakes in Interviews

- Cache with no TTL
- Update DB without invalidating cache
- Cache personalized data without key scoping

---

## Q053: IMemoryCache vs Redis

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Caching |
| **Frequency** | Common |

### Question

When use IMemoryCache vs IDistributedCache (Redis)?

### Short Answer (30 seconds)

IMemoryCache for single-instance L1 hot data. Redis for multi-instance shared cache and pub/sub invalidation.

### Detailed Answer (3–5 minutes)

**L1 + L2:** Local memory for microseconds; Redis for cross-pod consistency.

**.NET 9 HybridCache:** Built-in L1+L2.

**Architect:** Single App Service instance can use memory only; AKS with 10 pods needs distributed.

### Architecture Perspective

Cache tier choice follows deployment topology.

### Follow-up Questions

1. **Memory cache eviction? — Size limits and compaction policies.**
2. **Redis connection multiplexer? — Singleton — one per app.**

### Common Mistakes in Interviews

- IMemoryCache on multi-instance expecting consistency
- Redis for tiny single-server app unnecessarily
- No cache key namespace per tenant

---

## Q054: Factory Pattern DI

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Design Patterns |
| **Frequency** | Common |

### Question

When use a factory with DI instead of direct service resolution?

### Short Answer (30 seconds)

When creation depends on runtime input — tenant-specific provider, file type parser, or notification channel selected per request.

### Detailed Answer (3–5 minutes)

```csharp
public interface INotificationFactory {
  INotifier Create(NotificationChannel channel);
}
```

**Prefer keyed services (.NET 8)** when types known at compile time.

**Architect:** Factory for plugin and multi-tenant provider selection — not for every `new`.

### Architecture Perspective

Factory connects patterns to DI registration modules.

### Follow-up Questions

1. **Abstract factory vs factory method? — Family of products vs one product.**
2. **Service locator smell? — Factory interface injected — not static resolver.**

### Common Mistakes in Interviews

- Factory for every object creation
- new() in business logic bypassing DI
- Static factory with hidden dependencies

---

## Q055: Strategy Pattern DI

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Design Patterns |
| **Frequency** | Common |

### Question

Implement Strategy pattern for shipping calculation in .NET.

### Short Answer (30 seconds)

Define `IShippingStrategy` implementations; select via keyed DI or factory based on customer tier or shipping method.

### Detailed Answer (3–5 minutes)

```csharp
public interface IShippingStrategy {
  decimal Calculate(Order order);
}
// StandardShipping, ExpressShipping registered keyed
```

**vs if/else:** Open for new carriers without editing `CheckoutService`.

**Architect:** Strategy key in config/DB — ops can switch without deploy.

### Architecture Perspective

Strategy maps to business variability — runtime selection story.

### Follow-up Questions

1. **Rules engine alternative? — Complex tax/discount rules — external engine.**
2. **Default strategy? — Always provide fallback for unknown key.**

### Common Mistakes in Interviews

- switch on string for every new carrier
- Strategy with static global mutable state
- No unit tests per strategy implementation

---

## Q056: Observer Domain Events

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Design Patterns |
| **Frequency** | Common |

### Question

How handle domain events in-process vs across microservices?

### Short Answer (30 seconds)

In-process: MediatR `INotification` after SaveChanges. Cross-service: outbox table → message bus — not C# static events.

### Detailed Answer (3–5 minutes)

**In-process:**
```csharp
await _mediator.Publish(new OrderPlaced(order.Id));
```

**Distributed:** Transactional outbox → Service Bus topic.

**Architect:** Don't use static events in web apps — scoped lifetime issues.

### Architecture Perspective

Observer scope boundary — in-proc vs distributed — is the architect distinction.

### Follow-up Questions

1. **Event vs command? — Past tense, multiple subscribers vs single handler.**
2. **Ordering? — In-proc ordered; bus may need partition keys.**

### Common Mistakes in Interviews

- Static C# events in ASP.NET
- Synchronous handler doing HTTP in same request
- Dual-write DB and bus without outbox

---

## Q057: Decorator with Scrutor

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Design Patterns |
| **Frequency** | Common |

### Question

Use Decorator pattern to add caching to a repository in .NET.

### Short Answer (30 seconds)

Wrap `IOrderRepository` with `CachingOrderRepository` using Scrutor `Decorate` — adds behavior without subclassing.

### Detailed Answer (3–5 minutes)

```csharp
services.AddScoped<IOrderRepository, SqlOrderRepository>();
services.Decorate<IOrderRepository, CachingOrderRepository>();
```

**Also:** `DelegatingHandler` for HttpClient logging/retry.

**Architect:** Cross-cutting concerns as decorators — limit stack depth for debuggability.

### Architecture Perspective

Decorator is structural pattern behind HttpClient handlers.

### Follow-up Questions

1. **Decorator order? — Cache outside or inside logging — document.**
2. **Manual decorator vs Scrutor? — Scrutor reduces registration boilerplate.**

### Common Mistakes in Interviews

- Subclass explosion instead of wrap
- Decorator changing interface contract
- Five decorators deep with no docs

---

## Q058: Unit Test Mocking

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Testing |
| **Frequency** | Very Common |

### Question

What should you mock in unit tests vs use real implementations?

### Short Answer (30 seconds)

Mock external boundaries — DB, HTTP, message bus, clock. Use real domain logic and value objects — don't mock what you don't own.

### Detailed Answer (3–5 minutes)

**Mock:** `IOrderRepository`, `IPaymentGateway`, `IDateTimeProvider`.

**Real:** Domain entities, validators, pure functions.

**Architect:** Over-mocking tests implementation not behavior — prefer testing outcomes.

### Architecture Perspective

Mocking discipline separates useful unit tests from brittle ones.

### Follow-up Questions

1. **Moq vs NSubstitute? — Team standard — either works.**
2. **Mock DbContext? — Often integration test territory — mock repo interface instead.**

### Common Mistakes in Interviews

- Mock every dependency including domain
- No tests on business rules
- Mock verifying internal call order only

---

## Q059: Integration Test WebApplicationFactory

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Testing |
| **Frequency** | Very Common |

### Question

How write integration tests for ASP.NET Core APIs?

### Short Answer (30 seconds)

Use `WebApplicationFactory` with test database (Testcontainers or local), exercise HTTP endpoints, assert status and payload.

### Detailed Answer (3–5 minutes)

```csharp
public class OrdersApiTests : IClassFixture<WebApplicationFactory<Program>> {
  [Fact]
  public async Task Create_Returns201() {
    var response = await _client.PostAsJsonAsync("/orders", dto);
    response.StatusCode.Should().Be(HttpStatusCode.Created);
  }
}
```

**Architect:** Integration tests for auth, validation, and persistence — unit tests for domain rules.

### Architecture Perspective

Integration tests catch DI and middleware wiring bugs.

### Follow-up Questions

1. **Testcontainers? — Real Postgres in CI — higher confidence.**
2. **Custom WebApplicationFactory? — Override config and swap services.**

### Common Mistakes in Interviews

- Only unit tests — no HTTP pipeline coverage
- Shared prod database for tests
- No cleanup between test runs

---

## Q060: Test Pyramid for APIs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Testing |
| **Frequency** | Common |

### Question

Describe the test pyramid for a .NET microservice team.

### Short Answer (30 seconds)

Many fast unit tests, fewer integration tests, few E2E smoke tests. Contract tests between services at API boundary.

### Detailed Answer (3–5 minutes)

**Layers:**
- **Unit:** Domain, handlers, validators — milliseconds
- **Integration:** API + DB — seconds
- **E2E:** Critical user journeys — minutes
- **Contract:** Pact between consumer/provider

**Architect:** CI gates — unit on every commit, integration on PR, E2E nightly.

### Architecture Perspective

Test pyramid prevents slow flaky CI.

### Follow-up Questions

1. **Snapshot testing? — OpenAPI response snapshots — catch contract drift.**
2. **Load tests? — Separate pipeline — not in unit suite.**

### Common Mistakes in Interviews

- E2E only — slow feedback
- No contract tests between microservices
- Skipping integration because Testcontainers 'hard'

---

## Q061: IHttpClientFactory Why

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | HTTP |
| **Frequency** | Very Common |

### Question

Why use IHttpClientFactory instead of new HttpClient()?

### Short Answer (30 seconds)

Avoids socket exhaustion from disposing clients per request and DNS staleness from singleton HttpClient — pooled handlers with configurable lifetime.

### Detailed Answer (3–5 minutes)

**Problems:**
- `using var client = new HttpClient()` — SNAT port exhaustion
- Static HttpClient — DNS never refreshes

**Fix:** Typed/named clients with `PooledConnectionLifetime` of 2–5 minutes.

**Architect:** Coding standard — never raw HttpClient in production services.

### Architecture Perspective

Classic .NET production footgun — expected senior answer.

### Follow-up Questions

1. **Typed client? — Interface wraps HttpClient with base address.**
2. **Named client? — Multiple configs for different APIs.**

### Common Mistakes in Interviews

- new HttpClient() per request
- Static HttpClient forever
- Ignoring Azure SNAT limits

---

## Q062: HttpClient Polly Integration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | HTTP |
| **Frequency** | Common |

### Question

How add Polly policies to HttpClient in .NET?

### Short Answer (30 seconds)

Use `AddHttpClient<T>().AddPolicyHandler()` or `AddStandardResilienceHandler()` (.NET 8+) for retry, timeout, circuit breaker.

### Detailed Answer (3–5 minutes)

```csharp
services.AddHttpClient<IPaymentClient, PaymentClient>()
  .AddPolicyHandler(GetRetryPolicy())
  .AddPolicyHandler(GetCircuitBreakerPolicy());
```

**Order:** Retry outside circuit breaker; timeout innermost.

**Architect:** Standard resilience package per platform — teams don't hand-roll per service.

### Architecture Perspective

HttpClient + Polly is standard outbound resilience stack.

### Follow-up Questions

1. **Standard resilience handler? — .NET 8 built-in — prefer over custom.**
2. **DelegatingHandler chain? — Logging handler outermost.**

### Common Mistakes in Interviews

- Polly policy per request new HttpClient
- Infinite retry on 500
- No timeout policy

---

## Q063: API Versioning URL

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | API Design |
| **Frequency** | Common |

### Question

How version REST APIs — URL path vs header?

### Short Answer (30 seconds)

URL `/v1/orders` most visible and cache-friendly. Header `Api-Version` or media type for clients wanting stable URL. Pick one org standard.

### Detailed Answer (3–5 minutes)

**ASP.NET:** `Asp.Versioning` supports URL, header, query.

**Breaking change:** New major version — deprecate old with sunset header.

**Architect:** Document breaking change policy — additive changes only in same version.

### Architecture Perspective

Versioning strategy is long-term API evolution.

### Follow-up Questions

1. **Deprecation headers? — Sunset and Link — give clients migration time.**
2. **Parallel versions how long? — Typically 6–12 months enterprise.**

### Common Mistakes in Interviews

- Breaking change in same /v1 without notice
- Three versioning schemes mixed
- No deprecation communication

---

## Q064: API Versioning Minimal APIs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | API Design |
| **Frequency** | Common |

### Question

How apply API versioning to Minimal APIs in .NET?

### Short Answer (30 seconds)

Use `Asp.Versioning.Http` with `MapGroup` per version or `HasApiVersion` on endpoints; generate separate OpenAPI docs per version.

### Detailed Answer (3–5 minutes)

```csharp
var v1 = app.MapGroup("/v1/orders").HasApiVersion(1.0);
var v2 = app.MapGroup("/v2/orders").HasApiVersion(2.0);
```

**Architect:** Shared handlers where logic identical — different DTO mapping per version.

### Architecture Perspective

Minimal API versioning mirrors controller attribute approach.

### Follow-up Questions

1. **OpenAPI per version? — Swashbuckle/NSwag multi-document.**
2. **Internal vs public versioning? — Internal can move faster.**

### Common Mistakes in Interviews

- Duplicate all logic per version
- Version only in docs not routing
- Remove v1 without client migration plan

---

## Q065: Global Exception Handler

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | ASP.NET Core |
| **Frequency** | Very Common |

### Question

Implement global exception handling returning ProblemDetails.

### Short Answer (30 seconds)

Use exception middleware or `IExceptionHandler` (.NET 8+) mapping domain exceptions to 400/404/409 and logging 500 with correlation ID.

### Detailed Answer (3–5 minutes)

```csharp
app.UseExceptionHandler(handler => handler.Run(async ctx => {
  var ex = ctx.Features.Get<IExceptionHandlerFeature>()?.Error;
  // map to ProblemDetails status
}));
```

**Never:** Stack traces to clients in production.

**Architect:** Exception taxonomy per bounded context.

### Architecture Perspective

Global handler is production hygiene — consistent errors.

### Follow-up Questions

1. **IExceptionHandler .NET 8? — Multiple handlers — chain of responsibility.**
2. **Result pattern? — Expected failures as Result not exceptions.**

### Common Mistakes in Interviews

- try/catch in every controller
- Stack trace in mobile API response
- Swallowing exceptions silently

---

## Q066: Domain Exception Mapping

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | ASP.NET Core |
| **Frequency** | Common |

### Question

How map domain exceptions to HTTP status codes?

### Short Answer (30 seconds)

NotFoundException → 404, ValidationException → 400, ConflictException → 409, unauthorized domain rule → 403. Unknown → 500 logged.

### Detailed Answer (3–5 minutes)

**Handler switch:**
```csharp
var (status, title) = ex switch {
  NotFoundException => (404, "Not Found"),
  DomainValidationException => (400, ex.Message),
  _ => (500, "Internal Server Error")
};
```

**Architect:** Business rule violations are 400/409 — not 500.

### Architecture Perspective

Correct status codes improve client and monitoring signal.

### Follow-up Questions

1. **ProblemDetails extensions? — Add error codes for client handling.**
2. **Exception as flow control for expected paths? — Prefer Result type.**

### Common Mistakes in Interviews

- Everything returns 500
- 404 for validation errors
- Leaking internal exception messages

---

## Q067: MediatR Command Handler

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | MediatR |
| **Frequency** | Very Common |

### Question

How structure a MediatR command handler in clean architecture?

### Short Answer (30 seconds)

Command record + handler in application layer; controller sends command; handler orchestrates domain and infrastructure.

### Detailed Answer (3–5 minutes)

```csharp
public record CreateOrderCommand(CreateOrderDto Dto) : IRequest<OrderDto>;

public class Handler(IOrderRepository repo) : IRequestHandler<CreateOrderCommand, OrderDto> {
  public async Task<OrderDto> Handle(...) { /* use case */ }
}
```

**Controller:** One line `await _mediator.Send(command)`.

### Architecture Perspective

MediatR enables thin controllers and pipeline behaviors.

### Follow-up Questions

1. **Pipeline behaviors? — Validation, logging, transactions wrap handlers.**
2. **Notifications? — Domain events in-process.**

### Common Mistakes in Interviews

- Fat controller with business logic
- MediatR in domain layer
- Handler calling DbContext directly from controller

---

## Q068: MediatR Pipeline Behaviors

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | MediatR |
| **Frequency** | Common |

### Question

What cross-cutting concerns belong in MediatR pipeline behaviors?

### Short Answer (30 seconds)

Validation, logging, performance timing, transaction wrapping, and authorization checks before handler executes.

### Detailed Answer (3–5 minutes)

```csharp
public class ValidationBehavior<TReq,TRes>(IEnumerable<IValidator<TReq>> validators)
  : IPipelineBehavior<TReq,TRes> { /* validate before next */ }
```

**Order:** Logging → Validation → Transaction → Handler.

**Architect:** Behaviors replace attribute soup on controllers.

### Architecture Perspective

Pipeline behaviors centralize cross-cutting in application layer.

### Follow-up Questions

1. **OpenBehavior generic constraints? — Register once for all requests.**
2. **Too many behaviors? — Keep focused — don't hide business logic.**

### Common Mistakes in Interviews

- Duplicate validation in behavior and controller
- Transaction behavior on queries accidentally
- Behavior order undocumented

---

## Q069: Repository When to Use

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Data Access |
| **Frequency** | Very Common |

### Question

When is repository pattern justified in EF Core projects?

### Short Answer (30 seconds)

When you need test seam, aggregate persistence, multiple backing stores, or explicit domain mapping — not as pass-through CRUD wrapper.

### Detailed Answer (3–5 minutes)

**Good use:**
- Aggregate root `Order` with items — single repository method `Save(Order aggregate)`
- SQL + Elasticsearch dual write abstraction

**Skip:** Generic `IRepository<T>` with GetAll on every entity — EF DbContext already is repository.

### Architecture Perspective

Senior answer: repository is a seam, not mandatory layer.

### Follow-up Questions

1. **Specification pattern? — Composable query specs for complex filters.**
2. **CQRS read side? — Queries may bypass repository to projections.**

### Common Mistakes in Interviews

- Mandatory IRepository<T> everywhere
- Repository returning IQueryable to API
- Pass-through CRUD with no added value

---

## Q070: Repository vs DbContext

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Data Access |
| **Frequency** | Common |

### Question

Should application services use DbContext directly or IOrderRepository?

### Short Answer (30 seconds)

Simple read-heavy apps may use DbContext in infrastructure query handlers. Domain-centric apps use repository interface at aggregate boundary.

### Detailed Answer (3–5 minutes)

**DbContext direct:** CQRS read models, reports, admin queries.

**Repository:** Write model aggregate persistence, swap storage, strict unit test boundary.

**Architect:** Consistent rule per bounded context — document in ADR.

### Architecture Perspective

Pragmatism over pattern dogma — justify boundary.

### Follow-up Questions

1. **DbContext in application layer? — Anti-pattern — leaks EF to domain.**
2. **Unit of Work? — DbContext is UoW — explicit wrapper optional.**

### Common Mistakes in Interviews

- Repository wrapping every DbSet blindly
- DbContext in domain project
- Mixed approach with no team guideline

---
