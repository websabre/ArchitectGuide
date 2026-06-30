# Week 21 — Expert Scenario Q&A

> Q101–Q120: Premium format (Week 1 quality).

---


## Q101: Global Order System Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Architecture |
| **Frequency** | Occasional |
| **Type** | Scenario |

### Question

Design globally distributed order system with 99.99% availability.

### Short Answer (30 seconds)

Region-local write path with home shard per customer; async cross-region replication; saga orchestration; idempotency everywhere; CP payment partition.

### Detailed Answer

**Architecture:**
- Home region assignment via geo-DNS + sticky routing
- Order aggregate CP within region
- Cross-region: event replication for analytics only
- Payment: region-local PSP with failover runbook

**Trade-offs:** Cross-region order view eventual; acceptable for support tools not checkout.

### Architecture Perspective

Week 21 expert depth on Architecture — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Global Order System Design?**
2. **What failure mode is most common with Global Order System Design?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Global Order System Design
- Ignoring cost or security implications of Global Order System Design
- No rollback or monitoring plan for Global Order System Design

---

## Q102: Financial Ledger Event Sourcing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Event Sourcing |
| **Frequency** | Occasional |
| **Type** | Scenario |

### Question

Design immutable financial ledger with event sourcing.

### Short Answer (30 seconds)

Append-only journal; double-entry as event pairs; snapshot for balance queries; regulatory export from event stream.

### Detailed Answer

**Events:** `DebitPosted`, `CreditPosted` — never delete; compensating events for reversal.

**Controls:** Hash chain per account; daily balance reconciliation; WORM storage for archive.

**Architect:** Ledger is CP — reject write if quorum lost.

### Architecture Perspective

Week 21 expert depth on Event Sourcing — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Financial Ledger Event Sourcing?**
2. **What failure mode is most common with Financial Ledger Event Sourcing?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Financial Ledger Event Sourcing
- Ignoring cost or security implications of Financial Ledger Event Sourcing
- No rollback or monitoring plan for Financial Ledger Event Sourcing

---

## Q103: Outbox at 100K TPS

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Outbox |
| **Frequency** | Occasional |
| **Type** | Scenario |

### Question

Scale transactional outbox to 100K events/sec.

### Short Answer (30 seconds)

Partition outbox table; CDC (Debezium) not polling; batch publish; separate relay per partition; monitor relay lag SLO.

### Detailed Answer

**Schema:** `outbox` partitioned by `aggregate_id` hash.

**Relay:** Kafka Connect with multiple tasks; idempotent producer.

**Bottleneck watch:** DB WAL throughput — may need dedicated event store.

### Architecture Perspective

Week 21 expert depth on Outbox — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Outbox at 100K TPS?**
2. **What failure mode is most common with Outbox at 100K TPS?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Outbox at 100K TPS
- Ignoring cost or security implications of Outbox at 100K TPS
- No rollback or monitoring plan for Outbox at 100K TPS

---

## Q104: Spanner TrueTime Tradeoffs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Consensus |
| **Frequency** | Occasional |
| **Type** | Scenario |

### Question

When Spanner-style TrueTime is worth the cost?

### Short Answer (30 seconds)

External consistency globally when business pays for GPS/atomic clocks and Google-scale ops — rare for typical enterprise.

### Detailed Answer

**TrueTime:** Bounded clock uncertainty → global transactions.

**Alternatives:** CockroachDB HLC, per-region CP with async replication.

**Architect:** Honest TCO — Spanner/TrueTime class for regulatory global SQL at scale only.

### Architecture Perspective

Week 21 expert depth on Consensus — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Spanner TrueTime Tradeoffs?**
2. **What failure mode is most common with Spanner TrueTime Tradeoffs?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Spanner TrueTime Tradeoffs
- Ignoring cost or security implications of Spanner TrueTime Tradeoffs
- No rollback or monitoring plan for Spanner TrueTime Tradeoffs

---

## Q105: Jepsen-Style Testing Program

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Testing |
| **Frequency** | Occasional |
| **Type** | Scenario |

### Question

Establish Jepsen-style distributed systems test program.

### Short Answer (30 seconds)

Chaos partition injection in staging; consistency oracles; automated invariant checks; run before major DB/middleware upgrades.

### Detailed Answer

**Program:**
1. Define invariants (no lost writes, no double apply)
2. Fault injection library
3. CI weekly chaos job
4. Report for architecture review board

**Architect:** Vendor claims validated by your tests — not slides.

### Architecture Perspective

