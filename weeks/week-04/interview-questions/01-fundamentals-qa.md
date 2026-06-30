# Week 04 — Fundamentals Interview Q&A

> Q001–Q030: Premium format (Week 1 quality).  
> See also: [Interview prep hub](../../../interview-prep/README.md)

---


## Q001: Singleton vs DI Singleton

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Creational |
| **Frequency** | Very Common |

### Question

Static singleton vs DI-registered singleton lifetime?

### Short Answer (30 seconds)

Static singleton: global hidden state, hard to test. DI singleton: one instance per container, mockable, explicit lifetime.

### Detailed Answer (3–5 minutes)

```csharp
services.AddSingleton<ICacheService, MemoryCacheService>();
```

**Architect:** Ban static mutable singletons in coding standards. DI singleton for stateless caches and config readers.

**Exception:** `IOptions` effectively singleton.

### Architecture Perspective

DI singleton is not the Singleton pattern anti-pattern.

### Follow-up Questions

1. **Singleton vs Scoped for cache? — Scoped if cache must be per-tenant request.**
2. **IMemoryCache thread safety? — Built-in thread-safe.**

### Common Mistakes in Interviews

- static Database.Instance
- Singleton holding Scoped DbContext
- Global mutable static cache

---

## Q002: Factory Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Creational |
| **Frequency** | Common |

### Question

Factory pattern for payment gateway selection?

### Short Answer (30 seconds)

Encapsulate creation logic — `IPaymentGatewayFactory.Create(PaymentType type)` returns Stripe or Adyen implementation.

### Detailed Answer (3–5 minutes)

**When:** Creation complex (config, credentials, sandbox vs prod). **SimpleFactory vs FactoryMethod:** Method per product vs subclass override.

**Architect:** Register factory in DI; unit test returns mocks.

### Architecture Perspective

Factories isolate construction from business logic.

### Follow-up Questions

1. **DI container as factory? — `GetRequiredService` by key .NET 8.**
2. **Abstract factory when? — Families of related gateways + reporting.**

### Common Mistakes in Interviews

- new StripeGateway() in controller
- Factory with 50 case switch
- No interface on products

---

## Q003: Adapter Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Structural |
| **Frequency** | Very Common |

### Question

Adapter for legacy ERP integration?

### Short Answer (30 seconds)

Wrap legacy XML/SOAP ERP API behind `IOrderPort` your application understands.

### Detailed Answer (3–5 minutes)

**Anti-corruption layer** is architect-level adapter — translate models at boundary.

**Example:** `LegacyErpOrderAdapter` maps `ErpXmlOrder` → `PlaceOrderCommand`.

### Architecture Perspective

Adapters enable strangler fig migrations.

### Follow-up Questions

1. **Two-way adapter? — Rare — usually one direction inbound.**
2. **Adapter vs Facade? — Adapter changes interface; Facade simplifies subsystem.**

### Common Mistakes in Interviews

- Import ERP types into domain
- Copy-paste ERP parsing everywhere
- Adapter with business logic bloat

---

## Q004: Decorator vs Inheritance

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Structural |
| **Frequency** | Common |

### Question

Decorator pattern for cross-cutting without inheritance?

### Short Answer (30 seconds)

Wrap `IOrderService` with `CachingOrderServiceDecorator` — adds behavior without subclass explosion.

### Detailed Answer (3–5 minutes)

**vs Inheritance:** 3 cross-cutting concerns = 8 subclasses combinatorial explosion with inheritance; 3 decorators stack cleanly.

**DI:** `services.Decorate<IOrderService, CachingDecorator>()` Scrutor library.

### Architecture Perspective

Decorator is composition over inheritance exemplified.

### Follow-up Questions

1. **Middleware vs decorator? — HTTP pipeline similar concept different layer.**
2. **Decorator order matters? — Cache outside or inside logging — document.**

### Common Mistakes in Interviews

- Inheritance tree LoggingCachingOrderService
- Decorator changing interface contract
- Infinite decorator recursion

---

## Q005: Facade Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Structural |
| **Frequency** | Common |

### Question

Facade for checkout orchestration?

### Short Answer (30 seconds)

`CheckoutFacade.PlaceOrder()` coordinates inventory, payment, notification — controller calls one method.

### Detailed Answer (3–5 minutes)

