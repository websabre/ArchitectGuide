# Lab 35: Transactional Outbox Pattern

| **Week** | 35 | **Duration** | 120 min |

## Objectives

- [ ] Implement outbox table in EF Core
- [ ] Background worker publishes to message bus
- [ ] Verify atomic order create + event publish

## Schema

```csharp
public class OutboxMessage
{
    public Guid Id { get; set; }
    public string Type { get; set; } = "";
    public string Payload { get; set; } = "";
    public DateTime CreatedAt { get; set; }
    public DateTime? ProcessedAt { get; set; }
}
```

## Flow

1. `SaveChanges` writes Order + OutboxMessage in same transaction
2. `OutboxProcessor` polls unprocessed messages
3. Publish to Service Bus / in-memory queue for lab
4. Mark `ProcessedAt`

## Chaos Test

Kill publisher mid-batch — messages must not duplicate on retry (use message Id dedup).

## Report

1. Outbox vs dual-write — why outbox wins
2. Polling vs log-based (Debezium) outbox
3. Link to [Week 15 messaging theory](../theory/01-fundamentals.md)
