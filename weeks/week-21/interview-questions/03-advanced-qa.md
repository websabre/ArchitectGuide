# Week 21 — Advanced Q&A

> Q071–Q100: Premium format (Week 1 quality).

---


## Q071: 2PC vs 3PC Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Transactions |
| **Frequency** | Common |

### Question

Compare 2PC and 3PC for distributed transactions.

### Short Answer (30 seconds)

2PC blocks on coordinator failure after prepare. 3PC adds pre-commit phase reducing blocking but adds complexity and is rarely used in practice.

### Detailed Answer (3–5 minutes)

**2PC:** Prepare → Commit/Abort. Blocking if coordinator dies after prepare.

**3PC:** CanComplete phase — non-blocking in theory; network assumptions often violated.

**Architect:** Avoid both for microservices — sagas + outbox instead. Reserve 2PC for same-DC same-team DB clusters only.

### Architecture Perspective

Week 21 advanced depth on Transactions — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing 2PC vs 3PC Trade-offs?**
2. **What failure mode is most common with 2PC vs 3PC Trade-offs?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for 2PC vs 3PC Trade-offs
- Ignoring cost or security implications of 2PC vs 3PC Trade-offs
- No rollback or monitoring plan for 2PC vs 3PC Trade-offs

---

## Q072: Saga Orchestration Durable Functions

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Sagas |
| **Frequency** | Common |

### Question

Implement order saga with Azure Durable Functions orchestrator.

### Short Answer (30 seconds)

Orchestrator function calls activities with retry policies; built-in state persistence; compensation via `try/catch` with compensating activity calls.

### Detailed Answer (3–5 minutes)

```csharp
[FunctionName("OrderSaga")]
public async Task Run([OrchestrationTrigger] IDurableOrchestrationContext ctx) {
  try {
    await ctx.CallActivityAsync("ReserveInventory", input);
    await ctx.CallActivityAsync("ChargePayment", input);
  } catch {
    await ctx.CallActivityAsync("ReleaseInventory", input);
    throw;
  }
}
```

**Architect:** Durable Functions gives visible saga state — ops-friendly vs pure choreography.

### Architecture Perspective

Week 21 advanced depth on Sagas — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Saga Orchestration Durable Functions?**
2. **What failure mode is most common with Saga Orchestration Durable Functions?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Saga Orchestration Durable Functions
- Ignoring cost or security implications of Saga Orchestration Durable Functions
- No rollback or monitoring plan for Saga Orchestration Durable Functions

---

## Q073: Debezium CDC Outbox Relay

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Outbox |
| **Frequency** | Common |

### Question

Configure Debezium to relay outbox table to Kafka.

### Short Answer (30 seconds)

Debezium connector reads WAL, filters `outbox` table, transforms to CloudEvents, publishes to topic — no polling load on OLTP.

### Detailed Answer (3–5 minutes)

**Setup:**
- Outbox table with `aggregate_id`, `event_type`, `payload`
- Debezium Outbox Event Router SMT
- Kafka topic per event type or single topic with headers

**Architect:** CDC scales beyond polling — ops overhead for Connect cluster.

### Architecture Perspective

Week 21 advanced depth on Outbox — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Debezium CDC Outbox Relay?**
2. **What failure mode is most common with Debezium CDC Outbox Relay?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Debezium CDC Outbox Relay
- Ignoring cost or security implications of Debezium CDC Outbox Relay
- No rollback or monitoring plan for Debezium CDC Outbox Relay

---

## Q074: Raft Log Replication Deep

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Consensus |
| **Frequency** | Common |

### Question

Explain Raft log replication and commit index semantics.

### Short Answer (30 seconds)

Leader appends to log; replicates to followers; commits when majority replicated; followers apply committed entries in order.

### Detailed Answer (3–5 minutes)

**Key rules:**
- Leader-only writes
- Log matching: same term + index → same command
- Commit index = highest entry known replicated on majority