**Not god object:** Facade delegates; doesn't implement business rules.

**Architect:** BFF is facade at API boundary. Application service can be facade over domain.

### Architecture Perspective

Facade simplifies client interaction.

### Follow-up Questions

1. **Facade vs MediatR? — MediatR dispatches; facade explicit API.**
2. **Multiple facades per bounded context? — Yes per use case area.**

### Common Mistakes in Interviews

- Controller calls 8 services directly
- Facade with 500 lines business logic
- Facade bypassing domain invariants

---

## Q006: Strategy Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Behavioral |
| **Frequency** | Very Common |

### Question

Strategy for shipping cost calculation?

### Short Answer (30 seconds)

`IShippingStrategy` implementations: Standard, Express, International — selected by order context.

### Detailed Answer (3–5 minutes)

**DI registration:** `services.AddTransient<IShippingStrategy, ExpressShipping>()` with factory key.

**Architect:** Strategy + OCP together — add carrier without editing calculator.

### Architecture Perspective

Strategy is most practical GoF pattern daily.

### Follow-up Questions

1. **Strategy vs policy pattern? — Similar intent different name.**
2. **Functional strategy as lambda? — OK for simple cases.**

### Common Mistakes in Interviews

- switch on string shipping type
- Strategy interface with 1 implementation forever
- Context class knowing all strategies concretely

---

## Q007: Observer and Domain Events

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Behavioral |
| **Frequency** | Common |

### Question

Observer pattern vs .NET events vs domain events?

### Short Answer (30 seconds)

Observer: subject notifies subscribers. .NET `event` keyword. Domain events: DDD pattern — `OrderPlaced` raised from aggregate, handled in-process or outbox.

### Detailed Answer (3–5 minutes)

**Architect:** Domain events for business facts; integration events for cross-service. MediatR `INotification` for in-process handlers.

### Architecture Perspective

Event-driven decoupling within and across services.

### Follow-up Questions

1. **Event vs command? — Past tense fact vs imperative.**
2. **Spaghetti event chains? — Document flow; consider orchestration.**

### Common Mistakes in Interviews

- God object firing 20 events synchronously
- Domain event published before commit
- No handler idempotency cross-service

---

## Q008: Repository Pattern Debate

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Enterprise |
| **Frequency** | Very Common |

### Question

Do you still use Repository with EF Core?

### Short Answer (30 seconds)

DbContext is already repository+UoW. Use repository per aggregate when interface adds value — custom queries, testing seam, swap storage.

### Detailed Answer (3–5 minutes)

**Architect position:** `IOrderRepository` with meaningful methods — not generic `IRepository<T>` on 40 entities.

**Skip when:** Small service, team proficient with DbContext directly.

### Architecture Perspective

Repository debate shows architect pragmatism.

### Follow-up Questions

1. **Specification + repository? — Composable queries.**
2. **Cosmos repository same interface? — Possible adapter.**

### Common Mistakes in Interviews

- IRepository<T> everywhere
- Repository returns IQueryable to API
- Pass-through repo adding no value

---

## Q009: Outbox Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Enterprise |
| **Frequency** | Very Common |

### Question

Implement transactional outbox in .NET?

### Short Answer (30 seconds)

Same transaction: save aggregate + insert outbox row. Background relay publishes to Service Bus and marks sent.

### Detailed Answer (3–5 minutes)

**Libraries:** MassTransit EF outbox, custom relay worker.

**Architect:** Never `SaveChanges` then `Publish` without outbox — crash between = inconsistency.

**Idempotent consumers** on other side still required.

### Architecture Perspective

Outbox is architect messaging reliability standard.

### Follow-up Questions

1. **Inbox pattern pairing? — Consumer dedup table.**
2. **Outbox polling vs CDC? — Polling simpler; CDC lower latency.**

### Common Mistakes in Interviews

- Publish before commit
- No poison message handling
- Outbox table unbounded no cleanup

---

## Q010: Saga Pattern Introduction

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Enterprise |
| **Frequency** | Common |

### Question

Orchestrated vs choreographed saga for order flow?

### Short Answer (30 seconds)

Choreography: services react to events — loose coupling. Orchestration: central coordinator (Durable Functions) — visible flow, easier debug.

### Detailed Answer (3–5 minutes)

