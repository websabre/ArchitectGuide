# Week 34 — Fundamentals Interview Q&A

> Q001–Q030: Premium format (Week 1 quality).
> See also: [Interview prep hub](../../../interview-prep/README.md)

---


## Q001: Cache-Aside Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Caching |
| **Frequency** | Very Common |

### Question

Explain cache-aside. Cache miss flow?

### Short Answer (30 seconds)

App checks cache → miss → read DB → populate cache → return. On write: update DB → invalidate or update cache.

### Detailed Answer (3–5 minutes)

Standard for Redis + SQL. TTL prevents stale forever. Stampede protection on hot keys.

Read-through/write-through alternatives when cache layer owns load logic.

### Architecture Perspective

Cache-aside is default architect pattern.

### Follow-up Questions

1. **Cache penetration? — Bloom filter for non-existent keys.**
2. **Cache avalanche? — Stagger TTLs — random jitter.**

### Common Mistakes in Interviews

- Cache without TTL
- Write DB without cache invalidation
- Thundering herd on hot key expiry

---

## Q002: CDN Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | CDN |
| **Frequency** | Very Common |

### Question

When CDN vs origin-only?

### Short Answer (30 seconds)

CDN for static assets, video, global users, DDoS absorption. Origin for dynamic personalized API unless edge compute.

### Detailed Answer (3–5 minutes)

CloudFront/Front Door: cache static `/assets/*`, pass-through `/api/*`. Geo routing for latency.

Cache invalidation on deploy — versioned filenames `app.v123.js`.

### Architecture Perspective

CDN is edge architecture decision.

### Follow-up Questions

1. **Edge compute? — Lambda@Edge, CloudFront Functions — auth geo block.**
2. **Cache key design? — Vary by `Accept-Language` if needed.**

### Common Mistakes in Interviews

- CDN for personalized JSON API
- No cache bust on deploy
- Origin exposed without CDN DDoS protection

---

## Q003: Horizontal Scaling

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Scale |
| **Frequency** | Very Common |

### Question

Scale web tier from 1K to 100K RPS.

### Short Answer (30 seconds)

Stateless app servers behind L7 LB. Session in Redis not sticky server memory. Auto-scale on CPU/RPS. DB becomes bottleneck next — read replicas then shard.

### Detailed Answer (3–5 minutes)

Remove server affinity. Externalize sessions. Connection pool to DB per instance — watch total DB connections = instances × pool size.

### Architecture Perspective

Horizontal scale requires stateless design.

### Follow-up Questions

1. **Sticky sessions when needed? — Prefer Redis session store over LB stickiness.**
2. **Auto-scale signal? — RPS or queue depth — not CPU alone.**

### Common Mistakes in Interviews

- In-memory session on scaled servers
- DB connection exhaustion
- Stateful app servers behind LB

---

## Q004: Database Sharding Key

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Sharding |
| **Frequency** | Very Common |

### Question

Choose shard key for multi-tenant SaaS orders.

### Short Answer (30 seconds)

`tenantId` — co-locate tenant data — efficient tenant queries. Hot large tenant risk — salting or dedicated shard for enterprise tier.

### Detailed Answer (3–5 minutes)

Avoid shard key with poor cardinality. Queries must include shard key or scatter-gather expensive.

Re-sharding plan: consistent hashing, dual-write migration.

### Architecture Perspective

Shard key is hardest to change — get right early.

### Follow-up Questions

1. **Cross-shard query? — Fan-out to all shards — avoid in hot path.**
2. **Tenant dedicated shard? — Enterprise SLA — isolate noisy neighbor.**

### Common Mistakes in Interviews

- UserId shard for tenant-scoped queries
- Shard key not in queries
- No plan for resharding

---

## Q005: Read Replica Lag

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Replication |
| **Frequency** | Common |

### Question

Product catalog read replica 30s lag — acceptable?

### Short Answer (30 seconds)

Often yes for browse — not for inventory count at checkout. Route critical reads to primary or use sync replication for stock.

### Detailed Answer (3–5 minutes)

Display 'prices may update' vs hard correctness on payment amount from primary snapshot.

### Architecture Perspective

Lag tolerance is business decision documented in ADR.

### Follow-up Questions

