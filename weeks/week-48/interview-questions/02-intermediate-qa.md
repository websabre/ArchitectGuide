# Week 48 — Intermediate Q&A

> Q031–Q070: Premium format (Week 1 quality).

---


## Q031: Notification System Mock Intro

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

How open and structure a 45-minute notification system whiteboard mock?

### Short Answer (30 seconds)

Spend first 5 minutes on channels, volume, latency (OTP vs marketing), and compliance. Then HLD: ingest → queue → workers → provider adapters. Deep dive channel fanout, idempotency, and DLQ — not email HTML.

### Detailed Answer (3–5 minutes)

**Minute-by-minute script:**
| Time | Focus |
|------|-------|
| 0–5 | Requirements — email/SMS/push; 1M/day; OTP <10s |
| 5–15 | HLD — API/event → Service Bus → worker pool → SendGrid/Twilio/FCM |
| 15–30 | Deep dive — priority queues, user prefs, template i18n, idempotency key |
| 30–40 | Failures — provider down, DLQ, retry backoff, rate limits |
| 40–45 | Trade-offs — at-least-once + dedup vs exactly-once fantasy |

**Components to label:**
- Template service (versioned content)
- User preference store (opt-out per channel — CAN-SPAM/GDPR)
- Separate queues: transactional vs marketing
- Delivery status webhook + audit log

**Clarifying questions:**
- 'Is OTP latency hard SLA?'
- 'Do users set quiet hours?'
- 'Duplicate notification acceptable or not?'

**Self-score:** Did I mention idempotency and opt-out before scale?

### Architecture Perspective

Notification mock intro sets scope — interviewers reward compliance and delivery semantics early.

### Follow-up Questions

1. **Exactly-once delivery? — Honest at-least-once + idempotent consumers.**
2. **Scale to 1B/day? — Partition queues; batch digest emails.**

### Common Mistakes in Interviews

- Spend 25 minutes on template HTML design
- Synchronous send in API request path
- No DLQ or provider failure handling

---

## Q032: E-Commerce Cart Mock Intro

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

How begin an e-commerce shopping cart whiteboard mock for architect interviews?

### Short Answer (30 seconds)

Clarify concurrent users, flash sale scenario, guest vs logged-in, inventory rules. Propose Redis-backed cart per user, separate inventory reservation, saga on checkout — draw before deep-diving inventory.

### Detailed Answer (3–5 minutes)

**Opening questions (5 min):**
- Peak concurrent add-to-cart? (e.g. 50K flash sale)
- Guest cart merge on login?
- Inventory oversell tolerance? (zero for most retailers)
- Checkout payment sync or async?

**HLD sketch (10 min):**
```
Client → Cart API → Redis (cart:{userId})
Checkout → Inventory Service (reserve) → Payment → Order DB
Flash sale → waiting room / token queue optional
```

**Deep dive target (15 min):** Inventory reservation with timeout; optimistic concurrency; saga compensation on payment fail.

**Patterns to mention:**
- Cart TTL 7–30 days
- Product catalog cached — short TTL during sale
- Idempotent checkout with `Idempotency-Key`

**Trade-off close:** Redis cart for speed; SQL order of record on commit only.

**Trap to avoid:** Cart rows in SQL at 50K RPS without cache.

### Architecture Perspective

Cart mock intro frames concurrency and inventory — the deep dive is oversell prevention, not CRUD.

### Follow-up Questions

1. **Virtual waiting room? — Flash sale admission control — mention when 50K concurrent stated.**
2. **Saga on checkout? — Release inventory if payment fails.**

### Common Mistakes in Interviews

- Cart in SQL without cache at flash sale scale
- No inventory reservation timeout
- Ignore guest-to-logged-in cart merge

---

## Q033: Queue Design Mock Intro

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

How structure the opening of a message queue design whiteboard mock?

### Short Answer (30 seconds)

Establish producer volume, processing time, ordering needs, failure tolerance, and consumer scale signal. Draw upload/event → durable queue → autoscaling workers → status callback — state visibility timeout math early.

### Detailed Answer (3–5 minutes)

**Requirements checklist (5 min):**
- Throughput — 10K jobs/hour vs 10K/sec
- Job duration — 30s vs 5 min (drives visibility timeout)
- Ordering — FIFO per user or global order irrelevant?
- Priority lanes — paid vs free tier?
- Delivery — at-least-once acceptable with idempotent workers?

**HLD template (10 min):**
```
Producer → Blob (payload) → Queue (metadata) → Worker pool
                              ↓
                         DLQ (poison messages)
Status API / webhook on completion
```

**Deep dive (15 min):** Autoscale on queue depth; `visibility timeout > max processing time`; `maxReceiveCount` before DLQ.

**Example narrative:** Image processing — S3 event → SQS → GPU workers scale 0→N.

**Say aloud:** 'I choose queue over Kafka here because task distribution, not replay log, is the primary need.'

### Architecture Perspective

Queue mock intro is semantics and ops — visibility timeout and DLQ before drawing microservices.

### Follow-up Questions

1. **FIFO queue when? — Strict per-entity ordering — costs throughput.**
2. **Poison message? — DLQ + alert — don't infinite redrive.**

### Common Mistakes in Interviews

