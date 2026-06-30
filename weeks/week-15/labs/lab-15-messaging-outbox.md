# Lab 15: Service Bus, Event Grid & Outbox Pattern

| **Week** | 15 | **Duration** | 120 min |

## Objectives
- [ ] Create Service Bus queue and topic
- [ ] Trigger Function from Event Grid blob event
- [ ] Implement Outbox pattern in .NET order service
- [ ] Handle dead letter queue

## Steps

### 1. Service Bus
```bash
az servicebus namespace create --name sb-archlab-$RANDOM --resource-group rg-architect-lab-09 --sku Standard
az servicebus queue create --namespace-name <sb> --resource-group rg-architect-lab-09 --name order-created
az servicebus topic create --namespace-name <sb> --resource-group rg-architect-lab-09 --name order-events
az servicebus topic subscription create --namespace-name <sb> --resource-group rg-architect-lab-09 \
  --topic-name order-events --name notification-service
```

### 2. Event Grid System Topic (Storage)
```bash
az eventgrid system-topic create --name eg-blob --resource-group rg-architect-lab-09 \
  --source /subscriptions/<sub>/resourceGroups/rg-architect-lab-09/providers/Microsoft.Storage/storageAccounts/<storage> \
  --topic-type Microsoft.Storage.StorageAccounts
```

### 3. Outbox Table + Worker
```csharp
// Same transaction: save Order + OutboxMessage
public class OutboxMessage
{
    public Guid Id { get; set; }
    public string Type { get; set; } = "";
    public string Payload { get; set; } = "";
    public DateTime CreatedAt { get; set; }
    public bool Processed { get; set; }
}
// Background worker polls outbox, publishes to Service Bus, marks processed
```

### 4. Idempotent Consumer
```csharp
// Store MessageId in ProcessedMessages table with unique constraint
```

### 5. DLQ Monitoring
Send poison message (invalid JSON). Verify DLQ. Document replay procedure.

## Architect Report
1. Service Bus vs Event Grid for order-created event?
2. Draw event-driven order flow with Outbox
3. How idempotency + at-least-once delivery work together
