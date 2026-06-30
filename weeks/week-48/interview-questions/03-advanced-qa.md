# Week 48 — Advanced Q&A

> Q071–Q100: Premium format (Week 1 quality).

---


## Q071: Notification Exactly Once Debate

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Interviewer demands exactly-once notification delivery — respond honestly.

### Short Answer (30 seconds)

True exactly-once end-to-end impossible with external providers — at-least-once transport + idempotent consumer + dedup key = effectively-once user experience.

### Detailed Answer (3–5 minutes)

**Honest answer:**
- SMTP/SMS providers don't offer exactly-once
- Our guarantee: user sees max one notification per eventId
- Implementation: dedup store + provider idempotency keys where supported

**Architect:** Define guarantee precisely — don't over-promise.

### Architecture Perspective

Honesty on delivery semantics scores higher than buzzword exactly-once.

### Follow-up Questions

1. **Transactional outbox? — Ensures we don't lose intent to send.**
2. **Duplicate UX test? — QA sends same event twice — verify one push.**

### Common Mistakes in Interviews

- Claim Kafka exactly-once solves provider duplicates
- No dedup layer
- Ignore provider failure retry duplicates

---

## Q072: Cart Inventory Race Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Two users buy last item simultaneously — walk through cart mock resolution.

### Short Answer (30 seconds)

Optimistic version on inventory row, reserve on checkout start, first commit wins, second gets 409 Conflict 'out of stock', release reservation on payment timeout.

### Detailed Answer (3–5 minutes)

**Flow:**
1. Both add to cart — OK
2. Both checkout — reserve attempts
3. First reserve succeeds (version match)
4. Second fails version — return error
5. First completes payment — decrement

**Architect:** Never check-then-set without atomic operation.

### Architecture Perspective

Inventory race is cart mock crux — atomic reserve expected.

### Follow-up Questions

1. **Pessimistic lock? — Higher contention — optimistic usually enough.**
2. **Oversell audit? — Reconcile reservations nightly.**

### Common Mistakes in Interviews

- Read count then write without lock
- Cart holds inventory indefinitely
- No reservation timeout

---

## Q073: Queue Priority Inversion Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

Low-priority batch jobs block OTP messages in shared queue — fix in mock.

### Short Answer (30 seconds)

Separate queues: transactional (OTP) vs batch (marketing), dedicated worker pools, WFQ or strict priority consumer always drains OTP queue first.

### Detailed Answer (3–5 minutes)

**Architecture:**
```
OTP → high-priority queue → dedicated workers
Marketing → bulk queue → scale separately
```

**Never:** Single FIFO queue all message types.

**Architect:** Priority separation is ops requirement — not optional.

### Architecture Perspective

Priority inversion real in notification systems — separate queues standard.

### Follow-up Questions

1. **Head-of-line blocking? — Why shared queue fails OTP SLA.**
2. **Autoscale per queue? — OTP pool fixed minimum always on.**

### Common Mistakes in Interviews

- Single queue all priorities
- Batch job consumes all workers
- OTP SLA missed during marketing blast

---

## Q074: Pagination Keyset Seek Method

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

Implement keyset pagination with seek method for large admin table.

### Short Answer (30 seconds)

Seek: `WHERE id > @lastId ORDER BY id LIMIT 50` — simpler than tuple cursor for single-column sort; cursor encodes lastId for opaque client token.

### Detailed Answer (3–5 minutes)

**vs OFFSET:** OFFSET 100000 scans skipped rows — O(n) degradation.

**Keyset tuple:** `(created_at, id)` for non-unique sort columns.

**Mock tip:** Admin tables millions rows — always keyset not offset.

### Architecture Perspective

Keyset/seek pagination depth beyond basic cursor mention.

### Follow-up Questions

1. **Stable sort column? — Must be indexed unique or composite.**
2. **Page jump to arbitrary page? — Offset acceptable for admin only — not feed.**

### Common Mistakes in Interviews

- OFFSET on 10M row admin export
- Seek without index on sort column
- Cursor tampering exposes SQL injection

---

## Q075: Rate Limit Sliding Window Lua

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

Write Redis Lua script for sliding window rate limit in mock.