**Examples:** etcd, CockroachDB, Consul.

**Architect:** Failover time = election timeout + catch-up replication lag.

### Architecture Perspective

Week 21 advanced depth on Consensus — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Raft Log Replication Deep?**
2. **What failure mode is most common with Raft Log Replication Deep?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Raft Log Replication Deep
- Ignoring cost or security implications of Raft Log Replication Deep
- No rollback or monitoring plan for Raft Log Replication Deep

---

## Q075: Paxos vs Raft

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Consensus |
| **Frequency** | Common |

### Question

When would you discuss Paxos vs Raft with your team?

### Short Answer (30 seconds)

Raft designed for understandability — same safety as Paxos. Use Raft literacy for etcd/K8s; Paxos for academic or legacy systems (Chubby).

### Detailed Answer (3–5 minutes)

**Raft:** Leader-based, strong docs, implemented in etcd.
**Paxos:** Multi-decree, harder to implement correctly.

**Architect:** Don't build custom consensus — use etcd/Consul. Understand for vendor evaluation.

### Architecture Perspective

Week 21 advanced depth on Consensus — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Paxos vs Raft?**
2. **What failure mode is most common with Paxos vs Raft?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Paxos vs Raft
- Ignoring cost or security implications of Paxos vs Raft
- No rollback or monitoring plan for Paxos vs Raft

---

## Q076: Byzantine Fault Tolerance

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Consensus |
| **Frequency** | Common |

### Question

What is Byzantine fault tolerance and do most cloud apps need it?

### Short Answer (30 seconds)

BFT tolerates malicious or arbitrary faulty nodes — requires 3f+1 nodes for f Byzantine. Overkill for most enterprise apps; needed for blockchain, some financial networks.

### Detailed Answer (3–5 minutes)

**PBFT:** Practical Byzantine Fault Tolerance — complex, high overhead.

**Most apps:** Crash fault tolerance (Raft) sufficient — assume nodes fail-stop not malicious.

**Architect:** Mention BFT awareness; default to Raft-based systems unless threat model includes malicious insiders on nodes.

### Architecture Perspective

Week 21 advanced depth on Consensus — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Byzantine Fault Tolerance?**
2. **What failure mode is most common with Byzantine Fault Tolerance?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Byzantine Fault Tolerance
- Ignoring cost or security implications of Byzantine Fault Tolerance
- No rollback or monitoring plan for Byzantine Fault Tolerance

---

## Q077: SWIM Gossip Protocol

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Consensus |
| **Frequency** | Common |

### Question

How does SWIM improve failure detection over naive heartbeat?

### Short Answer (30 seconds)

SWIM uses probing + indirect ping + suspicion states — reduces false positives and network overhead at scale.

### Detailed Answer (3–5 minutes)

**Used in:** Consul memberlist, Cassandra influenced protocols.

**States:** Alive → Suspect → Dead with configurable timeouts.

**Architect:** Gossip membership is eventually consistent — brief stale routing windows during failures.

### Architecture Perspective

Week 21 advanced depth on Consensus — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing SWIM Gossip Protocol?**
2. **What failure mode is most common with SWIM Gossip Protocol?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for SWIM Gossip Protocol
- Ignoring cost or security implications of SWIM Gossip Protocol
- No rollback or monitoring plan for SWIM Gossip Protocol

---

## Q078: Kafka Partition Ordering

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Messaging |
| **Frequency** | Common |

### Question

Design Kafka topic partitioning for order lifecycle events.

### Short Answer (30 seconds)

Partition by `orderId` — all events for one order in single partition — strict order per order. Scale partitions for throughput across orders.

### Detailed Answer (3–5 minutes)

**Rules:**
- Key = business aggregate ID
- Partition count = max parallel consumers per group
- Rebalance causes brief ordering blip — design idempotent consumers

**Architect:** Never rely on global order across partitions — only per-key.

### Architecture Perspective

