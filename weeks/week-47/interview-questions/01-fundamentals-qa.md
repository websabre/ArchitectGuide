# Week 47 — Fundamentals Interview Q&A

> Q001–Q030: Premium format (Week 1 quality).  
> See also: [Interview prep hub](../../../interview-prep/README.md)

---


## Q001: Microservices Interview Decomposition

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Microservices |
| **Frequency** | Very Common |

### Question

How approach microservices decomposition questions in system design interviews?

### Short Answer (30 seconds)

Decompose by bounded context and team topology — not entity-per-service. State criteria: independent deploy, different scale profiles, change frequency. Recommend modular monolith first; strangler fig extraction when metrics prove pain.

### Detailed Answer (3–5 minutes)

**Decomposition criteria:**
| Criterion | Question to ask |
|-----------|----------------|
| Business capability | Does this map to a domain experts own? |
| Data ownership | Can one team own this schema? |
| Scale profile | Does search need 10× checkout QPS? |
| Deploy independence | Can we ship without coordinating 6 teams? |
| Failure isolation | Should payment outage block catalog browse? |

**Anti-patterns to call out:**
- Microservice per database table
- Distributed monolith — 6 synchronous HTTP calls, shared DB
- Split before identifying aggregate roots

**Migration pattern:** Strangler fig — route `%` traffic to new service via gateway; retire monolith module when stable.

**Conway's law:** Service boundaries should align with team boundaries — or expect friction.

**Interview structure:**
1. Clarify org and scale
2. Identify bounded contexts (payments, catalog, notifications)
3. Draw services with owned data stores
4. Async where possible (events, not chains)
5. Acknowledge operational cost (K8s, tracing, CI × N)

### Architecture Perspective

Microservices decomposition is organizational architecture — interviewers want bounded contexts, not box explosion.

### Follow-up Questions

1. **Modular monolith first? — .NET vertical slices in one deployable — extract when proven.**
2. **Shared database anti-pattern? — Integration via APIs/events — not shared tables.**

### Common Mistakes in Interviews

- 50 services sharing one SQL database
- Synchronous chain across six services
- Split monolith before measuring team or scale pain

---

## Q002: Resilience Patterns Interview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Resilience |
| **Frequency** | Very Common |

### Question

What resilience patterns should architects prioritize in system design interviews?

### Short Answer (30 seconds)

Layer timeouts, retries (idempotent only), circuit breakers, bulkheads, fallbacks, and graceful degradation. State delivery semantics (at-least-once + idempotency) and never retry non-idempotent POSTs blindly.

### Detailed Answer (3–5 minutes)

**Resilience stack (outer to inner):**
```
Timeout → Retry (with jitter) → Circuit Breaker → Bulkhead → Fallback
```

**Pattern guide:**
| Pattern | Purpose | Example |
|---------|---------|--------|
| Timeout | Bound wait | 300ms gateway budget |
| Retry | Transient failures | 3× on 5xx GET with jitter |
| Circuit breaker | Fail fast when downstream sick | Open after 5 fails / 30s |
| Bulkhead | Isolate thread pools | Separate pool per dependency |
| Fallback | Degraded UX | 'Payment pending' queue |
| Rate limit | Protect self and neighbor | 429 at gateway |

**Critical rules:**
- Retry POST payments only with `Idempotency-Key`
- No nested retries across layers (3×3×3 = 27 attempts)
- Circuit half-open: single probe — avoid thundering herd
- Pair resilience with observability — breaker state metric

**Implementations:** Polly (.NET), Istio (service mesh), API gateway policies.

**Interview deep dive pick:** Payment dependency — draw states closed/open/half-open with fallback queue.

### Architecture Perspective

Resilience interviews separate seniors who've seen outages — idempotency and timeout budgets are non-negotiable.

### Follow-up Questions

1. **Chaos engineering? — Inject failures in staging — validate breakers work.**
2. **Saga vs 2PC? — Distributed transactions — compensation not locks.**

### Common Mistakes in Interviews

- Infinite retry on failing payment API
- No timeout on 5-deep microservice chain
- Retry at gateway, service, and client all maxed

---

## Q003: Kubernetes Interview for Architects

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

What Kubernetes topics matter for solution architects — not cluster admin trivia?

### Short Answer (30 seconds)

Focus on workload placement (Deployments, HPA), networking (Ingress, services), config/secrets, health probes, rollout strategies, and when AKS/EKS beats PaaS. Defer CNI plugin details unless platform role.

