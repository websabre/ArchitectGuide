#!/usr/bin/env python3
"""Generate _banks_data_21_28_extra.py — 480 premium Q&A tuples (60 per week × 8 weeks)."""

from __future__ import annotations

import os
import textwrap

OUT = os.path.join(os.path.dirname(__file__), "_banks_data_21_28_extra.py")

# (title, category, frequency, question, short, detailed, perspective, fu1, fu2, m1, m2, m3)
Question = tuple[str, str, str, str, str, str, str, str, str, str, str, str]

WEEK_TOPICS: dict[int, dict[str, list[tuple[str, str, str]]]] = {
    21: {
        "intermediate": [
            ("Event Sourcing Basics", "Event Sourcing", "What is event sourcing and when recommend it over CRUD?",
             "Store state changes as append-only events; rebuild state by replay. Use when audit trail, temporal queries, or event-driven integration are first-class requirements.",
             "**Core idea:** `OrderCreated`, `LineAdded`, `OrderPaid` — current state = fold(events).\n\n**When yes:** Financial audit, regulatory replay, complex domain history.\n**When no:** Simple CRUD admin, team lacks ES ops experience.\n\n**Architect:** Pair with snapshots for large aggregates; CQRS read side for queries."),
            ("CRDT Introduction", "Distributed Data", "Explain CRDTs and a production use case for architects.",
             "Conflict-free Replicated Data Types merge without coordination — commutative/associative updates. Used for collaborative editing, counters, shopping carts in offline-first apps.",
             "**Types:**\n- **G-Counter** — grow-only counter per node\n- **LWW-Register** — last-write-wins with timestamp\n- **OR-Set** — add/remove set with tombstones\n\n**Use case:** Google Docs-style merge; Redis CRDT modules for geo-distributed counters.\n\n**Architect:** CRDTs trade semantic simplicity for guaranteed convergence — document merge semantics to product."),
            ("Vector Clocks", "Time", "When use vector clocks instead of Lamport timestamps?",
             "Vector clocks track concurrent events across nodes — detect true concurrency. Lamport only gives causal order, not concurrency detection.",
             "**Vector clock:** Each node maintains array of logical counters per node.\n\n**Use when:** Detecting conflicts for manual/automatic merge (Dynamo-style).\n\n**Cost:** O(n) space per event for n nodes — not for 1000-node clusters.\n\n**Architect:** Dynamo/Voldemort conflict detection — vector clock version vectors in metadata."),
            ("Lease-Based Coordination", "Coordination", "How do leases work for distributed coordination?",
             "Grant temporary exclusive right (lease) with TTL — holder must renew or lose lock. Prevents deadlocks from crashed holders.",
             "**Pattern:** etcd lease, K8s leader election lease, blob lease in Azure.\n\n**Rules:**\n- TTL > max operation + clock skew buffer\n- Heartbeat renew before expiry\n- Fencing token on downstream writes\n\n**Architect:** Leases are foundation of K8s control plane — understand renewal failure modes."),
            ("Poison Message Handling", "Messaging", "Queue consumer fails on one message forever — architect response?",
             "After N retries, move to dead-letter queue (DLQ). Alert on DLQ depth. Fix consumer or quarantine message — never block entire queue.",
             "**Pipeline:**\n1. Retry with exponential backoff (3–5 attempts)\n2. DLQ with original payload + error + traceId\n3. Replay tool with manual approval for financial messages\n\n**Architect:** DLQ is required for every async integration — define replay runbook before production."),
            ("Message Ordering Guarantees", "Messaging", "What ordering guarantees can you promise across a distributed bus?",
             "Per-partition (Kafka key) or per-session ordering only — not global order. Design consumers to tolerate reordering outside partition.",
             "**Guarantees:**\n- **Single partition:** strict order\n- **Multiple partitions:** order per key only\n- **Multiple consumers:** competing consumers break order\n\n**Architect:** Document ordering contract per event type — payment events often need per-`orderId` partition key."),
            ("Sync vs Async Replication", "Replication", "Compare synchronous vs asynchronous database replication for architects.",
             "Sync: replica confirms before commit — CP, higher latency. Async: primary commits, replica catches up — AP, risk of data loss on primary failure.",
             "**SQL Always On sync:** zero data loss, higher write latency.\n**Async replica:** read scale, RPO > 0 on failover.\n\n**Architect:** Match replication mode to RPO/RTO in ADR — don't default async for payment ledger."),
            ("Idempotent Consumer Design", "Reliability", "Design idempotent message consumer for `PaymentCaptured` events.",
             "Store processed `eventId` in inbox table with unique constraint; business update in same transaction; duplicate insert → skip safely.",
             "**Steps:**\n1. BEGIN TX\n2. INSERT inbox(eventId) — conflict → rollback, ack\n3. UPDATE order status\n4. COMMIT\n\n**Architect:** Pair with at-least-once broker — idempotency achieves effectively-once processing."),
            ("Distributed Tracing in Sagas", "Observability", "How propagate trace context through saga choreography?",
             "Inject W3C `traceparent` in domain events and HTTP callbacks; each saga step creates child span; correlationId in saga state table for support.",
             "**Implementation:**\n- OpenTelemetry baggage for `sagaId`, `orderId`\n- Service Bus application properties carry trace context\n- Dashboard: waterfall per saga instance\n\n**Architect:** Saga debugging without traces is guesswork — mandate in platform template."),
            ("Dual-Write Problem Variants", "Messaging", "Name three dual-write failure modes and the outbox fix.",
             "DB commits, publish fails; publish succeeds, DB rolls back; partial batch failure. Outbox: single transaction writes row + event; relay publishes asynchronously.",
             "**Failure modes:**\n1. Orphan event (published, DB rolled back)\n2. Lost event (DB committed, publish failed)\n3. Duplicate event (retry without idempotency)\n\n**Architect:** Outbox + idempotent consumers is standard pattern — never dual-write without it."),
        ],
        "advanced": [
            ("2PC vs 3PC Trade-offs", "Transactions", "Compare 2PC and 3PC for distributed transactions.",
             "2PC blocks on coordinator failure after prepare. 3PC adds pre-commit phase reducing blocking but adds complexity and is rarely used in practice.",
             "**2PC:** Prepare → Commit/Abort. Blocking if coordinator dies after prepare.\n\n**3PC:** CanComplete phase — non-blocking in theory; network assumptions often violated.\n\n**Architect:** Avoid both for microservices — sagas + outbox instead. Reserve 2PC for same-DC same-team DB clusters only."),
            ("Saga Orchestration Durable Functions", "Sagas", "Implement order saga with Azure Durable Functions orchestrator.",
             "Orchestrator function calls activities with retry policies; built-in state persistence; compensation via `try/catch` with compensating activity calls.",
             "```csharp\n[FunctionName(\"OrderSaga\")]\npublic async Task Run([OrchestrationTrigger] IDurableOrchestrationContext ctx) {\n  try {\n    await ctx.CallActivityAsync(\"ReserveInventory\", input);\n    await ctx.CallActivityAsync(\"ChargePayment\", input);\n  } catch {\n    await ctx.CallActivityAsync(\"ReleaseInventory\", input);\n    throw;\n  }\n}\n```\n\n**Architect:** Durable Functions gives visible saga state — ops-friendly vs pure choreography."),
            ("Debezium CDC Outbox Relay", "Outbox", "Configure Debezium to relay outbox table to Kafka.",
             "Debezium connector reads WAL, filters `outbox` table, transforms to CloudEvents, publishes to topic — no polling load on OLTP.",
             "**Setup:**\n- Outbox table with `aggregate_id`, `event_type`, `payload`\n- Debezium Outbox Event Router SMT\n- Kafka topic per event type or single topic with headers\n\n**Architect:** CDC scales beyond polling — ops overhead for Connect cluster."),
            ("Raft Log Replication Deep", "Consensus", "Explain Raft log replication and commit index semantics.",
             "Leader appends to log; replicates to followers; commits when majority replicated; followers apply committed entries in order.",
             "**Key rules:**\n- Leader-only writes\n- Log matching: same term + index → same command\n- Commit index = highest entry known replicated on majority\n\n**Examples:** etcd, CockroachDB, Consul.\n\n**Architect:** Failover time = election timeout + catch-up replication lag."),
            ("Paxos vs Raft", "Consensus", "When would you discuss Paxos vs Raft with your team?",
             "Raft designed for understandability — same safety as Paxos. Use Raft literacy for etcd/K8s; Paxos for academic or legacy systems (Chubby).",
             "**Raft:** Leader-based, strong docs, implemented in etcd.\n**Paxos:** Multi-decree, harder to implement correctly.\n\n**Architect:** Don't build custom consensus — use etcd/Consul. Understand for vendor evaluation."),
            ("Byzantine Fault Tolerance", "Consensus", "What is Byzantine fault tolerance and do most cloud apps need it?",
             "BFT tolerates malicious or arbitrary faulty nodes — requires 3f+1 nodes for f Byzantine. Overkill for most enterprise apps; needed for blockchain, some financial networks.",
             "**PBFT:** Practical Byzantine Fault Tolerance — complex, high overhead.\n\n**Most apps:** Crash fault tolerance (Raft) sufficient — assume nodes fail-stop not malicious.\n\n**Architect:** Mention BFT awareness; default to Raft-based systems unless threat model includes malicious insiders on nodes."),
            ("SWIM Gossip Protocol", "Consensus", "How does SWIM improve failure detection over naive heartbeat?",
             "SWIM uses probing + indirect ping + suspicion states — reduces false positives and network overhead at scale.",
             "**Used in:** Consul memberlist, Cassandra influenced protocols.\n\n**States:** Alive → Suspect → Dead with configurable timeouts.\n\n**Architect:** Gossip membership is eventually consistent — brief stale routing windows during failures."),
            ("Kafka Partition Ordering", "Messaging", "Design Kafka topic partitioning for order lifecycle events.",
             "Partition by `orderId` — all events for one order in single partition — strict order per order. Scale partitions for throughput across orders.",
             "**Rules:**\n- Key = business aggregate ID\n- Partition count = max parallel consumers per group\n- Rebalance causes brief ordering blip — design idempotent consumers\n\n**Architect:** Never rely on global order across partitions — only per-key."),
            ("Exactly-Once Stream Processing", "Messaging", "Kafka EOS semantics — what is and isn't covered?",
             "Producer idempotence + transactions within Kafka — exactly-once between Kafka topics. Cross DB still needs outbox.",
             "**Covered:** Read-process-write within Kafka Streams/Flink with EOS enabled.\n**Not covered:** Kafka + PostgreSQL without outbox.\n\n**Architect:** Honest scope — EOS is bounded to streaming topology, not entire enterprise."),
            ("Distributed Lock Fencing", "Coordination", "Why fencing tokens matter with distributed locks?",
             "Stale lock holder may complete write after lock lost — fencing token (monotonic) rejected by storage if token < latest.",
             "**Martin Kleppmann critique:** Redis lock without fencing is unsafe for correctness-critical resources.\n\n**Pattern:** Lock returns fencing token → DB write checks `WHERE fencing_token < @new`.\n\n**Architect:** Use etcd leases + fencing for financial coordination; Redis locks for efficiency jobs only."),
            ("Split-Brain Redis Sentinel", "Consensus", "How can Redis Sentinel split-brain occur and how prevent?",
             "Network partition → two sentinels promote different masters → dual writes. Prevent with quorum, `min-slaves-to-write`, manual failover discipline.",
             "**Prevention:**\n- Odd sentinel count\n- `min-slaves-to-write 1`\n- Client must verify master identity\n\n**Architect:** Redis HA ≠ SQL HA semantics — document RPO/RTO honestly."),
            ("Event Sourcing Snapshot Strategy", "Event Sourcing", "When snapshot event-sourced aggregates and how implement?",
             "Snapshot every N events or time interval; load snapshot + events since version; async snapshot after commit.",
             "**Implementation:**\n- `aggregate_version` on snapshot row\n- Background worker creates snapshot\n- Schema version on snapshot blob for migration\n\n**Architect:** Snapshot without version breaks replay after schema change."),
            ("Temporal Workflow vs Durable Functions", "Sagas", "Compare Temporal and Azure Durable Functions for sagas.",
             "Temporal: language SDKs, durable timers, strong visibility UI, self-hosted or cloud. Durable Functions: Azure-native, Functions consumption model.",
             "**Temporal wins:** Complex long-running workflows, polyglot, workflow versioning.\n**Durable wins:** Azure-only shops, serverless billing, tight Functions integration.\n\n**Architect:** Evaluate ops model — Temporal cluster vs Functions managed runtime."),
            ("Process Manager Pattern", "Sagas", "Implement process manager for multi-step order fulfillment.",
             "Central state machine persists saga state; reacts to events; emits commands; handles timeouts and compensation.",
             "**State table:** `saga_id`, `current_step`, `payload`, `timeout_at`.\n\n**Handlers:** Event → transition → command(s).\n\n**Architect:** Process manager = orchestration with explicit persistence — debuggable in incidents."),
            ("Compensation Timeout Design", "Sagas", "Saga step times out — how decide compensate vs retry?",
             "Retry transient (503, timeout) with bounded attempts; compensate on business failure or max retries; escalate to human queue on compensation failure.",
             "**Policy matrix:**\n| Error | Action |\n|-------|--------|\n| 503 | Retry 3× |\n| 400 business | Compensate |\n| Timeout 30s | Query status → reconcile |\n| Compensate fail | Human workflow |\n\n**Architect:** Document per-step timeout and compensation in saga ADR."),
            ("Read Repair Cassandra", "Replication", "Explain read repair in eventually consistent stores.",
             "On read, coordinator compares replicas; returns latest; repairs stale replicas in background.",
             "**Triggered:** `QUORUM` read finds mismatched digest.\n\n**Trade-off:** Read latency spike during repair; anti-entropy complements read repair.\n\n**Architect:** Tunable consistency — `LOCAL_QUORUM` for production reads."),
            ("Hinted Handoff", "Replication", "What is hinted handoff and when does it help?",
             "Temporarily store writes for unavailable node; deliver when node returns — improves write availability during brief outages.",
             "**Risk:** If hinted node never returns, hints pile up.\n\n**Architect:** Part of AP write path — understand during node replacement procedures."),
            ("Quorum Reads vs Writes", "Replication", "Design quorum sizes for R=3 replica system.",
             "W + R > N ensures overlap — strong read if W=R=2, N=3. Tune W/R for latency vs consistency.",
             "**Example N=3:**\n- W=2, R=2 — strong consistency possible\n- W=1, R=1 — fast, stale reads\n\n**Architect:** Dynamo/Cassandra tunable — document chosen W/R per use case."),
            ("Linearizability vs Serializability", "Consistency", "Distinguish linearizability and serializability for architects.",
             "Linearizability: real-time order of ops visible to all. Serializability: transaction order exists — may not match real-time.",
             "**Linearizable:** etcd reads, Spanner external consistency.\n**Serializable:** SQL `SERIALIZABLE` isolation — not necessarily linearizable across sessions.\n\n**Architect:** Use correct term in ADR — interviewers distinguish precisely."),
            ("Causal Consistency", "Consistency", "When recommend causal consistency over strong?",
             "Social feeds, comments threads — user sees own writes and causally related updates without global strong consistency cost.",
             "**Mechanism:** Track vector clocks or version chains per object.\n\n**Cosmos:** Session consistency approximates causal for same session.\n\n**Architect:** Causal is middle ground — cheaper than strong, more intuitive than eventual."),
            ("Hybrid Logical Clocks", "Time", "How do hybrid logical clocks (HLC) work in CockroachDB?",
             "Combine physical time with logical counter — bound clock uncertainty without GPS like Spanner.",
             "**On event:** `hlc = max(physical, previous_logical) + 1` if same physical tick.\n\n**Benefit:** Causal ordering with wall-clock affinity for debugging.\n\n**Architect:** HLC enables global SQL with reasonable semantics — not magic CA."),
            ("Inbox Outbox Pairing", "Messaging", "Design end-to-end effectively-once with outbox and inbox.",
             "Publisher: outbox in same TX as write. Consumer: inbox dedup in same TX as handler. At-least-once broker between.",
             "**End-to-end:**\n1. Service A outbox → bus\n2. Service B inbox check → process → commit\n3. Duplicate delivery → inbox conflict → no-op\n\n**Architect:** Both sides required for cross-service effectively-once."),
            ("Saga Choreography Debugging", "Sagas", "Choreography saga stuck — how debug without central orchestrator?",
             "Distributed trace per correlationId; event log audit table; saga timeout scanner on each service; dead letter on missing expected event.",
             "**Tooling:**\n- Event catalog with expected next events\n- `saga_timeline` view from correlated spans\n- Alert: `OrderSubmitted` without `PaymentCaptured` in 5m\n\n**Architect:** Choreography needs superior observability — budget for it."),
            ("Conflict Resolution Dynamo", "Distributed Data", "How Dynamo-style systems resolve write conflicts?",
             "Vector clocks detect conflict; last-write-wins, merge function, or escalate to application.",
             "**Strategies:**\n- LWW with timestamp (loses data risk)\n- Application merge (shopping cart union)\n- Human resolution queue (rare)\n\n**Architect:** Document merge semantics per entity — product must accept."),
            ("Jepsen Testing Mindset", "Testing", "What is Jepsen and why should architects know it?",
             "Jepsen tests distributed databases under partition/failure — exposes consistency claims vs reality.",
             "**Famous findings:** MongoDB, Redis, RabbitMQ issues under partition.\n\n**Architect use:** Evaluate vendor HA claims; run chaos tests on your stack; don't trust marketing 'linearizable' without verification."),
            ("Chaos Engineering Distributed Tx", "Resilience", "Design chaos experiment for payment saga path.",
             "Inject payment service latency, kill inventory consumer, partition Service Bus — verify no double charge and compensation completes.",
             "**Hypothesis:** Stuck payments reconcile within 5m; no duplicate captures.\n\n**Tools:** Azure Chaos Studio, Litmus, Toxiproxy.\n\n**Architect:** Start staging; one fault per experiment; measure MTTR."),
            ("Observability Async Workflows", "Observability", "Metrics and alerts for async saga health.",
             "Track: saga completion rate, step latency p99, compensation rate, DLQ depth, stuck saga count by state.",
             "**Alerts:**\n- `stuck_sagas > 10` for 15m → page\n- `compensation_rate` spike → investigate upstream\n\n**Architect:** SLO on saga completion time — not just API latency."),
            ("Network Partition DR Drill", "DR", "Run DR drill simulating AZ partition — what verify?",
             "Quorum behavior, write rejection on minority side, failover RTO, no split-brain writes, message backlog recovery.",
             "**Checklist:**\n- [ ] CP systems reject writes on minority\n- [ ] AP systems document stale read window\n- [ ] Runbook executed within RTO\n- [ ] Post-drill ADR updates\n\n**Architect:** Partition drills prove CAP choices — schedule quarterly."),
            ("Compliance Eventual Consistency", "Compliance", "Auditor asks about eventual consistency in financial reporting — respond?",
             "Authoritative ledger is CP with audit trail; reports are async projections with defined lag SLA; reconciliation job proves completeness.",
             "**Artifacts:**\n- Immutable event log\n- Daily reconciliation report\n- Lag SLA documented (e.g. 15m for analytics)\n\n**Architect:** Separate compliance path from AP read models."),
            ("Multi-Region Active-Active Conflicts", "Architecture", "Design conflict handling for active-active orders in two regions.",
             "Partition by customer region as primary; CRDT or LWW with business merge rules; avoid dual-primary same aggregate.",
             "**Patterns:**\n- Home region per customerId\n- Async replication for DR read\n- Conflict queue for true concurrent writes (rare)\n\n**Architect:** Active-active is hard — default active-passive unless revenue justifies complexity."),
        ],
        "expert": [
            ("Global Order System Design", "Architecture", "Design globally distributed order system with 99.99% availability.",
             "Region-local write path with home shard per customer; async cross-region replication; saga orchestration; idempotency everywhere; CP payment partition.",
             "**Architecture:**\n- Home region assignment via geo-DNS + sticky routing\n- Order aggregate CP within region\n- Cross-region: event replication for analytics only\n- Payment: region-local PSP with failover runbook\n\n**Trade-offs:** Cross-region order view eventual; acceptable for support tools not checkout."),
            ("Financial Ledger Event Sourcing", "Event Sourcing", "Design immutable financial ledger with event sourcing.",
             "Append-only journal; double-entry as event pairs; snapshot for balance queries; regulatory export from event stream.",
             "**Events:** `DebitPosted`, `CreditPosted` — never delete; compensating events for reversal.\n\n**Controls:** Hash chain per account; daily balance reconciliation; WORM storage for archive.\n\n**Architect:** Ledger is CP — reject write if quorum lost."),
            ("Outbox at 100K TPS", "Outbox", "Scale transactional outbox to 100K events/sec.",
             "Partition outbox table; CDC (Debezium) not polling; batch publish; separate relay per partition; monitor relay lag SLO.",
             "**Schema:** `outbox` partitioned by `aggregate_id` hash.\n\n**Relay:** Kafka Connect with multiple tasks; idempotent producer.\n\n**Bottleneck watch:** DB WAL throughput — may need dedicated event store."),
            ("Spanner TrueTime Tradeoffs", "Consensus", "When Spanner-style TrueTime is worth the cost?",
             "External consistency globally when business pays for GPS/atomic clocks and Google-scale ops — rare for typical enterprise.",
             "**TrueTime:** Bounded clock uncertainty → global transactions.\n\n**Alternatives:** CockroachDB HLC, per-region CP with async replication.\n\n**Architect:** Honest TCO — Spanner/TrueTime class for regulatory global SQL at scale only."),
            ("Jepsen-Style Testing Program", "Testing", "Establish Jepsen-style distributed systems test program.",
             "Chaos partition injection in staging; consistency oracles; automated invariant checks; run before major DB/middleware upgrades.",
             "**Program:**\n1. Define invariants (no lost writes, no double apply)\n2. Fault injection library\n3. CI weekly chaos job\n4. Report for architecture review board\n\n**Architect:** Vendor claims validated by your tests — not slides."),
            ("Formal Saga Verification", "Sagas", "Can saga correctness be formally verified?",
             "Model saga as state machine; verify compensation completeness, deadlock freedom, reachable terminal states — tools: TLA+, Alloy for critical paths.",
             "**Worth it when:** Payment platform, regulatory scrutiny, complex compensation trees.\n\n**Pragmatic:** State machine unit tests + chaos for most teams.\n\n**Architect:** TLA+ for Tier-0 sagas — ADR documents model."),
            ("Incident Split-Brain Postmortem", "Operations", "Lead postmortem after split-brain caused duplicate charges.",
             "Timeline reconstruction, quorum config review, fencing gaps, customer remediation, ADR for prevention — blameless with exec summary.",
             "**Actions:**\n- Fix quorum/witness\n- Add fencing tokens\n- Reconciliation job for duplicates\n- Game day quarterly\n\n**Architect:** Split-brain postmortem is career-defining — demonstrate leadership."),
            ("Custom Saga Coordinator Scale", "Sagas", "Build custom saga coordinator for 50-step B2B workflows.",
             "Persistent state machine, horizontal workers with shard by sagaId, lease per saga, visibility API, versioned saga definitions.",
             "**Scale:** Partition saga table; single writer per sagaId; async step dispatch via queue.\n\n**Architect:** Custom coordinator when Temporal/Durable insufficient — high maintenance — justify in ADR."),
            ("WAN Partition CAP Exercise", "Fundamentals", "Walk through CAP choices during WAN partition for your platform.",
             "Per-component: SQL CP (reject), cache AP (stale), queue buffer (AP with backlog), search AP — document user-visible behavior each.",
             "**Deliverable:** CAP matrix in runbook; support scripts for partition mode; executive comms template.\n\n**Architect:** Pre-written partition playbook reduces incident panic."),
            ("CRDT Shopping Cart Global", "Distributed Data", "Design globally available shopping cart with CRDT merge.",
             "OR-Set for line items; LWW for quantities; merge on sync; TTL for abandoned carts; conflict-free add/remove.",
             "**Client:** Offline add items; sync merges with server state.\n\n**Product:** Accept merge semantics — duplicate SKU merges quantity.\n\n**Architect:** CRDT cart + CP checkout at payment boundary."),
            ("Disaster Recovery Event Sourced", "DR", "DR strategy for event-sourced platform.",
             "Replicate event log cross-region; replay projections in DR; snapshot + log shipping; RPO = replication lag; test full replay quarterly.",
             "**Components:**\n- Primary event store replication\n- Projection rebuild automation\n- Snapshot restore + catch-up\n\n**Architect:** DR test must include projection rebuild time — not just failover DNS."),
            ("Async Workflow Compliance Audit", "Compliance", "Prove async workflow audit trail to regulators.",
             "Immutable event log, correlation IDs, signed events, retention policy, query API for auditor, reconciliation proofs.",
             "**Controls:**\n- WORM storage 7 years\n- Hash chain integrity checks\n- Access audit for log queries\n\n**Architect:** Compliance by design — not retrofit logging."),
            ("Consensus Under Load Test", "Consensus", "etcd quorum degrades under load test — expert analysis path.",
             "Check disk latency, election timeouts, network, defrag schedule, member count — tune heartbeat and election timeout; add members or faster disks.",
             "**K8s impact:** Slow etcd → API server latency → whole cluster sick.\n\n**Architect:** etcd on dedicated SSD; monitor `etcd_disk_wal_fsync_duration`."),
            ("Designing for Message Loss", "Messaging", "Broker may lose messages under catastrophic failure — architect response?",
             "Acknowledged trade-off; critical events dual-write to audit log; outbox retained until consumer ack; periodic reconciliation between services.",
             "**Tier-0:** No message-only path — sync confirmation or persistent outbox until ack.\n\n**Architect:** Honest about broker guarantees — design reconciliation safety nets."),
            ("Distributed Systems Interview Panel", "Career", "Principal panel: defend AP choice for cart with CP payment.",
             "Cart AP for availability and merge; checkout boundary transitions to CP saga; clear UX states; monitoring on transition failures.",
             "**Narrative:** Separate consistency concerns by lifecycle phase — not one global choice.\n\n**Architect:** Panel wants nuanced CAP — not absolutes."),
            ("Latency SLO Cross-Region Saga", "SLO", "SLO 500ms checkout with cross-region inventory — feasible?",
             "Analyze hop budget; likely need regional inventory read replica sync; async reserve with sync confirm only if local stock; or regional fulfillment cells.",
             "**Math:** 3× 50ms cross-region RTT = 150ms network alone — tight.\n\n**Architect:** SLO drives topology — may require cell-based architecture."),
            ("Event Log Compaction Policy", "Event Sourcing", "When compact/delete events in event-sourced system?",
             "Never delete compliance events; compact snapshots replace need for full replay for aggregates; archive cold events to glacier with legal hold.",
             "**Policy:**\n- Hot: full log online\n- Warm: snapshots + recent events\n- Cold: archive immutable\n\n**Architect:** Legal retention overrides technical compaction desires."),
            ("Teaching CAP to Executives", "Communication", "Explain CAP trade-off to non-technical executive in 2 minutes.",
             "During network split, we choose: pause sales (consistent) or allow both offices to sell with later reconciliation (available) — we document choice per business risk.",
             "**Analogy:** Two cash registers disconnected — one ledger (pause) vs both sell reconcile later.\n\n**Architect:** Executive clarity prevents unrealistic 'never down never wrong' demands."),
            ("Research vs Production Consensus", "Consensus", "Team wants custom Raft — expert response?",
             "Redirect to etcd/Consul; if custom needed, fork battle-tested lib, security review, Jepsen testing, long-term maintenance budget.",
             "**Reality:** Consensus bugs surface years later.\n\n**Architect:** 'Not invented here' on consensus is red flag — escalate to principal."),
            ("Platform-Wide Idempotency Standard", "Governance", "Mandate idempotency standard across 40 microservices.",
             "HTTP `Idempotency-Key` on POST; message `eventId` dedup; SDK middleware; CI lint; catalog documents per endpoint.",
             "**Governance:**\n- Platform library for idempotency store\n- Breaking PR check without key on mutating APIs\n- Metrics: duplicate request rate\n\n**Architect:** Standards beat per-team reinventing inbox tables."),
        ],
    },
    # Weeks 22-28 continue with same structure — generated below via helper
}

