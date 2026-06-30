# Week 47 — Expert Scenario Q&A

> Q101–Q120: Premium format (Week 1 quality).

---


## Q101: Twitter Scale Panel Defense

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | System Design |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

45-minute panel: defend Twitter-like feed design under skeptical principal engineer.

### Short Answer (30 seconds)

Acknowledge fanout trade-offs, state celebrity hybrid explicitly, cite monitoring (p99 feed load), offer phased rollout, stay calm on consistency — collaboration not combat.

### Detailed Answer

**Defense structure:**
1. Repeat concern — validate
2. Evidence: fanout threshold data, cache hit rates
3. Trade-off: eventual consistency 2s acceptable per requirements
4. Evolution: Phase 1 read fanout only

**Red team questions:** Hot celebrity, delete propagation, ranking freshness.

**Architect:** Document accepted risks with expiry review.

### Architecture Perspective

Panel defense tests communication under pressure — not just design knowledge.

### Follow-up Questions

1. **What if requirements change mid-interview? — Adapt diagram — show flexibility.**
2. **Weak area honest? — 'I'd spike ranking separately' — credibility.**

### Common Mistakes in Interviews

- Dismiss reviewer concerns
- Claim zero eventual consistency
- No monitoring or rollback plan

---

## Q102: Payment Platform Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | System Design |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Design payment processing platform — ledger, idempotency, reconciliation.

### Short Answer (30 seconds)

Double-entry ledger, idempotent charge API, webhook dedup, daily reconciliation batch, strong consistency on balance, async notification on settlement.

### Detailed Answer

**Components:**
- Payment API (idempotency-key)
- Ledger service (append-only entries)
- Provider adapter (Stripe/Adyen)
- Reconciliation worker (provider report vs ledger)
- Audit log immutable

**Consistency:** Balance read from ledger primary — never cache.

**Architect:** PCI scope minimization — tokenize cards — no PAN storage.

### Architecture Perspective

Payment design combines consistency, idempotency, compliance.

### Follow-up Questions

1. **Exactly-once money movement? — Idempotent + ledger — not distributed 2PC.**
2. **Chargeback flow? — Separate dispute state machine.**

### Common Mistakes in Interviews

- Cache account balance
- No reconciliation batch
- Double charge on retry without idempotency

---

## Q103: Black Friday Flash Sale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | System Design |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Black Friday: cart service melting at 50K RPS — live incident system design response.

### Short Answer (30 seconds)

Enable waiting room, Redis cart only, disable non-critical paths, scale read replicas, queue checkout, extend inventory reservation TTL, circuit break recommendation service.

### Detailed Answer

**Immediate:**
1. Shed marketing API load
2. Scale cart Redis cluster
3. CDN product pages
4. Queue checkout — async order confirmation

**Post-incident:** Load test 2× peak, waiting room automation, inventory reservation audit.

**Architect:** Pre-approved runbook beats improvisation.

### Architecture Perspective

Incident scenario tests operational thinking under scale.

### Follow-up Questions

1. **Virtual waiting room? — Token admission — Fair queuing.**
2. **Oversell audit? — Reconcile reservations vs inventory post-event.**

### Common Mistakes in Interviews

- Scale SQL cart table vertically only
- No waiting room for predictable flash sale
- Disable monitoring to reduce load

---

## Q104: Cross Region Active Active DB

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | System Design |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Design active-active database across US and EU with data residency.

### Short Answer (30 seconds)

Cell-based: EU users pinned to EU cell; US to US; async replication for global admin reports only; no cross-region synchronous writes in hot path.

### Detailed Answer

**Challenge:** Conflict resolution if active-active same record.

**Approach:**
- Partition users by home region
- Cross-region reads via replica — not writes
- Global entities (product catalog) — CRDT or single writer region

**Architect:** GDPR — EU data stays EU cell — routing enforcement.

### Architecture Perspective

Active-active is hard — scoped cells beat naive multi-master.

### Follow-up Questions