**Steps:** Reserve inventory → Charge payment → Confirm order. Compensate on failure: release, refund.

**Architect:** Start choreography 2-3 steps; orchestration when complexity grows.

### Architecture Perspective

Sagas replace distributed 2PC.

### Follow-up Questions

1. **Saga vs 2PC? — Saga eventual consistency with compensation.**
2. **Long-running saga state? — Durable Functions or MassTransit state machine.**

### Common Mistakes in Interviews

- Sync HTTP chain 5 services
- No compensation defined
- Saga state lost on restart

---

## Q011: Chain of Responsibility

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Behavioral |
| **Frequency** | Common |

### Question

Chain of Responsibility for request validation pipeline?

### Short Answer (30 seconds)

Each handler validates one concern, passes to next — composable validation without god method.

### Detailed Answer (3–5 minutes)

**Example:** Auth check → rate limit → schema validate → business handler.

**Architect:** ASP.NET middleware is chain of responsibility at HTTP level.

### Architecture Perspective

Chain composes cross-cutting steps cleanly.

### Follow-up Questions

1. **Pipeline vs chain? — Similar concepts different scales.**
2. **Short-circuit on failure? — Stop chain return error.**

### Common Mistakes in Interviews

- God validator 50 checks
- Chain order wrong silent bypass
- No test per chain link

---

## Q012: Command Pattern with Handlers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Behavioral |
| **Frequency** | Very Common |

### Question

Command pattern in .NET with MediatR?

### Short Answer (30 seconds)

Command object encapsulates request; handler executes — single responsibility per use case.

### Detailed Answer (3–5 minutes)

**Benefits:** Testable units, discoverable handlers, pipeline behaviors.

**Architect:** One command per write operation — not generic `Execute(string action)`.

### Architecture Perspective

Commands are application layer backbone.

### Follow-up Questions

1. **ICommand vs IRequest? — MediatR IRequest naming.**
2. **Undo command? — Memento + command for editor apps.**

### Common Mistakes in Interviews

- God command with 20 properties optional
- Handler calls handler directly not mediator
- No idempotency on retryable commands

---

## Q013: State Pattern for Order Workflow

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Behavioral |
| **Frequency** | Common |

### Question

State pattern vs switch for order status?

### Short Answer (30 seconds)

Each state class implements transitions — `ConfirmedState.Ship()` vs giant switch on enum.

### Detailed Answer (3–5 minutes)

**When:** Many states, complex transition rules.

**Modern C#:** Switch expressions OK for simple; State pattern for rich behavior per state.

**Architect:** Align with domain-driven design — `order.Confirm()` delegates to state.

### Architecture Perspective

State pattern tames workflow complexity.

### Follow-up Questions

1. **Stateless state pattern? — Stateless singleton state objects possible.**
2. **Persist state how? — Status enum + behavior from factory.**

### Common Mistakes in Interviews

- switch on status 40 cases
- Invalid transitions throw generic Exception
- State logic in controller

---

## Q014: Template Method Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Behavioral |
| **Frequency** | Occasional |

### Question

Template Method in export/report generation?

### Short Answer (30 seconds)

Base class defines algorithm skeleton; subclasses override steps — `FetchData`, `Format`, `Deliver`.

### Detailed Answer (3–5 minutes)

**Architect:** Prefer composition (strategy for steps) over inheritance when possible — .NET favors composition.

**Use inheritance template** when framework defines lifecycle (ASP.NET middleware base).

### Architecture Perspective

Template Method vs Strategy — inheritance vs composition.

### Follow-up Questions

1. **Hook methods? — Optional override points in template.**
2. **Virtual methods fragility? — Document extension points.**

### Common Mistakes in Interviews

- Deep inheritance hierarchy
- Template with 15 abstract methods
- Subclass breaks base invariant

---

## Q015: Proxy Pattern for Lazy Loading

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Structural |
| **Frequency** | Occasional |

### Question

Proxy for lazy loading expensive dependency?

### Short Answer (30 seconds)

Proxy implements same interface, defers real object creation until first use — caching proxy, remote proxy, protection proxy.

### Detailed Answer (3–5 minutes)

**Architect:** DI can register decorator proxy. EF lazy loading is proxy-based — understand N+1 risk.

