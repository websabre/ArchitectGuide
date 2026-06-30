# Week 01 — Intermediate Q&A

> Q031–Q070: Premium format (Week 1 quality).

---


## Q031: Interface vs Abstract Class

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | C# OOP |
| **Frequency** | Very Common |

### Question

When choose interface over abstract class in enterprise .NET?

### Short Answer (30 seconds)

Interface: multiple inheritance, behavior contract without implementation. Abstract class: shared base state/implementation, single inheritance.

### Detailed Answer (3–5 minutes)

**Interface:** `IPaymentGateway`, `IRepository<T>` — swap implementations, test doubles, plugin architecture.

**Abstract class:** shared template method, common fields, protected helpers — `EntityBase` with Id and audit.

**Architect rule:** Default to interface for DI dependencies; abstract class when genuine shared implementation exists — not as a dumping ground for duplicate code.

```csharp
public interface IOrderNotifier { Task NotifyAsync(Order order); }
public abstract class EntityBase { public Guid Id { get; protected set; } }
```

### Architecture Perspective

Contract design drives testability and team boundaries.

### Follow-up Questions

1. **Default interface methods C# 8? — Use sparingly — breaks binary compatibility if changed.**
2. **Sealed abstract class? — Prevent further inheritance when hierarchy complete.**

### Common Mistakes in Interviews

- Abstract class for every service
- Fat interface with 15 unrelated methods
- Interface on concrete class already — redundant abstraction

---

## Q032: Composition over Inheritance

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Design Principles |
| **Frequency** | Very Common |

### Question

Explain composition over inheritance with ASP.NET Core example.

### Short Answer (30 seconds)

Favor has-a over is-a — inject behaviors (`IValidator`, `ICache`) instead of deep inheritance trees.

### Detailed Answer (3–5 minutes)

**Bad:** `PremiumOrderService : BaseOrderService : OrderService` — fragile base class, hidden coupling.

**Good:**
```csharp
public class OrderService(IValidator<Order> validator, IOrderRepository repo, IEventPublisher events)
```

**Architect:** Decorator pattern (`CachingOrderRepository` wraps `OrderRepository`) over subclassing. Inheritance for true subtype polymorphism only — domain entities, strategy hierarchies with shared algorithm skeleton.

### Architecture Perspective

Composition aligns with DI and microservice boundaries.

### Follow-up Questions

1. **When is inheritance OK? — Framework hooks (Controller base), domain taxonomy with invariants.**
2. **Mixin via extension methods vs inheritance? — Extensions for stateless helpers only.**

### Common Mistakes in Interviews

- Five-level service inheritance chain
- Override base method breaks LSP silently
- Composition replaced by service locator

---

## Q033: DI Lifetimes — Singleton, Scoped, Transient

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DI |
| **Frequency** | Very Common |

### Question

Explain singleton, scoped, and transient lifetimes. Common pitfalls?

### Short Answer (30 seconds)

Singleton: one per app — config, caches. Scoped: one per request — DbContext, user context. Transient: new each resolve — lightweight stateless services.

### Detailed Answer (3–5 minutes)

**Captive dependency:** Singleton holding Scoped service — stale DbContext, memory leak, wrong tenant data.

```csharp
// WRONG: singleton injecting scoped DbContext
services.AddSingleton<BadService>(); // if ctor takes DbContext
```

**Architect:** Lifetime validation at startup (`ValidateOnBuild`). Document lifetime rules in platform template. BackgroundService gets its own scope per iteration.

### Architecture Perspective

Lifetime bugs are subtle production data-corruption causes.

### Follow-up Questions

1. **DbContext singleton? — Never — always scoped or factory per operation.**
2. **IServiceScopeFactory in singleton? — Create scope manually for background work.**

### Common Mistakes in Interviews

- Singleton captures scoped DbContext
- Transient DbContext per call — connection storm
- No ValidateOnBuild in production templates

---

## Q034: Options Pattern — IOptions

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Configuration |
| **Frequency** | Very Common |

### Question

How use IOptions, IOptionsSnapshot, and IOptionsMonitor?

### Short Answer (30 seconds)

`IOptions<T>`: singleton, bound at startup — immutable. `IOptionsSnapshot<T>`: scoped, reloads per request. `IOptionsMonitor<T>`: singleton with change callbacks — hot reload.

### Detailed Answer (3–5 minutes)

```csharp
services.Configure<PaymentOptions>(config.GetSection("Payment"));
public class PaymentService(IOptions<PaymentOptions> opts) { }
```

**Architect:** Strongly typed options classes with validation (`IValidateOptions<T>`, DataAnnotations). Never inject `IConfiguration` into business services — hides config surface.

**Secrets:** bind from Key Vault; options class holds structure, not raw secrets in appsettings.json.

### Architecture Perspective

Options pattern is the config contract for services.

### Follow-up Questions

1. **Named options? — Multiple registrations same type — `IOptionsSnapshot<AuthOptions>` with name.**
2. **PostConfigure? — Layer defaults then environment overrides.**

### Common Mistakes in Interviews

- IConfiguration injected everywhere
- IOptions for values that change per request without Snapshot
- No validation on critical options at startup

---

## Q035: Hosted Services and BackgroundService

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | ASP.NET Core |
| **Frequency** | Common |

### Question

When use BackgroundService vs Hangfire/queue for background work?

### Short Answer (30 seconds)

BackgroundService: in-process, host-lifetime tied, simple periodic or long-running tasks. Queue/Hangfire: durable, retriable, scale-out workers.

### Detailed Answer (3–5 minutes)

```csharp
public class OutboxProcessor(IServiceScopeFactory scopeFactory) : BackgroundService
{
    protected override async Task ExecuteAsync(CancellationToken ct)
    {
        while (!ct.IsCancellationRequested)
        {
            using var scope = scopeFactory.CreateScope();
            // process outbox
            await Task.Delay(TimeSpan.FromSeconds(5), ct);
        }
    }
}
```

**Architect:** BackgroundService for lightweight polling (outbox drain). Never heavy job processing on web tier — use dedicated worker + queue. Honor `IHostApplicationLifetime` shutdown token.