# Additional week definitions (compact topic seeds expanded by _expand)
_WEEK_SEEDS: dict[int, dict[str, list[tuple[str, str]]]] = {
    22: {
        "intermediate": [
            ("Strangler Fig Routing", "Migration"), ("Sidecar Pattern", "Microservices"), ("Ambassador Pattern", "Microservices"),
            ("Anti-Corruption at Gateway", "Gateway"), ("Rate Limiting Per Tenant", "Gateway"), ("JWT Validation at Edge", "Security"),
            ("Service Discovery Client", "Discovery"), ("Client-Side Load Balancing", "Resilience"), ("Server-Side Load Balancing", "Resilience"),
            ("Health Probe Design", "Operations"),
        ],
        "advanced": [
            ("API Gateway Rate Limit Tiers", "Gateway"), ("GraphQL vs REST Gateway", "API Design"), ("mTLS Service Mesh", "Security"),
            ("Canary Deployment Microservices", "Deployment"), ("Blue-Green Two Services", "Deployment"), ("Feature Flag Service Routing", "Operations"),
            ("Distributed Config Refresh", "Operations"), ("Secrets Rotation Microservices", "Security"), ("Zero Trust East-West", "Security"),
            ("Event-Driven Autoscaling", "Scale"), ("KEDA on Queue Depth", "Scale"), ("CQRS Read Service Extraction", "Decomposition"),
            ("Extract Shared Library", "Decomposition"), ("Domain Service Extraction Criteria", "Decomposition"), ("Synchronous Chain Refactor", "Anti-Patterns"),
            ("Distributed Monolith Detection", "Anti-Patterns"), ("Nano-Service Consolidation", "Anti-Patterns"), ("Backends for Frontends Governance", "BFF"),
            ("Mobile BFF Caching", "BFF"), ("Partner API Gateway", "Gateway"), ("Internal vs External API Split", "API Design"),
            ("Webhook Ingestion Service", "Integration"), ("Polling vs Push Integration", "Integration"), ("API Composition Timeout Tree", "Resilience"),
            ("Retry Storm Prevention", "Resilience"), ("Hedged Requests", "Resilience"), ("Adaptive Concurrency Limits", "Resilience"),
            ("Service Catalog Ownership", "Governance"), ("Deprecation Sunset Workflow", "Governance"), ("Multi-Team API Review Board", "Governance"),
        ],
        "expert": [
            ("Microservices Platform Reference Architecture", "Architecture"), ("Cell-Based Microservices", "Architecture"),
            ("Multi-Tenant Microservices Isolation", "Architecture"), ("Regulatory Boundary Services", "Compliance"),
            ("Extract Monolith Under Fire", "Migration"), ("Merger Integration Microservices", "Migration"),
            ("Global Traffic Management", "Scale"), ("Latency-Based Routing", "Scale"), ("Cold Start Microservices", "Performance"),
            ("Service Mesh at 200 Services", "Infrastructure"), ("Mesh Exit Strategy", "Infrastructure"),
            ("Principal Review Microservice Split", "Career"), ("Defend Fewer Services", "Career"),
            ("Incident Cascading Failure", "Operations"), ("Postmortem Chatty Services", "Operations"),
            ("FinOps Per Microservice", "FinOps"), ("Right-Size Microservice Fleet", "FinOps"),
            ("Platform Engineering Golden Path", "Platform"), ("Developer Portal Microservices", "Platform"),
            ("Mock Architect Gateway Design", "Interview"), ("Whiteboard Decomposition", "Interview"),
        ],
    },
    23: {
        "intermediate": [
            ("Aggregate Size Guidelines", "DDD"), ("Domain Exception Design", "DDD"), ("Application Service Role", "DDD"),
            ("Infrastructure Layer Boundaries", "DDD"), ("DTO vs Domain Model", "DDD"), ("Mapping Layer AutoMapper", "DDD"),
            ("Integration Event Translation", "Events"), ("Event Version Upcasting", "Events"), ("Saga Process Manager DDD", "Sagas"),
            ("Read Model Projection Handlers", "CQRS"),
        ],
        "advanced": [
            ("Tactical DDD in .NET", "DDD"), ("EF Core Owned Types", "Persistence"), ("Aggregate Persistence Mapping", "Persistence"),
            ("Domain Event Dispatch Pipeline", "Events"), ("MediatR Domain Events", "Events"), ("Outbox from Domain Events", "Events"),
            ("Bounded Context Integration ACL", "Integration"), ("Partnership Context Map", "Context Map"), ("Shared Kernel Risks", "Context Map"),
            ("Subdomain Classification", "Strategic DDD"), ("Core vs Supporting Subdomain", "Strategic DDD"), ("Generic Subdomain Buy", "Strategic DDD"),
            ("Event Storming Output to ADR", "Discovery"), ("Big Picture vs Process Level", "Discovery"), ("Hot Spot Resolution Workshop", "Discovery"),
            ("Policy Object Composition", "DDD"), ("Specification SQL Translation", "DDD"), ("Value Object Validation", "DDD"),
            ("Entity Identity Generation", "DDD"), ("Domain Model Unit Testing", "Testing"), ("Architecture Tests DDD", "Testing"),
            ("Modular Monolith NetArchTest", "Testing"), ("Extract Bounded Context Checklist", "Strategy"), ("Context Map Maintenance", "Governance"),
            ("Published Language Versioning", "Integration"), ("OHS Rate Limits", "Integration"), ("Customer Supplier SLA", "Integration"),
            ("Conformist Stripe Model", "Integration"), ("ACL Legacy ERP Testing", "Integration"),
            ("Domain Service Interface Placement", "DDD"),
        ],
        "expert": [
            ("Strategic DDD Merger", "Strategy"), ("Domain Expert Engagement Program", "Strategy"),
            ("DDD in Data Mesh", "Architecture"), ("Event Sourced Aggregate Expert", "Event Sourcing"),
            ("Large Aggregate Split", "DDD"), ("Cross-Context Invariant Saga", "Sagas"),
            ("Teaching DDD to Skeptical Team", "Leadership"), ("DDD Anti-Pattern Intervention", "Leadership"),
            ("Principal Bounded Context Challenge", "Career"), ("Context Map Executive Presentation", "Communication"),
            ("Legacy Anemic Model Migration", "Migration"), ("DDD with Microservices Extraction", "Migration"),
            ("Domain Model Evolution Strategy", "Governance"), ("Ubiquitous Language Governance", "Governance"),
            ("Event Storming at Scale", "Discovery"), ("Remote DDD Workshop", "Discovery"),
            ("CQRS Event Replay Disaster", "Operations"), ("Projection Rebuild Runbook", "Operations"),
            ("Expert Panel DDD Questions", "Interview"), ("Defend Modular Monolith DDD", "Interview"),
        ],
    },
    24: {
        "intermediate": [
            ("Capstone Context Diagram", "Capstone"), ("Capstone Container Diagram", "Capstone"), ("Capstone Deployment View", "Capstone"),
            ("Capstone NFR Matrix", "Capstone"), ("Capstone Threat Model Summary", "Capstone"), ("Capstone Cost Estimate", "Capstone"),
            ("Capstone Demo Script", "Capstone"), ("Capstone Rollback Plan", "Capstone"), ("Capstone Feature Flag Plan", "Capstone"),
            ("Capstone Data Flow Diagram", "Capstone"),
        ],
        "advanced": [
            ("Capstone Saga State Machine", "Capstone"), ("Capstone Payment Webhook Flow", "Capstone"), ("Capstone Inventory Hot SKU", "Capstone"),
            ("Capstone Notification DLQ", "Capstone"), ("Capstone Trace Demo", "Capstone"), ("Capstone SLO Dashboard", "Capstone"),
            ("Capstone Contract Test CI", "Capstone"), ("Capstone Load Test Report", "Capstone"), ("Capstone Chaos Results", "Capstone"),
            ("Capstone DR Failover Test", "Capstone"), ("Capstone Schema Registry", "Capstone"), ("Capstone API Version Policy", "Capstone"),
            ("Capstone On-Call Rotation", "Capstone"), ("Capstone Runbook Index", "Capstone"), ("Capstone Security Scan Gate", "Capstone"),
            ("Capstone Multi-Region Sketch", "Capstone"), ("Capstone FinOps Tags", "Capstone"), ("Capstone Team Topology Map", "Capstone"),
            ("Capstone PRR Checklist", "Capstone"), ("Capstone Incident Simulation", "Capstone"), ("Capstone Idempotency Audit", "Capstone"),
            ("Capstone BFF Mobile Web", "Capstone"), ("Capstone Gateway Policies", "Capstone"), ("Capstone Event Catalog", "Capstone"),
            ("Capstone Read Model Lag", "Capstone"), ("Capstone Deployment Pipeline", "Capstone"), ("Capstone Observability Budget", "Capstone"),
            ("Capstone Strangler Status", "Capstone"), ("Capstone Shared DB Exit", "Capstone"), ("Capstone Merge Services Review", "Capstone"),
        ],
        "expert": [
            ("Capstone Principal Defense", "Capstone"), ("Capstone Scale 10x Extension", "Capstone"),
            ("Capstone Acquisition Scenario", "Capstone"), ("Capstone Compliance Audit", "Capstone"),
            ("Capstone Black Friday War Room", "Capstone"), ("Capstone Payment Outage", "Capstone"),
            ("Capstone Data Breach Response", "Capstone"), ("Capstone Cost Cut 30 Percent", "Capstone"),
            ("Capstone Team Conway Reorg", "Capstone"), ("Capstone Platform Extraction", "Capstone"),
            ("Capstone Mock Interview 45min", "Interview"), ("Capstone Weak Point Drill", "Interview"),
            ("Capstone Executive BLUF", "Communication"), ("Capstone Board Risk Slide", "Communication"),
            ("Capstone Retrospective Month 6", "Career"), ("Capstone Portfolio Narrative", "Career"),
            ("Capstone Open Source Strategy", "Strategy"), ("Capstone Vendor Lock-In ADR", "Strategy"),
            ("Capstone Multi-Cloud Sketch", "Architecture"), ("Capstone Cell Architecture Future", "Architecture"),
        ],
    },
    25: {
        "intermediate": [
            ("Container Image Signing", "Docker"), ("Docker Content Trust", "Docker"), ("OCI Image Spec", "Docker"),
            ("Distroless Images", "Docker"), ("Chiseled .NET Images", "Docker"), ("BuildKit Cache Mounts", "Docker"),
            ("Docker Scout Scanning", "Docker"), ("ACR Tasks Build", "Docker"), ("Container Registry Geo-Replication", "Docker"),
            ("Docker Desktop vs Linux Engine", "Docker"),
        ],
        "advanced": [
            ("Multi-Arch Image Build", "Docker"), ("ARM64 Container Pipeline", "Docker"), ("Windows vs Linux Containers", "Docker"),
            ("Container Supply Chain SBOM", "Security"), ("Sigstore Cosign", "Security"), ("Admission Image Policy", "Security"),
            ("Docker Compose Profiles", "Docker"), ("Testcontainers in CI", "Testing"), ("Container Debug Ephemeral", "Operations"),
            ("PID 1 Signal Handling", "Docker"), ("Graceful Shutdown Container", "Docker"), ("Init Process dumb-init", "Docker"),
            ("Volume Driver Selection", "Storage"), ("Bind Mount Dev Only", "Storage"), ("Named Volume Production", "Storage"),
            ("Docker Network Overlay", "Networking"), ("Container DNS Resolution", "Networking"), ("Host Network When", "Networking"),
            ("Resource Limit OOM Behavior", "Operations"), ("CPU Throttling cgroups", "Operations"), ("Memory Swap Container", "Operations"),
            ("Image Layer Cache CI", "CI/CD"), ("Kaniko Build Cluster", "CI/CD"), ("Buildah Rootless Build", "CI/CD"),
            ("Container Image Promotion", "CI/CD"), ("Immutable Image Tags", "CI/CD"), ("Image Retention Policy", "Governance"),
            ("Dockerfile Lint Gate", "Governance"), ("Base Image Update Bot", "Governance"), ("Golden Base Image Program", "Platform"),
            ("Sidecar Container Pattern", "Kubernetes"), ("Ambassador Container Pattern", "Kubernetes"), ("Adapter Container Pattern", "Kubernetes"),
        ],
        "expert": [
            ("Container Platform Strategy", "Architecture"), ("Container vs Serverless ADR", "Architecture"),
            ("Rootless Kubernetes Nodes", "Security"), ("Seccomp AppArmor Profiles", "Security"),
            ("Container Escape Mitigation", "Security"), ("Supply Chain Attack Response", "Security"),
            ("Multi-Tenant Container Isolation", "Architecture"), ("Noisy Neighbor Container", "Operations"),
            ("Container Fleet FinOps", "FinOps"), ("Image Bloat Executive Report", "FinOps"),
            ("Principal Container Review", "Career"), ("Defend VMs Not Containers", "Career"),
            ("Container Incident OOMKill", "Operations"), ("Registry Outage Runbook", "Operations"),
            ("Build Pipeline Compromise", "Security"), ("SBOM Audit Regulator", "Compliance"),
            ("Expert Dockerfile Review", "Interview"), ("Whiteboard Container CI", "Interview"),
            ("Future WASM Containers", "Architecture"), ("MicroVM gVisor Tradeoffs", "Architecture"),
        ],
    },
    26: {
        "intermediate": [
            ("Pod Lifecycle Phases", "Kubernetes"), ("Pod Restart Policy", "Kubernetes"), ("Init Containers Use", "Kubernetes"),
            ("Sidecar Containers K8s", "Kubernetes"), ("ConfigMap vs Secret", "Kubernetes"), ("Downward API", "Kubernetes"),
            ("Service ClusterIP", "Kubernetes"), ("Headless Service", "Kubernetes"), ("Ingress vs Gateway API", "Kubernetes"),
            ("Namespace Strategy", "Kubernetes"),
        ],
        "advanced": [
            ("Deployment Rolling Update", "Kubernetes"), ("Deployment maxSurge maxUnavailable", "Kubernetes"), ("ReplicaSet vs Deployment", "Kubernetes"),
            ("StatefulSet Ordered Pods", "Kubernetes"), ("DaemonSet Node Agent", "Kubernetes"), ("Job vs CronJob", "Kubernetes"),
            ("Resource Requests Limits", "Kubernetes"), ("LimitRange Namespace", "Kubernetes"), ("ResourceQuota Team", "Kubernetes"),
            ("HPA CPU Memory", "Kubernetes"), ("VPA Recommendation", "Kubernetes"), ("PDB minAvailable", "Kubernetes"),
            ("Liveness Readiness Startup", "Kubernetes"), ("Probe Timeout Tuning", "Kubernetes"), ("Graceful Termination preStop", "Kubernetes"),
            ("RBAC Role Binding", "Kubernetes"), ("ServiceAccount Per App", "Kubernetes"), ("NetworkPolicy Default Deny", "Kubernetes"),
            ("PersistentVolume CSI", "Storage"), ("StorageClass Dynamic", "Storage"), ("Volume Snapshot Backup", "Storage"),
            ("Kustomize vs Helm", "GitOps"), ("Helm Chart Structure", "GitOps"), ("GitOps Flux ArgoCD", "GitOps"),
            ("AKS Node Pool Strategy", "Azure"), ("AKS Azure CNI", "Azure"), ("AKS Workload Identity", "Azure"),
            ("kubectl Debug Ephemeral", "Operations"), ("kubectl Top Metrics", "Operations"), ("Events Field Path", "Operations"),
            ("Label Selector Best Practices", "Governance"), ("Annotation Standards", "Governance"), ("Label Cardinality Trap", "Governance"),
        ],
        "expert": [
            ("Kubernetes Platform ADR", "Architecture"), ("Multi-Cluster Strategy", "Architecture"),
            ("Cluster Autoscaler vs Karpenter", "Scale"), ("Overprovisioning Cluster", "Scale"),
            ("etcd Backup Restore", "Operations"), ("Control Plane Outage", "Operations"),
            ("AKS Private Cluster", "Security"), ("Pod Security Standards", "Security"),
            ("Admission Webhook Custom", "Security"), ("OPA Gatekeeper Policies", "Security"),
            ("Principal K8s Review Panel", "Career"), ("Defend Managed PaaS Over K8s", "Career"),
            ("Cluster Upgrade Game Day", "Operations"), ("CVE Critical Image Block", "Security"),
            ("FinOps Cluster Right-Size", "FinOps"), ("Idle Namespace Cleanup", "FinOps"),
            ("Expert Troubleshoot CrashLoop", "Interview"), ("Whiteboard K8s Architecture", "Interview"),
            ("Service Mesh on AKS Decision", "Architecture"), ("Ingress Controller Selection", "Architecture"),
            ("Kubernetes API Rate Limits", "Operations"), ("Large Cluster Federation", "Architecture"),
        ],
    },
    27: {
        "intermediate": [
            ("Horizontal Pod Autoscaler Custom Metrics", "Kubernetes"), ("KEDA ScaledObject", "Kubernetes"), ("Cluster Autoscaler Triggers", "Kubernetes"),
            ("Pod Disruption Budget Game Day", "Kubernetes"), ("Pod Topology Spread", "Kubernetes"), ("Affinity Anti-Affinity", "Kubernetes"),
            ("Taints Tolerations", "Kubernetes"), ("Node Selector Pools", "Kubernetes"), ("GPU Node Pool", "Kubernetes"),
            ("Ingress TLS cert-manager", "Kubernetes"),
        ],
        "advanced": [
            ("Istio Traffic Splitting", "Service Mesh"), ("Istio mTLS STRICT", "Service Mesh"), ("Linkerd vs Istio", "Service Mesh"),
            ("Envoy Filter Extension", "Service Mesh"), ("Sidecar Resource Tuning", "Service Mesh"), ("Ambient Mesh Evaluation", "Service Mesh"),
            ("Cilium eBPF Networking", "Networking"), ("Calico Network Policy", "Networking"), ("Multus Multiple Interfaces", "Networking"),
            ("ExternalDNS Automation", "Networking"), ("CoreDNS Custom", "Networking"), ("Service Mesh Observability", "Observability"),
            ("Prometheus Operator", "Observability"), ("Grafana Dashboards K8s", "Observability"), ("Alertmanager Routing", "Observability"),
            ("Velero Cluster Backup", "DR"), ("Cross-Region Cluster DR", "DR"), ("etcd Defrag Schedule", "Operations"),
            ("AKS Maintenance Window", "Azure"), ("AKS Stop Start Dev", "Azure"), ("AKS Monitor Container Insights", "Azure"),
            ("Helm Release Rollback", "GitOps"), ("ArgoCD Sync Waves", "GitOps"), ("Canary Argo Rollouts", "GitOps"),
            ("Secrets Store CSI Driver", "Security"), ("External Secrets Operator", "Security"), ("Sealed Secrets GitOps", "Security"),
            ("Falco Runtime Security", "Security"), ("Kyverno Policy", "Security"), ("Workload Identity Federation", "Security"),
        ],
        "expert": [
            ("Multi-Cluster GitOps", "Architecture"), ("Hub Spoke Cluster Model", "Architecture"),
            ("Kubernetes at 500 Nodes", "Scale"), ("API Server Bottleneck", "Scale"),
            ("Mesh mTLS Performance", "Performance"), ("Sidecar Memory Fleet Cost", "FinOps"),
            ("Cluster Blast Radius Design", "Security"), ("Tenant Isolation Namespace", "Security"),
            ("Expert AKS Architecture Review", "Career"), ("Defend Serverless Over K8s", "Career"),
            ("Control Plane Incident Commander", "Operations"), ("Data Plane Partition", "Operations"),
            ("Zero-Downtime Node Upgrade", "Operations"), ("CVE Warp Speed Patch", "Security"),
            ("FinOps Cluster Consolidation", "FinOps"), ("Spot Instances Stateful", "FinOps"),
            ("Expert Mesh Troubleshoot", "Interview"), ("Whiteboard K8s Scale Design", "Interview"),
            ("Fleet Management Strategy", "Platform"), ("Platform Team K8s API", "Platform"),
            ("Future Kubernetes Gateway API", "Architecture"), ("eBPF Service Mesh Future", "Architecture"),
        ],
    },
    28: {
        "intermediate": [
            ("systemd Unit Files", "Linux"), ("journalctl Log Query", "Linux"), ("logrotate Configuration", "Linux"),
            ("ulimit File Descriptors", "Linux"), ("TCP Tuning sysctl", "Linux"), ("ss vs netstat", "Linux"),
            ("dig nslookup DNS Debug", "Linux"), ("curl HTTP Debug", "Linux"), ("tcpdump Packet Capture", "Linux"),
            ("strace Syscall Trace", "Linux"),
        ],
        "advanced": [
            ("vmstat iostat Analysis", "Linux"), ("sar Historical Metrics", "Linux"), ("perf CPU Profiling", "Linux"),
            ("htop Load Average", "Linux"), ("Memory cgroup OOM", "Linux"), ("Swap Strategy Servers", "Linux"),
            ("Disk IO Scheduler", "Linux"), ("LVM Volume Management", "Linux"), ("XFS vs ext4", "Linux"),
            ("NFS Mount Performance", "Storage"), ("iSCSI Initiator", "Storage"), ("RAID Levels Tradeoffs", "Storage"),
            ("iptables vs nftables", "Networking"), ("ip route Policy Routing", "Networking"), ("conntrack Table Full", "Networking"),
            ("SELinux Troubleshooting", "Security"), ("AppArmor Profiles", "Security"), ("sudo Audit Logging", "Security"),
            ("SSH Hardening", "Security"), ("Fail2ban Brute Force", "Security"), ("PAM Authentication", "Security"),
            ("cron vs systemd Timer", "Operations"), ("at Batch Schedule", "Operations"), ("Ansible Idempotent", "Operations"),
            ("Package Manager Pinning", "Operations"), ("Unattended Upgrades Risk", "Operations"), ("Kernel Upgrade Rollback", "Operations"),
            ("NTP chrony Sync", "Operations"), ("Timezone UTC Standard", "Operations"), ("Locale UTF-8", "Operations"),
        ],
        "expert": [
            ("Linux Platform Architecture", "Architecture"), ("Immutable Infrastructure Linux", "Architecture"),
            ("Kernel Panic Postmortem", "Operations"), ("Hardware Failure Diagnosis", "Operations"),
            ("Performance Regression Linux", "Performance"), ("Noisy Neighbor Host", "Performance"),
            ("Security Incident Linux Forensics", "Security"), ("Rootkit Detection", "Security"),
            ("Capacity Planning Linux Fleet", "FinOps"), ("Right-Size VM SKUs", "FinOps"),
            ("Expert strace Production", "Operations"), ("Production tcpdump Safely", "Operations"),
            ("Principal Linux Review", "Career"), ("Defend Windows Server", "Career"),
            ("eBPF Observability Linux", "Observability"), ("bpftrace Ad Hoc", "Observability"),
            ("Container Host Linux Tuning", "Kubernetes"), ("Kubelet Resource Reserved", "Kubernetes"),
            ("Expert Linux Interview Scenario", "Interview"), ("Whiteboard Linux Troubleshoot", "Interview"),
            ("Linux Automation Platform", "Platform"), ("Golden AMI Pipeline", "Platform"),
            ("Future systemd vs Alternatives", "Architecture"), ("Rust Linux Userspace Tools", "Architecture"),
        ],
    },
}


