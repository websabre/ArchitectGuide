# Week 47 — Advanced Q&A

> Q071–Q100: Premium format (Week 1 quality).

---


## Q071: Dual Write Outbox Fix

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Messaging |
| **Frequency** | Very Common |

### Question

Fix dual-write problem when API writes DB and publishes to Kafka synchronously.

### Short Answer (30 seconds)

Replace with transactional outbox — same DB transaction for entity + outbox row; async relay publishes; consumers idempotent.

### Detailed Answer (3–5 minutes)

**Failure modes of dual-write:**
1. DB commits, Kafka fails — downstream never notified
2. Kafka succeeds, DB rolls back — ghost events

**Outbox relay:** Polling or Debezium CDC.

**Architect:** Contract test outbox schema; monitor relay lag.

### Architecture Perspective

Dual-write is classic distributed systems trap — outbox is the fix.

### Follow-up Questions

1. **Change data capture? — Debezium reads WAL — lower latency than poll.**
2. **Ordering guarantees? — Partition by aggregateId.**

### Common Mistakes in Interviews

- Try/catch around Kafka after SaveChanges
- Distributed transaction 2PC across DB and Kafka
- No relay monitoring

---

## Q072: Feed Fanout Hybrid Deep Dive

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

Deep dive: hybrid fanout for news feed with celebrities having 10M followers.

### Short Answer (30 seconds)

Fanout-on-write for users with <10K followers; fanout-on-read for celebrities; merge at read time with cap on timeline size.

### Detailed Answer (3–5 minutes)

**Write path normal user:** Push postId to each follower's Redis list (cap 1000).
**Celebrity post:** Store in celebrity post list only.
**Read path:** Merge own write-fanout + celebrity lists + rank.

**Storage:** Redis sorted sets for timelines; Cassandra for posts.

**Architect:** Threshold configurable — tune based on follower distribution metrics.

### Architecture Perspective

Hybrid fanout is the canonical feed deep dive answer.

### Follow-up Questions

1. **Ranking pipeline? — Async score computation — don't block publish.**
2. **Feed dedup? — Set semantics or postId uniqueness check.**

### Common Mistakes in Interviews

- Fanout on write for 10M follower account
- Unbounded timeline list in Redis
- No ranking — pure chronological only at scale

---

## Q073: URL Shortener Collision Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | System Design |
| **Frequency** | Common |

### Question

Compare counter+base62 vs hash-based URL shortener ID generation.

### Short Answer (30 seconds)

Counter+base62: sequential, predictable length, needs distributed counter. Hash: fixed length, collision handling required, not sortable.

### Detailed Answer (3–5 minutes)

**Counter approach:**
- Shard counters per range
- Base62 encode — short URLs
- Snowflake variant for distributed

**Hash approach:**
- MD5/SHA truncate — collision probability
- Retry on unique constraint violation

**Architect:** Counter simpler at 100M URLs; hash if no central coordinator.

### Architecture Perspective

ID strategy affects DB index performance and collision handling.

### Follow-up Questions

1. **Custom alias? — Separate unique index — user-facing feature.**
2. **Sequential IDs enumerable? — Security concern — use random if needed.**

### Common Mistakes in Interviews

- MD5 truncate without collision handling
- Single auto-increment DB at 10K writes/sec
- No TTL on expired short links

---

## Q074: Chat Message Ordering

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

Guarantee message ordering in distributed chat system.

### Short Answer (30 seconds)

Per-conversation sequence number assigned by single partition owner; clients display by sequenceId; partition key = conversationId.

### Detailed Answer (3–5 minutes)

**Design:**
- Conversation service owns sequence counter
- Message: `{ conversationId, sequenceId, body, senderId }`
- Kafka partition key = conversationId for ordering

**Groups:** Same pattern — sequence per group channel.

**Multi-region:** Sticky routing or CRDT for offline — document conflict policy.

**Architect:** Ordering scope is per-conversation — not global.

### Architecture Perspective

Ordering scope definition is critical — global order impossible at scale.

### Follow-up Questions

1. **Vector clocks? — Causal ordering — advanced offline sync.**
2. **Gap detection? — Client requests missing sequence range.**

### Common Mistakes in Interviews

- Global timestamp ordering across servers
- No sequence on concurrent sends
- HTTP poll without ordering guarantee

---

## Q075: Search Reindex Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | System Design |
| **Frequency** | Common |

### Question

