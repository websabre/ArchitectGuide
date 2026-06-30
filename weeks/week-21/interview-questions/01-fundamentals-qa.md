# Week 21 — Fundamentals Interview Q&A

> Q001–Q030: Premium format (Week 1 quality).
> See also: [Interview prep hub](../../../interview-prep/README.md)

---


## Q001: CAP Theorem in Practice

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Fundamentals |
| **Frequency** | Very Common |

### Question

Explain CAP and how it applies to choosing between SQL, Redis, and Cassandra.

### Short Answer (30 seconds)

During partition, choose C or A. All distributed systems need P. SQL with sync replica: CP. Redis cluster with async: AP. Cassandra tunable — often AP with eventual consistency.

### Detailed Answer (3–5 minutes)

CAP is not 'pick two of three always' — it's 'during partition, C or A.'

**Examples:**
- Bank transfer: CP — reject if cannot verify consistency
- Product view count: AP — approximate OK
- Shopping cart in Redis: AP — merge on reconnect

Architect maps each datastore in design to CAP stance and documents business acceptance of inconsistency.

### Architecture Perspective

CAP literacy separates architects from developers who treat all DBs as equal.

### Follow-up Questions

1. **PACELC extension? — Else Latency vs Consistency — even without partition.**
2. **Does Cosmos DB beat CAP? — Tunable consistency — still trade-offs exist.**

### Common Mistakes in Interviews

- Claiming 'we are CA' for distributed system
- Same consistency model for ledger and analytics
- Ignoring partition in multi-region design

---

## Q002: Idempotency Keys

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Reliability |
| **Frequency** | Very Common |

### Question

Design idempotent payment API. What can go wrong without it?

### Short Answer (30 seconds)

Client sends `Idempotency-Key` UUID. Server stores key → response mapping 24h. Retry returns cached response without double charge. Without it: network timeout → client retry → double payment.

### Detailed Answer (3–5 minutes)

**Implementation:**
```
POST /payments
Idempotency-Key: 550e8400-e29b-41d4-a716-446655440000
```
Store in Redis or SQL with unique constraint on key. Process payment in transaction with key insert — duplicate key returns original result.

**Architect:** Mandate for all non-idempotent POST from mobile clients (unreliable networks).

### Architecture Perspective

Idempotency is financial-system hygiene — interview favorite.

### Follow-up Questions

1. **Same key different body? — Return 422 conflict — key reused incorrectly.**
2. **Stripe idempotency window? — 24 hours — industry standard reference.**

### Common Mistakes in Interviews

- Only client-side dedup without server store
- GET requests with side effects
- Idempotency key in URL logged in access logs

---

## Q003: Saga Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Transactions |
| **Frequency** | Very Common |

### Question

Design order checkout saga across inventory, payment, shipping.

### Short Answer (30 seconds)

Choreography: OrderPlaced event → Inventory reserves → Payment charges → Shipping schedules. Compensation: PaymentFailed → release inventory. Orchestration: central coordinator if logic complex.

### Detailed Answer (3–5 minutes)

**Steps:**
1. Reserve inventory (TTL 15 min)
2. Charge payment (idempotent)
3. Confirm order
4. On failure: compensate in reverse order

**Orchestration (Durable Functions):** visible state, easier debug. **Choreography:** looser coupling, harder trace.

Never 2PC across microservices — sagas with compensation instead.

### Architecture Perspective

Distributed transactions without XA is core microservices architecture.

### Follow-up Questions

1. **Saga vs 2PC? — 2PC blocks on failure; saga compensates — eventual consistency.**
2. **Orchestration when? — 6+ steps or complex compensation logic.**

### Common Mistakes in Interviews

- Sync chain without compensation plan
- Distributed 2PC across three services
- No idempotency on saga steps

---

## Q004: Outbox Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Messaging |
| **Frequency** | Very Common |

### Question

Why transactional outbox instead of publish after SaveChanges?

### Short Answer (30 seconds)

Dual-write problem: DB commits, message publish fails (or reverse) — inconsistent state. Outbox writes event in same transaction; relay publishes asynchronously.

### Detailed Answer (3–5 minutes)

**Flow:**
1. BEGIN TRANSACTION
2. INSERT order + INSERT outbox_event
3. COMMIT
4. Relay polls outbox → publishes to Service Bus → marks processed

