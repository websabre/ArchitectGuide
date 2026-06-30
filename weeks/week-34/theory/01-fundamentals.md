# Scalability, Caching & CDN

> **Week 34** | **Module:** [caching-messaging](../../../modules/caching-messaging/README.md)

## 1. Scaling Patterns

| Pattern | Description | When |
|---------|-------------|------|
| **Vertical** | Bigger machine | Quick fix, single-node limits |
| **Horizontal** | More machines | Web APIs, stateless services |
| **Read replicas** | Scale reads | Read-heavy (10:1+) |
| **Sharding** | Partition data | Write scale, storage limits |
| **Caching** | Reduce DB load | Hot data, 80/20 rule |

---

## 2. Caching Strategies

| Strategy | Description | Risk |
|----------|-------------|------|
| **Cache-aside** | App checks cache, miss → DB → populate | Stale data |
| **Read-through** | Cache loads from DB on miss | Cache failure = miss |
| **Write-through** | Write to cache + DB together | Latency on writes |
| **Write-behind** | Write cache, async to DB | Data loss risk |

```csharp
// Cache-aside pattern
var order = await _cache.GetAsync<Order>($"order:{id}");
if (order is null)
{
    order = await _db.Orders.FindAsync(id);
    await _cache.SetAsync($"order:{id}", order, TimeSpan.FromMinutes(5));
}
```

---

## 3. Cache Invalidation

> "There are only two hard things: cache invalidation and naming things."

| Strategy | Use |
|----------|-----|
| TTL | Simple, acceptable staleness |
| Event-driven | Invalidate on update event |
| Version key | `order:123:v2` |

**Architect:** Define staleness tolerance per data type. Product catalog: 5 min OK. Stock count: seconds.

---

## 4. Redis Architecture

| Use | Redis Feature |
|-----|---------------|
| Session store | String with TTL |
| Leaderboard | Sorted Set (ZSET) |
| Rate limiting | INCR + EXPIRE |
| Distributed lock | SET NX EX |
| Pub/Sub | Real-time notifications |

**HA:** Redis Cluster or Azure Cache for Redis Enterprise with geo-replication.

---

## 5. CDN (Content Delivery Network)

```
User (Tokyo) → CloudFront/Front Door edge (Tokyo) → cache HIT → fast
                                              → cache MISS → origin (US)
```

**Cache:** Static assets (JS, CSS, images), API responses (careful with auth).

**Headers:** `Cache-Control: max-age=3600`, `ETag`, `Vary`.

---

## 6. Database Sharding

```
userId hash % 4 → Shard 0, 1, 2, 3
```

**Challenges:**
- Cross-shard queries expensive
- Rebalancing when adding shards (consistent hashing)
- Joins across shards — avoid

**Architect:** Shard when single DB hits write/storage limits — not preemptively.

**Next:** Week 35 Messaging