Week 21 expert depth on Testing — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Jepsen-Style Testing Program?**
2. **What failure mode is most common with Jepsen-Style Testing Program?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Jepsen-Style Testing Program
- Ignoring cost or security implications of Jepsen-Style Testing Program
- No rollback or monitoring plan for Jepsen-Style Testing Program

---

## Q106: Formal Saga Verification

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Sagas |
| **Frequency** | Occasional |
| **Type** | Scenario |

### Question

Can saga correctness be formally verified?

### Short Answer (30 seconds)

Model saga as state machine; verify compensation completeness, deadlock freedom, reachable terminal states — tools: TLA+, Alloy for critical paths.

### Detailed Answer

**Worth it when:** Payment platform, regulatory scrutiny, complex compensation trees.

**Pragmatic:** State machine unit tests + chaos for most teams.

**Architect:** TLA+ for Tier-0 sagas — ADR documents model.

### Architecture Perspective

Week 21 expert depth on Sagas — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Formal Saga Verification?**
2. **What failure mode is most common with Formal Saga Verification?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Formal Saga Verification
- Ignoring cost or security implications of Formal Saga Verification
- No rollback or monitoring plan for Formal Saga Verification

---

## Q107: Incident Split-Brain Postmortem

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Operations |
| **Frequency** | Occasional |
| **Type** | Scenario |

### Question

Lead postmortem after split-brain caused duplicate charges.

### Short Answer (30 seconds)

Timeline reconstruction, quorum config review, fencing gaps, customer remediation, ADR for prevention — blameless with exec summary.

### Detailed Answer

**Actions:**
- Fix quorum/witness
- Add fencing tokens
- Reconciliation job for duplicates
- Game day quarterly

**Architect:** Split-brain postmortem is career-defining — demonstrate leadership.

### Architecture Perspective

Week 21 expert depth on Operations — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Incident Split-Brain Postmortem?**
2. **What failure mode is most common with Incident Split-Brain Postmortem?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Incident Split-Brain Postmortem
- Ignoring cost or security implications of Incident Split-Brain Postmortem
- No rollback or monitoring plan for Incident Split-Brain Postmortem

---

## Q108: Custom Saga Coordinator Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Sagas |
| **Frequency** | Occasional |
| **Type** | Scenario |

### Question

Build custom saga coordinator for 50-step B2B workflows.

### Short Answer (30 seconds)

Persistent state machine, horizontal workers with shard by sagaId, lease per saga, visibility API, versioned saga definitions.

### Detailed Answer

**Scale:** Partition saga table; single writer per sagaId; async step dispatch via queue.

**Architect:** Custom coordinator when Temporal/Durable insufficient — high maintenance — justify in ADR.

### Architecture Perspective

Week 21 expert depth on Sagas — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Custom Saga Coordinator Scale?**
2. **What failure mode is most common with Custom Saga Coordinator Scale?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Custom Saga Coordinator Scale
- Ignoring cost or security implications of Custom Saga Coordinator Scale
- No rollback or monitoring plan for Custom Saga Coordinator Scale

---

## Q109: WAN Partition CAP Exercise

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Fundamentals |
| **Frequency** | Occasional |
| **Type** | Scenario |

### Question

Walk through CAP choices during WAN partition for your platform.

### Short Answer (30 seconds)

Per-component: SQL CP (reject), cache AP (stale), queue buffer (AP with backlog), search AP — document user-visible behavior each.

### Detailed Answer

**Deliverable:** CAP matrix in runbook; support scripts for partition mode; executive comms template.

**Architect:** Pre-written partition playbook reduces incident panic.

### Architecture Perspective

Week 21 expert depth on Fundamentals — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing WAN Partition CAP Exercise?**
2. **What failure mode is most common with WAN Partition CAP Exercise?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for WAN Partition CAP Exercise
- Ignoring cost or security implications of WAN Partition CAP Exercise
- No rollback or monitoring plan for WAN Partition CAP Exercise

---

## Q110: CRDT Shopping Cart Global

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Distributed Data |
| **Frequency** | Occasional |
| **Type** | Scenario |

### Question

Design globally available shopping cart with CRDT merge.

### Short Answer (30 seconds)

OR-Set for line items; LWW for quantities; merge on sync; TTL for abandoned carts; conflict-free add/remove.

### Detailed Answer

**Client:** Offline add items; sync merges with server state.

**Product:** Accept merge semantics — duplicate SKU merges quantity.

**Architect:** CRDT cart + CP checkout at payment boundary.

### Architecture Perspective