### Architecture Perspective

Background work placement affects reliability and scale.

### Follow-up Questions

1. **IHostedService vs BackgroundService? — BackgroundService abstracts ExecuteAsync loop.**
2. **Graceful shutdown timeout? — Configure `HostOptions.ShutdownTimeout`.**

### Common Mistakes in Interviews

- Long CPU work on web pod BackgroundService
- No scope in background loop — captive DbContext
- Ignore cancellation on shutdown

---

## Q036: Middleware Pipeline Ordering

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | ASP.NET Core |
| **Frequency** | Very Common |

### Question

Why does middleware order matter? Show critical ordering rules.

### Short Answer (30 seconds)

Middleware runs as onion — first registered runs first on request, last on response. Wrong order breaks auth, routing, exception handling.

### Detailed Answer (3–5 minutes)

**Correct order (simplified):**
1. Exception handler (early)
2. HTTPS redirection
3. Static files
4. Routing
5. CORS (before auth if needed)
6. Authentication
7. Authorization
8. Endpoints

**Architect:** Document standard pipeline in platform template. `UseAuthentication` before `UseAuthorization`. Endpoint middleware after routing.

### Architecture Perspective

Pipeline order bugs manifest as 401 on valid tokens or CORS failures.

### Follow-up Questions

1. **Terminal middleware? — Short-circuits pipeline — no next() call.**
2. **Branching pipeline MapWhen? — Path-specific middleware — order still matters per branch.**

### Common Mistakes in Interviews

- CORS after authorization
- Exception handler after endpoints
- Custom middleware before routing reads route data

---

## Q037: Action Filters vs Middleware

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | ASP.NET Core |
| **Frequency** | Common |

### Question

When use action filters vs middleware?

### Short Answer (30 seconds)

Middleware: all requests, transport-level, no MVC knowledge. Action filters: MVC pipeline, per-controller/action, model binding aware.

### Detailed Answer (3–5 minutes)

**Middleware:** correlation ID, global exception wrapper, request logging.

**Action filters:** `[Authorize]`-style custom rules, model validation short-circuit, per-action timing, audit logging with action name.

**Architect:** Cross-cutting HTTP concerns → middleware. MVC-specific behavior (action arguments, IActionResult) → filters. Avoid duplicate logic in both.

### Architecture Perspective

Right layer reduces coupling to MVC.

### Follow-up Questions

1. **IAsyncActionFilter vs middleware perf? — Filters skip non-MVC endpoints — minimal APIs need middleware or endpoint filters.**
2. **Endpoint filters .NET 7+? — Minimal API equivalent of action filters.**

### Common Mistakes in Interviews

- Duplicate auth in middleware and filter
- Action filter for static file requests
- Middleware tries to read action parameters

---

## Q038: Minimal APIs vs Controllers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | ASP.NET Core |
| **Frequency** | Common |

### Question

When choose Minimal APIs over controllers?

### Short Answer (30 seconds)

Minimal APIs: small microservices, simple CRUD, low ceremony. Controllers: complex routing, filters, versioning, large teams needing convention.

### Detailed Answer (3–5 minutes)

**Minimal API strengths:**
```csharp
app.MapGet("/orders/{id}", async (Guid id, IOrderService svc) =>
    await svc.GetAsync(id));
```

**Controller strengths:** `[ApiController]` automatic 400, filter ecosystem, clear folder structure for 200+ endpoints.

**Architect:** Microservice with 10 endpoints → Minimal API. Bounded context with rich validation, versioning, multiple content types → Controllers. Can mix in same app.

### Architecture Perspective

API style is team-scale and complexity decision.

### Follow-up Questions

1. **Minimal API validation? — `AddEndpointsApiExplorer`, FluentValidation filter, or `Results.ValidationProblem`.**
2. **OpenAPI both styles? — Swashbuckle supports both — same doc standard.**

### Common Mistakes in Interviews

- Controllers for 5-endpoint internal tool
- Minimal APIs without versioning plan at 50 endpoints
- No separation — business logic inline in MapGet lambdas

---

## Q039: IHttpClientFactory Rationale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | HTTP |
| **Frequency** | Very Common |

### Question

Why architect mandates IHttpClientFactory over new HttpClient()?

### Short Answer (30 seconds)

Factory manages `HttpMessageHandler` lifetime — prevents socket exhaustion and stale DNS from misused HttpClient patterns.

### Detailed Answer (3–5 minutes)

**Problems solved:**
- `new HttpClient()` per request → socket port exhaustion
- Singleton HttpClient → DNS never refreshes

```csharp
services.AddHttpClient<IInventoryClient, InventoryClient>(c =>
{
    c.BaseAddress = new Uri(config["Inventory:BaseUrl"]);
    c.Timeout = TimeSpan.FromSeconds(30);
});
```

**Architect:** Typed clients as standard. Centralize Polly handlers, default headers, resilience. Ban raw `new HttpClient()` via analyzer.

### Architecture Perspective

HttpClient misuse causes classic scale outages.

### Follow-up Questions

1. **SocketsHttpHandler.PooledConnectionLifetime? — Rotate connections — default 2 min in factory.**
2. **DelegatingHandler chain? — Auth token injection, correlation ID propagation.**

### Common Mistakes in Interviews

- new HttpClient() in repository
- Singleton HttpClient for all outbound calls forever
- No timeout configured on outbound clients

---

## Q040: Polly Resilience Policies

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Resilience |
| **Frequency** | Common |

### Question

Design resilience pipeline for external payment API calls.

### Short Answer (30 seconds)

Combine retry (transient failures), circuit breaker (cascade prevention), timeout (bounded wait), optional bulkhead (concurrency limit).

### Detailed Answer (3–5 minutes)

**Order matters:** timeout wraps retry or vice versa — document team standard.

```csharp
services.AddHttpClient<IPaymentGateway>()
    .AddStandardResilienceHandler(); // .NET 8+
```

**Architect:** Retry only idempotent ops or with idempotency keys. Circuit breaker open → fail fast, shed load. Per-dependency policies — not one global retry for everything. Log breaker state changes.