1. **Spanner/Cosmos multi-region? — Managed global consistency — cost trade-off.**
2. **Failover? — DNS + verify replication lag before write accept.**

### Common Mistakes in Interviews

- Active-active writes same account both regions
- Cross-region sync call in checkout
- Ignore data residency law

---

## Q105: Celebrity Fanout Failure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | System Design |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Fanout-on-write for celebrity with 5M followers caused 6-hour outage — postmortem design fix.

### Short Answer (30 seconds)

Switch celebrities to fanout-on-read permanently; threshold auto-classify accounts >100K followers; async fanout job with rate limit for medium accounts.

### Detailed Answer

**Root cause:** Write fanout 5M Redis writes blocked publish path.

**Fix:**
1. Follower threshold config
2. Celebrity flag in user profile
3. Publish O(1) — push to celebrity list only
4. Followers pull at read time

**Architect:** Load test fanout cost before enabling write fanout globally.

### Architecture Perspective

Real postmortem format demonstrates learning from failure.

### Follow-up Questions

1. **Dynamic threshold? — Metrics-driven — auto-promote to celebrity tier.**
2. **Backfill fanout? — Don't — forward-only fix.**

### Common Mistakes in Interviews

- Retry 5M fanout synchronously
- No follower count threshold
- Ignore publish path latency SLO

---

## Q106: Cache Avalanche Product Launch

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | System Design |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

New iPhone launch — cache expired, DB collapsed — expert mitigation plan.

### Short Answer (30 seconds)

Pre-warm cache 1h before launch, TTL jitter all product keys, single-flight mutex, autoscale DB read replicas, CDN cache product API responses, feature flag throttle non-buyers.

### Detailed Answer

**Launch runbook:**
1. T-60min: cache warmup job
2. T-0: monitor miss rate + DB CPU
3. Trigger: enable request coalescing + extend TTL emergency
4. Post: analyze miss storm timeline

**Architect:** Game day before major launch — mandatory.

### Architecture Perspective

Launch cache scenarios are retail war stories — preparation beats reaction.

### Follow-up Questions

1. **Queue waiting room? — If checkout also hot — separate control.**
2. **Static product page? — CDN serve — bypass API entirely for browse.**

### Common Mistakes in Interviews

- No pre-warm before known launch
- Identical TTL millions of keys
- First production load test on launch day

---

## Q107: Saga Compensation Walkthrough

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | System Design |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Walk through failed checkout saga — payment succeeded, shipment failed — compensate.

### Short Answer (30 seconds)

Shipment fails → compensate: refund payment → release inventory → mark order failed → notify customer — each compensation idempotent with sagaId.

### Detailed Answer

**State machine:**
```
Reserved → Paid → ShipmentFailed
  → CompensateRefund (idempotent)
  → CompensateReleaseInventory
  → OrderStatus=Failed
```

**Durable saga log:** Every step + compensation recorded.

**Architect:** Manual intervention queue for compensation failure — don't lose money.

### Architecture Perspective

Compensation walkthrough is saga interview gold — concrete steps.

### Follow-up Questions

1. **Partial refund? — Business rule — full refund vs retry shipment.**
2. **Timeout? — Shipment wait max 30m — then compensate automatically.**

### Common Mistakes in Interviews

- No compensation defined for payment success
- Saga state lost on service restart
- Hope manual ops fixes overnight

---

## Q108: Skeptical Interviewer System Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Interview Skills |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Interviewer says 'your design won't work' — how respond in system design?

### Short Answer (30 seconds)

Listen, clarify their concern, validate valid points, adjust design or explain trade-off with metrics, invite collaboration — never defensive.

### Detailed Answer

**Techniques:**
- 'Help me understand the failure mode you see'
- Whiteboard the concern as scenario
- Offer alternative: 'We could also...'
- Cite production precedent if true

**Architect:** Interview is collaboration simulation — ego hurts score.

### Architecture Perspective

Soft skills matter at staff level — adaptability under challenge.