Week 21 expert depth on Distributed Data — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing CRDT Shopping Cart Global?**
2. **What failure mode is most common with CRDT Shopping Cart Global?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for CRDT Shopping Cart Global
- Ignoring cost or security implications of CRDT Shopping Cart Global
- No rollback or monitoring plan for CRDT Shopping Cart Global

---

## Q111: Disaster Recovery Event Sourced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | DR |
| **Frequency** | Occasional |
| **Type** | Scenario |

### Question

DR strategy for event-sourced platform.

### Short Answer (30 seconds)

Replicate event log cross-region; replay projections in DR; snapshot + log shipping; RPO = replication lag; test full replay quarterly.

### Detailed Answer

**Components:**
- Primary event store replication
- Projection rebuild automation
- Snapshot restore + catch-up

**Architect:** DR test must include projection rebuild time — not just failover DNS.

### Architecture Perspective

Week 21 expert depth on DR — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Disaster Recovery Event Sourced?**
2. **What failure mode is most common with Disaster Recovery Event Sourced?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Disaster Recovery Event Sourced
- Ignoring cost or security implications of Disaster Recovery Event Sourced
- No rollback or monitoring plan for Disaster Recovery Event Sourced

---

## Q112: Async Workflow Compliance Audit

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Compliance |
| **Frequency** | Occasional |
| **Type** | Scenario |

### Question

Prove async workflow audit trail to regulators.

### Short Answer (30 seconds)

Immutable event log, correlation IDs, signed events, retention policy, query API for auditor, reconciliation proofs.

### Detailed Answer

**Controls:**
- WORM storage 7 years
- Hash chain integrity checks
- Access audit for log queries

**Architect:** Compliance by design — not retrofit logging.

### Architecture Perspective

Week 21 expert depth on Compliance — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Async Workflow Compliance Audit?**
2. **What failure mode is most common with Async Workflow Compliance Audit?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Async Workflow Compliance Audit
- Ignoring cost or security implications of Async Workflow Compliance Audit
- No rollback or monitoring plan for Async Workflow Compliance Audit

---

## Q113: Consensus Under Load Test

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Consensus |
| **Frequency** | Occasional |
| **Type** | Scenario |

### Question

etcd quorum degrades under load test — expert analysis path.

### Short Answer (30 seconds)

Check disk latency, election timeouts, network, defrag schedule, member count — tune heartbeat and election timeout; add members or faster disks.

### Detailed Answer

**K8s impact:** Slow etcd → API server latency → whole cluster sick.

**Architect:** etcd on dedicated SSD; monitor `etcd_disk_wal_fsync_duration`.

### Architecture Perspective

Week 21 expert depth on Consensus — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Consensus Under Load Test?**
2. **What failure mode is most common with Consensus Under Load Test?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Consensus Under Load Test
- Ignoring cost or security implications of Consensus Under Load Test
- No rollback or monitoring plan for Consensus Under Load Test

---

## Q114: Designing for Message Loss

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Messaging |
| **Frequency** | Occasional |
| **Type** | Scenario |

### Question

Broker may lose messages under catastrophic failure — architect response?

### Short Answer (30 seconds)

Acknowledged trade-off; critical events dual-write to audit log; outbox retained until consumer ack; periodic reconciliation between services.

### Detailed Answer

**Tier-0:** No message-only path — sync confirmation or persistent outbox until ack.

**Architect:** Honest about broker guarantees — design reconciliation safety nets.

### Architecture Perspective

Week 21 expert depth on Messaging — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Designing for Message Loss?**
2. **What failure mode is most common with Designing for Message Loss?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Designing for Message Loss
- Ignoring cost or security implications of Designing for Message Loss
- No rollback or monitoring plan for Designing for Message Loss

---

## Q115: Distributed Systems Interview Panel

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Career |
| **Frequency** | Occasional |
| **Type** | Scenario |

### Question

Principal panel: defend AP choice for cart with CP payment.

### Short Answer (30 seconds)

Cart AP for availability and merge; checkout boundary transitions to CP saga; clear UX states; monitoring on transition failures.

### Detailed Answer

**Narrative:** Separate consistency concerns by lifecycle phase — not one global choice.

**Architect:** Panel wants nuanced CAP — not absolutes.

### Architecture Perspective

Week 21 expert depth on Career — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Distributed Systems Interview Panel?**
2. **What failure mode is most common with Distributed Systems Interview Panel?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Distributed Systems Interview Panel
- Ignoring cost or security implications of Distributed Systems Interview Panel
- No rollback or monitoring plan for Distributed Systems Interview Panel

---