**Remote proxy:** gRPC client wrapper.

### Architecture Perspective

Proxy controls access and initialization.

### Follow-up Questions

1. **DispatchProxy in .NET? — Dynamic proxy for interfaces.**
2. **Virtual proxy vs remote? — Know types for interviews.**

### Common Mistakes in Interviews

- EF lazy loading N+1 unnoticed
- Proxy without interface
- Hidden side effects in proxy

---

## Q016: Composite Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Structural |
| **Frequency** | Occasional |

### Question

Composite pattern real enterprise example?

### Short Answer (30 seconds)

Tree structures treated uniformly — org chart, menu permissions, file system folders.

### Detailed Answer (3–5 minutes)

**Component interface:** `GetTotal()`, `Render()` on leaf and composite alike.

**Architect:** Useful for hierarchical permissions and nested product categories.

### Architecture Perspective

Composite models part-whole hierarchies.

### Follow-up Questions

1. **Iterator over composite? — Recursive traversal or stack-based.**
2. **Cycle detection? — Guard parent pointers in mutable trees.**

### Common Mistakes in Interviews

- Special case every leaf in client code
- Composite allows cycles
- No interface for leaf vs composite

---

## Q017: Bridge Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Structural |
| **Frequency** | Occasional |

### Question

Bridge pattern vs Strategy — difference?

### Short Answer (30 seconds)

Bridge splits abstraction and implementation hierarchies independently — `Message` abstraction × `Sender` implementation (Email, SMS).

### Detailed Answer (3–5 minutes)

**Strategy:** interchangeable algorithm. **Bridge:** structural decoupling of two dimensions.

**Architect:** Bridge when both hierarchies evolve independently.

### Architecture Perspective

Naming confusion common in interviews.

### Follow-up Questions

1. **Adapter vs Bridge? — Adapter fixes interface; Bridge designs separation upfront.**
2. **DI replaces some Bridge uses? — Often inject implementation.**

### Common Mistakes in Interviews

- Multiply inheritance instead of bridge
- Confuse with Strategy always
- Two dimensions coupled in one class

---

## Q018: Memento for Audit Trail

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Behavioral |
| **Frequency** | Occasional |

### Question

Memento pattern for undo/audit?

### Short Answer (30 seconds)

Capture object state externally without exposing internals — undo in editor, audit snapshots.

### Detailed Answer (3–5 minutes)

**Enterprise:** Event sourcing is scalable memento — state as event log.

**Architect:** Memento for simple undo; event sourcing for audit at scale.

### Architecture Perspective

Audit requirements drive pattern choice.

### Follow-up Questions

1. **Caretaker role? — Stores mementos without peeking.**
2. **Immutable memento? — Safer for audit history.**

### Common Mistakes in Interviews

- Expose all fields for audit copy
- Unbounded memento memory
- Memento instead of domain events at scale

---

## Q019: Visitor vs Pattern Matching

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Behavioral |
| **Frequency** | Common |

### Question

When Visitor still needed in modern C#?

### Short Answer (30 seconds)

Open hierarchy, many operations across types — tax calculation on expression tree. Pattern matching for closed simple hierarchies.

### Detailed Answer (3–5 minutes)

**Visitor:** Add new operation without changing element classes. **Pattern matching:** Add new types requires updating switches (exhaustiveness helps).

**Architect:** Prefer pattern matching for `OrderStatus`; Visitor for compiler/AST style problems.

### Architecture Perspective

Modern C# reduces Visitor need but not eliminate.

### Follow-up Questions

1. **Double dispatch explained? — Visitor achieves via Accept method.**
2. **Source generators for visitors? — Reduce boilerplate.**

### Common Mistakes in Interviews

- Visitor for 3-type hierarchy
- Pattern matching without exhaustiveness
- Visitor every tax line item

---

## Q020: Repository Pattern Debate

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Enterprise |
| **Frequency** | Very Common |

### Question

Repository pattern — still use with EF Core?

### Short Answer (30 seconds)

Debate continues. EF DbContext already repository+UoW. Generic `IRepository<T>` often leaky abstraction.

### Detailed Answer (3–5 minutes)

**Architect position:** Repository per aggregate meaningful interface — `IOrderRepository.GetWithLines(id)` — not generic CRUD on 50 entities.