Reindex Elasticsearch without search downtime.

### Short Answer (30 seconds)

Blue-green index: build new index alias target, bulk reindex, swap alias atomically, delete old index after validation.

### Detailed Answer (3–5 minutes)

**Steps:**
1. Create `products_v2` index with new mapping
2. Reindex API or Kafka dual-write to both
3. Validate document counts + sample queries
4. `POST _aliases` atomic swap
5. Drop `products_v1`

**Zero-downtime:** Alias `products` always points to active.

**Architect:** Reindex runbook in ops docs; rollback = swap alias back.

### Architecture Perspective

Index migration without alias swap causes search outages.

### Follow-up Questions

1. **Mapping breaking change? — New index required — not in-place.**
2. **Incremental reindex? — CDC pipeline to new index continuously.**

### Common Mistakes in Interviews

- Delete old index before validating new
- In-place mapping change on live index
- No rollback alias plan

---

## Q076: Notification Dedup at Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

Prevent duplicate push notifications when consumer retries.

### Short Answer (30 seconds)

Idempotency key per `(userId, notificationType, eventId)` stored in Redis with TTL; skip send if key exists.

### Detailed Answer (3–5 minutes)

**Flow:**
1. Worker receives event with eventId
2. `SETNX notify:{userId}:{eventId}` with 24h TTL
3. If set succeeds → send; else skip

**At-least-once delivery + dedup = effective exactly-once UX.

**Architect:** Separate dedup store TTL from business retention.

### Architecture Perspective

Notification dedup is mandatory with at-least-once queues.

### Follow-up Questions

1. **Provider idempotency? — FCM collapse_key — secondary defense.**
2. **Digest batching? — Separate dedup key for digest window.**

### Common Mistakes in Interviews

- No dedup on retry
- Dedup key too short — collision skip legitimate
- Infinite dedup table growth

---

## Q077: Saga Orchestration Temporal

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | System Design |
| **Frequency** | Common |

### Question

Implement checkout saga with Temporal workflow engine.

### Short Answer (30 seconds)

Orchestrator workflow: reserve inventory → charge payment → create shipment; each step activity with timeout; compensation activities on failure; durable state in Temporal.

### Detailed Answer (3–5 minutes)

**Workflow pseudocode:**
```
try:
  inventory.reserve()
  payment.charge()
  shipping.create()
except PaymentFailed:
  inventory.release()
```

**Benefits:** Durable timers, visibility UI, retry policies per activity.

**Architect:** Prefer orchestration when debugging and compliance audit trail needed.

### Architecture Perspective

Temporal/Cadence mention signals production saga experience.

### Follow-up Questions

1. **Choreography vs orchestration? — Events only — harder to trace.**
2. **Saga timeout? — Workflow timer triggers compensation.**

### Common Mistakes in Interviews

- Saga state in memory only
- No compensation for inventory release
- Distributed 2PC across three services

---

## Q078: Circuit Breaker Cascade

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Resilience |
| **Frequency** | Very Common |

### Question

Payment API circuit opens — design cascade prevention across microservices.

### Short Answer (30 seconds)

Bulkheads isolate thread pools; breakers per dependency; fallbacks return degraded response; shed load at gateway; don't retry into open circuit.

### Detailed Answer (3–5 minutes)

**Cascade chain:** Order → Payment → Fraud → all retry simultaneously → amplifies failure.

**Prevention:**
- Timeout budget 300ms total
- Breaker on Payment fails fast
- Fallback: queue order as 'payment pending'
- No retry from Order when breaker open

**Architect:** Chaos test breaker behavior quarterly.

### Architecture Perspective

Cascade failure prevention is staff-level resilience topic.

### Follow-up Questions

1. **Bulkhead thread pools? — Separate pool per downstream.**
2. **Half-open probe? — Single test request — not full traffic.**

### Common Mistakes in Interviews

- Retry storm into failing payment API
- Shared thread pool all dependencies
- No fallback UX when breaker open

---

## Q079: Distributed Rate Limiter Sharding

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | System Design |
| **Frequency** | Common |

### Question

Shard Redis rate limiter across cluster for 1M API keys.

### Short Answer (30 seconds)

Hash API key to Redis cluster slot; Lua script atomic increment; local approximate counters for coarse global limit optional.

### Detailed Answer (3–5 minutes)

**Centralized:** Single Redis key hot — shard by `hash(apiKey) % N`.

**Hierarchical:** Edge approximate + central authoritative for billing.

