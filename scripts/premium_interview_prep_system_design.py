"""Premium System Design Top 50 — Part 2 (Q009–Q030) and Part 3 (Q031–Q050)."""


def q(title, category, frequency, question, short, detailed, perspective, fu1, fu2, m1, m2, m3):
    return dict(
        title=title,
        category=category,
        frequency=frequency,
        question=question,
        short=short,
        detailed=detailed,
        perspective=perspective,
        followups=f"1. **{fu1}**\n2. **{fu2}**",
        mistakes=f"- {m1}\n- {m2}\n- {m3}",
    )


SYSTEM_DESIGN_PART2_Q009_Q030 = [
    q(
        "URL Shortener Design",
        "Classic Design",
        "Very Common",
        "Design bit.ly for 100M URLs, 10K writes/sec, 100K reads/sec. Redirect latency p99 < 50ms.",
        "Base62 short code from distributed ID generator; authoritative store (SQL/NoSQL) + Redis cache for hot URLs; 301 redirect; async analytics via queue. Read-heavy — cache-aside dominates.",
        """**Requirements clarification:**
| Type | Detail |
|------|--------|
| Functional | Create short URL, redirect, optional custom alias, analytics |
| NFR | 100:1 read/write, p99 redirect < 50ms, 7-year retention |

**Estimation:** 100K read QPS peak ≈ 3× avg ≈ 33K avg. 10K write QPS. Storage: 100M × 500B ≈ 50GB + indexes.

**High-level design:**
```mermaid
flowchart LR
  Client --> LB --> API
  API --> Redis[(Redis cache)]
  API --> DB[(URL store)]
  API --> Queue[Analytics queue]
  Queue --> DW[(Analytics DB)]
```

**Create flow:** Generate ID (Snowflake) → encode Base62 → write DB → return short URL.
**Redirect flow:** Cache-aside: Redis GET → miss → DB lookup → populate cache → 301.

**Key decisions:**
| Decision | Choice | Why |
|----------|--------|-----|
| ID generation | Snowflake / DB sequence | Avoid collision at 10K writes/sec |
| Cache | Redis cluster | Sub-ms reads, TTL on cold URLs |
| Redirect | 301 permanent | SEO + browser cache |
| Analytics | Async queue | Don't block redirect path |

**Deep dive — cache:** 80/20 rule — 20% URLs get 80% hits. LRU eviction; bloom filter optional for "definitely not exists" before DB.""",
        "Interviewers expect RESHADED flow: numbers first, then read path optimization. Redirect is the money path.",
        "Custom vanity URLs with collision handling? — Reserve in DB with unique constraint; 409 on conflict.",
        "How handle expired URLs? — TTL column + lazy delete; 410 Gone response.",
        "Hash long URL instead of ID — collision risk at scale",
        "No cache on read-heavy workload",
        "302 instead of 301 without explaining trade-off",
    ),
    q(
        "Rate Limiter Design",
        "Infrastructure",
        "Very Common",
        "Design a distributed rate limiter: 1000 requests/minute per user globally across 50 API servers.",
        "Token bucket or sliding window counter in Redis keyed by userId; atomic INCR + EXPIRE or Lua script; return 429 with Retry-After header; optional local cache for coarse pre-check.",
        """**Algorithm comparison:**
| Algorithm | Pros | Cons |
|-----------|------|------|
| Fixed window | Simple | Burst at window boundary |
| Sliding window log | Accurate | Memory per request |
| Token bucket | Smooth burst allowance | Slightly complex |
| Sliding window counter | Good balance | Redis Lua script |

**Architecture:**
```mermaid
flowchart LR
  Client --> LB --> API1[API server]
  API1 --> Redis[(Redis cluster)]
  API1 -->|429| Client
```

**Redis sliding window (Lua):**
```
KEY = rate:{userId}:{window}
INCR → if count > limit → reject
EXPIRE window key
```

**Distributed concerns:**
- **Centralized Redis** — single source of truth; ~100K ops/sec per shard
- **Local token cache** — reduce Redis calls; accept slight over-admission
- **Per-IP fallback** — when userId unknown

**Headers:** `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `Retry-After`.

**Placement:** API gateway (Kong, APIM) for coarse limits; app-level for business rules (free vs paid tier).""",
        "Architects distinguish edge rate limiting (DDoS) from application quotas (billing tiers).",
        "Rate limit per API key vs IP vs user? — Layer all three; API key for B2B, IP for anonymous.",
        "Multi-region rate limiting without global Redis? — Regional buckets + sync delay; or CRDT counters.",
        "In-memory only on each server — 50× over-admission",
        "No Retry-After header on 429",
        "Fixed window without mentioning boundary burst",
    ),
    q(
        "Chat System Design",
        "Real-Time Messaging",
        "Very Common",
        "Design WhatsApp-scale messaging: 500M DAU, 1:1 and group chat, delivery receipts, offline delivery.",
        "WebSocket gateway for online users; message service writes to partition by conversationId; inbox/outbox per user in Cassandra; push notification for offline; sequence numbers for ordering; at-least-once with client dedup.",
        """**Components:**
| Component | Role |
|-----------|------|
| Connection service | WebSocket long-lived connections, heartbeats |
| Message service | Persist, route, fan-out to recipients |
| Presence service | Online/offline status (Redis) |
| Push service | APNs/FCM for offline |
| Media service | Blob storage for attachments |

```mermaid
flowchart TB
  A[User A WS] --> GW[Gateway]
  GW --> MS[Message Service]
  MS --> MQ[Partition queue]
  MS --> DB[(Message store)]
  MS --> GW
  GW --> B[User B WS]
  MS --> Push[Push service]
```

**Message flow:** Client sends → gateway → message service → persist (conversationId partition) → push to recipient gateway OR enqueue for offline sync.

**Group chat:** Fan-out to N members on write; or pull on read for large groups (500+).

**Ordering:** Per-conversation sequence ID (Snowflake or local counter). Client displays by sequence; handles gaps with sync API.

**Delivery states:** Sent → Delivered → Read (separate lightweight ACK channel).""",
        "Scale hinges on connection management (millions of WebSockets) and partition strategy (conversationId, not userId).",
        "End-to-end encryption impact? — Server can't read content; key exchange out of band; affects search/ moderation.",
        "Group with 10K members? — Pull model on read; don't push to 10K sockets synchronously.",
        "Polling instead of WebSocket at scale",
        "No offline message queue",
        "Global ordering across all chats — unnecessary bottleneck",
    ),
    q(
        "News Feed Fan-Out",
        "Social Feed",
        "Very Common",
        "Design Twitter/X home timeline. 300M users, celebrities with 50M followers. Fan-out on write vs read?",
        "Hybrid: fan-out on write for normal users (<10K followers); fan-out on read for celebrities; merge timelines at read with cache; rank/score in separate service.",
        """**The fork:**
| Strategy | Write cost | Read cost | Best for |
|----------|------------|-----------|----------|
| Fan-out on write | O(followers) | O(1) | Normal users |
| Fan-out on read | O(1) | O(following) | Celebrities |
| Hybrid | Mixed | Mixed | Production Twitter |

**Fan-out on write:**
Post created → for each follower, push postId to their timeline cache (Redis sorted set by timestamp).

**Celebrity problem:** Lady Gaga posts → 50M Redis writes synchronously = minutes. **Solution:** Mark celebrity; followers pull celebrity posts at read time and merge.

```mermaid
flowchart LR
  Post --> FO[Fan-out worker]
  FO -->|normal user| TL1[Follower timelines]
  Post --> Celeb[Celeb index]
  Read --> Merge[Merge service]
  TL1 --> Merge
  Celeb --> Merge
```

**Storage:** Post table (postId, userId, content, ts). Timeline = sorted set of postIds per userId.

**Ranking:** Separate feed ranker (ML) may reorder cached candidates — don't block write path.""",
        "This is THE social feed interview question — hybrid approach shows production awareness.",
        "How regenerate timeline after unfollow? — Remove postIds from cached timeline; lazy cleanup OK.",
        "Feed ranking vs chronological? — Precompute candidate set; rank at read with cached features.",
        "Pure fan-out on write for all users",
        "No celebrity exception path",
        "Cross-shard timeline JOIN at read time",
    ),
    q(
        "Sharding Strategy",
        "Database Scale",
        "Very Common",
        "Shard a users table with 1B rows, 50K QPS. Choose sharding key and strategy.",
        "Hash(userId) mod N for even distribution; avoid cross-shard JOINs by co-locating related data; consistent hashing for resharding; shard map service for routing.",
        """**Sharding key selection:**
| Key | Pros | Cons |
|-----|------|------|
| userId hash | Even spread | Can't range query by region |
| tenantId | Multi-tenant isolation | Hot tenant problem |
| geo | Data residency | Uneven distribution |

**Architecture:**
```mermaid
flowchart TB
  App --> Router[Shard router]
  Router --> S1[(Shard 1)]
  Router --> S2[(Shard 2)]
  Router --> SN[(Shard N)]
```

**Rules:**
1. **Co-locate** user + user's orders on same shard (same hash key)
2. **Avoid cross-shard transactions** — use saga or denormalize
3. **Global secondary indexes** — async replication to search index (Elasticsearch)
4. **Resharding** — consistent hashing minimizes key movement; dual-write migration window

**Hot shard mitigation:** Split hot key range; add read replicas; cache layer above hot shard.

**Capacity:** 1B rows / 16 shards = 62M rows/shard — manageable with proper indexes.""",
        "Interviewers want sharding key justification tied to access patterns, not just 'hash the ID'.",
        "When shard by geography? — GDPR/data residency; accept uneven load with overflow shards.",
        "Cross-shard pagination? — Cursor on global index (ES) not SQL OFFSET.",
        "Range shard on auto-increment ID — hot last shard",
        "Cross-shard JOIN in OLTP path",
        "No plan for resharding as data grows",
    ),
    q(
        "Consistent Hashing",
        "Distributed Systems",
        "Very Common",
        "Explain consistent hashing and why distributed caches use it. What happens when a node is added?",
        "Keys and nodes mapped to a hash ring; key assigned to first node clockwise; virtual nodes (vnodes) for even distribution; adding node moves only ~K/n keys (not all keys).",
        """**Problem:** Simple hash(key) mod N — when N changes, nearly all keys remap → cache stampede.

**Consistent hashing:** Ring 0 to 2^32-1; nodes placed on ring (with 100-200 vnodes each); key → clockwise nearest node.

```mermaid
flowchart LR
  subgraph ring [Hash Ring]
    N1((Node A))
    N2((Node B))
    N3((Node C))
    K1[Key K1]
  end
  K1 --> N2
```

**Node add/remove:** Only keys between predecessor and new node migrate.

| Event | Keys affected |
|-------|---------------|
| Add 1 node to 10 | ~10% of keys |
| mod N change | ~100% of keys |

**Production:** Dynamo, Cassandra, Redis Cluster, memcached clients all use variants.

**Replication:** Walk clockwise for replica nodes (N+1, N+2 on ring).

**Hot key:** Doesn't solve hot keys — need local cache or key splitting.""",
        "Connects directly to cache cluster elasticity — architects specify vnode count and replication factor.",
        "Consistent hashing vs rendezvous hashing? — Rendezvous (HRW) better for small clusters; consistent hash for large.",
        "How handle node failure? — Replica promotion; temporary over-replication on neighbors.",
        "Think mod N is fine at scale",
        "No virtual nodes — uneven distribution",
        "Forget replication walk on ring",
    ),
    q(
        "Distributed Cache Design",
        "Caching",
        "Very Common",
        "Design a distributed cache layer for 1M QPS, 10TB working set, 99.9% availability.",
        "Redis Cluster or Memcached with consistent hashing; cache-aside pattern; TTL + LRU eviction; local L1 cache optional; replication for HA; separate hot-key handling.",
        """**Tiered cache:**
```mermaid
flowchart LR
  App --> L1[Local L1 ~1ms]
  L1 --> L2[Redis Cluster ~2ms]
  L2 --> DB[(Database ~20ms)]
```

**Redis Cluster:** 16384 hash slots; min 3 masters; replica per master for failover.

| Pattern | Use when |
|---------|----------|
| Cache-aside | General read-heavy (most common) |
| Write-through | Strong consistency needed |
| Write-behind | Write-heavy, tolerate loss window |

**Eviction:** allkeys-lru for pure cache; volatile-lru if mixed TTL keys.

**Hot key:** Local JVM cache; read replicas; key splitting (`user:123 → user:123:0..9`).

**Invalidation:** Pub/sub channel; or version stamp in key; avoid flush-all.

**Monitoring:** Hit ratio >95% target; p99 latency; memory usage per shard.""",
        "Architects specify cache pattern, eviction, and invalidation strategy — not just 'add Redis'.",
        "Redis vs Memcached? — Redis: structures, persistence, cluster; Memcached: simpler, multithreaded, pure KV.",
        "Cache stampede prevention? — Mutex, early expiration jitter, request coalescing.",
        "No TTL — unbounded memory growth",
        "Cache-aside without invalidation on write",
        "Single Redis instance for 1M QPS",
    ),
    q(
        "Notification System Design",
        "Async Messaging",
        "Common",
        "Design a notification system supporting email, SMS, and push for 10M users. 1M notifications/hour peak.",
        "Event bus ingests triggers → router picks channel(s) → priority queues per channel → worker pools → template service → provider adapters (SendGrid, Twilio, FCM); retry + DLQ; user preference store.",
        """**Flow:**
```mermaid
flowchart LR
  Event[Domain event] --> Bus[Event bus]
  Bus --> Router[Channel router]
  Router --> EQ[Email queue]
  Router --> SQ[SMS queue]
  Router --> PQ[Push queue]
  EQ --> EW[Email workers]
  SQ --> SW[SMS workers]
  PQ --> PW[Push workers]
```

**Components:**
| Component | Purpose |
|-----------|---------|
| Preference service | User opt-in/out per channel and category |
| Template service | Render with variables; i18n |
| Idempotency store | Dedup by (userId, eventId, channel) |
| Rate limiter | Per-user caps (max 10 push/day) |

**Priority:** OTP/security > transactional > marketing. Separate queues prevent marketing backlog blocking OTP.

**Failure:** Exponential backoff retry (3×); DLQ for manual replay; dead letter alerting.

**Scale:** ~280 notif/sec peak — modest; bottleneck is provider API limits, not internal throughput.""",
        "Strategy pattern for providers; priority queues show you won't let marketing email block password reset.",
        "Digest vs real-time? — Batch queue with scheduled worker for daily digest.",
        "Multi-tenant template isolation? — Namespace templates by tenantId; RBAC on edit.",
        "Synchronous send in request path",
        "No user preference checks (CAN-SPAM/GDPR)",
        "Single queue for all channels and priorities",
    ),
    q(
        "Paste Bin Design",
        "Classic Design",
        "Common",
        "Design Pastebin: create text paste, optional expiry, read by URL. 10M pastes/month, 100:1 read/write.",
        "Short key (Base62 ID); blob storage for content (S3/Azure Blob); metadata in SQL (id, created, expiry, size); CDN for popular pastes; scan queue for abuse/malware.",
        """**Create:** Validate size (<1MB) → store blob → insert metadata → return URL.
**Read:** Lookup metadata → if expired 410 → fetch blob → return with syntax highlighting (client-side).

| Storage | Content |
|---------|---------|
| SQL/NoSQL | id, userId?, createdAt, expiresAt, blobKey, viewCount |
| Object store | Actual paste text |

**Expiry:** Lazy delete on read + nightly sweeper job for cleanup.

**Custom URLs:** Unique constraint on vanity slug; premium feature.

**Abuse:** Rate limit creates; virus scan async; report/block workflow.

**Scale:** 10M/month ≈ 4 creates/sec avg; reads 400/sec — CDN caches hot pastes by URL.""",
        "Read-heavy blob + metadata split is a recurring pattern (also applies to attachments, exports).",
        "Syntax highlighting server vs client? — Client (highlight.js) saves CPU; server for API consumers.",
        "Private pastes with auth? — Signed URLs with TTL; or require login + ACL table.",
        "Store large pastes in SQL BLOB",
        "No expiry mechanism",
        "Skip abuse scanning on user-generated content",
    ),
    q(
        "Search Autocomplete",
        "Search",
        "Common",
        "Design typeahead/autocomplete for Amazon-scale search. p99 < 100ms, top 10 suggestions.",
        "Trie or prefix index in memory/Redis; popular queries precomputed; FST (finite state transducer) for compact storage; client debounce 150ms; optional personalization layer.",
        """**Data pipeline:** Search logs → aggregate query prefixes → rank by frequency/recency/revenue → publish to serving tier hourly.

**Serving architecture:**
```mermaid
flowchart LR
  Client -->|debounced| API[Autocomplete API]
  API --> Trie[(Prefix index)]
  API --> Rank[Ranking service]
```

| Approach | Latency | Storage |
|----------|---------|---------|
| In-memory trie | <1ms | Large for full catalog |
| Redis ZSET per prefix | ~2ms | `prefix:appl → [(apple, score)]` |
| Elasticsearch completion | ~10ms | Easier ops, higher latency |

**Ranking signals:** Query frequency, click-through rate, inventory, margin (e-commerce).

**Personalization:** Blend global top-10 with user's recent searches (separate micro-index).

**Guardrails:** Blocklist offensive prefixes; minimum 2 chars before query.""",
        "Autocomplete is a prefix query problem — trie/FST is the DS interviewers expect tied to latency SLA.",
        "Update frequency for trending queries? — Stream aggregate (Flink) + publish every 5 min for viral terms.",
        "Multi-language autocomplete? — Separate index per locale; detect language from keyboard/input.",
        "Full table scan LIKE 'prefix%' on SQL",
        "No debounce — DDoS your own API",
        "Return unranked alphabetical results",
    ),
    q(
        "Video Streaming Platform",
        "Media",
        "Common",
        "Design YouTube-style video upload and playback for 1B users. Upload 500K videos/day, stream 1M concurrent.",
        "Chunked upload to blob storage → transcode queue (multiple bitrates) → HLS/DASH segments on CDN → metadata DB → recommendation separate; adaptive bitrate on client.",
        """**Upload pipeline:**
```mermaid
flowchart LR
  Upload[Chunked upload] --> Blob[(Raw blob)]
  Blob --> Trans[Transcode farm]
  Trans --> CDN[CDN segments]
  Trans --> Meta[(Video metadata)]
```

**Playback:** Client requests manifest (.m3u8) → CDN serves segments → player switches bitrate based on bandwidth.

| Component | Technology pattern |
|-----------|-------------------|
| Upload | Multipart resumable (tus protocol) |
| Transcode | FFmpeg workers on spot instances |
| Storage | S3 + CloudFront / Azure Blob + CDN |
| Metadata | SQL (title, owner, status, renditions) |

**Scale:** 1M concurrent × 2Mbps avg = 2Tbps CDN — must use edge; origin only on cache miss.

**Live vs VOD:** Live uses RTMP ingest → packager → low-latency HLS (LL-HLS).""",
        "Separate upload (write-heavy batch) from playback (CDN read) — different scaling profiles.",
        "Copyright detection? — Content ID fingerprinting async after upload; block before publish if match.",
        "Transcode priority for premium creators? — Priority queue tiers; SLA per subscription.",
        "Serve video from origin server directly",
        "Single bitrate for all clients",
        "Synchronous transcode blocking upload response",
    ),
    q(
        "Ticket Booking System",
        "Concurrency",
        "Very Common",
        "Design Ticketmaster: 50K seats, prevent double booking, handle 100K concurrent users at on-sale.",
        "Virtual waiting room → queue token → seat map in Redis with atomic hold (SETNX/HSET); 10-min TTL hold; payment confirms booking; optimistic locking fallback in DB.",
        """**On-sale flow:**
```mermaid
flowchart TB
  Users --> WR[Waiting room]
  WR --> Q[Fair queue]
  Q --> BS[Booking service]
  BS --> Redis[(Seat locks)]
  BS --> Pay[Payment]
  Pay --> DB[(Confirmed orders)]
```

**Seat locking:**
```
HSET event:123:seats A12 locked userId:456 TTL:600
```
Atomic check-and-set prevents double book.

| Strategy | When |
|----------|------|
| Pessimistic lock (Redis) | High contention on-sale |
| Optimistic (version column) | Low contention |
| DB row lock | Small venues only |

**Waiting room:** Token bucket admission; random shuffle for fairness; static "queue position" page.

**Failure:** Hold expires → seat returns to pool; websocket/poll for seat map updates.

**Bot prevention:** CAPTCHA at queue entry; device fingerprint; rate limits.""",
        "Concurrency control is the core — show atomic operations, TTL holds, and queue fairness.",
        "Best available vs pick-your-seat? — Best available: simpler lock on count; pick-seat: 2D seat map locks.",
        "Resale marketplace integration? — Transfer ownership atomically; void original barcode.",
        "Check-then-set race condition without atomic ops",
        "No hold TTL — seats locked forever",
        "Direct DB row lock for 100K concurrent users",
    ),
    q(
        "Web Crawler Design",
        "Distributed Systems",
        "Common",
        "Design a web crawler to index 1B pages, politeness (robots.txt), deduplication, 100 pages/sec sustained.",
        "URL frontier queue → fetcher workers → parser → link extractor → bloom filter + URL store for dedup; respect robots.txt cache; priority by PageRank/recency; blob store for raw HTML.",
        """**Architecture:**
```mermaid
flowchart LR
  Frontier[URL frontier] --> Fetch[Fetcher pool]
  Fetch --> Parse[Parser]
  Parse --> Extract[Link extractor]
  Extract --> Bloom[Bloom filter]
  Bloom --> Frontier
  Parse --> Store[(Content store)]
```

**Politeness:** Per-host queue; min 1 sec between requests to same domain; robots.txt cached 24h.

**Dedup:** Bloom filter (might exist) → exact URL hash in DB (definitely exists).

**Priority frontier:** High PageRank, fresh content, sitemap URLs first.

**Challenges:**
| Challenge | Solution |
|-----------|----------|
| Duplicate content | Content hash dedup |
| Spider traps | Max depth per domain |
| Dynamic JS pages | Headless browser pool (expensive) |

**Scale:** 100 pages/sec = 8.6M/day; 1B pages ≈ 116 days single cluster — horizontal fetchers.""",
        "Shows distributed systems thinking: frontier queue, politeness, probabilistic dedup.",
        "How detect content change for re-crawl? — Last-Modified/ETag headers; content hash comparison.",
        "Distributed crawler coordination? — Partition frontier by URL hash; shared bloom via Redis.",
        "Ignore robots.txt",
        "Unbounded frontier memory",
        "Fetch all URLs without per-host rate limit",
    ),
    q(
        "Distributed ID Generation",
        "Infrastructure",
        "Very Common",
        "Design a globally unique ID generator for a distributed system. 10K IDs/sec, sortable by time, no coordination per ID.",
        "Snowflake-style: timestamp (41b) + datacenter (5b) + worker (5b) + sequence (12b) = 64-bit sortable ID; or UUID v7 for standard sortable UUID; avoid DB auto-increment at scale.",
        """**Requirements:**
| Requirement | Solution |
|-------------|----------|
| Unique | Machine ID + sequence |
| Sortable | Leading timestamp bits |
| High throughput | Local generation, no DB round-trip |
| Clock skew | Wait or use logical clock |

**Snowflake layout:**
```
| 41 bit timestamp | 5 bit DC | 5 bit worker | 12 bit sequence |
```

**Alternatives:**
| Approach | Pros | Cons |
|----------|------|------|
| DB sequence | Simple | Single point, latency |
| UUID v4 | No coordination | Not sortable |
| UUID v7 | Sortable, standard | 128-bit |
| Snowflake | Compact, fast | Custom, clock dependency |

**Deployment:** One generator per machine; register workerId in ZooKeeper/etcd; NTP sync critical.""",
        "Every sharded system needs this — interviewers connect IDs to URL shorteners, order numbers, tweets.",
        "ID exhaustion at sequence overflow? — Wait 1ms for next timestamp window; 4096/ms per machine.",
        "Multi-region ID generation? — Embed region in datacenter bits; still no cross-region coordination.",
        "DB auto-increment for 10K/sec global writes",
        "UUID v4 for time-ordered feeds",
        "Ignore clock skew handling",
    ),
    q(
        "Snowflake ID Deep Dive",
        "Infrastructure",
        "Common",
        "Explain Twitter Snowflake ID structure. What breaks if system clock moves backward?",
        "64-bit: timestamp + machine ID + sequence; IDs sortable by creation time; clock backward → duplicate risk — wait until caught up or use reserved sequence bits; NTP discipline required.",
        """**Bit allocation (Twitter original):**
- 41 bits: milliseconds since epoch (~69 years)
- 10 bits: machine ID (1024 machines)
- 12 bits: sequence (4096 IDs/ms per machine)

**Generation algorithm:**
```
1. Get current timestamp T
2. If T == last_T: increment sequence (overflow → wait next ms)
3. If T < last_T: clock moved backward → error or wait
4. If T > last_T: reset sequence to 0
5. Compose ID = (T << 22) | (machine << 12) | sequence
```

**Clock backward handling:**
| Strategy | Trade-off |
|----------|-----------|
| Throw exception | Safe, brief unavailability |
| Wait until caught up | Simple, adds latency |
| Use reserved bit | Complex, rare |

**vs UUID v7:** Snowflake is 64-bit (fits JS Number with caution); UUID v7 is standard, 128-bit, interops better across systems.

**Monitoring:** Alert on clock skew >5ms; sequence overflow rate.""",
        "Deep dive follow-on to distributed IDs — shows you understand operational failure modes.",
        "JavaScript Number precision for Snowflake? — Use string or BigInt; IDs > 2^53 lose precision.",
        "Snowflake vs DB UUID primary key index performance? — Both B-tree friendly when sortable; UUID v4 causes page splits.",
        "No clock skew handling plan",
        "Same worker ID on two machines",
        "Assume NTP never fails",
    ),
    q(
        "API Design for System Design",
        "API Design",
        "Very Common",
        "Design REST APIs for a social media platform. Posts, feeds, follows. Discuss pagination, versioning, idempotency.",
        "Resource-oriented URLs; cursor pagination; idempotency keys on POST; versioning via URL prefix or header; rate limit headers; ProblemDetails errors (RFC 7807).",
        """**Core endpoints:**
```
POST   /v1/posts              (Idempotency-Key header)
GET    /v1/feed?cursor=abc&limit=20
POST   /v1/users/{id}/follow
DELETE /v1/users/{id}/follow
GET    /v1/posts/{id}
```

**Pagination:**
| Type | Use |
|------|-----|
| Cursor | Feeds, real-time data (stable) |
| Offset | Admin, small datasets only |

**Idempotency:** Store `(key, request_hash, response)` 24h; replay same response on retry.

**Versioning:** `/v1/` prefix; sunset policy 12 months; breaking change = v2.

```mermaid
flowchart LR
  Client --> GW[API Gateway]
  GW --> Auth[Auth]
  GW --> RL[Rate limit]
  GW --> Svc[Services]
```

**HATEOAS:** Optional for public API; skip in mobile-first internal APIs.""",
        "System design interviews increasingly include API surface — show REST maturity beyond CRUD.",
        "GraphQL vs REST for mobile feed? — GraphQL reduces round trips; REST + BFF simpler at scale.",
        "Webhook design for third parties? — HMAC signature, retry backoff, idempotent receiver docs.",
        "Offset pagination on infinite feed",
        "POST without idempotency for payments/orders",
        "No API versioning strategy",
    ),
    q(
        "Multi-Tenant SaaS Architecture",
        "SaaS",
        "Common",
        "Design data isolation for a multi-tenant B2B SaaS with 10K tenants, enterprise customers needing isolation.",
        "Bridge model: pooled DB with tenant_id + RLS default; silo (DB per tenant) for enterprise; shared app tier; tenant context in every query; feature flags per tier.",
        """**Isolation models:**
| Model | Isolation | Cost | Use |
|-------|-----------|------|-----|
| Pool | Row-level (tenant_id) | Lowest | SMB tenants |
| Silo | Database per tenant | Highest | Enterprise/regulated |
| Bridge | Pool default, silo premium | Balanced | Most SaaS |

**Implementation:**
```sql
-- Every table
CREATE TABLE orders (
  id BIGINT,
  tenant_id UUID NOT NULL,
  ...
);
-- RLS policy
CREATE POLICY tenant_isolation ON orders
  USING (tenant_id = current_setting('app.tenant_id')::uuid);
```

**Tenant routing:** Subdomain or JWT claim → set `app.tenant_id` on connection.

**Noisy neighbor:** Per-tenant rate limits; query cost caps; separate silo for heavy tenants.

**Compliance:** Data residency → silo in specific region; backup per tenant for enterprise.""",
        "Bridge model is the architect answer — pool for scale, silo for contract requirements.",
        "Tenant provisioning automation? — Terraform per silo; schema migration fleet-wide with Flyway.",
        "Cross-tenant analytics? — ETL to warehouse with tenant dimension; never query across RLS in OLTP.",
        "Separate schema per tenant without migration strategy",
        "Missing tenant_id on some tables",
        "Hard-code tenant in application code",
    ),
    q(
        "Search System Design",
        "Search",
        "Common",
        "Design full-text search for an e-commerce catalog: 100M products, faceted filters, p99 < 200ms.",
        "Elasticsearch/OpenSearch cluster; inverted index; write via CDC from OLTP; faceted aggregations; query understanding layer; cache popular queries; spell correction via separate index.",
        """**Index pipeline:**
```mermaid
flowchart LR
  OLTP[(Product DB)] --> CDC[CDC/Debezium]
  CDC --> ES[(Search cluster)]
  API[Search API] --> ES
  API --> Cache[(Query cache)]
```

**Document structure:**
```json
{
  "productId": "123",
  "title": "Apple iPhone",
  "category": "Electronics",
  "price": 999,
  "attributes": {"color": "black"}
}
```

**Facets:** ES aggregations on category, brand, price ranges — parallel to hit query.

| Component | Role |
|-----------|------|
| Analyzer | Tokenization, stemming |
| Synonym filter | "laptop" = "notebook" |
| Suggest | Completion suggester for typos |

**Ranking:** BM25 default + business boosts (margin, stock, sponsored).

**Freshness:** Near-real-time ES refresh (1s) or pull from cache for price/stock overlay.""",
        "Search is inverted index + pipeline — don't query OLTP for full-text at 100M rows.",
        "Personalized search ranking? — Blend BM25 with user embedding; separate ranking service.",
        "Search index rebuild without downtime? — Blue-green index alias swap.",
        "SQL LIKE for catalog search",
        "Synchronous index on write path",
        "No spell correction or synonym handling",
    ),
    q(
        "CDN Architecture",
        "Edge",
        "Common",
        "Design CDN strategy for global media and API acceleration. 10Tbps peak, 50ms latency worldwide.",
        "Multi-CDN or single provider with PoPs; cache static assets aggressively; signed URLs for private content; edge compute for A/B and auth; origin shield; cache key design for API.",
        """**What belongs on CDN:**
| Content | Cache | TTL |
|---------|-------|-----|
| Static JS/CSS/images | Yes | 1 year (hash in filename) |
| Video segments | Yes | Hours-days |
| Public API GET | Maybe | Short, cache-key by params |
| Personalized JSON | No* | *Unless edge compute |

```mermaid
flowchart LR
  User --> Edge[CDN PoP]
  Edge -->|miss| Shield[Origin shield]
  Shield --> Origin[Origin]
```

**Cache key design:** Include only relevant query params; strip session tokens.

**Invalidation:** Purge API on deploy; versioned asset URLs preferred over purge.

**Private content:** Signed cookies or URL tokens (CloudFront signed URLs).

**Origin shield:** Collapse miss storms — one request to origin per PoP region.""",
        "CDN is cost and latency optimization — architects know what NOT to cache.",
        "Multi-CDN failover? — DNS traffic management; health checks; higher ops complexity.",
        "Edge compute (Workers/Lambda@Edge)? — Auth at edge, geo routing, HTML personalization.",
        "Cache authenticated API responses without Vary header",
        "Same cache key for all users on personalized content",
        "No origin shield — thundering herd on deploy",
    ),
    q(
        "Load Balancer Architecture",
        "Networking",
        "Very Common",
        "Design load balancing for 500K RPS HTTP API globally. L4 vs L7, health checks, session affinity.",
        "L7 ALB/API Gateway at edge for path routing, TLS, WAF; L4 NLB for TCP/extreme throughput; round-robin + least connections; health checks every 30s; sticky sessions only when required.",
        """**Layer comparison:**
| Layer | Routes on | Use case |
|-------|-----------|----------|
| L4 | IP + port | Gaming, MQTT, NLB passthrough |
| L7 | HTTP path/header | Microservices, TLS termination |

**Global:**
```mermaid
flowchart TB
  DNS[Geo DNS / Anycast]
  DNS --> LB1[Regional LB]
  LB1 --> AZ1[AZ-a instances]
  LB1 --> AZ2[AZ-b instances]
```

**Algorithms:**
| Algorithm | Best for |
|-----------|----------|
| Round robin | Equal capacity servers |
| Least connections | Long-lived requests |
| Weighted | Heterogeneous instance sizes |
| Consistent hash | Cache affinity |

**Health checks:** `/health` returning 200; drain connections before deregister (connection draining).

**Avoid sticky sessions** when possible — use shared Redis session store instead.""",
        "Load balancer choice is early in every design — L7 default for HTTP microservices.",
        "Active-active multi-region LB? — Global accelerator + regional LBs; session in global store.",
        "gRPC load balancing? — Client-side LB or L7 proxy with HTTP/2 awareness (Envoy).",
        "L7 LB for raw TCP binary protocol",
        "No health checks — route to dead instances",
        "Sticky sessions without failover plan",
    ),
    q(
        "Database Replication",
        "Data",
        "Very Common",
        "Design MySQL/PostgreSQL replication for 99.99% availability. RPO 1 min, RTO 5 min. Read scaling.",
        "Primary-replica async replication; read replicas for read scale; automatic failover (Patroni/Orchestrator); synchronous replica for zero RPO if required; connection router sends writes to primary.",
        """**Topology:**
```mermaid
flowchart LR
  AppW[Write app] --> Primary[(Primary)]
  Primary -->|async| R1[(Replica 1)]
  Primary -->|async| R2[(Replica 2)]
  AppR[Read app] --> R1
  AppR --> R2
```

| Mode | RPO | Throughput |
|------|-----|------------|
| Async | Seconds | Highest |
| Semi-sync | 1 replica ack | Medium |
| Sync | Zero | Lower (latency) |

**Failover:** Monitor primary heartbeat; promote replica with most recent LSN; update DNS/VIP; fence old primary.

**Read replica lag:** Monitor seconds_behind_master; route stale-sensitive reads to primary.

**Multi-region:** Cross-region async replication; higher lag; regional read replicas for local reads.""",
        "Replication underpins every HA discussion — know RPO/RTO trade-offs by replication mode.",
        "Split-brain after failover? — Quorum + fencing (STONITH); prefer brief unavailability over dual-write.",
        "Read your writes consistency? — Route same-user reads to primary or track replication LSN in session.",
        "Assume sync replication with no latency cost",
        "No replica lag monitoring",
        "Failover without fencing old primary",
    ),
    q(
        "Caching Layers Strategy",
        "Caching",
        "Very Common",
        "Design a multi-layer caching strategy for a read-heavy e-commerce site. Product catalog, sessions, cart.",
        "Browser → CDN → API gateway cache → app local cache → Redis cluster → DB; different TTL and invalidation per layer; cache-aside default; write-through for cart.",
        """**Layer responsibilities:**
| Layer | Content | TTL |
|-------|---------|-----|
| Browser | Static assets | Long (immutable hashes) |
| CDN | Product images, static API | Minutes-hours |
| Redis | Product details, sessions | Minutes |
| App L1 | Hot config, feature flags | Seconds |
| DB buffer pool | Rows | Managed |

```mermaid
flowchart TB
  B[Browser] --> CDN
  CDN --> GW[Gateway]
  GW --> App[App L1]
  App --> Redis
  Redis --> DB[(Database)]
```

**Invalidation cascade:** Product update → purge Redis → publish invalidation event → CDN purge API → version bump on static JSON.

**Cart:** Write-through to Redis; async persist to DB; session affinity optional with Redis backing.

**Metrics per layer:** Hit ratio, latency contribution, memory — tune TTL where miss rate spikes.""",
        "Layered cache shows holistic thinking — each tier has different consistency and TTL semantics.",
        "When skip a layer? — Small apps: browser + Redis + DB sufficient; don't over-engineer L1.",
        "Cache warming on deploy? — Preload hot keys; gradual traffic shift (canary).",
        "Same TTL for all data types",
        "Invalidate CDN without versioned URLs",
        "No monitoring of per-layer hit rates",
    ),
]

