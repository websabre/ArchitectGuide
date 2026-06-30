# Week 35 — Intermediate Q&A

> Q031–Q070: Premium format (Week 1 quality).

---


## Q031: Message Queue vs Event Stream

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Messaging |
| **Frequency** | Very Common |

### Question

SQS vs Kafka — when each?

### Short Answer (30 seconds)

SQS: simple queue, consumer deletes message, lower ops. Kafka: log, replay, high throughput, stream processing, ordering per partition.

### Detailed Answer (3–5 minutes)

Order processing: SQS fine. Clickstream analytics: Kafka. Azure: Service Bus vs Event Hubs mirrors this split.

### Architecture Perspective

Right messaging tech avoids re-architecture later.

### Follow-up Questions

1. **Ordering guarantee? — Kafka partition key; Service Bus sessions.**
2. **Poison message? — DLQ after maxReceiveCount.**

### Common Mistakes in Interviews

- Kafka for 10 messages/day
- SQS when need replay history
- No DLQ configured

---

## Q032: At-Least-Once Delivery

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Semantics |
| **Frequency** | Very Common |

### Question

Design consumer for at-least-once messaging.

### Short Answer (30 seconds)

Idempotent handler + business key dedup store. Ack message only after successful processing. Store processed message IDs.

### Detailed Answer (3–5 minutes)

Duplicate delivery normal — not exceptional. `ProcessedEvents` table with unique `messageId`.

Outbox publisher also at-least-once — consumers must cope.

### Architecture Perspective

Semantic understanding separates architect from beginner.

### Follow-up Questions

1. **Exactly-once illusion? — Say effectively-once via idempotency.**
2. **Ordering + duplicates? — Handle out-of-order with version numbers.**

### Common Mistakes in Interviews

- Assume one delivery only
- Ack before processing completes
- No dedup on consumer

---

## Q033: Event Choreography

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Events |
| **Frequency** | Common |

### Question

OrderPlaced event — who listens?

### Short Answer (30 seconds)

Inventory, Payment, Notification services subscribe independently. No central orchestrator. Risk: hard to see global flow — use distributed tracing.

### Detailed Answer (3–5 minutes)

Choreography: loose coupling. Add process manager view in observability dashboard documenting event flow.

Compensation via compensating events — PaymentFailed → ReleaseInventory.

### Architecture Perspective

Choreography suits simple flows — document event catalog.

### Follow-up Questions

1. **Event schema registry? — Confluent/Azure Schema Registry — evolution governance.**
2. **Circular events? — Design dead letter — detect cycles.**

### Common Mistakes in Interviews

- God orchestrator in monolith ESB
- No event documentation
- Synchronous chain disguised as events

---

## Q034: Outbox and Inbox

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Patterns |
| **Frequency** | Very Common |

### Question

Pair outbox with inbox pattern?

### Short Answer (30 seconds)

Outbox: reliable publish from producer. Inbox: consumer deduplicates incoming `messageId` before processing — together effectively-once.

### Detailed Answer (3–5 minutes)

Producer TX → outbox. Consumer: insert inbox record → process → mark done — same messageId unique constraint prevents duplicate processing.

### Architecture Perspective

Inbox completes reliability story.

### Follow-up Questions

1. **Shared inbox table per service? — Yes — local to consumer DB.**
2. **Outbox relay failure? — Retry with backoff — monitor lag.**

### Common Mistakes in Interviews

- Consumer without dedup
- Outbox without transactional insert
- At-most-once ack too early

---

## Q035: Service Bus Sessions

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Azure Messaging |
| **Frequency** | Common |

### Question

When use Service Bus sessions?

### Short Answer (30 seconds)

Ordered processing per session key — e.g., all events for `orderId` processed in sequence by one consumer at a time.

### Detailed Answer (3–5 minutes)

SessionId = orderId. One consumer holds session lock — sequential processing.

Trade-off: less parallelism per session — hot session bottleneck.

### Architecture Perspective

Sessions solve ordering without Kafka.

### Follow-up Questions

1. **Max concurrent sessions? — Tune for throughput vs ordering strictness.**
2. **Session lock lost? — Message redelivered — handler idempotent.**

### Common Mistakes in Interviews

- Sessions for all messages unnecessarily
- Hot session single consumer bottleneck unmitigated
- No session timeout handling

---

## Q036: Event Schema Evolution

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

Add field to OrderPlaced event — safe rollout?

### Short Answer (30 seconds)

Additive changes only in v1 — new optional field. Consumers ignore unknown fields. Breaking change → new event type or version `OrderPlacedV2`.

### Detailed Answer (3–5 minutes)

Schema registry compatibility: backward compatible readers. Deploy consumers before producers or vice versa per compatibility rule.

### Architecture Perspective

Event contracts are API contracts — version them.

### Follow-up Questions

1. **Envelope pattern? — `{ metadata, payload }` — version in metadata.**
2. **JSON vs Avro/Protobuf? — Binary schemas enforce compatibility better.**

### Common Mistakes in Interviews

- Breaking rename without version
- No schema registry
- Deploy producer breaking consumers

---

## Q037: Dead Letter Queue

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reliability |
| **Frequency** | Very Common |

### Question