Debezium CDC alternative for high volume. Architect chooses polling outbox for simplicity or log-based for scale.

### Architecture Perspective

Outbox is the correct answer for reliable event publishing from OLTP DB.

### Follow-up Questions

1. **At-least-once delivery? — Consumers must be idempotent — pair outbox with idempotent handlers.**
2. **Inbox pattern? — Dedup incoming messages — complement outbox.**

### Common Mistakes in Interviews

- Fire-and-forget after SaveChangesAsync
- No duplicate detection on consumer
- Outbox relay single point without HA

---

## Q005: Eventual Consistency UX

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Consistency |
| **Frequency** | Common |

### Question

User complains 'I paid but order still shows pending.' How design for this?

### Short Answer (30 seconds)

Async pipeline causes visible lag. UX: optimistic UI with rollback, status polling, email confirmation as source of truth, 'processing' state not 'failed.'

### Detailed Answer (3–5 minutes)

**Technical:** Read-your-writes via sticky session to primary or short TTL cache invalidation after write.

**Product:** Set expectation — 'Payment processing, refresh in 30 seconds.'

Architect aligns consistency model with user mental model — don't promise instant if pipeline is async.

### Architecture Perspective

Consistency is UX problem as much as technical.

### Follow-up Questions

1. **Strong consistency when needed? — Sync read from primary for order status page only.**
2. **WebSocket for status? — Push update when saga completes — better UX than polling.**

### Common Mistakes in Interviews

- Showing failed before saga timeout
- Reading stale replica for own transaction
- No correlation ID for support lookup

---

## Q006: Quorum and Leader Election

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Consensus |
| **Frequency** | Occasional |

### Question

Why do distributed systems need odd-numbered quorum nodes?

### Short Answer (30 seconds)

Quorum (n/2+1) prevents split brain — two partitions cannot both elect leader. Even nodes risk tie; odd (3, 5) ensures majority on one side.

### Detailed Answer (3–5 minutes)

**Examples:** etcd for K8s, Redis Sentinel, ZooKeeper, Patroni for Postgres.

**Architect:** When evaluating HA product, ask 'how does it prevent split brain?' — not just 'is it HA?'

### Architecture Perspective

Consensus underpins every HA claim.

### Follow-up Questions

1. **Split brain consequence? — Dual writes corrupt data — worse than downtime.**
2. **Witness node? — Cloud blob witness for 2-node SQL AG quorum.**

### Common Mistakes in Interviews

- Two-node cluster without witness
- Ignoring fencing during failover
- Assuming automatic HA means no split brain risk

---

## Q007: Clock Skew and Ordering

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Time |
| **Frequency** | Occasional |

### Question

Why can't you rely on wall-clock timestamps for event ordering?

### Short Answer (30 seconds)

NTP skew between servers — events appear out of order. Use logical clocks (Lamport), vector clocks, or database-assigned monotonic sequence.

### Detailed Answer (3–5 minutes)

**Solutions:**
- Database `rowversion`/sequence for ordering
- Kafka partition ordering per key
- Hybrid logical clocks (CockroachDB)

**Architect:** Never sort distributed events by `DateTime.UtcNow` from different machines for correctness.

### Architecture Perspective

Time is unreliable in distributed systems — plan ordering explicitly.

### Follow-up Questions

1. **Lamport timestamp? — causal ordering without synchronized clocks.**
2. **TTL based on local clock? — Skew causes early expiry — use server authority.**

### Common Mistakes in Interviews

- Cross-machine timestamp sort for audit trail
- No monotonic ID generator
- Assuming NTP perfect in cloud

---

## Q008: Backpressure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Resilience |
| **Frequency** | Common |

### Question

Consumer cannot keep up with producer — architectural responses?

### Short Answer (30 seconds)

Backpressure: slow producer, buffer with bounds, scale consumers, drop/dead-letter low priority, circuit break upstream.

### Detailed Answer (3–5 minutes)

**Patterns:**
- Reactive Streams `request(n)` flow control
- KEDA scale consumers on queue depth
- Bounded channel — block producer when full

**Architect:** Unbounded queue = memory bomb — always bound buffers and alert on lag.

### Architecture Perspective

Backpressure prevents cascade overload.

### Follow-up Questions

1. **Kafka consumer lag alert? — Primary scaling signal.**
2. **Drop vs delay? — Business decision — payments delay, metrics may drop.**