### Architecture Perspective

Resilience policies are dependency contracts.

### Follow-up Questions

1. **Jitter on retry? — Prevents thundering herd when dependency recovers.**
2. **Hedging vs retry? — Parallel duplicate requests — rare, costly — architect approval.**

### Common Mistakes in Interviews

- Infinite retry on POST without idempotency key
- Circuit breaker never configured half-open
- Same 5 retries for read and write endpoints

---

## Q041: Structured Logging with Serilog

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Observability |
| **Frequency** | Very Common |

### Question

Serilog structured logging standards for ASP.NET Core microservices?

### Short Answer (30 seconds)

Message templates with named properties — `{OrderId}` not string interpolation — enables query and alerting.

### Detailed Answer (3–5 minutes)

```csharp
Log.Information("Order {OrderId} shipped to {Region}", order.Id, region);
// NOT: Log.Information($"Order {order.Id} shipped");
```

**Architect mandates:** JSON to stdout in containers, `CorrelationId` enricher from middleware, log level overrides per namespace, PII redaction destructuring. Sinks: Console (K8s), Application Insights, Seq dev.

**Request logging:** `UseSerilogRequestLogging` with level based on status code.

### Architecture Perspective

Structured logs are searchable production signals.

### Follow-up Questions

1. **LogContext.PushProperty? — Scope OrderId for entire request handler.**
2. **Serilog.Exceptions? — Structured exception details without stack string concat.**

### Common Mistakes in Interviews

- String interpolation in log messages
- Debug logging enabled in production always
- Logging credit card numbers or JWT tokens

---

## Q042: Health Checks — Liveness vs Readiness

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | ASP.NET Core |
| **Frequency** | Very Common |

### Question

Difference between liveness and readiness probes in ASP.NET Core?

### Short Answer (30 seconds)

Liveness: is process alive? — fail → restart pod. Readiness: can accept traffic? — fail → remove from load balancer.

### Detailed Answer (3–5 minutes)

```csharp
services.AddHealthChecks()
    .AddCheck("self", () => HealthCheckResult.Healthy())
    .AddSqlServer(connString, name: "sql")
    .AddRedis(redisConn);

app.MapHealthChecks("/health/live", new() { Predicate = _ => false }); // or dedicated
app.MapHealthChecks("/health/ready", new() { Predicate = check => check.Tags.Contains("ready") });
```

**Architect:** Liveness lightweight — don't check SQL (restart loop risk). Readiness checks DB, Redis, downstream dependency. Tag checks appropriately.

### Architecture Perspective

Probe design prevents cascading restarts and bad traffic routing.

### Follow-up Questions

1. **Startup probe? — Slow-starting apps — K8s waits before liveness kills.**
2. **Health check UI package? — Dev only — never expose detailed deps publicly.**

### Common Mistakes in Interviews

- SQL check on liveness — DB blip restarts all pods
- Readiness always healthy — traffic to broken instances
- Detailed health JSON public in production

---

## Q043: API Versioning Strategies

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | API Design |
| **Frequency** | Common |

### Question

Compare URL, header, and query string API versioning.

### Short Answer (30 seconds)

URL (`/v2/orders`): explicit, cache-friendly, visible. Header (`Api-Version`): clean URLs, harder to test in browser. Query (`?api-version=2.0`): easy override, messy caching.

### Detailed Answer (3–5 minutes)

**Architect recommendation:** URL path or header with `Asp.Versioning` package — deprecate with sunset headers.

```csharp
services.AddApiVersioning(o => o.DefaultApiVersion = new(1, 0));
```

**Policy:** Support N and N-1 versions. Document breaking vs additive changes. OpenAPI one doc per version or aggregated.

### Architecture Perspective

Versioning strategy affects clients, gateways, and caching.

### Follow-up Questions

1. **Media type versioning? — `application/vnd.company.orders.v2+json` — content negotiation coupling.**
2. **Version in route constraint? — `MapToApiVersion` on minimal APIs and controllers.**

### Common Mistakes in Interviews

- Breaking change without version bump
- Three versioning schemes mixed in one API
- No deprecation timeline communicated to consumers

---

## Q044: Problem Details — RFC 7807

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | API Design |
| **Frequency** | Common |

### Question

How implement RFC 7807 Problem Details in ASP.NET Core?

### Short Answer (30 seconds)

`ProblemDetails` standard error body: `type`, `title`, `status`, `detail`, `instance` — machine-readable, consistent across services.

### Detailed Answer (3–5 minutes)

```csharp
services.AddProblemDetails();
// or custom
return Results.Problem(
    title: "Order not found",
    statusCode: StatusCodes.Status404NotFound,
    type: "https://api.example.com/errors/order-not-found",
    detail: $"Order {id} does not exist.");
```

**Architect:** Global exception handler maps domain exceptions to ProblemDetails. Stable `type` URIs per error code — not stack traces in `detail`. Extensions for `traceId`, `errors` validation array.

### Architecture Perspective

Consistent errors reduce client integration cost.

### Follow-up Questions

1. **ValidationProblemDetails? — 400 with field-level errors array.**
2. **ProblemDetails in non-API contexts? — gRPC status, SignalR hub errors — parallel standards.**

### Common Mistakes in Interviews

- Stack trace in detail field production
- Different error shape per endpoint
- Generic 500 with no correlation id

---

## Q045: FluentValidation Integration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Validation |
| **Frequency** | Common |

### Question

Integrate FluentValidation in ASP.NET Core pipeline?

### Short Answer (30 seconds)

Register validators from assembly; auto-validate on model binding via filter or `AddFluentValidationAutoValidation`.

### Detailed Answer (3–5 minutes)

```csharp
services.AddValidatorsFromAssemblyContaining<CreateOrderValidator>();

public class CreateOrderValidator : AbstractValidator<CreateOrderCommand>
{
    public CreateOrderValidator() {
        RuleFor(x => x.Email).EmailAddress();
        RuleFor(x => x.Lines).NotEmpty();
    }
}
```