### Short Answer (30 seconds)

ZSET stores request timestamps; Lua removes expired, counts members, adds current if under limit, returns allowed/remaining atomically.

### Detailed Answer (3–5 minutes)

**Pseudocode Lua:**
```
redis.call('ZREMRANGEBYSCORE', key, 0, now-window)
if redis.call('ZCARD', key) < limit then
  redis.call('ZADD', key, now, now)
  return {1, limit - count}
else return {0, 0} end
```

**Architect:** Atomic Lua prevents race — mention in every distributed rate limit answer.

### Architecture Perspective

Lua atomicity is expected detail in rate limit deep dive.

### Follow-up Questions

1. **Token bucket Lua? — Alternative — store tokens + last_refill.**
2. **Fixed window? — Boundary burst problem — sliding preferred.**

### Common Mistakes in Interviews

- INCR without window cleanup
- Per-server in-memory limit
- No atomicity — race allows burst over limit

---

## Q076: Auth Token Refresh Rotation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Design refresh token rotation to detect theft in auth mock.

### Short Answer (30 seconds)

Issue refresh token family ID; on refresh issue new refresh + invalidate old; reuse of old token revokes entire family — signals theft.

### Detailed Answer (3–5 minutes)

**Flow:**
1. Login → access 15m + refresh (httpOnly cookie)
2. Refresh → new pair, old refresh blacklisted
3. Attacker reuses stolen old refresh → family revoked, user forced re-login

**Architect:** Store refresh token hash only — never plaintext.

### Architecture Perspective

Refresh rotation is OAuth best practice — auth mock depth.

### Follow-up Questions

1. **PKCE? — Mandatory for SPA public clients.**
2. **Session fixation? — New token on privilege elevation.**

### Common Mistakes in Interviews

- Refresh token never rotates
- Refresh in localStorage XSS vulnerable
- Long-lived access token no refresh

---

## Q077: Logging Injection Prevention

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

Prevent log injection when logging user-supplied input in mock design.

### Short Answer (30 seconds)

Structured JSON logging — user input in field values not concatenated; sanitize newlines; centralized log pipeline; no log parsing as commands.

### Detailed Answer (3–5 minutes)

**Anti-pattern:**
```
logger.info('User login: ' + username)
// username = 'admin\nFAKE ERROR root access granted'
```

**Fix:**
```
logger.info('User login', { username: sanitize(username) })
```

**Architect:** SIEM rules parse JSON fields — injection fails.

### Architecture Perspective

Security detail in logging mock separates thorough candidates.

### Follow-up Questions

1. **PII in logs? — Redact email, token — compliance.**
2. **Log volume attack? — Rate limit log lines per request.**

### Common Mistakes in Interviews

- String concat user input in logs
- Log levels DEBUG in prod flood
- No centralized log schema

---

## Q078: Metrics Cardinality Control

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

High-cardinality labels crashed Prometheus — fix in metrics mock.

### Short Answer (30 seconds)

Never label metrics with userId, orderId, URL path — use bounded labels (service, route template, status class); aggregate high-cardinality to logs/traces.

### Detailed Answer (3–5 minutes)

**Rules:**
- `http_requests_total{route='/users/:id'}` OK
- `http_requests_total{userId='12345'}` BAD

**Cardinality explosion:** 1M users × metrics = OOM.

**Architect:** Metric naming review in CI — reject high-cardinality labels.

### Architecture Perspective

Cardinality is production Prometheus lesson — metrics mock depth.

### Follow-up Questions

1. **Histogram buckets? — Standard buckets — don't customize per endpoint excessively.**
2. **Recording rules? — Pre-aggregate expensive queries.**

### Common Mistakes in Interviews

- userId label on request counter
- Unbounded path label per URL
- No metric retention or cardinality limits

---

## Q079: Deployment Canary Analysis

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

Canary deployment: 10% traffic shows 2× error rate — automated rollback criteria.

### Short Answer (30 seconds)

Compare canary vs baseline error rate and p99; auto-rollback if error rate >1.5× baseline for 5 min or p99 >200ms delta; Argo Rollouts or Flagger.

