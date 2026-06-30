# Week 35 — Advanced Q&A

> Q071–Q100: Premium format (Week 1 quality).

---


## Q071: Kafka Partition Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Kafka |
| **Frequency** | Very Common |

### Question

How would you implement Kafka Partition Strategy with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Partition key = orderId for ordering; enough partitions for consumer parallelism.

### Detailed Answer (3–5 minutes)

**Kafka Partition Strategy** (Messaging context)

Partition key = orderId for ordering; enough partitions for consumer parallelism.

**Production implementation:**
```csharp
await using var tx = await _db.Database.BeginTransactionAsync();
await _db.Orders.AddAsync(order);
await _db.Outbox.AddAsync(new OutboxMessage(eventPayload));
await tx.CommitAsync();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Kafka Partition Strategy separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Kafka-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q072: Azure Service Bus Sessions

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Service Bus |
| **Frequency** | Very Common |

### Question

How would you implement Azure Service Bus Sessions with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

FIFO per sessionId; session lock; duplicate detection window.

### Detailed Answer (3–5 minutes)

**Azure Service Bus Sessions** (Messaging context)

FIFO per sessionId; session lock; duplicate detection window.

**Production implementation:**
```csharp
await using var tx = await _db.Database.BeginTransactionAsync();
await _db.Orders.AddAsync(order);
await _db.Outbox.AddAsync(new OutboxMessage(eventPayload));
await tx.CommitAsync();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Azure Service Bus Sessions separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Service Bus-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q073: Event-Driven Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Event-Driven |
| **Frequency** | Very Common |

### Question

How would you implement Event-Driven Architecture with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Domain events decouple services; event schema registry; versioned contracts.

### Detailed Answer (3–5 minutes)

**Event-Driven Architecture** (Messaging context)

Domain events decouple services; event schema registry; versioned contracts.

**Production implementation:**
```csharp
await using var tx = await _db.Database.BeginTransactionAsync();
await _db.Orders.AddAsync(order);
await _db.Outbox.AddAsync(new OutboxMessage(eventPayload));
await tx.CommitAsync();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Event-Driven Architecture separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Event-Driven-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q074: Saga Orchestration vs Choreography

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Saga |
| **Frequency** | Very Common |

### Question

How would you implement Saga Orchestration vs Choreography with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Orchestrator for complex flows; choreography for simple event chains — checkout example.

### Detailed Answer (3–5 minutes)

**Saga Orchestration vs Choreography** (Messaging context)

Orchestrator for complex flows; choreography for simple event chains — checkout example.

**Production implementation:**
```csharp
await using var tx = await _db.Database.BeginTransactionAsync();
await _db.Orders.AddAsync(order);
await _db.Outbox.AddAsync(new OutboxMessage(eventPayload));
await tx.CommitAsync();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Saga Orchestration vs Choreography separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Saga-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q075: Transactional Outbox Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Outbox |
| **Frequency** | Very Common |

### Question

How would you implement Transactional Outbox Pattern with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Same DB transaction for entity + outbox row; relay to Service Bus; idempotent consumers.

### Detailed Answer (3–5 minutes)

**Transactional Outbox Pattern** (Messaging context)

Same DB transaction for entity + outbox row; relay to Service Bus; idempotent consumers.

**Production implementation:**
```csharp
await using var tx = await _db.Database.BeginTransactionAsync();
await _db.Orders.AddAsync(order);
await _db.Outbox.AddAsync(new OutboxMessage(eventPayload));
await tx.CommitAsync();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Transactional Outbox Pattern separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Outbox-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q076: Idempotent Consumer Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Idempotency |
| **Frequency** | Very Common |

### Question

How would you implement Idempotent Consumer Design with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Processed message table with messageId; business idempotency key; at-least-once safe.

### Detailed Answer (3–5 minutes)

**Idempotent Consumer Design** (Messaging context)

Processed message table with messageId; business idempotency key; at-least-once safe.

**Production implementation:**
```csharp
await using var tx = await _db.Database.BeginTransactionAsync();
await _db.Orders.AddAsync(order);
await _db.Outbox.AddAsync(new OutboxMessage(eventPayload));
await tx.CommitAsync();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Idempotent Consumer Design separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Idempotency-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q077: Message Ordering Guarantees

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Messaging |
| **Frequency** | Very Common |