**Architect:** Validators for commands/DTOs — not entities with DB calls (use async validator sparingly). Separate from domain invariants — FluentValidation at boundary, domain rules inside aggregate.

### Architecture Perspective

Validation layer placement is architectural boundary.

### Follow-up Questions

1. **Async validation RuleForAsync? — DB uniqueness check — acceptable at API boundary.**
2. **MediatR ValidationBehavior? — Pipeline validates before handler — clean CQRS.**

### Common Mistakes in Interviews

- Validation logic duplicated in controller and domain
- Heavy DB calls in every RuleFor
- No localization on validation messages

---

## Q046: DTO Mapping — Mapster vs AutoMapper

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Mapping |
| **Frequency** | Common |

### Question

When choose Mapster over AutoMapper in .NET projects?

### Short Answer (30 seconds)

AutoMapper: convention-based, mature, runtime mapping. Mapster: compile-time code gen, faster, less magic.

### Detailed Answer (3–5 minutes)

**AutoMapper:** `CreateMap<Order, OrderDto>()` — profile classes, team knows it.

**Mapster:** `[Adapt]` or `TypeAdapterConfig` — source generator option, zero runtime reflection on hot paths.

**Architect:** Pick one per org — document in template. Mapster for performance-critical high-RPS read models. AutoMapper for large legacy migration. Never manual mapping in 50 places when codegen works.

### Architecture Perspective

Mapping tool choice affects build time and runtime perf.

### Follow-up Questions

1. **Projection EF + Mapster? — `ProjectToType<OrderDto>()` — SQL-level select.**
2. **Manual mapping when? — Complex domain transforms with business rules — not property copy.**

### Common Mistakes in Interviews

- Both AutoMapper and Mapster in same solution
- Mapping in controller action bodies
- Ignore null propagation bugs on nested DTOs

---

## Q047: EF Core Tracking vs AsNoTracking

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | EF Core |
| **Frequency** | Very Common |

### Question

When use AsNoTracking in EF Core queries?

### Short Answer (30 seconds)

AsNoTracking: read-only queries — no change tracker overhead, lower memory. Tracking: default for updates.

### Detailed Answer (3–5 minutes)

```csharp
var orders = await db.Orders.AsNoTracking()
    .Where(o => o.CustomerId == id)
    .ToListAsync();
```

**Architect:** All list/search/report endpoints → AsNoTracking by default. Global `NoTracking` with explicit `AsTracking()` for writes. Mis-tracked graphs cause stale data and surprise `SaveChanges` updates.

### Architecture Perspective

Tracking defaults drive API performance and correctness.

### Follow-up Questions

1. **AsNoTrackingWithIdentityResolution? — Deduplicate included entities in graph read.**
2. **ProjectTo vs AsNoTracking? — DTO projection avoids entity materialization entirely.**

### Common Mistakes in Interviews

- AsNoTracking then attach and update — subtle bugs
- Tracking on read-heavy report returning 10K rows
- NoTracking on entity you then modify and save

---

## Q048: EF Core Zero-Downtime Migrations

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | EF Core |
| **Frequency** | Common |

### Question

Strategies for zero-downtime EF Core schema migrations?

### Short Answer (30 seconds)

Expand-contract pattern: additive changes first, deploy code reading both, backfill, remove old — never destructive column drop in single deploy.

### Detailed Answer (3–5 minutes)

**Safe:** add nullable column → deploy app writing new column → backfill → make NOT NULL → remove old.

**Risky:** rename column, drop column, change type — require multi-phase.

**Architect:** Migrations in CI reviewed like code. `dotnet ef migrations script` for DBA review. Feature flags gate code paths using new schema. Consider separate migration runner job, not app startup `Migrate()` in multi-instance.

### Architecture Perspective

Schema changes are deployment architecture decisions.

### Follow-up Questions

1. **Idempotent SQL scripts? — Flyway-style vs EF migrations — pick team standard.**
2. **Online index creation? — SQL Server `ONLINE=ON` for large tables.**

### Common Mistakes in Interviews

- Drop column same release as code stops reading it
- Database.Migrate() on every pod startup race
- Breaking rename in single migration

---

## Q049: Specification Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DDD |
| **Frequency** | Common |

### Question

Implement specification pattern for repository queries?

### Short Answer (30 seconds)

Encapsulate query criteria as composable `ISpecification<T>` objects — reusable, testable, keeps LINQ out of handlers.

### Detailed Answer (3–5 minutes)

```csharp
public class ActiveOrdersSpec : Specification<Order>
{
    public ActiveOrdersSpec(Guid customerId) =>
        Query.Where(o => o.CustomerId == customerId && o.Status == OrderStatus.Active);
}
// Compose: activeSpec.And(new DateRangeSpec(from, to))
```

**Architect:** Specifications in domain or application layer — repository accepts `ISpecification<T>`. Avoid specification explosion — group common specs. Works with Ardalis.Specification library.

### Architecture Perspective

Query logic reuse without repository god methods.

### Follow-up Questions

1. **Specification vs inline LINQ? — Inline OK for one-off; spec when reused or complex.**
2. **Include expressions in spec? — `Query.Include(o => o.Lines)` centralized.**

### Common Mistakes in Interviews

- GetOrdersByCustomerAndStatusAndDate repository method proliferation
- Specification with IQueryable leaked to API layer
- Untestable 200-line LINQ in handler

---

## Q050: MediatR CQRS Introduction

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Architecture |
| **Frequency** | Very Common |

### Question

Introduce MediatR CQRS in ASP.NET Core service — architect view?

### Short Answer (30 seconds)

Commands mutate, queries read — handlers isolated, controllers thin, cross-cutting via pipeline behaviors.

### Detailed Answer (3–5 minutes)

```csharp
public record CreateOrderCommand(string CustomerId) : IRequest<OrderId>;

public class CreateOrderHandler : IRequestHandler<CreateOrderCommand, OrderId>
{
    public async Task<OrderId> Handle(CreateOrderCommand cmd, CancellationToken ct) { ... }
}
```

**Architect:** One handler per use case — clear boundaries. Pipeline behaviors: validation, logging, transactions. Don't MediatR for every CRUD if team is 2 people — ceremony cost. Great at 20+ use cases per bounded context.

