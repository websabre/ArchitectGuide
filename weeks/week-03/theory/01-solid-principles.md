# SOLID Principles — Fundamentals to Advanced

> **Week 03** | **Module:** [design-patterns-solid](../../../modules/design-patterns-solid/README.md)

## Learning Objectives

- Apply each SOLID principle with .NET examples
- Recognize violations in legacy codebases
- Connect SOLID to maintainability at scale

---

## 1. Single Responsibility Principle (SRP)

> A class should have only one reason to change.

```csharp
// VIOLATION: OrderService does too much
public class OrderService
{
    public void CreateOrder(Order order) { /* save to DB */ }
    public void SendConfirmationEmail(Order order) { /* SMTP */ }
    public string GenerateInvoicePdf(Order order) { /* PDF */ }
}

// BETTER: Separate responsibilities
public class OrderService(IOrderRepository repo, IEventPublisher events)
{
    public async Task CreateAsync(Order order)
    {
        await repo.AddAsync(order);
        await events.PublishAsync(new OrderCreatedEvent(order.Id));
    }
}
```

**Architect lens:** SRP at **module/service level** matters more than class level. A microservice should have one bounded context — one reason to change.

**Interview trap:** "One method per class" — wrong. Cohesive group of methods serving one responsibility is fine.

---

## 2. Open/Closed Principle (OCP)

> Open for extension, closed for modification.

```csharp
public interface IDiscountStrategy
{
    decimal Apply(Order order);
}

public class PercentageDiscount(decimal percent) : IDiscountStrategy
{
    public decimal Apply(Order order) => order.Total * (1 - percent);
}

public class VipDiscount : IDiscountStrategy
{
    public decimal Apply(Order order) => order.Total * 0.85m;
}

public class PricingService(IEnumerable<IDiscountStrategy> strategies) { ... }
```

**Architect use:** Plugin architectures, strategy registration via DI, feature flags for new behavior.

**Trade-off:** Too many abstractions for simple systems — apply OCP when change frequency justifies it.

---

## 3. Liskov Substitution Principle (LSP)

> Subtypes must be substitutable for base types without breaking behavior.

```csharp
// VIOLATION: Square inherits Rectangle, breaks SetWidth/SetHeight
public class Square : Rectangle
{
    public override void SetWidth(int w) { base.SetWidth(w); base.SetHeight(w); }
}

// BETTER: Separate types or common interface IShape with Area()
```

**Real-world .NET violation:** Overriding methods that throw `NotSupportedException` — indicates LSP break.

**Architect action:** Integration tests that verify all implementations of an interface behave per contract.

---

## 4. Interface Segregation Principle (ISP)

> Clients shouldn't depend on interfaces they don't use.

```csharp
// VIOLATION: Fat interface
public interface IWorker
{
    void Work();
    void Eat();
    void Sleep();
}

// BETTER: Segregated
public interface IWorkable { void Work(); }
public interface IFeedable { void Eat(); }
```

**Microservices parallel:** Don't expose one mega-API — split by client needs (BFF pattern implements ISP at API level).

---

## 5. Dependency Inversion Principle (DIP)

> Depend on abstractions, not concretions.

```csharp
// High-level module depends on abstraction
public class OrderService(IOrderRepository repository, IPaymentGateway payment)
{
    public async Task PlaceOrderAsync(Order order)
    {
        await payment.ChargeAsync(order.Total);
        await repository.SaveAsync(order);
    }
}
```

**This is the foundation of DI.** DIP is the principle; DI is the mechanism.

---

## SOLID at Architecture Level

| Principle | Code Level | Architecture Level |
|-----------|-----------|-------------------|
| SRP | One class, one job | One service, one bounded context |
| OCP | Strategy pattern | Plugin systems, extensibility |
| LSP | Correct inheritance | API contract compatibility |
| ISP | Small interfaces | Focused microservice APIs |
| DIP | Inject interfaces | Depend on events/contracts, not implementations |

---

## Common Mistakes

1. **SOLID obsession** — 5 interfaces for a CRUD app
2. **SRP = one method** — misinterpretation
3. **Ignoring YAGNI** — abstractions before needed change
4. **LSP ignored in DTO inheritance** — fragile base class

**Next:** [02-clean-architecture.md](02-clean-architecture.md)