### Detailed Answer (3–5 minutes)

**Metrics gate:**
- Error rate ratio >1.5× for 5 min → rollback
- p99 latency delta >200ms → rollback
- Manual promotion if all green 30 min

**Architect:** Feature flags decouple deploy from release — rollback code without rollback schema.

### Architecture Perspective

Canary analysis connects deployment mock to SLO metrics.

### Follow-up Questions

1. **Blue-green vs canary? — Blue-green faster rollback; canary gradual.**
2. **DB migration with canary? — Expand-contract — backward compatible only.**

### Common Mistakes in Interviews

- Promote canary with 2× errors
- No automated rollback criteria
- Breaking schema same deploy as canary

---

## Q080: Multi Tenant RLS PostgreSQL

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

Implement row-level security for shared-table multi-tenant SaaS in mock.

### Short Answer (30 seconds)

PostgreSQL RLS policy `tenant_id = current_setting('app.tenant_id')`; set tenant from JWT in connection middleware; defense in depth with app filter too.

### Detailed Answer (3–5 minutes)

**Setup:**
```sql
ALTER TABLE orders ENABLE ROW LEVEL SECURITY;
CREATE POLICY tenant_isolation ON orders
  USING (tenant_id = current_setting('app.tenant_id')::uuid);
```

**Architect:** RLS catches ORM bugs — not substitute for authZ review.

### Architecture Perspective

RLS is concrete multi-tenant mock depth beyond app filter mention.

### Follow-up Questions

1. **Connection pool + RLS? — Set tenant per request scope — reset after.**
2. **Bypass RLS superuser? — App uses non-super role only.**

### Common Mistakes in Interviews

- App filter only no RLS
- TenantId from client body not JWT
- Cross-tenant integration test missing

---

## Q081: Read Replica Read After Write

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

User updates profile then GET returns stale data from replica — fix in mock.

### Short Answer (30 seconds)

Route read-after-write to primary for session window (60s), or embed write version in JWT and reject stale replica reads below version.

### Detailed Answer (3–5 minutes)

**Patterns:**
- Sticky primary after write cookie
- `read_consistency=strong` query param internal
- Client receives updated payload from write response — skip immediate GET

**Architect:** Classify endpoints — profile edit needs read-your-writes.

### Architecture Perspective

Read-after-write is common mock follow-up to replica routing.

### Follow-up Questions

1. **Replication lag monitor? — Route away replica if lag >5s globally.**
2. **Global user? — Home region primary for writes — replica lag varies.**

### Common Mistakes in Interviews

- All GET to replica after POST
- No session stickiness option
- User must wait arbitrary seconds

---

## Q082: CQRS Projection Lag SLA

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Define and enforce read model lag SLA in CQRS mock.

### Short Answer (30 seconds)

SLA: dashboard read model <30s behind command side; monitor consumer lag; alert if >60s; UI show 'data as of' timestamp if lag detected.

### Detailed Answer (3–5 minutes)

**Monitoring:**
- Kafka consumer lag metric
- `read_model_updated_at` column
- Synthetic query comparing command vs read totals

**Recovery:** Replay events from offset if read model corrupt.

**Architect:** Lag SLA in ADR — not 'eventual' hand-wave.

### Architecture Perspective

CQRS mock incomplete without sync lag SLA.

### Follow-up Questions

1. **Multiple read models? — Separate lag per projection.**
2. **Rebuild read model? — Replay log — disaster recovery drill.**

### Common Mistakes in Interviews

- CQRS with no lag monitoring
- Synchronous dual write instead
- User unaware data stale

---

## Q083: Idempotency Distributed Race

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Two identical payment requests same idempotency key arrive simultaneously — handle.

### Short Answer (30 seconds)

DB unique constraint on (client_id, idempotency_key); first insert wins and processes; second waits or gets in-progress 409; return same response when complete.

### Detailed Answer (3–5 minutes)

**States:** `processing` | `completed` | `failed`

**Race flow:**
1. Both try INSERT key
2. One succeeds → process payment
3. Other gets unique violation → poll status → return cached result

**Architect:** Never process payment twice — DB constraint not app check alone.

