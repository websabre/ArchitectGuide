# Lab 01: C# Performance Profiling & Memory Analysis

| Attribute | Value |
|-----------|-------|
| **Week** | 01 |
| **Duration** | 90 minutes |
| **Prerequisites** | .NET 8 SDK, IDE with debugger |
| **Difficulty** | Intermediate |

## Objectives

- [ ] Profile a .NET API to identify allocation hotspots
- [ ] Apply `ArrayPool` and source-generated JSON to reduce allocations
- [ ] Measure before/after GC metrics
- [ ] Write an architect-style performance report

## Architecture Context

Architects don't micro-optimize every line — but they must **recognize when performance architecture matters** and **direct teams to profile before rewriting**. This lab builds that instinct.

---

## Environment Setup

```bash
dotnet new webapi -n PerfLab -o perf-lab
cd perf-lab
dotnet add package BenchmarkDotNet
```

---

## Step 1: Create the Baseline API

Add `Controllers/OrdersController.cs`:

```csharp
[ApiController]
[Route("api/[controller]")]
public class OrdersController : ControllerBase
{
    private static readonly List<Order> _orders = Enumerable
        .Range(1, 10000)
        .Select(i => new Order(i, $"Customer-{i % 100}", i * 10.5m))
        .ToList();

    [HttpGet("slow")]
    public IActionResult GetSlow([FromQuery] string filter)
    {
        var result = _orders
            .Where(o => o.CustomerName.Contains(filter, StringComparison.OrdinalIgnoreCase))
            .Select(o => new { o.Id, o.CustomerName, o.Total, Label = $"Order #{o.Id} - {o.CustomerName}" })
            .OrderByDescending(o => o.Total)
            .Take(100)
            .ToList();
        return Ok(result);
    }
}

public record Order(int Id, string CustomerName, decimal Total);
```

Run: `dotnet run` and test: `curl "http://localhost:5000/api/orders/slow?filter=customer-5"`

**Architect note:** This endpoint allocates on every request — LINQ intermediates, anonymous types, string concatenation.

---

## Step 2: Profile with dotnet-counters

```bash
# Terminal 1
dotnet run

# Terminal 2 — find process ID, then:
dotnet-counters monitor --process-id <PID> System.Runtime
```

Make 100 requests (use a loop or `ab`/`wrk`). Observe:
- `GC Heap Size`
- `% Time in GC`
- `Allocation Rate`

Record baseline metrics in your lab report.

---

## Step 3: Optimize the Hot Path

Create `Controllers/OrdersControllerOptimized.cs`:

```csharp
[HttpGet("fast")]
public IActionResult GetFast([FromQuery] string filter)
{
    var buffer = new List<OrderResult>(100);
    foreach (var order in _orders)
    {
        if (order.CustomerName.Contains(filter, StringComparison.OrdinalIgnoreCase))
        {
            buffer.Add(new OrderResult(order.Id, order.CustomerName, order.Total));
        }
    }
    buffer.Sort((a, b) => b.Total.CompareTo(a.Total));
    if (buffer.Count > 100) buffer.RemoveRange(100, buffer.Count - 100);
    return Ok(buffer);
}

public readonly record struct OrderResult(int Id, string CustomerName, decimal Total);
```

---

## Step 4: Benchmark Comparison

Add a BenchmarkDotNet project or use `dotnet-counters` again on `/fast` endpoint.

Compare:
| Metric | /slow | /fast |
|--------|-------|-------|
| Allocation rate | | |
| % Time in GC | | |
| p99 latency (approx) | | |

---

## Step 5: Source-Generated JSON (Optional Advanced)

```csharp
[JsonSerializable(typeof(OrderResult))]
[JsonSerializable(typeof(OrderResult[]))]
public partial class AppJsonContext : JsonSerializerContext { }

// In Program.cs:
builder.Services.ConfigureHttpJsonOptions(options =>
{
    options.SerializerOptions.TypeInfoResolverChain.Insert(0, AppJsonContext.Default);
});
```

---

## Verification

- [ ] Baseline metrics recorded
- [ ] Optimized endpoint shows lower allocation rate
- [ ] Lab report completed (see below)

---

## Break-It Exercise

Add `async void ProcessOrders()` called from the controller. Observe what happens when an exception is thrown. Document why architects ban `async void` in production services.

---

## Lab Report Prompt

Answer in writing:

1. What was the primary allocation source in the slow endpoint?
2. Would you recommend this optimization for all endpoints? Why or why not?
3. At what scale (RPS) would this optimization matter for a typical enterprise API?
4. What observability would you add in production to catch this class of problem?

---

## Cleanup

```bash
cd .. && rm -rf perf-lab
```
