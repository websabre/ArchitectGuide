# Week 45 — Fundamentals Interview Q&A

> Q001–Q030: Premium format (Week 1 quality).  
> See also: [Interview prep hub](../../../interview-prep/README.md)

---


## Q001: C# Fundamentals Interview Approach

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | C# Fundamentals |
| **Frequency** | Very Common |

### Question

How should a solution architect approach C# fundamentals questions in a senior .NET interview?

### Short Answer (30 seconds)

Lead with trade-offs and production context — value vs reference, async I/O, nullable types, records — not syntax trivia. Structure answers: definition → when to use → when to avoid → real API example → architect consequence (perf, safety, team conventions).

### Detailed Answer (3–5 minutes)

**Interview structure (3–5 min per topic):**
1. **One-sentence definition** — precise, not textbook length
2. **Decision criteria** — workload shape drives choice
3. **Production example** — payment API, order handler, hot path
4. **Architect angle** — team standards, analyzers, CI gates

**High-yield topics interviewers probe:**
| Topic | Architect answer hook |
|-------|----------------------|
| Value vs reference | `record struct Money` for hot DTOs; avoid large structs on stack |
| Nullable reference types | Enable on new projects; warnings-as-errors in CI |
| `record` vs `class` | Immutable API contracts vs domain entities with behavior |
| async/await | I/O-bound handlers only; `ConfigureAwait` in library code |
| `Span<T>` / `Memory<T>` | Parsing/serialization hot paths — not CRUD APIs |

**How to open:** 'Before I answer, I'll state the trade-off I'd document in an ADR...'

**Red flags to avoid:** Quoting language spec without use case; ignoring thread-safety with `DbContext`; claiming async makes CPU work faster.

**Practice:** Pick 5 fundamentals — answer in 90 seconds each with one .NET 8+ feature mention.

### Architecture Perspective

Architects are evaluated on judgment under constraints — C# fundamentals are the vocabulary for reliability and performance decisions.

### Follow-up Questions

1. **Generics variance? — Know `in`/`out` for library design — rare but senior signal.**
2. **LINQ deferred execution trap? — Multiple enumeration — materialize once or use `IAsyncEnumerable`.**

### Common Mistakes in Interviews

- Reciting syntax without production trade-off
- Treating `async void` as acceptable pattern
- Ignoring nullable reference types in API contracts

---

## Q002: ASP.NET Core Architecture Interview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | ASP.NET Core |
| **Frequency** | Very Common |

### Question

How do you structure answers for ASP.NET Core architecture questions at architect level?

### Short Answer (30 seconds)

Frame ASP.NET Core as a composable pipeline: host → middleware → routing → endpoints → cross-cutting (auth, validation, logging). Answer with layer boundaries, DI lifetimes, and operational concerns — not controller trivia alone.

### Detailed Answer (3–5 minutes)

**Reference mental model:**
```
Client → Reverse Proxy / WAF → ASP.NET Host
  → Middleware pipeline (exception, HTTPS, CORS, auth)
  → Endpoints (Minimal API / Controllers)
  → Application layer (MediatR handlers)
  → Domain → Infrastructure (EF, HTTP clients, messaging)
```

**Architect talking points:**
- **Middleware order** — auth before authz; exception handler outermost
- **DI lifetimes** — scoped `DbContext`; no captive dependencies in singletons
- **API surface** — thin endpoints, ProblemDetails, versioning, rate limits
- **Observability** — correlation ID middleware, OpenTelemetry, health checks (`/health/live`, `/health/ready`)
- **Resilience** — `IHttpClientFactory`, Polly policies, timeouts

**Answer template:**
1. Draw or describe request flow
2. Name the layer owning each concern
3. State one production failure you've prevented (CORS, scope bug, socket exhaustion)
4. Mention deployment target (App Service, AKS, container)

**Common interview prompts:** middleware order, minimal APIs at scale, global exception handling, validation pipeline.

**Differentiator:** Connect ASP.NET choices to blast radius — feature flags, blue-green, config per environment.

### Architecture Perspective

ASP.NET Core architecture interviews test whether you design operable APIs — pipeline, DI, and observability are the architect's toolkit.

### Follow-up Questions

1. **Minimal API vs controllers? — Team consistency and filter ecosystem — not performance religion.**
2. **YARP reverse proxy? — Gateway pattern in .NET — mention when API aggregation asked.**

### Common Mistakes in Interviews

- Fat controllers with business logic
- Wrong middleware order without explaining why
- Singleton service holding scoped DbContext

---

## Q003: SOLID Principles Interview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | SOLID |
| **Frequency** | Very Common |

### Question

How approach SOLID principles questions in a .NET architect interview?

### Short Answer (30 seconds)

Don't recite definitions — give violation → refactor → architectural consequence. Map each principle to service boundaries, testability, and change isolation. Acknowledge when over-application creates distributed monolith.

### Detailed Answer (3–5 minutes)

**Interview framework per principle:**
| Principle | Strong answer pattern |
|-----------|----------------------|
| **S**RP | One reason to change — split `OrderService` god class |
| **O**CP | Strategy/handlers — extend without editing stable code |
| **L**SP | Substitutable interfaces — no `NotSupportedException` surprises |
| **I**SP | Segregate read/write/admin repository interfaces |
| **D**IP | Domain depends on ports; `Program.cs` is composition root |

**Example arc (SRP):**
```csharp
// Violation: validate + save + email + PDF in one class
// Fix: OrderValidator, IOrderRepository, INotificationService
// Architecture: same logic at microservice boundary — one bounded context
```