### Common Mistakes in Interviews

- Unbounded in-memory queue
- Scale producer without consumer
- No DLQ for poison messages

---

## Q009: Exactly-Once Semantics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Messaging |
| **Frequency** | Common |

### Question

Is exactly-once delivery possible in distributed systems?

### Short Answer (30 seconds)

True exactly-once end-to-end is impossible — achieve effectively-once via idempotent consumers + dedup + transactional outbox. Kafka EOS within stream processing scope.

### Detailed Answer (3–5 minutes)

**Practical:** At-least-once delivery + idempotent handler + business key dedup = effectively once.

**Architect:** Design for at-least-once; make handlers idempotent. Don't pay complexity cost of EOS unless Kafka streams with specific semantics needed.

### Architecture Perspective

Honest semantics answer impresses principals.

### Follow-up Questions

1. **Kafka exactly-once? — Producer idempotence + transactions within Kafka — not across DB without outbox.**
2. **Distributed transaction across Kafka and DB? — Outbox pattern — not XA.**

### Common Mistakes in Interviews

- Claiming exactly-once without idempotent consumers
- No dedup store
- Ignoring duplicate in financial handlers

---

## Q010: Failure Detection and Heartbeats

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Reliability |
| **Frequency** | Common |

### Question

How do systems detect failed nodes? Gossip vs heartbeat?

### Short Answer (30 seconds)

Heartbeat: central coordinator or health checks at interval. Gossip: nodes exchange state probabilistically (Cassandra, Consul). Missed heartbeats → suspect → failed → failover.

### Detailed Answer (3–5 minutes)

**Architect settings:**
- Health check interval vs failover time trade-off
- False positive failover worse than slow detection sometimes
- Synthetic monitoring from user perspective

K8s: liveness vs readiness probes — different purposes.

### Architecture Perspective

Failure detection tuning affects availability and false failover.

### Follow-up Questions

1. **Phi accrual failure detector? — Adaptive timeout — used in Akka.**
2. **Flapping node? — Hysteresis — require N failed checks before failover.**

### Common Mistakes in Interviews

- No health checks on dependencies
- Liveness probe includes DB — kills pod on DB blip
- Too aggressive failover causes oscillation

---

## Q011: Two-Phase Commit Limits

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Transactions |
| **Frequency** | Very Common |

### Question

Why do architects avoid 2PC across microservices? What breaks at scale?

### Short Answer (30 seconds)

2PC blocks all participants until coordinator commits — locks held, latency spikes, single coordinator failure stalls all. Not suitable for WAN or long-running business logic.

### Detailed Answer (3–5 minutes)

**Phase 1 (prepare):** participants vote ready, hold locks. **Phase 2 (commit/abort):** coordinator decides.

**Problems:**
- Blocking: if coordinator dies after prepare, participants stuck until timeout
- Availability hit during partition — CP behavior
- Locks on inventory/payment rows block other orders

**Architect stance:** Use sagas with compensation, outbox, or single-service transactions. Reserve XA/2PC for legacy same-DC, same-team databases only.

### Architecture Perspective

Rejecting 2PC shows you understand distributed transaction reality.

### Follow-up Questions

1. **When is 2PC acceptable? — Same database cluster, short transactions, ops team owns coordinator HA.**
2. **3PC improvement? — Reduces blocking but adds complexity — rarely used in practice.**

### Common Mistakes in Interviews

- Distributed 2PC across payment and inventory microservices
- Long-running prepare phase holding row locks
- No coordinator HA plan

---

## Q012: Saga Compensation Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Transactions |
| **Frequency** | Very Common |

### Question

Payment succeeded but shipping failed — design compensation steps and ordering.

### Short Answer (30 seconds)

Compensate in reverse order of forward steps. Payment → refund (idempotent). Inventory → release reservation. Each compensating action must be safe to retry and semantically undo the forward step.

### Detailed Answer (3–5 minutes)

**Forward:** Reserve inventory → Charge payment → Create shipment.
**Compensate:** Cancel shipment (if created) → Refund payment → Release inventory.

**Design rules:**
- Compensating transactions are business operations (`RefundPayment`), not DB rollbacks
- Use saga log with state machine — `Compensating`, `Completed`, `Failed`
- TTL on reservations prevents orphan holds

