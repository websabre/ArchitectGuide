# Week 48 — Expert Scenario Q&A

> Q101–Q120: Premium format (Week 1 quality).

---


## Q101: Notification Mock Panel Defense

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Panel pushes back on at-least-once notifications — defend design for 10 minutes.

### Short Answer (30 seconds)

Define user-visible guarantee precisely; show dedup layer; cite industry (email providers); offer audit log; acknowledge provider limits; stay collaborative.

### Detailed Answer

**Defense:**
1. 'User sees max one notification per eventId'
2. Dedup Redis + idempotent workers
3. Provider retry is their semantics — we handle
4. Monitor duplicate rate metric target <0.01%

**Architect:** Precise guarantees beat buzzwords.

### Architecture Perspective

Panel defense on delivery semantics is common staff mock.

### Follow-up Questions

1. **Upgrade path to stronger guarantee? — Idempotent provider APIs where exist.**
2. **Acceptable duplicate rate? — Business defines — OTP stricter than marketing.**

### Common Mistakes in Interviews

- Claim exactly-once end-to-end
- No dedup architecture
- Dismiss provider retry concern

---

## Q102: Flash Sale Adversarial QA

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Adversarial QA: bots buy all inventory in 3 seconds — respond in cart mock.

### Short Answer (30 seconds)

Bot detection (rate limit, CAPTCHA, device fingerprint), waiting room token, purchase limit per account, inventory reservation per verified user, edge rate limit.

### Detailed Answer

**Layers:**
1. WAF bot score
2. Waiting room admission token
3. Per-user purchase cap
4. Reservation requires authenticated account

**Architect:** Abuse prevention is architecture — not afterthought.

### Architecture Perspective

Adversarial scenarios test security + scale together.

### Follow-up Questions

1. **Virtual queue fairness? — Randomized token — not FCFS only.**
2. **Partner API bots? — Separate rate limit tier.**

### Common Mistakes in Interviews

- No bot mitigation plan
- Inventory held by anonymous sessions
- Ignore resale abuse scenario

---

## Q103: Multi Tenant Breach Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Whiteboard Mock |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Tenant A sees Tenant B data — incident response in multi-tenant mock.

### Short Answer (30 seconds)

Immediate isolate: disable affected API pods, audit logs filter by tenantId, identify missing RLS/filter bug, notify customers per regulation, hotfix + penetration retest.

### Detailed Answer

**Root causes:**
- Missing tenantId in query
- Cache key without tenant prefix
- JWT validation bug

**Prevention:** Integration tests cross-tenant negative cases mandatory.

**Architect:** Tenant isolation test in CI blocks deploy.

### Architecture Perspective

Breach scenario is expert multi-tenant mock — response matters.

### Follow-up Questions

1. **Forensics? — Audit log immutable — who accessed what.**
2. **Communication? — Status page + regulatory timeline.**

### Common Mistakes in Interviews

- Only app filter no DB RLS
- Cache key missing tenantId
- No cross-tenant integration tests

---

## Q104: Zero Downtime Migration Mock

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Migrate monolith orders table to new service zero downtime — expert mock.

### Short Answer (30 seconds)

Strangler: dual-write, CDC sync, shadow read compare, cutover reads, cutover writes, retire monolith module — expand-contract schema.

### Detailed Answer

**Phases:**
1. New service reads old DB via view
2. Dual-write both stores validate counts
3. Switch reads feature flag
4. Switch writes
5. Remove dual-write

**Architect:** Rollback at each phase — feature flag revert.

### Architecture Perspective

Migration mock tests real-world extraction not greenfield.

### Follow-up Questions

1. **CDC tool? — Debezium — mention by name.**
2. **Data drift detection? — Hourly count reconciliation job.**

### Common Mistakes in Interviews

- Big-bang cutover weekend
- Breaking schema without expand-contract
- No rollback tested

---

## Q105: Webhook Scale Million Partners

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Scale webhook delivery to 1M partner endpoints — expert design.

### Short Answer (30 seconds)

Shard delivery queue by partnerId, rate limit per partner, worker pool autoscale, circuit breaker per failing URL, partner tier priority queues.

### Detailed Answer

**Architecture:**
```
Event → Router → Partner shard queues → Workers
                ↓
         Per-URL circuit breaker + DLQ
```

**Architect:** Noisy neighbor partner can't block others — isolation.

### Architecture Perspective

Webhook scale is partner isolation problem.

### Follow-up Questions

1. **Polling fallback? — Partners fetch missed events API.**
2. **Signature verification cost? — Batch HMAC where possible.**

### Common Mistakes in Interviews

- Single queue all partners
- One slow partner blocks all
- No per-partner rate limit

---