1. **Read-your-writes? — Route user's reads to primary briefly after write.**
2. **Global replicas? — Cross-region lag higher — geo routing aware.**

### Common Mistakes in Interviews

- All reads to lagging replica
- Inventory oversell from stale read
- No lag monitoring

---

## Q006: Rate Limiting Algorithms

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Rate Limiting |
| **Frequency** | Common |

### Question

Token bucket vs sliding window for API rate limit?

### Short Answer (30 seconds)

Token bucket: smooth burst allowance. Sliding window: precise requests per minute. Fixed window: simple but boundary burst.

### Detailed Answer (3–5 minutes)

Implement in Redis with Lua script atomicity. Return `429` + `Retry-After`.

Per-user and global limits — global protects platform.

### Architecture Perspective

Rate limiting protects availability — architect specifies at gateway.

### Follow-up Questions

1. **Distributed rate limit? — Redis central — not per-node counters.**
2. **Whitelist internal services? — Carefully — mTLS identity based.**

### Common Mistakes in Interviews

- No rate limit on public API
- Per-server limit only — uneven
- Rate limit without client feedback headers

---

## Q007: Hot Partition Problem

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Sharding |
| **Frequency** | Common |

### Question

Celebrity user breaks shard — mitigation?

### Short Answer (30 seconds)

Separate handling: dedicated shard, cache layer, async fan-out, read replicas for that key. Detect hot keys via metrics.

### Detailed Answer (3–5 minutes)

Twitter fan-out on read for celebrities instead of write to all followers.

General: monitor shard QPS variance — rebalance.

### Architecture Perspective

Hot key is common failure at scale — anticipate in design.

### Follow-up Questions

1. **Key salting? — `userId#random` spread writes — complicates reads.**
2. **Local cache on app for hot key? — Short TTL — reduce shard load.**

### Common Mistakes in Interviews

- Uniform sharding assumption
- No hot key monitoring
- Same path for celebrity and normal user

---

## Q008: Autoscaling Signals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Cloud Scale |
| **Frequency** | Common |

### Question

What metrics trigger autoscale for API tier?

### Short Answer (30 seconds)

RPS, CPU, request queue depth, p95 latency. Scale out cooldown prevents flapping. Pre-warm before known events.

### Detailed Answer (3–5 minutes)

K8s HPA: CPU + custom metrics from Prometheus. App Service: CPU + schedule rules.

Scale-in slowly — drain connections.

### Architecture Perspective

Autoscale policy is architecture not ops afterthought.

### Follow-up Questions

1. **Predictive scaling? — Schedule before Black Friday — historical pattern.**
2. **KEDA on queue depth? — Scale consumers with backlog.**

### Common Mistakes in Interviews

- CPU-only autoscale misses I/O bound
- Aggressive scale-in kills requests
- No max instance cap — cost runaway

---

## Q009: Multi-Region Active-Passive

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Availability |
| **Frequency** | Common |

### Question

Design active-passive multi-region for 99.99% SLA.

### Short Answer (30 seconds)

Active region serves traffic; passive warm standby. DNS/Traffic Manager failover on health check failure. Async replication — RPO > 0.

### Detailed Answer (3–5 minutes)

Document failover runbook: detection, decision, DNS flip, validation, comms.

Passive region: smaller footprint — scale on failover (cold/warm).

### Architecture Perspective

Multi-region is cost + complexity — justify with SLA revenue.

### Follow-up Questions

1. **Active-active when? — 99.99%+ and global users — conflict resolution harder.**
2. **Split brain during failover? — Ensure single writer — fencing.**

### Common Mistakes in Interviews

- Sync replication cross-region latency
- No failover tested annually
- DNS TTL 3600 slows failover

---

## Q010: Cost at Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

Estimate cost drivers at 100K RPS.

### Short Answer (30 seconds)

Compute instances, DB (largest often), cache, egress bandwidth, CDN. Egress often surprise — keep traffic in-region.

### Detailed Answer (3–5 minutes)

Order of magnitude with pricing calculator. Unit economics: $/million requests.

Architect proposes tiered architecture — cache reduces DB cost 10x.

### Architecture Perspective

Cost awareness completes scalability answer.

### Follow-up Questions

1. **Reserved capacity? — Baseline RIs + burst on-demand.**
2. **Egress optimization? — CDN, compress responses, regional data.**