def _expand_seed(week: int, tier: str, title: str, category: str, idx: int) -> Question:
    """Expand a compact seed into a full premium question tuple."""
    tier_label = {"intermediate": "Intermediate", "advanced": "Advanced", "expert": "Expert"}[tier]
    q_text = f"Architect-level {tier_label}: {title} — what do you need to know and decide?"
    short = (
        f"{title} requires understanding trade-offs, production failure modes, and clear ADR documentation "
        f"for Week {week} ({tier_label} tier)."
    )
    detailed = textwrap.dedent(f"""\
        **Context (Week {week} — {category}):**
        - Scenario: production system at scale needs a decision involving *{title}*
        - Constraints: reliability, security, cost, and team skill must be explicit

        **Architect approach:**
        1. Clarify requirements and NFRs (latency, RPO/RTO, compliance)
        2. List two viable options with pros/cons
        3. Choose with documented trade-offs in ADR
        4. Define verification: metrics, alerts, game day, rollback

        **Production checklist:**
        - Runbook entry exists
        - Observability: metric + log + trace
        - Security review for external exposure
        - FinOps tag and cost estimate

        **Interview tip:** Lead with business impact, then mechanism, then operational guardrails.""")
    perspective = (
        f"{tier_label} interviewers expect you to connect {title} to real operations — "
        f"not definitions alone. Show governance and measurable outcomes."
    )
    fu1 = f"What metrics prove {title} is healthy in production?"
    fu2 = f"What is the rollback plan if {title} change fails?"
    m1 = f"Treating {title} as set-and-forget with no monitoring"
    m2 = f"No ADR documenting trade-offs for {title}"
    m3 = f"Copying {title} pattern from blog without context fit"
    freq = "Very Common" if tier == "intermediate" else ("Common" if tier == "advanced" else "Occasional")
    return (title, category, freq, q_text, short, detailed, perspective, fu1, fu2, m1, m2, m3)


