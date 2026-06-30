# Azure Integration — Intermediate

> **Week 15** | **Level:** Intermediate

## Messaging Service Selection

| Pattern | Service |
|---------|---------|
| Queue (point-to-point) | Service Bus Queue |
| Pub/sub with topics | Service Bus Topic |
| Event routing (reactive) | Event Grid |
| High-volume streaming | Event Hubs |
| Orchestration | Logic Apps / Durable Functions |

## Service Bus vs Event Hubs

- **Service Bus:** Orders, commands, lower volume, sessions, transactions
- **Event Hubs:** Telemetry, clickstreams, millions of events/sec

## Idempotency and Duplicate Detection

- MessageId + duplicate detection window (Service Bus)
- Idempotent consumers with business key dedup table
- Outbox pattern for DB + message atomicity



## Architect Deep Dive: Integration Patterns

### Saga on Azure
Choreography: OrderPlaced event → Inventory + Payment subscribers. Orchestration: Durable Functions or Logic Apps for visual workflows with compensation.

### APIM as integration hub
External partners connect via APIM — throttling, JWT, request transformation — backend microservices stay private on VNet.

**Next:** [03-advanced.md](03-advanced.md)