**Skip when:** Simple app, DbContext directly in handler acceptable for small teams.

### Architecture Perspective

Repository should add value not pass-through.

### Follow-up Questions

1. **Specification + repository? — Compose query logic.**
2. **Cosmos repository? — Same interface different adapter.**

### Common Mistakes in Interviews

- IRepository<T> all entities
- Repository returns IQueryable
- Repository with no aggregate focus

---

## Q021: Unit of Work Enterprise Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Enterprise |
| **Frequency** | Common |

### Question

Unit of Work coordinating multiple repositories?

### Short Answer (30 seconds)

One transaction across repositories sharing same DbContext/session.

### Detailed Answer (3–5 minutes)

**EF:** Single DbContext scope = UoW. Multiple repos inject same context.

**Architect:** `IUnitOfWork.CommitAsync()` abstraction when testing commit behavior.

### Architecture Perspective

Transaction boundary is architect concern.

### Follow-up Questions

1. **Distributed UoW? — Avoid — saga pattern instead.**
2. **Mock UoW in tests? — Fake in-memory UoW for unit tests.**

### Common Mistakes in Interviews

- SaveChanges per repository method
- UoW without clear scope
- Mock UoW 10 layers deep

---

## Q022: Domain Events and Outbox

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Enterprise |
| **Frequency** | Very Common |

### Question

Raise domain events and publish reliably?

### Short Answer (30 seconds)

Raise events in aggregate; dispatch after SaveChanges; outbox table for reliable publish to broker.

### Detailed Answer (3–5 minutes)

**Flow:** Handler saves aggregate + outbox row same transaction → relay publishes to Service Bus.

**Architect:** Never publish before commit — lost message or inconsistent state.

### Architecture Perspective

Reliable messaging is architect integration pattern.

### Follow-up Questions

1. **MediatR notification vs domain event? — Domain in aggregate; MediatR dispatches in-process.**
2. **Transactional outbox library? — MassTransit, custom relay.**

### Common Mistakes in Interviews

- Publish before SaveChanges
- No idempotent consumer
- Domain event = integration event same class

---

## Q023: Saga Orchestration Introduction

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Enterprise |
| **Frequency** | Common |

### Question

Orchestrated saga for checkout — components?

### Short Answer (30 seconds)

Orchestrator coordinates: reserve inventory → charge payment → confirm order → compensate on failure.

### Detailed Answer (3–5 minutes)

**Implement:** Durable Functions, MassTransit, custom state machine.

**Architect:** Choreography for simple; orchestration when visibility and compensation complex.

### Architecture Perspective

Sagas replace 2PC in microservices.

### Follow-up Questions

1. **Compensating transaction? — Refund, release inventory.**
2. **Saga timeout? — Auto-compensate stuck steps.**

### Common Mistakes in Interviews

- Sync chain 5 services no compensation
- Saga state only in memory
- No idempotency on saga steps

---

## Q024: CQRS with Repository Together

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Patterns |
| **Frequency** | Common |

### Question

CQRS handlers with repositories — read side optimization?

### Short Answer (30 seconds)

Write handler uses aggregate repository. Read handler uses Dapper/raw SQL or denormalized view — skip domain load.

### Detailed Answer (3–5 minutes)

**Architect:** Read model can bypass domain — that's the point. Don't force repository on queries needing joins.

### Architecture Perspective

CQRS read side freedom is performance win.

### Follow-up Questions

1. **Separate read database? — When scale requires.**
2. **Projections from events? — With event sourcing.**

### Common Mistakes in Interviews

- Load full aggregate for list screen
- Same model read write forever
- ORM on complex report query

---

## Q025: God Object Anti-Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Anti-Pattern |
| **Frequency** | Common |

### Question

Identify and refactor God Object?

### Short Answer (30 seconds)

Class knowing/doing too much — `ApplicationService` with 80 methods.

### Detailed Answer (3–5 minutes)

**Refactor:** Extract by feature command handlers, vertical slices, domain services by capability.

**Architect:** Code review rule max methods per class; SonarQube cognitive complexity gate.

### Architecture Perspective

God objects signal missing boundaries.

### Follow-up Questions

1. **Facade vs God Object? — Facade coordinates subservices doesn't implement all logic.**
2. **Extract class refactoring? — Safe incremental.**