Week 21 advanced depth on Messaging — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Kafka Partition Ordering?**
2. **What failure mode is most common with Kafka Partition Ordering?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Kafka Partition Ordering
- Ignoring cost or security implications of Kafka Partition Ordering
- No rollback or monitoring plan for Kafka Partition Ordering

---

## Q079: Exactly-Once Stream Processing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Messaging |
| **Frequency** | Common |

### Question

Kafka EOS semantics — what is and isn't covered?

### Short Answer (30 seconds)

Producer idempotence + transactions within Kafka — exactly-once between Kafka topics. Cross DB still needs outbox.

### Detailed Answer (3–5 minutes)

**Covered:** Read-process-write within Kafka Streams/Flink with EOS enabled.
**Not covered:** Kafka + PostgreSQL without outbox.

**Architect:** Honest scope — EOS is bounded to streaming topology, not entire enterprise.

### Architecture Perspective

Week 21 advanced depth on Messaging — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Exactly-Once Stream Processing?**
2. **What failure mode is most common with Exactly-Once Stream Processing?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Exactly-Once Stream Processing
- Ignoring cost or security implications of Exactly-Once Stream Processing
- No rollback or monitoring plan for Exactly-Once Stream Processing

---

## Q080: Distributed Lock Fencing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Coordination |
| **Frequency** | Common |

### Question

Why fencing tokens matter with distributed locks?

### Short Answer (30 seconds)

Stale lock holder may complete write after lock lost — fencing token (monotonic) rejected by storage if token < latest.

### Detailed Answer (3–5 minutes)

**Martin Kleppmann critique:** Redis lock without fencing is unsafe for correctness-critical resources.

**Pattern:** Lock returns fencing token → DB write checks `WHERE fencing_token < @new`.

**Architect:** Use etcd leases + fencing for financial coordination; Redis locks for efficiency jobs only.

### Architecture Perspective

Week 21 advanced depth on Coordination — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Distributed Lock Fencing?**
2. **What failure mode is most common with Distributed Lock Fencing?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Distributed Lock Fencing
- Ignoring cost or security implications of Distributed Lock Fencing
- No rollback or monitoring plan for Distributed Lock Fencing

---

## Q081: Split-Brain Redis Sentinel

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Consensus |
| **Frequency** | Common |

### Question

How can Redis Sentinel split-brain occur and how prevent?

### Short Answer (30 seconds)

Network partition → two sentinels promote different masters → dual writes. Prevent with quorum, `min-slaves-to-write`, manual failover discipline.

### Detailed Answer (3–5 minutes)

**Prevention:**
- Odd sentinel count
- `min-slaves-to-write 1`
- Client must verify master identity

**Architect:** Redis HA ≠ SQL HA semantics — document RPO/RTO honestly.

### Architecture Perspective

Week 21 advanced depth on Consensus — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Split-Brain Redis Sentinel?**
2. **What failure mode is most common with Split-Brain Redis Sentinel?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Split-Brain Redis Sentinel
- Ignoring cost or security implications of Split-Brain Redis Sentinel
- No rollback or monitoring plan for Split-Brain Redis Sentinel

---

## Q082: Event Sourcing Snapshot Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Event Sourcing |
| **Frequency** | Common |

### Question

When snapshot event-sourced aggregates and how implement?

### Short Answer (30 seconds)

Snapshot every N events or time interval; load snapshot + events since version; async snapshot after commit.

### Detailed Answer (3–5 minutes)

**Implementation:**
- `aggregate_version` on snapshot row
- Background worker creates snapshot
- Schema version on snapshot blob for migration

**Architect:** Snapshot without version breaks replay after schema change.

### Architecture Perspective

Week 21 advanced depth on Event Sourcing — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Event Sourcing Snapshot Strategy?**
2. **What failure mode is most common with Event Sourcing Snapshot Strategy?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Event Sourcing Snapshot Strategy
- Ignoring cost or security implications of Event Sourcing Snapshot Strategy
- No rollback or monitoring plan for Event Sourcing Snapshot Strategy

