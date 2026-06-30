# Week 03 — Fundamentals Interview Q&A

> Q001–Q030: Premium format (Week 1 quality).  
> See also: [Interview prep hub](../../../interview-prep/README.md)

---


## Q001: Single Responsibility Principle

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | SOLID |
| **Frequency** | Very Common |

### Question

Explain SRP and how you enforce it at architecture level.

### Short Answer (30 seconds)

A module should have one reason to change. At architecture level: separate pricing, persistence, and notification — not one `OrderService` doing everything.

### Detailed Answer (3–5 minutes)

**Code:** `OrderPricingService`, `OrderRepository`, `OrderNotificationService` — each changes for different business reasons.

**Architect:** SRP drives microservice boundaries — if two teams change the same class for different reasons, split it.

**Measure:** Class cohesion metrics, change-frequency heat maps in git.

### Architecture Perspective

SRP is the most cited SOLID principle in architect interviews.

### Follow-up Questions

1. **SRP vs microservices? — SRP informs boundaries; not one service per class.**
2. **How small is too small? — When abstraction cost exceeds benefit.**

### Common Mistakes in Interviews

- God service with 40 methods
- Splitting every class into one method
- SRP only at class level ignoring module boundaries

---

## Q002: Open/Closed Principle

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | SOLID |
| **Frequency** | Very Common |

### Question

Give a production OCP example in C# enterprise code.

### Short Answer (30 seconds)

Open for extension, closed for modification. Add new discount types via `IDiscountStrategy` — don't edit `PricingService` switch.

### Detailed Answer (3–5 minutes)

```csharp
public interface IDiscountStrategy { decimal Apply(Order o); }
// New VIP discount = new class, register in DI
```

**Architect:** Plugin architectures, rule engines, strategy pattern for tax jurisdictions.

**Avoid:** Abstract factory explosion for 2 variants.

### Architecture Perspective

OCP enables safe extension without regression risk.

### Follow-up Questions

1. **Switch expressions vs OCP? — Closed set use switch; open set use strategy.**
2. **Feature flags vs OCP? — Flags for release; OCP for permanent variants.**

### Common Mistakes in Interviews

- Modify switch every new discount type
- Interface for single implementation
- OCP via copy-paste inheritance

---

## Q003: Liskov Substitution Principle

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | SOLID |
| **Frequency** | Common |

### Question

What is an LSP violation in a .NET API?

### Short Answer (30 seconds)

Subtype must honor parent contract. Override that throws `NotSupportedException` or tightens preconditions = LSP violation.

### Detailed Answer (3–5 minutes)

**Classic:** Square/Rectangle. **Enterprise:** `ReadOnlyCollection` wrapping list but exposing Add via cast.

**Architect:** Favor composition over inheritance when behavior diverges. Code review flags `throw new NotSupportedException()` in overrides.

### Architecture Perspective

LSP protects polymorphism reliability.

### Follow-up Questions

1. **Bird extends Animal flies? — Ostrich LSP teaching example.**
2. **Contract testing subtypes? — Consumer tests against interface.**

### Common Mistakes in Interviews

- Subclass narrows input acceptance
- Override changes expected side effects
- Inheritance where composition fits

---

## Q004: Interface Segregation Principle

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | SOLID |
| **Frequency** | Common |

### Question

ISP at microservice API level — example?

### Short Answer (30 seconds)

Clients shouldn't depend on methods they don't use. Split fat `IOrderService` into `IOrderReader` and `IOrderWriter`; BFF exposes only needed endpoints.

### Detailed Answer (3–5 minutes)

**API design:** Mobile BFF returns 5 fields; admin API returns full order — different interfaces not one bloated DTO for all.

**Architect:** Segregate NuGet package interfaces — consumers reference slim abstractions.

### Architecture Perspective

ISP reduces coupling and accidental API misuse.

### Follow-up Questions