Message fails 5 times — what happens?

### Short Answer (30 seconds)

Moves to DLQ. Alert on DLQ depth. Manual or automated replay after fix. Root cause: poison schema, bug, or bad data.

### Detailed Answer (3–5 minutes)

DLQ dashboard + runbook. Never infinite retry — blocks queue.

Sample DLQ messages to staging for debug.

### Architecture Perspective

DLQ is operational necessity — architect specifies in design.

### Follow-up Questions

1. **DLQ replay tool? — Script re-publish with same idempotency keys.**
2. **Alert threshold? — Any DLQ message > 0 for payment queue.**

### Common Mistakes in Interviews

- Infinite retry loop
- DLQ messages auto-deleted
- No alert on DLQ growth

---

## Q038: Pub/Sub vs Point-to-Point

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Patterns |
| **Frequency** | Common |

### Question

Notification to email SMS push — pattern?

### Short Answer (30 seconds)

Pub/sub topic — each channel subscriber independent. Point-to-point queue if exactly one worker must process job.

### Detailed Answer (3–5 minutes)

Topic: OrderPlaced → [EmailSub, SmsSub, PushSub]. Competing consumers on queue for work distribution.

### Architecture Perspective

Pattern choice affects scaling and semantics.

### Follow-up Questions

1. **Fan-out cost? — N subscribers × message size — budget.**
2. **Filtering? — Subscription filters on attributes — avoid wrong delivery.**

### Common Mistakes in Interviews

- Queue when need broadcast
- Topic when need single consumer
- No subscription error handling

---

## Q039: Event-Driven Microservices Integration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Architecture |
| **Frequency** | Very Common |

### Question

Sync API vs event between order and inventory?

### Short Answer (30 seconds)

Reserve inventory: sync if user waits at checkout. Low stock alert: async event. Replenish warehouse: async.

### Detailed Answer (3–5 minutes)

User-facing latency dictates sync. Everything else event-driven for resilience.

Never 30s sync HTTP chain — use async + polling/WebSocket for status.

### Architecture Perspective

Integration style follows user wait time.

### Follow-up Questions

1. **Eventual notification UX? — WebSocket push when async completes.**
2. **Saga via events? — Choreographed saga — document compensation events.**

### Common Mistakes in Interviews

- All sync between all services
- All async for user-blocking path
- No correlation ID on events

---

## Q040: Messaging Cost and Ops

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

Service Bus premium vs Kafka self-hosted TCO?

### Short Answer (30 seconds)

Service Bus: low ops, per-message cost. Kafka: high ops (cluster management), lower marginal message cost at huge volume.

### Detailed Answer (3–5 minutes)

Break-even depends on volume and team skills. Architect includes engineer time in TCO.

Start managed — migrate to Kafka if message volume forces it.

### Architecture Perspective

Build vs buy applies to messaging infrastructure.

### Follow-up Questions

1. **Serverless consumption plan? — Azure Service Bus premium for predictable latency.**
2. **Message size limit? — Large payloads → blob storage + event reference.**

### Common Mistakes in Interviews

- Kafka for low volume — ops waste
- Ignore ops cost in TCO
- Large payload in message body

---

## Q041: At-Least-Once Semantics Explained

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Semantics |
| **Frequency** | Very Common |

### Question

Why is at-least-once the practical default for distributed messaging?

### Short Answer (30 seconds)

Networks, crashes, and ack timing make exactly-once delivery impossible without cooperation. Broker redelivers if ack lost — consumer may see duplicate — design idempotent handlers.

### Detailed Answer (3–5 minutes)

**Guarantees:** At-most-once (fire forget, may lose). At-least-once (no loss, duplicates). Effectively-once (at-least-once + idempotency).

**Examples:** Kafka, SQS, Service Bus default to at-least-once with ack.

**Architect language:** Say 'we achieve effectively-once via idempotent consumer' not 'exactly-once'.

### Architecture Perspective

Semantic precision is messaging interview baseline.

### Follow-up Questions

1. **Kafka exactly-once? — Transactional producer + idempotent consumer — bounded scope.**
2. **Ordering + at-least-once? — Duplicates may arrive out of order — version handling.**

### Common Mistakes in Interviews

- Assume broker delivers exactly once
- Ack before processing complete
- No dedup strategy documented

---

## Q042: The Exactly-Once Myth

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Semantics |
| **Frequency** | Very Common |

### Question

Interviewer asks for exactly-once payment processing. Respond?

### Short Answer (30 seconds)

Acknowledge end-to-end exactly-once is impossible across heterogeneous systems. Propose effectively-once: idempotent payment API + unique business key + dedup store + outbox.

### Detailed Answer (3–5 minutes)

**Layers:** DB TX exactly-once within one database. Cross-service: saga + idempotency keys.

**Kafka EOS:** Exactly-once within Kafka streams pipeline — not your credit card processor.

**Honest architect:** Name the boundary where guarantee holds and where idempotency takes over.

### Architecture Perspective

Calling out the myth shows seniority — don't pretend magic broker flag.

### Follow-up Questions

1. **Two-phase commit across microservices? — Avoid — operational pain.**
2. **Idempotency key storage? — Unique constraint on `paymentIdempotencyKey`.**