---

## Q083: Temporal Workflow vs Durable Functions

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Sagas |
| **Frequency** | Common |

### Question

Compare Temporal and Azure Durable Functions for sagas.

### Short Answer (30 seconds)

Temporal: language SDKs, durable timers, strong visibility UI, self-hosted or cloud. Durable Functions: Azure-native, Functions consumption model.

### Detailed Answer (3–5 minutes)

**Temporal wins:** Complex long-running workflows, polyglot, workflow versioning.
**Durable wins:** Azure-only shops, serverless billing, tight Functions integration.

**Architect:** Evaluate ops model — Temporal cluster vs Functions managed runtime.

### Architecture Perspective

Week 21 advanced depth on Sagas — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Temporal Workflow vs Durable Functions?**
2. **What failure mode is most common with Temporal Workflow vs Durable Functions?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Temporal Workflow vs Durable Functions
- Ignoring cost or security implications of Temporal Workflow vs Durable Functions
- No rollback or monitoring plan for Temporal Workflow vs Durable Functions

---

## Q084: Process Manager Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Sagas |
| **Frequency** | Common |

### Question

Implement process manager for multi-step order fulfillment.

### Short Answer (30 seconds)

Central state machine persists saga state; reacts to events; emits commands; handles timeouts and compensation.

### Detailed Answer (3–5 minutes)

**State table:** `saga_id`, `current_step`, `payload`, `timeout_at`.

**Handlers:** Event → transition → command(s).

**Architect:** Process manager = orchestration with explicit persistence — debuggable in incidents.

### Architecture Perspective

Week 21 advanced depth on Sagas — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Process Manager Pattern?**
2. **What failure mode is most common with Process Manager Pattern?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Process Manager Pattern
- Ignoring cost or security implications of Process Manager Pattern
- No rollback or monitoring plan for Process Manager Pattern

---

## Q085: Compensation Timeout Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Sagas |
| **Frequency** | Common |

### Question

Saga step times out — how decide compensate vs retry?

### Short Answer (30 seconds)

Retry transient (503, timeout) with bounded attempts; compensate on business failure or max retries; escalate to human queue on compensation failure.

### Detailed Answer (3–5 minutes)

**Policy matrix:**
| Error | Action |
|-------|--------|
| 503 | Retry 3× |
| 400 business | Compensate |
| Timeout 30s | Query status → reconcile |
| Compensate fail | Human workflow |

**Architect:** Document per-step timeout and compensation in saga ADR.

### Architecture Perspective

Week 21 advanced depth on Sagas — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Compensation Timeout Design?**
2. **What failure mode is most common with Compensation Timeout Design?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Compensation Timeout Design
- Ignoring cost or security implications of Compensation Timeout Design
- No rollback or monitoring plan for Compensation Timeout Design

---

## Q086: Read Repair Cassandra

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Replication |
| **Frequency** | Common |

### Question

Explain read repair in eventually consistent stores.

### Short Answer (30 seconds)

On read, coordinator compares replicas; returns latest; repairs stale replicas in background.

### Detailed Answer (3–5 minutes)

**Triggered:** `QUORUM` read finds mismatched digest.

**Trade-off:** Read latency spike during repair; anti-entropy complements read repair.

**Architect:** Tunable consistency — `LOCAL_QUORUM` for production reads.

### Architecture Perspective

Week 21 advanced depth on Replication — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Read Repair Cassandra?**
2. **What failure mode is most common with Read Repair Cassandra?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Read Repair Cassandra
- Ignoring cost or security implications of Read Repair Cassandra
- No rollback or monitoring plan for Read Repair Cassandra

---

## Q087: Hinted Handoff

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Replication |
| **Frequency** | Common |

### Question

What is hinted handoff and when does it help?

### Short Answer (30 seconds)

Temporarily store writes for unavailable node; deliver when node returns — improves write availability during brief outages.

