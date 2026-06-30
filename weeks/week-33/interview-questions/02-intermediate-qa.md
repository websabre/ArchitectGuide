# Week 33 — Intermediate Q&A

> Q031–Q070: Premium format (Week 1 quality).

---


## Q031: RESHADED Framework

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Methodology |
| **Frequency** | Very Common |

### Question

Walk through RESHADED for system design interviews.

### Short Answer (30 seconds)

Requirements, Estimation, Storage, High-level design, API, Deep dive, Edge cases, Deployment. Never skip requirements — interviewers withhold info to test clarification.

### Detailed Answer (3–5 minutes)

Spend 5 min on functional + NFR: scale, latency, durability, consistency, geographic distribution.

Write assumptions on board. State what you defer (e.g., 'security detail in deep dive if time').

### Architecture Perspective

Framework discipline prevents premature diagramming.

### Follow-up Questions

1. **RESHADED vs C4? — RESHADED for timed interview; C4 for documentation.**
2. **Time check at 20 min? — Must enter deep dive — don't over-detail early components.**

### Common Mistakes in Interviews

- Jumping to microservices diagram in minute 2
- No numbers in estimation
- Silent design without thinking aloud

---

## Q032: Requirements Clarification

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Requirements |
| **Frequency** | Very Common |

### Question

What questions ask before designing Twitter feed?

### Short Answer (30 seconds)

Read/write ratio, fan-out model, celebrity users, latency SLA, consistency, media support, delete/edit, follower count limits.

### Detailed Answer (3–5 minutes)

Miss celebrity user problem → naive fan-out-on-write fails. Ask: 'Max followers per user? Read timeline latency target? Consistent global ordering needed?'

### Architecture Perspective

Requirements questions differentiate senior candidates.

### Follow-up Questions

1. **MVP scope? — Explicitly defer analytics, ads — focus core feed.**
2. **DAU vs MAU? — Drives estimation — clarify.**

### Common Mistakes in Interviews

- Assume requirements without asking
- Over-engineer features not requested
- Ignore read/write asymmetry

---

## Q033: Back-of-Envelope Estimation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Estimation |
| **Frequency** | Very Common |

### Question

Estimate storage for 100M users, 2 tweets/day, 280 chars, 5 years.

### Short Answer (30 seconds)

100M × 2 × 365 × 5 = 365B tweets. ~300 bytes/tweet with metadata ≈ 110TB raw before replication and indexes. 3x replication ≈ 330TB.

### Detailed Answer (3–5 minutes)

Show math on board. Round aggressively. State assumptions: average text length, metadata overhead, media excluded.

QPS: 100M DAU × 2 / 86400 ≈ 2300 write QPS average, peak 5×.

### Architecture Perspective

Estimation proves engineering judgment.

### Follow-up Questions

1. **Bandwidth estimate? — Write QPS × payload size — CDN for media separate.**
2. **Index overhead? — 2-3x storage — mention.**

### Common Mistakes in Interviews

- No assumptions stated
- Exact precision false confidence
- Forget replication factor

---

## Q034: API Design in System Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | API |
| **Frequency** | Common |

### Question

Design REST API for URL shortener.

### Short Answer (30 seconds)

`POST /v1/urls` {longUrl, customAlias?} → {shortCode}. `GET /{shortCode}` → 301 redirect. `DELETE /v1/urls/{code}` auth. Rate limit headers.

### Detailed Answer (3–5 minutes)

Idempotent POST with Idempotency-Key for create. Version in path. ProblemDetails errors.

Consider internal vs public API separation.

### Architecture Perspective

API sketch shows you can ship not just diagram boxes.

### Follow-up Questions

1. **302 vs 301 redirect? — 301 permanent — analytics implications.**
2. **Custom alias collision? — 409 Conflict — unique constraint.**

### Common Mistakes in Interviews

- RPC-style random verbs
- No error response design
- Missing rate limit discussion

---

## Q035: High-Level Diagram Discipline

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Communication |
| **Frequency** | Common |

### Question

How draw effective whiteboard architecture diagram?

### Short Answer (30 seconds)

Left: clients. Center: LB, API, cache, DB. Right: async workers. Label protocols. Legend for symbols. One box per logical component first — refine in deep dive.

### Detailed Answer (3–5 minutes)

Avoid 20 boxes minute one. Show data flow arrows with read vs write path different colors if possible.

Name technologies after logical design approved: 'cache' then 'Redis'.

### Architecture Perspective

Clear diagrams communicate faster than words in interview.

### Follow-up Questions

1. **Single diagram overload? — High-level first — zoom deep dive second diagram.**
2. **Bidirectional arrows everywhere? — Label read vs write paths.**

### Common Mistakes in Interviews

- Technology logos before logical design
- Unreadable tiny boxes
- No legend

---

## Q036: Deep Dive Selection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Strategy |
| **Frequency** | Common |

### Question

Interviewer says 'deep dive any component.' Which pick?

### Short Answer (30 seconds)

Pick bottleneck or most interesting: usually cache, database shard, or messaging. Show trade-offs you considered and rejected.

### Detailed Answer (3–5 minutes)

Prepare 2 deep dives in mind while drawing high-level — likely ask about data store and hot path.

Go deep on: schema, sharding key, cache invalidation, consistency.

### Architecture Perspective

Strategic deep dive choice shows experience.

### Follow-up Questions

1. **Database deep dive template? — Schema, indexes, shard key, replication.**
2. **Cache deep dive? — Pattern, TTL, invalidation, stampede.**

### Common Mistakes in Interviews