### Detailed Answer (3–5 minutes)

**Architect K8s checklist:**
| Topic | What to say |
|-------|-------------|
| Workloads | Deployment, StatefulSet for stateful, Job/CronJob |
| Scaling | HPA on CPU/custom metrics; cluster autoscaler |
| Networking | Service ClusterIP → Ingress → TLS |
| Config | ConfigMap, Secret — externalize; never bake in image |
| Health | Liveness vs readiness — readiness removes from LB |
| Rollouts | Rolling update, maxUnavailable 0; canary via mesh/Argo |
| Observability | Prometheus metrics, OTel collectors, log sidecars |
| Security | RBAC, network policies, pod identity to cloud IAM |

**When K8s vs PaaS:**
- **AKS/EKS** — polyglot, custom sidecars, GPU, portable workloads
- **App Service** — .NET team, steady traffic, less ops headcount

**Production narrative:**
```
CI → container registry → GitOps (ArgoCD) → Deployment
Readiness probe gates traffic; preStop drain connections
```

**Architect pitfalls:** Running K8s without platform team; no resource requests/limits; singleton DB in pod without PVC strategy.

### Architecture Perspective

Kubernetes for architects is deployability and operability — probes, rollouts, and identity — not kubectl trivia.

### Follow-up Questions

1. **Service mesh when? — mTLS, canary, observability — cost of complexity.**
2. **Pod Disruption Budget? — HA during node drains — mention in rollout mock.**

### Common Mistakes in Interviews

- K8s chosen because 'industry standard' without ops team
- Liveness and readiness identical probe
- No resource limits — noisy neighbor OOM kills

---

## Q004: System Design Interview Framework

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

What framework should architects use to structure a 45-minute system design interview?

### Short Answer (30 seconds)

Use RESHADED or equivalent: Requirements → Estimation → Storage → High-level design → APIs → Deep dive → Edge cases → Distinctive points. Never jump to Redis before clarifying read/write ratio and latency SLA.

### Detailed Answer (3–5 minutes)

**RESHADED (45-min time box):**
| Phase | Minutes | Actions |
|-------|---------|--------|
| **R**equirements | 5 | Functional + NFR; state assumptions |
| **E**stimation | 5 | QPS, storage, bandwidth |
| **S**torage | 5 | Schema, DB choice, sharding |
| **H**igh-level design | 10 | Boxes, arrows, data flow |
| **A**PIs | 5 | Key endpoints, contracts |
| **D**eep dive | 10 | Bottleneck — cache, queue, fanout |
| **E**dge cases | 3 | Failures, hot keys, duplicates |
| **D**istinctive | 2 | Trade-offs, monitoring, evolution |

**Requirements must clarify:**
- DAU, read/write ratio, p99 latency, consistency, geography, retention

**Estimation template:**
`QPS = DAU × actions/day ÷ 86400 × peak factor 3`

**Distinctive close:** 'Phase 1 monolith + cache; Phase 2 shard writes; monitor queue depth and p99.'

**Self-check before ending:** Did I address failures, security, and observability?

### Architecture Perspective

Framework discipline signals senior judgment — interviewers forgive imperfect depth if structure and assumptions are clear.

### Follow-up Questions

1. **C4 model relation? — Context/container in HLD phase — component detail only if time.**
2. **Similar frameworks? — REPE, FAST — same intent — pick one and practice.**

### Common Mistakes in Interviews

- Jump to components without requirements
- Skip estimation entirely
- Deep dive before drawing high-level diagram

---

## Q005: Scalability Interview Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Scalability |
| **Frequency** | Very Common |

### Question

What scalability patterns should architects rehearse for system design interviews?

### Short Answer (30 seconds)

Master horizontal scale, caching tiers, async decoupling, read replicas, sharding, CDN, and load balancing — each tied to a trigger (read-heavy, write-heavy, global users, hot keys).

### Detailed Answer (3–5 minutes)

**Pattern selection matrix:**
| Bottleneck signal | Pattern |
|-------------------|--------|
| Read-heavy | Cache-aside, CDN, read replicas |
| Write-heavy | Sharding, queue buffering, partition keys |
| Traffic spikes | Autoscale, queue absorption, rate limits |
| Global latency | CDN, multi-region read, geo DNS |
| Hot key | Key splitting, local L1, request coalescing |
| Heavy processing | Async workers, scale on queue depth |