### Architecture Perspective

Distributed idempotency race is payment mock advanced topic.

### Follow-up Questions

1. **Redis SETNX first? — Common pattern before DB — TTL on lock.**
2. **Different body same key? — 409 Conflict — client bug.**

### Common Mistakes in Interviews

- Check-then-act without unique constraint
- In-memory dedup only
- Double charge on concurrent requests

---

## Q084: Schema Evolution Avro Compatibility

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

Use Avro schema registry with backward compatibility for event evolution.

### Short Answer (30 seconds)

New schema adds optional fields with defaults; consumers read with old schema; registry rejects breaking changes in CI; subject naming strategy per event type.

### Detailed Answer (3–5 minutes)

**Compatibility modes:**
- BACKWARD — new consumer reads old data
- FORWARD — old consumer reads new data
- FULL — both

**Breaking:** Remove field without default — blocked by registry.

**Architect:** Contract tests consume sample events in CI.

### Architecture Perspective

Schema registry mention shows event-driven maturity.

### Follow-up Questions

1. **Protobuf? — Field numbers never reuse — same rules.**
2. **Upcasting? — Transform old events on read — ES pattern.**

### Common Mistakes in Interviews

- Breaking rename in same topic
- No schema registry CI gate
- Force all consumers deploy same hour

---

## Q085: Webhook Backoff Schedule

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Design webhook retry schedule for failing subscriber endpoint.

### Short Answer (30 seconds)

Exponential backoff: 1m, 5m, 30m, 2h, 8h, 24h — max 48h then DLQ; jitter each retry; disable subscriber after 7 days continuous failure; alert customer.

### Detailed Answer (3–5 minutes)

**Delivery record:**
`{ eventId, attempt, nextRetry, lastStatus, lastError }`

**Customer dashboard:** Failed deliveries visible with replay button.

**Architect:** HMAC signature on every attempt — subscriber verifies.

### Architecture Perspective

Webhook retry schedule is expected mock detail.

### Follow-up Questions

1. **Ordering? — Per-resource sequence optional — document.**
2. **Replay API? — Customer fetches missed events by cursor.**

### Common Mistakes in Interviews

- Single retry then drop
- No signature on payload
- No customer visibility into failures

---

## Q086: Batch ETL Idempotent Partitions

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

Make nightly 500M row batch job idempotent per partition.

### Short Answer (30 seconds)

Partition by date; each partition write to staging table; MERGE idempotent into warehouse; checkpoint completed partitions; rerun skips checkpointed.

### Detailed Answer (3–5 minutes)

**Pattern:**
```
FOR each date partition:
  IF checkpoint[date]: SKIP
  transform → staging
  MERGE INTO fact ON key
  SET checkpoint[date] = done
```

**Architect:** Staging zone before prod publish — validate counts.

### Architecture Perspective

Batch idempotency enables safe rerun after failure.

### Follow-up Questions

1. **Incremental watermark? — High-water mark since last success.**
2. **Data quality gate? — Block publish if row count delta >10%.**

### Common Mistakes in Interviews

- Overwrite prod directly no staging
- No checkpoint — full rerun 500M daily
- Single thread partition processing

---

## Q087: Stream Watermark Late Events

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

Handle late-arriving events in fraud detection stream mock.

### Short Answer (30 seconds)

Event-time windows with watermarks; allowed lateness 5 min; side output for very late events to reconciliation batch; processing-time trigger for low latency.

### Detailed Answer (3–5 minutes)

**Flink concepts:**
- Watermark advances with event time
- Window closes after watermark + allowed lateness
- Late events → side output or dropped with metric

**Architect:** Monitor `numLateRecordsDropped` — tune lateness.

### Architecture Perspective

Late event handling separates stream mock from batch poll.

### Follow-up Questions

1. **Event time vs processing time? — Always define in fraud SLA.**
2. **State retention? — Window state TTL — unbounded forbidden.**

### Common Mistakes in Interviews

- Processing time only windows
- Unbounded state per user
- Drop late events silently no metric

---

## Q088: Mock Security Pass Checklist

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Two-minute security pass in every whiteboard mock — checklist.

### Short Answer (30 seconds)