### Common Mistakes in Interviews

- Claim exactly-once because Kafka flag enabled
- Distributed 2PC for all microservices
- No idempotency on payment handler

---

## Q043: Dead Letter Queue Operations

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reliability |
| **Frequency** | Very Common |

### Question

Design operational runbook for DLQ depth > 100 messages.

### Short Answer (30 seconds)

Alert on-call → sample 5 messages → classify: poison (bad schema), transient (downstream), bug. Fix root cause → replay tool re-publishes with same idempotency key → monitor DLQ drain.

### Detailed Answer (3–5 minutes)

**Dashboards:** DLQ depth, age of oldest message, rate in vs out.

**Access control:** DLQ may contain PII — restrict replay tool.

**Automation:** Auto-replay transient after dependency healthy — manual approval for poison schema.

### Architecture Perspective

DLQ ops separate toy design from production-ready messaging.

### Follow-up Questions

1. **DLQ per queue? — Payment DLQ pages immediately; analytics DLQ daily review.**
2. **Retention? — DLQ messages retained 14 days — compliance.**

### Common Mistakes in Interviews

- DLQ messages deleted without analysis
- No replay tooling
- Infinite retry instead of DLQ

---

## Q044: Poison Message Handling

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reliability |
| **Frequency** | Very Common |

### Question

Message crashes consumer every time — poison pill. Architecture response?

### Short Answer (30 seconds)

Max delivery count (SQS `maxReceiveCount: 5`) → route to DLQ. Circuit breaker stop consuming queue until fix deployed. Schema validation reject before handler.

### Detailed Answer (3–5 minutes)

**Detection:** Same `messageId` in DLQ repeatedly after replay — classify poison.

**Quarantine:** Move to poison store for manual inspection — don't block entire queue.

**Prevention:** Contract tests on schema before deploy.

### Architecture Perspective

Poison messages happen — architecture includes ejection not infinite loop.

### Follow-up Questions

1. **Skip poison without DLQ? — Lose message — unacceptable for payments.**
2. **Canary consumer? — New version processes 1% traffic first.**

### Common Mistakes in Interviews

- Infinite retry on same message
- No maxReceiveCount configured
- Replay poison without code fix

---

## Q045: Outbox Relay Worker Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Patterns |
| **Frequency** | Very Common |

### Question

Design outbox relay: poll interval, failure handling, ordering.

### Short Answer (30 seconds)

Relay polls `Outbox` table `WHERE published_at IS NULL` batch 100. Publish to broker → mark published in same TX or follow-up TX with idempotent publish ID.

### Detailed Answer (3–5 minutes)

**Polling vs CDC:** Debezium/Logic Apps trigger on insert — lower latency than 1s poll.

**Failure:** Publish succeeds, mark fails → duplicate on retry — consumers idempotent.

**Ordering:** Per-aggregate sequence in outbox — relay preserves order for same `aggregateId`.

### Architecture Perspective

Outbox relay is critical path — design for failure not happy path.

### Follow-up Questions

1. **Relay lag metric? — `now() - min(unpublished.created_at)` — alert > 30s.**
2. **Multiple relay instances? — `SELECT FOR UPDATE SKIP LOCKED` — no duplicate publish.**

### Common Mistakes in Interviews

- Dual write API and broker without outbox
- Single-thread relay bottleneck unscaled
- No lag monitoring on outbox

---

## Q046: Inbox Pattern for Consumers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Patterns |
| **Frequency** | Very Common |

### Question

Implement inbox pattern on order consumer.

### Short Answer (30 seconds)

BEGIN TX → insert `Inbox(messageId)` unique → if conflict skip (duplicate) → process business logic → mark processed → COMMIT. Ack broker after TX commit.

### Detailed Answer (3–5 minutes)

**Effectively-once:** Same `messageId` cannot process twice — DB constraint enforces.

**Cleanup:** Archive processed inbox rows > 7 days.

**Pair with outbox:** Producer outbox + consumer inbox = robust cross-service.

### Architecture Perspective

Inbox completes the consumer side of reliable messaging.

### Follow-up Questions

1. **Inbox same DB as business data? — Yes — same TX boundary.**
2. **Ack before commit? — Message lost if crash after ack — ack after commit.**

### Common Mistakes in Interviews

- Process then check duplicate
- Ack before DB commit
- Inbox without unique constraint on messageId

---

## Q047: Event Choreography Walkthrough

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Events |
| **Frequency** | Common |

### Question

Choreograph `OrderPlaced` across inventory, payment, shipping without orchestrator.

### Short Answer (30 seconds)

`OrderPlaced` → Inventory reserves → `InventoryReserved` → Payment charges → `PaymentCaptured` → Shipping labels → `OrderShipped`. Failures emit compensating events.

### Detailed Answer (3–5 minutes)

**Pros:** Loose coupling, services autonomous. **Cons:** Hard to visualize — need event catalog diagram.

**Compensation:** `PaymentFailed` → `InventoryReleased` listener.

**Observability:** CorrelationId on every event — distributed trace across choreography.

### Architecture Perspective

Choreography example shows you can narrate multi-step flows.

### Follow-up Questions