1. **Role interfaces in C#? — Implicit segregation pattern.**
2. **GraphQL vs ISP? — Clients select fields — different approach.**

### Common Mistakes in Interviews

- IFatRepository with 30 methods
- Mobile client forced to reference admin API
- One DTO for all clients forever

---

## Q005: Dependency Inversion Principle

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | SOLID |
| **Frequency** | Very Common |

### Question

How does DIP relate to DI containers in .NET?

### Short Answer (30 seconds)

High-level modules depend on abstractions; low-level implements them. DI container wires `IOrderRepository` → `SqlOrderRepository`.

### Detailed Answer (3–5 minutes)

**Architect mandates:** Domain/application define interfaces; infrastructure implements. No `new SqlConnection` in handlers.

**Testability:** Mock abstractions in unit tests.

**Composition root:** `Program.cs` or extension method registers implementations.

### Architecture Perspective

DIP + DI is foundation of testable .NET architecture.

### Follow-up Questions

1. **DIP without DI container? — Manual composition root still valid.**
2. **Primary constructors affect DIP? — Still inject abstractions.**

### Common Mistakes in Interviews

- Application references SqlClient
- Concrete classes in domain layer
- Service locator instead of constructor injection

---

## Q006: Clean Architecture Layers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Clean Arch |
| **Frequency** | Very Common |

### Question

Name the layers and dependency direction in Clean Architecture.

### Short Answer (30 seconds)

Domain (center) → Application → Infrastructure/Presentation outward. Dependencies point inward only.

### Detailed Answer (3–5 minutes)

| Layer | Contains |
|-------|----------|
| Domain | Entities, value objects, domain events |
| Application | Use cases, handlers, ports |
| Infrastructure | EF, HTTP clients, messaging |
| Presentation | API, UI |

**Architect:** Enforce with NetArchTest in CI.

### Architecture Perspective

Layer violations are architect review red flags.

### Follow-up Questions

1. **Onion vs Clean vs Hexagonal? — Same dependency rule, different names.**
2. **Shared kernel between layers? — Only value objects cross carefully.**

### Common Mistakes in Interviews

- Domain references EF Core
- Controller calls DbContext directly
- Circular project references

---

## Q007: Vertical Slice Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Architecture |
| **Frequency** | Common |

### Question

Vertical slice vs horizontal layers — when choose vertical?

### Short Answer (30 seconds)

Vertical: organize by feature (`Features/Orders/Create`). Horizontal: by technical concern (`Controllers/`, `Services/`).

### Detailed Answer (3–5 minutes)

**Choose vertical when:** Feature teams ship independently, codebase large, change isolation matters.

**Choose horizontal when:** Small team, simple CRUD, everyone owns all layers.

**Architect:** MediatR handlers natural fit for slices.

### Architecture Perspective

Slice architecture matches agile delivery.

### Follow-up Questions

1. **Shared infrastructure slice? — Cross-cutting in `/Infrastructure` folder.**
2. **Slice boundaries = microservice boundaries? — Good stepping stone.**

### Common Mistakes in Interviews

- 500-file Services folder
- Duplicate validation per slice unchecked
- No shared kernel discipline

---

## Q008: CQRS — When to Introduce

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | CQRS |
| **Frequency** | Common |

### Question

When introduce CQRS in enterprise .NET system?

### Short Answer (30 seconds)

When read and write models diverge — complex reports, different scale, different storage optimization. Not day-one for simple CRUD.

### Detailed Answer (3–5 minutes)

**Start logical:** Separate query handlers from commands; same DB OK.

**Physical split:** When read replicas or Elasticsearch projection justified by metrics.

**Architect:** Measure read:write ratio and query complexity before physical CQRS.

### Architecture Perspective

CQRS is scaling tool not mandatory pattern.

### Follow-up Questions

1. **CQRS without event sourcing? — Common and valid.**
2. **Read model rebuild strategy? — From events or DB snapshot.**

### Common Mistakes in Interviews