### Follow-up Questions

1. **Wrong and they are right? — Acknowledge and pivot — scores higher.**
2. **Stuck defending bad choice? — 'Given that constraint, I'd revise to...'**

### Common Mistakes in Interviews

- Argue aggressively
- Ignore interviewer redirect
- Abandon entire design instead of targeted fix

---

## Q109: SQL vs NoSQL Under Pressure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | System Design |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Interviewer pushes SQL for your Cassandra chat design — defend or pivot?

### Short Answer (30 seconds)

Evaluate: chat messages are append-heavy, high write volume, flexible schema per message type — Cassandra fits. If they require strong cross-conversation transactions, pivot to SQL with sharding and cite trade-off.

### Detailed Answer

**Defense points:**
- Write pattern: append-only by conversationId
- Query: by conversation — partition key match
- Scale: horizontal shard native

**Pivot if:** Complex joins across conversations needed — SQL + shard.

**Architect:** Decision matrix on whiteboard — not religion.

### Architecture Perspective

Flexible defense/pivot shows judgment not dogma.

### Follow-up Questions

1. **When hybrid? — SQL metadata + Cassandra messages — common pattern.**
2. **DynamoDB? — Alternative — same access pattern argument.**

### Common Mistakes in Interviews

- NoSQL because 'web scale' buzzword
- SQL without shard plan at 1M writes/sec
- Refuse to pivot when interviewer identifies real requirement

---

## Q110: URL Shortener Full Mock Debrief

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Interview Skills |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Debrief 45-minute URL shortener mock — what separates strong from weak?

### Short Answer (30 seconds)

Strong: requirements stated, math shown, separate read/write paths, cache + DB, ID generation justified, analytics async, failures mentioned. Weak: jumped to hash table, no scale, no cache invalidation.

### Detailed Answer

**Rubric (22 pts):**
- Requirements (2) Estimation (2) HLD (3) API (2)
- Storage (2) Cache (2) ID gen (2) Deep dive (3)
- Failures (2) Security (1) Monitoring (1)

**Strong score:** 16+

**Improve one thing:** Always separate redirect hot path minimal deps.

### Architecture Perspective

Structured debrief builds improvement loop for mocks.

### Follow-up Questions

1. **Analytics deep dive? — Kafka click stream — optional if time.**
2. **Custom alias abuse? — Rate limit + reserved word blocklist.**

### Common Mistakes in Interviews

- No estimation performed
- Single monolithic service all concerns
- MD5-only collision hand-wave

---

## Q111: Chat Multi Region Split Brain

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | System Design |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Chat users in US and EU see different message order during partition — resolve.

### Short Answer (30 seconds)

Home region owns conversation partition; during partition reject writes to non-home; merge on heal with sequence log; document CAP choice CP for message order.

### Detailed Answer

**Detection:** Vector clock or sequence gap on heal.

**UX:** Show 'connecting...' not duplicate messages.

**Architect:** Prefer single write region per conversation — simpler than CRDT for most chat.

### Architecture Perspective

Split brain scenario tests distributed consistency depth.

### Follow-up Questions

1. **CRDT chat? — Auto-merge — operational complexity high.**
2. **Last-write-wins? — Document user-visible conflict policy.**

### Common Mistakes in Interviews

- Multi-master same conversation both regions
- Silent message loss on partition
- No sequence numbers

---

## Q112: Search Reindex Zero Downtime

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | System Design |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Executive asks: reindex 500M products without 1 minute search outage — plan.

### Short Answer (30 seconds)

Blue-green index alias swap, dual-write CDC during migration, validate parity, swap in maintenance window seconds, rollback alias if error rate spikes.

### Detailed Answer

**Timeline:**
- Week 1-2: Build v2 index parallel
- Week 3: Dual-write validation
- Cutover: atomic alias swap (<1s user impact)

**Communication:** Search may be briefly inconsistent during swap — acceptable per SLA.

**Architect:** Rehearse swap in staging with production volume snapshot.