### Question

How would you implement Message Ordering Guarantees with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Order within partition/session only; design for out-of-order across partitions.

### Detailed Answer (3–5 minutes)

**Message Ordering Guarantees** (Messaging context)

Order within partition/session only; design for out-of-order across partitions.

**Production implementation:**
```csharp
await using var tx = await _db.Database.BeginTransactionAsync();
await _db.Orders.AddAsync(order);
await _db.Outbox.AddAsync(new OutboxMessage(eventPayload));
await tx.CommitAsync();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Message Ordering Guarantees separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Messaging-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q078: Dead Letter Queue Handling

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | DLQ |
| **Frequency** | Very Common |

### Question

How would you implement Dead Letter Queue Handling with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

DLQ monitor alert; replay tooling with audit; poison message quarantine.

### Detailed Answer (3–5 minutes)

**Dead Letter Queue Handling** (Messaging context)

DLQ monitor alert; replay tooling with audit; poison message quarantine.

**Production implementation:**
```csharp
await using var tx = await _db.Database.BeginTransactionAsync();
await _db.Orders.AddAsync(order);
await _db.Outbox.AddAsync(new OutboxMessage(eventPayload));
await tx.CommitAsync();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Dead Letter Queue Handling separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — DLQ-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q079: Event Schema Evolution

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Events |
| **Frequency** | Very Common |

### Question

How would you implement Event Schema Evolution with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Backward compatible additive fields; schema registry validation; reject breaking changes.

### Detailed Answer (3–5 minutes)

**Event Schema Evolution** (Messaging context)

Backward compatible additive fields; schema registry validation; reject breaking changes.

**Production implementation:**
```csharp
await using var tx = await _db.Database.BeginTransactionAsync();
await _db.Orders.AddAsync(order);
await _db.Outbox.AddAsync(new OutboxMessage(eventPayload));
await tx.CommitAsync();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Event Schema Evolution separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Events-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q080: Exactly-Once Semantics Reality

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Messaging |
| **Frequency** | Very Common |

### Question

How would you implement Exactly-Once Semantics Reality with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

True exactly-once rare; idempotent consumer + dedup = practical exactly-once effect.

### Detailed Answer (3–5 minutes)

**Exactly-Once Semantics Reality** (Messaging context)

True exactly-once rare; idempotent consumer + dedup = practical exactly-once effect.

**Production implementation:**
```csharp
await using var tx = await _db.Database.BeginTransactionAsync();
await _db.Orders.AddAsync(order);
await _db.Outbox.AddAsync(new OutboxMessage(eventPayload));
await tx.CommitAsync();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Exactly-Once Semantics Reality separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Messaging-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q081: Service Bus vs Event Hubs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Azure Messaging |
| **Frequency** | Very Common |

### Question

How would you implement Service Bus vs Event Hubs with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Service Bus: commands, sessions, DLQ. Event Hubs: high-throughput event stream, Kafka API.

### Detailed Answer (3–5 minutes)

**Service Bus vs Event Hubs** (Messaging context)

Service Bus: commands, sessions, DLQ. Event Hubs: high-throughput event stream, Kafka API.

**Production implementation:**
```csharp
await using var tx = await _db.Database.BeginTransactionAsync();
await _db.Orders.AddAsync(order);
await _db.Outbox.AddAsync(new OutboxMessage(eventPayload));
await tx.CommitAsync();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Service Bus vs Event Hubs separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Azure Messaging-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q082: Competing Consumers Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Messaging |
| **Frequency** | Very Common |

### Question

How would you implement Competing Consumers Scale with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Multiple consumers same subscription; partition count = max parallelism.

### Detailed Answer (3–5 minutes)

**Competing Consumers Scale** (Messaging context)

Multiple consumers same subscription; partition count = max parallelism.

**Production implementation:**
```csharp
await using var tx = await _db.Database.BeginTransactionAsync();
await _db.Orders.AddAsync(order);
await _db.Outbox.AddAsync(new OutboxMessage(eventPayload));
await tx.CommitAsync();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Competing Consumers Scale separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Messaging-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q083: Message Size Limits

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Messaging |
| **Frequency** | Very Common |