- Shallow overview of all components
- Deep dive load balancer only — boring unless asked
- No trade-offs mentioned

---

## Q037: Failure Mode Analysis

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reliability |
| **Frequency** | Very Common |

### Question

What failures discuss before interview ends?

### Short Answer (30 seconds)

Single server down, DB primary failure, cache down, network partition, hot key, cascade failure. Mitigation: replication, circuit breaker, degrade gracefully.

### Detailed Answer (3–5 minutes)

Template: 'If Redis fails, fall through to DB — higher latency but available.' 'If DB primary down, failover to replica — 30s RTO.'

### Architecture Perspective

Failure discussion mandatory for pass score.

### Follow-up Questions

1. **Cascading failure? — Timeout + circuit breaker — stop retry storm.**
2. **Data center loss? — Multi-region — RPO/RTO numbers.**

### Common Mistakes in Interviews

- Happy path only design
- No monitoring mention
- Infinite retry on failure

---

## Q038: Monitoring and SLIs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Observability |
| **Frequency** | Common |

### Question

Define SLIs for URL shortener.

### Short Answer (30 seconds)

Availability: successful redirects / total. Latency: p99 redirect < 100ms. Correctness: wrong redirect rate ~ 0.

### Detailed Answer (3–5 minutes)

SLI → SLO → error budget. Alert on burn rate. Dashboard: QPS, cache hit ratio, DB replication lag.

### Architecture Perspective

SLO literacy expected at architect level.

### Follow-up Questions

1. **Synthetic monitoring? — Probe redirect from multiple regions.**
2. **Business metric SLI? — Links created per minute — capacity planning.**

### Common Mistakes in Interviews

- No metrics defined
- Alert on CPU only
- 100% availability SLO

---

## Q039: Scope Management in 45 Minutes

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Interview Skill |
| **Frequency** | Common |

### Question

Running out of time in system design interview?

### Short Answer (30 seconds)

Explicitly prioritize: 'I'll cover data model and skip CDN unless time.' Ask interviewer preference.

### Detailed Answer (3–5 minutes)

Better to deep dive one area well than shallow everything.

Leave 3 min for failures — reserve time early.

### Architecture Perspective

Time management is scored implicitly.

### Follow-up Questions

1. **Checkpoint at 15 min? — 'High-level complete — proceed to deep dive?'**
2. **Rabbit hole? — 'I'll note open question and continue.'**

### Common Mistakes in Interviews

- Panic and rush diagram
- Ignore interviewer hint to move on
- No time reserved for failures

---

## Q040: Post-Design Evolution

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Evolution |
| **Frequency** | Common |

### Question

Interviewer: 'How does design change at 100x scale?'

### Short Answer (30 seconds)

Identify first bottleneck from estimation. 100x QPS → shard DB, regional caches, separate write/read path, async preprocessing.

### Detailed Answer (3–5 minutes)

Show evolution path — not redesign from scratch. 'Phase 1 monolith OK; at 10M users add read replicas; at 100M shard by userId.'

### Architecture Perspective

Evolution thinking shows production experience.

### Follow-up Questions

1. **When rewrite? — When operational cost of patch exceeds rewrite — rare — justify.**
2. **Cost at 100x? — Mention linear vs superlinear cost drivers.**

### Common Mistakes in Interviews

- Same design regardless of scale
- Shard day one for 1000 users
- Cannot identify bottleneck

---

## Q041: Functional vs Non-Functional Requirements

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Requirements |
| **Frequency** | Very Common |

### Question

How separate functional and non-functional requirements in a system design interview?

### Short Answer (30 seconds)

Functional: what the system does (create short URL, redirect). Non-functional: how well (latency, scale, availability, consistency, cost). Clarify both before drawing.

### Detailed Answer (3–5 minutes)

**Functional examples:** user registration, post tweet, send message, search products.

**NFR examples:** 99.9% availability, p99 read < 100ms, 10M DAU, GDPR data residency, $X/month budget.

**Interview technique:** Write two columns on board. For each feature ask 'what breaks if we ignore NFR?' — e.g., feed without latency target leads to wrong fan-out choice.

**Architect habit:** NFRs drive technology choices; functional reqs drive API and data model.

### Architecture Perspective

Senior candidates surface NFRs proactively — juniors only list features.

### Follow-up Questions

1. **Which NFR first for URL shortener? — Read latency and availability — write is rare.**
2. **Implicit NFR trap? — 'Real-time' undefined — ask: p99 under 200ms?**

### Common Mistakes in Interviews

- Only listing features
- Treating all NFRs as hard constraints without trade-offs
- No prioritization when NFRs conflict

---

## Q042: Back-of-Envelope QPS

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Estimation |
| **Frequency** | Very Common |

### Question

Estimate peak QPS for 50M DAU social app, each user 20 actions/day.

### Short Answer (30 seconds)

50M × 20 / 86400 ≈ 11,600 avg QPS. Peak 3–5× → ~35K–58K QPS. Split read/write if ratio known.

### Detailed Answer (3–5 minutes)

**Formula:** `QPS = DAU × actions_per_user / 86400`.

**Peak factor:** Lunch/evening spikes, viral events — state assumption (3× or 5×).

**Read/write split:** If 90% read, 10% write → 52K read, 5.8K write at 5× peak.

**Why it matters:** 5K write QPS fits single primary DB with tuning; 500K needs sharding. Show math — interviewers score process not exact number.

### Architecture Perspective

QPS estimation gates every scaling decision in the interview.

### Follow-up Questions

