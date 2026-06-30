# Month 1 Top 50 — Part 2 (Q009–Q030)

> **.NET Runtime, DI, SOLID, Clean Architecture** | Weeks 2–3 | [Part 1](month-01-top-50-part1.md) | [Part 3](month-01-top-50-part3.md) | [Index](month-01-top-50-index.md)

---

## Q009: Dependency Injection Lifetimes

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | .NET / DI |
| **Week** | 02 |

### Question

Explain Singleton, Scoped, and Transient lifetimes. What goes wrong when you get them wrong?

### Short Answer (30 seconds)

Singleton: one instance per app — for stateless services, caches, config. Scoped: one per request — DbContext, unit of work. Transient: new every injection — lightweight stateless helpers. Captive dependency: injecting Scoped into Singleton causes stale DbContext or memory leaks.

### Detailed Answer (3–5 minutes)

| Lifetime | Created | Disposed | Example |
|----------|---------|----------|---------|
| Singleton | App start | App shutdown | `IMemoryCache`, `HttpClient` via factory |
| Scoped | Per request/scope | End of scope | `DbContext`, `IUnitOfWork` |
| Transient | Each resolve | After use | `IValidator<T>` |

**Captive dependency bug:** `Singleton<OrderService>` depending on `Scoped<AppDbContext>` — DbContext lives for app lifetime, not request. Fix: make service Scoped or use `IServiceScopeFactory`.

**Architect:** Document lifetime rules in platform template; analyze with `ValidateOnBuild` and `ValidateScopes`.

### Follow-up Questions

1. **Background service needs DbContext?** Create scope per message: `using var scope = _scopeFactory.CreateScope()`.
2. **Singleton with state?** Thread-safe or avoid — prefer immutable state.

### Common Mistakes in Interviews

- DbContext as Singleton
- Transient for everything "to be safe" — allocation overhead

---

## Q010: ASP.NET Core Request Pipeline

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | ASP.NET Core |
| **Week** | 02 |

### Question

Describe the ASP.NET Core middleware pipeline. Where do architects place cross-cutting concerns?

### Short Answer (30 seconds)

Request flows through middleware chain: exception handling → HTTPS → auth → routing → endpoints. Order matters. Cross-cutting: logging, correlation ID, auth, rate limiting early; caching after auth when user-specific.

### Detailed Answer (3–5 minutes)

```csharp
app.UseExceptionHandler();
app.UseHttpsRedirection();
app.UseMiddleware<CorrelationIdMiddleware>();
app.UseAuthentication();
app.UseAuthorization();
app.MapControllers();
```

**Architect decisions:**
- Global exception handler returns ProblemDetails (RFC 7807)
- Correlation ID before logging middleware
- Rate limiting after auth if per-user limits

**Minimal APIs vs MVC:** Same pipeline; controllers add filter pipeline layer.

### Common Mistakes in Interviews

- Auth after endpoint execution
- No centralized exception handling

---

## Q011: Configuration and Options Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | .NET Configuration |
| **Week** | 02 |

### Question

How should configuration be structured in a 12-factor .NET application?

### Short Answer (30 seconds)

`IOptions<T>` / `IOptionsMonitor<T>` for typed settings from environment variables, Key Vault, appsettings per environment. No secrets in appsettings.json in repo. Validate options at startup with `IValidateOptions<T>`.

### Detailed Answer (3–5 minutes)

**Hierarchy:** appsettings.json → appsettings.{Environment}.json → environment variables → Key Vault (highest).

**Options pattern:**
```csharp
builder.Services.Configure<PaymentOptions>(
    builder.Configuration.GetSection("Payment"));
```

**Architect:** `IOptionsMonitor` for reload without restart. Fail fast on invalid config at startup.

### Common Mistakes

- Connection strings in source control
- Reading `IConfiguration` directly everywhere instead of typed options

---

## Q012: Minimal APIs vs MVC Controllers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | ASP.NET Core |
| **Week** | 02 |

### Question

When do you choose Minimal APIs vs MVC controllers for a new .NET service?