### Common Mistakes in Interviews

- Ignore 5000-line service
- Add method 81 to god class
- No module ownership

---

## Q026: Spaghetti Callback Anti-Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Anti-Pattern |
| **Frequency** | Common |

### Question

Spaghetti callbacks in async code — fix?

### Short Answer (30 seconds)

Nested callbacks → async/await, or events, or reactive streams.

### Detailed Answer (3–5 minutes)

**Legacy:** Callback hell in old JS/Node patterns. .NET: `ContinueWith` chains — use async/await.

**Architect:** Mandate async/await; analyzers flag ContinueWith.

### Architecture Perspective

Control flow clarity is maintainability.

### Follow-up Questions

1. **Reactive Extensions? — When stream processing fits.**
2. **Channel for pipeline? — Structured producer-consumer.**

### Common Mistakes in Interviews

- ContinueWith chains in new code
- async void except events
- Fire-and-forget Task no log

---

## Q027: Service Locator Anti-Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Anti-Pattern |
| **Frequency** | Common |

### Question

Why service locator is anti-pattern vs DI?

### Short Answer (30 seconds)

Hidden dependencies — `ServiceLocator.Get<IRepo>()` — untestable, unclear constructor contract.

### Detailed Answer (3–5 minutes)

**Architect:** Constructor injection only in application code. Service locator acceptable only in legacy bridge code being removed.

### Architecture Perspective

Explicit dependencies are architect standard.

### Follow-up Questions

1. **IServiceProvider direct inject? — Service locator smell if abused in domain.**
2. **Factory vs locator? — Factory creates known types; locator hides.**

### Common Mistakes in Interviews

- Static ServiceLocator class
- Resolve in domain entity
- Test can't mock dependencies

---

## Q028: Pattern Selection ADR Framework

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Process |
| **Frequency** | Common |

### Question

Framework for choosing design pattern in review?

### Short Answer (30 seconds)

Problem statement → forces → pattern candidates → trade-offs → decision → consequences.

### Detailed Answer (3–5 minutes)

**Questions:** Variation in algorithm (Strategy)? Tree structure (Composite)? Object creation (Factory)? Integration reliability (Outbox)?

**Architect:** Simplest solution first — pattern when force justifies complexity.

### Architecture Perspective

ADR documents pattern choice prevents gold plating.

### Follow-up Questions

1. **YAGNI vs pattern? — Don't add pattern for one use case.**
2. **Team pattern glossary? — Shared vocabulary.**

### Common Mistakes in Interviews

- Pattern because blog post
- 15 patterns one feature
- No ADR for Outbox adoption

---

## Q029: Flyweight Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Structural |
| **Frequency** | Occasional |

### Question

Flyweight pattern — when relevant in .NET?

### Short Answer (30 seconds)

Share intrinsic state across many fine-grained objects — character formatting, icon caches, repeated metadata keys.

### Detailed Answer (3–5 minutes)

**Architect:** Rare in business LOB apps. Useful when millions of similar objects — memory optimization.

**.NET:** string interning is flyweight-like.

### Architecture Perspective

Know flyweight — don't force into CRUD apps.

### Follow-up Questions

1. **Intrinsic vs extrinsic state? — Flyweight holds shared; client passes extrinsic.**
2. **Object pool vs flyweight? — Pool reuses instances; flyweight shares state.**

### Common Mistakes in Interviews

- Flyweight for 50 order objects
- Thread-unsafe shared flyweight
- Premature flyweight complexity

---

## Q030: Over-Engineering Patterns Smell

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Pragmatism |
| **Frequency** | Very Common |

### Question

Signs pattern use is over-engineering?

### Short Answer (30 seconds)

Abstract factory for one implementation, strategy with one strategy, observer for single listener.

### Detailed Answer (3–5 minutes)

**Architect:** Refactor when abstraction cost exceeds change frequency. Rule of three — third duplication justifies abstraction.

**Interview:** Show judgment — patterns are tools not goals.

### Architecture Perspective

Senior architects know when to stop abstracting.

### Follow-up Questions

1. **Rule of three? — Third similar case extract abstraction.**
2. **Delete abstraction? — Valid refactor when YAGNI wins.**

### Common Mistakes in Interviews

- Interface per class
- Factory for single type
- Shame simple code

---