**Layered scale story:**
1. **Stateless app** — horizontal pods behind LB
2. **Cache** — Redis cluster, TTL + invalidation
3. **DB** — read replicas → shard when write ceiling hit
4. **Async** — Service Bus/Kafka decouple peak
5. **Edge** — CDN for static and cacheable API responses

**Architect rules:**
- Scale stateless first — session in JWT/Redis
- Measure before shard — operational cost is high
- Document consistency trade-off per read path

**Interview phrase:** 'At 100:1 read/write, I'd add Redis cache-aside before considering write sharding.'

### Architecture Perspective

Scalability patterns are conditional — architects match pattern to measured bottleneck, not checklist architecture.

### Follow-up Questions

1. **Vertical scale when? — Short-term relief — not long-term strategy; mention before horizontal.**
2. **Database connection storm? — Pooler, PgBouncer, limit pods × pool size.**

### Common Mistakes in Interviews

- Shard on day one without write pressure
- Cache with no invalidation strategy
- Scale servers without fixing N+1 queries first

---

## Q006: RESHADED Walkthrough

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

Walk through the RESHADED framework for system design interviews.

### Short Answer (30 seconds)

RESHADED: Requirements, Estimation, Storage, High-level design, APIs, Deep dive, Edge cases, Distinctive points. Structured 45-min flow interviewers expect.

### Detailed Answer (3–5 minutes)

**Steps:**
1. **Requirements** — functional + NFR (scale, latency, consistency)
2. **Estimation** — QPS, storage, bandwidth — back-of-envelope
3. **Storage** — schema, DB choice, sharding
4. **High-level design** — boxes and arrows
5. **APIs** — key endpoints, contracts
6. **Deep dive** — bottleneck component (feed fanout, cache)
7. **Edge cases** — failures, hot keys, duplicates
8. **Distinctive** — trade-offs, evolution, monitoring

**Architect:** RESHADED keeps you from jumping to Redis without clarifying read/write ratio.

### Architecture Perspective

Framework shows interview discipline — adapt naming but keep structure.

### Follow-up Questions

1. **Similar frameworks? — REPE / FAST — same intent.**
2. **When skip estimation? — Never — even rough orders of magnitude.**

### Common Mistakes in Interviews

- Random component list no requirements
- Deep dive before high-level
- Ignore NFR until end

---

## Q007: Requirements Clarification

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

What requirements must you clarify before designing a system?

### Short Answer (30 seconds)

Functional scope, users/DAU, read vs write ratio, latency p99, consistency needs, durability, geographic distribution, growth, and explicit out-of-scope.

### Detailed Answer (3–5 minutes)

**Questions to ask:**
- Mobile + web? Anonymous users?
- Real-time or eventual OK?
- Strong consistency for payments?
- Retention period (affects storage cost)
- Multi-tenant or consumer?

**Document assumptions:** 'Assume 10M DAU, 100:1 read/write, 200ms p99 feed load.'

**Architect:** Clarification prevents designing Twitter when they wanted internal admin tool.

### Architecture Perspective

Requirement questions signal senior judgment — interviewers reward this phase.

### Follow-up Questions

1. **Out of scope? — Explicitly state 'not designing ML ranking v2'.**
2. **NFR priority? — Ask which matters most if conflict.**

### Common Mistakes in Interviews

- Assume requirements silently
- Over-engineer without scale numbers
- Skip consistency discussion

---

## Q008: Scale Estimation Interview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

Perform back-of-envelope scale estimation for 10M DAU social app.

### Short Answer (30 seconds)

DAU 10M, 10 actions/day = 100M ops/day ≈ 1.2K QPS average, 3–5K peak. 1KB per post × 10M posts/day = 10GB/day storage growth before replication.

### Detailed Answer (3–5 minutes)

**Template:**
- Ops/day = DAU × actions
- QPS = ops/day / 86400 × peak factor 3
- Storage = objects/day × size × retention
- Bandwidth = QPS × payload size

**Example:**
- 100M reads, 1M writes → cache wins
- 3-year retention → plan TB archive tier

**Architect:** Estimation drives SQL vs NoSQL, shard count, CDN need — show math on whiteboard.

### Architecture Perspective

Estimation doesn't need precision — orders of magnitude and assumptions stated.

### Follow-up Questions

1. **Power of two? — 1M seconds ≈ 11.5 days — quick mental math.**
2. **Wrong by 10×? — OK if you note sensitivity.**

### Common Mistakes in Interviews

- No math at all
- Memorized numbers without derivation
- Ignore peak factor

---

## Q009: API Design Interview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