- Sync processing in upload API for long jobs
- Visibility timeout 30s for 5-minute job
- No dead-letter queue configured

---

## Q034: API Design Mock Intro

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

How open an API design whiteboard mock for architect-level interviews?

### Short Answer (30 seconds)

Clarify client types (mobile, partner, internal), consistency needs, and scale profile per endpoint. Sketch versioned REST resources, pagination strategy, auth, rate limits, and separate hot read path from write API.

### Detailed Answer (3–5 minutes)

**First 5 minutes — ask:**
- Who consumes — mobile, third-party, browser?
- Read vs write ratio per endpoint?
- Pagination — live feed (cursor) vs admin list (offset OK)?
- Auth — API key, OAuth, JWT scope?

**API skeleton (10 min):**
```
POST /v1/resources     — create (idempotent key header)
GET  /v1/resources/{id}
GET  /v1/resources?cursor=&limit=
PATCH /v1/resources/{id}
```

**Architect concerns to voice:**
- Version prefix `/v1` — breaking change policy
- ProblemDetails (RFC 7807) errors
- Rate limit 429 + Retry-After
- Cursor pagination for live feeds — avoid offset skip/duplicate

**Deep dive pick:** URL shortener redirect (hot read) vs create API (write) — different scale.

**Close:** 'Redirect service minimal deps; analytics async via event.'

### Architecture Perspective

API mock intro separates read/write paths and client constraints — versioning and pagination are scoring points.

### Follow-up Questions

1. **GraphQL when? — Complex mobile clients — REST fine for focused mock.**
2. **gRPC internal? — Edge HTTP public, gRPC service-to-service.**

### Common Mistakes in Interviews

- Unversioned public API
- OFFSET pagination on real-time feed
- Analytics on synchronous hot read path

---

## Q035: Scale Estimation Mock Intro

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

How lead scale estimation in the first 10 minutes of a system design mock?

### Short Answer (30 seconds)

State assumptions explicitly, compute DAU → daily ops → average QPS → peak QPS, then storage and bandwidth. Use results to justify cache, queue, shard, or CDN — estimation drives architecture.

### Detailed Answer (3–5 minutes)

**Estimation script:**
1. **Users** — 'Assume 10M DAU'
2. **Actions** — '10 actions/user/day → 100M ops/day'
3. **QPS** — `100M ÷ 86400 ≈ 1.2K avg`; `×3 peak ≈ 3.5K QPS`
4. **Read/write** — '100:1 → ~35 write QPS, ~3.5K read QPS'
5. **Storage** — `posts/day × size × retention`
6. **Bandwidth** — `QPS × payload KB`

**Quick mental math:**
- 1M seconds ≈ 11.5 days
- 1 billion bytes ≈ 1 GB

**Translate to decisions:**
| Result | Architecture hint |
|--------|-------------------|
| Read-heavy | CDN + Redis |
| 3K read QPS | Cache mandatory |
| 10GB/day growth | Shard later; plan retention |
| Large payloads | Async upload + queue |

**Say aloud:** 'These are order-of-magnitude — if DAU 10×, cache tier becomes insufficient.'

**Avoid:** Random 'billions of requests' without derivation.

### Architecture Perspective

Scale estimation mock intro proves architectural thinking — math links directly to component choices.

### Follow-up Questions

1. **Power-of-two shortcuts? — 1M sec ≈ 11.5 days — speeds mental division.**
2. **Sensitivity analysis? — 'If actions 50/day not 10, QPS 5×' — shows rigor.**

### Common Mistakes in Interviews

- No written assumptions on board
- Skip estimation and jump to Redis
- Memorized QPS without showing derivation

---

## Q036: Notification System Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

45-minute mock: design notification system. What do you cover in each phase?

### Short Answer (30 seconds)

0–5 req, 5–15 HLD (ingest, queue, workers, templates), 15–30 deep dive channel fanout + idempotency, 30–40 failures/DLQ, 40–45 trade-offs.

### Detailed Answer (3–5 minutes)

**Mock script:**
- Clarify channels, volume (1M/day), latency (OTP <10s)
- Draw: API → Service Bus → worker pool → providers
- Deep dive: priority queues, user prefs, retry
- Mention: CAN-SPAM opt-out, rate limits per provider

**Self-score:** Did you ask about transactional vs marketing?

### Architecture Perspective

Timed mock builds muscle memory — notification is high-frequency interview prompt.

### Follow-up Questions

1. **Follow-up trap? — Exactly-once delivery — honest at-least-once + idempotency.**
2. **Scale 1B/day? — Partition queues, batch email.**

### Common Mistakes in Interviews

- Spend 25 min on email template HTML
- Skip idempotency
- No provider failure handling

---

## Q037: E-Commerce Cart Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Mock: design shopping cart for flash sale — 50K concurrent add-to-cart.

### Short Answer (30 seconds)

Cart service Redis-backed per userId, inventory reservation separate service, optimistic concurrency, queue checkout, CDN for product static data.

### Detailed Answer (3–5 minutes)

**Key points:**
- Cart: `HSET cart:{userId}` TTL 7 days
- Inventory: reserve with timeout — saga on checkout
- Flash sale: token queue or virtual waiting room
- Don't hammer DB — cache product availability snapshot with short TTL