1. **MAU vs DAU? — Use DAU for capacity — MAU overestimates.**
2. **Global vs single-region QPS? — Shard estimate per region if geo-distributed.**

### Common Mistakes in Interviews

- Using MAU as DAU
- No peak multiplier
- Single QPS number without read/write split

---

## Q043: Storage Estimation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Estimation |
| **Frequency** | Very Common |

### Question

Estimate 5-year storage for photo-sharing: 200M users, 5 photos/week, 2MB average.

### Short Answer (30 seconds)

200M × 5 × 52 × 5 = 260B photos. × 2MB ≈ 520PB raw. Metadata ~1KB/photo adds ~260TB. Replication 3× → ~1.5EB class — CDN/object store not single DB.

### Detailed Answer (3–5 minutes)

**Steps:** objects/year × years × size + metadata overhead + indexes (often 10–20%).

**Compression:** JPEG already compressed — don't double-count.

**Tiering:** Hot 30 days SSD, warm S3, cold Glacier — effective cost not raw PB.

**Interview:** Round to nearest order of magnitude. State 'object storage + CDN, not relational DB for blobs.'

### Architecture Perspective

Storage math proves you won't put petabytes in PostgreSQL.

### Follow-up Questions

1. **Thumbnail storage? — 10× originals if not deduplicated — call out.**
2. **Delete/account erasure? — Tombstone + async purge — retention policy affects storage.**

### Common Mistakes in Interviews

- Storing blobs in SQL
- Forgetting metadata and index overhead
- No replication factor in estimate

---

## Q044: Bandwidth Estimation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Estimation |
| **Frequency** | Common |

### Question

Bandwidth for video streaming: 1M concurrent viewers, 5 Mbps stream.

### Short Answer (30 seconds)

1M × 5 Mbps = 5 Tbps egress. Requires CDN edge — origin cannot serve directly.

### Detailed Answer (3–5 minutes)

**Ingress:** Upload 10K creators × 5 Mbps = 50 Gbps — smaller than egress.

**CDN absorbs** 95%+ of viewer traffic — origin bandwidth = cache miss rate × viewers.

**Cost driver:** Egress is often largest cloud bill line — architect mentions CDN and peering.

**Units:** Watch Mbps vs MBps. 1 byte = 8 bits.

### Architecture Perspective

Bandwidth estimation connects QPS to infrastructure cost.

### Follow-up Questions

1. **API JSON bandwidth? — QPS × avg payload — often smaller than media.**
2. **Cross-AZ egress? — Same-region traffic pricing — design data locality.**

### Common Mistakes in Interviews

- Origin serves all video traffic
- Confuse Mbps and MBps
- Ignore CDN in bandwidth math

---

## Q045: REST API Design for System Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | API |
| **Frequency** | Very Common |

### Question

Design REST resources for a ride-sharing system.

### Short Answer (30 seconds)

`POST /v1/rides` request ride. `GET /v1/rides/{id}` status. `PATCH /v1/rides/{id}` cancel. `GET /v1/drivers/{id}/location` — separate resources, nouns not verbs.

### Detailed Answer (3–5 minutes)

**Principles:** Resource-oriented URLs, HTTP verbs match semantics, versioning in path, pagination on collections, HATEOAS optional in interview.

**Status codes:** 201 Created + Location header, 409 conflict on double-book, 202 Accepted for async dispatch.

**Internal vs external:** Public REST; internal may use gRPC — mention both layers.

### Architecture Perspective

REST sketch shows API thinking beyond boxes and arrows.

### Follow-up Questions

1. **RPC-style `/createRide`? — Acceptable if team standard — justify consistency.**
2. **Idempotency on POST? — `Idempotency-Key` header — critical for payments/rides.**

### Common Mistakes in Interviews

- Verb in URL `/getRide`
- 200 for everything
- No versioning strategy

---

## Q046: Idempotency Keys in API Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | API |
| **Frequency** | Very Common |

### Question

How implement idempotency keys for `POST /payments`?

### Short Answer (30 seconds)

Client sends `Idempotency-Key: uuid`. Server stores key + response in Redis/DB with TTL 24h. Duplicate key returns cached response without re-charging.

### Detailed Answer (3–5 minutes)

**Flow:** Receive request → check key exists → if yes return stored response → if no process in TX, store result, return.

**Scope:** Per merchant or per user. Key collision across users acceptable if UUID.

**Stripe pattern:** Standard industry reference — architects cite it.

**Failure:** Store result before returning 200 — crash after charge but before store causes duplicate on retry without key.

### Architecture Perspective

Idempotency is mandatory for any money or inventory mutation API.

### Follow-up Questions

1. **Key TTL? — 24h typical — balance storage vs client retry window.**
2. **Same key different body? — Reject 422 — key body mismatch.**

### Common Mistakes in Interviews

- Idempotency only on GET
- No storage of idempotent responses
- Assume network never retries

---

## Q047: Pagination Cursor vs Offset

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | API |
| **Frequency** | Common |

### Question

When cursor pagination vs offset for social feed API?

### Short Answer (30 seconds)

Cursor (keyset): stable under inserts, efficient at depth — `?after=tweetId&limit=20`. Offset: simple but slow `OFFSET 100000` and duplicates/skips under concurrent writes.

### Detailed Answer (3–5 minutes)

**Cursor:** Encode `(timestamp, id)` tuple — unique sort key. O(limit) per page.

**Offset:** OK for admin tables < 10K rows. Bad for infinite scroll feeds.

**Bidirectional:** `before` and `after` cursors for scroll up/down.