Design REST APIs for a URL shortener — key endpoints and considerations.

### Short Answer (30 seconds)

`POST /urls` create short link, `GET /{code}` redirect, `GET /urls/{id}/stats` analytics. Idempotent create with client key, 301 vs 302, rate limits, auth for management.

### Detailed Answer (3–5 minutes)

**Design:**
```
POST /v1/urls  { longUrl, customAlias?, ttl? } → { shortUrl, id }
GET  /{code}    → 302 Location (track click async)
GET  /v1/urls/{id}/analytics → { clicks, referrers }
```

**Considerations:**
- Version prefix `/v1`
- Pagination on list endpoints
- ProblemDetails errors
- API keys for create, public redirect

**Architect:** Separate read (redirect) hot path from write API — different scale profiles.

### Architecture Perspective

API design shows product thinking — not just CRUD names.

### Follow-up Questions

1. **GraphQL when? — Complex clients — shortener doesn't need it.**
2. **gRPC internal? — Redirect edge HTTP, internal gRPC fine.**

### Common Mistakes in Interviews

- Unversioned breaking changes
- Analytics on synchronous redirect path
- No rate limit on create

---

## Q010: Database Schema Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

Design database schema for e-commerce orders.

### Short Answer (30 seconds)

Tables: customers, products, orders, order_items, payments. Normalize OLTP, index (customer_id, created_at), avoid duplicating product price — snapshot at order time.

### Detailed Answer (3–5 minutes)

**Schema:**
```
orders(id, customer_id, status, total, created_at)
order_items(order_id, product_id, qty, unit_price_snapshot)
payments(order_id, provider, status, amount)
```

**Decisions:**
- Snapshot price in order_items — historical accuracy
- Status enum — state machine documented
- Soft delete vs archive

**Architect:** Identify aggregate root — Order owns items — transactional boundary.

### Architecture Perspective

Schema design tests normalization vs read optimization balance.

### Follow-up Questions

1. **JSON columns? — Flexible attributes — index carefully.**
2. **UUID vs bigint PK? — UUID for distributed ID gen.**

### Common Mistakes in Interviews

- Store only product_id — price changes break history
- God table orders+items+payments
- No index on customer order history query

---

## Q011: Caching Layer Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

Design caching layer for read-heavy product catalog.

### Short Answer (30 seconds)

CDN for static assets, Redis cache-aside for product JSON by ID, local in-process L1 for top 1K SKUs, TTL 5–15 min, invalidate on product update event.

### Detailed Answer (3–5 minutes)

**Layers:**
1. **CDN** — images, static JSON bundles
2. **Redis cluster** — `product:{id}` hash
3. **App L1** — MemoryCache 30s for hot items

**Invalidation:** ProductUpdated event → cache delete + CDN purge API.

**Architect:** Measure hit rate target 90%+. Stampede protection on popular product drop.

### Architecture Perspective

Multi-tier cache is standard senior answer — specify invalidation.

### Follow-up Questions

1. **Cache key design? — Include locale, version — `product:us:123:v2`.**
2. **Negative caching? — Cache 404 briefly — prevent DB hammer.**

### Common Mistakes in Interviews

- Infinite TTL on inventory counts
- Single Redis no HA
- Cache without miss path to DB

---

## Q012: Load Balancer Selection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

When use L4 vs L7 load balancer?

### Short Answer (30 seconds)

L4 (TCP): ultra-high throughput, pass-through TLS, gaming, DB proxy. L7 (HTTP): path-based routing, TLS termination, sticky sessions, WAF integration, gRPC/HTTP2.

### Detailed Answer (3–5 minutes)

**L7 (ALB, Azure App Gateway):**
- Route `/api` vs `/static`
- Health checks on HTTP path
- SSL offload

**L4 (NLB, Azure Load Balancer):**
- Millions RPS, static IP, preserve client IP

**Architect:** Public entry often L7 + WAF; internal microservice mesh may use L4 sidecar.

### Architecture Perspective

LB choice ties to routing needs — not 'always ALB'.

### Follow-up Questions

1. **Sticky sessions? — Session affinity — prefer stateless JWT.**
2. **Global LB? — Front Door, CloudFront, Route53 latency routing.**

### Common Mistakes in Interviews

- L7 when only TCP needed — unnecessary parsing cost
- No health checks
- Single LB SPOF no multi-AZ

---

## Q013: CDN Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

Design CDN usage for global media streaming startup.

### Short Answer (30 seconds)