- CQRS two databases for 100 users
- Duplicate business rules read/write
- Confuse CQRS with CRUD renaming

---

## Q009: MediatR — Pros and Cons

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Patterns |
| **Frequency** | Common |

### Question

MediatR in Clean Architecture — benefits and drawbacks?

### Short Answer (30 seconds)

Pros: decoupled handlers, pipeline behaviors, one class per use case. Cons: indirection, magic for juniors, assembly scanning perf negligible.

### Detailed Answer (3–5 minutes)

**Architect adoption:** Standard in enterprise .NET templates — document handler conventions.

**Pipeline:** Validation, logging, transactions as behaviors.

**Alternative:** Direct handler injection without MediatR for tiny apps.

### Architecture Perspective

MediatR is organizational pattern as much as technical.

### Follow-up Questions

1. **MediatR vs custom mediator? — Roll own if 3 handlers only.**
2. **Notification vs request? — Events in-process via notifications.**

### Common Mistakes in Interviews

- MediatR for every GET trivial
- Handler calls handler bypassing mediator
- No pipeline behavior standards

---

## Q010: Anemic vs Rich Domain Model

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DDD |
| **Frequency** | Very Common |

### Question

Anemic domain model — problem and fix?

### Short Answer (30 seconds)

Anemic: entities are data bags; all logic in services. Rich: entities enforce invariants (`order.Confirm()`).

### Detailed Answer (3–5 minutes)

**Problem:** Business rules scattered, duplication, hard to test domain in isolation.

**Fix:** Move behavior to aggregates; application layer orchestrates only.

**Pragmatic:** Not every DTO needs behavior — DTOs anemic OK; aggregates should be rich.

### Architecture Perspective

Domain model style is cultural architect decision.

### Follow-up Questions

1. **Transaction script pattern? — Valid for simple ETL — know trade-off.**
2. **Rich domain with EF change tracking? — Works with careful design.**

### Common Mistakes in Interviews

- OrderService 2000 lines all logic
- Public setters on every entity property
- No domain tests only integration

---

## Q011: Hexagonal Architecture Ports

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Hexagonal |
| **Frequency** | Common |

### Question

Explain ports and adapters in Clean/Hexagonal architecture.

### Short Answer (30 seconds)

Ports are interfaces the application defines (inbound/outbound). Adapters implement them — SQL adapter, REST adapter, message adapter.

### Detailed Answer (3–5 minutes)

**Dependency rule:** Application core depends on port abstractions; infrastructure implements adapters.

**Example:** `IOrderRepository` port, `SqlOrderRepository` adapter.

**Architect:** Enables testing with in-memory adapters; swap ERP adapter without domain change.

### Architecture Perspective

Ports/adapters is interview vocabulary for clean boundaries.

### Follow-up Questions

1. **Driving vs driven ports? — Inbound (API) vs outbound (DB, messaging).**
2. **How many adapters per port? — Multiple implementations valid (cache decorator).**

### Common Mistakes in Interviews

- Domain references SqlClient package
- Adapter leaks EF entities to API
- Port interface mirrors entire database

---

## Q012: Application Layer Use Cases

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Clean Arch |
| **Frequency** | Common |

### Question

What belongs in the application layer?

### Short Answer (30 seconds)

Use case orchestration: command/query handlers, transaction boundaries, authorization checks, DTO mapping — not business rules.

### Detailed Answer (3–5 minutes)

**Contains:** `CreateOrderHandler`, validators, unit of work coordination.

**Not:** HTTP concerns, SQL, domain invariants (those in domain).

**Architect:** Thin handlers — delegate to domain methods.

### Architecture Perspective

Application layer is orchestration not logic dump.

### Follow-up Questions

1. **Application service vs handler? — MediatR handler is application service unit.**
2. **Cross-cutting in behaviors? — Pipeline behaviors for logging/validation.**

### Common Mistakes in Interviews