### Common Mistakes in Interviews

- Ignore egress in estimate
- Over-provision 'just in case' forever
- No cache — DB scales linearly expensive

---

## Q011: Cache-Aside Deep Dive

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Caching |
| **Frequency** | Very Common |

### Question

Walk through cache-aside on product detail page: read, write, delete flows.

### Short Answer (30 seconds)

Read: cache get → miss → DB → set cache TTL 5m. Write: update DB → delete cache key (invalidate). Delete: DB delete → cache delete.

### Detailed Answer (3–5 minutes)

**Why invalidate not update on write?** Avoid race: two writes reorder → stale cache if update not delete.

**TTL:** Safety net if invalidation missed. **Jitter:** Random ±10% TTL prevents simultaneous expiry.

**Negative cache:** Cache 'not found' briefly — prevent DB hammer on invalid SKU.

### Architecture Perspective

Cache-aside nuances beyond the one-liner — interviewers probe write path.

### Follow-up Questions

1. **Read-through difference? — Cache layer loads on miss — app simpler.**
2. **Write-through? — Write cache and DB sync — higher write latency.**

### Common Mistakes in Interviews

- Update cache on write without invalidation strategy
- No TTL safety net
- Cache product object without version field

---

## Q012: Read-Through vs Write-Through Cache

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Caching |
| **Frequency** | Common |

### Question

When read-through or write-through vs cache-aside?

### Short Answer (30 seconds)

Read-through: cache library loads from DB on miss — good when cache product owns loading. Write-through: every write goes to cache and DB synchronously — strong consistency, slower writes.

### Detailed Answer (3–5 minutes)

**Cache-aside:** App orchestrates — most flexible, common in microservices.

**Write-behind:** Write cache async flush to DB — fast writes, data loss risk on crash.

**Choose write-through:** Financial balance display where cache must match DB. **Choose aside:** General CRUD with tolerance for brief staleness.

### Architecture Perspective

Pattern choice reflects consistency vs latency trade-off.

### Follow-up Questions

1. **Write-behind use case? — Analytics counters — loss acceptable.**
2. **Cache coherency multi-region? — Invalidation pub/sub across regions.**

### Common Mistakes in Interviews

- Write-behind for payment balances
- Read-through without stampede protection
- Same pattern for all data types

---

## Q013: Cache Stampede Prevention

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Caching |
| **Frequency** | Very Common |

### Question

Hot product expires from cache — 10K requests hit DB simultaneously. Fix?

### Short Answer (30 seconds)

Mutex per key: first request rebuilds, others wait or serve stale. Probabilistic early refresh. Request coalescing (singleflight pattern).

### Detailed Answer (3–5 minutes)

**Singleflight:** `sync.Map` or Redis lock `SET key NX` — one winner rebuilds.

**Stale-while-revalidate:** Return stale value while async refresh — user sees old price briefly.

**Never:** Infinite TTL on hot keys without invalidation path.

### Architecture Perspective

Stampede kills DB during exactly the moment cache should help.

### Follow-up Questions

1. **Lock timeout? — Prevent dead lock if builder crashes — TTL on lock key.**
2. **Thundering herd on app deploy? — Warm cache before traffic shift.**

### Common Mistakes in Interviews

- No protection on popular key expiry
- Blocking lock without timeout
- Drop requests instead of stale-while-revalidate

---

## Q014: CDN Cache Invalidation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | CDN |
| **Frequency** | Common |

### Question

Deploy new React bundle — how invalidate CDN without downtime?

### Short Answer (30 seconds)

Prefer cache busting: filename hash `app.a1b2c3.js` — new deploy = new URL — no invalidation needed. Purge API only for HTML entry or emergency.

### Detailed Answer (3–5 minutes)

**Immutable assets:** Long `Cache-Control: max-age=31536000, immutable` on hashed files.

**HTML:** Short TTL or no-cache — points to latest hashed assets.

**Invalidation cost:** CloudFront invalidation has limits and propagation delay — design around versioning.

**API cache:** Selective purge by tag if edge caches API responses.

### Architecture Perspective

Versioned filenames beat purge APIs in production deploys.

### Follow-up Questions