AuthN/Z, TLS, input validation, rate limit, secrets vault, PII encryption at rest, WAF edge — tick each mentally before closing.

### Detailed Answer (3–5 minutes)

**Checklist:**
- [ ] Who calls API?
- [ ] TLS in transit
- [ ] Encryption at rest for PII
- [ ] Rate limit abuse
- [ ] SQL injection — parameterized
- [ ] Secrets not in code

**Architect:** Tier-0 gets STRIDE — others get checklist.

### Architecture Perspective

Security pass prevents easy omission under time pressure.

### Follow-up Questions

1. **Zero trust internal? — mTLS mesh — mention if microservices.**
2. **DDoS? — WAF + edge rate limit separate from plan quota.**

### Common Mistakes in Interviews

- Skip security entirely
- Auth without encryption mention
- Secrets in config repo

---

## Q089: Mock Cost Estimate Slide

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

Add 60-second cost estimate to mock close when interviewer asks FinOps.

### Short Answer (30 seconds)

Rough monthly: compute (pods × $), DB tier, Redis GB, egress TB, queue messages — order of magnitude; call out biggest cost driver and optimization.

### Detailed Answer (3–5 minutes)

**Template:**
- 20 App Service P2v3 ≈ $X
- Azure SQL GP 4 vCore ≈ $Y
- Redis C2 ≈ $Z
- Egress 5TB ≈ $W

**Optimize:** Reserved instances, cache hit ratio, log retention.

**Architect:** Cost is architecture attribute — not afterthought.

### Architecture Perspective

FinOps mention at architect level increasingly common in mocks.

### Follow-up Questions

1. **Unit economics? — Cost per order/notification.**
2. **Serverless vs always-on? — Compare at stated QPS.**

### Common Mistakes in Interviews

- No cost awareness at all
- Underestimate egress by 10×
- Ignore log storage cost

---

## Q090: Mock Monitoring Golden Signals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Name four golden signals and map to components in mock close.

### Short Answer (30 seconds)

Latency (p99 API), Traffic (RPS), Errors (5xx rate), Saturation (CPU, queue depth, DB connections) — one metric per component.

### Detailed Answer (3–5 minutes)

**Mapping example:**
| Component | Signal |
|-----------|--------|
| API GW | RPS, 5xx |
| App | p99, CPU |
| Redis | hit rate, memory |
| Queue | depth, age |
| DB | connections, replication lag |

**Architect:** Alert on SLO burn not every blip.

### Architecture Perspective

Golden signals close shows operational completeness.

### Follow-up Questions

1. **RED method? — Rate Errors Duration — microservice standard.**
2. **USE method? — Utilization Saturation Errors — infrastructure.**

### Common Mistakes in Interviews

- Only CPU monitoring mentioned
- No alert strategy
- Metrics without logs/traces correlation

---

## Q091: Mock Async vs Sync Decision

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

When choose async queue over sync HTTP in mock — decision framework.

### Short Answer (30 seconds)

Async when: slow work (>500ms), spike buffering, fanout, decouple failure domains. Sync when: user needs immediate result, strong consistency read, simple CRUD low latency.

### Detailed Answer (3–5 minutes)

**Decision tree:**
1. User waiting for result? → if no, queue OK
2. Work duration? → >500ms prefer async
3. Peak spike? → queue absorbs
4. Consistency? → saga async; single DB sync OK

**Architect:** Default async for notifications, emails, analytics — sync for payment confirm UX.

### Architecture Perspective

Async/sync framing prevents over-queueing everything.

### Follow-up Questions

1. **Outbox? — Reliable async from sync API boundary.**
2. **Sync chain depth? — Max 2 hops — else async.**

### Common Mistakes in Interviews

- Queue everything including GET
- Sync email send in login API
- No visibility timeout on async work

---

## Q092: Mock Bulkhead Thread Pools

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

Apply bulkhead pattern in microservice mock with three dependencies.

### Short Answer (30 seconds)

Separate thread pool / connection budget per dependency — payment pool 20, inventory pool 30, recommendation pool 10 — starvation of one doesn't kill all.

### Detailed Answer (3–5 minutes)