**Interview:** Default recommend cursor for user-facing feeds; offset for internal reports.

### Architecture Perspective

Pagination choice affects DB index design and UX consistency.

### Follow-up Questions

1. **Opaque cursor? — Base64 encode — hide internal IDs.**
2. **Total count header? — Expensive on large tables — optional `X-Total-Count`.**

### Common Mistakes in Interviews

- OFFSET on billion-row feed
- Cursor without stable sort key
- Page number API for real-time feed

---

## Q048: Rate Limiting Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Rate Limiting |
| **Frequency** | Very Common |

### Question

Design rate limiting for public API: 1000 req/min per API key, burst allowed.

### Short Answer (30 seconds)

Token bucket in Redis: refill 1000/60 tokens/sec, bucket capacity 100 for burst. Return 429 + `Retry-After` + `X-RateLimit-Remaining`.

### Detailed Answer (3–5 minutes)

**Layers:** Edge (CloudFront/WAF), API gateway (APIM), app middleware — defense in depth.

**Distributed:** Central Redis — not per-node counters (uneven under LB).

**Tiers:** Free 100/min, paid 10K/min — keyed by API key or tenantId.

**Grace:** Soft limit warn header; hard limit 429.

### Architecture Perspective

Rate limiting protects platform and is architect-level API contract.

### Follow-up Questions

1. **Global vs per-endpoint limits? — Stricter on expensive endpoints (search, export).**
2. **Internal service bypass? — mTLS identity whitelist — not IP alone.**

### Common Mistakes in Interviews

- Per-server rate limit only
- 429 without Retry-After
- No rate limit on auth/login endpoints

---

## Q049: Authentication at Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Design auth for 100M-user SaaS: sessions vs JWT?

### Short Answer (30 seconds)

JWT access token (short TTL 15m) + refresh token (rotating, HttpOnly cookie or secure store). Validate JWT at gateway without DB hit. Revocation list for compromised tokens.

### Detailed Answer (3–5 minutes)

**Scale path:** Stateless JWT verification at edge — O(1) per request.

**Session store:** Redis for server-side session if needed — sticky avoided via shared store.

**OAuth2/OIDC:** Delegate to Entra/Auth0 for enterprise SSO.

**Architect:** Never put PII in JWT payload. Key rotation via JWKS endpoint.

### Architecture Perspective

Auth at scale requires stateless verification and clear token lifecycle.

### Follow-up Questions

1. **Refresh token rotation? — Detect reuse — revoke family on theft.**
2. **Service-to-service? — mTLS or client credentials — not user JWT.**

### Common Mistakes in Interviews

- Long-lived JWT with no revocation
- Session in server memory behind LB
- Validate auth only in app not gateway

---

## Q050: Multi-Tenant SaaS Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Multi-Tenancy |
| **Frequency** | Very Common |

### Question

Design data isolation for B2B SaaS with 10K tenants.

### Short Answer (30 seconds)

Pool model: `tenantId` on every row + row-level security. Bridge: pool for SMB, dedicated DB for enterprise. Cache keys always include `tenantId`.

### Detailed Answer (3–5 minutes)

**Isolation levels:** Pool (shared schema), bridge (pools by tier), silo (DB per tenant).

**Auth:** Resolve tenant from subdomain or JWT claim — inject into request context — every query scoped.

**Noisy neighbor:** Per-tenant rate limits and fair queue scheduling.

**Compliance:** Enterprise may require silo + encryption per tenant CMK.

### Architecture Perspective

Multi-tenancy is cross-cutting — data, cache, queue, and billing.

### Follow-up Questions

1. **Cross-tenant query leak test? — Automated security tests mandatory.**
2. **Tenant migration silo? — Dual-write + cutover playbook.**

### Common Mistakes in Interviews

- Missing tenantId in cache key
- Global admin API without tenant scope
- One shard key ignoring hot enterprise tenant

---

## Q051: URL Shortener System Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

Design URL shortener for 100M URLs/month, 10:1 read/write ratio.

### Short Answer (30 seconds)

Write: hash or base62 counter → store in SQL/NoSQL. Read: cache (Redis) → redirect 301. LB + stateless API. 7-char base62 ≈ 3.5T codes.

### Detailed Answer (3–5 minutes)

**Key components:** API, ID generator, DB (shortCode PK, longUrl, userId, createdAt), cache, analytics async.

**Custom alias:** Unique constraint — 409 on collision.

**Expiration:** TTL column + lazy delete.

**Scale read path:** 99% cache hit — DB handles miss only.

### Architecture Perspective

URL shortener is canonical interview — know cold.

### Follow-up Questions

1. **Base62 vs hash? — Counter + base62 sequential; hash risks collision.**
2. **Analytics separate? — Async click event to Kafka — don't block redirect.**

### Common Mistakes in Interviews

- DB hit on every redirect
- MD5 truncate without collision handling
- 302 vs 301 choice unexplained

---

## Q052: Paste Bin System Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | System Design |
| **Frequency** | Common |

### Question

Design Pastebin: 10M pastes/month, some expire in 10 minutes, some never.

### Short Answer (30 seconds)

Object storage (S3) for content + metadata DB. TTL index for expiry. CDN for popular pastes. Key: random 8-char ID — not sequential (security).

### Detailed Answer (3–5 minutes)

**Write:** Store blob → return URL. **Read:** CDN → origin on miss.

**Expiry:** DynamoDB TTL or cron sweeper. **Max size:** 1MB limit — reject larger.

**Privacy:** Unlisted vs public — no search index for unlisted.