**Time:** 5 min reqs, 10 min diagram, 15 min inventory deep dive.

### Architecture Perspective

Cart mock tests concurrency and inventory — classic e-commerce stress.

### Follow-up Questions

1. **Oversell prevention? — Atomic decrement or reservation tokens.**
2. **Guest cart merge? — On login merge Redis keys.**

### Common Mistakes in Interviews

- Cart in SQL row per session at 50K RPS
- No inventory reservation timeout
- Ignore flash sale queue

---

## Q038: Queue Design Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Mock: design task queue for image processing — 10K uploads/hour.

### Short Answer (30 seconds)

Upload to blob, metadata queue, workers scale on queue depth, priority lane for paid users, DLQ, result callback webhook.

### Detailed Answer (3–5 minutes)

**Architecture:**
- S3 event → SQS → auto-scaling worker pool (GPU optional)
- Visibility timeout > max processing time
- Status API polled or webhook on complete

**Deep dive:** Poison image crashing worker — DLQ + maxReceiveCount.

### Architecture Perspective

Queue mock — emphasize autoscale signal and visibility timeout math.

### Follow-up Questions

1. **FIFO needed? — Only if strict order per user album.**
2. **Exactly-once processing? — Idempotent output keys by uploadId.**

### Common Mistakes in Interviews

- Sync processing in upload API
- Visibility timeout 30s for 5min job
- No DLQ

---

## Q039: API Pagination Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Mock: design pagination for activity feed API — stable under concurrent writes.

### Short Answer (30 seconds)

Cursor-based pagination with `(created_at, id)` tuple, not offset. `?cursor=eyJ...` opaque token, `limit=20`, `hasMore` flag.

### Detailed Answer (3–5 minutes)

**Why not offset:** New items shift pages — duplicates/skips.

**Cursor:** `WHERE (created_at, id) < (@ts, @id) ORDER BY created_at DESC, id DESC LIMIT 21`

**Mock tip:** State default limit max 100, rate limit list endpoint.

### Architecture Perspective

Pagination mock is quick win if you know cursor vs offset cold.

### Follow-up Questions

1. **Bidirectional? — prev_cursor for infinite scroll up.**
2. **Keyset on UUID? — Use indexed tuple not OFFSET.**

### Common Mistakes in Interviews

- OFFSET pagination on live feed
- Expose internal DB id unsorted
- No max page size

---

## Q040: Rate Limiting Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Mock: rate limit public API 1000 req/hour per API key with burst.

### Short Answer (30 seconds)

Token bucket in Redis, key per API key, burst 50, refill 1000/3600 per sec, 429 + Retry-After, gateway enforcement.

### Detailed Answer (3–5 minutes)

**Whiteboard:**
```
Client → API GW → [Rate Limit Check Redis] → Service
```

**Discuss:** Global vs per-endpoint limits, DDoS at IP layer (WAF) separate from plan quota.

**5 min:** Draw algorithm. **10 min:** Redis atomicity Lua script.

### Architecture Perspective

Rate limit mock should fit in 15 min deep dive — don't over-engineer.

### Follow-up Questions

1. **Sliding window vs token bucket? — Mention both — pick one.**
2. **Distributed denial? — Edge WAF before app rate limit.**

### Common Mistakes in Interviews

- Per-server in-memory only
- No burst allowance UX
- Forget API key auth context

---

## Q041: Authentication System Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Mock: design auth for B2B SaaS — SSO, API keys, MFA.

### Short Answer (30 seconds)

Entra ID/Okta SAML/OIDC for SSO, JWT access + refresh rotation, API keys hashed in DB, MFA via TOTP, RBAC per tenant, session revocation list.

### Detailed Answer (3–5 minutes)

**Components:**
- Identity provider federation
- Auth service issues JWT (short TTL 15m)
- Refresh token httpOnly cookie rotation
- API keys for automation scoped per tenant

**Security:** PKCE for SPA, no tokens in localStorage if avoidable.

### Architecture Perspective

Auth mock spans human SSO and machine API keys — clarify both.

### Follow-up Questions

1. **Tenant isolation? — tenantId claim validated every request.**
2. **Password storage? — bcrypt/Argon2 — if local auth at all.**

### Common Mistakes in Interviews

- JWT forever no refresh
- API key plaintext in DB
- No MFA for admin

---

## Q042: Logging Aggregation Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Mock: centralized logging for 200 microservices.

### Short Answer (30 seconds)

Structured JSON logs, OpenTelemetry collector, Kafka buffer, Elasticsearch/OpenSearch index, retention tiers, correlation ID, PII scrubbing pipeline.

### Detailed Answer (3–5 minutes)

**Flow:**
App → sidecar/agent → collector → Kafka → indexer → Kibana/Grafana

**Discuss:** Log volume cost — sample debug in prod, hot/warm/cold indices.

**Alert:** Error rate anomaly on `service.name`.

### Architecture Perspective

Logging mock — mention cost and PII not just 'send to ELK'.

### Follow-up Questions

1. **Log levels in prod? — Info default, debug sampled.**
2. **Cardinality explosion? — Avoid high-cardinality labels in metrics/logs.**

### Common Mistakes in Interviews