### Architecture Perspective

CQRS scales team parallelism on features.

### Follow-up Questions

1. **IRequest vs INotification? — Commands return value; notifications publish to multiple handlers.**
2. **Query side read models? — Separate handlers hitting optimized views — full CQRS split.**

### Common Mistakes in Interviews

- MediatR for simple pass-through CRUD only
- Handler calls handler via MediatR recursively
- God IRequestHandler with switch on request type

---

## Q051: Repository Pattern — When to Use

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Architecture |
| **Frequency** | Common |

### Question

When is repository pattern justified over DbContext directly?

### Short Answer (30 seconds)

Justified: domain-centric persistence abstraction, swap storage, test without EF. Overkill: thin CRUD wrapping every DbSet call.

### Detailed Answer (3–5 minutes)

**Use when:** aggregate roots with persistence ignorance, multiple data sources, strict unit test boundaries.

**Skip when:** simple API with EF — `DbContext` is already unit of work; extra `IRepository<Order>` adds no value.

**Architect:** `IOrderRepository` with domain meaningful methods (`GetByCustomerWithLines`) — not `GetAll`, `GetById`, `Delete` generics on everything.

### Architecture Perspective

Repository is abstraction cost — apply where it earns value.

### Follow-up Questions

1. **Generic IRepository<T>? — Often leaky — encourages anemic queries.**
2. **Specification + repository? — Repository accepts spec — clean query composition.**

### Common Mistakes in Interviews

- Repository per entity table — 40 interfaces
- Repository re-exposes IQueryable to callers
- Mock repository integration test replaces real DB unnecessarily

---

## Q052: Unit of Work Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Architecture |
| **Frequency** | Common |

### Question

Unit of Work pattern with EF Core — still relevant?

### Short Answer (30 seconds)

DbContext already implements UoW — `SaveChanges` commits unit. Explicit `IUnitOfWork` wraps context when multiple repositories share one transaction.

### Detailed Answer (3–5 minutes)

```csharp
public interface IUnitOfWork { Task<int> SaveChangesAsync(CancellationToken ct); }
// Implementation holds DbContext
```

**Architect:** Single `SaveChanges` per request in MediatR transaction behavior. Multi-DbContext scenarios need `TransactionScope` or explicit database transaction. Don't nest multiple SaveChanges without reason.

### Architecture Perspective

Transaction boundary clarity prevents partial commits.

### Follow-up Questions

1. **Ambient transactions TransactionScope? — Cross-database — distributed — avoid if possible.**
2. **MediatR TransactionBehavior? — One UoW commit per command pipeline.**

### Common Mistakes in Interviews

- SaveChanges after every repository method call
- Multiple DbContexts without distributed transaction plan
- Unit of Work interface with 20 unrelated repos

---

## Q053: Domain Events in .NET

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DDD |
| **Frequency** | Common |

### Question

Raise and dispatch domain events in .NET cleanly?

### Short Answer (30 seconds)

Entities collect events; dispatch after successful persistence — decouple side effects from aggregate logic.

### Detailed Answer (3–5 minutes)

```csharp
public class Order : Entity
{
    public void Ship() { Status = Shipped; AddDomainEvent(new OrderShippedEvent(Id)); }
}
// Dispatch in SaveChanges interceptor or MediatR after SaveChanges
```

**Architect:** In-process MediatR `INotification` for same bounded context. Outbox pattern for cross-service — never dual-write DB + message bus. Handlers idempotent.

### Architecture Perspective

Domain events enable loose coupling within and across services.

### Follow-up Questions

1. **Event vs integration event? — Domain internal; integration crosses boundary with schema contract.**
2. **Dispatch before SaveChanges? — Side effects on uncommitted data — dangerous.**

### Common Mistakes in Interviews

- Publish to Kafka inside entity method
- Non-idempotent event handler on retry
- Domain event storm — 50 events per SaveChanges

---

## Q054: Background Jobs — Hangfire vs Queue

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Architecture |
| **Frequency** | Common |

### Question

Hangfire vs Azure Service Bus / RabbitMQ for background jobs?

### Short Answer (30 seconds)

Hangfire: in-process/SQL-backed scheduler — dashboards, cron, fire-and-forget in same app. Queue: durable async messaging — scale workers independently.

### Detailed Answer (3–5 minutes)

**Hangfire when:** internal ops jobs, retry UI, team already on SQL, moderate volume.

**Queue when:** high throughput, microservice workers, cloud-native scale, poison message handling.

**Architect:** Never Hangfire on web tier at scale — dedicated worker role. Queue + outbox for transactional consistency. Hangfire SQL storage becomes bottleneck.

### Architecture Perspective

Job infrastructure is reliability and scale decision.

### Follow-up Questions

1. **Hangfire recurring jobs vs IHostedService cron? — Hangfire gives dashboard and persistence.**
2. **Idempotency keys on queue consumers? — Mandatory for at-least-once delivery.**

### Common Mistakes in Interviews

- Hangfire on every API instance processing same jobs
- Fire-and-forget Task.Run for critical payments
- No dead-letter queue monitoring

---

## Q055: IMemoryCache vs Distributed Redis Cache

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Caching |
| **Frequency** | Very Common |

### Question

When IMemoryCache vs distributed Redis cache?

### Short Answer (30 seconds)

IMemoryCache: per-instance, fastest, not shared — good for reference data, config snapshots. Redis: shared across instances, session, rate limit counters.

### Detailed Answer (3–5 minutes)

```csharp
services.AddMemoryCache();
services.AddStackExchangeRedisCache(o => o.Configuration = redisConn);
```

**Architect:** Memory cache for read-heavy static catalog with short TTL + Redis pub/sub invalidation optional. Redis for user session, shopping cart, distributed locks. Always set size limits and eviction on MemoryCache.

### Architecture Perspective

Cache tier choice affects consistency across scaled pods.

### Follow-up Questions

1. **Cache-aside vs read-through? — Document pattern per use case.**
2. **IDistributedCache serialization? — JSON overhead — consider MessagePack for large objects.**