**Syntax highlighting:** Pre-render or client-side — async job for large files.

### Architecture Perspective

Pastebin exercises blob + metadata split and TTL design.

### Follow-up Questions

1. **Sequential IDs? — Enumeration attack — use random keys.**
2. **Encryption at rest? — Optional private pastes — per-object KMS.**

### Common Mistakes in Interviews

- Store megabyte pastes in SQL row
- No expiry mechanism
- Public listing of all pastes

---

## Q053: News Feed System Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

Design Twitter-style news feed for 300M users.

### Short Answer (30 seconds)

Hybrid fan-out: normal users fan-out on write to follower feeds (Redis sorted sets). Celebrities fan-out on read — merge at read time.

### Detailed Answer (3–5 minutes)

**Components:** post service, timeline service, social graph, media CDN, fan-out workers.

**Celebrity problem:** User with 50M followers — write fan-out impossible — detect threshold.

**Ranking:** Score = time decay + engagement — precompute vs real-time — trade latency.

### Architecture Perspective

Feed design tests fan-out strategy — the core scaling fork.

### Follow-up Questions

1. **Consistent ordering global? — Usually per-user timeline — not global total order.**
2. **Delete/edit tweet? — Fan-out cleanup job or tombstone in feed.**

### Common Mistakes in Interviews

- Fan-out on write for all users including celebrities
- Single DB for all timelines
- No cache for home timeline read

---

## Q054: Chat System Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

Design WhatsApp-scale 1:1 chat: delivery and read receipts.

### Short Answer (30 seconds)

WebSocket gateway per user connection. Message service stores in Cassandra/Scylla partitioned by `(conversationId, timestamp)`. Push via APNs/FCM when offline.

### Detailed Answer (3–5 minutes)

**Flow:** Send → persist → ack sender → push recipient → delivery receipt → read receipt.

**Ordering:** Per-conversation sequence number — not global.

**Group chat:** Separate fan-out to members — message ID idempotency.

**Presence:** Heartbeat + Redis presence store — 'last seen'.

### Architecture Perspective

Chat combines real-time connections with durable message store.

### Follow-up Questions

1. **WebSocket scaling? — Sticky connection to gateway node — Redis pub/sub cross-node.**
2. **E2E encryption? — Server stores ciphertext only — architect acknowledges trade-off.**

### Common Mistakes in Interviews

- HTTP poll for real-time chat
- No offline message queue
- Global message ordering requirement

---

## Q055: Notification System Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

Design notification system: email, SMS, push — 1B notifications/day.

### Short Answer (30 seconds)

Event bus → router by channel → priority queues → worker pools → provider adapters. Template service. User preference store. Idempotent `notificationId`.

### Detailed Answer (3–5 minutes)

**Priority:** OTP > transactional > marketing. **Rate limit:** Per user per channel per hour.

**Retry:** Exponential backoff — DLQ after N failures.

**Providers:** Abstract SendGrid/Twilio/FCM behind adapter interface.

**Digest:** Scheduler batches low-priority email.

### Architecture Perspective

Notification platform is common whiteboard — prepare template answer.

### Follow-up Questions

1. **Unsubscribe compliance? — CAN-SPAM/GDPR — preference honored before send.**
2. **Fan-out cost? — 1 event × 3 channels — budget provider API costs.**

### Common Mistakes in Interviews

- Synchronous send in user request path
- No user preference check
- Single thread for all email

---

## Q056: Search Autocomplete System Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | System Design |
| **Frequency** | Common |

### Question

Design search autocomplete for e-commerce: 10M queries/day, p99 < 50ms.

### Short Answer (30 seconds)

Trie or prefix index in Redis/memory + popular queries precomputed. Data pipeline aggregates search logs → updates top-K suggestions nightly + trending real-time stream.

### Detailed Answer (3–5 minutes)

**Architecture:** Typeahead API → cache layer → prefix index. Fallback to full search on miss.

**Personalization:** Optional user history segment — separate index per segment or post-filter.

**Bad words:** Blocklist filter before return.

### Architecture Perspective

Autocomplete is read-heavy prefix problem — not full Elasticsearch per keystroke.

### Follow-up Questions

1. **Elasticsearch completion suggester? — Valid at scale — shard by prefix.**
2. **Debouncing? — Client 200ms debounce — reduces QPS 5×.**

### Common Mistakes in Interviews

- Full search index per keystroke
- No trending update pipeline
- Return unfiltered user-generated suggestions

---

## Q057: Distributed ID Generation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | System Design |
| **Frequency** | Very Common |

### Question

Compare approaches for globally unique order IDs at 10K/sec.

### Short Answer (30 seconds)

Options: DB auto-increment (bottleneck), UUID v4 (random, index fragmentation), UUID v7 (time-sortable), Snowflake (64-bit structured), DB sequence per shard + offset.

### Detailed Answer (3–5 minutes)

**Requirements:** Unique, roughly sortable by time, no coordination hot spot, fits in 64 bits preferred.

**Snowflake:** 41-bit timestamp + 10-bit machine + 12-bit sequence — 4096/ms per machine.

**DB sequences:** `shardId << 48 | localSequence` — embed shard in ID.

**Interview:** State trade-offs — pick Snowflake or UUID v7 for distributed write-heavy.

### Architecture Perspective

ID generation is early deep-dive in order/payment systems.

### Follow-up Questions

1. **Clock skew Snowflake? — Wait or use logical clock — NTP discipline.**
2. **Expose sequential IDs publicly? — Enumeration risk — opaque encoding.**

### Common Mistakes in Interviews