**Implementation:**
- .NET: separate HttpClient with Polly isolation
- Java: resilience4j bulkhead
- K8s: separate deployments per critical path

**Architect:** Bulkhead + circuit breaker + timeout — resilience triad.

### Architecture Perspective

Bulkhead shows failure isolation depth in mocks.

### Follow-up Questions

1. **Semaphore vs thread pool? — Semaphore lighter — same concept.**
2. **Shared pool exhaustion? — Classic cascade — bulkhead prevents.**

### Common Mistakes in Interviews

- Single thread pool all HTTP clients
- Unbounded parallel calls
- No timeout on pooled calls

---

## Q093: Mock Graceful Degradation Tiers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

Design three degradation tiers when recommendation service fails.

### Short Answer (30 seconds)

Tier 0 full UX; Tier 1 hide recommendations show catalog; Tier 2 cached static homepage; Tier 3 maintenance page — feature flags switch tiers.

### Detailed Answer (3–5 minutes)

**Trigger:** Circuit open on recommendation → auto Tier 1.

**UX:** Never blank page — explain 'personalization temporarily unavailable'.

**Architect:** Degradation tiers documented in runbook — tested quarterly.

### Architecture Perspective

Graceful degradation is user-facing resilience — strong mock close.

### Follow-up Questions

1. **Static fallback cache? — Precomputed popular items.**
2. **Health endpoint reflects tier? — `/health/degraded` for ops.**

### Common Mistakes in Interviews

- 500 error entire site
- No cached fallback content
- Degradation never tested

---

## Q094: Mock API Compatibility Matrix

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

Maintain API compatibility matrix for mobile clients in mock discussion.

### Short Answer (30 seconds)

Matrix: client version × API version × supported — server returns 426 Upgrade Required for deprecated combo with store link.

### Detailed Answer (3–5 minutes)

**Example:**
| Client | Min API | Sunset |
|--------|---------|--------|
| iOS 3.2 | v2 | v1 Mar 2026 |
| Android 2.1 | v2 | v1 Mar 2026 |

**Architect:** Telemetry on client version drives sunset — not calendar alone.

### Architecture Perspective

Compatibility matrix shows platform thinking for mobile mocks.

### Follow-up Questions

1. **Forced upgrade? — Only security critical — grace period.**
2. **Feature flags per client version? — Decouple API from UI release.**

### Common Mistakes in Interviews

- Break API without version bump
- No client version telemetry
- Sunset v1 with 40% traffic still on it

---

## Q095: Mock Disaster Recovery Mention

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

One-minute DR mention in mock — RTO/RPO without over-engineering.

### Short Answer (30 seconds)

State RPO/RTO targets: 'RPO 1h, RTO 4h — async replication to secondary region, DNS failover runbook, quarterly drill.'

### Detailed Answer (3–5 minutes)

**Template:**
- **RPO:** Max data loss — replication lag bound
- **RTO:** Max downtime — failover procedure time
- **Backup:** Daily snapshots + PITR
- **Drill:** Game day quarterly

**Architect:** Match DR investment to tier — not every service multi-region active-active.

### Architecture Perspective

Brief DR mention scores points without derailing mock.

### Follow-up Questions

1. **Pilot light vs warm standby? — Cost vs RTO trade-off.**
2. **Backup untested? — Restore drill mandatory.**

### Common Mistakes in Interviews

- No DR mention ever
- Claim zero RPO without sync replication cost
- Backups never restored in test

---

## Q096: Mock Phased Rollout Narrative

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Close mock with phased rollout — 10% → 50% → 100% with gates.

### Short Answer (30 seconds)

Feature flag rollout by tenant segment; monitor error rate each phase; auto-rollback; dark launch async path before cutover.

### Detailed Answer (3–5 minutes)

**Phases:**
1. Internal dogfood
2. 1% canary tenants
3. 10% → 50% → 100% over 2 weeks
4. Retire old path

**Architect:** Rollout plan separate from architecture diagram — mention both.

### Architecture Perspective

Phased rollout shows production deployment thinking.

### Follow-up Questions