- Business rules in handler if/else
- DbContext in application layer interface
- God handler 500 lines

---

## Q013: Domain Layer Purity Rules

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DDD |
| **Frequency** | Very Common |

### Question

What must NOT be in the domain layer?

### Short Answer (30 seconds)

No EF attributes, no HTTP, no configuration, no DTOs, no infrastructure interfaces with tech details.

### Detailed Answer (3–5 minutes)

**Domain has:** Entities, value objects, domain events, domain services, repository interfaces (optional purist debate).

**Architect:** Enforce with architecture tests (NetArchTest.Rules).

**Violation smell:** `using Microsoft.EntityFrameworkCore` in Domain project.

### Architecture Perspective

Domain purity enables testability and longevity.

### Follow-up Questions

1. **Anemic domain still in domain project? — Rich behavior required not just POCOs.**
2. **Domain events vs integration events? — Domain inside; integration at boundary.**

### Common Mistakes in Interviews

- EF Core attributes on entities
- HttpClient in domain service
- Domain depends on Infrastructure project

---

## Q014: Infrastructure Layer Boundaries

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Clean Arch |
| **Frequency** | Common |

### Question

Infrastructure layer responsibilities?

### Short Answer (30 seconds)

Implements repositories, EF mappings, external API clients, message publishers, file storage — all driven adapters.

### Detailed Answer (3–5 minutes)

**One Infrastructure project or per-bounded-context?** Start one; split when boundaries clear.

**Architect:** Infrastructure references Application/Domain — never reverse.

### Architecture Perspective

Infrastructure is replaceable detail.

### Follow-up Questions

1. **DbContext location? — Always Infrastructure.**
2. **Integration tests on Infrastructure? — Testcontainers for SQL.**

### Common Mistakes in Interviews

- Business logic in repository
- Infrastructure referenced by Domain
- Leaking IQueryable to application

---

## Q015: Thin Controllers and Endpoints

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Presentation |
| **Frequency** | Common |

### Question

How thin should API controllers be?

### Short Answer (30 seconds)

Map request → command/query → send to mediator → map result to HTTP. No business logic.

### Detailed Answer (3–5 minutes)

```csharp
[HttpPost]
public async Task<IActionResult> Create(CreateOrderRequest req)
    => Ok(await _mediator.Send(req.ToCommand()));
```

**Architect:** Controller knows HTTP; application knows use cases.

### Architecture Perspective

Fat controllers are maintainability debt.

### Follow-up Questions

1. **Minimal API same rule? — Delegate to mediator in lambda.**
2. **Filter vs controller validation? — Input format in filter; business in handler.**

### Common Mistakes in Interviews

- Controller calls 5 repositories
- Try/catch per action with custom errors
- Controller builds SQL

---

## Q016: Cross-Cutting Middleware vs Behaviors

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Design |
| **Frequency** | Common |

### Question

Middleware vs MediatR pipeline behaviors?

### Short Answer (30 seconds)

Middleware: HTTP pipeline (auth, correlation, exception). Behaviors: per-request use case wrapper (validation, logging, transactions).

### Detailed Answer (3–5 minutes)

**Order:** Middleware first; behaviors around handler.

**Architect:** Don't duplicate validation in both middleware and handler.

### Architecture Perspective

Clear placement reduces duplicate cross-cutting code.

### Follow-up Questions

1. **OpenTelemetry span per behavior? — Yes for handler-level visibility.**
2. **Transaction behavior? — UnitOfWork behavior wraps handler.**

### Common Mistakes in Interviews

- Same validation middleware and FluentValidation
- Behavior order undocumented
- Business rules in logging behavior

---

## Q017: FluentValidation Placement

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Validation |
| **Frequency** | Common |

### Question

Where run FluentValidation in Clean Architecture?

### Short Answer (30 seconds)

Validate commands/queries in application layer — MediatR `ValidationBehavior` before handler.

### Detailed Answer (3–5 minutes)