Origin in S3/Blob, CloudFront/Azure CDN PoPs, cache-control headers, signed URLs for premium content, origin shield, separate cache behaviors for video segments vs thumbnails.

### Detailed Answer (3–5 minutes)

**Design:**
- **HLS/DASH segments** — long cache, immutable URLs with version
- **Thumbnails** — shorter TTL
- **Signed cookies** — prevent hotlinking
- **Origin shield** — reduce origin load

**Architect:** 90%+ egress from CDN not origin — monitor cache hit ratio.

### Architecture Perspective

CDN design includes security (signed URLs) and cache semantics.

### Follow-up Questions

1. **Cache invalidation? — Version in URL path — preferred over purge.**
2. **Dynamic content CDN? — Edge workers limited — mostly static.**

### Common Mistakes in Interviews

- CDN for uncacheable personalized API
- No TTL strategy
- Origin exposed publicly bypassing CDN

---

## Q014: Message Queue Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

Design message queue integration for order processing.

### Short Answer (30 seconds)

Order API writes DB + outbox, publisher sends to queue, workers process payment/shipping idempotently, DLQ for failures, visibility timeout, poison message handling.

### Detailed Answer (3–5 minutes)

**Flow:**
```
API → DB txn (order + outbox) → relay → Service Bus queue
→ workers (competing consumers) → external APIs
```

**Choices:**
- Ordering: partition by orderId
- At-least-once + idempotent consumer
- DLQ alert + replay tooling

**Architect:** Backpressure — queue depth metric autoscales workers.

### Architecture Perspective

Queue design requires delivery semantics and failure paths.

### Follow-up Questions

1. **Queue vs stream? — Kafka when replay needed; queue for task distribution.**
2. **Priority queue? — Separate queues premium vs standard.**

### Common Mistakes in Interviews

- Fire-and-forget HTTP no persistence
- No DLQ
- Exactly-once without idempotency plan

---

## Q015: Microservices Decomposition

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

How decompose monolith into microservices?

### Short Answer (30 seconds)

By bounded context (DDD), align to team topology, split on change frequency and scale profile, strangler fig migration, avoid distributed monolith shared DB.

### Detailed Answer (3–5 minutes)

**Criteria:**
- **Business capability** — payments, catalog, notifications
- **Independent deploy** — separate CI/CD
- **Different scale** — search vs checkout

**Anti-pattern:** 50 services sharing one database.

**Architect:** Start with modular monolith — extract when pain proven by metrics.

### Architecture Perspective

Decomposition by org and domain — not entity-per-service.

### Follow-up Questions

1. **Conway's law? — Team boundaries shape service boundaries.**
2. **Shared library vs service? — Duplicate small code OK — avoid shared DB.**

### Common Mistakes in Interviews

- Microservice per database table
- Distributed monolith synchronous chain
- Split before identifying bounded contexts

---

## Q016: Saga Interview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

Explain saga pattern for distributed order checkout.

### Short Answer (30 seconds)

Sequence of local transactions with compensating actions on failure — choreography (events) or orchestration (central coordinator).

### Detailed Answer (3–5 minutes)

**Orchestrated saga:**
1. Reserve inventory → OK
2. Charge payment → FAIL → compensate: release inventory
3. Create shipment — skipped

**Choreography:** Each service listens and publishes — OrderCreated → PaymentRequested.

**Architect:** Orchestration easier to debug; choreography looser coupling. Store saga state machine durable (SQL, Temporal).

### Architecture Perspective

Saga replaces 2PC — interviewers want compensation examples.

### Follow-up Questions

1. **Outbox? — Reliable event publish with local txn.**
2. **Duplicate saga step? — Idempotent handlers + sagaId.**

### Common Mistakes in Interviews

- Distributed two-phase commit across clouds
- No compensation defined
- Saga state only in memory

---

## Q017: Circuit Breaker Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

Design circuit breaker for payment service dependency.

### Short Answer (30 seconds)

States: closed (normal), open (fail fast), half-open (probe). Open after 5 failures in 30s, half-open after 60s, close after 3 successes.

### Detailed Answer (3–5 minutes)

**Implementation:**
- Polly / Istio / resilience4j
- Fallback: queue payment retry job, show 'payment pending' UX
- Monitor breaker state metric

**Architect:** Breaker protects your SLA when vendor down — don't retry storm into failing service.

### Architecture Perspective

Circuit breaker is failure isolation — pair with timeout and bulkhead.

### Follow-up Questions