- Unstructured printf logs
- No correlation ID standard
- Infinite retention all logs

---

## Q043: Metrics System Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Mock: metrics and alerting for payment platform.

### Short Answer (30 seconds)

Prometheus scrape or OTLP push, RED metrics (rate, errors, duration), business metrics (payment success $), Alertmanager PagerDuty, SLO burn alerts.

### Detailed Answer (3–5 minutes)

**Key metrics:**
- `http_server_duration_seconds` histogram
- `payment_success_total` counter by method
- Queue depth, DB connection pool

**SLO:** 99.9% success → error budget policy.

**Dashboard:** Golden signals per service.

### Architecture Perspective

Metrics mock ties technical RED to business KPIs.

### Follow-up Questions

1. **Histogram vs summary? — Histogram for percentile aggregation in Prometheus.**
2. **Alert fatigue? — SLO-based not every blip.**

### Common Mistakes in Interviews

- Only CPU monitoring
- No business success metric
- 1000 static threshold alerts

---

## Q044: Deployment Architecture Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Mock: zero-downtime deployment for API on Kubernetes.

### Short Answer (30 seconds)

Rolling update maxUnavailable 0, readiness probe, preStop hook, blue-green or canary with service mesh weights, DB migrations backward compatible.

### Detailed Answer (3–5 minutes)

**Diagram:**
- CI builds image → registry
- ArgoCD sync
- K8s Deployment rolling
- Ingress canary 10% → 100%

**Discuss:** Rollback via previous image tag, feature flags decouple deploy from release.

### Architecture Perspective

Deployment mock connects K8s mechanics to schema compatibility.

### Follow-up Questions

1. **Readiness vs liveness? — Readiness removes from LB during startup.**
2. **Database migration job? — Init container or Job before traffic.**

### Common Mistakes in Interviews

- Recreate deployment strategy production
- Breaking schema same deploy as code
- No health probes

---

## Q045: Multi-Tenant Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Mock: multi-tenant SaaS data isolation strategy.

### Short Answer (30 seconds)

Options: shared DB row-level tenantId, schema-per-tenant, DB-per-tenant enterprise. Start shared + RLS, premium isolated DB.

### Detailed Answer (3–5 minutes)

**Comparison:**
| Model | Cost | Isolation |
|-------|------|----------|
| Shared table | Low | RLS + app filter |
| Schema/tenant | Medium | Better |
| DB/tenant | High | Strongest |

**Must:** tenantId in every query, JWT claim validation, no cross-tenant cache keys.

### Architecture Perspective

Multi-tenant mock — pick model and justify for given customer mix.

### Follow-up Questions

1. **Noisy neighbor? — Per-tenant rate limits and query timeouts.**
2. **Compliance tenant? — Dedicated DB + VPC for one client.**

### Common Mistakes in Interviews

- Forget tenantId in cache key
- Only app-level filter no DB RLS
- One size for SMB and Fortune 500

---

## Q046: Read Replica Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Mock: when route reads to replica and handle lag.

### Short Answer (30 seconds)

Analytics and list pages → replica. Post-checkout balance → primary. Session stickiness after write or `read_consistency=strong` query param internal.

### Detailed Answer (3–5 minutes)

**Diagram:** Primary (writes) → async replication → 2+ replicas (reads)

**Monitor lag:** Route away if >5s.

**Mock answer structure:** Classify each endpoint read tolerance.

### Architecture Perspective

Read replica mock is consistency classification exercise.

### Follow-up Questions

1. **Globally distributed replicas? — Near-user read — lag varies.**
2. **Replica failure? — Fallback primary — capacity plan.**

### Common Mistakes in Interviews

- All reads replica always
- No lag monitoring
- User sees stale own payment immediately

---

## Q047: Write Path vs Read Path

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Mock: separate write and read paths for high-traffic blog platform.

### Short Answer (30 seconds)

CQRS-lite: write API → normalized DB → event → projector builds read model (denormalized ES/Redis). Reads never hit write schema.

### Detailed Answer (3–5 minutes)

**Write path:** Validate → DB txn → publish PostCreated
**Read path:** Query materialized view / cache

**Trade-off:** Eventual consistency seconds on read after publish.

**Mock time:** 10 min draw both paths explicitly.

### Architecture Perspective

Write/read split is CQRS gateway — common follow-up in mocks.

### Follow-up Questions

1. **When not CQRS? — Low traffic CRUD — keep simple.**
2. **Dual write problem? — Outbox not write DB+ES synchronously.**

### Common Mistakes in Interviews

- Same fat model read and write at scale
- ES updated in API txn synchronously
- No projection rebuild plan

---

## Q048: Event Sourcing When Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

Mock: when would you use event sourcing for audit-heavy ledger?

### Short Answer (30 seconds)

When complete audit trail, temporal queries ('balance at date'), and replay are requirements — finance ledger, not simple CRUD blog.

### Detailed Answer (3–5 minutes)

**ES design:**
- Append-only event store
- Projections rebuild state
- Snapshots every N events

**When NOT:** Simple CMS, no audit law, team inexperienced — operational cost high.

**Mock:** State trade-offs clearly — don't ES by default.

### Architecture Perspective

Event sourcing mock tests when NOT as much as when.

### Follow-up Questions