**Lua script:** INCR + EXPIRE atomic — no race.

**Architect:** Rate limit headers `X-RateLimit-Remaining` on every response.

### Architecture Perspective

Distributed rate limiting requires atomic ops — Lua or dedicated service.

### Follow-up Questions

1. **Token bucket Redis implementation? — Store tokens + last refill timestamp.**
2. **Sliding window log? — ZSET with timestamp members.**

### Common Mistakes in Interviews

- In-memory per node only
- Race without atomic Redis script
- No 429 Retry-After header

---

## Q080: CDN Cache Stampede

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | System Design |
| **Frequency** | Common |

### Question

Prevent CDN/origin stampede when popular cache entry expires simultaneously.

### Short Answer (30 seconds)

Staggered TTL jitter, request coalescing (single flight), early async refresh before expiry, stale-while-revalidate header.

### Detailed Answer (3–5 minutes)

**Techniques:**
1. TTL = base + random(0, 60s)
2. Mutex: one origin fetch, others wait
3. `stale-while-revalidate=60` — serve stale during refresh

**Architect:** Monitor origin spike correlated with TTL expiry — alert.

### Architecture Perspective

Cache stampede is production incident pattern — mitigations expected.

### Follow-up Questions

1. **Probabilistic early expiration? — Refresh in background before hard expiry.**
2. **CDN purge storm? — Version URLs — avoid mass purge.**

### Common Mistakes in Interviews

- Identical TTL all keys
- No coalescing on cache miss
- Origin unprotected behind CDN

---

## Q081: Hot Partition Cassandra

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | System Design |
| **Frequency** | Common |

### Question

Single IoT device sends 10K events/sec — hot partition in Cassandra.

### Short Answer (30 seconds)

Salt partition key: `(deviceId, bucket)` where bucket = random(0..N) or time bucket; merge on read; or dedicated queue for hot device.

### Detailed Answer (3–5 minutes)

**Problem:** Partition key = deviceId only → single Cassandra node overload.

**Fix:**
- Composite key `(deviceId, hourBucket)`
- Or write-behind queue serializing hot device

**Architect:** Monitor per-partition write rate — alert threshold.

### Architecture Perspective

Hot partition applies to any sharded store — Cassandra, DynamoDB.

### Follow-up Questions

1. **DynamoDB adaptive capacity? — Absorbs brief hot keys — not permanent fix.**
2. **Kafka hot partition? — More partitions + keyed sub-partition.**

### Common Mistakes in Interviews

- Ignore single-device flood scenario
- Only vertical scale bigger node
- Cross-partition query on hot path

---

## Q082: Geographic Chat Routing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | System Design |
| **Frequency** | Common |

### Question

Route chat users to nearest WebSocket region with cross-region messaging.

### Short Answer (30 seconds)

Geo-DNS to nearest gateway region; home region stores conversation; cross-region relay via internal message bus; document latency for cross-region chats.

### Detailed Answer (3–5 minutes)

**User A (US) → User B (EU):**
- Both connect to nearest gateway
- Message persists in conversation home region (e.g., hash conversationId)
- Relay to recipient's regional gateway via pub/sub

**Architect:** Cell architecture — pin conversation to region for data residency.

### Architecture Perspective

Multi-region chat adds routing complexity — state home region clearly.

### Follow-up Questions

1. **CRDT for offline? — Auto-merge — mention for advanced mock.**
2. **E2E encryption? — Key exchange out of scope or separate layer.**

### Common Mistakes in Interviews

- Single region WS for global users
- No cross-region message relay plan
- Ignore data residency requirements

---

## Q083: Microservice Data Ownership

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

Enforce database-per-service when legacy shared SQL database exists.

### Short Answer (30 seconds)

Strangler: new services get own DB; legacy modules read via API not JOIN; dual-write migration period; views deprecated; FK constraints removed across boundaries.

### Detailed Answer (3–5 minutes)

**Migration steps:**
1. Freeze shared schema changes
2. Extract service with schema copy
3. Sync via CDC until cutover
4. Remove cross-service FKs
5. Delete shared table access from old monolith

**Architect:** Shared DB is top distributed monolith smell.

### Architecture Perspective

Data ownership enforcement is organizational + technical migration.

### Follow-up Questions

1. **Shared read replica? — Still coupling — API boundary preferred.**
2. **Saga for cross-service data? — Events not shared tables.**

