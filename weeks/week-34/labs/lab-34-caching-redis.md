# Lab 34: Caching Layer with Redis (.NET)

| **Week** | 34 | **Duration** | 90 min |

## Objectives

- [ ] Implement cache-aside pattern for product catalog API
- [ ] Configure TTL and cache stampede mitigation
- [ ] Measure hit ratio with metrics

## Setup

```bash
docker run -d -p 6379:6379 redis:7-alpine
dotnet new webapi -n CacheLab
dotnet add package Microsoft.Extensions.Caching.StackExchangeRedis
dotnet add package StackExchange.Redis
```

## Cache-Aside Pattern

```csharp
public async Task<Product?> GetAsync(string id, CancellationToken ct)
{
    var cached = await _cache.GetStringAsync($"product:{id}", ct);
    if (cached != null) return JsonSerializer.Deserialize<Product>(cached);

    var product = await _db.Products.FindAsync(id);
    if (product != null)
        await _cache.SetStringAsync($"product:{id}", JsonSerializer.Serialize(product),
            new DistributedCacheEntryOptions { AbsoluteExpirationRelativeToNow = TimeSpan.FromMinutes(5) }, ct);
    return product;
}
```

## Stampede Mitigation

Use `HybridCache` (.NET 9) or lock per key for popular product refresh.

## Load Test

```bash
# Use bombardier or k6 — compare with cache disabled vs enabled
```

## Report

1. Cache hit ratio achieved?
2. When would you use write-through instead?
3. CDN vs Redis for this workload