**Not in:** Domain for input format (null, length) — domain validates invariants (cannot ship cancelled order).

**Architect:** Validation rules colocated with command class or separate validator class per team standard.

### Architecture Perspective

Input validation vs domain invariants — know both.

### Follow-up Questions

1. **Api behavior automatic validation? — ModelState for API models separate from domain commands.**
2. **Validate in controller and handler duplicate?**

### Common Mistakes in Interviews

- Domain exception for invalid email format
- No validation on internal commands
- 500 lines in one validator class

---

## Q018: Mapping Strategy ADR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Design |
| **Frequency** | Common |

### Question

AutoMapper vs manual mapping — architect decision?

### Short Answer (30 seconds)

AutoMapper: large DTO surface, convention-based — speed. Manual: complex aggregates, explicit control, easier debug.

### Detailed Answer (3–5 minutes)

**Architect:** Mapperly source generator middle ground — compile-time.

**Rule:** Map at boundaries only — never map entity to entity across contexts.

**Review:** Mapping profiles in PR review — silent null mapping bugs.

### Architecture Perspective

Mapping is boundary concern not domain.

### Follow-up Questions

1. **Bidirectional map entities? — Dangerous — one direction preferred.**
2. **Projection in repository? — Select DTO in query for read side.**

### Common Mistakes in Interviews

- AutoMapper everywhere including domain
- Map GET mutates entity accidentally
- No tests on critical mappings

---

## Q019: Global Exception Handling

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | API Design |
| **Frequency** | Common |

### Question

Design global exception handling for .NET API?

### Short Answer (30 seconds)

Middleware catches exceptions → maps domain exceptions to HTTP status → ProblemDetails.

### Detailed Answer (3–5 minutes)

**Mapping:** `OrderNotFoundException` → 404. `ValidationException` → 400. Unknown → 500 logged with correlation ID.

**Architect:** Domain exceptions carry no HTTP knowledge; middleware translates.

### Architecture Perspective

Consistent errors improve client and ops experience.

### Follow-up Questions

1. **ExceptionHandlerMiddleware vs filter? — Middleware catches all pipeline.**
2. **Development vs prod detail? — Stack trace dev only.**

### Common Mistakes in Interviews

- catch(Exception) return 200
- Different error shape per team
- Log same exception 5 times

---

## Q020: Result Pattern vs Exceptions

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Design |
| **Frequency** | Common |

### Question

When `Result<T>` instead of exceptions for flow control?

### Short Answer (30 seconds)

Expected failures (not found, conflict) → Result. Exceptional failures (null ref, DB down) → throw.

### Detailed Answer (3–5 minutes)

**Architect:** Result in application API reduces exception overhead for business cases.

**Library:** FluentResults, ErrorOr, or custom `Result<T>`.

**Don't:** Result for everything — exceptions still valid.

### Architecture Perspective

Flow control style is team consistency choice.

### Follow-up Questions

1. **Railway oriented programming? — Bind/Map on Result chains.**
2. **HTTP mapping from Result? — Extension ToActionResult().**

### Common Mistakes in Interviews

- Exception for validation expected case
- Result ignored without check
- Mixed Result and throw randomly

---

## Q021: Specification Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Patterns |
| **Frequency** | Occasional |

### Question

Specification pattern for complex queries?

### Short Answer (30 seconds)

Encapsulate query criteria in reusable spec objects — `ActiveOrdersSpec`, compose with And/Or.

### Detailed Answer (3–5 minutes)

**Benefits:** DRY query logic, testable criteria, repository stays clean.

**Architect:** Use when same filter in multiple handlers; avoid for one-off simple queries.

### Architecture Perspective

Specification reduces repository method explosion.

### Follow-up Questions

1. **Ardalis.Specification library? — Popular EF integration.**
2. **Spec in domain or infrastructure? — Domain defines; infra implements.**

### Common Mistakes in Interviews