1. **CQRS required? — Often paired — not mandatory.**
2. **Event schema evolution? — Upcasting old events.**

### Common Mistakes in Interviews

- Event sourcing for every microservice
- No snapshot strategy
- Delete events GDPR impossible

---

## Q049: CQRS Mock Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Mock: CQRS for order dashboard with heavy reports.

### Short Answer (30 seconds)

Command side OLTP normalized, query side denormalized read DB or ES updated by events, separate scale, different indexes optimized per query.

### Detailed Answer (3–5 minutes)

**Commands:** PlaceOrder, CancelOrder — strong consistency
**Queries:** Sales dashboard, order search — eventual OK

**Sync mechanism:** Outbox → Kafka → read model updater

**Mock pitfall:** Don't say separate DB without sync story.

### Architecture Perspective

CQRS mock needs sync mechanism — outbox/event handler.

### Follow-up Questions

1. **Read model rebuild? — Replay events — disaster recovery.**
2. **Multiple read models? — One per query shape OK.**

### Common Mistakes in Interviews

- CQRS with synchronous dual write
- Same team owns 12 read models day one
- No lag SLA to read side

---

## Q050: Backpressure Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Mock: backpressure when downstream email service slows.

### Short Answer (30 seconds)

Queue buffers, bounded channels, slow consumer detection, pause ingestion, 503 to clients with retry-after, scale workers, circuit breaker to provider.

### Detailed Answer (3–5 minutes)

**Signals:** Queue age growing, consumer lag metric.

**Responses:**
1. Scale consumers
2. Shed load — reject non-critical
3. Circuit open — stop accepting marketing sends

**Mock:** Draw feedback loop producer ← queue depth → throttle.

### Architecture Perspective

Backpressure mock shows flow control not unlimited queues.

### Follow-up Questions

1. **Reactive streams? — Bounded buffer concept in any stack.**
2. **User experience? — Graceful degradation message.**

### Common Mistakes in Interviews

- Unbounded queue OOM
- Block threads waiting forever
- No shedding strategy

---

## Q051: Timeout Design Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Mock: timeout strategy for 5-deep microservice call chain.

### Short Answer (30 seconds)

Budget 300ms total user SLA — allocate per hop, shortest timeout innermost, context deadline propagation, fail fast, avoid serial if parallel possible.

### Detailed Answer (3–5 minutes)

**Example:**
- Gateway: 300ms total
- Service A: 250ms ctx
- Service B: 100ms (called by A)

**Use:** gRPC deadline, Polly timeout, cancellation token .NET.

**Mock mistake:** 30s default HttpClient timeout everywhere.

### Architecture Perspective

Timeout budget propagation is staff-level distributed systems detail.

### Follow-up Questions

1. **Partial results? — Return degraded response if optional svc timeout.**
2. **Retry after timeout? — Only idempotent with capped retry.**

### Common Mistakes in Interviews

- Default 100s timeout all calls
- No cancellation propagation
- Serial chain when parallel possible

---

## Q052: Retry Design Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Mock: retry policy for idempotent GET vs payment POST.

### Short Answer (30 seconds)

GET: retry 3× exponential backoff on 5xx/timeout. POST payment: no retry unless idempotency-key stored — retry only same key returns same result.

### Detailed Answer (3–5 minutes)

**Layers:**
- Client retry (careful)
- Gateway retry (idempotent only)
- Worker retry with DLQ max attempts

**Jitter:** Prevent synchronized retry storm.

**Mock:** Draw idempotency key store lookup before execute.

### Architecture Perspective

Retry mock must distinguish safe vs unsafe methods.

### Follow-up Questions

1. **Retry-After header? — Honor on 429.**
2. **Nested retries? — Multiply attempts — dangerous.**

### Common Mistakes in Interviews

- Retry POST payment blindly
- Infinite retry on 400
- Retry at every layer 3× each

---

## Q053: Idempotency Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Mock: idempotent payment API design.

### Short Answer (30 seconds)

Client sends `Idempotency-Key: UUID`, server stores key → result mapping 24h, duplicate key returns cached response without double charge.

### Detailed Answer (3–5 minutes)

**Flow:**
1. Receive request + key
2. If key exists → return stored response
3. Else process payment, store result atomically
4. TTL cleanup

**Storage:** Redis or SQL unique constraint on key.

**Mock:** Mention race — two requests same key — DB unique or distributed lock.

### Architecture Perspective

Idempotency is payment mock must-have — key header pattern.

### Follow-up Questions

1. **Key scope? — Per merchant + key — global uniqueness.**
2. **Partial failure? — Store processing state — client retries safely.**

### Common Mistakes in Interviews

- No idempotency on charge endpoint
- Key only client-side
- Race double charge

---

## Q054: Schema Evolution Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Mock: evolve event schema without breaking consumers.

### Short Answer (30 seconds)

Additive changes only (new optional fields), version field in envelope, consumers ignore unknown fields, dual-schema period, contract tests in CI.

### Detailed Answer (3–5 minutes)

**Rules:**
- Never remove/rename in v1 stream
- New `schemaVersion: 2` parallel topic optional
- Upconverters for ES replay

**Mock:** Example add `shippingMethod` optional to OrderCreated.

### Architecture Perspective