**Architect:** Document which steps are compensatable vs require manual intervention (shipment already picked).

### Architecture Perspective

Compensation design is where saga interviews go deep.

### Follow-up Questions

1. **Pivot vs compensate? — If forward step not yet committed, pivot to alternate path instead of compensate.**
2. **Poison saga step? — Escalate to human workflow after N automated compensation failures.**

### Common Mistakes in Interviews

- Compensation as DELETE without audit trail
- Compensate out of order releasing inventory before refund
- No idempotency on refund API

---

## Q013: Outbox Pattern Deep Dive

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Messaging |
| **Frequency** | Very Common |

### Question

Compare polling outbox, transactional messaging, and CDC relay. When each?

### Short Answer (30 seconds)

Polling outbox: simple, slight lag. Transactional messaging (Kafka EOS): limited cross-store. CDC (Debezium): scales, captures all row changes, ops overhead.

### Detailed Answer (3–5 minutes)

**Polling relay:**
```sql
SELECT * FROM outbox WHERE processed_at IS NULL ORDER BY id LIMIT 100 FOR UPDATE SKIP LOCKED
```
Publish → mark processed in same worker transaction.

**CDC:** Reads DB WAL — no polling load on OLTP, delivers all changes, requires Kafka Connect ops.

**Architect decision matrix:**
- <1K events/sec, team small → polling outbox
- High volume, existing Kafka → Debezium
- Azure SQL + Service Bus → polling or Azure SQL trigger relay

### Architecture Perspective

Deep outbox knowledge separates textbook from production architects.

### Follow-up Questions

1. **Outbox ordering guarantees? — Per aggregate ID partition key preserves order.**
2. **Relay failure mid-batch? — At-least-once relay — consumer dedup required.**

### Common Mistakes in Interviews

- Dual write without outbox
- Outbox table without index on unprocessed rows
- Relay single instance without SKIP LOCKED

---

## Q014: Inbox Deduplication

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Messaging |
| **Frequency** | Common |

### Question

Partner sends duplicate webhooks. Design inbox pattern for exactly-once processing.

### Short Answer (30 seconds)

Store `message_id` in inbox table with unique constraint. Process in same transaction as business update. Duplicate insert fails → skip processing, return 200.

### Detailed Answer (3–5 minutes)

**Flow:**
1. BEGIN TRANSACTION
2. INSERT inbox (message_id) — conflict → rollback, ack duplicate
3. Apply business logic
4. COMMIT

**TTL:** Purge processed inbox rows after 7–30 days.

**Architect:** Pair with outbox on publisher side — end-to-end effectively-once. Redis SET NX for speed with SQL inbox for durability audit.

### Architecture Perspective

Inbox is the consumer-side mirror of outbox.

### Follow-up Questions

1. **At-least-once broker + inbox = effectively once? — Yes if business logic idempotent on replay.**
2. **Inbox vs idempotency key table? — Inbox for inbound events; idempotency keys for client API retries.**

### Common Mistakes in Interviews

- Dedup only in memory — lost on restart
- Process business logic before inbox insert
- No unique constraint on message_id

---

## Q015: Quorum and Raft Basics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Consensus |
| **Frequency** | Common |

### Question

Explain Raft leader election and why quorum is n/2+1.

### Short Answer (30 seconds)

Raft: one leader handles writes, replicates log to followers. Election on leader timeout — candidate needs majority votes. Quorum n/2+1 ensures at most one leader per term.

### Detailed Answer (3–5 minutes)

**Raft terms:**
1. Follower misses heartbeat → becomes candidate
2. Candidate requests votes — needs majority
3. Winner becomes leader — append entries to followers
4. Commit when majority replicated

**Examples:** etcd (K8s), CockroachDB, Consul.

**Architect:** Ask vendors 'Raft or custom?' — understand failover time = election timeout + replication lag.

### Architecture Perspective

Raft literacy explains modern distributed DB behavior.

### Follow-up Questions

1. **Raft vs Paxos? — Raft designed for understandability — same safety guarantees.**
2. **Read from follower? — Possible with linearizability trade-off — stale reads risk.**

### Common Mistakes in Interviews

- Even number of Raft nodes without witness
- Sub-quorum writes during partition
- Ignoring election timeout tuning

---

## Q016: Clock Skew and Ordering

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Time |
| **Frequency** | Common |

### Question