- GetOrdersByStatusAndDate method per combo
- IQueryable leaked to application
- Untestable 200-line LINQ in handler

---

## Q022: Unit of Work with EF Core

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Persistence |
| **Frequency** | Common |

### Question

Unit of Work pattern with DbContext in .NET?

### Short Answer (30 seconds)

DbContext is UoW — `SaveChangesAsync` commits transaction. One UoW per request scope.

### Detailed Answer (3–5 minutes)

**Architect:** Single `SaveChanges` per request unless explicit batch. Repository + UoW abstraction optional — DbContext often sufficient.

**Multiple contexts:** Distributed transaction avoided — saga instead.

### Architecture Perspective

Transaction boundary clarity prevents partial commits.

### Follow-up Questions

1. **Explicit Database.BeginTransaction? — When multiple SaveChanges need one TX.**
2. **Retry on SaveChanges failure? — Execution strategy for transient SQL.**

### Common Mistakes in Interviews

- SaveChanges in loop per item
- Multiple DbContext same request uncoordinated
- Long transaction with HTTP call inside

---

## Q023: Integration vs Unit Test Layers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Testing |
| **Frequency** | Common |

### Question

Testing strategy per Clean Architecture layer?

### Short Answer (30 seconds)

Domain: pure unit tests. Application: handler tests with mocked ports. Infrastructure: integration tests (Testcontainers). API: contract/E2E selective.

### Detailed Answer (3–5 minutes)

**Architect:** Testing pyramid — many fast domain tests, fewer E2E.

**WebApplicationFactory:** API integration without full browser.

### Architecture Perspective

Test placement mirrors architecture boundaries.

### Follow-up Questions

1. **Architecture tests? — NetArchTest enforce layer rules.**
2. **Testcontainers SQL? — Real DB integration in CI.**

### Common Mistakes in Interviews

- E2E only no unit tests
- Mock entire domain in unit tests
- Tests hit production database

---

## Q024: Modular Monolith Modules

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Architecture |
| **Frequency** | Common |

### Question

Design modules in modular monolith?

### Short Answer (30 seconds)

Separate projects per module (Orders, Billing) with explicit public API — internal classes invisible.

### Detailed Answer (3–5 minutes)

**Communication:** Module interface or domain events in-process.

**Architect:** Stepping stone to microservices — boundaries already drawn.

### Architecture Perspective

Modular monolith defers distributed complexity.

### Follow-up Questions

1. **Shared database modules? — Schema separation or table prefixes.**
2. **Extract module to service? — When team and scale justify.**

### Common Mistakes in Interviews

- Everything public internal classes
- Circular module references
- Shared EF DbContext god context

---

## Q025: Vertical Slice vs Layers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Architecture |
| **Frequency** | Very Common |

### Question

Team debates vertical slice vs horizontal layers — guidance?

### Short Answer (30 seconds)

Layers: shared technical grouping. Vertical slice: feature folders (CreateOrder, ShipOrder) with handler + validator + endpoint together.

### Detailed Answer (3–5 minutes)

**Architect:** Vertical slice improves feature velocity in large teams. Layers familiar for CRUD enterprise.

**Hybrid common:** Vertical slice folders inside application layer.

### Architecture Perspective

Organization should match change frequency.

### Follow-up Questions

1. **Jimmy Bogard vertical slice? — Reference architecture inspiration.**
2. **Shared kernel between slices? — Minimize — shared value objects only.**

### Common Mistakes in Interviews

- Religious layers only for 3 endpoints
- Vertical slice with no layer rules at all
- Copy-paste between slices

---

## Q026: CQRS Without Event Sourcing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | CQRS |
| **Frequency** | Common |

### Question

CQRS without event sourcing — when and how?

### Short Answer (30 seconds)

Separate read models (queries) from write models (commands) — same database OK initially.

### Detailed Answer (3–5 minutes)

**Start:** Different handlers and DTOs; optimize read queries with projections.

**Avoid:** Separate databases day one without need.