### Question

How would you implement Message Size Limits with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Large payload → blob storage reference in message; 256KB Service Bus limit.

### Detailed Answer (3–5 minutes)

**Message Size Limits** (Messaging context)

Large payload → blob storage reference in message; 256KB Service Bus limit.

**Production implementation:**
```csharp
await using var tx = await _db.Database.BeginTransactionAsync();
await _db.Orders.AddAsync(order);
await _db.Outbox.AddAsync(new OutboxMessage(eventPayload));
await tx.CommitAsync();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Message Size Limits separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Messaging-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q084: Scheduled Messages

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Service Bus |
| **Frequency** | Very Common |

### Question

How would you implement Scheduled Messages with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Delayed delivery for retry backoff; scheduled enqueue time.

### Detailed Answer (3–5 minutes)

**Scheduled Messages** (Messaging context)

Delayed delivery for retry backoff; scheduled enqueue time.

**Production implementation:**
```csharp
await using var tx = await _db.Database.BeginTransactionAsync();
await _db.Orders.AddAsync(order);
await _db.Outbox.AddAsync(new OutboxMessage(eventPayload));
await tx.CommitAsync();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Scheduled Messages separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Service Bus-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q085: Priority Queues Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Messaging |
| **Frequency** | Very Common |

### Question

How would you implement Priority Queues Pattern with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Separate queues OTP vs batch; never block critical on bulk.

### Detailed Answer (3–5 minutes)

**Priority Queues Pattern** (Messaging context)

Separate queues OTP vs batch; never block critical on bulk.

**Production implementation:**
```csharp
await using var tx = await _db.Database.BeginTransactionAsync();
await _db.Orders.AddAsync(order);
await _db.Outbox.AddAsync(new OutboxMessage(eventPayload));
await tx.CommitAsync();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Priority Queues Pattern separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Messaging-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q086: Event Sourcing vs Event-Driven

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Events |
| **Frequency** | Very Common |

### Question

How would you implement Event Sourcing vs Event-Driven with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

ES stores state as events; ED uses events for integration — different concerns.

### Detailed Answer (3–5 minutes)

**Event Sourcing vs Event-Driven** (Messaging context)

ES stores state as events; ED uses events for integration — different concerns.

**Production implementation:**
```csharp
await using var tx = await _db.Database.BeginTransactionAsync();
await _db.Orders.AddAsync(order);
await _db.Outbox.AddAsync(new OutboxMessage(eventPayload));
await tx.CommitAsync();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Event Sourcing vs Event-Driven separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Events-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q087: CQRS with Event Bus

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | CQRS |
| **Frequency** | Very Common |

### Question

How would you implement CQRS with Event Bus with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Write model publishes events; read models subscribe and project.

### Detailed Answer (3–5 minutes)

**CQRS with Event Bus** (Messaging context)

Write model publishes events; read models subscribe and project.

**Production implementation:**
```csharp
await using var tx = await _db.Database.BeginTransactionAsync();
await _db.Orders.AddAsync(order);
await _db.Outbox.AddAsync(new OutboxMessage(eventPayload));
await tx.CommitAsync();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

CQRS with Event Bus separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — CQRS-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q088: Poison Message Detection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | DLQ |
| **Frequency** | Very Common |

### Question

How would you implement Poison Message Detection with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Max delivery count 5 → DLQ; alert; manual triage workflow.

### Detailed Answer (3–5 minutes)

**Poison Message Detection** (Messaging context)

Max delivery count 5 → DLQ; alert; manual triage workflow.

**Production implementation:**
```csharp
await using var tx = await _db.Database.BeginTransactionAsync();
await _db.Orders.AddAsync(order);
await _db.Outbox.AddAsync(new OutboxMessage(eventPayload));
await tx.CommitAsync();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Poison Message Detection separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — DLQ-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q089: Message Correlation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Observability |
| **Frequency** | Very Common |