- Single DB auto-increment at 10K writes/sec
- UUID v4 as clustered index in SQL
- No plan for machine ID assignment

---

## Q058: Snowflake ID Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | IDs |
| **Frequency** | Common |

### Question

Explain Twitter Snowflake ID layout and operational concerns.

### Short Answer (30 seconds)

64 bits: 1 unused, 41 timestamp ms, 10 datacenter+worker, 12 sequence. Sortable, no DB coordination, ~4096 IDs/ms per worker.

### Detailed Answer (3–5 minutes)

**Deployment:** ZooKeeper/etcd assigns worker IDs — avoid manual collision.

**Clock backward:** Refuse to generate until caught up — or use sequence borrow.

**vs UUID v7:** Snowflake denser, custom layout; UUID v7 standard interoperable.

**Storage:** BIGINT column — efficient index vs 36-char UUID string.

### Architecture Perspective

Snowflake is production-proven pattern architects should detail.

### Follow-up Questions

1. **Sequence exhaustion 4096/ms? — Add worker IDs or microshard generators.**
2. **Parse ID for debugging? — Extract timestamp from bits — ops convenience.**

### Common Mistakes in Interviews

- Duplicate worker IDs across datacenters
- Ignore clock synchronization
- Snowflake for public-facing sequential exposure without encoding

---

## Q059: UUID vs Sequential IDs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | IDs |
| **Frequency** | Common |

### Question

When UUID vs sequential BIGINT primary key?

### Short Answer (30 seconds)

Sequential: better B-tree locality, smaller indexes, predictable — risk enumeration, single-writer hotspot. UUID: distributed generation, opaque — worse index fragmentation (v4), larger keys.

### Detailed Answer (3–5 minutes)

**Mitigations:** UUID v7 time-ordered reduces fragmentation. **Hybrid:** BIGINT internal + public UUID external.

**Postgres:** `gen_random_uuid()` vs `BIGSERIAL` — measure insert TPS.

**Security:** Public APIs use opaque IDs — not sequential orderId.

### Architecture Perspective

PK choice affects insert performance and security surface.

### Follow-up Questions

1. **COMB GUID? — Legacy SQL Server pattern — similar to UUID v7 goal.**
2. **Distributed sequences? — Hi/Lo, segment allocation from DB.**

### Common Mistakes in Interviews

- UUID v4 as PK on billion-row insert-heavy table without testing
- Sequential ID in public URL
- Ignore index fragmentation in estimate

---

## Q060: Design Interview Communication

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Interview Skill |
| **Frequency** | Very Common |

### Question

How structure thinking aloud in a 45-minute system design interview?

### Short Answer (30 seconds)

Narrate framework: 'I'll clarify requirements, estimate, sketch high-level, then deep dive.' Pause for interviewer input. State assumptions explicitly. Check time at 15 and 30 minutes.

### Detailed Answer (3–5 minutes)

**Techniques:** Think aloud not silent drawing. Label arrows. Say trade-offs: 'I chose X over Y because...'

**Engagement:** 'Does this match what you're looking for?' after requirements.

**Recovery:** Stuck → state options, pick one, justify. Better than freeze.

**Close:** Reserve 5 min for failures, monitoring, evolution.

### Architecture Perspective

Communication score is separate from technical score — practice narrating.

### Follow-up Questions

1. **Interviewer redirect? — Follow hint — they want specific depth.**
2. **Whiteboard vs virtual? — Excalidraw — pre-practice tool fluency.**

### Common Mistakes in Interviews

- Silent diagramming 10 minutes
- Defensive when challenged
- No time check — skip failure modes

---

## Q061: RESHADED Acronym

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | System Design Methodology |
| **Frequency** | Very Common |

### Question

Explain reshaded acronym for a system design or architecture interview.

### Short Answer (30 seconds)

Requirements, Estimation, Storage, High-level, API, Data model, Estimation, Deep-dive — interview framework.

### Detailed Answer (3–5 minutes)

**RESHADED Acronym:**

Requirements, Estimation, Storage, High-level, API, Data model, Estimation, Deep-dive — interview framework.

**Production context (.NET/Azure):**
Apply in ASP.NET Core on Azure App Service or AKS with patterns from week 33.

**Key points:**
- When to use vs avoid
- Measurable outcome (latency, DORA, SLO)
- Common production pitfall and mitigation

**Example:** Instrument with Application Insights; track deployment in Azure DevOps.

**Architect:** Capture trade-offs in ADR when multiple valid approaches exist.

### Architecture Perspective

RESHADED Acronym is foundational for week 33 — articulate clearly before tool names.

### Follow-up Questions

1. **How measure success? — Tie reshaded acronym to SLI, DORA metric, or business KPI.**
2. **Common anti-pattern? — Adopting tools before understanding reshaded acronym principles.**

### Common Mistakes in Interviews

- Define reshaded acronym with buzzwords only
- No concrete Azure/.NET example
- Cannot link concept to measurable outcome

---

## Q062: System Design Interview Flow

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | System Design Methodology |
| **Frequency** | Very Common |

### Question

Explain system design interview flow for a system design or architecture interview.

### Short Answer (30 seconds)

Clarify → estimate → diagram → deep dive → trade-offs → wrap — time-box each.

### Detailed Answer (3–5 minutes)

**System Design Interview Flow:**

Clarify → estimate → diagram → deep dive → trade-offs → wrap — time-box each.

**Production context (.NET/Azure):**
Apply in ASP.NET Core on Azure App Service or AKS with patterns from week 33.