### Short Answer (30 seconds)

Minimal APIs for small microservices, low ceremony, performance-sensitive simple endpoints. MVC for complex validation, filters, versioning, teams familiar with controller patterns, and large APIs needing conventions.

### Detailed Answer (3–5 minutes)

| Factor | Minimal APIs | MVC |
|--------|--------------|-----|
| Team familiarity | Modern/small teams | Enterprise .NET shops |
| Cross-cutting | Manual middleware | Action filters |
| OpenAPI | Built-in | Swashbuckle same |
| Testability | Handler delegates | Controller unit tests |

**Architect:** Consistency across org matters more than marginal perf — pick one per platform golden path.

### Common Mistakes

- "Minimal APIs always better" without team/governance context

---

## Q013: Single Responsibility Principle

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | SOLID |
| **Week** | 03 |

### Question

Explain SRP. Give an example of a violation and refactor.

### Short Answer (30 seconds)

A class should have one reason to change — one actor/stakeholder. Violation: `OrderService` that validates, persists, sends email, and generates PDF. Refactor: separate validators, repository, notification handler.

### Detailed Answer (3–5 minutes)

SRP is about **change drivers**, not "one method." If marketing changes email format and finance changes PDF layout, two reasons to change one class.

**Architect lens:** Microservice boundaries often align with SRP at service level — but don't split into 50 services for every class.

### Common Mistakes

- Every class with 2 methods violates SRP — over-fragmentation
- God service that does everything

---

## Q014: Open/Closed Principle

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SOLID |
| **Week** | 03 |

### Question

How does OCP apply to payment provider integration?

### Short Answer (30 seconds)

Extend behavior without modifying existing code — `IPaymentProvider` with Stripe, PayPal implementations. New provider = new class + DI registration, not editing switch statements.

### Detailed Answer (3–5 minutes)

```csharp
public interface IPaymentProvider { Task<Result> ChargeAsync(Payment p); }
// StripeProvider, PayPalProvider — register in DI
```

**Strategy pattern** implements OCP. Architect reviews PRs for growing `switch` on provider type — refactor to polymorphism.

### Common Mistakes

- Modifying core service for every new payment method

---

## Q015: Liskov Substitution Principle

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SOLID |
| **Week** | 03 |

### Question

Give an example of an LSP violation in a .NET codebase.

### Short Answer (30 seconds)

Subclass that throws `NotSupportedException` on base method — e.g., `ReadOnlyCollection` overriding `Add`. Clients expecting base behavior break. Fix: separate interfaces (`IReadOnlyRepository` vs `IRepository`).

### Detailed Answer (3–5 minutes)

LSP: subtypes must be substitutable without breaking callers. Violations cause runtime surprises.

**Architect:** Prefer composition and role interfaces over deep inheritance hierarchies in domain models.

### Common Mistakes

- Deep inheritance trees in enterprise domains

---

## Q016: Interface Segregation Principle

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SOLID |
| **Week** | 03 |

### Question

Why is `IUserRepository` with 20 methods a problem? How do you fix it?

### Short Answer (30 seconds)

Clients depend on methods they don't use — fat interfaces force implementers to stub methods. Split into `IUserReader`, `IUserWriter`, `IUserAdmin` — clients take only what they need.

### Detailed Answer (3–5 minutes)

ISP reduces coupling and makes testing easier — mock only relevant methods.

**EF Core note:** Don't expose `DbContext` as interface with 100 methods — repository per aggregate or use specification pattern.

### Common Mistakes

- One giant `IService` interface per domain

---

## Q017: Dependency Inversion Principle

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SOLID |
| **Week** | 03 |

### Question

How does DIP relate to Clean Architecture?

### Short Answer (30 seconds)

High-level modules depend on abstractions; low-level modules implement them. Domain defines `IOrderRepository`; Infrastructure implements SQL version. Dependencies point inward toward domain.

### Detailed Answer (3–5 minutes)

Clean Architecture layers:
- **Domain** — entities, interfaces (ports)
- **Application** — use cases
- **Infrastructure** — adapters (EF, HTTP)
- **API** — composition root, DI wiring