### Question

How would you implement Message Correlation with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

correlationId, causationId in message properties; trace across async boundary.

### Detailed Answer (3–5 minutes)

**Message Correlation** (Messaging context)

correlationId, causationId in message properties; trace across async boundary.

**Production implementation:**
```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(t => t.AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation())
    .UseAzureMonitor();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Message Correlation separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Observability-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q090: Bulkhead Queue Isolation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Messaging |
| **Frequency** | Very Common |

### Question

How would you implement Bulkhead Queue Isolation with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Separate namespace per domain; failure in analytics doesn't block orders.

### Detailed Answer (3–5 minutes)

**Bulkhead Queue Isolation** (Messaging context)

Separate namespace per domain; failure in analytics doesn't block orders.

**Production implementation:**
```csharp
await using var tx = await _db.Database.BeginTransactionAsync();
await _db.Orders.AddAsync(order);
await _db.Outbox.AddAsync(new OutboxMessage(eventPayload));
await tx.CommitAsync();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Bulkhead Queue Isolation separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Messaging-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q091: Kafka Consumer Group Rebalance

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Kafka |
| **Frequency** | Common |

### Question

How would you implement Kafka Consumer Group Rebalance with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Rebalance storm mitigation; cooperative sticky assignor; adequate partition count.

### Detailed Answer (3–5 minutes)

**Kafka Consumer Group Rebalance** (Messaging context)

Rebalance storm mitigation; cooperative sticky assignor; adequate partition count.

**Production implementation:**
```csharp
await using var tx = await _db.Database.BeginTransactionAsync();
await _db.Orders.AddAsync(order);
await _db.Outbox.AddAsync(new OutboxMessage(eventPayload));
await tx.CommitAsync();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Kafka Consumer Group Rebalance separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Kafka-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q092: Event Hub Capture Archive

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Event Hubs |
| **Frequency** | Common |

### Question

How would you implement Event Hub Capture Archive with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Auto-archive to ADLS for replay, audit, ML training pipeline.

### Detailed Answer (3–5 minutes)

**Event Hub Capture Archive** (Messaging context)

Auto-archive to ADLS for replay, audit, ML training pipeline.

**Production implementation:**
```csharp
await using var tx = await _db.Database.BeginTransactionAsync();
await _db.Orders.AddAsync(order);
await _db.Outbox.AddAsync(new OutboxMessage(eventPayload));
await tx.CommitAsync();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Event Hub Capture Archive separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Event Hubs-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q093: Saga Compensation Logic

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Saga |
| **Frequency** | Common |

### Question

How would you implement Saga Compensation Logic with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Payment succeeded, ship failed → refund idempotent with sagaId.

### Detailed Answer (3–5 minutes)

**Saga Compensation Logic** (Messaging context)

Payment succeeded, ship failed → refund idempotent with sagaId.

**Production implementation:**
```csharp
await using var tx = await _db.Database.BeginTransactionAsync();
await _db.Orders.AddAsync(order);
await _db.Outbox.AddAsync(new OutboxMessage(eventPayload));
await tx.CommitAsync();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Saga Compensation Logic separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Saga-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q094: Inbox Pattern Consumer

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Inbox |
| **Frequency** | Common |

### Question

How would you implement Inbox Pattern Consumer with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Consumer inbox table dedup before processing; pairs with outbox producer.

### Detailed Answer (3–5 minutes)

**Inbox Pattern Consumer** (Messaging context)

Consumer inbox table dedup before processing; pairs with outbox producer.

**Production implementation:**
```csharp
await using var tx = await _db.Database.BeginTransactionAsync();
await _db.Orders.AddAsync(order);
await _db.Outbox.AddAsync(new OutboxMessage(eventPayload));
await tx.CommitAsync();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Inbox Pattern Consumer separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Inbox-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q095: Message Encryption Transit

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Security |
| **Frequency** | Common |