### Detailed Answer (3–5 minutes)

**Risk:** If hinted node never returns, hints pile up.

**Architect:** Part of AP write path — understand during node replacement procedures.

### Architecture Perspective

Week 21 advanced depth on Replication — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Hinted Handoff?**
2. **What failure mode is most common with Hinted Handoff?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Hinted Handoff
- Ignoring cost or security implications of Hinted Handoff
- No rollback or monitoring plan for Hinted Handoff

---

## Q088: Quorum Reads vs Writes

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Replication |
| **Frequency** | Common |

### Question

Design quorum sizes for R=3 replica system.

### Short Answer (30 seconds)

W + R > N ensures overlap — strong read if W=R=2, N=3. Tune W/R for latency vs consistency.

### Detailed Answer (3–5 minutes)

**Example N=3:**
- W=2, R=2 — strong consistency possible
- W=1, R=1 — fast, stale reads

**Architect:** Dynamo/Cassandra tunable — document chosen W/R per use case.

### Architecture Perspective

Week 21 advanced depth on Replication — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Quorum Reads vs Writes?**
2. **What failure mode is most common with Quorum Reads vs Writes?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Quorum Reads vs Writes
- Ignoring cost or security implications of Quorum Reads vs Writes
- No rollback or monitoring plan for Quorum Reads vs Writes

---

## Q089: Linearizability vs Serializability

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Consistency |
| **Frequency** | Common |

### Question

Distinguish linearizability and serializability for architects.

### Short Answer (30 seconds)

Linearizability: real-time order of ops visible to all. Serializability: transaction order exists — may not match real-time.

### Detailed Answer (3–5 minutes)

**Linearizable:** etcd reads, Spanner external consistency.
**Serializable:** SQL `SERIALIZABLE` isolation — not necessarily linearizable across sessions.

**Architect:** Use correct term in ADR — interviewers distinguish precisely.

### Architecture Perspective

Week 21 advanced depth on Consistency — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Linearizability vs Serializability?**
2. **What failure mode is most common with Linearizability vs Serializability?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Linearizability vs Serializability
- Ignoring cost or security implications of Linearizability vs Serializability
- No rollback or monitoring plan for Linearizability vs Serializability

---

## Q090: Causal Consistency

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Consistency |
| **Frequency** | Common |

### Question

When recommend causal consistency over strong?

### Short Answer (30 seconds)

Social feeds, comments threads — user sees own writes and causally related updates without global strong consistency cost.

### Detailed Answer (3–5 minutes)

**Mechanism:** Track vector clocks or version chains per object.

**Cosmos:** Session consistency approximates causal for same session.

**Architect:** Causal is middle ground — cheaper than strong, more intuitive than eventual.

### Architecture Perspective

Week 21 advanced depth on Consistency — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Causal Consistency?**
2. **What failure mode is most common with Causal Consistency?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Causal Consistency
- Ignoring cost or security implications of Causal Consistency
- No rollback or monitoring plan for Causal Consistency

---

## Q091: Hybrid Logical Clocks

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Time |
| **Frequency** | Common |

### Question

How do hybrid logical clocks (HLC) work in CockroachDB?

### Short Answer (30 seconds)

Combine physical time with logical counter — bound clock uncertainty without GPS like Spanner.

### Detailed Answer (3–5 minutes)

**On event:** `hlc = max(physical, previous_logical) + 1` if same physical tick.

**Benefit:** Causal ordering with wall-clock affinity for debugging.

**Architect:** HLC enables global SQL with reasonable semantics — not magic CA.

### Architecture Perspective

Week 21 advanced depth on Time — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Hybrid Logical Clocks?**
2. **What failure mode is most common with Hybrid Logical Clocks?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Hybrid Logical Clocks
- Ignoring cost or security implications of Hybrid Logical Clocks
- No rollback or monitoring plan for Hybrid Logical Clocks

---

## Q092: Inbox Outbox Pairing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Messaging |
| **Frequency** | Common |