1. **Circular dependency? — Event cycle detection in CI catalog review.**
2. **Timeout? — `OrderPlacementExpired` after 30 min no payment.**

### Common Mistakes in Interviews

- Hidden orchestrator in monolith
- No compensation events defined
- Missing correlation ID

---

## Q048: Saga Orchestration on Azure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Saga |
| **Frequency** | Common |

### Question

Implement orchestrated saga for checkout on Azure.

### Short Answer (30 seconds)

Durable Functions orchestrator: call Inventory → Payment → Shipping activity functions. Built-in compensation handlers on failure. State persisted in orchestration history.

### Detailed Answer (3–5 minutes)

**vs Service Bus sessions choreography:** Orchestrator central visibility — easier debug.

**Timeout:** Orchestration timeout 30 min — auto compensate.

**Idempotency:** Each activity checks idempotency key before side effect.

### Architecture Perspective

Azure architects should know Durable Functions as saga engine option.

### Follow-up Questions

1. **Logic Apps for saga? — Low-code alternative — simpler flows.**
2. **Human approval step? — External event wait in orchestrator.**

### Common Mistakes in Interviews

- Choreography when team needs central visibility
- No compensation in orchestrator
- Orchestrator calls HTTP sync chain 30s each

---

## Q049: Message Ordering Keys

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Ordering |
| **Frequency** | Common |

### Question

Guarantee order of status updates per `orderId` — how?

### Short Answer (30 seconds)

Partition key = `orderId` (Kafka) or Service Bus session = `orderId`. Single consumer per partition/session processes sequentially.

### Detailed Answer (3–5 minutes)

**Trade-off:** Hot `orderId` with flood of updates — single consumer bottleneck — acceptable for order state machine.

**Global order:** Not needed — per-aggregate order sufficient.

**Out-of-order detection:** `version` field — ignore stale.

### Architecture Perspective

Ordering keys scope parallelism correctly in messaging design.

### Follow-up Questions

1. **Kafka partition count? — More partitions more parallelism — order only within partition.**
2. **Reorder buffer? — Small heap wait for gap fill — adds latency.**

### Common Mistakes in Interviews

- Require global total order
- Random partition key for related events
- No version on status events

---

## Q050: Kafka Partition Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kafka |
| **Frequency** | Common |

### Question

Choose partition count and key for clickstream topic: 100K events/sec.

### Short Answer (30 seconds)

Partition key = `userId` — user session events ordered. Partition count ≥ max consumer parallelism — start 48–96, scale with throughput. Avoid key skew — monitor per-partition bytes/sec.

### Detailed Answer (3–5 minutes)

**Rule of thumb:** Target 10–50 MB/s per partition. 100K small events/sec → many partitions.

**Rebalance:** Add partitions — existing keys may move — plan consumer rebalance.

**Compacted topic:** Config changes — key = config name — one value per key.

### Architecture Perspective

Partition strategy directly caps throughput and ordering scope.

### Follow-up Questions

1. **Too few partitions? — Consumer idle — cannot scale past partition count.**
2. **Hot key skew? — Salt key for writes — accept order loss on salted sub-key.**

### Common Mistakes in Interviews

- Single partition for 'simplicity'
- Partition = consumer always false
- Never monitor partition skew

---

## Q051: Schema Registry with Avro

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

Why Avro + Schema Registry for event platform?

### Short Answer (30 seconds)

Avro binary compact with embedded schema ID. Registry enforces backward/forward compatibility. Producers register schema v3 — consumers with v2 reader still work if compatible.

### Detailed Answer (3–5 minutes)

**Azure:** Event Hubs with Schema Registry preview / Confluent on AKS.

**Compatibility modes:** BACKWARD (new schema, old reader) — default for consumers-first deploy.

**vs JSON:** Enforced contract — breaking changes caught in CI not production.

### Architecture Perspective

Schema registry is governance for event-driven architecture at scale.

### Follow-up Questions

1. **Subject naming? — `order-value` per topic value schema.**
2. **Delete schema? — Soft delete — old messages still reference ID.**

### Common Mistakes in Interviews

- Unversioned JSON events in production
- Breaking field rename without version bump
- Deploy producer before consumer on backward incompatible change

---

## Q052: CloudEvents Envelope Standard

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Standards |
| **Frequency** | Occasional |

### Question

Wrap domain events in CloudEvents — what fields and why?

### Short Answer (30 seconds)

Required: `id`, `source`, `specversion`, `type`, `time`. Optional: `datacontenttype`, `subject`, `data`. Enables uniform routing, logging, and cross-cloud tooling.

### Detailed Answer (3–5 minutes)

**Example:**
```json
{"specversion":"1.0","type":"com.shop.order.placed","source":"/orders","id":"uuid","data":{...}}
```

**Benefits:** Azure Event Grid native support, observability filters on `type`.

### Architecture Perspective

Standards literacy shows maturity in event platform design.

### Follow-up Questions

1. **CloudEvents vs custom envelope? — Standard wins multi-team integration.**
2. **Binary mode? — HTTP headers carry metadata — smaller body.**

### Common Mistakes in Interviews

- Bare JSON blob no metadata
- Duplicate `id` across events
- No `type` for router filtering

---

## Q053: Message Size Limits and Blob Reference

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Patterns |
| **Frequency** | Common |