## Q106: Stream Fraud False Positive

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Fraud model blocks 5% legitimate transactions — tune in stream mock.

### Short Answer (30 seconds)

Human review queue for borderline scores, adaptive threshold by merchant, shadow mode new model, A/B test false positive rate, feedback loop labels chargebacks.

### Detailed Answer

**Ops:**
- Score 0.9+ auto block
- 0.7-0.9 review queue
- <0.7 pass
- Monitor FP rate SLO <0.1%

**Architect:** ML ops loop — model version in audit trail.

### Architecture Perspective

Expert stream mock includes ML ops not just Flink boxes.

### Follow-up Questions

1. **Cold start merchant? — Higher threshold until history.**
2. **Explainability? — Reason codes for support team.**

### Common Mistakes in Interviews

- Auto block threshold too aggressive
- No human review path
- No model version tracking

---

## Q107: Auth SAML Outage Fallback

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Corporate SAML IdP down — B2B SaaS auth fallback in mock.

### Short Answer (30 seconds)

Cached session grace period, break-glass local admin accounts, status communication, optional backup IdP federation, don't expire all sessions immediately.

### Detailed Answer

**Fallback hierarchy:**
1. Existing sessions valid until TTL
2. Break-glass admin local auth (MFA + IP allowlist)
3. Backup IdP if configured
4. Read-only mode if no auth

**Architect:** IdP dependency is availability risk — document in SLA.

### Architecture Perspective

IdP outage scenario shows auth architecture resilience.

### Follow-up Questions

1. **Session TTL? — Balance security vs outage UX.**
2. **Multi-IdP federation? — Enterprise feature — mention.**

### Common Mistakes in Interviews

- All sessions invalidated when IdP blips
- No break-glass procedure
- Hard dependency single IdP no fallback

---

## Q108: CQRS Read Model Corruption

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Read model corrupted after bad deploy — recovery in CQRS expert mock.

### Short Answer (30 seconds)

Stop projector, replay events from last known good offset, rebuild read DB from scratch in parallel, swap alias, root cause fix before resume.

### Detailed Answer

**Recovery:**
1. Halt consumer
2. Snapshot last good offset from checkpoint
3. Rebuild `read_model_v2` from event log
4. Validate counts vs command side
5. Swap read alias

**Architect:** Replay capability is CQRS prerequisite — test quarterly.

### Architecture Perspective

Read model corruption recovery separates CQRS theory from ops.

### Follow-up Questions

1. **Snapshot + replay? — Faster than full replay if snapshots current.**
2. **Dual read models during rebuild? — Blue-green read side.**

### Common Mistakes in Interviews

- No event replay capability
- Edit read model in place manually
- No checkpoint on projector

---

## Q109: Schema Breaking Change Emergency

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Accidental breaking event schema deployed — emergency response mock.

### Short Answer (30 seconds)

Rollback producer deploy, replay DLQ with old schema consumers, parallel v2 topic if needed, postmortem + schema registry CI gate, never reuse field numbers.

### Detailed Answer

**Immediate:**
1. Stop producer publishing v2
2. Roll back to v1 schema deploy
3. Drain/reprocess DLQ
4. Add registry breaking change block in CI

**Architect:** Schema registry mandatory for event platforms.

### Architecture Perspective

Breaking schema incident is realistic expert scenario.

### Follow-up Questions

1. **Protobuf field numbers? — Never reuse — permanent rule.**
2. **Consumer defensive coding? — Ignore unknown fields — required.**

### Common Mistakes in Interviews

- Force all consumers same-day deploy
- No schema registry
- Delete old events to fix

---

## Q110: Batch ETL Missed SLA Executive

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Nightly ETL missed 6am SLA — brief executives in mock scenario.

### Short Answer (30 seconds)

Impact: dashboards stale until 9am, no revenue impact, root cause worker OOM, fix scaled cluster, preventive autoscale on memory, communication template.

### Detailed Answer

**Briefing (3 min):**
1. What failed: partition 2024-03-15 OOM
2. Business impact: reporting delayed 3h — no transactional impact
3. Fix: rerun from checkpoint complete 9am
4. Prevent: memory limit + partition size cap

**Architect:** Translate technical failure to business impact.

### Architecture Perspective

Executive communication is staff architect skill tested in mocks.

### Follow-up Questions

1. **SLA tier? — Reporting vs transactional different severity.**
2. **Checkpoint? — Enabled rerun not full 500M replay.**

### Common Mistakes in Interviews

- Technical jargon only briefing
- Hide delay from stakeholders
- No preventive action after repeat miss

---

## Q111: Mock Silent Interviewer

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Interview Skills |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Interviewer silent after your design — what do you do?

### Short Answer (30 seconds)

