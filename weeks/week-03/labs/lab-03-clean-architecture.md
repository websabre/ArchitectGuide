# Lab 03: Clean Architecture Solution Structure

| **Week** | 03 | **Duration** | 120 min |

## Objectives

- [ ] Create 4-project Clean Architecture solution
- [ ] Implement domain entity with behavior
- [ ] Add MediatR command/handler
- [ ] Enforce dependency rules with NetArchTest

## Steps

### 1. Create Solution

```bash
dotnet new sln -n CleanOrder
dotnet new classlib -n CleanOrder.Domain -o src/Domain
dotnet new classlib -n CleanOrder.Application -o src/Application
dotnet new classlib -n CleanOrder.Infrastructure -o src/Infrastructure
dotnet new webapi -n CleanOrder.Api -o src/Api --use-minimal-apis
dotnet sln add src/*/
```

### 2. Domain Entity (Rich Model)

```csharp
// Domain/Entities/Order.cs
public class Order
{
    public Guid Id { get; private set; }
    public OrderStatus Status { get; private set; }

    public static Order Create(Guid customerId, Money total)
    {
        return new Order
        {
            Id = Guid.NewGuid(),
            Status = OrderStatus.Pending,
            Total = total
        };
    }

    public void Confirm()
    {
        if (Status != OrderStatus.Pending)
            throw new DomainException("Cannot confirm non-pending order");
        Status = OrderStatus.Confirmed;
    }
}
```

### 3. Application Command

```csharp
public record ConfirmOrderCommand(Guid OrderId) : IRequest;
public class ConfirmOrderHandler(IOrderRepository repo) : IRequestHandler<ConfirmOrderCommand>
{
    public async Task Handle(ConfirmOrderCommand cmd, CancellationToken ct)
    {
        var order = await repo.GetByIdAsync(cmd.OrderId)
            ?? throw new NotFoundException(cmd.OrderId);
        order.Confirm();
        await repo.SaveAsync(order);
    }
}
```

### 4. Architecture Test

```bash
dotnet add src/Tests package NetArchTest.Rules
```

```csharp
[Fact]
public void Domain_Should_Not_Reference_Infrastructure()
{
    var result = Types.InAssembly(DomainAssembly)
        .ShouldNot().HaveDependencyOn("CleanOrder.Infrastructure")
        .GetResult();
    Assert.True(result.IsSuccessful);
}
```

## Lab Report

1. Why is `Confirm()` on the entity, not in the handler?
2. When would you choose Vertical Slice over this structure?
3. Write a mini-ADR for your architecture choice.