Schema evolution mock — backward compatible contracts.

### Follow-up Questions

1. **Protobuf? — Field numbers never reuse.**
2. **Breaking change? — New topic/version consumer group.**

### Common Mistakes in Interviews

- Breaking rename field production
- No contract tests
- Force all consumers deploy same day

---

## Q055: Versioning API Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Mock: API versioning strategy for mobile clients slow to update.

### Short Answer (30 seconds)

URL path `/v1` `/v2` or header `Accept-Version`, maintain v1 minimum 12 months, deprecation sunset headers, feature parity doc.

### Detailed Answer (3–5 minutes)

**Approach:**
- Path versioning visible in logs — common
- Breaking: new major only
- Non-breaking: add fields OK in same version

**Mobile:** Long tail — never force upgrade without grace.

### Architecture Perspective

API versioning mock — mobile long tail drives policy.

### Follow-up Questions

1. **GraphQL versioning? — Deprecate fields — schema registry.**
2. **Internal vs public? — Internal can break faster with coordinated deploy.**

### Common Mistakes in Interviews

- Breaking change in minor version
- No deprecation timeline
- Version only in docs not URL

---

## Q056: Mobile Offline Sync Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

Mock: offline-first mobile notes app sync architecture.

### Short Answer (30 seconds)

Client local SQLite, operation log queue, sync API with vector clocks or last-write-wins per note, conflict UI for merge, background sync on connectivity.

### Detailed Answer (3–5 minutes)

**Server:**
- `POST /sync` batch upsert with client revision
- Return conflicts array

**IDs:** Client-generated UUID for offline creates.

**Mock:** State conflict resolution policy explicitly.

### Architecture Perspective

Offline sync mock — conflict strategy is the crux.

### Follow-up Questions

1. **CRDT? — Auto-merge rich text — advanced mention.**
2. **Delta sync? — Only changes since cursor token.**

### Common Mistakes in Interviews

- Server-only auto-increment IDs
- Last-write-wins no user visibility on conflict
- Full dump sync every time

---

## Q057: Webhook Delivery Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Mock: reliable webhook delivery to customer endpoints.

### Short Answer (30 seconds)

Event queue, HMAC signature, exponential retry 24h, DLQ, delivery log UI, idempotent eventId, circuit per subscriber URL.

### Detailed Answer (3–5 minutes)

**Payload:** `{ eventId, type, data, timestamp }`
**Security:** `X-Signature: HMAC-SHA256(secret, body)`

**Subscriber down:** Retry schedule 1m, 5m, 30m... disable after N days fail.

### Architecture Perspective

Webhook mock — signing and retry schedule expected.

### Follow-up Questions

1. **Ordering? — Per resource sequence number optional.**
2. **Replay? — Customer fetches missed via API by eventId cursor.**

### Common Mistakes in Interviews

- Fire HTTP once no retry
- No signature verification
- No delivery visibility for customer

---

## Q058: Batch Processing Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

Mock: nightly batch ETL 500M rows.

### Short Answer (30 seconds)

Partition input files, Spark/Databricks parallel transform, idempotent writes to warehouse, checkpoint, SLA by 6am, alert on failure, rerun from checkpoint.

### Detailed Answer (3–5 minutes)

**Architecture:**
- Blob raw zone → Spark cluster → Synapse/BigQuery
- Partition by date shard parallel
- Data quality checks gate publish

**Mock:** Estimate runtime with cluster size rough calc.

### Architecture Perspective

Batch mock — partition parallelism and idempotent output.

### Follow-up Questions

1. **Incremental vs full? — Watermark high since last run.**
2. **Failure mid-job? — Checkpoint partition completion.**

### Common Mistakes in Interviews

- Single thread 500M rows
- Overwrite production no staging
- No data quality validation

---

## Q059: Stream Processing Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

Mock: real-time fraud detection on transaction stream.

### Short Answer (30 seconds)

Kafka ingest, Flink/Spark Streaming windowed aggregates, rules + ML model side input, sub-second alert to case management, dead letter for malformed events.

### Detailed Answer (3–5 minutes)

**Windows:** 5-min sliding velocity check
**State:** RocksDB state store per Flink
**Output:** Flag → human review queue + block payment API callback

**Mock:** Discuss at-least-once and idempotent alerts.

### Architecture Perspective

Stream mock — windowing and state store mention scores well.

### Follow-up Questions

1. **Event time vs processing time? — Watermarks for late events.**
2. **Cold path? — Batch retrain model offline.**

### Common Mistakes in Interviews

- Batch poll DB every minute
- Unbounded state per user forever
- No late event handling

---

## Q060: Mock Interview Time Management

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Interview Skills |
| **Frequency** | Very Common |

### Question

How manage time in 45-minute system design mock?

### Short Answer (30 seconds)

5 clarify, 10 HLD, 15 deep dive ONE area, 5 failure/ops, 5 trade-offs, 5 buffer. Set timer mentally at 15 min — must have diagram by then.

### Detailed Answer (3–5 minutes)

**Rules:**
- Interviewer redirect — follow their interest
- Stuck >3 min — state assumption, move on
- Leave last 5 min for their questions
- Practice with phone timer weekly

**Signals to move on:** 'I'll deep dive caching unless you prefer API design.'