1. **Wildcard purge? — Expensive — last resort.**
2. **Stale CDN after deploy? — Users on old HTML until TTL — acceptable brief window.**

### Common Mistakes in Interviews

- Same filename every deploy
- Rely on manual CDN purge in CI without automation
- Cache personalized API responses at CDN without Vary

---

## Q015: Horizontal vs Vertical Scaling

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Scale |
| **Frequency** | Very Common |

### Question

When scale up (bigger VM) vs scale out (more instances)?

### Short Answer (30 seconds)

Vertical first for stateful legacy or quick fix — ceiling at largest SKU. Horizontal for stateless web/API tiers — preferred long-term. DB vertical until shard required.

### Detailed Answer (3–5 minutes)

**Vertical limits:** Single machine max RAM/CPU, no HA. **Horizontal needs:** Stateless app, shared session store, load balancer.

**Cost curve:** 2× large VM often > 2× small VMs — but ops simplicity varies.

**Interview:** 'Start vertical for DB primary; scale out app tier from day one if stateless.'

### Architecture Perspective

Scale direction shows production pragmatism vs textbook only.

### Follow-up Questions

1. **Kubernetes vertical pod autoscaler? — Niche — horizontal default.**
2. **DB scale up then read replicas then shard — classic sequence.**

### Common Mistakes in Interviews

- Horizontal stateful app with in-memory session
- Vertical scale forever ignoring ceiling
- Shard before read replicas exhausted

---

## Q016: Database Read Replica Lag Handling

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Replication |
| **Frequency** | Very Common |

### Question

User updates profile then sees old name on next read — replica lag 2s. Solutions?

### Short Answer (30 seconds)

Read-your-writes: route user's reads to primary for N seconds after write, or session stickiness to primary, or version check client-side.

### Detailed Answer (3–5 minutes)

**Patterns:**
1. **Primary read after write** — flag in session
2. **Synchronous replica** — for critical reads (inventory)
3. **Client polling** — return version token, client retries until match

**Product tolerance:** Profile 2s lag maybe OK; payment status not OK.

### Architecture Perspective

Replica lag is default — architects design read routing explicitly.

### Follow-up Questions

1. **Global Database (Spanner/Cosmos multi-write)? — Strong consistency — higher cost/latency.**
2. **Monitor lag? — Alert replica lag > 5s — auto-failover read to primary.**

### Common Mistakes in Interviews

- All reads to replica always
- No lag metric monitored
- Inventory check on async replica

---

## Q017: Sharding Key Selection Deep Dive

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Sharding |
| **Frequency** | Very Common |

### Question

Evaluate shard keys for global payments ledger.

### Short Answer (30 seconds)

`userId`: good user history queries, hot whale users. `paymentId`: even write spread, bad user history (scatter). `regionId+userId`: locality + isolation.

### Detailed Answer (3–5 minutes)

**Criteria:** High cardinality, even distribution, query patterns include shard key, avoid cross-shard transactions.

**Hot key mitigation:** Salting `userId#bucket`, dedicated shard for whales.

**Resharding:** Consistent hashing, dual-write migration — plan before 1TB.

**Interview:** Justify with access patterns — no universal best key.

### Architecture Perspective

Shard key is hardest migration — defend choice with queries listed.

### Follow-up Questions

1. **Cross-shard ACID? — Avoid — saga per payment flow.**
2. **Monotonic shard split? — Split hot shard into two — rehash subset.**

### Common Mistakes in Interviews

- Shard by month on infinite growth table
- Key not in 80% of queries
- No hot key detection plan

---

## Q018: Hot Partition Mitigation Strategies

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Sharding |
| **Frequency** | Common |

### Question

DynamoDB partition throttling on single hot partition — mitigation playbook?

### Short Answer (30 seconds)

Detect via `ConsumedWriteCapacityUnits` per key. Write sharding: append random suffix to sort key. Burst capacity credits temporary. DAX cache for hot reads.

### Detailed Answer (3–5 minutes)

**AWS:** Partition limit 3000 RCU/1000 WCU per partition — design sort key distribution.

**Application:** Local in-process cache for celebrity key — 1s TTL.

**Architecture:** Separate hot path — celebrity table or dedicated shard.

**Prevention:** Load test with realistic Zipf distribution not uniform.