Continue structured flow, narrate thinking aloud, propose deep dive choice, ask 'Would you like me to explore X or Y?' — silence isn't always negative.

### Detailed Answer

**Tactics:**
- 'I'll document assumptions and move to estimation'
- 'Next I'll sketch high-level components'
- Pause 3 sec then proceed — don't freeze
- Ask targeted question if truly stuck

**Architect:** Interviewers take notes — silence can mean thinking.

### Architecture Perspective

Handling silence tests composure — practice narrating alone.

### Follow-up Questions

1. **Talk too much? — Balance — structured not rambling.**
2. **Misread silence as failure? — Continue confidently.**

### Common Mistakes in Interviews

- Stop talking and wait awkwardly 5 min
- Ask 'is this wrong?' repeatedly
- Abandon structure and ramble

---

## Q112: Mock Conflicting Requirements

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Interview Skills |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Interviewer gives conflicting requirements: strong consistency AND global low latency — resolve.

### Short Answer (30 seconds)

Surface conflict explicitly, ask priority, propose scoped consistency (strong for payments, eventual for feed), or geo-partitioned cells with trade-off documentation.

### Detailed Answer

**Script:**
'These requirements tension — which is priority if we can't have both globally?'

**Options:**
1. Strong consistency in home region only
2. CRDT for specific data types
3. Sync replication with latency cost — quantify

**Architect:** Conflict identification scores higher than pretending both free.

### Architecture Perspective

Requirement conflict resolution is senior judgment signal.

### Follow-up Questions

1. **CAP reference? — Use carefully — tie to their scenario.**
2. **Fake both? — Interviewers notice hand-wave.**

### Common Mistakes in Interviews

- Ignore conflict proceed with both claimed
- Pick without asking priority
- No trade-off documented

---

## Q113: Mock Time Overrun Recovery

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Interview Skills |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

5 minutes left and still on requirements — recover mock.

### Short Answer (30 seconds)

State 'I'll accelerate — assumptions on board, rapid HLD, one deep dive, trade-offs' — compress estimation to 30 seconds, draw minimal diagram, pick one deep dive, close with risks.

### Detailed Answer

**Recovery script:**
'Given time, I'm assuming [list]. Here's the core architecture [3 boxes]. Deep dive: cache. Trade-off: eventual consistency OK.'

**Architect:** Controlled acceleration beats incomplete silence.

### Architecture Perspective

Time overrun recovery is trainable — have compression script ready.

### Follow-up Questions

1. **Skip diagram entirely? — Minimal 3-box still required.**
2. **Panic? — Breath — structured compression works.**

### Common Mistakes in Interviews

- Keep optimizing requirements detail
- No trade-offs because out of time
- Give up 'we'd need more time'

---

## Q114: Staff Mock Cost vs Reliability

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Interview Skills |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Staff mock: VP asks cut 40% cloud cost — what change in design?

### Short Answer (30 seconds)

Reserved instances, reduce replica count with accepted RPO risk, tier storage, cache more aggressively, right-size pods — document SLA impact per cut.

### Detailed Answer

**Negotiated cuts:**
| Change | Savings | SLA impact |
|--------|---------|------------|
| 1 replica less | 20% DB | RTO +30min |
| Smaller Redis | 10% | Hit rate drop — monitor |
| Log retention 7d | 5% | Debug harder |

**Architect:** Never cut without written risk acceptance.

### Architecture Perspective

Staff level balances FinOps with reliability explicitly.

### Follow-up Questions

1. **Multi-region to single? — Major DR impact — Tier-0 pushback.**
2. **Spot for workers? — OK if fault tolerant.**

### Common Mistakes in Interviews

- Cut replicas with no risk doc
- Delete monitoring to save cost
- Accept cuts without SLA analysis

---

## Q115: Mock Defending Monolith Choice

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Interview Skills |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Interviewer expects microservices — defend modular monolith for early-stage product.

### Short Answer (30 seconds)

Team 8 engineers, unclear boundaries, moderate scale — modular monolith with clear modules, single deploy, extract services when metrics prove pain — lower ops burden.

### Detailed Answer

**Defense points:**
- Conway's law — team size doesn't support 20 services
- Operational cost: K8s, tracing, CI × N
- Domain still evolving — wrong boundaries costly
- Clear module seams enable future extraction

**Architect:** Monolith is valid — justify with constraints not fear of microservices.

### Architecture Perspective

Defending monolith shows judgment not hype following.

### Follow-up Questions

1. **When extract? — Independent scale or deploy pain measured.**
2. **Modular monolith patterns? — Vertical slices, bounded packages.**

### Common Mistakes in Interviews

- Microservices because resume driven
- Monolith with no module boundaries
- Refuse microservices without listening to scale needs