### Question

Design end-to-end effectively-once with outbox and inbox.

### Short Answer (30 seconds)

Publisher: outbox in same TX as write. Consumer: inbox dedup in same TX as handler. At-least-once broker between.

### Detailed Answer (3–5 minutes)

**End-to-end:**
1. Service A outbox → bus
2. Service B inbox check → process → commit
3. Duplicate delivery → inbox conflict → no-op

**Architect:** Both sides required for cross-service effectively-once.

### Architecture Perspective

Week 21 advanced depth on Messaging — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Inbox Outbox Pairing?**
2. **What failure mode is most common with Inbox Outbox Pairing?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Inbox Outbox Pairing
- Ignoring cost or security implications of Inbox Outbox Pairing
- No rollback or monitoring plan for Inbox Outbox Pairing

---

## Q093: Saga Choreography Debugging

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Sagas |
| **Frequency** | Common |

### Question

Choreography saga stuck — how debug without central orchestrator?

### Short Answer (30 seconds)

Distributed trace per correlationId; event log audit table; saga timeout scanner on each service; dead letter on missing expected event.

### Detailed Answer (3–5 minutes)

**Tooling:**
- Event catalog with expected next events
- `saga_timeline` view from correlated spans
- Alert: `OrderSubmitted` without `PaymentCaptured` in 5m

**Architect:** Choreography needs superior observability — budget for it.

### Architecture Perspective

Week 21 advanced depth on Sagas — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Saga Choreography Debugging?**
2. **What failure mode is most common with Saga Choreography Debugging?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Saga Choreography Debugging
- Ignoring cost or security implications of Saga Choreography Debugging
- No rollback or monitoring plan for Saga Choreography Debugging

---

## Q094: Conflict Resolution Dynamo

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Distributed Data |
| **Frequency** | Common |

### Question

How Dynamo-style systems resolve write conflicts?

### Short Answer (30 seconds)

Vector clocks detect conflict; last-write-wins, merge function, or escalate to application.

### Detailed Answer (3–5 minutes)

**Strategies:**
- LWW with timestamp (loses data risk)
- Application merge (shopping cart union)
- Human resolution queue (rare)

**Architect:** Document merge semantics per entity — product must accept.

### Architecture Perspective

Week 21 advanced depth on Distributed Data — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Conflict Resolution Dynamo?**
2. **What failure mode is most common with Conflict Resolution Dynamo?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Conflict Resolution Dynamo
- Ignoring cost or security implications of Conflict Resolution Dynamo
- No rollback or monitoring plan for Conflict Resolution Dynamo

---

## Q095: Jepsen Testing Mindset

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Testing |
| **Frequency** | Common |

### Question

What is Jepsen and why should architects know it?

### Short Answer (30 seconds)

Jepsen tests distributed databases under partition/failure — exposes consistency claims vs reality.

### Detailed Answer (3–5 minutes)

**Famous findings:** MongoDB, Redis, RabbitMQ issues under partition.

**Architect use:** Evaluate vendor HA claims; run chaos tests on your stack; don't trust marketing 'linearizable' without verification.

### Architecture Perspective

Week 21 advanced depth on Testing — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Jepsen Testing Mindset?**
2. **What failure mode is most common with Jepsen Testing Mindset?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Jepsen Testing Mindset
- Ignoring cost or security implications of Jepsen Testing Mindset
- No rollback or monitoring plan for Jepsen Testing Mindset

---

## Q096: Chaos Engineering Distributed Tx

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Resilience |
| **Frequency** | Common |

### Question

Design chaos experiment for payment saga path.

### Short Answer (30 seconds)

Inject payment service latency, kill inventory consumer, partition Service Bus — verify no double charge and compensation completes.

### Detailed Answer (3–5 minutes)

**Hypothesis:** Stuck payments reconcile within 5m; no duplicate captures.

**Tools:** Azure Chaos Studio, Litmus, Toxiproxy.