### Question

Event payload is 5MB PDF — Service Bus limit 256KB. Pattern?

### Short Answer (30 seconds)

Upload blob to storage → event carries `{ blobUrl, contentType, checksum }` only. Consumer fetches blob on process. Claim check pattern.

### Detailed Answer (3–5 minutes)

**Limits:** SQS 256KB, Service Bus 256KB standard, Event Hubs 1MB. Kafka configurable ~1MB default.

**Security:** SAS token or managed identity on blob read — not public URL.

**Cleanup:** Lifecycle policy delete blob after consumer ack.

### Architecture Perspective

Large payload reference pattern is messaging essential.

### Follow-up Questions

1. **Compress then send? — May still exceed limit — blob reference safer.**
2. **Inline base64 5MB? — Blocks broker and consumers — anti-pattern.**

### Common Mistakes in Interviews

- 5MB in message body
- Public blob URL in event
- No blob cleanup after process

---

## Q054: Idempotent Consumer Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Patterns |
| **Frequency** | Very Common |

### Question

Design idempotent `PaymentCaptured` consumer.

### Short Answer (30 seconds)

Unique `messageId` in `ProcessedEvents` table. Business logic in TX: if already processed return success. Use natural idempotency: `UPDATE balance WHERE paymentId=X` idempotent.

### Detailed Answer (3–5 minutes)

**Levels:**
1. Message dedup (inbox)
2. Business key idempotency (paymentId)
3. State check (if status already Captured, skip)

**Ack:** Only after durable record of processing.

### Architecture Perspective

Idempotent consumer is non-negotiable for at-least-once brokers.

### Follow-up Questions

1. **Redis dedup set? — Faster than DB — TTL matches broker retention.**
2. **Partial failure? — TX rollback — message redelivered — safe retry.**

### Common Mistakes in Interviews

- Insert without unique constraint
- Side effect before dedup check
- Ack on receive not process

---

## Q055: Retry with Exponential Backoff

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Resilience |
| **Frequency** | Very Common |

### Question

Configure retry for transient downstream failure in message handler.

### Short Answer (30 seconds)

Retry 1: 1s, 2: 2s, 3: 4s, 4: 8s + jitter. Max 5 attempts → DLQ. Non-transient (400 validation) → DLQ immediately no retry.

### Detailed Answer (3–5 minutes)

**Jitter:** `delay * (0.5 + random())` — desynchronize consumers.

**Visibility timeout:** SQS visibility ≥ max processing time — else duplicate processing.

**Idempotency:** Required — retry causes duplicate attempts.

### Architecture Perspective

Retry policy is architect-specified not library default.

### Follow-up Questions

1. **Infinite retry? — Blocks queue — always cap.**
2. **Retry storm on outage? — Circuit breaker pause all retries.**

### Common Mistakes in Interviews

- Fixed 1s retry forever
- Retry on validation error
- No jitter — thundering herd on recovery

---

## Q056: Circuit Breaker in Messaging

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Resilience |
| **Frequency** | Common |

### Question

Payment service down — message consumers keep retrying. Circuit breaker design?

### Short Answer (30 seconds)

After 5 failures in 60s, open circuit — nack messages to queue with delay without calling payment. Half-open: probe one message. Close on success.

### Detailed Answer (3–5 minutes)

**Polly / custom:** Share circuit state across consumer instances via Redis.

**Queue growth:** Expected during outage — alert depth not false positive if circuit working.

**Bulkhead:** Separate consumer pool for payment vs notification.

### Architecture Perspective

Circuit breaker prevents retry storm amplifying outage.

### Follow-up Questions

1. **Fallback on open? — Queue for manual review — not fake success.**
2. **Health check endpoint? — Probe payment `/health` before half-open.**

### Common Mistakes in Interviews

- Tight retry loop hammers dead service
- Per-message circuit without shared state
- Circuit open drops messages

---

## Q057: Additive Event Versioning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

Evolve `OrderPlaced` v1 → v2 adding optional `loyaltyPoints` field.

### Short Answer (30 seconds)

Additive only — v2 consumers read v1 events (default 0 points). v1 consumers ignore unknown fields if using tolerant reader. Schema registry BACKWARD compatibility.

### Detailed Answer (3–5 minutes)

**Deploy order:** Register v2 schema → deploy consumers → deploy producers.

**Breaking change:** New event type `OrderPlacedV2` or new topic — parallel run migration.

### Architecture Perspective

Additive versioning is default safe evolution strategy.

### Follow-up Questions

1. **Remove field? — Breaking — new event type required.**
2. **Rename field? — Add new, deprecate old, dual-write transition.**

### Common Mistakes in Interviews

- Rename `amount` to `total` in place
- Required new field on old events
- No schema compatibility check in CI

---

## Q058: Pub/Sub vs Queue Decision Matrix

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Patterns |
| **Frequency** | Very Common |

### Question

Invoice generated — notify accounting (one consumer) and email (another). Pattern?

### Short Answer (30 seconds)

Pub/sub topic `InvoiceGenerated` — accounting subscription + email subscription independent. If accounting must process exactly once alone — dedicated queue for accounting, pub/sub for fan-out notifications.