**Key points:**
- When to use vs avoid
- Measurable outcome (latency, DORA, SLO)
- Common production pitfall and mitigation

**Example:** Instrument with Application Insights; track deployment in Azure DevOps.

**Architect:** Capture trade-offs in ADR when multiple valid approaches exist.

### Architecture Perspective

System Design Interview Flow is foundational for week 33 — articulate clearly before tool names.

### Follow-up Questions

1. **How measure success? — Tie system design interview flow to SLI, DORA metric, or business KPI.**
2. **Common anti-pattern? — Adopting tools before understanding system design interview flow principles.**

### Common Mistakes in Interviews

- Define system design interview flow with buzzwords only
- No concrete Azure/.NET example
- Cannot link concept to measurable outcome

---

## Q063: Requirements Clarification

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | System Design Methodology |
| **Frequency** | Very Common |

### Question

Explain requirements clarification for a system design or architecture interview.

### Short Answer (30 seconds)

Ask about scale, users, read/write, consistency, latency before designing.

### Detailed Answer (3–5 minutes)

**Requirements Clarification:**

Ask about scale, users, read/write, consistency, latency before designing.

**Production context (.NET/Azure):**
Apply in ASP.NET Core on Azure App Service or AKS with patterns from week 33.

**Key points:**
- When to use vs avoid
- Measurable outcome (latency, DORA, SLO)
- Common production pitfall and mitigation

**Example:** Instrument with Application Insights; track deployment in Azure DevOps.

**Architect:** Capture trade-offs in ADR when multiple valid approaches exist.

### Architecture Perspective

Requirements Clarification is foundational for week 33 — articulate clearly before tool names.

### Follow-up Questions

1. **How measure success? — Tie requirements clarification to SLI, DORA metric, or business KPI.**
2. **Common anti-pattern? — Adopting tools before understanding requirements clarification principles.**

### Common Mistakes in Interviews

- Define requirements clarification with buzzwords only
- No concrete Azure/.NET example
- Cannot link concept to measurable outcome

---

## Q064: Back-of-Envelope Math

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | System Design Methodology |
| **Frequency** | Very Common |

### Question

Explain back-of-envelope math for a system design or architecture interview.

### Short Answer (30 seconds)

QPS, storage, bandwidth — round assumptions; state aloud for interviewer correction.

### Detailed Answer (3–5 minutes)

**Back-of-Envelope Math:**

QPS, storage, bandwidth — round assumptions; state aloud for interviewer correction.

**Production context (.NET/Azure):**
Apply in ASP.NET Core on Azure App Service or AKS with patterns from week 33.

**Key points:**
- When to use vs avoid
- Measurable outcome (latency, DORA, SLO)
- Common production pitfall and mitigation

**Example:** Instrument with Application Insights; track deployment in Azure DevOps.

**Architect:** Capture trade-offs in ADR when multiple valid approaches exist.

### Architecture Perspective

Back-of-Envelope Math is foundational for week 33 — articulate clearly before tool names.

### Follow-up Questions

1. **How measure success? — Tie back-of-envelope math to SLI, DORA metric, or business KPI.**
2. **Common anti-pattern? — Adopting tools before understanding back-of-envelope math principles.**

### Common Mistakes in Interviews

- Define back-of-envelope math with buzzwords only
- No concrete Azure/.NET example
- Cannot link concept to measurable outcome

---

## Q065: API Design in Interviews

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | System Design Methodology |
| **Frequency** | Very Common |

### Question

Explain api design in interviews for a system design or architecture interview.

### Short Answer (30 seconds)

REST resources, pagination, errors, auth — sketch key endpoints early.

### Detailed Answer (3–5 minutes)

**API Design in Interviews:**

REST resources, pagination, errors, auth — sketch key endpoints early.

**Production context (.NET/Azure):**
Apply in ASP.NET Core on Azure App Service or AKS with patterns from week 33.

**Key points:**
- When to use vs avoid
- Measurable outcome (latency, DORA, SLO)
- Common production pitfall and mitigation

**Example:** Instrument with Application Insights; track deployment in Azure DevOps.

**Architect:** Capture trade-offs in ADR when multiple valid approaches exist.

### Architecture Perspective

API Design in Interviews is foundational for week 33 — articulate clearly before tool names.

### Follow-up Questions

1. **How measure success? — Tie api design in interviews to SLI, DORA metric, or business KPI.**
2. **Common anti-pattern? — Adopting tools before understanding api design in interviews principles.**

### Common Mistakes in Interviews

- Define api design in interviews with buzzwords only
- No concrete Azure/.NET example
- Cannot link concept to measurable outcome

---

## Q066: Failure Modes Brainstorm

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | System Design Methodology |
| **Frequency** | Very Common |

### Question

Explain failure modes brainstorm for a system design or architecture interview.

### Short Answer (30 seconds)

What if DB down, cache miss, network partition — show resilience thinking.

### Detailed Answer (3–5 minutes)

**Failure Modes Brainstorm:**

What if DB down, cache miss, network partition — show resilience thinking.

**Production context (.NET/Azure):**
Apply in ASP.NET Core on Azure App Service or AKS with patterns from week 33.

**Key points:**
- When to use vs avoid
- Measurable outcome (latency, DORA, SLO)
- Common production pitfall and mitigation

**Example:** Instrument with Application Insights; track deployment in Azure DevOps.

**Architect:** Capture trade-offs in ADR when multiple valid approaches exist.

### Architecture Perspective

Failure Modes Brainstorm is foundational for week 33 — articulate clearly before tool names.