1. **Bulkhead? — Separate thread pool per dependency.**
2. **Half-open thundering herd? — Single probe request.**

### Common Mistakes in Interviews

- Infinite retry to failing payment API
- No fallback UX
- Breaker never monitored

---

## Q018: Rate Limiter Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

Design distributed rate limiter — 100 req/min per user.

### Short Answer (30 seconds)

Token bucket or sliding window in Redis with Lua atomicity, key `ratelimit:{userId}`, return 429 + Retry-After, optional global limit per API key.

### Detailed Answer (3–5 minutes)

**Algorithm:**
```
Sliding window log in Redis ZSET
OR token bucket: tokens += rate * dt, cap burst
```

**Placement:** API gateway edge — reject before app tier.

**Architect:** Different limits per tier (free vs paid). Log rate limit hits for abuse detection.

### Architecture Perspective

Distributed rate limiter is classic design — Redis + atomic ops.

### Follow-up Questions

1. **Local vs global? — Per-node limit unfair — use Redis.**
2. **Fair queuing? — Advanced — weighted shares.**

### Common Mistakes in Interviews

- In-memory limit per server only
- Race condition without atomic Redis script
- No 429 response headers

---

## Q019: Notification System Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

High-level design for multi-channel notification system (email, SMS, push).

### Short Answer (30 seconds)

Event ingestion → template service → priority queues per channel → workers with provider adapters → delivery status webhook → user preference filter.

### Detailed Answer (3–5 minutes)

**Components:**
- Notification API / event consumer
- Template store (i18n)
- User preferences (opt-out per channel)
- Queue per channel (SMS rate limited)
- Provider abstraction (SendGrid, Twilio, FCM)
- Idempotency key per notification

**Scale:** Millions/day — batch digest emails separately from transactional OTP.

### Architecture Perspective

Notification design hits fanout, preferences, and provider failure — classic interview.

### Follow-up Questions

1. **Priority? — OTP > marketing — separate queues.**
2. **Quiet hours? — Scheduler delays non-urgent.**

### Common Mistakes in Interviews

- Synchronous send in API request
- No unsubscribe compliance
- Single queue all channels

---

## Q020: URL Shortener Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

Design URL shortener supporting 100M URLs and 10K redirects/sec.

### Short Answer (30 seconds)

Base62 encode ID or hash, SQL/NoSQL store mapping, Redis cache hot codes, read replicas, 302 redirect, analytics async via Kafka.

### Detailed Answer (3–5 minutes)

**ID generation:** Counter shard or Snowflake — avoid collision.
**Read path:** Cache → DB replica → 302.
**Write path:** Primary DB, populate cache.

**Storage:** 100M × 500B ≈ 50GB — single shard OK initially.

**Architect:** Separate redirect service minimal deps — ultra-low latency.

### Architecture Perspective

URL shortener tests read-heavy optimization and ID generation.

### Follow-up Questions

1. **Custom alias collision? — Unique constraint, 409 conflict.**
2. **Expired URLs? — TTL job or lazy check.**

### Common Mistakes in Interviews

- MD5 truncate collision prone
- Analytics on redirect critical path
- No cache for hot links

---

## Q021: News Feed Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

Design news feed for 10M users — fanout on write vs read?

### Short Answer (30 seconds)

Hybrid: fanout on write for normal users (precompute timeline in Redis), fanout on read for celebrities (millions followers). Ranked feed optional ML tier async.

### Detailed Answer (3–5 minutes)

**Write fanout:** Post created → push postId to followers' feed lists (cap 1000 recent).
**Read:** Pull merged timeline, rank, paginate.

**Celebrity:** Followers fetch from celebrity post list at read time.

**Storage:** User feed cache (Redis), posts table (Cassandra/SQL).

**Architect:** Define consistency — follower may see post few seconds late OK.

### Architecture Perspective

Feed fanout trade-off is THE news feed interview topic.

### Follow-up Questions

1. **Ranking? — Score = time decay + engagement — precompute or realtime.**
2. **Pagination? — Cursor not offset — stable under new posts.**

### Common Mistakes in Interviews

- Fanout on write for 50M follower account
- No feed cap unbounded memory
- Pull all posts global on read

---

## Q022: Chat System Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

Design real-time chat for 1M concurrent connections.

### Short Answer (30 seconds)

WebSocket gateway cluster, message service, conversation store (Cassandra by conversationId), presence service, push for offline, sequence numbers per conversation.

### Detailed Answer (3–5 minutes)

