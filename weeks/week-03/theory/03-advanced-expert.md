# Clean Architecture — Advanced & Expert

> **Week 03** | **Level:** Advanced → Expert

## 1. Rich Domain Model vs Anemic Domain Model

### Anemic (Anti-pattern for complex domains)

```csharp
public class Order
{
    public Guid Id { get; set; }
    public decimal Total { get; set; }
    public OrderStatus Status { get; set; }
}
// All logic in OrderService
```

### Rich Domain Model

```csharp
public class Order
{
    public Guid Id { get; private set; }
    public OrderStatus Status { get; private set; }
    public Money Total { get; private set; }

    public void Confirm()
    {
        if (Status != OrderStatus.Pending)
            throw new InvalidOperationException("Only pending orders can be confirmed");
        Status = OrderStatus.Confirmed;
        AddDomainEvent(new OrderConfirmedEvent(Id));
    }
}
```

**Architect decision:** Rich model for complex business rules (insurance, finance). Anemic acceptable for simple CRUD with little domain logic.

---

## 2. Domain Events

```csharp
public record OrderConfirmedEvent(Guid OrderId, DateTime ConfirmedAt) : IDomainEvent;

// Handler in Application layer
public class OrderConfirmedHandler(INotificationService notifications)
    : INotificationHandler<OrderConfirmedEvent>
{
    public async Task Handle(OrderConfirmedEvent e, CancellationToken ct)
        => await notifications.SendConfirmationAsync(e.OrderId);
}
```

**Use when:** Decouple side effects from core transaction. Enable event-driven architecture evolution.

---

## 3. Anti-Corruption Layer (ACL)

When integrating with legacy or external systems with incompatible models:

```csharp
// External legacy XML API returns LegacyOrderFormat
public class LegacyOrderAdapter : IOrderRepository
{
    public async Task<Order> GetByIdAsync(Guid id)
    {
        var legacy = await _legacyClient.FetchAsync(id);
        return MapToDomain(legacy); // ACL translation
    }
}
```

**Architect role:** Protect domain purity from external system pollution.

---

## 4. Modular Monolith

```
┌─────────────────────────────────────────┐
│           Modular Monolith             │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐  │
│  │ Orders  │ │ Payments│ │ Shipping│  │
│  │ Module  │ │ Module  │ │ Module  │  │
│  └────┬────┘ └────┬────┘ └────┬────┘  │
│       └───────────┼───────────┘        │
│              Shared Kernel              │
└─────────────────────────────────────────┘
```

**When to recommend:**
- Team not ready for microservices ops
- Need clear boundaries without distributed complexity
- Plan to extract modules to services later

**Rules:** Modules communicate via public API or events — never direct DB access across modules.

---

## 5. Expert Scenario: Architecture Review

**Context:** 8-year .NET monolith, 500K LOC, 30 developers. VP wants microservices in 6 months.

**Your response:**

1. **Assess:** No CI/CD, no containers, shared database — not ready
2. **Recommend:** Modular monolith first (3 months) → extract 1 service (3 months)
3. **First extraction candidate:** Notification service (clear boundary, async-friendly)
4. **Reject:** Big-bang 20-microservice split
5. **Metrics:** Track module coupling, deployment frequency, lead time

---

## Best Practices

1. Domain layer has zero NuGet dependencies (except maybe MediatR contracts)
2. Integration tests at application layer; unit tests at domain
3. Architecture tests (NetArchTest) enforce dependency direction
4. ADR for every architecture style choice
5. Refactor toward Clean when pain appears — don't start there for MVPs

**Next:** [diagrams/](../diagrams/) | [interview-questions/](../interview-questions/)