### Detailed Answer (3–5 minutes)

**Queue:** Competing consumers, work distribution, one processor wins. **Pub/sub:** Broadcast, each subscriber gets copy.

**Hybrid:** Topic → subscriptions some queue-backed (Service Bus topics/subscriptions).

### Architecture Perspective

Pattern matrix prevents wrong semantics under load.

### Follow-up Questions

1. **Fan-out cost? — N subscribers × message size — FinOps aware.**
2. **Filter subscriptions? — `amount > 10000` routing — avoid wrong handlers.**

### Common Mistakes in Interviews

- Queue for email+SMS+push broadcast
- Pub/sub for job queue work distribution
- No dead letter on subscriptions

---

## Q059: Webhook Reliability Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Integration |
| **Frequency** | Common |

### Question

Your SaaS sends webhooks to customer endpoints — reliability design?

### Short Answer (30 seconds)

At-least-once delivery with signed payload, exponential retry 24h, DLQ for failed endpoints, customer idempotency via `eventId`, disable endpoint after 7 days failure.

### Detailed Answer (3–5 minutes)

**Security:** HMAC signature `X-Signature`, timestamp anti-replay.

**UX:** Customer dashboard shows delivery log, manual replay button.

**Ordering:** Per-customer sequence number — customer handles out-of-order.

### Architecture Perspective

Webhook design mirrors event platform consumer concerns in reverse.

### Follow-up Questions

1. **Stripe webhook pattern? — Reference implementation study.**
2. **Concurrent webhooks? — Limit per customer — don't DDoS their server.**

### Common Mistakes in Interviews

- Fire-and-forget single HTTP attempt
- No signature verification docs
- No endpoint health disable logic

---

## Q060: Async API SLA Definition

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SLA |
| **Frequency** | Common |

### Question

Define SLA for async `POST /reports` returning 202 Accepted.

### Short Answer (30 seconds)

202 immediately < 500ms. Report ready within 15 min p99. Status endpoint `GET /reports/{id}`. Webhook or poll when complete. Failed generation alert within 1 min.

### Detailed Answer (3–5 minutes)

**SLA components:** Acceptance latency, processing duration, availability of status API, delivery notification latency.

**User contract:** Document percentiles not averages.

**Overload:** 503 with `Retry-After` when queue > capacity — SLA excludes customer retry after 503.

### Architecture Perspective

Async APIs need processing SLA — not just HTTP response time.

### Follow-up Questions

1. **Cancellation SLA? — `DELETE /reports/{id}` stops job if not started.**
2. **Priority tiers? — Enterprise 5 min p99, free 60 min.**

### Common Mistakes in Interviews

- 202 with no processing time commitment
- No status endpoint
- SLA on average only hiding tail

---

## Q061: Event-Driven Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Messaging & Events |
| **Frequency** | Very Common |

### Question

Explain event-driven architecture for a system design or architecture interview.

### Short Answer (30 seconds)

Services communicate via events; loose coupling; async processing; eventual consistency.

### Detailed Answer (3–5 minutes)

**Event-Driven Architecture:**

Services communicate via events; loose coupling; async processing; eventual consistency.

**Production context (.NET/Azure):**
Apply in ASP.NET Core on Azure App Service or AKS with patterns from week 35.

**Key points:**
- When to use vs avoid
- Measurable outcome (latency, DORA, SLO)
- Common production pitfall and mitigation

**Example:** Instrument with Application Insights; track deployment in Azure DevOps.

**Architect:** Capture trade-offs in ADR when multiple valid approaches exist.

### Architecture Perspective

Event-Driven Architecture is foundational for week 35 — articulate clearly before tool names.

### Follow-up Questions

1. **How measure success? — Tie event-driven architecture to SLI, DORA metric, or business KPI.**
2. **Common anti-pattern? — Adopting tools before understanding event-driven architecture principles.**

### Common Mistakes in Interviews

- Define event-driven architecture with buzzwords only
- No concrete Azure/.NET example
- Cannot link concept to measurable outcome

---

## Q062: Kafka vs Service Bus

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Messaging & Events |
| **Frequency** | Very Common |

### Question

Explain kafka vs service bus for a system design or architecture interview.

### Short Answer (30 seconds)

Kafka: high-throughput log, replay. Service Bus: enterprise messaging, sessions, DLQ.

### Detailed Answer (3–5 minutes)

**Kafka vs Service Bus:**

Kafka: high-throughput log, replay. Service Bus: enterprise messaging, sessions, DLQ.

**Production context (.NET/Azure):**
Apply in ASP.NET Core on Azure App Service or AKS with patterns from week 35.

**Key points:**
- When to use vs avoid
- Measurable outcome (latency, DORA, SLO)
- Common production pitfall and mitigation

**Example:** Instrument with Application Insights; track deployment in Azure DevOps.

**Architect:** Capture trade-offs in ADR when multiple valid approaches exist.

### Architecture Perspective

Kafka vs Service Bus is foundational for week 35 — articulate clearly before tool names.

### Follow-up Questions

1. **How measure success? — Tie kafka vs service bus to SLI, DORA metric, or business KPI.**
2. **Common anti-pattern? — Adopting tools before understanding kafka vs service bus principles.**

