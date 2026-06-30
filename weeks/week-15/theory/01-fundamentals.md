# Azure Integration & Messaging

## Service Comparison
| Service | Pattern | Use Case |
|---------|---------|----------|
| **Service Bus** | Queue/Topic | Enterprise messaging, transactions |
| **Event Grid** | Pub/sub (push) | Event routing, reactive |
| **Event Hubs** | Streaming | High-throughput ingestion |
| **Logic Apps** | Workflow | Low-code integration |
| **API Management** | API Gateway | Rate limit, auth, versioning |

## Service Bus
- Queues: point-to-point
- Topics: pub/sub with subscriptions
- Sessions for ordered processing
- Dead letter queues
- Duplicate detection

## Event Grid
- Event-driven, push model
- System topics (Azure resource events)
- Custom topics for app events
- Event-driven architecture foundation

## Enterprise Integration Patterns
- Message Router, Content-Based Router
- Aggregator, Splitter
- Claim Check (large payload in blob)

## Architect Deep Dive: Messaging Selection

### Service Bus vs Event Grid vs Event Hubs
| Service | Pattern | Example |
|---------|---------|---------|
| Service Bus | Commands, workflows, ordering | `ProcessOrder` queue |
| Event Grid | Reactive notifications | Blob created → trigger Function |
| Event Hubs | High-volume event stream | Clickstream, IoT ingress |

### Reliability trio
1. **Outbox** — atomic DB write + message intent
2. **Idempotent consumer** — `messageId` dedup table
3. **DLQ** — poison messages isolated with alert

### At-least-once reality
Design every handler to be idempotent — exactly-once is a myth without distributed transactions you should avoid.