### Common Mistakes in Interviews

- IMemoryCache for user-specific cart in K8s 10 replicas
- Unbounded MemoryCache — OOM kill
- Cache without TTL on mutable data

---

## Q056: ASP.NET Core Rate Limiting

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Implement rate limiting in ASP.NET Core 7+?

### Short Answer (30 seconds)

Built-in `Microsoft.AspNetCore.RateLimiting` — fixed window, sliding window, token bucket, concurrency limiter.

### Detailed Answer (3–5 minutes)

```csharp
builder.Services.AddRateLimiter(o => o.AddFixedWindowLimiter("api", opt =>
{
    opt.PermitLimit = 100;
    opt.Window = TimeSpan.FromMinutes(1);
}));
app.UseRateLimiter();
app.MapGet("/orders", ...).RequireRateLimiting("api");
```

**Architect:** Per-IP for anonymous, per-API-key or per-user for authenticated. Return 429 with `Retry-After`. Gateway-level (APIM, Cloudflare) + app-level for defense in depth.

### Architecture Perspective

Rate limiting protects dependencies and fair usage.

### Follow-up Questions

1. **Partitioned rate limiter? — Rate limit by user ID not just IP.**
2. **Rate limit vs throttling downstream? — App limits ingress; bulkhead limits egress.**

### Common Mistakes in Interviews

- No rate limit on expensive export endpoint
- 429 without Retry-After header
- Rate limit only at app — DDoS overwhelms before Kestrel

---

## Q057: JWT Authentication Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

JWT authentication architecture for microservices?

### Short Answer (30 seconds)

Identity provider issues signed JWT; resource APIs validate signature, issuer, audience, expiry — stateless auth.

### Detailed Answer (3–5 minutes)

**Flow:** Login → IdP (Entra, Auth0) → access token + refresh token → API validates with `AddJwtBearer`.

```csharp
services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(o => {
        o.Authority = "https://login.example.com";
        o.Audience = "orders-api";
    });
```

**Architect:** Short-lived access tokens (15 min), refresh rotation, never store JWT in localStorage if XSS risk — HttpOnly cookie pattern for SPAs. Validate `aud`, `iss`, clock skew minimal.

### Architecture Perspective

Token design affects security posture and scale.

### Follow-up Questions

1. **Reference tokens vs JWT? — Opaque tokens validated via introspection — more server calls.**
2. **JWT in BFF pattern? — Backend-for-frontend holds tokens — SPA never sees access token.**

### Common Mistakes in Interviews

- Accept JWT without audience validation
- Long-lived JWT (30 days) as access token
- Symmetric key shared across 20 microservices leaked

---

## Q058: Authorization Policies vs Roles

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Policies vs roles in ASP.NET Core authorization?

### Short Answer (30 seconds)

Roles: coarse group membership (`Admin`, `User`). Policies: composable requirements — role + claim + custom handler.

### Detailed Answer (3–5 minutes)

```csharp
services.AddAuthorization(o => o.AddPolicy("CanRefund", p =>
    p.RequireClaim("permission", "orders:refund")));

[Authorize(Policy = "CanRefund")]
```

**Architect:** Prefer policy-based and permission claims over role explosion (`Admin`, `SuperAdmin`, `RegionalAdmin`...). `IAuthorizationHandler` for resource-based auth (`CanEditOrder` checks order owner).

### Architecture Perspective

Authorization model must scale with product complexity.

### Follow-up Questions

1. **FallbackPolicy? — Default deny all endpoints — explicit `[AllowAnonymous]`.**
2. **Resource-based auth IAuthorizationService? — `AuthorizeAsync(user, order, "EditPolicy")`.**

### Common Mistakes in Interviews

- Role checks scattered as string literals in controllers
- Authorize attribute without authentication middleware
- God role with all permissions

---

## Q059: CORS Architecture Decisions

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

CORS architecture for SPA + multiple APIs?

### Short Answer (30 seconds)

CORS is browser enforcement — server returns `Access-Control-Allow-Origin`. Not a substitute for auth.

### Detailed Answer (3–5 minutes)

**Architect:** Explicit allowed origins — never `*` with credentials. BFF or API gateway as single origin to SPA reduces CORS surface.

```csharp
services.AddCors(o => o.AddPolicy("Spa", p => p
    .WithOrigins("https://app.example.com")
    .AllowCredentials()));
```

**Preflight:** OPTIONS handled before auth middleware for anonymous preflight. Document which APIs need CORS vs server-to-server (no CORS needed).

### Architecture Perspective

CORS misconfiguration is common production bug.

### Follow-up Questions

1. **SameSite cookies vs CORS? — Related but different — cookie CSRF protection.**
2. **Wildcard subdomain WithOrigins? — Avoid overly broad `*.example.com` parsing limits.**

### Common Mistakes in Interviews

- AllowAnyOrigin with AllowCredentials
- CORS on internal service-to-service calls unnecessarily
- Auth middleware blocks OPTIONS preflight

---

## Q060: Content Negotiation and Versioning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | API Design |
| **Frequency** | Occasional |

### Question

How content negotiation relates to API versioning?

### Short Answer (30 seconds)

Content negotiation: client sends `Accept` header — server returns JSON, XML, or versioned media type. Versioning can live in URL, header, or `Accept: application/vnd.api.v2+json`.

### Detailed Answer (3–5 minutes)

**Architect:** Prefer URL or header versioning for clarity — media type versioning couples format and version (`vnd.company.order.v2+json`). `AddMvc().AddXmlSerializerFormatters()` only if enterprise clients require XML.

**Default:** `application/json` with URL `/v1/` — simplest ops and gateway routing.

### Architecture Perspective

Negotiation complexity should match actual client needs.

### Follow-up Questions

1. **406 Not Acceptable when? — No formatter matches Accept — rare if JSON default always offered.**
2. **Producing custom format? — `return Results.Content(data, "application/custom");`**

### Common Mistakes in Interviews

- Media type versioning without client support
- XML formatter enabled nobody uses — attack surface
- Version in URL and Accept header disagree

---