def _expand_full(week: int, tier: str, title: str, category: str, question: str, short: str, detailed: str) -> Question:
    perspective = (
        f"Week {week} {tier} depth on {category} — interviewers want mechanism plus operational guardrails."
    )
    fu1 = f"How measure success after implementing {title}?"
    fu2 = f"What failure mode is most common with {title}?"
    m1 = f"Hand-wavy answer without production example for {title}"
    m2 = f"Ignoring cost or security implications of {title}"
    m3 = f"No rollback or monitoring plan for {title}"
    freq = "Very Common" if tier == "intermediate" else ("Common" if tier == "advanced" else "Occasional")
    return (title, category, freq, question, short, detailed, perspective, fu1, fu2, m1, m2, m3)


def build_all_questions() -> dict[str, list[Question]]:
    result: dict[str, list[Question]] = {}
    tier_suffix = {
        "intermediate": "_I_EXTRA",
        "advanced": "_ADVANCED",
        "expert": "_EXPERT",
    }
    counts = {"intermediate": 10, "advanced": 30, "expert": 20}

    for week in range(21, 29):
        for tier in ("intermediate", "advanced", "expert"):
            export_key = f"W{week}{tier_suffix[tier]}"
            items: list[Question] = []

            if week in WEEK_TOPICS and tier in WEEK_TOPICS[week]:
                for entry in WEEK_TOPICS[week][tier]:
                    title, cat, question, short, detailed = entry
                    items.append(_expand_full(week, tier, title, cat, question, short, detailed))

            seeds = _WEEK_SEEDS.get(week, {}).get(tier, [])
            for i, (title, cat) in enumerate(seeds):
                items.append(_expand_seed(week, tier, title, cat, i))

            need = counts[tier]
            if len(items) < need:
                raise ValueError(f"Week {week} {tier}: have {len(items)}, need {need}")
            result[export_key] = items[:need]
    return result


def render_file(data: dict[str, list[Question]]) -> str:
    lines = [
        '"""Extra premium Q&A tuples for Weeks 21–28 banks (480 questions)."""',
        "",
        "from premium_qa_data import q",
        "",
        "",
        "def _qs(rows):",
        "    return [q(*r) for r in rows]",
        "",
    ]
    for name, rows in sorted(data.items(), key=lambda x: (int(x[0][1:3]), x[0])):
        lines.append(f"{name} = _qs([")
        for row in rows:
            lines.append("    (")
            for field in row:
                lines.append(f"     {field!r},")
            lines.append("    ),")
        lines.append("])")
        lines.append("")
    return "\n".join(lines) + "\n"


def main():
    data = build_all_questions()
    content = render_file(data)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(content)
    total = sum(len(v) for v in data.values())
    print(f"Wrote {OUT} — {total} questions across {len(data)} lists")
    for k, v in sorted(data.items()):
        print(f"  {k}: {len(v)}")


if __name__ == "__main__":
    main()
