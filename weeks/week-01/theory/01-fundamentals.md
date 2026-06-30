# C# Language — Fundamentals (Architect Lens)

> **Week 01** | **Level:** Fundamentals | **Module:** [csharp-dotnet](../../../modules/csharp-dotnet/README.md)

## Learning Objectives

- Explain C# type system decisions and their architectural impact
- Understand value vs reference types for API and domain modeling
- Know when language features reduce vs increase system complexity

---

## 1. Type System Overview

C# is a **statically typed**, **managed** language. For architects, the type system is a **design tool** — not just a compiler feature.

### Value Types vs Reference Types

| Aspect | Value Types (`struct`, primitives) | Reference Types (`class`) |
|--------|-----------------------------------|---------------------------|
| Storage | Stack (usually) or inline | Heap |
| Copy semantics | Copy by value | Copy by reference |
| Nullability | Non-nullable by default (structs) | Nullable unless constrained |
| GC pressure | Lower | Higher |
| Best for | Small, immutable data (coordinates, money) | Entities, services, large objects |

**Architect decision:** Use `record struct` for small immutable value objects (DTOs in hot paths). Use `class` for identity-bearing domain entities.

```csharp
// Value object — no identity, compared by value
public readonly record struct Money(decimal Amount, string Currency);

// Entity — has identity
public class Order
{
    public Guid Id { get; init; }
    public Money Total { get; set; }
}
```

### Architecture Perspective

Choosing struct vs class affects:
- **Memory allocation rate** → GC pauses in high-throughput services
- **API contracts** → serialization behavior differs (System.Text.Json)
- **Thread safety** → structs copied on assignment; classes shared by reference

---

## 2. Nullable Reference Types (NRT)

Enabled via `<Nullable>enable</Nullable>`. The compiler tracks nullability at compile time.

```csharp
public string? FindCustomerName(Guid id) => _cache.TryGetValue(id, out var name) ? name : null;

public void Process(string name) // non-nullable parameter
{
    ArgumentNullException.ThrowIfNull(name);
    // ...
}
```

**Architect impact:** NRT reduces null-reference bugs in large codebases — a significant maintainability win. Enforce in CI with `warningsAsErrors` for nullable warnings.

---

## 3. Records and Immutability

C# 9+ `record` types provide value-based equality and `with` expressions:

```csharp
public record CustomerDto(Guid Id, string Name, string Email);

var updated = customer with { Email = "new@email.com" };
```

**When architects recommend records:**
- API response models (immutable by default)
- Event/message payloads in event-driven systems
- Configuration snapshots

**When NOT to use records:**
- EF Core entities (change tracking requires mutable classes)
- Objects with complex lifecycle state machines

---

## 4. Pattern Matching

```csharp
public decimal CalculateShipping(Order order) => order switch
{
    { Total.Amount: > 1000 } => 0m,
    { ShippingAddress.Country: "US" } => 9.99m,
    { Type: OrderType.Digital } => 0m,
    _ => 19.99m
};
```

**Architect perspective:** Pattern matching reduces cyclomatic complexity in business rules — fewer nested if/else chains, more maintainable rule engines. Consider replacing Strategy pattern with pattern matching for simple rule sets.

---

## 5. Generics and Type Constraints

```csharp
public interface IRepository<T> where T : class, IEntity
{
    Task<T?> GetByIdAsync(Guid id, CancellationToken ct = default);
    Task AddAsync(T entity, CancellationToken ct = default);
}
```

**Architect note:** Generic constraints document contracts at the type level. Prefer generic repositories only at infrastructure boundaries — domain services should work with specific types.

---

## Common Mistakes

1. **Using `class` for all DTOs** — unnecessary GC pressure at scale
2. **Ignoring NRT** — leaving nullable disabled in new projects
3. **Mutable records** — defeats the purpose; use `init` accessors
4. **Over-genericizing** — `IRepository<T>` everywhere adds indirection without value

---

## Best Practices

1. Enable NRT on all new projects
2. Use `record` for DTOs and events; `class` for EF entities
3. Prefer `readonly struct` for small value types in hot paths
4. Use pattern matching to simplify business rules
5. Document type choices in ADRs for domain models

---

## Further Reading

- [C# Language Reference — Types](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/)
- [Performance best practices — .NET](https://learn.microsoft.com/en-us/dotnet/framework/performance/)

**Next:** [02-intermediate.md](02-intermediate.md) — Memory model, GC, Span/Memory