### Architecture Perspective

Hot partitions appear at scale — proactive detection in design review.

### Follow-up Questions

1. **Write sharding read cost? — Scatter-gather on read — acceptable for writes.**
2. **Kafka hot partition? — More partitions + keyed sub-partition salt.**

### Common Mistakes in Interviews

- Assume uniform key distribution forever
- No CloudWatch per-key metrics
- Infinite retry on throttling

---

## Q019: Custom Autoscaling Metrics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Cloud Scale |
| **Frequency** | Common |

### Question

Design autoscaling beyond CPU: custom metrics for order API.

### Short Answer (30 seconds)

Scale on `requests_per_second`, `p95_latency`, and `queue_depth` composite. K8s HPA with Prometheus adapter. Scale-out aggressive, scale-in slow with cooldown.

### Detailed Answer (3–5 minutes)

**Metrics:**
- RPS from load balancer
- Custom app metric: checkout queue length
- Saturation: thread pool queue depth

**Predictive:** Scheduled scale before Black Friday + reactive on RPS.

**Avoid:** CPU-only when I/O bound waiting on DB.

### Architecture Perspective

Custom metrics tie scaling to user-visible SLO not infrastructure proxy.

### Follow-up Questions

1. **KEDA? — Scale on Service Bus queue depth — event-driven workloads.**
2. **Max instances cap? — Cost guardrail — alert before cap hit.**

### Common Mistakes in Interviews

- CPU-only HPA on I/O-bound API
- Scale-in during active requests
- No cooldown — flapping

---

## Q020: Connection Pool Storms

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Database |
| **Frequency** | Common |

### Question

Deploy 50 new API pods — DB connections spike to 5000, DB max 500. Fix?

### Short Answer (30 seconds)

Reduce per-pod pool size (10 not 100). PgBouncer/RDS Proxy connection multiplexer. Stagger rollout. Right-size pool: `max_connections / expected_pods`.

### Detailed Answer (3–5 minutes)

**Formula:** `pool_per_instance = floor(DB_max * 0.8 / max_instances)`.

**Proxy:** Transaction vs session pooling mode — know ORM compatibility.

**Architect:** Connection budget in deployment checklist — same importance as CPU.

### Architecture Perspective

Connection storms cause outages on deploy — architect prevents by math.

### Follow-up Questions

1. **RDS Proxy vs PgBouncer? — Managed vs self-hosted — similar role.**
2. **Long idle connections? — Pool timeout — release to proxy.**

### Common Mistakes in Interviews

- Default pool 100 per pod
- No connection proxy at scale
- Big bang deploy all pods simultaneously

---

## Q021: Async Processing at Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Async |
| **Frequency** | Very Common |

### Question

Move order confirmation email off sync path — async architecture?

### Short Answer (30 seconds)

Order API writes DB + outbox row → returns 201. Relay worker publishes `OrderConfirmed` → email consumer sends async. User sees confirmation page immediately.

### Detailed Answer (3–5 minutes)

**Benefits:** Shorter p99 API latency, independent scaling of email workers, retry without blocking user.

**UX:** Poll status or WebSocket if user must see 'email sent'.

**Backpressure:** Queue depth triggers scale-out of consumers.

### Architecture Perspective

Async is default architect response to non-critical path work.

### Follow-up Questions

1. **Transactional outbox? — Guarantees event published iff order saved.**
2. **Poison email template? — DLQ — don't block order queue.**

### Common Mistakes in Interviews

- Sync SMTP in checkout request
- No outbox — dual-write race
- Unbounded queue without consumer scale

---

## Q022: Message Queue Backpressure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Messaging |
| **Frequency** | Common |

### Question

Queue depth growing faster than consumers process — backpressure strategy?

### Short Answer (30 seconds)

Scale consumers (KEDA on queue depth). Throttle producers when depth > threshold. Shed load: reject new orders with 503. Priority queue: process paid orders first.

### Detailed Answer (3–5 minutes)

**Signals:** Age of oldest message, depth, consumer lag.

**Prevention:** Capacity plan consumers for peak × 1.5 headroom.

**Cascading:** Don't unbounded buffer — memory explodes — push back to caller.

### Architecture Perspective

Backpressure protects system from overload collapse.

### Follow-up Questions