Design event ordering for audit trail across three data centers without synchronized clocks.

### Short Answer (30 seconds)

Never sort by `DateTime.UtcNow` from different hosts. Use database sequence, Snowflake IDs, or Lamport/vector clocks for causal ordering.

### Detailed Answer (3–5 minutes)

**Patterns:**
- **DB authority:** `BIGSERIAL` or `rowversion` assigned at write primary
- **Kafka:** partition by `orderId` — order within partition guaranteed
- **Hybrid logical clocks:** CockroachDB `hlc` — wall time + logical counter

**Audit requirement:** Display events sorted by authoritative sequence, show originating DC as metadata not sort key.

**Architect:** NTP drift in cloud is real (milliseconds to seconds) — design for logical order.

### Architecture Perspective

Time ordering mistakes cause compliance and debugging nightmares.

### Follow-up Questions

1. **TrueTime (Spanner)? — GPS + atomic clocks bound clock uncertainty — expensive.**
2. **Lamport vs vector clocks? — Vector tracks concurrent events — Lamport only causal.**

### Common Mistakes in Interviews

- Cross-DC sort by client timestamp
- Assuming NTP perfect in containers
- No monotonic ID for financial audit

---

## Q017: Split Brain Prevention

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Consensus |
| **Frequency** | Common |

### Question

Two-node SQL Always On AG lost quorum witness — what is split brain and how prevent?

### Short Answer (30 seconds)

Split brain: two nodes both believe they are primary, accept writes — data diverges irreconcilably. Prevent with quorum, fencing/STONITH, and witness.

### Detailed Answer (3–5 minutes)

**Prevention:**
- Odd quorum or witness for 2-node
- Fencing: losing node forcibly stopped from I/O
- `required_synched_secondaries_to_commit` tuning

**Cloud:** Blob witness in Azure, file share witness on-prem.

**Architect:** During partition, **availability vs consistency** — quorum chooses consistency (one side stops). Document RTO/RPO for witness failure.

### Architecture Perspective

Split brain is worse than brief outage — architects prioritize prevention.

### Follow-up Questions

1. **STONITH? — Shoot The Other Node In The Head — isolate before promote.**
2. **Last man standing? — Dangerous without quorum — can promote stale replica.**

### Common Mistakes in Interviews

- Two-node cluster no witness
- Manual failover without fencing
- Both sides accepting writes during partition

---

## Q018: Backpressure Strategies

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Resilience |
| **Frequency** | Common |

### Question

Queue depth growing 10x — architect backpressure response beyond 'scale consumers'.

### Short Answer (30 seconds)

Layered response: bound buffers, slow producers, shed load, scale consumers, dead-letter poison, alert on lag SLO.

### Detailed Answer (3–5 minutes)

**Strategies:**
1. **Bounded channel** — block or drop producer when full
2. **Adaptive publish rate** — reduce batch size when lag > threshold
3. **Priority queues** — drop analytics, preserve payments
4. **KEDA** — scale consumers on lag metric
5. **Circuit break upstream** — stop accepting work user can't complete

**Architect:** Unbounded queue = OOM. Define max lag SLO and escalation runbook before incident.

### Architecture Perspective

Backpressure is load management not just autoscaling.

### Follow-up Questions

1. **Reactive Streams request(n)? — Pull-based flow control in streaming APIs.**
2. **Shed load vs delay? — Payments delay with 503; telemetry sample/drop.**

### Common Mistakes in Interviews

- Unbounded in-memory queue
- Scale producer without consumer capacity plan
- No DLQ for poison messages

---

## Q019: Circuit Breaker Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Resilience |
| **Frequency** | Very Common |

### Question

How tune circuit breaker thresholds for payment vs recommendation services?

### Short Answer (30 seconds)

Payment: low failure threshold, short sampling window, no retry when open. Recommendations: higher threshold, fallback to cached defaults, longer half-open probe interval.

### Detailed Answer (3–5 minutes)

**Polly / resilience pipeline parameters:**
- `FailureRatio` / `MinimumThroughput` — avoid opening on 1/2 requests
- `BreakDuration` — 30s payment, 5s recommendations
- `SamplingDuration` — window for failure rate calculation

**Monitor:** `circuit_state` metric — alert when open > 1 min.

**Architect:** Per-dependency policy — never one global breaker. Document fallback behavior in ADR.