**Architect:** Breadth with one solid depth beats shallow everything.

### Architecture Perspective

Time management is trainable — mocks worthless without timer discipline.

### Follow-up Questions

1. **45 vs 60 min? — Adjust deep dive proportionally.**
2. **Post-mock retro? — Score rubric, one improvement next mock.**

### Common Mistakes in Interviews

- No diagram until minute 35
- Argue one detail entire session
- Skip trade-offs at end

---

## Q061: Mock Opening Script

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Open a 45-minute whiteboard mock with a strong first 2 minutes.

### Short Answer (30 seconds)

Confirm problem, state you'll clarify requirements first, ask 3–4 scope questions, propose RESHADED time box, get interviewer agreement before drawing.

### Detailed Answer (3–5 minutes)

**Script:**
'I'll spend 5 minutes on requirements and estimation, 10 on high-level design, 15 on deep dive — does that work?'

**First questions:** DAU, read/write, latency SLA, consistency, out of scope.

**Architect:** Agreement on structure prevents mid-interview derail.

### Architecture Perspective

Strong opening sets senior tone — interviewers notice discipline.

### Follow-up Questions

1. **Interviewer silent? — State assumption and proceed — don't freeze.**
2. **Wrong problem? — Confirm 'design X or Y?' — avoid wasted 20 min.**

### Common Mistakes in Interviews

- Start drawing boxes immediately
- No time box proposed
- Ask zero clarifying questions

---

## Q062: Whiteboard Diagram Conventions

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Label conventions for clear whiteboard architecture diagrams in mocks.

### Short Answer (30 seconds)

Boxes = services, cylinders = databases, clouds = external, arrows labeled with protocol/data, dashed = async, numbers on arrows for QPS optional.

### Detailed Answer (3–5 minutes)

**Conventions:**
- Client left, data stores bottom
- Number components if referencing in talk track
- Color optional: red = critical path
- Legend if symbols non-standard

**Digital:** Excalidraw/Miro same rules — readability > art.

**Architect:** Diagram readable from 6 feet — large text.

### Architecture Perspective

Clear diagrams reduce interviewer confusion — speeds mock.

### Follow-up Questions

1. **C4 level? — Container diagram sufficient — not component unless asked.**
2. **Update diagram? — Cross out old — redraw section — explain change.**

### Common Mistakes in Interviews

- Spaghetti arrows unlabeled
- Tiny unreadable text
- 20 boxes no grouping

---

## Q063: Clarifying Questions Cheat Sheet

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Memorize clarifying questions that apply to most system design mocks.

### Short Answer (30 seconds)

Users/DAU, read vs write ratio, latency p99, consistency, retention, geography, mobile/web, auth required, peak vs average, explicit out-of-scope.

### Detailed Answer (3–5 minutes)

**Universal questions:**
1. Who are the users and scale?
2. Read-heavy or write-heavy?
3. Real-time or eventual consistency OK?
4. Geographic distribution?
5. What's explicitly out of scope?

**Write assumptions on board:** 'Assume 10M DAU, 100:1 R/W.'

**Architect:** 5 questions > 0 — always.

### Architecture Perspective

Question bank prevents blanking under mock pressure.

### Follow-up Questions

1. **NFR conflict? — Ask priority: latency vs consistency if clash.**
2. **Growth rate? — Drives sharding timeline discussion.**

### Common Mistakes in Interviews

- Assume scale silently
- Over-engineer admin tool as Twitter
- Skip consistency question

---

## Q064: Deep Dive Component Selection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

How choose which component to deep dive in a mock when interviewer doesn't specify?

### Short Answer (30 seconds)

Pick the bottleneck from estimation — read-heavy → cache; write-heavy → queue/shard; real-time → WebSocket routing; fanout → feed or notification.

### Detailed Answer (3–5 minutes)

**Selection heuristic:**
| Signal | Deep dive |
|--------|----------|
| 100:1 read | Cache layers + invalidation |
| High write | Sharding or queue |
| Fanout | Notification or feed |
| Consistency | DB replication routing |

**Say:** 'I'll deep dive caching unless you prefer API design.'

**Architect:** One solid depth > three shallow.

### Architecture Perspective

Proactive deep dive choice shows leadership in mock.

### Follow-up Questions

1. **Interviewer redirect? — Follow immediately — their interest scores.**
2. **Stuck 5 min? — State assumption, move on — breadth matters.**

### Common Mistakes in Interviews

- Random deep dive unrelated to scale
- Deep dive before HLD exists
- Refuse to move on when stuck

---

## Q065: Failure Mode Brainstorming

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Spend 5 minutes on failure modes in every mock — what to cover?

### Short Answer (30 seconds)

Single points of failure, dependency outage, hot keys, duplicate messages, network partition, deploy failure — one mitigation each.

### Detailed Answer (3–5 minutes)

**Rapid fire list:**
- DB primary down → replica promote
- Cache down → degrade to DB + circuit breaker
- Queue backlog → autoscale workers
- Provider outage → fallback provider
- Hot key → split + local L1

**Architect:** Pair failure with observability alert.

### Architecture Perspective

Failure section is easy points — don't skip for time.

### Follow-up Questions