1. **Dead letter before infinite retry? — Yes — poison stops pipeline.**
2. **Batch consume? — Higher throughput — tune batch size vs latency.**

### Common Mistakes in Interviews

- Unbounded in-memory queue
- Scale producers not consumers
- No alert on queue age

---

## Q023: Stateless Application Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Architecture |
| **Frequency** | Very Common |

### Question

What must leave the app server for true horizontal scale?

### Short Answer (30 seconds)

Session state → Redis. Uploaded files → object storage. Job state → queue/DB. In-memory caches → shared Redis. Config → env/Key Vault not local file.

### Detailed Answer (3–5 minutes)

**Stateless checklist:** Any pod can handle any request. Rolling deploy safe. No sticky session requirement.

**Exceptions:** WebSocket connection state on gateway node — use Redis pub/sub bridge.

**12-factor:** Processes disposable — crash OK, restart clean.

### Architecture Perspective

Stateless is prerequisite for autoscale and zero-downtime deploy.

### Follow-up Questions

1. **Sticky sessions workaround? — Admit state on connection — document limitation.**
2. **Local disk temp? — Ephemeral OK if reconstructable.**

### Common Mistakes in Interviews

- Session in Tomcat memory
- Local file upload storage
- Assuming sticky LB solves everything

---

## Q024: Session Externalization with Redis

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Caching |
| **Frequency** | Common |

### Question

Design shared session store for 20 API instances.

### Short Answer (30 seconds)

ASP.NET `AddStackExchangeRedisCache` or JWT-only stateless. Session: `sessionId` cookie → Redis hash `session:{id}` TTL 24h sliding.

### Detailed Answer (3–5 minutes)

**Data in session:** UserId, tenantId, cartId — not large objects.

**Security:** HttpOnly, Secure, SameSite cookie. Rotate session ID on login.

**Failover:** Redis cluster with replication — session loss on failover acceptable brief re-login.

### Architecture Perspective

External session enables scale and deploy without drain.

### Follow-up Questions

1. **JWT vs server session? — JWT scales better — revocation harder.**
2. **GDPR session delete? — User delete purges Redis keys.**

### Common Mistakes in Interviews

- 20MB session object in Redis
- No TTL on session keys
- Redis single node no HA

---

## Q025: Content Hashing for Cache and CDN

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Caching |
| **Frequency** | Common |

### Question

Use content hashing in architecture — examples?

### Short Answer (30 seconds)

Asset URLs: `bundle.[contenthash].js` — immutable CDN cache. API: ETag `If-None-Match` — 304 saves bandwidth. Dedup storage: hash blob → skip upload if exists.

### Detailed Answer (3–5 minutes)

**ETag flow:** Server hashes response body → client sends `If-None-Match` → 304 no body.

**Storage dedup:** Same file uploaded twice → one physical copy — backup systems use this.

**Cache key:** Hash of normalized query params for search cache.

### Architecture Perspective

Hashing enables efficient cache validation and storage deduplication.

### Follow-up Questions

1. **Weak vs strong ETag? — Byte-identical vs semantic equivalence.**
2. **Hash algorithm? — SHA-256 for dedup; MD5 OK for cache key non-security.**

### Common Mistakes in Interviews

- ETag ignored on large API responses
- Hash in URL for dynamic personalized content
- MD5 for security-sensitive dedup keys

---

## Q026: Edge Computing Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Edge |
| **Frequency** | Common |

### Question

When use edge compute (CloudFront Functions, Lambda@Edge) vs origin?

### Short Answer (30 seconds)

Edge: auth token validation, geo routing, A/B test assignment, header rewrite, bot detection — sub-ms cold start. Origin: business logic, DB access.

### Detailed Answer (3–5 minutes)

**Limits:** Edge runtime restricted CPU/memory — no DB connection pool.

**Examples:** Block country at edge, inject `X-Experiment` header, resize image at edge.

**Cost:** Per-invocation — cheap at volume vs round-trip to origin.

### Architecture Perspective

Edge moves latency-sensitive logic closer to users.

### Follow-up Questions

1. **Workers vs Lambda@Edge? — Cloudflare Workers global — similar pattern.**
2. **Edge KV cache? — Small config at edge — reduce origin hits.**