**Flow:**
- Client WS to gateway (sticky or user routing table)
- Message → queue → persist → fanout to recipient gateways
- Delivery receipts async

**History:** Paginate by sequenceId. **Groups:** fanout to member list.

**Architect:** Partition by conversationId. Multi-region: CRDT or last-write-wins policy documented.

### Architecture Perspective

Chat combines real-time, ordering, and presence — state connection routing.

### Follow-up Questions

1. **WebSocket vs SSE? — Bidirectional needs WS.**
2. **E2E encryption? — Out of scope or key exchange layer.**

### Common Mistakes in Interviews

- HTTP poll every second
- No message ordering guarantee
- Single WS server no scale plan

---

## Q023: Search System Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

Design product search for e-commerce.

### Short Answer (30 seconds)

Ingest pipeline (CDC) → Elasticsearch index, search API with filters/facets, autocomplete from edge n-grams, spell correction, ranking by relevance + business rules.

### Detailed Answer (3–5 minutes)

**Components:**
- Catalog changes → Kafka → indexer
- ES cluster sharded by category
- Search API: query parsing, pagination, aggregations
- Cache popular queries

**Architect:** Search is eventually consistent with catalog — lag SLA 1–5 min acceptable.

### Architecture Perspective

Search is inverted index + pipeline — not SQL LIKE.

### Follow-up Questions

1. **Personalization? — Boost user brand affinity — separate ranker.**
2. **Zero results? — Synonyms, fuzzy match fallback.**

### Common Mistakes in Interviews

- SQL LIKE on product name
- Synchronous index on every write to ES in API
- No facet/filter design

---

## Q024: File Storage Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

Design file upload/storage for Dropbox-like service.

### Short Answer (30 seconds)

Client uploads to blob via presigned URL, metadata DB (fileId, userId, chunks, hash), dedup by content hash, CDN download, multipart for large files, virus scan async.

### Detailed Answer (3–5 minutes)

**Upload:**
1. Client requests upload URL
2. Direct PUT to S3/Blob
3. Callback registers metadata
4. Chunking for >100MB resume

**Dedup:** SHA-256 block-level saves storage.

**Architect:** Never proxy large files through API servers — direct to object storage.

### Architecture Perspective

File storage design emphasizes presigned URLs and metadata separation.

### Follow-up Questions

1. **Conflict resolution? — Version vector or last-write-wins.**
2. **Sharing links? — ACL table + signed download URL.**

### Common Mistakes in Interviews

- Files through app server memory
- No multipart resume
- Metadata and blob orphan risk on failed callback

---

## Q025: Distributed Cache

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

Design distributed cache cluster for 100GB working set.

### Short Answer (30 seconds)

Redis Cluster or Memcached consistent hash, replication for HA, client-side hashing, TTL policy, monitor evictions and hot keys.

### Detailed Answer (3–5 minutes)

**Sizing:** 100GB + 30% overhead = 130GB RAM across 6 nodes.
**HA:** Primary-replica per shard, auto-failover.
**Hot key:** Local replica read, or key splitting `user:123:part{n}`.

**Architect:** Cache is not source of truth — define cold-start warmup.

### Architecture Perspective

Distributed cache ops: sharding, eviction, hot keys — all fair game.

### Follow-up Questions

1. **Redis vs Memcached? — Redis richer data structures; Memcached simpler.**
2. **Near cache? — Client library L1 in app pod.**

### Common Mistakes in Interviews

- Single Redis instance production
- No eviction policy
- Cache stampede unmitigated

---

## Q026: ID Generation Snowflake

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

Explain Snowflake ID generation and trade-offs.

### Short Answer (30 seconds)

64-bit: timestamp + machineId + sequence — sortable, unique without coordination, ~4096 IDs/ms per machine. Needs clock sync and machine ID assignment.

### Detailed Answer (3–5 minutes)

**Layout (Twitter Snowflake):** 41b timestamp | 10b node | 12b sequence.

**Pros:** Time-ordered, DB index friendly, no central DB bottleneck.
**Cons:** Clock rollback handling, machine ID management in K8s.

**Alternatives:** UUID v4 (random, not sortable), DB sequence (bottleneck), ULID.

**Architect:** Snowflake for high-write sharded OLTP; UUID for client-generated offline IDs.

### Architecture Perspective

ID generation appears in every high-scale design — know Snowflake layout.

### Follow-up Questions

1. **Clock skew? — Wait or use logical clock increment.**
2. **K8s pod machineId? — Assign from StatefulSet ordinal or coordination service.**