## Q061: IAsyncEnumerable API Streaming

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | ASP.NET Core |
| **Frequency** | Common |

### Question

Expose IAsyncEnumerable from ASP.NET Core for large datasets?

### Short Answer (30 seconds)

Stream results incrementally — lower memory, faster time-to-first-byte for exports and live feeds.

### Detailed Answer (3–5 minutes)

```csharp
app.MapGet("/orders/export", async IAsyncEnumerable<OrderDto> (
    IOrderService svc, [EnumeratorCancellation] CancellationToken ct) =>
{
    await foreach (var order in svc.StreamOrdersAsync(ct))
        yield return order;
});
```

**Architect:** Prefer streaming for million-row exports over `ToListAsync`. Set response timeout accordingly. NDJSON or SSE for browser clients. `[EnumeratorCancellation]` propagates client disconnect.

### Architecture Perspective

Streaming is memory architecture for data-heavy APIs.

### Follow-up Questions

1. **EF Core AsAsyncEnumerable? — Forward-only read — don't compose then ToList.**
2. **Backpressure IAsyncEnumerable? — Consumer speed limits producer — Channel alternative.**

### Common Mistakes in Interviews

- ToListAsync on million row query then return
- No cancellation — client disconnect leaves DB cursor open
- Buffer entire export in memory 'for simplicity'

---

## Q062: gRPC vs REST Decision

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | API Design |
| **Frequency** | Common |

### Question

When choose gRPC over REST for internal microservices?

### Short Answer (30 seconds)

gRPC: HTTP/2, protobuf binary, streaming, strong contracts — internal east-west. REST/JSON: browser-friendly, human-debuggable, public APIs.

### Detailed Answer (3–5 minutes)

**gRPC when:** service-to-service, high throughput, bi-directional streaming, polyglot with `.proto` contract.

**REST when:** public API, mobile/web clients, caching with HTTP semantics, teams without proto toolchain.

**Architect:** gRPC behind mesh (mTLS); REST at edge via gateway translation if needed. Don't expose raw gRPC to browsers without gRPC-Web proxy.

### Architecture Perspective

Protocol choice is boundary and consumer decision.

### Follow-up Questions

1. **gRPC transcoding? — REST facade on gRPC — Envoy, YARP.**
2. **Versioning proto breaking changes? — Field numbers never reuse — additive only.**

### Common Mistakes in Interviews

- gRPC for public browser API without gRPC-Web
- REST binary payloads for 10K RPS internal fan-out
- No deadline/timeout propagation in gRPC metadata

---

## Q063: SignalR Scale-Out Redis Backplane

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Real-Time |
| **Frequency** | Occasional |

### Question

Scale SignalR across multiple servers with Redis backplane?

### Short Answer (30 seconds)

Without backplane, WebSocket messages stay on one server. Redis backplane broadcasts hub messages to all instances.

### Detailed Answer (3–5 minutes)

```csharp
services.AddSignalR().AddStackExchangeRedis(redisConn, o => o.Configuration.ChannelPrefix = "MyApp");
```

**Architect:** Sticky sessions not required with Redis backplane but connection affinity helps. Azure SignalR Service preferred at scale — offloads connection management. Group names consistent across instances. Monitor Redis pub/sub latency.

### Architecture Perspective

Real-time scale requires shared message fabric.

### Follow-up Questions

1. **Azure SignalR vs self-hosted Redis? — Managed removes connection limit ops burden.**
2. **SignalR with JWT? — Pass token in query string WebSocket or use cookies — document security.**

### Common Mistakes in Interviews

- Scale SignalR horizontally without backplane
- Group message only reaches users on same pod
- Redis backplane single point of failure unmonitored

---

## Q064: Configuration and Azure Key Vault

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Configuration |
| **Frequency** | Very Common |

### Question

Load secrets from Azure Key Vault in ASP.NET Core?

### Short Answer (30 seconds)

Use `Azure.Extensions.AspNetCore.Configuration.Secrets` — merge Key Vault into configuration at startup with managed identity.

### Detailed Answer (3–5 minutes)

```csharp
builder.Configuration.AddAzureKeyVault(
    new Uri("https://myvault.vault.azure.net/"),
    new DefaultAzureCredential());
```

**Architect:** No secrets in appsettings committed to git. Managed identity in Azure — no client secrets in config. Reload with `AddAzureKeyVault` + `IOptionsMonitor` for rotatable secrets. Separate vault per environment.

### Architecture Perspective

Secret management is security baseline for cloud apps.

### Follow-up Questions

1. **Key Vault references App Service? — `@Microsoft.KeyVault(...)` — no code change deploy.**
2. **Local dev Key Vault? — `DefaultAzureCredential` + Azure CLI login or user secrets locally.**

### Common Mistakes in Interviews

- Connection strings in appsettings.Production.json in repo
- Service principal secret expires — no rotation runbook
- All config in Key Vault — non-secrets too — slow startup

---

## Q065: Feature Flags — Microsoft.FeatureManagement

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Configuration |
| **Frequency** | Common |

### Question

Adopt Microsoft.FeatureManagement in ASP.NET Core?

### Short Answer (30 seconds)

Decouple deploy from release — toggle features via config, App Configuration, or LaunchDarkly adapter.

### Detailed Answer (3–5 minutes)

```csharp
services.AddFeatureManagement();

[FeatureGate("NewCheckout")]
public class CheckoutV2Controller { }

if (await featureManager.IsEnabledAsync("BetaSearch"))
```

**Architect:** Percentage rollout, time window filters, targeting by user ID. Flags in Azure App Configuration with refresh. Remove stale flags quarterly — tech debt accumulates.

### Architecture Perspective

Feature flags enable safe progressive delivery.

### Follow-up Questions

1. **IFeatureFilter custom? — Tenant-based, region-based enablement.**
2. **Flags in zero-downtime migration? — Dual-write behind flag — expand-contract ally.**

### Common Mistakes in Interviews

- Permanent if-feature-flag else legacy
- No flag cleanup — 200 dead flags
- Flag default true in production by mistake

---