### Common Mistakes in Interviews

- Microservices sharing one PostgreSQL schema
- Cross-service SQL JOIN in reports as excuse
- No migration plan from shared DB

---

## Q084: API Versioning Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | API Design |
| **Frequency** | Common |

### Question

Version public API when mobile clients update slowly.

### Short Answer (30 seconds)

URL path `/v1` `/v2`, maintain v1 12+ months, additive changes in same version, breaking changes only in new major, sunset headers `Deprecation: date`.

### Detailed Answer (3–5 minutes)

**Rules:**
- Add optional fields — non-breaking
- Remove/rename — breaking → new major
- Mobile long tail — never force upgrade without grace

**Gateway:** Route version to backend deployment.

**Architect:** Usage metrics drive sunset — not calendar alone.

### Architecture Perspective

API versioning affects mobile and partner integrations — plan explicitly.

### Follow-up Questions

1. **Header vs URL versioning? — URL more visible in logs — common choice.**
2. **GraphQL deprecation? — `@deprecated` directive — schema registry.**

### Common Mistakes in Interviews

- Breaking change in minor version
- No deprecation timeline communicated
- Single unversioned public API

---

## Q085: Snowflake vs ULID

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | System Design |
| **Frequency** | Common |

### Question

Compare Snowflake IDs and ULID for distributed order IDs.

### Short Answer (30 seconds)

Snowflake: 64-bit, time-sortable, needs machine ID coordination. ULID: 128-bit, lexicographic sort, random component, no coordination — larger keys.

### Detailed Answer (3–5 minutes)

| Property | Snowflake | ULID |
|----------|-----------|------|
| Sortable | Yes (time) | Yes (time prefix) |
| Coordination | Machine ID required | None |
| Size | 8 bytes | 16 bytes |
| Clock dependency | Yes — rollback handling | Yes |

**Architect:** Snowflake for high-write sharded SQL; ULID for client-generated offline IDs.

### Architecture Perspective

ID format affects index locality and operational complexity.

### Follow-up Questions

1. **UUID v7? — Time-sortable UUID — newer alternative.**
2. **DB sequence bottleneck? — Single writer at scale — avoid.**

### Common Mistakes in Interviews

- Duplicate Snowflake machine IDs
- Random UUID v4 for time-range queries
- No clock rollback strategy for Snowflake

---

## Q086: Redis Cluster Failover

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Distributed Cache |
| **Frequency** | Common |

### Question

Handle Redis Cluster node failure during flash sale.

### Short Answer (30 seconds)

Cluster auto-failover promotes replica; clients redirect via MOVED/ASK; app retry logic; monitor cluster state; pre-warm replicas; avoid full cluster during sale.

### Detailed Answer (3–5 minutes)

**Failure behavior:**
- Primary down → replica promoted (~seconds)
- Slot migration during recovery
- Client library handles topology refresh

**Mitigation:**
- Multi-AZ deployment
- Replica per shard minimum
- Circuit breaker if cluster unhealthy

**Architect:** Load test failover before sale — not first time in prod.

### Architecture Perspective

Cache HA is part of system design — not assumed.

### Follow-up Questions

1. **Redis Sentinel vs Cluster? — Cluster for sharding; Sentinel for single-master HA.**
2. **Local L1 during Redis outage? — Short TTL emergency — measure staleness.**

### Common Mistakes in Interviews

- Single Redis instance production
- No client retry on connection failure
- Flash sale without failover drill

---

## Q087: Queue Ordering Throughput

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Messaging |
| **Frequency** | Common |

### Question

Trade FIFO ordering against throughput in order processing queue.

### Short Answer (30 seconds)

FIFO partition per orderId preserves order for one entity; multiple partitions for global throughput; strict global order rarely needed.

### Detailed Answer (3–5 minutes)

**Azure Service Bus:** Sessions for FIFO per sessionId.
**Kafka:** Partition key = orderId.
**SQS FIFO:** 300 msg/sec per queue — throughput limit.

**Architect:** Document which operations require ordering — not entire system.

### Architecture Perspective

Ordering scope minimization unlocks throughput.

### Follow-up Questions

1. **Out-of-order handling? — Idempotent + sequence check at consumer.**
2. **Priority queue? — Separate queues — don't block OTP behind batch.**

### Common Mistakes in Interviews

- Global FIFO for all message types
- Single partition Kafka for 'ordering'
- Ignore FIFO throughput ceiling

---