### Common Mistakes in Interviews

- Auto-increment single DB at 100K writes/sec
- UUID v1 MAC leakage concern ignored
- Duplicate machine IDs

---

## Q027: Consistency Models Interview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Distributed Systems |
| **Frequency** | Very Common |

### Question

Compare strong, eventual, and causal consistency with examples.

### Short Answer (30 seconds)

Strong: read sees latest write (SQL primary read). Eventual: replicas converge (DNS, Dynamo). Causal: preserve cause ordering (social comments thread).

### Detailed Answer (3–5 minutes)

**Examples:**
- **Bank balance** — strong or linearizable
- **Like count** — eventual OK
- **Chat order** — causal or per-partition ordering

**Cosmos:** Tunable consistency per request.

**Architect:** Pick per operation not per system — payment strong, analytics eventual.

### Architecture Perspective

Consistency model literacy avoids one-size-fits-all CAP hand-waving.

### Follow-up Questions

1. **Read-your-writes? — Session consistency — common UX need.**
2. **Linearizability cost? — Coordination latency cross-region.**

### Common Mistakes in Interviews

- Strong everywhere unnecessarily
- Eventual for inventory deduction
- No user-visible consistency definition

---

## Q028: Partition Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

Choose partition key for IoT time-series telemetry.

### Short Answer (30 seconds)

Partition by (deviceId, date) or deviceId hash — avoid hot partition on single device flood, enable time-range pruning, consider Timescale/Cosmos partition key design.

### Detailed Answer (3–5 minutes)

**Strategies:**
- **deviceId** — even if devices equal rate
- **deviceId + hour** — if single device very hot
- **Geo region** — compliance + locality

**Anti-pattern:** Partition only by timestamp — all writes one partition.

**Architect:** Validate with peak device telemetry rate estimate.

### Architecture Perspective

Partition key choice is irreversible pain — interview focus area.

### Follow-up Questions

1. **Repartition migration? — Dual-write new shard scheme — expensive.**
2. **Synthetic key? — Salt hot keys `{deviceId}#{random 0-9}`.**

### Common Mistakes in Interviews

- Timestamp-only partition key
- Cross-partition queries in hot path
- Ignore storage growth per partition limit

---

## Q029: Hot Key Problem

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

How solve hot key problem in distributed cache or database?

### Short Answer (30 seconds)

Key splitting, local in-process cache replica, read replicas with random fanout, pre-warm, combine request coalescing, or application-level aggregation.

### Detailed Answer (3–5 minutes)

**Techniques:**
1. **Split key** — `popularProduct:{0..N}` round-robin
2. **Local cache** — 1s TTL on app node for scorching key
3. **Read replica random** — spread reads
4. **Coalescing** — single flight pattern — one DB hit

**Celebrity post:** Fanout on read not write.

**Architect:** Monitor per-key QPS — alert threshold.

### Architecture Perspective

Hot key is production war story — multiple mitigations show experience.

### Follow-up Questions

1. **Redis hot key? — Redis Cluster slot still one node — split key.**
2. **Write hot key? — Queue serialization — shard writers.**

### Common Mistakes in Interviews

- Ignore viral event scenario
- Only vertical scale bigger Redis
- No monitoring per-key metrics

---

## Q030: System Design Rubric Self-Check

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Interview Skills |
| **Frequency** | Very Common |

### Question

Self-check rubric before ending system design interview.

### Short Answer (30 seconds)

Did I clarify requirements, estimate scale, draw diagram, define APIs, deep dive bottleneck, address failures, security, monitoring, and trade-offs?

### Detailed Answer (3–5 minutes)

**Checklist (score 0–2 each):**
- Requirements & assumptions stated
- Back-of-envelope math
- Clear component diagram
- Data model / storage choice justified
- API contracts sketched
- Deep dive on critical path
- Single points of failure addressed
- Caching / async where appropriate
- Security (auth, encryption)
- Observability (metrics, logs, alerts)
- Evolution path mentioned

**Architect:** 16+ / 22 points — strong loop. Leave 3 min for questions.

### Architecture Perspective

Self-check prevents leaving easy points on table — practice with rubric.

### Follow-up Questions

1. **Weak deep dive? — Pick cache or queue — always have go-to.**
2. **Time box? — Move on if stuck 5 min — breadth beats perfect depth.**

### Common Mistakes in Interviews

- End without trade-off summary
- Never mention monitoring
- No assumptions documented

---