**Architect:** Logical CQRS first; physical split when read scale demands.

### Architecture Perspective

CQRS ≠ event sourcing — common confusion.

### Follow-up Questions

1. **Read model rebuild? — Without ES, from current DB state.**
2. **MediatR natural fit? — IRequest handlers per command/query.**

### Common Mistakes in Interviews

- CQRS with two databases day one
- Confuse CQRS with CRUD split only names
- No sync strategy read/write

---

## Q027: MediatR Pipeline Behaviors

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Patterns |
| **Frequency** | Common |

### Question

Order and examples of MediatR pipeline behaviors?

### Short Answer (30 seconds)

Validation → Logging → Transaction → Handler. Behaviors implement `IPipelineBehavior<TRequest,TResponse>`.

### Detailed Answer (3–5 minutes)

**Architect:** Open generic behaviors registered once. Ordering via `Order` property or registration order.

**Test:** Mock pipeline or test behavior in isolation.

### Architecture Perspective

Pipeline is clean cross-cutting for use cases.

### Follow-up Questions

1. **Pre-processor vs behavior? — Behaviors wrap entire pipeline.**
2. **Notification handlers? — Domain events in-process.**

### Common Mistakes in Interviews

- Duplicate transaction in behavior and handler
- Behavior swallows exceptions
- 10 behaviors deep opaque pipeline

---

## Q028: Feature Flags in Clean Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Release |
| **Frequency** | Common |

### Question

Feature flags without polluting domain?

### Short Answer (30 seconds)

Check flag in application layer or infrastructure adapter — domain stays flag-agnostic.

### Detailed Answer (3–5 minutes)

**Providers:** Azure App Configuration, LaunchDarkly.

**Architect:** Flag drives adapter selection or handler branch — not `if (flag)` scattered in domain entity.

### Architecture Perspective

Flags decouple deploy from release.

### Follow-up Questions

1. **Kill switch pattern? — Disable feature without redeploy.**
2. **Flag debt cleanup? — Remove flags after full rollout.**

### Common Mistakes in Interviews

- Feature flag in domain entity method
- 100 permanent flags
- No monitoring per flag evaluation

---

## Q029: API Contract Versioning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | API Design |
| **Frequency** | Common |

### Question

Version DTOs and handlers together?

### Short Answer (30 seconds)

V2 command/DTO separate from V1 — shared domain where possible. Handlers may diverge per version.

### Detailed Answer (3–5 minutes)

**Architect:** Controllers map v1/v2 routes to version-specific commands. Domain aggregates version-agnostic when possible.

**Deprecation:** Sunset header on v1 responses.

### Architecture Perspective

Contract versioning is client empathy.

### Follow-up Questions

1. **OpenAPI per version? — Swagger doc v1 and v2.**
2. **Shared handler both versions? — Risky — separate clearer.**

### Common Mistakes in Interviews

- Break DTO without version
- Domain changes for API tweak only
- Infinite version support

---

## Q030: When to Simplify Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Pragmatism |
| **Frequency** | Very Common |

### Question

When would you NOT use Clean Architecture?

### Short Answer (30 seconds)

Internal admin CRUD 5 endpoints, prototype, throwaway — simple 3-layer or even minimal API + DbContext is fine.

### Detailed Answer (3–5 minutes)

**Architect honesty:** CA has ceremony cost — justify with team size, lifespan, complexity.

**Signals for CA:** Multiple integrations, complex domain rules, 5+ year lifespan, multiple teams.

**Graduate into CA** when pain appears — not day-one mandate for all apps.

### Architecture Perspective

Pragmatism earns trust in architecture reviews.

### Follow-up Questions

1. **Strangler to CA? — Extract domain gradually from monolith.**
2. **Document simplification ADR? — Yes — explain why not CA.**

### Common Mistakes in Interviews

- CA for every console utility
- Big Design Up Front CA weeks before code
- Shame teams for simple layering

---