### Architecture Perspective

Tuning shows production resilience experience.

### Follow-up Questions

1. **Half-open probe? — Single test request — success closes, failure reopens.**
2. **Circuit breaker vs retry interaction? — Don't retry when circuit open.**

### Common Mistakes in Interviews

- Same breaker settings all dependencies
- Circuit open with no fallback UX
- No metrics on breaker state transitions

---

## Q020: Bulkhead Isolation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Resilience |
| **Frequency** | Common |

### Question

Design bulkhead isolation for API calling payment, inventory, and email services.

### Short Answer (30 seconds)

Separate thread pools / semaphores / HttpClient pipelines per downstream — email slowness cannot exhaust threads for payment.

### Detailed Answer (3–5 minutes)

**Implementation:**
```csharp
// Polly bulkhead: max 10 parallel, 20 queue
.AddBulkhead(maxParallelization: 10, maxQueuingActions: 20)
```

**K8s:** Separate deployments for critical vs batch paths.

**Architect:** Bulkhead + circuit breaker + timeout = defense in depth. Size pools from load test — payment pool sized for peak checkout.

### Architecture Perspective

Bulkhead prevents one slow dependency from sinking the ship.

### Follow-up Questions

1. **Bulkhead vs timeout? — Timeout limits wait; bulkhead limits concurrency — use both.**
2. **Thread pool starvation signal? — Growing queue length with flat throughput.**

### Common Mistakes in Interviews

- Single shared HttpClient pool all dependencies
- Bulkhead queue unbounded
- No bulkhead on background email worker affecting API

---

## Q021: Retry with Jitter

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Resilience |
| **Frequency** | Very Common |

### Question

Design retry policy for transient 503 from inventory API. Why jitter?

### Short Answer (30 seconds)

Exponential backoff with full jitter: `delay = random(0, min(cap, base * 2^attempt))`. Prevents thundering herd when service recovers — clients don't retry simultaneously.

### Detailed Answer (3–5 minutes)

**Rules:**
- Retry only idempotent operations (GET, PUT with idempotency key)
- Max 3–5 attempts with cap (30s)
- Retry 408, 429, 502, 503, 504 — not 400, 401, 404

**Polly:** `WaitAndRetryAsync` with decorrelated jitter.

**Architect:** Mandate jitter in org resilience standards — without it, recovery causes second outage.

### Architecture Perspective

Jitter is small detail with large production impact.

### Follow-up Questions

1. **Retry-After header? — Honor server hint on 429/503.**
2. **Retry on POST payment without idempotency key? — Never.**

### Common Mistakes in Interviews

- Fixed 1s retry interval on all clients
- Infinite retry on 500 errors
- Retry storm after regional recovery

---

## Q022: Timeout Budgets

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Resilience |
| **Frequency** | Very Common |

### Question

Page load budget 800ms — allocate timeout budget across gateway and three sync services.

### Short Answer (30 seconds)

Subtract network overhead; allocate remaining budget top-down. Client 800ms → gateway 750ms → service A 400ms → B 200ms → C 100ms. Child timeout < parent.

### Detailed Answer (3–5 minutes)

**Pattern:**
- Propagate `X-Timeout-Deadline` or use `CancellationToken` linked to remaining budget
- Fail fast when budget exhausted — don't start call with 50ms left

**Architect:** Document timeout tree in service catalog. Alert when p95 approaches budget — scaling signal before timeouts cascade.

### Architecture Perspective

Timeout budgets connect SLOs to implementation.

### Follow-up Questions

1. **Timeout vs deadline? — Deadline is absolute wall clock; timeout is relative duration.**
2. **Default HttpClient 100s timeout? — Change — kills thread pool under load.**

### Common Mistakes in Interviews

- Same 30s timeout every hop
- Child timeout exceeds parent
- No timeout on outbound calls

---

## Q023: Graceful Degradation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Resilience |
| **Frequency** | Common |

### Question

Recommendations service down during Black Friday — design graceful degradation for product page.

### Short Answer (30 seconds)

Serve cached popular products, hide personalization block, show 'recommendations temporarily unavailable' — core catalog and checkout unaffected.

### Detailed Answer (3–5 minutes)

**Tiers:**
1. **Full:** live recommendations
2. **Degraded:** 1-hour stale cache
3. **Minimal:** bestsellers static list
4. **Off:** section hidden — page loads