### Common Mistakes in Interviews

- Define kafka vs service bus with buzzwords only
- No concrete Azure/.NET example
- Cannot link concept to measurable outcome

---

## Q063: Saga Pattern Purpose

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Messaging & Events |
| **Frequency** | Very Common |

### Question

Explain saga pattern purpose for a system design or architecture interview.

### Short Answer (30 seconds)

Distributed transaction across services; compensating actions on failure.

### Detailed Answer (3–5 minutes)

**Saga Pattern Purpose:**

Distributed transaction across services; compensating actions on failure.

**Production context (.NET/Azure):**
Apply in ASP.NET Core on Azure App Service or AKS with patterns from week 35.

**Key points:**
- When to use vs avoid
- Measurable outcome (latency, DORA, SLO)
- Common production pitfall and mitigation

**Example:** Instrument with Application Insights; track deployment in Azure DevOps.

**Architect:** Capture trade-offs in ADR when multiple valid approaches exist.

### Architecture Perspective

Saga Pattern Purpose is foundational for week 35 — articulate clearly before tool names.

### Follow-up Questions

1. **How measure success? — Tie saga pattern purpose to SLI, DORA metric, or business KPI.**
2. **Common anti-pattern? — Adopting tools before understanding saga pattern purpose principles.**

### Common Mistakes in Interviews

- Define saga pattern purpose with buzzwords only
- No concrete Azure/.NET example
- Cannot link concept to measurable outcome

---

## Q064: Outbox Pattern Reliability

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Messaging & Events |
| **Frequency** | Very Common |

### Question

Explain outbox pattern reliability for a system design or architecture interview.

### Short Answer (30 seconds)

Atomic DB write + outbox; relay publishes; no dual-write inconsistency.

### Detailed Answer (3–5 minutes)

**Outbox Pattern Reliability:**

Atomic DB write + outbox; relay publishes; no dual-write inconsistency.

**Production context (.NET/Azure):**
Apply in ASP.NET Core on Azure App Service or AKS with patterns from week 35.

**Key points:**
- When to use vs avoid
- Measurable outcome (latency, DORA, SLO)
- Common production pitfall and mitigation

**Example:** Instrument with Application Insights; track deployment in Azure DevOps.

**Architect:** Capture trade-offs in ADR when multiple valid approaches exist.

### Architecture Perspective

Outbox Pattern Reliability is foundational for week 35 — articulate clearly before tool names.

### Follow-up Questions

1. **How measure success? — Tie outbox pattern reliability to SLI, DORA metric, or business KPI.**
2. **Common anti-pattern? — Adopting tools before understanding outbox pattern reliability principles.**

### Common Mistakes in Interviews

- Define outbox pattern reliability with buzzwords only
- No concrete Azure/.NET example
- Cannot link concept to measurable outcome

---

## Q065: Idempotent Consumer

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Messaging & Events |
| **Frequency** | Very Common |

### Question

Explain idempotent consumer for a system design or architecture interview.

### Short Answer (30 seconds)

Same message processed once effect; messageId dedup table; safe at-least-once.

### Detailed Answer (3–5 minutes)

**Idempotent Consumer:**

Same message processed once effect; messageId dedup table; safe at-least-once.

**Production context (.NET/Azure):**
Apply in ASP.NET Core on Azure App Service or AKS with patterns from week 35.

**Key points:**
- When to use vs avoid
- Measurable outcome (latency, DORA, SLO)
- Common production pitfall and mitigation

**Example:** Instrument with Application Insights; track deployment in Azure DevOps.

**Architect:** Capture trade-offs in ADR when multiple valid approaches exist.

### Architecture Perspective

Idempotent Consumer is foundational for week 35 — articulate clearly before tool names.

### Follow-up Questions

1. **How measure success? — Tie idempotent consumer to SLI, DORA metric, or business KPI.**
2. **Common anti-pattern? — Adopting tools before understanding idempotent consumer principles.**

### Common Mistakes in Interviews

- Define idempotent consumer with buzzwords only
- No concrete Azure/.NET example
- Cannot link concept to measurable outcome

---

## Q066: Message Ordering Scope

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Messaging & Events |
| **Frequency** | Very Common |

### Question

Explain message ordering scope for a system design or architecture interview.

### Short Answer (30 seconds)

FIFO per partition/session/entity — not global across system.

### Detailed Answer (3–5 minutes)

**Message Ordering Scope:**

FIFO per partition/session/entity — not global across system.

**Production context (.NET/Azure):**
Apply in ASP.NET Core on Azure App Service or AKS with patterns from week 35.

**Key points:**
- When to use vs avoid
- Measurable outcome (latency, DORA, SLO)
- Common production pitfall and mitigation

**Example:** Instrument with Application Insights; track deployment in Azure DevOps.

**Architect:** Capture trade-offs in ADR when multiple valid approaches exist.

### Architecture Perspective

Message Ordering Scope is foundational for week 35 — articulate clearly before tool names.

### Follow-up Questions

1. **How measure success? — Tie message ordering scope to SLI, DORA metric, or business KPI.**
2. **Common anti-pattern? — Adopting tools before understanding message ordering scope principles.**

### Common Mistakes in Interviews

