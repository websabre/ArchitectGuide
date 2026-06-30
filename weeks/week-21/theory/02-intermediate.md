# Distributed Systems — Intermediate (Consensus, Replication, Quorum)

> **Week 21** | **Level:** Intermediate

## 1. Replication Strategies

| Strategy | Leader | Use Case |
|----------|--------|----------|
| **Leader-follower** | Single writer | PostgreSQL, MySQL, Kafka |
| **Leader-leader** | Multi-writer (conflict) | Multi-master (risky) |
| **Leaderless** | Quorum read/write | DynamoDB, Cassandra |

**Quorum:** `R + W > N` ensures overlap (read sees latest write)
- N=3 replicas, W=2, R=2 → tolerates 1 node failure

---

## 2. Consensus (Raft, Paxos)

**Problem:** Multiple nodes agree on a value/order.

**Raft (understand conceptually):**
- Leader election
- Log replication
- Used in: etcd (Kubernetes), Consul

**Architect relevance:** You don't implement Raft — you choose systems that use it (etcd, Kafka with KRaft). Know that leader election takes time during partition.

---

## 3. Split Brain

Two nodes both think they're primary → data corruption.

**Prevention:**
- Quorum majority required for writes
- Fencing tokens (STONITH)
- Kubernetes: single writer via lease

---

## 4. Exactly-Once Semantics (Illusion)

True exactly-once end-to-end is impossible. **Practical exactly-once = at-least-once delivery + idempotent processing.**

Kafka: transactional producer + idempotent consumer offset + business idempotency key.

---

## 5. Backpressure

When consumer slower than producer — system must slow producers or buffer.

| Strategy | Mechanism |
|----------|-----------|
| Bounded queue | Drop or reject when full |
| Rate limiting | Token bucket at API gateway |
| Reactive streams | `IAsyncEnumerable`, Project Reactor |

**Architect:** Unbounded queues = OOM eventually. Always define max queue depth and rejection policy.

---

## Production Example

**E-commerce inventory during flash sale:**
- Strong consistency on stock decrement → bottleneck
- **Design:** Reserve inventory in Redis (atomic DECR), async confirm via saga to SQL
- Accept brief oversell risk → reconcile with compensating cancel
- Trade-off: Availability + latency over perfect consistency

**Next:** [03-advanced-expert.md](03-advanced-expert.md)