**Architect:** Define degradation levels in ADR. Feature flags toggle tiers. Never block checkout on non-critical dependency.

### Architecture Perspective

Graceful degradation protects revenue during partial outages.

### Follow-up Questions

1. **Fallback cache warming? — Pre-populate top 100 SKUs before event.**
2. **Health check drives degradation? — Auto-fallback when dependency unhealthy.**

### Common Mistakes in Interviews

- Entire page 500 when recommendations fail
- No cached fallback path
- Degradation not tested in game day

---

## Q024: CAP in Practice Examples

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Fundamentals |
| **Frequency** | Very Common |

### Question

Map five production components to CAP stance during network partition.

### Short Answer (30 seconds)

During partition: SQL sync replica CP (reject writes), Redis async replica AP (stale reads), Cassandra AP (tunable), ZooKeeper CP, CDN AP.

### Detailed Answer (3–5 minutes)

**Scenario walkthrough — partition between AZs:**
- **Order DB (CP):** reject write if quorum lost — user sees error, no double charge
- **Session cart (AP):** accept writes both sides, merge on heal — acceptable conflict rules
- **Search index (AP):** stale results OK briefly

**Architect:** Document per-component CAP choice and business sign-off on inconsistency windows.

### Architecture Perspective

Concrete CAP mapping beats abstract theorem recitation.

### Follow-up Questions

1. **Bank transfer during partition? — CP — reject rather than risk duplicate.**
2. **Social like count? — AP — approximate acceptable.**

### Common Mistakes in Interviews

- Claiming distributed system is CA
- Same CAP stance for ledger and analytics
- No partition scenario in DR design review

---

## Q025: PACELC Theorem

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Fundamentals |
| **Frequency** | Common |

### Question

Explain PACELC and how it guides database selection beyond CAP.

### Short Answer (30 seconds)

If Partition → choose A or C. Else (normal operation) → choose Latency or Consistency. DynamoDB/Cassandra favor EL; Spanner/Cockroach favor EC.

### Detailed Answer (3–5 minutes)

**Examples:**
- **DynamoDB (PA/EL):** fast writes, eventual consistency default
- **Cosmos strong session (PC/EC):** higher latency for consistency even without partition
- **CockroachDB (PC/EC):** distributed SQL with tunable isolation

**Architect:** CAP only describes partition — PACELC captures everyday latency vs consistency trade-off that dominates most designs.

### Architecture Perspective

PACELC shows mature distributed systems thinking.

### Follow-up Questions

1. **Cosmos consistency levels? — Five levels map to LC spectrum.**
2. **Read-your-writes without strong? — Session consistency — practical middle ground.**

### Common Mistakes in Interviews

- Only discussing CAP in interviews
- Ignoring latency cost of strong consistency
- Strong consistency globally for all reads

---

## Q026: Gossip Protocols

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Consensus |
| **Frequency** | Occasional |

### Question

How do gossip protocols work in Cassandra and Consul? Trade-offs?

### Short Answer (30 seconds)

Nodes periodically exchange state with random peers — epidemic spread. Eventually all nodes converge. O(log n) rounds for cluster-wide awareness.

### Detailed Answer (3–5 minutes)

**Uses:**
- **Cassandra:** failure detection, ring membership
- **Consul:** cluster membership, health state
- **Redis Cluster:** slot map propagation

**Trade-offs:** Eventually consistent membership view — brief window of stale routing. Low overhead vs centralized coordinator.

**Architect:** Understand gossip ≠ consensus — use for membership, not financial ledger writes.

### Architecture Perspective

Gossip explains how decentralized clusters self-organize.

### Follow-up Questions

1. **SWIM protocol? — Improved failure detection — used in Consul.**
2. **Gossip vs heartbeat? — Gossip scales better; heartbeat simpler for small clusters.**

### Common Mistakes in Interviews

- Assuming gossip gives strong consistency
- No handling of stale membership during failover
- Central coordinator without HA for membership

---

## Q027: Leader Election

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Consensus |
| **Frequency** | Common |

### Question

Kubernetes controller needs single leader — compare etcd election vs database advisory lock.

### Short Answer (30 seconds)

etcd/K8s lease: built-in, TTL, watch-based — standard for K8s operators. DB advisory lock: simpler if already on Postgres, risk if DB slow.