- Define message ordering scope with buzzwords only
- No concrete Azure/.NET example
- Cannot link concept to measurable outcome

---

## Q067: Dead Letter Queue Purpose

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Messaging & Events |
| **Frequency** | Common |

### Question

Explain dead letter queue purpose for a system design or architecture interview.

### Short Answer (30 seconds)

Poison messages isolated after max retries; manual triage; prevent block.

### Detailed Answer (3–5 minutes)

**Dead Letter Queue Purpose:**

Poison messages isolated after max retries; manual triage; prevent block.

**Production context (.NET/Azure):**
Apply in ASP.NET Core on Azure App Service or AKS with patterns from week 35.

**Key points:**
- When to use vs avoid
- Measurable outcome (latency, DORA, SLO)
- Common production pitfall and mitigation

**Example:** Instrument with Application Insights; track deployment in Azure DevOps.

**Architect:** Capture trade-offs in ADR when multiple valid approaches exist.

### Architecture Perspective

Dead Letter Queue Purpose is foundational for week 35 — articulate clearly before tool names.

### Follow-up Questions

1. **How measure success? — Tie dead letter queue purpose to SLI, DORA metric, or business KPI.**
2. **Common anti-pattern? — Adopting tools before understanding dead letter queue purpose principles.**

### Common Mistakes in Interviews

- Define dead letter queue purpose with buzzwords only
- No concrete Azure/.NET example
- Cannot link concept to measurable outcome

---

## Q068: At-Least-Once Delivery

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Messaging & Events |
| **Frequency** | Common |

### Question

Explain at-least-once delivery for a system design or architecture interview.

### Short Answer (30 seconds)

Default for most buses; design consumers idempotent; embrace not fight.

### Detailed Answer (3–5 minutes)

**At-Least-Once Delivery:**

Default for most buses; design consumers idempotent; embrace not fight.

**Production context (.NET/Azure):**
Apply in ASP.NET Core on Azure App Service or AKS with patterns from week 35.

**Key points:**
- When to use vs avoid
- Measurable outcome (latency, DORA, SLO)
- Common production pitfall and mitigation

**Example:** Instrument with Application Insights; track deployment in Azure DevOps.

**Architect:** Capture trade-offs in ADR when multiple valid approaches exist.

### Architecture Perspective

At-Least-Once Delivery is foundational for week 35 — articulate clearly before tool names.

### Follow-up Questions

1. **How measure success? — Tie at-least-once delivery to SLI, DORA metric, or business KPI.**
2. **Common anti-pattern? — Adopting tools before understanding at-least-once delivery principles.**

### Common Mistakes in Interviews

- Define at-least-once delivery with buzzwords only
- No concrete Azure/.NET example
- Cannot link concept to measurable outcome

---

## Q069: Event Schema Versioning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Messaging & Events |
| **Frequency** | Common |

### Question

Explain event schema versioning for a system design or architecture interview.

### Short Answer (30 seconds)

Additive changes backward compatible; breaking changes need new topic/version.

### Detailed Answer (3–5 minutes)

**Event Schema Versioning:**

Additive changes backward compatible; breaking changes need new topic/version.

**Production context (.NET/Azure):**
Apply in ASP.NET Core on Azure App Service or AKS with patterns from week 35.

**Key points:**
- When to use vs avoid
- Measurable outcome (latency, DORA, SLO)
- Common production pitfall and mitigation

**Example:** Instrument with Application Insights; track deployment in Azure DevOps.

**Architect:** Capture trade-offs in ADR when multiple valid approaches exist.

### Architecture Perspective

Event Schema Versioning is foundational for week 35 — articulate clearly before tool names.

### Follow-up Questions

1. **How measure success? — Tie event schema versioning to SLI, DORA metric, or business KPI.**
2. **Common anti-pattern? — Adopting tools before understanding event schema versioning principles.**

### Common Mistakes in Interviews

- Define event schema versioning with buzzwords only
- No concrete Azure/.NET example
- Cannot link concept to measurable outcome

---

## Q070: Competing Consumers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Messaging & Events |
| **Frequency** | Common |

### Question

Explain competing consumers for a system design or architecture interview.

### Short Answer (30 seconds)

Multiple workers same subscription; scale with partition count.

### Detailed Answer (3–5 minutes)

**Competing Consumers:**

Multiple workers same subscription; scale with partition count.

**Production context (.NET/Azure):**
Apply in ASP.NET Core on Azure App Service or AKS with patterns from week 35.

**Key points:**
- When to use vs avoid
- Measurable outcome (latency, DORA, SLO)
- Common production pitfall and mitigation

**Example:** Instrument with Application Insights; track deployment in Azure DevOps.

**Architect:** Capture trade-offs in ADR when multiple valid approaches exist.

### Architecture Perspective

Competing Consumers is foundational for week 35 — articulate clearly before tool names.

### Follow-up Questions

1. **How measure success? — Tie competing consumers to SLI, DORA metric, or business KPI.**
2. **Common anti-pattern? — Adopting tools before understanding competing consumers principles.**

### Common Mistakes in Interviews

- Define competing consumers with buzzwords only
- No concrete Azure/.NET example
- Cannot link concept to measurable outcome

---