## Q088: Load Balancer Health Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | System Design |
| **Frequency** | Common |

### Question

Design health checks that prevent cascading LB traffic to sick pods.

### Short Answer (30 seconds)

Readiness: deep check (DB connection). Liveness: lightweight. LB uses readiness only. PreStop hook drains connections 30s before terminate.

### Detailed Answer (3–5 minutes)

**Kubernetes:**
```yaml
readinessProbe: GET /health/ready (includes DB)
livenessProbe: GET /health/live (process only)
```

**LB config:** Unhealthy threshold 2, healthy 3, interval 10s.

**Architect:** `/health/ready` fails during dependency outage — pod removed from rotation.

### Architecture Perspective

Health check design prevents traffic to broken instances.

### Follow-up Questions

1. **Deep vs shallow readiness? — Deep catches DB outage; slower probe.**
2. **Startup probe? — Slow-starting JVM apps — avoid premature kill.**

### Common Mistakes in Interviews

- Liveness includes DB — restart loop on DB blip
- No preStop drain on deploy
- LB health check hits expensive endpoint

---

## Q089: Security in System Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Cover security in a 45-minute system design without derailing scope.

### Short Answer (30 seconds)

2 minutes: authN (OAuth/JWT), authZ (RBAC), encryption in transit (TLS) and at rest, input validation, rate limiting, secrets in vault — not full STRIDE unless Tier-0.

### Detailed Answer (3–5 minutes)

**Security checklist:**
- Who can call each API?
- PII encrypted at rest?
- TLS everywhere external
- SQL injection — parameterized queries
- DDoS — WAF + rate limit edge

**Architect:** Tier-0 designs get full STRIDE — others get checklist pass.

### Architecture Perspective

Brief security mention scores points — omission is red flag.

### Follow-up Questions

1. **Zero trust? — Service mesh mTLS internal — mention if microservices.**
2. **Secrets management? — Key Vault / Secrets Manager — never in config.**

### Common Mistakes in Interviews

- Security entirely skipped
- Auth only — no encryption mention
- Secrets in environment variables git-tracked

---

## Q090: Viral Content Hot Key

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

Celebrity posts — 1M QPS read same cache key. Mitigate.

### Short Answer (30 seconds)

Local L1 cache on app nodes (1-2s TTL), key splitting `post:{id}:replica{n}`, read replicas with request coalescing, CDN edge cache for public post API.

### Detailed Answer (3–5 minutes)

**Incident flow:**
1. Monitor single-key QPS alert
2. Enable request coalescing (single flight)
3. Deploy L1 cache emergency config
4. Shift to fanout-on-read for that user permanently

**Architect:** Runbook for viral event — pre-approved mitigations.

### Architecture Perspective

Hot key war stories demonstrate production experience.

### Follow-up Questions

1. **Redis hot key? — Even with cluster — one slot — split key.**
2. **Pre-warm cache? — Before scheduled celebrity post.**

### Common Mistakes in Interviews

- Single Redis key no mitigation plan
- Only vertical scale
- No per-key monitoring

---

## Q091: System Design Phased Evolution

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

Present phased evolution from MVP to global scale in system design close.

### Short Answer (30 seconds)

Phase 1: monolith + SQL + cache. Phase 2: read replicas + CDN. Phase 3: async workers + queue. Phase 4: shard writes + multi-region.

### Detailed Answer (3–5 minutes)

**Example narrative:**
- **0–100K DAU:** Single region App Service + Azure SQL + Redis
- **100K–1M:** Read replicas, CDN, Service Bus for async
- **1M+:** Shard by tenantId, multi-region read, dedicated search cluster

**Architect:** Each phase triggered by measured bottleneck — not premature.

### Architecture Perspective

Phased evolution shows pragmatism — interviewers prefer over day-one Google architecture.

### Follow-up Questions

1. **Triggers per phase? — p99 latency, write QPS ceiling, cost threshold.**
2. **Rollback per phase? — Feature flags — revert to previous topology.**

### Common Mistakes in Interviews

- Day-one 50 microservices
- No metrics trigger between phases
- Skip Phase 1 entirely in answer

---

## Q092: Presigned URL Security

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | File Storage |
| **Frequency** | Common |

### Question

Secure presigned S3 upload URLs for user-generated content.

### Short Answer (30 seconds)

Short TTL (15 min), max size constraint, content-type restriction, virus scan async post-upload, callback validates ownership before marking complete.