## Q066: Unit Testing — xUnit Best Practices

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Testing |
| **Frequency** | Common |

### Question

xUnit best practices for .NET service unit tests?

### Short Answer (30 seconds)

Arrange-Act-Assert, one logical assertion per test, descriptive names, avoid test inheritance, use fixtures sparingly.

### Detailed Answer (3–5 minutes)

```csharp
[Fact]
public async Task CreateOrder_ValidCommand_ReturnsOrderId()
{
    var handler = new CreateOrderHandler(_fakeRepo, _fakeClock);
    var result = await handler.Handle(new CreateOrderCommand(...), CancellationToken.None);
    Assert.NotEqual(Guid.Empty, result);
}
```

**Architect:** Test behavior not implementation — mock ports, not every private method. `Theory` + `InlineData` for parameter matrix. No shared mutable state between tests. CI runs unit tests < 2 min.

### Architecture Perspective

Test quality gates merge confidence.

### Follow-up Questions

1. **IClassFixture vs ICollectionFixture? — Expensive setup once per class/collection.**
2. **FluentAssertions? — Readable — org standard optional.**

### Common Mistakes in Interviews

- Mocking concrete classes instead of interfaces
- Tests hit real database labeled unit tests
- Async void test methods

---

## Q067: WebApplicationFactory Integration Tests

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Testing |
| **Frequency** | Common |

### Question

Integration test ASP.NET Core API with WebApplicationFactory?

### Short Answer (30 seconds)

Bootstraps real app in memory with test server — exercises middleware, DI, routing, database (often Testcontainers).

### Detailed Answer (3–5 minutes)

```csharp
public class OrdersApiTests : IClassFixture<WebApplicationFactory<Program>>
{
    private readonly HttpClient _client;
    public OrdersApiTests(WebApplicationFactory<Program> factory)
    {
        _client = factory.WithWebHostBuilder(b => b.ConfigureServices(s => {
            // replace DbContext with test DB
        })).CreateClient();
    }
}
```

**Architect:** `partial class Program` for test visibility. Replace external HTTP with `TestHandler`. Testcontainers SQL for realistic migrations test. Separate integration from unit in CI jobs.

### Architecture Perspective

Integration tests catch wiring bugs unit tests miss.

### Follow-up Questions

1. **CustomWebApplicationFactory pattern? — Shared seed data and auth header helpers.**
2. **Respawn DB reset? — Fast DB cleanup between tests.**

### Common Mistakes in Interviews

- Mock entire DbContext in integration test
- Shared production database connection string
- No assertion on HTTP status code and body shape

---

## Q068: Containerizing ASP.NET Core

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DevOps |
| **Frequency** | Very Common |

### Question

Dockerfile best practices for ASP.NET Core microservice?

### Short Answer (30 seconds)

Multi-stage build: SDK stage publish, runtime aspnet stage copy — small image, non-root user.

### Detailed Answer (3–5 minutes)

```dockerfile
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY . .
RUN dotnet publish -c Release -o /app

FROM mcr.microsoft.com/dotnet/aspnet:8.0
WORKDIR /app
COPY --from=build /app .
USER $APP_UID
ENTRYPOINT ["dotnet", "Orders.Api.dll"]
```

**Architect:** Pin image digests in prod. Health check `HEALTHCHECK` instruction. `ASPNETCORE_URLS=http://+:8080`. Read-only root filesystem where possible. Distroless or chiseled images for attack surface reduction.

### Architecture Perspective

Container hygiene affects security and deploy speed.

### Follow-up Questions

1. **K8s resources requests/limits? — Set from load test — not unset.**
2. **Graceful shutdown SIGTERM? — Kestrel drains — configure `terminationGracePeriodSeconds`.**

### Common Mistakes in Interviews

- SDK image as production runtime
- Running as root in container
- No health check — K8s sends traffic to starting pod

---

## Q069: CI Pipeline for .NET Microservice

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DevOps |
| **Frequency** | Common |

### Question

Essential CI pipeline stages for .NET microservice?

### Short Answer (30 seconds)

Restore → build → test (unit + integration) → analyze (Sonar) → pack/publish → container build → push → deploy staging.

### Detailed Answer (3–5 minutes)

**Architect gates:**
- `dotnet test` with coverage threshold
- `dotnet format --verify-no-changes`
- Security scan (Dependabot, Trivy image scan)
- EF migration script artifact for DBA review

**GitHub Actions / Azure DevOps:** cache NuGet, matrix SDK version only if multi-target. Fail fast on analyzer warnings as errors in main.

### Architecture Perspective

CI is quality contract before production.

### Follow-up Questions

1. **Trunk-based vs GitFlow CI? — Main branch always deployable — feature flags for incomplete.**
2. **Integration test in CI with Testcontainers? — Docker-in-Docker service required.**

### Common Mistakes in Interviews

- Deploy without running tests
- No lock file — floating package versions break main
- Skip container scan — vulnerable base image shipped

---

## Q070: Performance Profiling Workflow

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Common |

### Question

Performance profiling workflow for slow ASP.NET Core endpoint?

### Short Answer (30 seconds)

Reproduce → measure (dotnet-counters, App Insights) → profile (dotnet-trace, dotMemory) → fix → verify.

### Detailed Answer (3–5 minutes)

**Steps:**
1. Load test baseline (k6, NBomber)
2. `dotnet-counters monitor System.Runtime` — GC, thread pool
3. `dotnet-trace collect` during load — analyze in Speedscope
4. Check SQL execution plan, N+1 queries

**Architect:** Profile in staging with production-like data volume. Fix biggest bottleneck first — often DB not CPU. Establish perf budget per endpoint in CI smoke load test.

### Architecture Perspective

Systematic profiling beats guessing optimizations.

### Follow-up Questions

1. **EventPipe vs Application Insights profiler? — EventPipe local deep dive; App Insights production sampling.**
2. **BenchmarkDotNet for micro-optimization? — Library code — not full HTTP stack.**

### Common Mistakes in Interviews

- Optimize code before measuring
- Profile dev laptop with 100 rows seed data
- string concatenation optimized while SQL does table scan

---
