# C# Language — Intermediate (Memory, GC, Async Foundations)

> **Week 01** | **Level:** Intermediate

## Learning Objectives

- Explain how the .NET GC affects service architecture
- Understand `Span<T>` and stack allocation for performance-critical paths
- Know async/await fundamentals and common pitfalls

---

## 1. .NET Memory Model

### Stack vs Heap

```
┌─────────────────────────────────────────┐
│                  Stack                   │
│  Local variables, value types, frames    │
├─────────────────────────────────────────┤
│                  Heap                    │
│  Reference type objects, LOH objects     │
│  ┌─────────┐ ┌─────────┐ ┌───────────┐  │
│  │ Gen 0   │ │ Gen 1   │ │ Gen 2/LOH │  │
│  └─────────┘ └─────────┘ └───────────┘  │
└─────────────────────────────────────────┘
```

### Garbage Collection Generations

| Generation | Contents | Collection Frequency |
|------------|----------|---------------------|
| Gen 0 | Short-lived objects | Most frequent |
| Gen 1 | Buffer between 0 and 2 | Moderate |
| Gen 2 | Long-lived objects | Rare, expensive |
| LOH | Objects ≥ 85,000 bytes | With Gen 2, not compacted by default |

**Architect impact:** High allocation rates in hot paths (e.g., string concatenation in loops, LINQ in request handlers) cause Gen 0/1 collections → latency spikes. Monitor `% Time in GC` in production.

---

## 2. Span<T> and Memory<T>

`Span<T>` provides stack-safe, zero-copy access to contiguous memory:

```csharp
ReadOnlySpan<char> span = input.AsSpan();
var slice = span.Slice(0, 10);
```

**Use cases architects should know:**
- Parsing protocols without allocating substrings
- Buffer pooling in high-throughput APIs
- Interop with native memory

**When to recommend:** Services processing >10K RPS with string manipulation bottlenecks.

---

## 3. async/await Fundamentals

```csharp
public async Task<Order> GetOrderAsync(Guid id, CancellationToken ct)
{
    var order = await _db.Orders.FindAsync(id, ct);
    if (order is null) throw new NotFoundException(id);
    return order;
}
```

### How It Works (Simplified)

1. Method returns `Task` immediately when hitting `await`
2. Thread returns to thread pool
3. When I/O completes, continuation runs (possibly different thread)
4. No thread blocked during I/O wait

### Architect Rules for Async

| Rule | Rationale |
|------|-----------|
| Async all the way | Mixing sync/async causes deadlocks |
| Always pass `CancellationToken` | Enables graceful shutdown in K8s |
| Never `async void` except event handlers | Unhandled exceptions crash process |
| Avoid `Task.Result` / `.Wait()` | Causes thread pool starvation |

---

## 4. IAsyncEnumerable<T>

```csharp
public async IAsyncEnumerable<Order> StreamOrdersAsync(
    [EnumeratorCancellation] CancellationToken ct)
{
    await foreach (var order in _db.Orders.AsAsyncEnumerable().WithCancellation(ct))
    {
        yield return order;
    }
}
```

**Architect use case:** Streaming large datasets without loading into memory — critical for export APIs, ETL pipelines, and report generation.

---

## 5. LINQ and Allocation Awareness

```csharp
// Allocates intermediate collections
var result = orders.Where(o => o.IsActive).Select(o => o.Total).ToList();

// More efficient for large collections
var sum = 0m;
foreach (var order in orders)
{
    if (order.IsActive) sum += order.Total;
}
```

**Architect perspective:** LINQ is fine for most business logic. In hot paths (>1K items per request, high RPS), profile and consider explicit loops or `Span<T>`.

---

## Production Example

**Scenario:** Payment API at 5K RPS experiencing p99 latency spikes.

**Investigation:** dotMemory showed Gen 0 collections every 200ms. Root cause: JSON deserialization creating temporary strings, LINQ chains on every request.

**Fix:**
- Source-generated `System.Text.Json` serializers
- Object pooling for request DTOs
- Replaced LINQ with foreach in hot path

**Result:** p99 dropped from 180ms to 45ms; GC time reduced 60%.

---

## Trade-offs

| Approach | Pros | Cons |
|----------|------|------|
| LINQ everywhere | Readable, maintainable | Allocations in hot paths |
| Manual loops + Span | Performance | Harder to maintain |
| Value types for DTOs | Less GC | Serialization complexity |
| IAsyncEnumerable | Memory efficient streaming | More complex consumer code |

---

## Common Mistakes

1. **`ConfigureAwait(false)` in library code only** — not needed in ASP.NET Core app code
2. **Blocking on async** — `.Result` in controllers causes thread pool starvation
3. **Ignoring CancellationToken** — pods killed mid-operation without cleanup
4. **Premature optimization** — micro-optimizing before profiling

---

**Next:** [03-advanced.md](03-advanced.md) — Async internals, performance engineering