### Detailed Answer (3–5 minutes)

**Upload flow:**
1. Client requests presigned PUT URL (authenticated)
2. Server generates URL with conditions: `content-length-range`, `Content-Type`
3. Client uploads direct to S3
4. S3 event → scan + register metadata

**Architect:** Never expose bucket write without conditions.

### Architecture Perspective

Presigned URL security prevents abuse of open upload endpoints.

### Follow-up Questions

1. **POST policy vs PUT presigned? — POST allows form conditions.**
2. **Malware scan? — ClamAV Lambda on S3 event — mandatory for UGC.**

### Common Mistakes in Interviews

- Presigned URL no expiry
- Any content-type allowed
- Skip ownership validation on callback

---

## Q093: Distributed Lock Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | System Design |
| **Frequency** | Common |

### Question

Implement distributed lock for inventory decrement across pods.

### Short Answer (30 seconds)

Redis Redlock or DB advisory lock with TTL; lock key `inventory:{sku}`; always set TTL to prevent deadlock; idempotent decrement inside lock.

### Detailed Answer (3–5 minutes)

**Pattern:**
```
if redis.set(lock_key, token, nx=True, ex=30):
  try: decrement()
  finally: release if token matches
```

**Architect:** Prefer optimistic concurrency (version column) over locks when contention moderate.

### Architecture Perspective

Lock vs optimistic concurrency — justify based on contention.

### Follow-up Questions

1. **Redlock controversy? — Martin Kleppmann critique — know trade-offs.**
2. **Lock TTL too short? — Extend with watchdog if job long.**

### Common Mistakes in Interviews

- Lock without TTL — deadlock on crash
- Distributed lock for every read
- Ignore lock release on exception

---

## Q094: Idempotency Distributed API

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

Design idempotency layer for all mutating API endpoints.

### Short Answer (30 seconds)

Require `Idempotency-Key` header on POST/PATCH; store key+request hash → response; 24h TTL; return cached response on duplicate; 409 if same key different body.

### Detailed Answer (3–5 minutes)

**Storage:** Redis or SQL unique index.

**Race:** Two requests same key — DB unique constraint or distributed lock on first insert.

**Scope:** Per client/tenant + key.

**Architect:** Gateway can enforce key presence on payment routes.

### Architecture Perspective

Idempotency layer is platform concern — not per-endpoint one-off.

### Follow-up Questions

1. **Stripe pattern? — Reference industry standard.**
2. **Partial failure? — Store `processing` state — client retries safely.**

### Common Mistakes in Interviews

- No idempotency on charge endpoint
- Key only client-side honor system
- Race allows double charge

---

## Q095: News Feed Cursor Pagination

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | System Design |
| **Frequency** | Common |

### Question

Stable cursor pagination for news feed under concurrent new posts.

### Short Answer (30 seconds)

Cursor = `(publishedAt, postId)` tuple; query `WHERE (published_at, id) < (@cursor) ORDER BY published_at DESC, id DESC LIMIT 21`; opaque base64 cursor to client.

### Detailed Answer (3–5 minutes)

**Why not offset:** New posts shift pages — duplicates/skips.

**HasMore:** Fetch limit+1, return 20, if 21st exists hasMore=true.

**Architect:** Document cursor stability guarantee — new posts may appear on refresh — expected UX.

### Architecture Perspective

Feed pagination is keyset not offset — quick scoring point.

### Follow-up Questions

1. **Bidirectional scroll? — Provide prev_cursor.**
2. **Real-time insert top? — WebSocket push new item — pagination separate.**

### Common Mistakes in Interviews

- OFFSET on live feed
- Cursor exposes internal sequential id only
- No max page size limit

---

## Q096: Cache Avalanche Mitigation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

1000 cache keys expire simultaneously — DB overload. Prevent.

### Short Answer (30 seconds)

TTL jitter, mutex single-flight on miss, circuit breaker on DB, pre-warm hot keys, never expire all keys at same absolute time.

### Detailed Answer (3–5 minutes)

**Single flight:**
```
if cache.miss(key):
  if lock.acquire(key):
    data = db.load(key)
    cache.set(key, data, ttl+jitter)
    lock.release(key)
  else: wait and retry cache
```

**Architect:** Load test cache expiry scenario in staging.

### Architecture Perspective

Cache avalanche is classic failure mode — mitigations expected in deep dive.

### Follow-up Questions

