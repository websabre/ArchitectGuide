# Messaging & Event-Driven Architecture at Scale

> **Week 35** | **Module:** [caching-messaging](../../../modules/caching-messaging/README.md)

## 1. Messaging System Comparison

| System | Throughput | Ordering | Retention | Best For |
|--------|------------|----------|-----------|----------|
| **Kafka** | Millions/sec | Per partition | Days/weeks | Event streaming, log |
| **RabbitMQ** | Thousands/sec | Queue order | Until consumed | Task queues, routing |
| **Azure Service Bus** | Thousands/sec | Sessions | TTL-based | Enterprise .NET |
| **Amazon SQS** | Unlimited* | FIFO option | 14 days | AWS decoupling |
| **Amazon SNS** | High | None | N/A | Fan-out |

---

## 2. Event-Driven vs Event-Carried State Transfer

**Event notification:** "Order 123 was placed" — consumer calls API for details.

**Event-carried state transfer:** Event includes full order data — no callback needed.

**Trade-off:** Larger messages vs fewer sync calls.

---

## 3. Event Sourcing (Awareness)

Store state as sequence of events, not current state.

```
OrderCreated → LineItemAdded → PaymentReceived → OrderConfirmed
```

**Pros:** Audit trail, temporal queries, replay.
**Cons:** Complexity, eventual consistency, learning curve.

**Architect:** Use for audit-critical domains (finance). Skip for simple CRUD.

---

## 4. CQRS at Scale

```
Commands → Write DB (normalized)
              ↓ events
         Read DB (denormalized projections)
Queries ← Read DB
```

**Example:** Order write to SQL. `OrderSummary` projection to Elasticsearch for search.

---

## 5. Kafka Architecture (Interview Favorite)

| Concept | Description |
|---------|-------------|
| **Topic** | Category of messages |
| **Partition** | Ordered log shard |
| **Offset** | Position in partition |
| **Consumer Group** | Competing consumers share work |
| **Broker** | Kafka server |

**Partition key:** Same key → same partition → ordering guaranteed.

**Retention:** Replay capability — consumers can re-read history.

---

## 6. Dead Letter Queue Pattern

Failed messages after N retries → DLQ → alert → manual replay or fix.

**Architect mandate:** Every async system has DLQ monitoring.

**Next:** Week 36 Capstone designs