**Architect nuance:**
- SOLID at class level ≠ microservice per class
- SRP at deployable unit aligns with team ownership (Conway's law)
- DIP enables hexagonal architecture — domain never references EF

**Follow-up readiness:** 'How does OCP relate to MediatR behaviors?' 'When is repository pattern violating YAGNI?'

**Score higher:** Mention contract tests verifying interface implementations across teams.

### Architecture Perspective

SOLID interviews reward refactor instinct and boundary judgment — principles are tools for change management, not badges.

### Follow-up Questions

1. **SOLID vs microservices? — Bounded context per service is SRP at architecture scale.**
2. **When skip repository? — EF DbContext is UoW — justify seams with testing needs.**

### Common Mistakes in Interviews

- Defining SRP as one method per class
- Abstract factory for every `new` statement
- SOLID buzzwords without .NET code example

---

## Q004: Design Patterns Interview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Design Patterns |
| **Frequency** | Very Common |

### Question

How should architects answer design pattern questions without sounding like a Gang of Four textbook?

### Short Answer (30 seconds)

Connect patterns to .NET idioms: Strategy → DI keyed services; Decorator → `HttpMessageHandler` chain; Observer → MediatR domain events; Factory → plugin registration. State problem, pattern, .NET implementation, and when NOT to use.

### Detailed Answer (3–5 minutes)

**Pattern → .NET mapping (interview cheat sheet):**
| Pattern | Enterprise .NET use | Skip when |
|---------|---------------------|----------|
| Strategy | `IShippingCalculator`, payment gateways | Single algorithm forever |
| Factory | `INotificationFactory` by channel | DI handles all cases |
| Decorator | Caching repository, logging handler | Decorator stack >4 deep |
| Observer | MediatR `INotification`, outbox events | Static C# events in web app |
| Repository | Aggregate persistence seam | Thin EF CRUD wrapper |
| Unit of Work | `DbContext.SaveChanges()` | Cross-service 'UoW' fantasy |

**Answer structure:**
1. **Problem** — interchangeable behavior or cross-cutting concern
2. **Pattern** — name it once, then show code
3. **DI wiring** — how it registers in `Program.cs`
4. **Distributed boundary** — in-proc pattern vs message bus

**Architect distinction:** Patterns solve *local* coupling; microservices solve *organizational* coupling — don't confuse.

**Anti-pattern callout:** Abstract factory when only one product type exists — YAGNI.

**Bonus:** Mention Scrutor `Decorate<T>()` for decorator registration.

### Architecture Perspective

Pattern interviews test whether you map structure to maintainability — .NET DI and MediatR are the modern pattern runtime.

### Follow-up Questions

1. **Mediator vs MediatR? — CQRS command/query dispatch — not chat room pattern.**
2. **Chain of Responsibility? — Middleware pipeline and Polly policy wrap — good follow-up.**

### Common Mistakes in Interviews

- Listing 23 GoF patterns from memory
- Pattern for every line of code
- Static events for cross-service communication

---

## Q005: EF Core Architecture Interview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | EF Core |
| **Frequency** | Very Common |

### Question

How approach Entity Framework Core architecture questions as a solution architect?

### Short Answer (30 seconds)

Position EF Core as data access infrastructure — not the domain model. Cover DbContext lifetime, query strategy (projection vs Include), transaction boundaries, migrations governance, and when raw SQL or read replicas belong in the architecture.

### Detailed Answer (3–5 minutes)

**Architectural layers:**
```
API → Application handler → Domain (entities, invariants)
                              ↓
                    Infrastructure (EF Core DbContext, configurations)
```

**Key interview topics:**
| Concern | Architect answer |
|---------|------------------|
| DbContext scope | Scoped per HTTP request — never singleton |
| N+1 queries | `.Include`, projection `.Select()`, split queries |
| Tracking | `AsNoTracking()` on read APIs |
| Transactions | `SaveChanges()` once per request; explicit tx for multi-step |
| Migrations | CI pipeline, backward-compatible, separate from app deploy |
| Raw SQL | Isolated query classes; parameterized; ADR with plan evidence |
| Distributed data | Saga/outbox — not shared DbContext across services |

**Repository pattern stance:** Use when aggregate boundary, multiple stores, or test seam — anti-pattern when generic `IRepository<T>` wraps `DbSet` with no value.

**Performance narrative:** Detect with App Insights SQL deps → fix projection → measure → document.

**Migration governance:** Idempotent scripts, rollback plan, expand-contract for zero-downtime schema changes.

### Architecture Perspective

EF Core architecture is about boundaries and query discipline — architects prevent ORM leaks into domain and API contracts.

### Follow-up Questions

1. **DbContext pooling? — Performance optimization — distinct from connection pooling.**
2. **Compiled queries? — Hot path micro-optimization after projection and indexes.**

### Common Mistakes in Interviews

- Expose `IQueryable` from repository to controllers
- Lazy loading enabled globally in APIs
- One SaveChanges per row in a loop

---

## Q006: SOLID Single Responsibility

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | SOLID |
| **Frequency** | Very Common |

### Question

Explain the Single Responsibility Principle. Give a .NET example of a violation and how you would refactor it.

### Short Answer (30 seconds)

A class should have one reason to change — one job. Violation: `OrderService` that validates, persists, sends email, and generates PDF. Refactor into separate services orchestrated by a thin coordinator.

### Detailed Answer (3–5 minutes)

**SRP:** Each module owns one axis of change — persistence, notification, or business rules — not all three.

**Violation:**
```csharp
public class OrderService {
  public void PlaceOrder(Order o) {
    Validate(o); _db.Save(o); _email.Send(o); _pdf.Generate(o);
  }
}
```

**Refactor:** `OrderValidator`, `IOrderRepository`, `INotificationService`, `IInvoiceGenerator` injected into a slim `PlaceOrderHandler`.

**Architect lens:** SRP at service boundary — microservice 'does one thing' is SRP at deployable unit. Over-splitting creates distributed monolith — balance cohesion vs change isolation.

### Architecture Perspective

Interviewers want refactor instinct, not textbook definition — show before/after with reasons to change.

### Follow-up Questions

1. **SRP vs microservices? — One bounded context per service — SRP at architecture level.**
2. **When is a god class acceptable? — Prototype or script — never in production domain layer.**

### Common Mistakes in Interviews

- Defining SRP as 'one method per class'
- Splitting into 20 one-liner classes with no cohesion
- Ignoring that 'reason to change' comes from stakeholders not code shape

---

## Q007: Open Closed Principle

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | SOLID |
| **Frequency** | Very Common |

### Question

What is the Open/Closed Principle and how do you apply it in ASP.NET extensibility?

### Short Answer (30 seconds)

Open for extension, closed for modification. Add behavior via new types (strategies, handlers) without editing existing stable code — e.g. `IAuthorizationHandler`, MediatR pipeline behaviors, or policy-based auth.

### Detailed Answer (3–5 minutes)

**OCP in .NET:**
- **Strategy injection** — new `IPricingStrategy` implementation without changing `CheckoutService`
- **MediatR behaviors** — add logging/validation pipeline without touching handlers
- **Policy-based authorization** — new `IAuthorizationRequirement` + handler

**Anti-pattern:** Giant `switch` on `orderType` in one service — every new type edits core class.

**Architect:** Plugin architecture (MEF, DI registration modules) enables third-party extensions. Document extension points in ADR — which assemblies are stable vs pluggable.

### Architecture Perspective

OCP is how platforms scale feature velocity without regression risk on core paths.

### Follow-up Questions

1. **OCP vs YAGNI? — Introduce extension point when second variant is certain — not ten speculative interfaces.**
2. **Decorator vs inheritance for OCP? — Prefer composition — decorators wrap without subclass explosion.**

### Common Mistakes in Interviews

- switch/if-else chains for every new feature
- Abstracting before second use case exists
- Modifying shared library for one team's edge case

---

## Q008: Liskov Substitution

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | SOLID |
| **Frequency** | Common |

### Question

Explain Liskov Substitution Principle with a .NET collections or inheritance example.

### Short Answer (30 seconds)

Subtypes must be substitutable for base types without breaking callers. Classic violation: `Square : Rectangle` where setting width breaks height invariant. In .NET: don't throw `NotSupportedException` on base interface methods callers expect to work.

### Detailed Answer (3–5 minutes)

**LSP:** Preconditions not strengthened, postconditions not weakened, invariants preserved.

**.NET examples:**
- `ReadOnlyCollection<T>` — callers expecting mutable list break
- `Repository` subclass that throws on `Delete` when base allows it
- EF `DbContext` override that skips `SaveChanges` side effects

**Fix:** Smaller interfaces (`IReadRepository`, `IWriteRepository`) so read-only impl doesn't fake unsupported writes.

**Architect:** Contract tests on interface implementations — CI verifies LSP across teams.

### Architecture Perspective

LSP connects inheritance design to production bugs when mocks don't match real behavior.

### Follow-up Questions

1. **Interface segregation relation? — ISP prevents LSP violations from fat interfaces.**
2. **Testing LSP? — Property-based tests — any impl satisfies same contract.**

### Common Mistakes in Interviews

- Subclass that changes expected behavior silently
- Throwing NotSupportedException on half the interface
- Mock in tests that violates production impl contract

---

## Q009: Interface Segregation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | SOLID |
| **Frequency** | Common |

### Question

What is Interface Segregation and how does it show up in repository and API design?

### Short Answer (30 seconds)

Clients should not depend on methods they don't use. Split `IUserRepository` into `IUserReader`, `IUserWriter`, `IUserAdmin` — consumers take only what they need.

### Detailed Answer (3–5 minutes)

**Fat interface smell:**
```csharp
interface IOrderRepo {
  Get(); Save(); Delete(); BulkImport(); GenerateReport();
}
```
Reporting service forced to depend on `Delete`.

**Segregated:**
- `IOrderQueries` — read models
- `IOrderCommands` — writes
- `IOrderMaintenance` — admin batch jobs

**API parallel:** Don't expose 40-field admin DTO on mobile BFF — separate read contracts.

**Architect:** Segregation reduces blast radius of change and clarifies security boundaries (read-only service account gets `IReader` only).

### Architecture Perspective

ISP is permission and dependency minimization — critical for zero-trust service accounts.

### Follow-up Questions

1. **ISP vs too many interfaces? — Segregate by client role — not every method gets its own file.**
2. **CQRS connection? — Command/query split is ISP at architectural level.**

### Common Mistakes in Interviews

- One IRepository<T> with 15 methods for all consumers
- Admin operations on same interface as public API
- Segregating into unusable one-method interfaces

---

## Q010: Dependency Inversion

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | SOLID |
| **Frequency** | Very Common |

### Question

Explain Dependency Inversion and how DI containers implement it in ASP.NET Core.

### Short Answer (30 seconds)

High-level modules depend on abstractions, not concretions. `OrderService` depends on `IOrderRepository`, not `SqlOrderRepository`. ASP.NET Core DI registers implementations at composition root.

### Detailed Answer (3–5 minutes)

**DIP layers:**
1. Domain defines `IOrderRepository` port
2. Infrastructure implements `SqlOrderRepository` adapter
3. `Program.cs` wires `AddScoped<IOrderRepository, SqlOrderRepository>`

**Benefits:** Unit test with fakes, swap SQL for Cosmos without domain change, clear module boundaries.

**Composition root:** Only `Program.cs`/startup references concrete types — rest of app sees interfaces.

**Architect:** DIP enables hexagonal architecture — domain never imports EF or HTTP.

### Architecture Perspective

DIP is the foundation of testable .NET microservices — interviewers probe composition root discipline.

### Follow-up Questions

1. **DI vs service locator? — Constructor injection only — service locator hides dependencies.**
2. **Registering concrete types everywhere? — Bind to interfaces at boundaries.**

### Common Mistakes in Interviews

- Domain project references Entity Framework
- new SqlConnection() inside business logic
- Service locator or static singletons in domain

---

## Q011: Repository Anti-Pattern When

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Data Access |
| **Frequency** | Very Common |

### Question

When is the repository pattern an anti-pattern in .NET?

### Short Answer (30 seconds)

When it wraps EF `DbSet` with no added value — leaky CRUD pass-through, duplicate LINQ in repo and service, or hides `IQueryable` leading to N+1. Skip for simple CRUD; use when aggregating multiple sources, caching, or test seam needed.

### Detailed Answer (3–5 minutes)

**Anti-pattern signals:**
- `GetById`, `GetAll`, `Add`, `Update`, `Delete` only — EF already is a repository
- Generic `IRepository<T>` used everywhere — anemic domain
- Repository returns `IQueryable` — data access leaks to controllers

**Good use:**
- Aggregate root persistence with domain mapping
- Multiple backing stores (SQL + search index)
- Explicit test double boundary

**Architect:** CQRS read side often skips repository — queries hit optimized projections directly.

### Architecture Perspective

Senior answer: repository is a seam, not a mandatory layer — justify with testing and boundary needs.

### Follow-up Questions

1. **Specification pattern instead? — Composable query specs when complex filtering reused.**
2. **DbContext as unit of work? — Often sufficient — don't wrap for ceremony.**

### Common Mistakes in Interviews

- Mandatory IRepository<T> on every entity
- Repository per table in DDD aggregate design
- Returning IQueryable to API layer

---

## Q012: Unit of Work Interview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Data Access |
| **Frequency** | Very Common |

### Question

Explain Unit of Work pattern and how EF Core DbContext implements it.

### Short Answer (30 seconds)

Unit of Work tracks changes across multiple repositories in one transaction. EF `DbContext` is a UoW — `SaveChanges()` commits atomically. Explicit UoW wrapper useful when multiple DbContexts or non-EF stores participate.

### Detailed Answer (3–5 minutes)

**EF Core UoW:**
```csharp
await using var tx = await _db.Database.BeginTransactionAsync();
try {
  _db.Orders.Add(order);
  _db.Inventory.Update(stock);
  await _db.SaveChangesAsync();
  await tx.CommitAsync();
} catch { await tx.RollbackAsync(); throw; }
```

**Explicit `IUnitOfWork`:** Wraps `DbContext` for domain services that shouldn't know EF — `Commit()`/`Rollback()`.

**Distributed:** Cross-service UoW needs saga — not one SQL transaction.

**Architect:** Scoped `DbContext` per HTTP request = one UoW per request — default ASP.NET pattern.

### Architecture Perspective

UoW interview tests transaction boundary understanding — critical for consistency.

### Follow-up Questions

1. **Multiple SaveChanges in one request? — Usually one at end — intermediate saves break atomicity.**
2. **UoW across microservices? — Saga/outbox — not shared DbContext.**

### Common Mistakes in Interviews

- Calling SaveChanges after every single insert
- Singleton DbContext
- Expecting SQL transaction across HTTP calls

---

## Q013: EF Core N+1 Problem

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | EF Core |
| **Frequency** | Very Common |

### Question

What is the N+1 query problem in EF Core and how do you fix it?

### Short Answer (30 seconds)

N+1: load N parent rows, then one query per child in a loop — 1 + N round trips. Fix with `.Include()`, `.ThenInclude()`, projection `.Select()`, or explicit split query / batching.

### Detailed Answer (3–5 minutes)

**Problem:**
```csharp
var orders = await _db.Orders.ToListAsync();
foreach (var o in orders)
  var items = o.Items; // lazy load triggers query each time
```

**Fixes:**
1. **Eager load** — `.Include(o => o.Items)`
2. **Projection** — `.Select(o => new { o.Id, Items = o.Items.Select(...) })`
3. **Split query** — `.AsSplitQuery()` for cartesian explosion
4. **Explicit loading** — `Entry(o).Collection(x => x.Items).LoadAsync()` once batched

**Detection:** EF logging, MiniProfiler, Application Insights dependency traces.

**Architect:** API pagination + projection beats Include on large graphs.

### Architecture Perspective

N+1 is the #1 EF production perf bug — show detection and fix, not just definition.

### Follow-up Questions

1. **AsNoTracking when? — Read-only lists — reduces memory and tracking overhead.**
2. **Cartesian explosion? — Multiple Includes inflate rows — split query or projection.**

### Common Mistakes in Interviews

- Lazy loading enabled globally in API
- Include entire object graph by default
- Not profiling SQL in staging

---

## Q014: EF Core Raw SQL When

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | EF Core |
| **Frequency** | Common |

### Question

When should you use raw SQL with EF Core instead of LINQ?

### Short Answer (30 seconds)

Raw SQL for: complex reports, bulk updates, table hints, database-specific features (JSON indexes, CTEs), or proven perf-critical paths where LINQ generates poor plans. Use `FromSqlRaw` with parameters — never string concat.

### Detailed Answer (3–5 minutes)

**Use cases:**
- Bulk `UPDATE`/`DELETE` — `ExecuteSqlRawAsync`
- Window functions, recursive CTEs
- Indexed view queries
- Migration-time data fixes

**Safe pattern:**
```csharp
_db.Orders.FromSqlInterpolated($"SELECT * FROM Orders WHERE Status = {status}")
```

**Risks:** Bypasses change tracker, DB coupling, harder to test.

**Architect:** Isolate raw SQL in query classes — keep domain free of SQL strings. Document in ADR with benchmark evidence.

### Architecture Perspective

Raw SQL is a scalpel — justify with execution plan or unsupported LINQ, not preference.

### Follow-up Questions

1. **FromSql vs ExecuteSql? — FromSql materializes entities; Execute for non-query.**
2. **Stored procedures? — Valid for DBA-owned tuning — map with FromSqlRaw.**

### Common Mistakes in Interviews

- String concatenation SQL — injection risk
- Raw SQL everywhere avoiding LINQ maintainability
- No parameterization on user input

---

## Q015: ASP.NET Middleware Order

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | ASP.NET Core |
| **Frequency** | Very Common |

### Question

What is the correct middleware order in ASP.NET Core and why does it matter?

### Short Answer (30 seconds)

Order matters because each middleware wraps the next. Typical: Exception handler → HTTPS → Static files → Routing → CORS → Authentication → Authorization → Endpoints. Correlation ID early; auth before authz.

### Detailed Answer (3–5 minutes)

**Recommended order:**
1. Exception handling / developer exception page
2. HTTPS redirection
3. Static files (if any)
4. Routing
5. CORS
6. Authentication
7. Authorization
8. Custom (logging, correlation ID)
9. Endpoints

**Why:** Auth middleware must run before `[Authorize]` endpoints execute. CORS before auth for preflight. Exception handler outermost to catch all.

**Architect:** Document middleware pipeline diagram per environment — dev vs prod differ (HSTS, exception detail).

### Architecture Perspective

Wrong middleware order causes 'works locally' auth and CORS bugs — common senior trap question.

### Follow-up Questions

1. **Terminal middleware? — Run, Map, Use when short-circuit — nothing after runs.**
2. **Request buffering? — Enable early if body read multiple times.**

### Common Mistakes in Interviews

- Authorization before Authentication
- CORS after endpoints
- Exception handler innermost — errors escape unhandled

---

## Q016: DI Container Scopes Interview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Dependency Injection |
| **Frequency** | Very Common |

### Question

Explain DI lifetimes in ASP.NET Core: Singleton, Scoped, Transient. Give a dangerous mismatch example.

### Short Answer (30 seconds)

Singleton: one instance app-wide. Scoped: per request (DbContext). Transient: new each resolve. Danger: injecting Scoped `DbContext` into Singleton — captive dependency, stale context, thread-safety bugs.

### Detailed Answer (3–5 minutes)

**Lifetime rules:**
- `DbContext` → **Scoped**
- Stateless services → Singleton OK
- Lightweight helpers → Transient

**Captive dependency:**
```csharp
// BAD: Singleton holds Scoped DbContext
services.AddSingleton<ICacheWarmup, CacheWarmup>(); // ctor takes DbContext
```

**Fix:** `IServiceScopeFactory` to create scope inside singleton background work.

**Hosted services:** Create scope per iteration:
```csharp
using var scope = _scopeFactory.CreateScope();
var db = scope.ServiceProvider.GetRequiredService<AppDbContext>();
```

**Architect:** Validate lifetimes in code review checklist — static analysis catches some mismatches.

### Architecture Perspective

Scope mistakes cause production-only concurrency bugs — classic staff-level .NET question.

### Follow-up Questions

1. ** IDisposable singleton? — Rare — ensure thread-safe or use scoped.**
2. **HttpClient? — IHttpClientFactory — not new HttpClient per request.**

### Common Mistakes in Interviews

- Singleton injecting DbContext
- Transient DbContext per resolve
- Background service without scope factory

---

## Q017: Minimal API Production

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | ASP.NET Core |
| **Frequency** | Common |

### Question

When are Minimal APIs appropriate for production and what structure do you add at scale?

### Short Answer (30 seconds)

Minimal APIs suit micro-endpoints, internal tools, and BFFs with low ceremony. At scale add: endpoint groups, filters, validation, OpenAPI, auth policies, and separate handlers — don't put business logic inline.

### Detailed Answer (3–5 minutes)

**Production structure:**
```csharp
var orders = app.MapGroup("/orders").RequireAuthorization();
orders.MapPost("/", CreateOrder.Handle)
  .AddEndpointFilter<ValidationFilter<CreateOrderRequest>>();
```

**Add:**
- Carter/vertical slices or MediatR handlers
- `ProblemDetails` exception handling
- API versioning
- Rate limiting (.NET 7+)

**When MVC instead:** Complex model binding, Razor, filter ecosystems teams already know.

**Architect:** Minimal vs controllers is team consistency — not religion.

### Architecture Perspective

Minimal APIs are production-ready with discipline — interview tests whether you know the guardrails.

### Follow-up Questions

1. **Endpoint filters vs middleware? — Filters per-route; middleware pipeline-wide.**
2. **Testability? — WebApplicationFactory integration tests same as controllers.**

### Common Mistakes in Interviews

- 500-line lambda in Program.cs
- No auth on internal 'temp' endpoints
- Skipping OpenAPI on public APIs

---

## Q018: API Controller Fat vs Thin

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | API Design |
| **Frequency** | Very Common |

### Question

Fat controller vs thin controller — where should logic live in a .NET API?

### Short Answer (30 seconds)

Thin controllers: validate input, call application service/handler, map response. Fat controllers mix HTTP, business rules, and data access — untestable and duplicated across endpoints.

### Detailed Answer (3–5 minutes)

**Thin:**
```csharp
[HttpPost]
public async Task<IActionResult> Create(CreateOrderDto dto)
  => Ok(await _mediator.Send(new CreateOrderCommand(dto)));
```

**Layers:**
- Controller — HTTP concerns
- Application — use cases, orchestration
- Domain — invariants, entities
- Infrastructure — EF, messaging

**Fat smell:** `if (user.IsPremium && order.Total > 100)` in controller.

**Architect:** Vertical slice folders (`Features/Orders/Create`) colocate handler + validator + endpoint — thin surface, cohesive module.

### Architecture Perspective

Thin controllers enable MediatR/CQRS and consistent cross-cutting — architecture not MVC trivia.

### Follow-up Questions

1. **MediatR worth it? — Valuable at 20+ endpoints with shared pipelines.**
2. **Exception handling in controller? — Global middleware — not try/catch per action.**

### Common Mistakes in Interviews

- Business rules in controller actions
- Direct DbContext in controller
- Duplicate validation in every action

---

## Q019: DTO vs Domain Model

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | API Design |
| **Frequency** | Very Common |

### Question

When use DTOs vs domain entities in API contracts?

### Short Answer (30 seconds)

Never expose domain entities directly on APIs — use DTOs/records to control shape, versioning, and prevent over-posting and lazy-load serialization leaks.

### Detailed Answer (3–5 minutes)

**DTO benefits:**
- Hide internal fields (`PasswordHash`, navigation props)
- Stable contract when domain refactors
- Input validation on dedicated request types
- Prevent mass assignment attacks

**Mapping:** Mapster, AutoMapper, or manual `ToDto()` in application layer.

**Read models:** Separate query DTOs optimized for UI — not reused for writes.

**Architect:** Version DTOs (`CreateOrderV2Request`) — domain can evolve independently. Document breaking change policy.

### Architecture Perspective

DTO boundary is API security and evolution — entities over the wire is a red flag.

### Follow-up Questions

1. **Record DTOs? — Immutable request types — great for Minimal APIs.**
2. **Bidirectional mapping leaks? — Map inbound DTO to command — don't round-trip entity.**

### Common Mistakes in Interviews

- Return EF entities with circular references
- Same model for read and write on complex aggregates
- AutoMapper config untested — silent null mapping

---

## Q020: Validation Pipeline

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | ASP.NET Core |
| **Frequency** | Common |

### Question

Design validation for ASP.NET Core APIs — where does it run?

### Short Answer (30 seconds)

Use FluentValidation or DataAnnotations + `IValidatableObject`, executed via filter or MediatR pipeline behavior before handler. Domain validation stays in domain for invariants.

### Detailed Answer (3–5 minutes)

**Layers:**
1. **Request validation** — format, required fields (`FluentValidation`)
2. **Domain validation** — business rules (`OrderCannotExceedCreditLimit`)
3. **Database constraints** — last line of defense

**Pipeline:**
```csharp
public class ValidationBehavior<TReq,TRes> : IPipelineBehavior<TReq,TRes> {
  // run validators before handler
}
```

**ProblemDetails:** Return 400 with field errors — RFC 7807.

**Architect:** Single validation path — not duplicated in controller and service.

### Architecture Perspective

Validation pipeline shows clean architecture layering — not just attributes on DTOs.

### Follow-up Questions

1. **FluentValidation vs DataAnnotations? — Fluent for complex rules; annotations for simple.**
2. **Client-side only validation? — Never sufficient — always server validate.**

### Common Mistakes in Interviews

- Validation only in UI
- Business rules in FluentValidation that belong in domain
- 500 instead of 400 on validation failure

---

## Q021: Exception Handling Middleware

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | ASP.NET Core |
| **Frequency** | Very Common |

### Question

How implement global exception handling in ASP.NET Core for APIs?

### Short Answer (30 seconds)

Use exception handling middleware or `IExceptionHandler` (.NET 8+) returning `ProblemDetails` — map domain exceptions to 400/404/409, log 500 with correlation ID, never leak stack traces in prod.

### Detailed Answer (3–5 minutes)

**Pattern:**
```csharp
app.UseExceptionHandler(app => app.Run(async ctx => {
  var ex = ctx.Features.Get<IExceptionHandlerFeature>()?.Error;
  var (status, title) = ex switch {
    NotFoundException => (404, "Not Found"),
    ValidationException => (400, "Validation Failed"),
    _ => (500, "Internal Server Error")
  };
  await Results.Problem(title: title, statusCode: status).ExecuteAsync(ctx);
}));
```

**Log:** Structured log with traceId, userId, exception type — not full PII.

**Architect:** Exception taxonomy per bounded context — avoid catching `Exception` in business code.

### Architecture Perspective

Global handler is production hygiene — consistent errors and safe leakage policy.

### Follow-up Questions

1. **Developer exception page in prod? — Never — security and noise.**
2. **Exception as flow control? — Use Result pattern for expected failures.**

### Common Mistakes in Interviews

- try/catch in every controller method
- Stack trace returned to mobile clients
- Swallowing exceptions without logging

---

## Q022: Logging Correlation ID

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Observability |
| **Frequency** | Very Common |

### Question

How propagate correlation IDs across ASP.NET Core services?

### Short Answer (30 seconds)

Accept `X-Correlation-ID` header or generate on entry, store in `Activity`/scoped service, enrich Serilog `LogContext`, forward on HttpClient calls and message bus headers.

### Detailed Answer (3–5 minutes)

**Implementation:**
1. Middleware reads/generates correlation ID
2. `using (LogContext.PushProperty("CorrelationId", id))`
3. `Activity.Current` for OpenTelemetry trace ID alignment
4. `HttpClient` delegating handler adds header to downstream calls
5. MassTransit/RabbitMQ header propagation

**ASP.NET:** `services.AddHttpContextAccessor()` + middleware sets `Items["CorrelationId"]`.

**Architect:** Correlate logs, traces, and support tickets — same ID end-to-end. Dashboard filter by correlation ID for incident triage.

### Architecture Perspective

Correlation ID is minimum viable observability for distributed .NET — must mention outbound propagation.

### Follow-up Questions

1. **TraceId vs CorrelationId? — Often same or mapped — align with OpenTelemetry.**
2. **Missing on async boundaries? — Flow through `AsyncLocal` or Activity.**

### Common Mistakes in Interviews

- Correlation ID only in first service
- Random GUID per log line
- Not returning correlation ID in error response body

---

## Q023: HttpClient DNS Issue

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | HTTP |
| **Frequency** | Very Common |

### Question

Explain the HttpClient DNS staleness problem and the fix in .NET.

### Short Answer (30 seconds)

`new HttpClient()` per request exhausts sockets; singleton `HttpClient` caches DNS forever — stale IPs after scale-out/failover. Fix: `IHttpClientFactory` with configurable handler lifetime (~2–5 min PooledConnectionLifetime).

### Detailed Answer (3–5 minutes)

**Problems:**
- **Dispose per use** — socket exhaustion (SNAT port exhaustion in Azure)
- **Static HttpClient** — DNS not refreshed when K8s service IPs change

**Fix:**
```csharp
services.AddHttpClient<IPaymentClient, PaymentClient>(c => {
  c.BaseAddress = new Uri("https://payments");
}).ConfigurePrimaryHttpMessageHandler(() => new SocketsHttpHandler {
  PooledConnectionLifetime = TimeSpan.FromMinutes(2)
});
```

**Architect:** Always register typed clients in DI — document in coding standards. Load test validates no socket leak.

### Architecture Perspective

Classic .NET production footgun — IHttpClientFactory is the expected senior answer.

### Follow-up Questions

1. **Polly with HttpClient? — AddPolicyHandler on named client — retry/timeout.**
2. **gRPC same issue? — Channel lifetime management — don't channel per call.**

### Common Mistakes in Interviews

- new HttpClient() in using block per request
- Static HttpClient never recycled
- Ignoring SNAT limits in Azure App Service

---

## Q024: Polly Retry Interview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Resilience |
| **Frequency** | Very Common |

### Question

How configure Polly retry for HTTP calls — what should you avoid?

### Short Answer (30 seconds)

Retry transient failures (408, 429, 5xx) with exponential backoff + jitter, max 3 attempts, only on idempotent operations or with idempotency keys. Never blind retry POST payments without dedup.

### Detailed Answer (3–5 minutes)

**Policy:**
```csharp
Policy.Handle<HttpRequestException>()
  .OrResult(r => (int)r.StatusCode >= 500)
  .WaitAndRetryAsync(3, attempt =>
    TimeSpan.FromSeconds(Math.Pow(2, attempt)) + Jitter());
```

**Combine:** Retry wrapped by circuit breaker and timeout — timeout innermost.

**429:** Respect `Retry-After` header.

**Architect:** Idempotency-Key header on mutating APIs — enable safe retry. Monitor retry storms — they amplify outages.

### Architecture Perspective

Polly interview tests idempotency awareness — retry without it is a money bug.

### Follow-up Questions

1. **Circuit breaker when? — After sustained failures — fail fast — protect downstream.**
2. **Hedging? — Rare — duplicate requests — only if explicitly safe.**

### Common Mistakes in Interviews

- Retry non-idempotent POST unlimited
- No jitter — thundering herd on recovery
- Retry inside retry across service layers

---

## Q025: Caching Interview Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Caching |
| **Frequency** | Very Common |

### Question

Compare cache-aside, read-through, write-through, and write-behind for .NET APIs.

### Short Answer (30 seconds)

Cache-aside: app reads cache, on miss loads DB and populates — most common with Redis. Read-through: cache library loads. Write-through: sync write cache+DB. Write-behind: async DB write — higher throughput, data loss risk.

### Detailed Answer (3–5 minutes)

| Pattern | Pros | Cons |
|---------|------|------|
| Cache-aside | Simple, app control | Stampede risk, stale data |
| Read-through | Centralized load | Cache vendor lock-in |
| Write-through | Consistent | Write latency |
| Write-behind | Fast writes | Durability window |

**.NET:** `IDistributedCache` + Redis, `IMemoryCache` for local L1.

**Architect:** TTL + invalidation on write. Hot keys — shard or local L1. Never cache auth tokens or personalized medical data without policy review.

### Architecture Perspective

Caching pattern choice affects consistency and incident behavior — go beyond 'use Redis'.

### Follow-up Questions

1. **Cache stampede? — Mutex, early expiration, probabilistic refresh.**
2. **HybridCache (.NET 9)? — L1+L2 built-in — simplifies two-tier.**

### Common Mistakes in Interviews

- Cache everything with no TTL
- Distributed cache for single-server app unnecessarily
- No cache invalidation on update

---

## Q026: Design Pattern Factory

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Design Patterns |
| **Frequency** | Common |

### Question

When use Factory Method vs Abstract Factory in .NET?

### Short Answer (30 seconds)

Factory Method: subclass or delegate decides which product to create (`IFileParserFactory.Create(extension)`). Abstract Factory: family of related products (`IUiFactory` → WinButton + WinCheckbox). Use when creation logic is complex or config-driven.

### Detailed Answer (3–5 minutes)

**Factory Method example:**
```csharp
public interface INotificationFactory {
  INotifier Create(NotificationChannel channel);
}
```

**Abstract Factory:** Theme kits — all controls match skin.

**DI as factory:** `IServiceProvider.GetRequiredService<T>()` — prefer when types known at compile time use straight DI.

**Architect:** Factory for plugin systems and multi-tenant provider selection — not for every `new`.

### Architecture Perspective

Pattern interview: connect to DI and plugin registration — not Gang of Four recitation.

### Follow-up Questions

1. **Simple Factory vs static? — Inject factory interface — testable.**
2. **Options pattern? — Configuration-driven factory selection.**

### Common Mistakes in Interviews

- Factory for every object creation
- Service locator disguised as factory
- Abstract factory when one product type

---

## Q027: Strategy Pattern Example

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Design Patterns |
| **Frequency** | Common |

### Question

Give a Strategy pattern example in .NET enterprise code.

### Short Answer (30 seconds)

Encapsulate interchangeable algorithms — `IShippingCalculator` implementations (Standard, Express, Overnight) selected at runtime by rule engine or customer tier.

### Detailed Answer (3–5 minutes)

```csharp
public interface IShippingStrategy {
  decimal Calculate(Order order);
}
// DI: services.AddScoped<IShippingStrategy, ExpressShipping>();
// Or keyed services (.NET 8): keyed by enum
```

**vs if/else:** Open for new carriers without editing `CheckoutService`.

**Real-world:** Payment providers (`IPaymentGateway`), tax by jurisdiction, discount rules.

**Architect:** Store strategy key in DB/config — enable ops to switch without deploy.

### Architecture Perspective

Strategy maps to business variability — interviewers want runtime selection story.

### Follow-up Questions

1. **Strategy vs Chain of Responsibility? — Chain passes along until handled; strategy picks one.**
2. **Rules engine? — Drools/Azure Logic Apps for complex rule sets.**

### Common Mistakes in Interviews

- switch on string for every new variant
- Strategy with static global state
- No default/fallback strategy

---

## Q028: Observer Events .NET

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Design Patterns |
| **Frequency** | Common |

### Question

How do events and observer pattern work in .NET — and when prefer messaging?

### Short Answer (30 seconds)

In-process: C# `event`, `IObservable<T>`, or MediatR notifications for domain events within monolith. Cross-service: message bus (Service Bus, Kafka) — not .NET events.

### Detailed Answer (3–5 minutes)

**In-process:**
```csharp
public class Order {
  public event EventHandler<OrderPlacedArgs> Placed;
}
// Or: await _mediator.Publish(new OrderPlaced(orderId));
```

**Domain events:** Raised on aggregate change, handled after `SaveChanges` in same UoW or via outbox.

**Distributed:** Outbox pattern → Service Bus topic — subscribers decoupled.

**Architect:** Don't use static events in web apps — scoped lifetime issues. Prefer MediatR or explicit dispatcher.

### Architecture Perspective

Observer scope boundary — in-proc vs distributed — is the architect distinction.

### Follow-up Questions

1. **Event vs command? — Event past tense, multiple subscribers; command one handler.**
2. **Ordering guarantees? — In-proc ordered; bus may need partitions.**

### Common Mistakes in Interviews

- Static C# events in ASP.NET request scope
- Synchronous event handler doing HTTP calls
- Missing outbox — dual-write DB and bus

---

## Q029: Decorator Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Design Patterns |
| **Frequency** | Common |

### Question

Explain Decorator pattern with a .NET example.

### Short Answer (30 seconds)

Wrap object to add behavior without subclassing — `CachingRepository` decorates `IOrderRepository`, `LoggingHandler` decorates `HttpMessageHandler`.

### Detailed Answer (3–5 minutes)

```csharp
public class CachingOrderRepository : IOrderRepository {
  private readonly IOrderRepository _inner;
  private readonly IDistributedCache _cache;
  public async Task<Order?> GetAsync(Guid id) {
    var cached = await _cache.GetAsync(id);
    if (cached != null) return cached;
    var order = await _inner.GetAsync(id);
    await _cache.SetAsync(id, order);
    return order;
  }
}
```

**DI registration:** `services.Decorate<IOrderRepository, CachingOrderRepository>()` (Scrutor).

**Architect:** Cross-cutting concerns (cache, audit, retry) as decorators — keeps core clean.

### Architecture Perspective

Decorator is the structural pattern behind HttpClient handlers and Scrutor — practical .NET.

### Follow-up Questions

1. **Decorator vs middleware? — Similar — middleware is pipeline decorator for HTTP.**
2. **Too many layers? — Watch debug difficulty — limit stack depth.**

### Common Mistakes in Interviews

- Subclass explosion instead of wrap
- Decorator changing interface contract
- Order of decorators matters — document

---

## Q030: Interview Coding Communication

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Interview Skills |
| **Frequency** | Very Common |

### Question

How communicate effectively during a live coding interview in .NET?

### Short Answer (30 seconds)

Think aloud: restate problem, clarify inputs/edge cases, propose approach and complexity, code incrementally, test with example, discuss trade-offs. Silence is worse than wrong direction with correction.

### Detailed Answer (3–5 minutes)

**Structure (25–35 min):**
1. **Clarify** (3 min) — nulls, scale, duplicates
2. **Approach** (5 min) — brute force then optimize
3. **Code** (15 min) — meaningful names, small methods
4. **Test** (5 min) — walk through example + edge case
5. **Optimize** (5 min) — time/space, .NET collections choice

**Phrases:** 'I'll use Dictionary for O(1) lookup because...' 'Trade-off: memory for speed.'

**Architect angle:** Mention production concerns — thread safety, testability — even if not asked.

### Architecture Perspective

Communication is scored equally to correctness at senior levels — practice narration.

### Follow-up Questions

1. **Stuck? — Say so, ask hint, try simpler subproblem.**
2. **Finish early? — Discuss monitoring, API shape, failure modes.**

### Common Mistakes in Interviews

- Silent coding for 20 minutes
- Jump to code without examples
- Argue with interviewer instead of incorporating hints

---