---

## Q116: Mock Multi Region Clock Skew

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | System Design |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Snowflake IDs collide after clock skew across regions — expert response.

### Short Answer (30 seconds)

Detect clock rollback in ID generator — wait or use logical increment; NTP discipline; dedicated machine ID per region; monitor ID collision metric.

### Detailed Answer

**Mitigation:**
- Wait until clock catches up on rollback
- Logical clock increment on rollback detection
- Never share machine IDs across regions
- Alert on NTP drift >100ms

**Architect:** ID generation runbook includes clock skew procedure.

### Architecture Perspective

Clock skew is Snowflake production reality — expert detail.

### Follow-up Questions

1. **UUID alternative? — No clock dependency — trade sortability.**
2. **Central ID service? — Bottleneck — regional generators preferred.**

### Common Mistakes in Interviews

- Ignore NTP in distributed ID design
- Duplicate machine IDs across pods
- No collision monitoring

---

## Q117: Mock GDPR Right To Delete

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

45-minute mock adds GDPR delete mid-session — adapt design.

### Short Answer (30 seconds)

Add delete orchestration saga, tombstone events, blob lifecycle delete, search index purge, 30-day soft delete, audit without PII — revise diagram in 5 min.

### Detailed Answer

**Additions:**
- `UserDeleteRequested` event
- Per-service delete consumer
- Blob storage lifecycle rule
- ES delete by query
- Completion certificate API

**Architect:** Adaptability mid-mock is staff signal — don't restart from scratch.

### Architecture Perspective

Mid-mock requirement change tests adaptability.

### Follow-up Questions

1. **Legal hold? — Pause delete workflow state.**
2. **Anonymize vs delete orders? — Retention notification mock.**

### Common Mistakes in Interviews

- Hard delete immediate all backups
- Ignore delete propagation to cache
- No audit trail of deletion

---

## Q118: Mock Observability Budget Overrun

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Whiteboard Mock |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Log volume costs 3× forecast — optimize observability architecture.

### Short Answer (30 seconds)

Sample debug logs in prod, structured info default, hot/warm/cold tiers, metric cardinality limits, trace sampling 10%, retain errors 100%.

### Detailed Answer

**Cuts:**
- DEBUG → 1% sample
- Access logs → aggregate metrics instead
- Trace sample rate 0.1 → 0.01 except errors
- 90d → 30d retention hot

**Architect:** Observability budget in FinOps review — SLO-driven sampling.

### Architecture Perspective

Observability cost is real architecture concern.

### Follow-up Questions

1. **Tail sampling? — Keep errors always — sample success.**
2. **Log-based metrics? — Reduce log volume — derive counters.**

### Common Mistakes in Interviews

- Infinite log retention
- DEBUG everywhere production
- Full trace every request at 10K RPS

---

## Q119: Mock Panel Security Architect

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Interview Skills |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Security architect challenges public API design in panel mock — respond.

### Short Answer (30 seconds)

Acknowledge STRIDE gaps, cite WAF + auth + rate limit + input validation + pen test plan, offer threat model iteration, collaborative tone.

### Detailed Answer

**Response structure:**
1. Validate concern ('SQL injection risk on search param')
2. Mitigation ('parameterized queries + WAF rule')
3. Residual risk ('admin API needs mTLS — add to phase 2')
4. Evidence ('SAST in CI, annual pen test')

**Architect:** Security partnership not checkbox.

### Architecture Perspective

Panel with security tests collaboration under scrutiny.

### Follow-up Questions

1. **Zero trust? — mTLS internal — offer roadmap.**
2. **Compliance mapping? — PCI control reference if payment.**

### Common Mistakes in Interviews

- Dismiss security as slowdown
- Claim 'cloud provider handles security'
- No pen test or threat model plan

---

## Q120: Mock Retrospective Improvement

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Interview Skills |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

After mock, create one improvement action for next week — expert habit.

### Short Answer (30 seconds)

Pick lowest rubric dimension, one concrete drill — e.g., 'next mock timer set 15min must have diagram; practice cursor pagination 10 min'.

### Detailed Answer

**Retrospective template:**
1. Score rubric /22
2. Weakest: estimation
3. Action: 5 estimation drills with timer
4. Next mock prompt: notification again
5. Success metric: estimation score 2/2

**Architect:** Deliberate practice loop — mocks compound weekly.

### Architecture Perspective

Retrospective habit separates candidates who improve from those who repeat.

### Follow-up Questions

1. **Peer feedback? — Mock partner notes filler words.**
2. **Video review? — Painful but effective.**

### Common Mistakes in Interviews

- Mock without any debrief
- Same weakness 10 mocks straight
- No measurable improvement goal

---
