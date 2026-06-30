# C# Language — Advanced & Expert

> **Week 01** | **Level:** Advanced → Expert

## Learning Objectives

- Understand async state machine internals for debugging production issues
- Apply performance engineering patterns in .NET services
- Make informed language feature decisions at architecture reviews

---

## 1. Async State Machine Internals

The compiler transforms `async` methods into state machine classes:

```csharp
// What you write
public async Task<int> ComputeAsync()
{
    var a = await GetAAsync();
    var b = await GetBAsync();
    return a + b;
}

// Conceptually what compiler generates (simplified)
class ComputeAsyncStateMachine : IAsyncStateMachine
{
    int state;
    int a, b;
    TaskAwaiter awaiter;
    // MoveNext() switches on state...
}
```

**Architect relevance:** Each `await` in a method = state machine overhead + potential heap allocation for the machine itself. Methods with many awaits in tight loops may benefit from refactoring.

**Debugging tip:** Stack traces show `MoveNext()` — this is normal async behavior, not a framework bug.

---

## 2. Performance Engineering Patterns

### ArrayPool<T>

```csharp
var buffer = ArrayPool<byte>.Shared.Rent(4096);
try
{
    // use buffer
}
finally
{
    ArrayPool<byte>.Shared.Return(buffer);
}
```

### Object Pooling (Microsoft.Extensions.ObjectPool)

```csharp
builder.Services.AddSingleton<ObjectPoolProvider, DefaultObjectPoolProvider>();
builder.Services.AddSingleton(serviceProvider =>
{
    var provider = serviceProvider.GetRequiredService<ObjectPoolProvider>();
    return provider.Create(new StringBuilderPooledObjectPolicy());
});
```

### Source Generators (.NET 6+)

```csharp
[JsonSerializable(typeof(OrderDto))]
public partial class AppJsonContext : JsonSerializerContext { }

// Zero-reflection serialization
var json = JsonSerializer.Serialize(order, AppJsonContext.Default.OrderDto);
```

**When architects mandate these:**
- Services with SLA < 50ms p99
- High-throughput event processors
- AOT compilation requirements (Native AOT, trimming)

---

## 3. Native AOT and Trimming

.NET 8+ supports ahead-of-time compilation:

| Aspect | JIT (default) | Native AOT |
|--------|---------------|------------|
| Startup time | Slower (JIT warmup) | Fast (no JIT) |
| Memory footprint | Higher | Lower |
| Reflection | Full | Limited |
| Dynamic code | Supported | Restricted |
| Best for | General web APIs | Microservices, CLI tools, edge |

**Architect decision framework:**
- Choose AOT for: serverless cold start, container density, edge deployment
- Avoid AOT for: heavy reflection, dynamic plugin systems, EF Core (limited support)

---

## 4. C# 12–13 Features for Architects

### Primary Constructors

```csharp
public class OrderService(IOrderRepository repo, ILogger<OrderService> logger)
{
    public async Task<Order> GetAsync(Guid id) => await repo.GetByIdAsync(id);
}
```

Reduces boilerplate; use for simple DI services. Avoid for classes with complex initialization logic.

### Collection Expressions

```csharp
int[] numbers = [1, 2, 3, 4, 5];
List<string> names = ["Alice", "Bob"];
```

### `ref readonly` Parameters

For large structs passed without copying:

```csharp
public decimal Calculate(ref readonly LargeStruct data) { ... }
```

---

## 5. Expert: Language Choice in System Design

### When C# Is the Right Choice

- Enterprise .NET shops with existing investment
- High-performance backends with .NET 8+ optimizations
- Azure-first architectures (best SDK/integration support)
- Teams with strong C# expertise

### When to Consider Alternatives

| Scenario | Consider | Why |
|----------|----------|-----|
| Extreme low-latency trading | Rust, C++ | No GC pauses |
| ML inference serving | Python, Go | Ecosystem |
| Simple CRUD, small team | Node, Go | Faster iteration |
| Polyglot microservices | Go, Java | Team diversity |

**Architect role:** Language choice is a **team + ecosystem + operational** decision — not a performance beauty contest.

---

## Scenario: Architect Review

**Question:** "Should we rewrite our payment service from C# to Go for performance?"

**Structured answer:**
1. **Profile first** — is C# actually the bottleneck? (DB, network, serialization?)
2. **Measure current** — p50/p99 latency, throughput, GC metrics
3. **Team cost** — Go expertise? Dual maintenance during migration?
4. **Ecosystem** — payment SDKs, compliance libraries in Go?
5. **Operational** — existing .NET observability, deployment pipelines
6. **Recommendation:** Optimize C# first (source gen JSON, pooling, DB query tuning). Revisit if p99 still exceeds SLA after optimization.

---

## Best Practices (Expert Level)

1. **Profile before optimizing** — dotTrace, PerfView, Application Insights
2. **Set performance budgets** — e.g., "request handler < 5ms excluding I/O"
3. **GC awareness in design reviews** — question allocation-heavy patterns
4. **Async discipline** — CancellationToken everywhere, no sync-over-async
5. **Document language decisions** in ADRs with measurable criteria

---

**Next:** [diagrams/](../diagrams/) | [interview-questions/](../interview-questions/)