**Architect:** Start staging; one fault per experiment; measure MTTR.

### Architecture Perspective

Week 21 advanced depth on Resilience — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Chaos Engineering Distributed Tx?**
2. **What failure mode is most common with Chaos Engineering Distributed Tx?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Chaos Engineering Distributed Tx
- Ignoring cost or security implications of Chaos Engineering Distributed Tx
- No rollback or monitoring plan for Chaos Engineering Distributed Tx

---

## Q097: Observability Async Workflows

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Observability |
| **Frequency** | Common |

### Question

Metrics and alerts for async saga health.

### Short Answer (30 seconds)

Track: saga completion rate, step latency p99, compensation rate, DLQ depth, stuck saga count by state.

### Detailed Answer (3–5 minutes)

**Alerts:**
- `stuck_sagas > 10` for 15m → page
- `compensation_rate` spike → investigate upstream

**Architect:** SLO on saga completion time — not just API latency.

### Architecture Perspective

Week 21 advanced depth on Observability — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Observability Async Workflows?**
2. **What failure mode is most common with Observability Async Workflows?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Observability Async Workflows
- Ignoring cost or security implications of Observability Async Workflows
- No rollback or monitoring plan for Observability Async Workflows

---

## Q098: Network Partition DR Drill

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | DR |
| **Frequency** | Common |

### Question

Run DR drill simulating AZ partition — what verify?

### Short Answer (30 seconds)

Quorum behavior, write rejection on minority side, failover RTO, no split-brain writes, message backlog recovery.

### Detailed Answer (3–5 minutes)

**Checklist:**
- [ ] CP systems reject writes on minority
- [ ] AP systems document stale read window
- [ ] Runbook executed within RTO
- [ ] Post-drill ADR updates

**Architect:** Partition drills prove CAP choices — schedule quarterly.

### Architecture Perspective

Week 21 advanced depth on DR — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Network Partition DR Drill?**
2. **What failure mode is most common with Network Partition DR Drill?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Network Partition DR Drill
- Ignoring cost or security implications of Network Partition DR Drill
- No rollback or monitoring plan for Network Partition DR Drill

---

## Q099: Compliance Eventual Consistency

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Compliance |
| **Frequency** | Common |

### Question

Auditor asks about eventual consistency in financial reporting — respond?

### Short Answer (30 seconds)

Authoritative ledger is CP with audit trail; reports are async projections with defined lag SLA; reconciliation job proves completeness.

### Detailed Answer (3–5 minutes)

**Artifacts:**
- Immutable event log
- Daily reconciliation report
- Lag SLA documented (e.g. 15m for analytics)

**Architect:** Separate compliance path from AP read models.

### Architecture Perspective

Week 21 advanced depth on Compliance — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Compliance Eventual Consistency?**
2. **What failure mode is most common with Compliance Eventual Consistency?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Compliance Eventual Consistency
- Ignoring cost or security implications of Compliance Eventual Consistency
- No rollback or monitoring plan for Compliance Eventual Consistency

---

## Q100: Multi-Region Active-Active Conflicts

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Architecture |
| **Frequency** | Common |

### Question

Design conflict handling for active-active orders in two regions.

### Short Answer (30 seconds)

Partition by customer region as primary; CRDT or LWW with business merge rules; avoid dual-primary same aggregate.

### Detailed Answer (3–5 minutes)

**Patterns:**
- Home region per customerId
- Async replication for DR read
- Conflict queue for true concurrent writes (rare)

**Architect:** Active-active is hard — default active-passive unless revenue justifies complexity.

### Architecture Perspective

Week 21 advanced depth on Architecture — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Multi-Region Active-Active Conflicts?**
2. **What failure mode is most common with Multi-Region Active-Active Conflicts?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Multi-Region Active-Active Conflicts
- Ignoring cost or security implications of Multi-Region Active-Active Conflicts
- No rollback or monitoring plan for Multi-Region Active-Active Conflicts

---