1. **Probabilistic early refresh? — Background refresh before hard TTL.**
2. **Bulk expiry event? — Stagger by hash(key) % window.**

### Common Mistakes in Interviews

- Identical TTL all product keys
- No DB circuit breaker on cache miss storm
- Cold start no warmup plan

---

## Q097: Capacity Planning Interview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | System Design |
| **Frequency** | Common |

### Question

Translate QPS estimate into server and database capacity.

### Short Answer (30 seconds)

App: QPS / RPS per pod (load test) = pod count × headroom 2×. DB: connections = pods × pool size < max_connections. Cache: working set GB × 1.3 overhead.

### Detailed Answer (3–5 minutes)

**Example:**
- 5K read QPS, 500 RPS per pod → 10 pods + 10 buffer = 20 pods
- 20 pods × 20 pool = 400 connections < SQL 500 max
- 50GB hot catalog × 1.3 = 65GB Redis cluster

**Architect:** Document assumptions — load test evidence beats guess.

### Architecture Perspective

Capacity math connects estimation to infrastructure sizing.

### Follow-up Questions

1. **Headroom factor? — 2× for failover + spike — state explicitly.**
2. **Autoscale bounds? — Min/max pods from capacity calc.**

### Common Mistakes in Interviews

- QPS estimate with no pod sizing
- Connection pool unbounded
- No headroom for failover

---

## Q098: Blob Storage Metadata Orphan

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | File Storage |
| **Frequency** | Common |

### Question

Prevent orphaned blobs when upload callback fails after S3 PUT succeeds.

### Short Answer (30 seconds)

Two-phase: upload to staging prefix; callback moves to final prefix + writes metadata; lifecycle rule deletes staging >24h; reconciliation job finds orphans.

### Detailed Answer (3–5 minutes)

**States:** `pending` → `complete` | `failed`

**Reconciliation:** Daily scan staging prefix + compare metadata table.

**Architect:** Idempotent callback handler — duplicate callback safe.

### Architecture Perspective

Upload lifecycle completeness prevents storage cost leak.

### Follow-up Questions

1. **S3 event notification? — At-least-once — handler idempotent.**
2. **Multipart abort? — Lifecycle abort incomplete uploads.**

### Common Mistakes in Interviews

- Metadata write before upload completes
- No staging prefix cleanup
- Non-idempotent callback handler

---

## Q099: Search Personalization Layer

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | System Design |
| **Frequency** | Common |

### Question

Add personalization to product search without breaking relevance.

### Short Answer (30 seconds)

Base BM25 relevance score + business boost (margin, inventory) + user affinity vector optional; separate ranking tier async; A/B test ranking models.

### Detailed Answer (3–5 minutes)

**Pipeline:**
Query → ES retrieve top 100 → ranker rescores top 20 → response

**Personalization:** Precomputed user category affinity in Redis — multiply score.

**Architect:** Fallback to non-personalized if affinity missing — cold start.

### Architecture Perspective

Search ranking layers separate retrieval from business ranking.

### Follow-up Questions

1. **Learning to rank? — Offline model — mention for senior depth.**
2. **Zero results? — Synonyms, fuzzy, category browse fallback.**

### Common Mistakes in Interviews

- Personalization blocks entire search if model down
- SQL LIKE fallback
- Synchronous ML inference on every query at 5K QPS

---

## Q100: Leader Election Service Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | System Design |
| **Frequency** | Common |

### Question

Design leader election for singleton background job across Kubernetes pods.

### Short Answer (30 seconds)

Use Kubernetes Lease API or etcd distributed lock; only leader runs scheduler; followers standby; lease TTL with renewal heartbeat; graceful step-down on shutdown.

### Detailed Answer (3–5 minutes)

**Pattern:**
```
while running:
  if acquire_lease('job-leader', ttl=30s):
    run_batch()
    renew_lease()
  sleep(poll_interval)
```

**Alternatives:** CronJob with `concurrencyPolicy: Forbid` — simpler if K8s native enough.

**Architect:** Avoid split-brain — lease TTL > max job duration + margin.

### Architecture Perspective

Leader election appears in scheduler and ID generator designs.

### Follow-up Questions

1. **Split brain two leaders? — Fencing token or lease validation before write.**
2. **CronJob vs leader election? — CronJob simpler for periodic batch.**

### Common Mistakes in Interviews

- No TTL on leader lock
- Two pods both think they are leader
- Leader job runs longer than lease TTL without renew

---