**Architect:** Enforce with architecture tests (NetArchTest) — domain must not reference infrastructure.

### Common Mistakes

- Domain project referencing EF Core packages

---

## Q018: Clean Architecture vs Vertical Slice

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Architecture |
| **Week** | 03 |

### Question

Compare Clean Architecture layers vs Vertical Slice architecture.

### Short Answer (30 seconds)

Clean Architecture: horizontal layers (domain, app, infra). Vertical Slice: organize by feature (`Features/Orders/CreateOrder.cs` with handler, validator, endpoint together). Vertical slice scales better for feature teams; Clean Architecture clearer for strict domain isolation.

### Detailed Answer (3–5 minutes)

| Approach | Pros | Cons |
|----------|------|------|
| Clean Architecture | Clear boundaries, testable domain | Cross-layer navigation for simple features |
| Vertical Slice (MediatR) | Feature cohesion, faster delivery | Risk of anemic domain if discipline slips |

**Architect:** Hybrid common — vertical slices in application layer, domain stays pure.

### Common Mistakes

- Cargo cult Clean Architecture with empty domain and all logic in services

---

## Q019: CQRS — When to Use

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Architecture |
| **Week** | 03 |

### Question

When should you apply CQRS? When is it overkill?

### Short Answer (30 seconds)

Use when read and write models differ significantly — different scale, shape, or storage. Overkill for simple CRUD with same model. Full CQRS with separate databases adds complexity — justify with read/write scale mismatch.

### Detailed Answer (3–5 minutes)

**Good fit:** 100:1 read/write ratio, complex reports vs simple writes, event sourcing.

**Overkill:** Internal admin CRUD with 10 users.

**Architect:** Start with logical CQRS (separate query handlers) before separate databases.

### Common Mistakes

- CQRS + separate DB on day one for every microservice

---

## Q020: MediatR and Application Layer

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | .NET Patterns |
| **Week** | 03 |

### Question

What role does MediatR play in enterprise .NET APIs?

### Short Answer (30 seconds)

MediatR dispatches commands/queries to handlers — thin controllers, pipeline behaviors for logging, validation, transactions. Architect standardizes cross-cutting in behaviors instead of filters scattered per controller.

### Detailed Answer (3–5 minutes)

```csharp
public record CreateOrderCommand(...) : IRequest<OrderId>;
// Handler + FluentValidation + TransactionBehavior
```

**Trade-off:** Indirection — new developers need onboarding. Worth it at 20+ endpoint services.

### Common Mistakes

- MediatR for 3-endpoint microservice — unnecessary

---

## Q021–Q030: Rapid Review

### Q021: Domain vs Application vs Infrastructure?
**Domain** = business rules. **Application** = orchestration. **Infrastructure** = EF, email, HTTP. Dependencies inward.

### Q022: Repository pattern — always?
No — EF Core `DbContext` is already a repository/unit of work. Add repository when you need abstraction over ORM or test seams at scale.

### Q023: Unit of Work?
Coordinates multiple repository operations in one transaction — `DbContext.SaveChangesAsync()` is UoW.

### Q024: Anemic domain model?
Entities with only properties, logic in services — avoid; put behavior on entities where it belongs.

### Q025: Bounded context in monolith?
Separate .NET projects per context — `Ordering.Domain`, `Billing.Domain` — before splitting to microservices.

### Q026: Validation — where?
Input validation at API (FluentValidation). Invariant validation in domain entities.

### Q027: Exception handling strategy?
Domain exceptions → ProblemDetails mapping. Never expose stack traces to clients.

### Q028: API versioning?
URL (`/v1/`) or header — pick one org standard. Azure APIM can route versions.

### Q029: Health checks?
Liveness vs readiness — readiness includes DB. K8s uses both probes differently.

### Q030: Architect reviewing PR for SOLID?
Look for: new switch on type, domain referencing infra, god classes, captive DI dependencies.

---

**Navigation:** [Part 3 — Design Patterns](month-01-top-50-part3.md) →