### Architecture Perspective

Executive scenario tests communication + technical plan.

### Follow-up Questions

1. **Parity validation? — Sample 10K queries compare results.**
2. **Cost? — Double ES cluster during migration — budget upfront.**

### Common Mistakes in Interviews

- In-place reindex on live serving index
- No rollback plan
- Skip validation before alias swap

---

## Q113: Notification Provider Outage

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | System Design |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Twilio down — OTP login blocked — expert response design.

### Short Answer (30 seconds)

Multi-provider failover (Twilio → Vonage), circuit breaker per provider, queue OTP with delay message, fallback email OTP, status page communication.

### Detailed Answer

**Architecture:**
- Provider abstraction interface
- Health check on provider error rate
- Automatic failover after N failures
- OTP queue retains 10 min — deliver on recovery

**Architect:** SLA with provider + contractual failover requirement.

### Architecture Perspective

Provider dependency failure is real — multi-provider expected.

### Follow-up Questions

1. **Circuit breaker per channel? — SMS separate from email.**
2. **Rate limit provider? — Respect vendor limits — separate queues.**

### Common Mistakes in Interviews

- Single SMS provider hardcoded
- Sync OTP in login request only
- No fallback channel

---

## Q114: Rate Limiter Bypass Attack

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | System Design |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Attacker rotates IP to bypass per-IP rate limit — mitigate.

### Short Answer (30 seconds)

Layer limits: IP (edge WAF), API key (authoritative), device fingerprint, behavioral anomaly detection, captcha challenge on threshold.

### Detailed Answer

**Defense layers:**
1. Cloudflare/AWS WAF rate limit
2. API key required for mutating endpoints
3. Redis sliding window per apiKey
4. ML anomaly on request patterns

**Architect:** Never rely on IP-only for authenticated API abuse.

### Architecture Perspective

Security-aware rate limiting beyond basic token bucket.

### Follow-up Questions

1. **Distributed attack? — Global Redis limit still applies per key.**
2. **Cost attack? — Expensive endpoint lower limit tier.**

### Common Mistakes in Interviews

- IP-only rate limit for B2B API
- No WAF in front of origin
- Captcha never triggered

---

## Q115: Microservices Blast Radius

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | System Design |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Payment service bug takes down entire platform — reduce blast radius.

### Short Answer (30 seconds)

Bulkheads: separate deployment, circuit breakers on callers, async boundary for non-critical paths, catalog browse must work without payment, timeout fail-fast.

### Detailed Answer

**Architecture review:**
- Catalog → no sync call to Payment
- Checkout → Payment with 2s timeout + breaker
- Browse degraded mode: hide buy button if payment health red

**Architect:** Dependency graph analysis quarterly — break cycles.

### Architecture Perspective

Blast radius is failure isolation — staff architect responsibility.

### Follow-up Questions

1. **Chaos monkey? — Inject payment failure — verify catalog OK.**
2. **Sync chain depth? — Max 2 hops — prefer events.**

### Common Mistakes in Interviews

- Every page sync calls payment for 'personalization'
- No circuit breaker on callers
- Shared thread pool all dependencies

---

## Q116: Network Partition Consistency

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Distributed Systems |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

During AZ network partition, inventory shows 5 units on each side — oversell risk — design fix.

### Short Answer (30 seconds)

Leader-elected inventory writer per SKU shard, or optimistic locking with version + reserve tokens in central store, reject purchase if quorum unavailable.

### Detailed Answer

**CP choice for inventory:** Sacrifice availability during partition — reject purchases rather than oversell.

**Reserve pattern:** Decrement on reserve not on view — TTL on reservation.

**Architect:** Document CAP choice per entity — inventory is CP.

### Architecture Perspective

Partition scenario makes CAP concrete — inventory is CP classic.

### Follow-up Questions

1. **CRDT inventory? — Usually wrong domain — reservations better.**
2. **Eventual inventory for flash sale? — Only with oversell tolerance — rare.**