## Q116: Latency SLO Cross-Region Saga

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | SLO |
| **Frequency** | Occasional |
| **Type** | Scenario |

### Question

SLO 500ms checkout with cross-region inventory — feasible?

### Short Answer (30 seconds)

Analyze hop budget; likely need regional inventory read replica sync; async reserve with sync confirm only if local stock; or regional fulfillment cells.

### Detailed Answer

**Math:** 3× 50ms cross-region RTT = 150ms network alone — tight.

**Architect:** SLO drives topology — may require cell-based architecture.

### Architecture Perspective

Week 21 expert depth on SLO — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Latency SLO Cross-Region Saga?**
2. **What failure mode is most common with Latency SLO Cross-Region Saga?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Latency SLO Cross-Region Saga
- Ignoring cost or security implications of Latency SLO Cross-Region Saga
- No rollback or monitoring plan for Latency SLO Cross-Region Saga

---

## Q117: Event Log Compaction Policy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Event Sourcing |
| **Frequency** | Occasional |
| **Type** | Scenario |

### Question

When compact/delete events in event-sourced system?

### Short Answer (30 seconds)

Never delete compliance events; compact snapshots replace need for full replay for aggregates; archive cold events to glacier with legal hold.

### Detailed Answer

**Policy:**
- Hot: full log online
- Warm: snapshots + recent events
- Cold: archive immutable

**Architect:** Legal retention overrides technical compaction desires.

### Architecture Perspective

Week 21 expert depth on Event Sourcing — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Event Log Compaction Policy?**
2. **What failure mode is most common with Event Log Compaction Policy?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Event Log Compaction Policy
- Ignoring cost or security implications of Event Log Compaction Policy
- No rollback or monitoring plan for Event Log Compaction Policy

---

## Q118: Teaching CAP to Executives

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Communication |
| **Frequency** | Occasional |
| **Type** | Scenario |

### Question

Explain CAP trade-off to non-technical executive in 2 minutes.

### Short Answer (30 seconds)

During network split, we choose: pause sales (consistent) or allow both offices to sell with later reconciliation (available) — we document choice per business risk.

### Detailed Answer

**Analogy:** Two cash registers disconnected — one ledger (pause) vs both sell reconcile later.

**Architect:** Executive clarity prevents unrealistic 'never down never wrong' demands.

### Architecture Perspective

Week 21 expert depth on Communication — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Teaching CAP to Executives?**
2. **What failure mode is most common with Teaching CAP to Executives?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Teaching CAP to Executives
- Ignoring cost or security implications of Teaching CAP to Executives
- No rollback or monitoring plan for Teaching CAP to Executives

---

## Q119: Research vs Production Consensus

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Consensus |
| **Frequency** | Occasional |
| **Type** | Scenario |

### Question

Team wants custom Raft — expert response?

### Short Answer (30 seconds)

Redirect to etcd/Consul; if custom needed, fork battle-tested lib, security review, Jepsen testing, long-term maintenance budget.

### Detailed Answer

**Reality:** Consensus bugs surface years later.

**Architect:** 'Not invented here' on consensus is red flag — escalate to principal.

### Architecture Perspective

Week 21 expert depth on Consensus — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Research vs Production Consensus?**
2. **What failure mode is most common with Research vs Production Consensus?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Research vs Production Consensus
- Ignoring cost or security implications of Research vs Production Consensus
- No rollback or monitoring plan for Research vs Production Consensus

---

## Q120: Platform-Wide Idempotency Standard

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Governance |
| **Frequency** | Occasional |
| **Type** | Scenario |

### Question

Mandate idempotency standard across 40 microservices.

### Short Answer (30 seconds)

HTTP `Idempotency-Key` on POST; message `eventId` dedup; SDK middleware; CI lint; catalog documents per endpoint.

### Detailed Answer

**Governance:**
- Platform library for idempotency store
- Breaking PR check without key on mutating APIs
- Metrics: duplicate request rate

**Architect:** Standards beat per-team reinventing inbox tables.

### Architecture Perspective

Week 21 expert depth on Governance — interviewers want mechanism plus operational guardrails.

### Follow-up Questions

1. **How measure success after implementing Platform-Wide Idempotency Standard?**
2. **What failure mode is most common with Platform-Wide Idempotency Standard?**

### Common Mistakes in Interviews

- Hand-wavy answer without production example for Platform-Wide Idempotency Standard
- Ignoring cost or security implications of Platform-Wide Idempotency Standard
- No rollback or monitoring plan for Platform-Wide Idempotency Standard

---