### Detailed Answer (3–5 minutes)

**K8s pattern:**
```yaml
leaderElection:
  leaseDuration: 15s
  renewDeadline: 10s
```

**Postgres:** `pg_advisory_lock(id)` — released on connection drop.

**Redis:** `SET key NX EX ttl` — fencing token required for safety.

**Architect:** Leader election for background jobs only — not user-facing request routing without load balancer coordination.

### Architecture Perspective

Leader election prevents duplicate cron side effects.

### Follow-up Questions

1. **Split brain in leader election? — TTL + fencing — stale leader must stop.**
2. **ZooKeeper ephemeral nodes? — Classic pattern — etcd replaced in cloud-native.**

### Common Mistakes in Interviews

- Two leaders processing same payment batch
- No TTL on Redis leader key
- Leader election on every API request

---

## Q028: Distributed Locks Redis

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Coordination |
| **Frequency** | Common |

### Question

Implement safe distributed lock with Redis for invoice generation job.

### Short Answer (30 seconds)

Redlock or single-instance `SET lock_key token NX PX 30000`. Verify token before unlock (Lua script). Always set TTL — prevent deadlock on crash.

### Detailed Answer (3–5 minutes)

**Safety requirements:**
- Unique token per acquirer
- TTL > max job duration + clock skew buffer
- Extend lock (heartbeat) for long jobs
- Fencing token passed to downstream (DB write rejects stale leader)

**Architect:** Redis lock OK for efficiency jobs; use DB or etcd for financial correctness. Martin Kleppmann critique — understand limitations.

### Architecture Perspective

Redis locks are common — knowing limits is architect duty.

### Follow-up Questions

1. **Redlock algorithm? — Multi-master quorum — debated safety.**
2. **Lock without TTL? — Crashed holder blocks forever.**

### Common Mistakes in Interviews

- DEL lock_key without token check
- Single Redis instance claimed 'fully safe'
- Lock duration shorter than job runtime

---

## Q029: Consensus vs Coordination

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Consensus |
| **Frequency** | Occasional |

### Question

Distinguish consensus and coordination. Which does etcd provide?

### Short Answer (30 seconds)

Consensus: nodes agree on single value/ordering (Raft log). Coordination: broader — locks, leader election, config — may use consensus underneath.

### Detailed Answer (3–5 minutes)

**etcd provides both:**
- Consensus via Raft replicated log
- Coordination primitives: leases, watches, elections

**Examples:**
- **Consensus needed:** distributed config version, schema migration leader
- **Coordination only:** job scheduling lock, feature flag propagation

**Architect:** Don't build custom consensus — use etcd, Consul, or cloud leader election. Use consensus layer for correctness-critical state.

### Architecture Perspective

Precise vocabulary shows distributed systems depth.

### Follow-up Questions

1. **ZooKeeper znode? — Coordination primitive on top of ZAB consensus.**
2. **Why not roll your own Raft? — Subtle bugs — use battle-tested library.**

### Common Mistakes in Interviews

- Using database row lock as cluster consensus
- Confusing service discovery with consensus
- Custom leader election without fencing

---

## Q030: Phi Accrual Failure Detection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Reliability |
| **Frequency** | Occasional |

### Question

How does phi accrual failure detector differ from fixed heartbeat timeout?

### Short Answer (30 seconds)

Phi accrual adapts to network jitter — computes suspicion level (phi) from heartbeat arrival distribution. Fixed timeout false-positives on slow networks or false-negatives on fast failures.

### Detailed Answer (3–5 minutes)

**Concept:** Model heartbeat inter-arrival times; phi rises as time since last heartbeat exceeds expected distribution. Threshold triggers suspect → failed.

**Used in:** Akka, Cassandra (phi accrual influenced failure detection).

**Architect:** Tune suspicion thresholds — aggressive = flapping failover; lenient = slow detection. Pair with hysteresis (N consecutive failures).

### Architecture Perspective

Adaptive failure detection reduces false failover.

### Follow-up Questions

1. **Fixed 5s heartbeat timeout problems? — Jitter causes false positives at scale.**
2. **Suspect vs failed state? — Suspect: probe more; failed: trigger failover.**

### Common Mistakes in Interviews

- Single missed heartbeat triggers failover
- No hysteresis on flapping node
- Failure detection without considering GC pauses

---