### Common Mistakes in Interviews

- Active-active inventory counters both AZ
- No reservation TTL
- Browse count equals available without lock

---

## Q117: System Design Cost Optimization

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | System Design |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

CFO says cloud bill doubled — optimize architecture without killing SLA.

### Short Answer (30 seconds)

Right-size over-provisioned pods, reserved instances for baseline, tier storage (S3 IA/Glacier), cache to reduce DB tier, autoscale min lowered with SLO guard, review cross-AZ traffic.

### Detailed Answer

**Quick wins:**
- Delete unused resources
- RDS → reserved 1-year
- Log retention 30d not forever
- CDN hit ratio improvement

**Architect trade-off:** Don't cut replicas below HA requirement — document risk acceptance.

### Architecture Perspective

FinOps awareness expected at architect level.

### Follow-up Questions

1. **Unit economics? — Cost per order metric — FinOps dashboard.**
2. **Spot instances? — Stateless workers OK — not stateful DB.**

### Common Mistakes in Interviews

- Cut all replicas to save cost
- No logging retention policy
- Ignore cross-AZ data transfer cost

---

## Q118: GDPR Delete Distributed

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | System Design |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

User requests deletion — propagate across 15 microservices and blob storage.

### Short Answer (30 seconds)

Orchestrated delete workflow: tombstone userId, event `UserDeleteRequested`, each service deletes/anonymizes, blob lifecycle delete, audit log retention legal hold exception, completion certificate.

### Detailed Answer

**Pattern:**
- Saga orchestrator tracks per-service ack
- Idempotent delete handlers
- 30-day soft delete then hard purge
- Search index remove document

**Architect:** Legal holds pause delete — workflow state machine.

### Architecture Perspective

GDPR delete is cross-system orchestration — common enterprise scenario.

### Follow-up Questions

1. **Anonymize vs delete? — Orders may anonymize PII — retain aggregate.**
2. **Backup retention? — Crypto-shred or re-backup without user.**

### Common Mistakes in Interviews

- Delete one DB table only
- No audit trail of deletion
- Immediate hard delete backups impossible

---

## Q119: Real Time Analytics Stream

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | System Design |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Design real-time dashboard for 100K events/sec clickstream.

### Short Answer (30 seconds)

Kafka ingest → Flink windowed aggregates → Redis materialized counters → WebSocket push to dashboard, Lambda for ad-hoc drill-down to ClickHouse.

### Detailed Answer

**Windows:** 1-min tumbling for live chart
**State:** Flink RocksDB
**Display:** Sample if >10K points — aggregate for UI

**Architect:** Separate real-time path from batch data warehouse.

### Architecture Perspective

Lambda architecture — speed layer + batch layer — classic pattern.

### Follow-up Questions

1. **Late events? — Watermarks in Flink — allowed lateness config.**
2. **Exactly-once counts? — Idempotent sink or accept approximate.**

### Common Mistakes in Interviews

- Poll SQL every second
- Unbounded state per user key
- Dashboard queries raw event log

---

## Q120: System Design Post Mortem Present

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Interview Skills |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Present architecture postmortem to leadership after 4-hour outage — structure.

### Short Answer (30 seconds)

Timeline, customer impact, root cause (5 whys), contributing factors, what worked, action items with owners/dates, blameless tone, no jargon without translation.

### Detailed Answer

**Executive format (10 min):**
1. Impact: 40K users, $200K revenue, 4h duration
2. Root cause: cache config deploy without warmup
3. Fix: rolled back + runbook updated
4. Prevention: launch game day, automated warmup CI gate

**Architect:** Own technical narrative — translate to business impact.

### Architecture Perspective

Postmortem presentation is staff skill — blameless + actionable.

### Follow-up Questions

1. **5 whys? — Dig past proximate cause.**
2. **Action item tracking? — Jira with exec visibility.**

### Common Mistakes in Interviews

- Blame individual engineer
- Jargon-heavy without impact translation
- No preventive action items

---