1. **Dark launch? — Process async shadow — compare outputs.**
2. **Kill switch? — Feature flag off — instant revert.**

### Common Mistakes in Interviews

- Big-bang 100% day one
- No metrics gate between phases
- Rollout without rollback tested

---

## Q097: Mock Sequence Diagram Fast

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

Draw checkout sequence diagram in 3 minutes during mock.

### Short Answer (30 seconds)

Client → API → Inventory.reserve → Payment.charge → Order.create → Queue.notify — label sync vs async arrows; number happy path only first.

### Detailed Answer (3–5 minutes)

**Tips:**
- Abbreviate service names
- `(async)` on notification arrow
- Mark failure return path dashed
- Don't draw every HTTP header

**Architect:** Sequence diagram clarifies sync chain depth — exposes timeout budget need.

### Architecture Perspective

Fast sequence diagram skill saves time in deep dive.

### Follow-up Questions

1. **C4 vs sequence? — Sequence for one flow; C4 for structure.**
2. **Too detailed? — 7 boxes max on whiteboard.**

### Common Mistakes in Interviews

- No diagram at all
- Sequence with 15 participants unreadable
- Unlabeled sync/async arrows

---

## Q098: Mock Capacity Math Whiteboard

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Show capacity math on whiteboard in 2 minutes during mock.

### Short Answer (30 seconds)

Write: DAU × actions / 86400 × 3 = peak QPS → pods = QPS/RPS_per_pod × 2 headroom — circle numbers interviewer can follow.

### Detailed Answer (3–5 minutes)

**Visible steps:**
```
10M DAU × 10 actions = 100M/day
100M / 86400 ≈ 1.2K avg QPS
× 3 peak ≈ 3.6K QPS
÷ 500 RPS/pod ≈ 8 pods → 16 with HA
```

**Architect:** Math on board > verbal 'millions of requests'.

### Architecture Perspective

Visible math builds interviewer confidence in estimation.

### Follow-up Questions

1. **Sensitivity? — 'If 20 actions/day → double QPS' — one line.**
2. **Wrong math OK? — Yes if assumptions stated and corrected.**

### Common Mistakes in Interviews

- No numbers written
- Random billion QPS claim
- Estimation never tied to components

---

## Q099: Mock Data Model Normalization

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |

### Question

When normalize vs denormalize in mock data model discussion.

### Short Answer (30 seconds)

Normalize OLTP write path (3NF); denormalize read models, caches, search indexes; never denormalize without invalidation strategy.

### Detailed Answer (3–5 minutes)

**Rules:**
- Orders + order_items normalized — transactional integrity
- Product catalog denormalized in Redis for read
- ES index denormalized for search

**Architect:** Same entity different shapes per access pattern — CQRS lite.

### Architecture Perspective

Normalization debate shows data modeling maturity.

### Follow-up Questions

1. **JSON column? — Flexible attrs — index carefully.**
2. **Eventual denormalized read? — Accept lag — state SLA.**

### Common Mistakes in Interviews

- Single denormalized table everything
- Normalize search index per relation
- Denormalize without update strategy

---

## Q100: Mock Retry Idempotency Layers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |

### Question

Interviewer asks where retries belong in mock architecture — answer.

### Short Answer (30 seconds)

Client: idempotent GET only. Gateway: retry safe reads. Service: Polly on outbound with timeout. Worker: retry with DLQ max — never nested 3×3×3 across all layers.

### Detailed Answer (3–5 minutes)

**Layer rules:**
| Layer | Retry? | Condition |
|-------|--------|----------|
| Browser | Rare | GET only |
| API GW | Careful | Idempotent routes |
| Service outbound | Yes | Timeout + jitter |
| Queue worker | Yes | Max 3 → DLQ |

**Architect:** Document retry budget per call chain — total attempts capped.

### Architecture Perspective

Retry layer question tests distributed systems maturity in mocks.

### Follow-up Questions

1. **Jitter? — Prevent synchronized retry storm on recovery.**
2. **Retry-After 429? — Honor header — don't immediate retry.**

### Common Mistakes in Interviews

- Retry POST payment at all three layers
- Infinite worker retry no DLQ
- No idempotency key on mutating retry

---