### Common Mistakes in Interviews

- Full checkout logic at edge
- Edge function calls origin DB directly
- Ignore edge execution limits

---

## Q027: Global Traffic Routing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Networking |
| **Frequency** | Common |

### Question

Route users to nearest healthy region — design?

### Short Answer (30 seconds)

GeoDNS (Route 53 latency routing) or Anycast (Cloudflare). Health checks remove unhealthy region. Active-active or active-passive per SLA.

### Detailed Answer (3–5 minutes)

**Latency routing:** Resolve to lowest-latency ALB. **Failover:** Primary unhealthy → secondary region.

**Data:** Active-active needs conflict resolution or read-local write-global strategy.

**Compliance:** EU users → EU region only — geofencing policy.

### Architecture Perspective

Global routing is architecture for international products.

### Follow-up Questions

1. **DNS TTL trade-off? — Low TTL faster failover — higher DNS load.**
2. **Split horizon DNS? — Internal vs external routing different.**

### Common Mistakes in Interviews

- Single region for global users
- DNS TTL 3600 with no health check
- Active-active without conflict strategy

---

## Q028: Capacity Headroom Planning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Capacity |
| **Frequency** | Common |

### Question

How much headroom above peak load should production maintain?

### Short Answer (30 seconds)

20–40% headroom above measured peak for compute. 50% for critical path before auto-scale lag catches up. Load test at 2× expected peak annually.

### Detailed Answer (3–5 minutes)

**Headroom covers:** Auto-scale delay (2–5 min), deploy surge, viral spike, AZ failure (lose 33% capacity).

**Document:** Peak RPS from last Black Friday + growth factor.

**Cost trade-off:** Reserved baseline + burst on-demand for headroom.

### Architecture Perspective

Headroom is explicit capacity NFR — not accidental over-provision.

### Follow-up Questions

1. **Chaos test headroom? — Kill AZ during load test — validate surviving capacity.**
2. **Queue-based absorption? — Queue adds temporal headroom — bounded buffer.**

### Common Mistakes in Interviews

- 100% utilized at peak — no scale room
- Never load test above production peak
- Headroom only on CPU not connections

---

## Q029: Performance Budgets at Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Performance |
| **Frequency** | Common |

### Question

Define performance budget for search API at 50K RPS.

### Short Answer (30 seconds)

p99 < 150ms end-to-end. Max 2 internal hops. Elasticsearch query < 80ms. Serialization < 10ms. Zero N+1 DB calls on search path.

### Detailed Answer (3–5 minutes)

**Enforcement:** Load test gate in CI on PR touching search. RUM vs synthetic gap tracked.

**Budget breakdown:** Network 20ms + gateway 10ms + service 80ms + ES 80ms — identify slack.

**Regression:** Alert when p99 degrades 10% week-over-week.

### Architecture Perspective

Performance budgets make NFR measurable and enforceable.

### Follow-up Questions

1. **Mobile budget? — Add 100ms RTT for 3G — separate target.**
2. **Third-party API in budget? — Include or async exclude from sync path.**

### Common Mistakes in Interviews

- No per-component budget
- Budget only measured in dev laptop
- Ignore regression alerts

---

## Q030: Load Test Interpretation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Testing |
| **Frequency** | Common |

### Question

Load test: p50 50ms, p99 2000ms, errors 0.1% at target RPS. Interpret.

### Short Answer (30 seconds)

Tail latency problem — likely GC pause, lock contention, slow dependency, or connection pool wait. 0.1% errors may be timeout under load — investigate before launch.

### Detailed Answer (3–5 minutes)

**Analysis steps:**
1. Trace slow p99 requests — distributed tracing
2. Check DB slow query log during test
3. Thread pool queue depth correlation
4. Compare ramp vs steady state

**Pass criteria:** p99 within SLO at 1.5× target RPS with <0.01% errors.

### Architecture Perspective

Architects interpret load tests — not just run and screenshot.

### Follow-up Questions

1. **Coordinated omission? — Gatling/k6 handle better than naive JMeter — know tool bias.**
2. **Soak test? — 4h run detects memory leak invisible in 10min test.**

### Common Mistakes in Interviews

- Only report p50
- Ignore 0.1% errors as noise
- Load test without production-like data volume

---
