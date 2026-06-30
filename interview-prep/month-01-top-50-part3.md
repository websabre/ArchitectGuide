# Month 1 Top 50 — Part 3 (Q031–Q050)

> **Design Patterns & Scenarios** | Week 4 | [Part 2](month-01-top-50-part2.md) | [Index](month-01-top-50-index.md)

---

## Q031: Strategy Pattern in .NET

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Design Patterns |
| **Week** | 04 |

### Question

Implement shipping cost calculation with Strategy pattern. When prefer Strategy over switch?

### Short Answer (30 seconds)

`IShippingStrategy` with Standard, Express, Overnight implementations registered in DI. Prefer Strategy when algorithms vary independently and you add new strategies without modifying existing code (OCP).

### Detailed Answer (3–5 minutes)

```csharp
public interface IShippingStrategy { decimal Calculate(Order o); }
// DI: services.AddKeyed<IShippingStrategy>("express", typeof(ExpressShipping));
```

**vs switch:** 2 strategies — switch OK. 5+ with frequent additions — Strategy + DI.

### Common Mistakes

- Strategy for every if/else — over-engineering

---

## Q032: Factory vs Abstract Factory

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Design Patterns |
| **Week** | 04 |

### Question

Difference between Factory Method and Abstract Factory?

### Short Answer

Factory Method: one product, subclass decides type. Abstract Factory: families of related products (UI kit: Button + Checkbox for Windows vs Mac).

### Detailed Answer

In .NET: `IHttpClientFactory` is factory — creates configured HttpClients. Abstract Factory rare — use when swapping entire provider families.

### Common Mistakes

- Calling every `new` wrapper a "factory"

---

## Q033: Observer / Event-Driven in Process

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Design Patterns |
| **Week** | 04 |

### Question

How does Observer relate to `IObserver<T>` and domain events?

### Short Answer

Domain raises events; handlers subscribe — in-process MediatR notifications or `IDomainEventDispatcher`. Decouples side effects (email, audit) from core logic.

### Detailed Answer

```csharp
public record OrderPlaced(Guid OrderId) : IDomainEvent;
// Handler: SendConfirmationEmailHandler
```

**Architect:** Distinguish in-process events from integration events (message bus).

### Common Mistakes

- Synchronous email in same transaction as order create — coupling and latency

---

## Q034: Decorator Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Design Patterns |
| **Week** | 04 |

### Question

Use Decorator pattern for cross-cutting without modifying services.

### Short Answer

Wrap `IOrderService` with `LoggingOrderServiceDecorator`, `CachingDecorator` via DI decoration or Scrutor library.

### Detailed Answer

```csharp
services.Decorate<IOrderService, LoggingOrderServiceDecorator>();
```

Order of decoration matters — log outside cache or inside.

### Common Mistakes

- Copy-paste logging in every method instead of decorator

---

## Q035: Repository Pattern Debate

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Design Patterns |
| **Week** | 04 |

### Question

Should architects mandate Repository pattern over EF Core DbContext?

### Short Answer

Not by default. DbContext is unit of work + repository. Add `IRepository<T>` when you need provider swap, strict test doubles, or hide LINQ from application layer. Otherwise — unnecessary abstraction.

### Detailed Answer

**For:** Multi-database, strict hexagonal architecture, legacy ORM swap.

**Against:** Leaky abstraction (`GetQueryable()` exposes EF), extra mapping layer, generic repos add little.

**Architect decision:** Document per bounded context — not global mandate.

### Common Mistakes

- Generic `IRepository<T>` with 50 entities — boilerplate factory

---

## Q036: Anti-Pattern: God Class

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Anti-Patterns |
| **Week** | 04 |

### Question

How do you refactor a 5000-line `OrderManager` god class?

### Short Answer

Identify responsibilities (validate, persist, notify, report). Extract classes per SRP. Introduce application commands. Strangler inside monolith before microservice split.

### Detailed Answer

Week 4 capstone pattern. Measure: cyclomatic complexity, change frequency per method cluster.

### Common Mistakes

- Split to microservices without refactoring god class first

---

## Q037: Anti-Pattern: Golden Hammer

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Anti-Patterns |
| **Week** | 04 |

### Question

Give an example of Golden Hammer in architecture decisions.

### Short Answer

"Everything must be Kafka" or "Everything must be microservices" regardless of problem. Architects evaluate fit — event bus for async decoupling; sync API when user waits.

### Common Mistakes

- Kubernetes for 3-user internal tool

---

## Q038: Scenario — Refactor Monolith Module

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Week** | 04 |

### Question

Legacy `BillingModule` — 3000 lines, no tests, changes monthly. Refactor approach?

### Short Answer

Characterization tests → identify seams → extract `Billing.Application` project → introduce interfaces at boundaries → strangler to new module. No big-bang rewrite.

### Detailed Answer

ADR for each extraction step. Feature flags to route traffic. 3–6 month plan for critical path only.

### Common Mistakes

- Rewrite from scratch in parallel

---

## Q039: Scenario — Choose Patterns for Notification System

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Week** | 04 |

### Question

Email, SMS, push notifications — which patterns?

### Short Answer

Strategy (`INotificationChannel`) + Factory or DI keyed services. Observer/domain events trigger notifications. Retry with Polly. Queue for async delivery.

### Detailed Answer

Separate template rendering (Builder) from transport (Strategy). Architect diagram: OrderPlaced event → NotificationService → channels.

### Common Mistakes

- Single `SendNotification` method with type enum growing forever

---

## Q040: Scenario — Architect Code Review

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Week** | 04 |

### Question

What do you look for reviewing a junior's PR adding new payment method?

### Short Answer

OCP compliance — new class vs editing switch. Tests for new path. DI registration. No secrets in code. ADR if architectural change. Performance on hot path.

### Common Mistakes

- Only style comments, missing design feedback

---

## Q041–Q050: Month 1 Capstone Review Questions

### Q041: Document pattern choice in ADR?
Context, decision, consequences, alternatives — link to Week 3 ADR template.

### Q042: record for DTOs at API boundary?
Yes for immutable API contracts; validate on input.

### Q043: IAsyncEnumerable for large exports?
Stream CSV/JSON without memory spike — set correct content-type.

### Q044: Source generators in enterprise?
Use for boilerplate reduction (mapping, DI) — team must maintain generator knowledge.

### Q045: Primary constructors C# 12?
Reduce ceremony in small services — don't put logic in constructors.

### Q046: Test pyramid for modular API?
Many unit (domain), some integration (API + DB), few E2E.

### Q047: Architecture tests with NetArchTest?
`domain.Should().NotHaveDependencyOn("Infrastructure")` in CI.

### Q048: When to extract microservice from monolith?
Independent scale, team boundary, deployment pain — not "because microservices."

### Q049: Month 1 readiness checklist?
Weeks 1–4 assessments ≥70%, 100+ Q&A aloud, capstone API, 5 ADRs.

### Q050: Explain architect lens on C# in 2 minutes?
Language choices affect GC, async throughput, maintainability at scale — not just syntax.

---

**Complete:** [Month 1 Top 50 Index](month-01-top-50-index.md)