1. **Chaos testing? — Mention staging injection — credibility.**
2. **Graceful degradation? — Reduced feature set — not 500 error.**

### Common Mistakes in Interviews

- Never mention failures
- Failure without mitigation
- Only 'we'll add redundancy' vague

---

## Q066: Trade Off Summary Template

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Close mock with 60-second trade-off summary — template.

### Short Answer (30 seconds)

'We chose X over Y because [scale/consistency/team]. Phase 2 would add Z if [trigger metric]. Risk: [item] mitigated by [control].'

### Detailed Answer (3–5 minutes)

**Template:**
1. **Chose:** Cache-aside over write-through — read-heavy 100:1
2. **Deferred:** Sharding — writes only 500 QPS today
3. **Risk:** Cache stale 30s — acceptable per requirements
4. **Monitor:** p99, hit rate, queue depth
5. **Phase 2:** Shard at 5K write QPS

**Architect:** Trade-offs in business terms — not only tech.

### Architecture Perspective

Strong close leaves lasting impression — practice verbatim.

### Follow-up Questions

1. **Alternative rejected? — Name one — shows options considered.**
2. **Evolution path? — Always mention — pragmatism signal.**

### Common Mistakes in Interviews

- End abruptly at time buzzer
- No trade-off stated
- Only list components no decisions

---

## Q067: Mock Debrief Self Scoring

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Self-score after mock using 22-point rubric — what to track?

### Short Answer (30 seconds)

Requirements 2, estimation 2, HLD 3, API 2, storage 2, deep dive 3, failures 2, security 1, monitoring 1, trade-offs 2, communication 2 — log weak dimension for next mock.

### Detailed Answer (3–5 minutes)

**Weekly practice log:**
| Date | Prompt | Score | Weak area | Fix next time |
|------|--------|-------|-----------|---------------|

**Target:** +2 points per week over 4 weeks.

**Architect:** Record mocks — video review catches filler and pacing.

### Architecture Perspective

Deliberate practice requires measurement — rubric enables improvement.

### Follow-up Questions

1. **Peer mock? — Swap interviewer role — calibrate scoring.**
2. **Same prompt repeat? — Retry after 2 weeks — measure delta.**

### Common Mistakes in Interviews

- Mock without debrief
- No written improvement action
- Score yourself perfect every time

---

## Q068: Interviewer Redirect Handling

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Interviewer says 'let's focus on the database' mid-mock — respond.

### Short Answer (30 seconds)

'Absolutely — I'll zoom into storage schema and sharding' — pivot immediately, don't cling to previous deep dive thread.

### Detailed Answer (3–5 minutes)

**Rules:**
- Interviewer interest = scoring path
- Brief acknowledge: 'Great, database is the critical piece here'
- Erase or section off irrelevant deep dive
- Apply full depth to new focus

**Architect:** Flexibility simulates real stakeholder meetings.

### Architecture Perspective

Redirect handling tests adaptability — common in real interviews.

### Follow-up Questions

1. **Disagree with redirect? — Still follow — argue gently offline if wrong.**
2. **Lost time? — Compress remaining sections — still close with trade-offs.**

### Common Mistakes in Interviews

- Ignore redirect continue cache tangent
- Apologize excessively lose time
- Start entirely from scratch

---

## Q069: Assumption Documentation Board

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Maintain visible assumptions list on whiteboard during mock.

### Short Answer (30 seconds)

Top-left box: 'Assumptions' — DAU, R/W ratio, p99, consistency, retention — update as clarified; reference when estimating.

### Detailed Answer (3–5 minutes)

**Example board corner:**
```
ASSUMPTIONS
- 10M DAU
- 100:1 R/W
- p99 200ms feed
- Eventual OK 5s
- US-only v1
```

**Benefit:** Interviewer can correct early — saves redesign.

**Architect:** Assumptions = contract for rest of design.

### Architecture Perspective

Visible assumptions prevent mismatch with interviewer mental model.

### Follow-up Questions

1. **Wrong assumption corrected? — Update list aloud — revise design.**
2. **Sensitivity? — 'If DAU 10×, cache insufficient' — point to assumption.**

### Common Mistakes in Interviews

- Hidden mental assumptions
- Never revise after correction
- Assumptions contradict design choices

---

## Q070: Mock Pacing Time Signals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Recognize pacing signals during mock — when accelerate or stop.

### Short Answer (30 seconds)

15 min no diagram → accelerate HLD. 30 min still on requirements → interviewer will redirect. 40 min no failures → skip to trade-offs. '5 minutes left' → close immediately.

### Detailed Answer (3–5 minutes)

**Time checkpoints:**
| Minute | Must have |
|--------|----------|
| 15 | Diagram + estimation |
| 30 | Deep dive underway |
| 40 | Failures or trade-offs started |
| 45 | Close + questions |

**Architect:** Practice with visible timer — build internal clock.

### Architecture Perspective

Pacing signals prevent incomplete mocks — train with timer.

### Follow-up Questions

1. **Interviewer '5 min left'? — Stop deep dive — summarize trade-offs.**
2. **Over time? — Ask 'should I summarize or continue deep dive?'**

### Common Mistakes in Interviews

- No diagram at 25 minutes
- Deep dive entire second half
- Ignore interviewer time hints

---