SYSTEM_DESIGN_PART3_Q031_Q050 = [
    q(
        "E-Commerce Checkout",
        "Full Scenario",
        "Very Common",
        "Design checkout for 5K orders/minute. Cart, inventory, payment, order creation. Handle partial failures.",
        "Cart in Redis → inventory reservation (TTL 15 min) → idempotent payment → order persist → saga with compensation (release inventory, refund) on failure; outbox for downstream events.",
        """**Saga flow:**
```mermaid
flowchart LR
  Cart --> Inv[Reserve inventory]
  Inv --> Pay[Payment]
  Pay --> Ord[Create order]
  Ord --> Event[Publish events]
  Pay -->|fail| Comp[Compensate: release inv]
```

| Step | Failure handling |
|------|------------------|
| Reserve inventory | Return 409 insufficient stock |
| Payment fail | Release reservation |
| Order create fail | Refund payment + release |

**Inventory:** `DECRBY sku:123 reserved` with check ≥0 atomic; or row lock in DB for low SKU count.

**Idempotency:** Client sends `Idempotency-Key`; server returns cached result on retry.

**Scale:** 5K/min ≈ 83/sec — moderate; peak 3× plan for flash sales with queue admission.

See also: [mock-05 checkout](mock-interviews/mock-05-system-design-checkout.md).""",
        "Checkout is the canonical saga interview — compensation paths matter more than happy path.",
        "Flash sale 10× traffic? — Queue + waiting room; oversell protection with atomic counters.",
        "Split shipment partial fulfillment? — Sub-orders; partial capture on payment.",
        "Two-phase commit across all services",
        "No inventory reservation TTL",
        "Payment retry without idempotency key",
    ),
    q(
        "Notification System (Full Design)",
        "Full Scenario",
        "Common",
        "Design enterprise notification platform: email, SMS, push, in-app, webhooks. 100M users, templates, analytics, compliance.",
        "Event ingestion → rules engine (who, what channel) → template render → provider abstraction → delivery tracking → analytics pipeline; CAN-SPAM/GDPR preference center; priority lanes.",
        """**Extended architecture:**
```mermaid
flowchart TB
  Events --> Rules[Rules engine]
  Rules --> Pref[Preference filter]
  Pref --> Tpl[Template service]
  Tpl --> Router[Channel router]
  Router --> P1[Provider adapters]
  P1 --> Track[Delivery tracker]
  Track --> Analytics[(Analytics)]
```

**Tracking states:** queued → sent → delivered → opened → clicked (email pixels/links).

**Compliance:** Opt-in audit log; unsubscribe one-click; regional SMS regulations (10DLC).

**Webhook outbound:** HMAC-SHA256 signature; retry 3× exponential; customer idempotency docs.

**Analytics:** Kafka → Flink aggregations → dashboard (delivery rate, latency by channel).

**Multi-tenant:** Template namespace; isolated provider API keys per tenant.""",
        "Full notification design adds compliance, analytics, and webhooks — beyond basic queue workers.",
        "In-app notification feed storage? — Per-user inbox table partitioned by userId; mark read API.",
        "A/B test notification copy? — Experiment flag in rules engine; track conversion per variant.",
        "No unsubscribe mechanism",
        "Same provider key for all tenants",
        "Blocking domain logic on SMS send completion",
    ),
    q(
        "Ride-Sharing Platform",
        "Full Scenario",
        "Very Common",
        "Design Uber/Lyft: real-time driver location, rider request, matching, ETA, surge pricing.",
        "Driver location stream (Kafka) → geospatial index (Redis GEO / QuadTree) → matching service (nearest available) → dispatch with timeout → ETA via routing graph → surge by supply/demand ratio.",
        """**Real-time location:**
```mermaid
flowchart LR
  Driver --> Loc[Location service]
  Loc --> Stream[Kafka]
  Stream --> Geo[Geo index]
  Rider --> Match[Matching]
  Geo --> Match
  Match --> Dispatch[Dispatch]
```

**Matching:** Query drivers within 2km radius → filter available → rank by distance, rating, acceptance rate → offer to top 3 sequentially with 15s timeout.

**ETA:** Precomputed road graph (OSRM/Google); cache frequent routes; update with live traffic feed.

**Surge:** `multiplier = f(demand/supply)` per geo cell (H3 hex grid); update every 2 min.

**Trip state machine:** requested → matched → arrived → in_progress → completed → payment.""",
        "Geospatial indexing + streaming location is the differentiator from generic CRUD designs.",
        "Driver going offline mid-match? — Heartbeat 30s; re-match rider on timeout.",
        "Pool/shared rides? — Match compatible routes; detour constraint in algorithm.",
        "Poll DB for driver locations",
        "Match without timeout — rider waits forever",
        "No surge isolation between adjacent cells",
    ),
    q(
        "Dropbox File Sync",
        "Full Scenario",
        "Common",
        "Design Dropbox: upload, sync across devices, conflict resolution, sharing, 500M users.",
        "Metadata DB (files, versions, ACLs) + blob storage (S3); content-defined chunking + hash dedup; delta sync (rsync-style); vector clock or version tree for conflicts; notification via long poll/WebSocket.",
        """**Sync protocol:**
```mermaid
flowchart TB
  Client --> Meta[Metadata service]
  Client --> Blob[(Blob store)]
  Meta --> DB[(Metadata DB)]
  Meta --> Notif[Change notifier]
```

**Chunking:** Split file 4MB blocks → SHA256 hash → upload only changed chunks (dedup saves storage).

**Conflict:** Last-write-wins for casual users; version branch for power users (save both copies).

**Sharing:** ACL table (fileId, userId, permission); signed download URLs.

**Scale:** Metadata hot path in SQL sharded by userId; blobs infinitely scalable on object store.

**Mobile:** Background sync queue; bandwidth-aware (WiFi only setting).""",
        "Content-hash chunking and dedup separates Dropbox from naive 'upload whole file' designs.",
        "End-to-end encryption (Zero Knowledge)? — Client-side encrypt; server stores ciphertext; no dedup across users.",
        "Large team shared folders? — Namespace permissions; activity log; quota per team.",
        "Upload entire file on every save",
        "No conflict detection — silent overwrite",
        "Metadata and blob on same SQL server",
    ),
    q(
        "Ticketmaster Scale Design",
        "Full Scenario",
        "Very Common",
        "Design high-demand concert on-sale: 500K users, 20K seats, zero double booking, fair queue.",
        "Virtual waiting room with random shuffle → admit N users/min → seat service with Redis atomic locks → payment window 10 min → anti-bot (CAPTCHA, device ID) → static seat map CDN with dynamic availability overlay.",
        """**Scale tactics:**
| Tactic | Purpose |
|--------|---------|
| Waiting room | Protect origin from 500K simultaneous |
| Queue tokens | Fair admission, prevent refresh advantage |
| Edge caching | Static venue map at CDN |
| WebSocket | Live seat availability updates |

**Architecture extension of Q020:**
- Pre-load seat map into Redis before on-sale
- Atomic Lua script: check available + lock + decrement in one op
- Idempotent booking token prevents double-submit

**Observability:** Queue depth, lock contention rate, payment conversion funnel.

**Post-sale:** Waitlist queue for cancelled holds backfill.""",
        "Combines concurrency (Q020) with traffic shaping — interviewers test both fairness and correctness.",
        "Dynamic pricing during queue? — Display price at lock time; honor locked price for TTL.",
        "Accessibility / verified fan programs? — Separate queue pool with identity verification.",
        "Allow refresh to skip queue",
        "Optimistic UI showing seat available without lock",
        "No bot mitigation on high-value on-sales",
    ),
    q(
        "Instagram Design",
        "Full Scenario",
        "Very Common",
        "Design Instagram: photo upload, feed, stories, likes, follow graph. 1B users, 100M DAU.",
        "Blob + CDN for media; metadata in Cassandra (posts by userId); feed via hybrid fan-out; stories TTL 24h separate store; likes sharded counter; social graph in separate service.",
        """**Media pipeline:** Upload → transcoding (thumbnails) → CDN → metadata write.

**Feed:** Hybrid fan-out (see Q012); rank by engagement score.

**Stories:** Separate Redis TTL store (24h expiry); ring buffer per user; viewed-by bitmap.

```mermaid
flowchart LR
  Upload --> Media[Media service]
  Media --> CDN
  Media --> Post[Post service]
  Post --> Feed[Feed fan-out]
  Follow[Graph service] --> Feed
```

**Likes:** Sharded Redis counter + async persist; approximate OK for display.

**Explore/discover:** ML ranker on candidate generation from graph + interests — offline batch + online serve.""",
        "Instagram bundles media CDN, social graph, and feed — hit each subsystem briefly then deep dive one.",
        "Comments threading at scale? — Partition by postId; paginate cursor; hot post comment cache.",
        "Direct messaging overlap? — Reuse chat architecture (Q011) with separate partition.",
        "Store images in database BLOB",
        "Fan-out on write for celebrity accounts",
        "No CDN for photo delivery",
    ),
    q(
        "Twitter/X Timeline",
        "Full Scenario",
        "Very Common",
        "Design home timeline and tweet posting. 400M users, 500M tweets/day, celebrity accounts.",
        "Tweet write → fan-out hybrid; timeline cache Redis sorted sets; tweet store sharded by tweetId; retweet/quote as reference not copy; search index async; trending via stream aggregation.",
        """**Post tweet:**
1. Persist tweet (userId, content, ts, tweetId)
2. Fan-out to followers (unless celebrity flag)
3. Update search index async

**Read timeline:**
1. Fetch precomputed timeline IDs from Redis
2. Merge celebrity tweets from pull cache
3. Hydrate tweet objects (batch mget)
4. Apply ranker (optional)

| Storage | Key pattern |
|---------|-------------|
| Tweet | tweet:{id} |
| User timeline | timeline:{userId} (sorted set) |
| Fan-out queue | Async workers for bulk push |

**Retweet:** Store pointer to original tweetId — avoid duplicate content.

**Trending:** Count hashtags in 5-min windows via Flink; locality per country.""",
        "Twitter timeline IS the fan-out question in product form — expect deep dive on celebrity hybrid.",
        "Quote tweet vs retweet storage? — Quote stores new tweet with embedded reference ID.",
        "Edit tweet (30 min window)? — Version chain; serve latest to timeline; audit old versions.",
        "Materialize full tweet in every follower timeline",
        "No async fan-out workers — block post request",
        "Global trending without sharded aggregation",
    ),
    q(
        "Uber ETA Service",
        "Full Scenario",
        "Common",
        "Design ETA prediction for ride-hailing: pickup ETA, trip duration, update every 30 seconds.",
        "Road graph database (OSRM/custom); ML model on historical trips (time of day, weather); live traffic ingestion; cache ETA(origin, dest, time_bucket); WebSocket push updates to client.",
        """**ETA pipeline:**
```mermaid
flowchart LR
  Req[ETA request] --> Cache[(ETA cache)]
  Cache -->|miss| Graph[Road graph]
  Graph --> ML[ML adjustment]
  ML --> Traffic[Live traffic]
  Traffic --> Resp[ETA response]
```

**Components:**
| Component | Role |
|-----------|------|
| Graph server | Shortest path baseline |
| ML model | Adjust for real-world vs theoretical |
| Traffic feed | Incidents, congestion |
| Geofence | Airport rules, one-way streets |

**Cache key:** `(origin_cell, dest_cell, hour_of_week)` — H3 hex ~500m resolution.

**Accuracy metric:** MAE < 2 min for pickup; monitor p95 error by city.

**Update loop:** Driver location stream recalculates en route every 30s.""",
        "ETA is graph + ML + streaming — show you know map data is precomputed not live Dijkstra every request.",
        "Multi-stop trip ETA? — Sum segments; reoptimize order for pool rides (TSP heuristic).",
        "Offline maps vs online? — Cache graph tiles regionally; fallback when connectivity poor.",
        "Straight-line distance for ETA",
        "No traffic data integration",
        "Recalculate full path every second per active trip",
    ),
    q(
        "Yelp / Local Search",
        "Full Scenario",
        "Common",
        "Design Yelp: business search, reviews, ratings, geo filters. 200M reviews, search by location + category.",
        "Geo-sharded index (Elasticsearch geo_point); reviews partitioned by businessId; rating aggregate cached; search + filter + sort by distance/rating; photo CDN separate.",
        """**Search query:** "Italian restaurants within 2km" → geo filter + text match + sort by rating/distance.

```mermaid
flowchart LR
  Query --> ES[(Elasticsearch)]
  ES --> Rank[Ranking]
  Rank --> Resp[Results + facets]
  Reviews[(Review store)] --> Rank
```

**Review write:** Insert review → async update business aggregate (count, avg rating) → invalidate cache.

**Ranking signals:** Wilson score (statistical rating), review count, distance, sponsored boost.

**Sharding:** Businesses geo-sharded or ES cluster handles geo natively.

**Abuse:** Review fraud detection ML; rate limit reviews per user per day.""",
        "Local search combines geo + full-text + aggregated ratings — three data patterns in one design.",
        "Business owner claims listing? — Verification workflow; separate admin API.",
        "Real-time busy hours (like Google)? — Anonymized visit stream; heatmap by hour.",
        "Calculate average rating on every search query",
        "Single global SQL table for geo search",
        "No review spam controls",
    ),
    q(
        "Distributed Lock",
        "Infrastructure",
        "Very Common",
        "Design a distributed lock service for coordinating jobs across 100 servers. Avoid split brain.",
        "Redis Redlock or etcd/ZooKeeper consensus lock; fencing token monotonic; TTL prevents deadlock; renew heartbeat for long jobs; prefer DB advisory lock only for low scale.",
        """**Redis single-instance lock (simple):**
```
SET lock:resource uuid NX EX 30
```
Release with Lua compare-and-del (only owner releases).

**Redlock:** Quorum across N independent Redis masters; controversial — know trade-offs.

**etcd/consensus (preferred for correctness):**
```mermaid
flowchart LR
  Worker --> etcd[(etcd)]
  etcd -->|lease + revision| Worker
```

**Fencing token:** Lock returns monotonic token; resource (DB) rejects writes with stale token — prevents delayed worker from corrupting data after lock lost.

| Approach | Correctness | Complexity |
|----------|-------------|------------|
| Redis SET NX | Good with fencing | Low |
| Redlock | Debated | Medium |
| etcd lease | Strong | Medium |

**Always set TTL** — prevent dead worker holding lock forever.""",
        "Distributed locks are easy to get wrong — fencing token separates senior answers.",
        "Lock vs leader election? — Leader election is long-held lock with watch notification on loss.",
        "Database advisory lock (pg_advisory_lock)? — OK single-DB low scale; not cross-service.",
        "Lock without TTL — deadlock on crash",
        "Release lock without verifying owner",
        "Redlock without mentioning Martin Kleppmann critique",
    ),
    q(
        "Metrics and Monitoring System",
        "Observability",
        "Common",
        "Design metrics collection for 10K microservices. 1M metrics/sec, dashboards, alerting.",
        "Prometheus pull or OTLP push → time-series DB (Prometheus/Cortex/Mimir) → Grafana dashboards; recording rules for aggregates; Alertmanager for routing; cardinality control.",
        """**Pipeline:**
```mermaid
flowchart LR
  Svc[Services] -->|OTLP| Coll[Collector]
  Coll --> TSDB[(Time-series DB)]
  TSDB --> Graf[Grafana]
  TSDB --> Alert[Alertmanager]
```

**Metric types:**
| Type | Example |
|------|---------|
| Counter | requests_total |
| Gauge | queue_depth |
| Histogram | request_duration_seconds |

**Cardinality explosion:** Avoid high-cardinality labels (userId); aggregate at scrape or recording rule.

**Retention:** 15 days hot → downsample → 1 year cold (Thanos/Cortex).

**SLI/SLO:** Error rate + latency histogram → burn rate alerts (multi-window).""",
        "Metrics design is increasingly asked — know pull vs push and cardinality limits.",
        "Logs vs metrics vs traces? — Metrics for aggregates; traces for request path; logs for details.",
        "Custom business metrics at checkout? — orders_completed_total counter with status label.",
        "userId as metric label — cardinality disaster",
        "No alerting on SLO burn rate",
        "Single Prometheus for 1M metrics/sec",
    ),
    q(
        "Logging Aggregation",
        "Observability",
        "Common",
        "Design centralized logging for 50TB/day across 5000 servers. Search, retention, cost control.",
        "Structured JSON logs → agent (Fluent Bit) → Kafka buffer → Elasticsearch/OpenSearch hot tier → S3 cold archive; index by service/environment; 30-day hot, 1-year cold.",
        """**Architecture:**
```mermaid
flowchart LR
  App --> Agent[Fluent Bit]
  Agent --> Kafka
  Kafka --> ES[(OpenSearch hot)]
  Kafka --> S3[(S3 archive)]
```

**Structured logging:**
```json
{"ts":"...","level":"ERROR","service":"payment","traceId":"abc","msg":"..."}
```

**Cost control:**
| Tier | Retention | Storage |
|------|-----------|---------|
| Hot | 7-30 days | SSD index |
| Warm | 90 days | Reduced replicas |
| Cold | 1+ year | S3 + Athena query |

**Sampling:** 100% ERROR; 1% DEBUG in prod; always keep audit/security logs.

**Correlation:** traceId links logs ↔ traces (Jaeger/Tempo).""",
        "Log volume at scale forces tiered retention — interviewers want cost-aware design.",
        "PII in logs? — Scrub at agent; field-level redaction; GDPR delete propagation.",
        "Log-based alerting vs metrics? — Metrics preferred for alerts; logs for investigation.",
        "Plain text unstructured logs at scale",
        "Infinite hot retention on SSD",
        "No trace correlation ID",
    ),
    q(
        "Configuration Service",
        "Infrastructure",
        "Common",
        "Design a dynamic configuration service for 500 microservices. Feature flags, gradual rollout, audit trail.",
        "Central config store (etcd/Consul/AppConfig) → watch/subscribe push to clients; versioned namespaces per env; feature flag with percentage rollout; audit log on change; cache locally with fallback.",
        """**Model:**
```mermaid
flowchart TB
  Admin[Config UI] --> Store[(Config store)]
  Store -->|watch| Svc1[Service A]
  Store -->|watch| Svc2[Service B]
```

| Feature | Implementation |
|---------|----------------|
| Versioning | Git-backed or revision numbers |
| Rollout | Flag: 5% → 25% → 100% by user hash |
| Rollback | Instant revert to previous revision |
| Secrets | Separate vault; never in config service |

**Client SDK:** Local cache + long poll/watch; stale cache OK for non-critical flags; fail-safe defaults.

**Examples:** LaunchDarkly, Azure App Configuration, Consul KV.""",
        "Config service enables safe deploys — connect to feature flags and blast radius reduction.",
        "Config change without restart? — Push watch updates; IOptionsMonitor pattern in .NET.",
        "Multi-region config consistency? — Eventually consistent OK; critical flags use consensus store.",
        "Config in code only — require redeploy for toggle",
        "Secrets in same store as feature flags",
        "No audit trail on production config changes",
    ),
    q(
        "Distributed Key-Value Store",
        "Storage",
        "Very Common",
        "Design Dynamo-style distributed KV store. Partitioning, replication, eventual consistency, conflict resolution.",
        "Consistent hash partitioning; N replicas (typically 3); quorum read/write (R+W>N); vector clocks for conflict detection; hinted handoff on temporary failure; anti-entropy repair (Merkle trees).",
        """**Dynamo principles:**
```mermaid
flowchart TB
  Client --> Coord[Coordinator]
  Coord --> N1[(Node 1)]
  Coord --> N2[(Node 2)]
  Coord --> N3[(Node 3)]
```

| Parameter | Typical |
|-----------|---------|
| N replicas | 3 |
| W write quorum | 2 |
| R read quorum | 2 |

**Conflict:** Vector clock detects concurrent writes → return all versions to client (last-write-wins or merge).

**Failure handling:**
- **Hinted handoff:** Temporarily store for down node
- **Read repair:** Fix stale replica on read
- **Merkle tree:** Compare checksums between replicas periodically

**Not ACID:** Eventually consistent; tuned for availability (AP in CAP).""",
        "Dynamo/paper questions test CAP understanding — quorum math is expected.",
        "Dynamo vs Cassandra? — Cassandra implements Dynamo model with CQL; know lineage.",
        "When strong consistency? — R+W > N with W=ALL — latency cost.",
        "Single replica — no durability",
        "Last-write-wins without vector clocks for concurrent writes",
        "Ignore hinted handoff on node failure",
    ),
    q(
        "Distributed Rate Limiter",
        "Infrastructure",
        "Common",
        "Design rate limiting across 20 API regions without single Redis bottleneck. 10M users, tiered limits.",
        "Global counter via Redis Cluster with local token bucket fallback; or regional budgets + async sync; GCRA algorithm; edge rate limit (CDN/API gateway) + regional enforcement.",
        """**Multi-region options:**
| Approach | Accuracy | Latency |
|----------|----------|---------|
| Global Redis Cluster | Exact | Cross-region RTT |
| Regional + sync | Approximate | Low local |
| Edge + regional | Coarse + fine | Lowest |

```mermaid
flowchart TB
  Edge[CDN edge limit] --> Regional[Regional Redis]
  Regional --> Global[Global sync optional]
```

**Tiered limits:**
| Tier | Limit |
|------|-------|
| Free | 100 req/min |
| Pro | 10K req/min |
| Enterprise | Custom contract |

**GCRA (Generic Cell Rate Algorithm):** Used in Envoy; smooth limiting with burst.

**Response:** 429 + Retry-After; distinguish burst vs sustained violation in headers.""",
        "Extends Q010 to multi-region — shows evolution from single Redis to hierarchical limiting.",
        "Rate limit distributed cron jobs? — Token per job type globally; leader election for scheduler.",
        "DDoS vs user rate limit? — Edge network (Cloudflare) for DDoS; app limit for quotas.",
        "Single global Redis at 10M users — latency and SPOF",
        "Exact global count without cross-region cost analysis",
        "Same limit for free and enterprise tiers",
    ),
    q(
        "Message Queue System Design",
        "Messaging",
        "Very Common",
        "Design a message queue like SQS/RabbitMQ. Ordering, durability, at-least-once delivery, DLQ.",
        "Partitioned log (Kafka-style) or broker queues; persist to disk before ack; consumer groups; visibility timeout (SQS); dead letter queue after N failures; idempotent consumers.",
        """**SQS-style semantics:**
```mermaid
flowchart LR
  Prod[Producer] --> Q[Queue]
  Q --> Cons[Consumer]
  Cons -->|ack| Q
  Cons -->|fail N times| DLQ[Dead letter]
```

| Guarantee | Mechanism |
|-----------|-----------|
| Durability | Replicate to disk before ACK |
| At-least-once | Visibility timeout + redelivery |
| Ordering | Single partition / FIFO queue |
| Backpressure | Queue depth monitoring + scale consumers |

**Kafka vs SQS:**
| | Kafka | SQS |
|---|-------|-----|
| Model | Log (replay) | Queue (delete on ack) |
| Ordering | Per partition | FIFO variant |
| Throughput | Very high | High managed |

**Consumer design:** Idempotent processing + dedup store (processed message IDs).""",
        "Message queue questions test delivery semantics — at-least-once + idempotent consumer is the standard answer.",
        "Exactly-once semantics? — Kafka transactions or idempotent producer + dedup; expensive.",
        "Priority queues? — Separate queues per priority; weighted consumer allocation.",
        "Assume exactly-once without idempotent consumers",
        "No DLQ — poison message blocks queue",
        "Unbounded queue without consumer scaling plan",
    ),
    q(
        "Payment System Design",
        "Full Scenario",
        "Very Common",
        "Design payment processing: authorize, capture, refund, idempotency. PCI compliance, 99.99% accuracy.",
        "Tokenized cards (Stripe/Adyen); payment state machine; idempotency keys; ledger double-entry accounting; webhook reconciliation; never store raw PAN.",
        """**State machine:**
```mermaid
stateDiagram-v2
  [*] --> Authorized
  Authorized --> Captured
  Authorized --> Voided
  Captured --> Refunded
  Captured --> PartialRefund
```

**Architecture:**
| Component | Role |
|-----------|------|
| Payment gateway adapter | Stripe/Adyen abstraction |
| Ledger service | Double-entry audit trail |
| Idempotency store | Prevent duplicate charges |
| Reconciliation worker | Match provider webhooks to internal state |

**PCI:** SAQ-A — card data never touches your servers (hosted fields / tokenization).

**Failure:** Timeout → query provider status before retry (avoid double charge).

**Ledger:** Every money movement = debit + credit entries; immutable append-only.""",
        "Payment design demands idempotency and ledger — financial correctness over availability theater.",
        "Multi-currency? — Presentment vs settlement currency; FX rate snapshot at capture.",
        "Chargeback workflow? — Dispute state; evidence upload; link to original transaction.",
        "Store credit card numbers in database",
        "Retry failed payment without idempotency key",
        "No reconciliation with payment provider",
    ),
    q(
        "Fraud Detection System",
        "Full Scenario",
        "Common",
        "Design real-time fraud detection for e-commerce checkout. <100ms decision, minimize false positives.",
        "Feature extraction stream → rules engine (hard blocks) → ML model score → decision (approve/review/decline); feature store; human review queue for borderline; feedback loop for model retrain.",
        """**Decision pipeline:**
```mermaid
flowchart LR
  Checkout --> Feat[Feature fetch]
  Feat --> Rules[Rules engine]
  Rules --> ML[ML scorer]
  ML --> Dec{Decision}
  Dec -->|review| Queue[Manual review]
  Dec -->|decline| Block[Block + alert]
```

**Features:** Velocity (5 txns/10min), device fingerprint, geo mismatch, email domain age, amount anomaly.

| Layer | Latency | Purpose |
|-------|---------|---------|
| Rules | <5ms | Known bad patterns |
| ML | <50ms | Novel fraud |
| Graph | Async | Ring detection |

**False positive cost:** Lost revenue + customer anger — tune threshold for review band (0.4-0.7 score).

**Compliance:** Model explainability for disputes; audit log per decision.""",
        "Fraud is rules + ML + human review — show latency budget and false positive trade-off.",
        "Real-time graph fraud (shared cards)? — Neo4j or custom graph batch; not in 100ms path.",
        "Account takeover vs payment fraud? — Separate models; credential stuffing rules on login.",
        "Block all high-value orders — revenue loss",
        "ML only without explainable rules layer",
        "No manual review queue for edge cases",
    ),
    q(
        "Multi-Region Architecture",
        "Infrastructure",
        "Very Common",
        "Design active-active multi-region deployment for global SaaS. US, EU, APAC. Data residency, latency, conflicts.",
        "Geo-routed DNS/Global Accelerator; regional stacks with data replication; CRDT or last-write-wins for conflicts; strong consistency within region; async cross-region; GDPR data stays in EU region.",
        """**Topology:**
```mermaid
flowchart TB
  GA[Global accelerator]
  GA --> US[US region]
  GA --> EU[EU region]
  GA --> AP[APAC region]
  US <-->|async repl| EU
  EU <-->|async repl| AP
```

| Concern | Pattern |
|---------|---------|
| Latency | Route user to nearest region |
| Data residency | EU PII never leaves EU |
| Consistency | Strong local, eventual global |
| Failover | Health check → drain → redirect |

**Conflict resolution:** Version vectors; application merge; avoid cross-region synchronous transactions.

**Cost:** 3× infrastructure baseline + cross-region egress — justify with SLA/revenue.""",
        "Multi-region is the capstone infrastructure question — tie to CAP, residency, and failover RTO.",
        "Active-passive vs active-active? — Active-passive simpler; active-active for zero RTO read path.",
        "Global database (Spanner/Cosmos multi-write)? — Strong consistency option at premium cost/latency.",
        "Synchronous cross-region writes for all data",
        "Ignore GDPR data residency",
        "No conflict resolution strategy for concurrent edits",
    ),
    q(
        "System Design Capstone Rubric",
        "Interview Readiness",
        "Common",
        "How do you self-evaluate a system design interview answer? Provide a rubric scoring ≥75/100 for readiness.",
        "Score 5 dimensions × 20 points: Requirements (20), Estimation (20), High-level design (20), Deep dive (20), Ops/failures (20). Pass ≥75. Practice 5 full designs timed 45 min.",
        """**Rubric (100 points):**
| Dimension | 20 pts criteria | Common deductions |
|-----------|-----------------|-------------------|
| Requirements | Functional + NFR clarified; assumptions stated | Jump to diagram (-10) |
| Estimation | QPS, storage, bandwidth with math | No numbers (-15) |
| High-level | Clear components, data flow, APIs | Spaghetti diagram (-10) |
| Deep dive | 2 components with trade-offs | Surface-level only (-10) |
| Ops/failures | Monitoring, scaling, failure modes | Happy path only (-15) |

**Time management (45 min):**
| Phase | Minutes |
|-------|---------|
| Requirements | 5 |
| Estimation | 5 |
| High-level | 10 |
| Deep dive | 15 |
| Wrap-up | 5 |
| Buffer | 5 |

**Month 9 capstone:** Complete 5 designs (URL shortener, feed, chat, checkout, ride-share) each scored ≥75 by peer or mentor.

**Pitch template (2 min):** Problem → scale → architecture → key trade-off → how it fails.""",
        "Meta-question closing the Top 50 — shows interview process maturity and self-assessment discipline.",
        "RESHADED vs C4? — RESHADED for whiteboard interview; C4 for documentation deliverables.",
        "Map design to Azure/AWS quickly? — App Service/AKS/SQL/Redis vs ALB/ECS/RDS/ElastiCache.",
        "No estimation in any design",
        "Cannot name single trade-off decision",
        "Never timed full 45-min practice",
    ),
]