### Question

How would you implement Message Encryption Transit with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

TLS 1.2+; Premium Service Bus private endpoint; CMK at rest.

### Detailed Answer (3–5 minutes)

**Message Encryption Transit** (Messaging context)

TLS 1.2+; Premium Service Bus private endpoint; CMK at rest.

**Production implementation:**
```csharp
await using var tx = await _db.Database.BeginTransactionAsync();
await _db.Orders.AddAsync(order);
await _db.Outbox.AddAsync(new OutboxMessage(eventPayload));
await tx.CommitAsync();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Message Encryption Transit separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Security-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q096: Event Replay Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Events |
| **Frequency** | Common |

### Question

How would you implement Event Replay Strategy with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Replay from offset with idempotent consumers; new consumer group for rebuild.

### Detailed Answer (3–5 minutes)

**Event Replay Strategy** (Messaging context)

Replay from offset with idempotent consumers; new consumer group for rebuild.

**Production implementation:**
```csharp
await using var tx = await _db.Database.BeginTransactionAsync();
await _db.Orders.AddAsync(order);
await _db.Outbox.AddAsync(new OutboxMessage(eventPayload));
await tx.CommitAsync();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Event Replay Strategy separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Events-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q097: Ordering vs Throughput Trade

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Messaging |
| **Frequency** | Common |

### Question

How would you implement Ordering vs Throughput Trade with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Global FIFO kills throughput — scope ordering to entity.

### Detailed Answer (3–5 minutes)

**Ordering vs Throughput Trade** (Messaging context)

Global FIFO kills throughput — scope ordering to entity.

**Production implementation:**
```csharp
await using var tx = await _db.Database.BeginTransactionAsync();
await _db.Orders.AddAsync(order);
await _db.Outbox.AddAsync(new OutboxMessage(eventPayload));
await tx.CommitAsync();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Ordering vs Throughput Trade separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Messaging-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q098: Azure Functions Service Bus Trigger

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Azure |
| **Frequency** | Common |

### Question

How would you implement Azure Functions Service Bus Trigger with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Prefetch count tuning; max concurrent calls; DLQ handling in function.

### Detailed Answer (3–5 minutes)

**Azure Functions Service Bus Trigger** (Messaging context)

Prefetch count tuning; max concurrent calls; DLQ handling in function.

**Production implementation:**
```csharp
await using var tx = await _db.Database.BeginTransactionAsync();
await _db.Orders.AddAsync(order);
await _db.Outbox.AddAsync(new OutboxMessage(eventPayload));
await tx.CommitAsync();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Azure Functions Service Bus Trigger separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Azure-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q099: CloudEvents Specification

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Events |
| **Frequency** | Common |

### Question

How would you implement CloudEvents Specification with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Standard envelope: type, source, id, time — interoperability across services.

### Detailed Answer (3–5 minutes)

**CloudEvents Specification** (Messaging context)

Standard envelope: type, source, id, time — interoperability across services.

**Production implementation:**
```csharp
await using var tx = await _db.Database.BeginTransactionAsync();
await _db.Orders.AddAsync(order);
await _db.Outbox.AddAsync(new OutboxMessage(eventPayload));
await tx.CommitAsync();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

CloudEvents Specification separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Events-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q100: Message Bus HA Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Messaging |
| **Frequency** | Common |

### Question

How would you implement Message Bus HA Design with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Zone-redundant namespace; geo-disaster pairing; documented RPO for messages.

### Detailed Answer (3–5 minutes)

**Message Bus HA Design** (Messaging context)

Zone-redundant namespace; geo-disaster pairing; documented RPO for messages.

**Production implementation:**
```csharp
await using var tx = await _db.Database.BeginTransactionAsync();
await _db.Orders.AddAsync(order);
await _db.Outbox.AddAsync(new OutboxMessage(eventPayload));
await tx.CommitAsync();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Message Bus HA Design separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Messaging-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---