### Follow-up Questions

1. **How measure success? — Tie failure modes brainstorm to SLI, DORA metric, or business KPI.**
2. **Common anti-pattern? — Adopting tools before understanding failure modes brainstorm principles.**

### Common Mistakes in Interviews

- Define failure modes brainstorm with buzzwords only
- No concrete Azure/.NET example
- Cannot link concept to measurable outcome

---

## Q067: Scope Management Technique

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | System Design Methodology |
| **Frequency** | Common |

### Question

Explain scope management technique for a system design or architecture interview.

### Short Answer (30 seconds)

Explicit in/out of scope; parking lot; don't gold-plate v1.

### Detailed Answer (3–5 minutes)

**Scope Management Technique:**

Explicit in/out of scope; parking lot; don't gold-plate v1.

**Production context (.NET/Azure):**
Apply in ASP.NET Core on Azure App Service or AKS with patterns from week 33.

**Key points:**
- When to use vs avoid
- Measurable outcome (latency, DORA, SLO)
- Common production pitfall and mitigation

**Example:** Instrument with Application Insights; track deployment in Azure DevOps.

**Architect:** Capture trade-offs in ADR when multiple valid approaches exist.

### Architecture Perspective

Scope Management Technique is foundational for week 33 — articulate clearly before tool names.

### Follow-up Questions

1. **How measure success? — Tie scope management technique to SLI, DORA metric, or business KPI.**
2. **Common anti-pattern? — Adopting tools before understanding scope management technique principles.**

### Common Mistakes in Interviews

- Define scope management technique with buzzwords only
- No concrete Azure/.NET example
- Cannot link concept to measurable outcome

---

## Q068: Trade-off Communication

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | System Design Methodology |
| **Frequency** | Common |

### Question

Explain trade-off communication for a system design or architecture interview.

### Short Answer (30 seconds)

SQL vs NoSQL table with pros/cons and your choice — decisive but flexible.

### Detailed Answer (3–5 minutes)

**Trade-off Communication:**

SQL vs NoSQL table with pros/cons and your choice — decisive but flexible.

**Production context (.NET/Azure):**
Apply in ASP.NET Core on Azure App Service or AKS with patterns from week 33.

**Key points:**
- When to use vs avoid
- Measurable outcome (latency, DORA, SLO)
- Common production pitfall and mitigation

**Example:** Instrument with Application Insights; track deployment in Azure DevOps.

**Architect:** Capture trade-offs in ADR when multiple valid approaches exist.

### Architecture Perspective

Trade-off Communication is foundational for week 33 — articulate clearly before tool names.

### Follow-up Questions

1. **How measure success? — Tie trade-off communication to SLI, DORA metric, or business KPI.**
2. **Common anti-pattern? — Adopting tools before understanding trade-off communication principles.**

### Common Mistakes in Interviews

- Define trade-off communication with buzzwords only
- No concrete Azure/.NET example
- Cannot link concept to measurable outcome

---

## Q069: High-Level Diagram Discipline

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | System Design Methodology |
| **Frequency** | Common |

### Question

Explain high-level diagram discipline for a system design or architecture interview.

### Short Answer (30 seconds)

5-7 boxes; label protocols; iterate don't erase — add revision box.

### Detailed Answer (3–5 minutes)

**High-Level Diagram Discipline:**

5-7 boxes; label protocols; iterate don't erase — add revision box.

**Production context (.NET/Azure):**
Apply in ASP.NET Core on Azure App Service or AKS with patterns from week 33.

**Key points:**
- When to use vs avoid
- Measurable outcome (latency, DORA, SLO)
- Common production pitfall and mitigation

**Example:** Instrument with Application Insights; track deployment in Azure DevOps.

**Architect:** Capture trade-offs in ADR when multiple valid approaches exist.

### Architecture Perspective

High-Level Diagram Discipline is foundational for week 33 — articulate clearly before tool names.

### Follow-up Questions

1. **How measure success? — Tie high-level diagram discipline to SLI, DORA metric, or business KPI.**
2. **Common anti-pattern? — Adopting tools before understanding high-level diagram discipline principles.**

### Common Mistakes in Interviews

- Define high-level diagram discipline with buzzwords only
- No concrete Azure/.NET example
- Cannot link concept to measurable outcome

---

## Q070: Phased Evolution Close

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | System Design Methodology |
| **Frequency** | Common |

### Question

Explain phased evolution close for a system design or architecture interview.

### Short Answer (30 seconds)

MVP → scale phases triggered by metrics — pragmatic architect signal.

### Detailed Answer (3–5 minutes)

**Phased Evolution Close:**

MVP → scale phases triggered by metrics — pragmatic architect signal.

**Production context (.NET/Azure):**
Apply in ASP.NET Core on Azure App Service or AKS with patterns from week 33.

**Key points:**
- When to use vs avoid
- Measurable outcome (latency, DORA, SLO)
- Common production pitfall and mitigation

**Example:** Instrument with Application Insights; track deployment in Azure DevOps.

**Architect:** Capture trade-offs in ADR when multiple valid approaches exist.

### Architecture Perspective

Phased Evolution Close is foundational for week 33 — articulate clearly before tool names.

### Follow-up Questions

1. **How measure success? — Tie phased evolution close to SLI, DORA metric, or business KPI.**
2. **Common anti-pattern? — Adopting tools before understanding phased evolution close principles.**

### Common Mistakes in Interviews

- Define phased evolution close with buzzwords only
- No concrete Azure/.NET example
- Cannot link concept to measurable outcome

---
