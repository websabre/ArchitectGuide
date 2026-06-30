# Lab 21: Resilience Patterns with Polly (.NET)

| **Week** | 21 | **Duration** | 90 min |

## Objectives
- [ ] Implement retry, circuit breaker, timeout with Polly v8
- [ ] Simulate downstream failure and observe circuit open
- [ ] Add idempotency key to command handler

## Setup
```bash
dotnet new webapi -n ResilienceLab
cd ResilienceLab
dotnet add package Microsoft.Extensions.Http.Resilience
dotnet add package Polly
```

## Step 1: HttpClient with Resilience
```csharp
builder.Services.AddHttpClient<IInventoryClient, InventoryClient>()
    .AddStandardResilienceHandler(options =>
    {
        options.Retry.MaxRetryAttempts = 3;
        options.CircuitBreaker.SamplingDuration = TimeSpan.FromSeconds(30);
        options.AttemptTimeout.Timeout = TimeSpan.FromSeconds(3);
    });
```

## Step 2: Idempotency Middleware
```csharp
app.Use(async (context, next) =>
{
    var key = context.Request.Headers["Idempotency-Key"].FirstOrDefault();
    if (key != null && await cache.ExistsAsync(key))
    {
        context.Response.StatusCode = 200;
        await context.Response.WriteAsync(await cache.GetAsync(key));
        return;
    }
    await next(context);
});
```

## Step 3: Chaos Test
Use fault injection — return 503 from mock inventory 60% of requests. Observe circuit breaker open in logs.

## Report
1. What happens without circuit breaker at 60% failure rate?
2. When is retry dangerous?
3. Document resilience policy in ADR
