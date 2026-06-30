# Distributed Systems Fundamentals — Architect Lens

> **Week 21** | **Module:** [microservices-distributed-systems](../../../modules/microservices-distributed-systems/README.md)

## Learning Objectives
- Explain CAP and PACELC theorems with production examples
- Choose consistency models for business requirements
- Design for failure as the default state

---

## 1. CAP Theorem

**In a network partition, you must choose between Consistency and Availability.**

| Property | Meaning |
|----------|---------|
| **Consistency** | Every read receives the most recent write or error |
| **Availability** | Every request receives a non-error response |
| **Partition tolerance** | System continues despite network failures between nodes |

**Reality:** Partitions happen. So you choose CP or AP during partition.

| Choice | Example | Use Case |
|--------|---------|----------|
| **CP** | HBase, MongoDB (strong), ZooKeeper | Banking ledger, inventory deduction |
| **AP** | Cassandra, DynamoDB (eventual), DNS | Social feeds, shopping cart (with merge) |
| **CA** | Single-node RDBMS (no partition) | Not distributed — doesn't apply at scale |

**Architect interview answer:** "CAP isn't pick two of three forever — it's what you sacrifice during partition. Most systems are AP with tunable consistency (Cassandra, Cosmos DB consistency levels)."

---

## 2. PACELC Extension

**If Partition → choose A or C. Else (normal operation) → choose Latency or Consistency.**

| System | PA/EL | PA/EC | PC/EL | PC/EC |
|--------|-------|-------|-------|-------|
| DynamoDB | | ✓ default | | |
| Cassandra | | ✓ | | |
| MongoDB | | | ✓ | |
| PostgreSQL | | | | ✓ (single node) |

**Architect use:** Explain why DynamoDB is fast (latency) but may return stale reads unless strongly consistent reads requested (2x RCU cost).

---

## 3. Consistency Models

| Model | Guarantee | Example |
|-------|-----------|---------|
| **Strong** | Linearizable reads | Bank balance after transfer |
| **Sequential** | Operations appear in some order | |
| **Causal** | Causally related ops in order | Social comments |
| **Eventual** | Converges if no new writes | DNS, CDN cache |
| **Read-your-writes** | User sees own updates | Session consistency |

**Business mapping:**
- Payment confirmation → Strong
- Product catalog → Eventual (5 sec stale OK)
- User profile after edit → Read-your-writes

---

## 4. Failure Modes

Distributed systems fail partially and unpredictably.

| Failure | Symptom | Mitigation |
|---------|---------|------------|
| **Crash** | Process dies | Health checks, auto-restart, K8s |
| **OOM** | Process killed | Memory limits, profiling |
| **Slow** | Timeout appears as failure | Circuit breaker, timeouts, bulkheads |
| **Network partition** | Split brain | Quorum, fencing tokens |
| **Clock skew** | Ordering breaks | Logical clocks, NTP, avoid wall-clock ordering |
| **Byzantine** | Malicious/corrupt node | Blockchain, rarely in enterprise |

**Architect mantra:** Design every remote call as if it will fail, hang, or return duplicate.

---

## 5. Idempotency

**Same operation applied multiple times = same result as once.**

```csharp
public async Task ProcessPaymentAsync(PaymentCommand cmd)
{
    if (await _idempotencyStore.ExistsAsync(cmd.IdempotencyKey))
        return await _idempotencyStore.GetResultAsync(cmd.IdempotencyKey);

    var result = await _gateway.ChargeAsync(cmd);
    await _idempotencyStore.SaveAsync(cmd.IdempotencyKey, result);
}
```

**Required for:** Message queues (at-least-once delivery), retry logic, mobile clients (duplicate taps).

**Idempotency key sources:** Client-generated UUID, `orderId + operation`, message ID.

---

## 6. Timeouts, Retries, Circuit Breakers

```csharp
// Polly resilience pipeline
var pipeline = new ResiliencePipelineBuilder()
    .AddRetry(new RetryStrategyOptions { MaxRetryAttempts = 3, BackoffType = DelayBackoffType.Exponential })
    .AddCircuitBreaker(new CircuitBreakerStrategyOptions { FailureRatio = 0.5, MinimumThroughput = 10 })
    .AddTimeout(TimeSpan.FromSeconds(5))
    .Build();
```

| Pattern | Purpose |
|---------|---------|
| **Timeout** | Don't wait forever — fail fast |
| **Retry** | Transient failures (with exponential backoff + jitter) |
| **Circuit breaker** | Stop calling failing service — fail fast, allow recovery |
| **Bulkhead** | Isolate thread pools — one slow dependency doesn't drain all |

**Architect rule:** Retry only idempotent operations. Never retry without backoff (thundering herd).

---

## 7. Distributed Transactions Problem

**2PC (Two-Phase Commit)** — coordinator, blocking, doesn't scale across microservices.

**Alternatives architects use:**
- **Saga** — sequence of local transactions + compensating actions
- **Eventual consistency** — accept temporary inconsistency
- **Outbox pattern** — atomic local write + event publish

**Never:** Distributed 2PC across 12 microservices — coupling and availability killer.

---

## Common Mistakes
1. Assuming network is reliable
2. No idempotency with message queues
3. Unbounded retries without circuit breaker
4. Strong consistency everywhere (latency and availability cost)
5. Using wall-clock time for ordering across services

**Next:** [02-intermediate.md](02-intermediate.md)
