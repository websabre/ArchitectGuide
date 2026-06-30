# Design Patterns — Fundamentals (GoF + Enterprise)

> **Week 04** | **Module:** [design-patterns-solid](../../../modules/design-patterns-solid/README.md)

## Learning Objectives

- Apply GoF patterns in C# with architect-level judgment
- Know when patterns add value vs complexity
- Recognize anti-patterns in production codebases

---

## Creational Patterns

### Singleton

```csharp
public sealed class ConfigurationCache
{
    private static readonly Lazy<ConfigurationCache> _instance = new(() => new());
    public static ConfigurationCache Instance => _instance.Value;
}
```

**Modern .NET:** Use DI Singleton instead of static Singleton.

**Use when:** Truly one instance needed (cache, connection pool manager).
**Avoid:** Global state, testability problems.

### Factory Method / Abstract Factory

```csharp
public interface IPaymentGatewayFactory
{
    IPaymentGateway Create(string provider);
}
```

**Use when:** Object creation logic is complex or provider-specific.
**Architect use:** Multi-cloud, multi-region provider selection.

### Builder

```csharp
var email = new EmailBuilder()
    .To("user@example.com")
    .Subject("Order Confirmed")
    .Body(template)
    .Build();
```

**Use when:** Complex object construction with many optional parameters.
**Modern alternative:** Named parameters, `with` expressions for records.

---

## Structural Patterns

### Adapter

```csharp
public class StripePaymentAdapter : IPaymentGateway
{
    private readonly StripeClient _stripe;
    public async Task<PaymentResult> ChargeAsync(Money amount)
        => MapResult(await _stripe.ChargeAsync(MapRequest(amount)));
}
```

**Architect essential:** Every external integration should use Adapter (ACL).

### Decorator

```csharp
public class CachingOrderService(IOrderService inner, ICache cache) : IOrderService
{
    public async Task<Order?> GetAsync(Guid id)
    {
        return await cache.GetOrCreateAsync($"order:{id}",
            () => inner.GetAsync(id));
    }
}
```

**Use when:** Add behavior without modifying original class.
**DI registration:** `services.Decorate<IOrderService, CachingOrderService>()`

### Facade

```csharp
public class OrderFacade(IOrderService orders, IPaymentService payments, IInventoryService inventory)
{
    public async Task<PlaceOrderResult> PlaceOrderAsync(PlaceOrderRequest request)
    {
        await inventory.ReserveAsync(request.Items);
        var payment = await payments.ChargeAsync(request.Total);
        var order = await orders.CreateAsync(request);
        return new PlaceOrderResult(order.Id, payment.TransactionId);
    }
}
```

**Use when:** Simplify complex subsystem for clients. BFF is a Facade at API level.

### Proxy

Virtual proxy (lazy loading), protection proxy (access control), remote proxy (gRPC stub).

---

## Behavioral Patterns

### Strategy

```csharp
public interface IShippingStrategy { decimal Calculate(Order order); }
public class StandardShipping : IShippingStrategy { ... }
public class ExpressShipping : IShippingStrategy { ... }
```

**Use when:** Interchangeable algorithms. Often replaced by pattern matching in simple cases.

### Observer / Event

```csharp
public class Order
{
    private readonly List<IDomainEvent> _events = new();
    public IReadOnlyList<IDomainEvent> DomainEvents => _events.AsReadOnly();
    protected void Raise(IDomainEvent e) => _events.Add(e);
}
```

**Modern .NET:** MediatR, `IObservable`, domain events, message bus.

### Command (with MediatR)

```csharp
public record CancelOrderCommand(Guid OrderId, string Reason) : IRequest;
```

**Use when:** Audit trail, undo, queue processing, CQRS.

### State

```csharp
public class Order
{
    private IOrderState _state = new PendingState();
    public void Confirm() => _state = _state.Confirm(this);
}
```

**Use when:** Object behavior changes significantly by state (order workflow, document approval).

### Template Method

```csharp
public abstract class ReportGenerator
{
    public byte[] Generate() { var data = FetchData(); return Format(data); }
    protected abstract object FetchData();
    protected abstract byte[] Format(object data);
}
```

**Use when:** Algorithm skeleton fixed, steps vary.

---

## Enterprise Patterns (.NET)

| Pattern | Purpose | Modern .NET |
|---------|---------|-------------|
| Repository | Abstract persistence | DbContext directly often sufficient |
| Unit of Work | Transaction boundary | DbContext IS a UoW |
| Specification | Composable query logic | Useful for complex queries |
| Saga | Distributed transactions | Orchestration/choreography |
| Outbox | Reliable messaging | Critical for event-driven |
| Circuit Breaker | Fault tolerance | Polly library |

### Repository Debate

```csharp
// Traditional
public interface IOrderRepository
{
    Task<Order?> GetByIdAsync(Guid id);
    Task AddAsync(Order order);
}

// Pragmatic (.NET community trend)
// Use DbContext directly in handlers — EF Core already implements Repository+UoW
```

**Architect stance:** Repository adds value when:
- Swapping persistence technology
- Complex test mocking requirements
- Multiple persistence sources

Skip when EF Core is the only store and team is pragmatic.

---

## Anti-Patterns to Recognize

| Anti-Pattern | Symptom | Fix |
|--------------|---------|-----|
| God Object | 2000-line service class | SRP, extract services |
| Spaghetti Code | No structure | Layer or slice architecture |
| Golden Hammer | Patterns everywhere | YAGNI |
| Lava Flow | Dead code nobody touches | Remove, document |
| Boat Anchor | Keeping unused "future" code | Delete |
| Service Locator | `ServiceProvider.GetService<T>()` in domain | Constructor DI |

**Next:** [02-gof-deep-dive.md](02-gof-deep-dive.md)
