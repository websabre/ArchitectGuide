# Week 36 — Intermediate Q&A

> Q031–Q070: Premium format (Week 1 quality).

---


## Q031: Capstone System Design Presentation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Very Common |

### Question

Present e-commerce platform design — structure?

### Short Answer (30 seconds)

Requirements recap, estimation, diagram, catalog/cart/checkout deep dives, failure modes, evolution roadmap, cost order of magnitude.

### Detailed Answer (3–5 minutes)

10-minute version for exec; 45-minute whiteboard for technical. Have ADRs for SQL vs NoSQL, cache, saga.

### Architecture Perspective

Capstone simulates senior interview.

### Follow-up Questions

1. **Challenge defense? — Acknowledge trade-off — don't be defensive.**
2. **What cut if 6 months not 12? — Prioritize checkout path MVP.**

### Common Mistakes in Interviews

- No failure scenarios
- Cannot estimate QPS
- Single diagram only

---

## Q032: Checkout Saga End-to-End

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Saga |
| **Frequency** | Very Common |

### Question

Whiteboard checkout in 15 minutes.

### Short Answer (30 seconds)

Cart (Redis) → reserve inventory (sync, TTL) → payment (idempotent) → confirm order → async notify. Compensate on payment fail.

### Detailed Answer (3–5 minutes)

Draw numbered steps. Label sync vs async arrows. Idempotency-Key on payment. Inventory release compensation.

### Architecture Perspective

Checkout is #1 system design + microservices crossover.

### Follow-up Questions

1. **Double-click pay? — Idempotency key — same result.**
2. **Inventory TTL? — 15 min — release on timeout job.**

### Common Mistakes in Interviews

- No compensation path
- Sync email in checkout path
- Missing idempotency

---

## Q033: Notification Platform Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | System Design |
| **Frequency** | Common |

### Question

Design multi-channel notification system.

### Short Answer (30 seconds)

Event bus → router → priority queues per channel → workers → provider adapters (SendGrid, Twilio). Template service. Retry + DLQ.

### Detailed Answer (3–5 minutes)

Rate limit per user — don't spam. Preference center — opt out per channel.

Idempotent send — `notificationId` dedup.

### Architecture Perspective

Notification is common whiteboard — prepare template.

### Follow-up Questions

1. **Priority queue? — OTP before marketing email.**
2. **Batching? — Digest emails — separate scheduler.**

### Common Mistakes in Interviews

- Single thread sends all email
- No provider abstraction
- No user preference store

---

## Q034: Search and Catalog at Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Search |
| **Frequency** | Common |

### Question

10M products — search architecture?

### Short Answer (30 seconds)

Elasticsearch/Azure AI Search index fed by product change events. Primary DB source of truth. Cache hot searches.

### Detailed Answer (3–5 minutes)

CDC or domain events update index. Search replica lag acceptable for browse.

Faceted search — denormalize attributes in index document.

### Architecture Perspective

Search is separate read optimized store.

### Follow-up Questions

1. **Index rebuild? — Blue-green index alias swap.**
2. **Typo tolerance? — Fuzzy match — product decision.**

### Common Mistakes in Interviews

- SQL LIKE for search at 10M products
- No index update pipeline
- Search and DB strong consistency

---

## Q035: Multi-Tenant E-Commerce

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Multi-Tenancy |
| **Frequency** | Common |

### Question

B2B marketplace — tenant isolation?

### Short Answer (30 seconds)

Pool: `tenantId` on all rows + RLS. Silo: DB per enterprise tenant. Bridge: pool default, silo for premium.

### Detailed Answer (3–5 minutes)

Auth resolves tenant — every query scoped. Cache keys include tenantId.

Noisy neighbor: rate limit per tenant.

### Architecture Perspective

Multi-tenancy permeates data and cache design.

### Follow-up Questions

1. **Cross-tenant leak test? — Security test suite mandatory.**
2. **Tenant-specific config? — Feature flags per tenant tier.**

### Common Mistakes in Interviews

- Missing tenantId in cache key
- Shared admin API without tenant scope
- One rate limit global

---

## Q036: Disaster Recovery for Platform

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DR |
| **Frequency** | Common |

### Question

Region loss — RPO/RTO for e-commerce capstone?

### Short Answer (30 seconds)

RPO 1h, RTO 4h example: async cross-region DB replica, Traffic Manager failover, runbook tested quarterly.

### Detailed Answer (3–5 minutes)

Payment during DR: pause or read-only mode decision — document.business choice.

Backup restore test — untested backup is fiction.

### Architecture Perspective

DR numbers make design concrete.

### Follow-up Questions

1. **Chaos engineering? — Game day regional failover drill.**
2. **Data residency? — EU tenants stay EU region — affects DR.**

### Common Mistakes in Interviews

- No DR for 'we'll rebuild'
- RPO=0 claim with async replication
- Untested failover runbook

---

## Q037: Performance Budget

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Common |

### Question

Set performance budget for checkout page.

### Short Answer (30 seconds)

p99 checkout API < 500ms. CDN static < 50ms. Max 3 sync service calls. Database queries < 50ms each.

### Detailed Answer (3–5 minutes)

Budget drives architecture — exceed budget → add cache or async.

Measure in CI with load test gate on PR for critical paths.

### Architecture Perspective

Performance budgets connect NFR to design.

### Follow-up Questions

1. **Real user monitoring? — Compare lab load test to production RUM.**
2. **Budget owner? — Architect proposes — product approves trade-offs.**

### Common Mistakes in Interviews

- No latency targets
- Budget only on homepage
- Ignore mobile network latency

---

## Q038: Security in Platform Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Security layers for e-commerce capstone?

### Short Answer (30 seconds)

WAF at edge, auth at gateway, PCI scope reduction (tokenized payments), encryption at rest, audit logs, rate limiting, input validation.

### Detailed Answer (3–5 minutes)

Card data never touches your servers — Stripe/Adyen tokenization.

OWASP top 10 addressed in threat model document.

### Architecture Perspective

Security woven in — not bolted on at end.

### Follow-up Questions

1. **PCI DSS scope? — Minimize — SAQ A if iframe checkout.**
2. **Secrets? — Key Vault — rotation policy.**

### Common Mistakes in Interviews

- Store PAN in database
- No WAF on public API
- Security only in week 14

---

## Q039: Evolution from Monolith to Platform

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Evolution |
| **Frequency** | Common |

### Question

Year 1 monolith → Year 3 platform — phases?

### Short Answer (30 seconds)

Y1: modular monolith. Y2: extract checkout + catalog. Y3: event bus + search + notifications. Document triggers for each phase.

### Detailed Answer (3–5 minutes)

Triggers: team size, deploy pain, scale metrics — not calendar alone.

Strangler fig throughout — never big bang.

### Architecture Perspective

Evolution roadmap shows strategic thinking.

### Follow-up Questions

1. **Team topology per phase? — Align stream-aligned teams to services.**
2. **Technical debt budget? — 20% capacity for platform improvements.**

### Common Mistakes in Interviews

- Microservices day 1
- No phase criteria
- Rewrite instead of strangler

---

## Q040: Month 9 Graduation Criteria

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Readiness |
| **Frequency** | Common |

### Question

Prove system design month mastery?

### Short Answer (30 seconds)

5 whiteboards ≥75/100, System Design Top 50 ≥75%, capstone doc complete, mock-02 and mock-05 passed, RESHADED under 45 min.

### Detailed Answer (3–5 minutes)

Record yourself whiteboarding — painful but effective. Weak area log updated.

### Architecture Perspective

Demonstrable skill — not content consumed.

### Follow-up Questions

1. **Peer review capstone? — Another student challenges design.**
2. **Schedule mock-06 panel when ready.**

### Common Mistakes in Interviews

- Theory only no whiteboard practice
- Cannot do estimation under pressure
- Skip failure mode section every time

---

## Q041: E-Commerce Cart and Checkout

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Very Common |

### Question

Design cart and checkout for 50K orders/hour peak.

### Short Answer (30 seconds)

Cart in Redis (userId/session keyed, TTL 7d). Checkout: validate cart → reserve inventory (TTL 15m) → payment → create order → clear cart. Idempotent checkout endpoint.

### Detailed Answer (3–5 minutes)

**Cart merge:** Login merges anonymous cart to user cart — conflict resolution last-write-wins per SKU.

**Abandoned cart:** Event for marketing — async.

**Scale:** Redis cluster, checkout API stateless, order write to primary DB.

### Architecture Perspective

Cart/checkout is capstone bread-and-butter — practice end-to-end.

### Follow-up Questions

1. **Guest checkout? — Session cart — email capture before payment.**
2. **Cart price staleness? — Revalidate prices at checkout — not cart add time.**

### Common Mistakes in Interviews

- Cart in SQL row per session
- No inventory reservation TTL
- Checkout without idempotency key

---

## Q042: Payment PCI Boundaries

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Draw PCI scope boundary for e-commerce checkout.

### Short Answer (30 seconds)

Card data never touches merchant servers — Stripe Elements/Adyen hosted fields tokenize → merchant gets `paymentMethodId` only. SAQ A scope smallest.

### Detailed Answer (3–5 minutes)

**In scope if:** You store, process, or transmit PAN. **Out of scope:** Token references only.

**Architect diagram:** Browser → payment provider → webhook → order service. Merchant DB stores last4 + brand only.

**Network:** CDE segmented if any custom card handling — avoid.

### Architecture Perspective

PCI boundary drawing is security capstone question.

### Follow-up Questions

1. **Webhook authenticity? — Verify Stripe signature — prevent fake paid events.**
2. **Refund flow? — API to provider with original charge ID — idempotent.**

### Common Mistakes in Interviews

- POST card number to your API
- Log full payment request body
- PAN in database encrypted 'for convenience'

---

## Q043: Order Fulfillment Flow

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Very Common |

### Question

Design order fulfillment from payment capture to delivery notification.

### Short Answer (30 seconds)

`PaymentCaptured` → warehouse pick list → ship label API → `ShipmentCreated` → carrier tracking webhook → `Delivered` → customer notification.

### Detailed Answer (3–5 minutes)

**WMS integration:** Async queue to warehouse system — not sync in checkout.

**Partial shipment:** Order line items ship independently — sub-state per line.

**Saga:** Cancel order before ship → refund + restock compensation.

### Architecture Perspective

Fulfillment connects e-commerce to logistics — common extension question.

### Follow-up Questions

1. **Split warehouse? — Route line items to nearest stock — orchestration rules.**
2. **International customs? — Hold state until docs — async step.**

### Common Mistakes in Interviews

- Sync warehouse API in checkout
- No shipment state machine
- Missing carrier webhook idempotency

---

## Q044: Inventory Consistency Model

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Consistency |
| **Frequency** | Very Common |

### Question

Prevent overselling 1 unit left, two buyers checkout simultaneously.

### Short Answer (30 seconds)

Optimistic: `UPDATE stock SET qty=qty-1 WHERE sku=X AND qty>0` — rows affected 0 → sold out. Or pessimistic lock row for high contention SKU.

### Detailed Answer (3–5 minutes)

**Reservation:** Hold stock on checkout start, release on timeout/payment fail.

**Read path:** Product browse may use replica; stock check at payment uses primary or sync read.

**Eventual:** Analytics inventory OK lagging; checkout not.

### Architecture Perspective

Inventory is classic consistency interview fork.

### Follow-up Questions

1. **Distributed inventory multi-warehouse? — Reserve at specific warehouse node.**
2. **Negative stock allowed? — Backorder business rule — explicit ADR.**

### Common Mistakes in Interviews

- Check-then-act race on replica read
- No reservation TTL
- Cache stock count for checkout decision

---

## Q045: Product Catalog at Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Common |

### Question

10M SKUs, 100K catalog reads/sec — architecture?

### Short Answer (30 seconds)

CDN for product images. API cache (Redis) for product JSON. DB sharded by `categoryId` or read replicas. Search index separate (Elasticsearch) fed by CDC.

### Detailed Answer (3–5 minutes)

**Write:** Admin updates infrequent — invalidate cache on change.

**Bulk import:** Nightly batch — not inline API.

**Attributes:** JSONB or EAV for variant attributes — index hot facets in search only.

### Architecture Perspective

Catalog read-heavy — optimize read path not write.

### Follow-up Questions

1. **GraphQL product API? — DataLoader batch — prevent N+1.**
2. **Seasonal catalog? — Pre-warm cache before campaign launch.**

### Common Mistakes in Interviews

- 10M JOIN query per product page
- No CDN on product images
- Single MySQL for 100K reads/sec

---

## Q046: Recommendation Pipeline Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | ML Ops |
| **Frequency** | Common |

### Question

Design product recommendation for homepage — real-time vs batch?

### Short Answer (30 seconds)

Batch: nightly collaborative filtering → feature store. Real-time: session events (views, cart) → stream processor updates short-term scores. API merges batch + real-time at request.

### Detailed Answer (3–5 minutes)

**Components:** Clickstream → Kafka → Flink/Spark → Redis feature store → Rec API → fallback popular items.

**Cold start:** New user → category bestsellers.

**Latency budget:** Rec service < 50ms — precompute heavy work.

### Architecture Perspective

Recommendation shows batch + stream hybrid thinking.

### Follow-up Questions

1. **A/B test rec models? — Shadow traffic compare CTR.**
2. **Explainability? — 'Because you viewed X' — product requirement.**

### Common Mistakes in Interviews

- ML model inference 2s in request path
- No fallback when rec service down
- Train on production checkout without PII governance

---

## Q047: Fraud Detection Hook

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Where hook fraud check in checkout without blocking p99?

### Short Answer (30 seconds)

Sync rules engine (< 50ms): velocity, blocklist, AVS mismatch → decline. Async ML scoring post-auth → cancel/shipment hold if fraud score high. Risk tier by order amount.

### Detailed Answer (3–5 minutes)

**Integration:** Stripe Radar or custom rules service. **False positive:** Manual review queue not auto-cancel happy customers.

**Data:** Device fingerprint, IP geo, account age signals.

### Architecture Perspective

Fraud is risk trade-off — architect shows layered sync/async approach.

### Follow-up Questions

1. **Chargeback workflow? — Evidence collection automated — ops tooling.**
2. **Guest checkout fraud? — Stricter rules — higher friction acceptable.**

### Common Mistakes in Interviews

- No fraud check on high-value orders
- 2s ML model in sync checkout
- Auto-decline with no review path

---

## Q048: Multi-Region Active-Active E-Commerce

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Availability |
| **Frequency** | Common |

### Question

Active-active regions for global storefront — hardest problems?

### Short Answer (30 seconds)

Inventory split per region, cart/session sticky or replicated, price catalog eventually consistent, payment in local currency region, conflict on rare cross-region account edits.

### Detailed Answer (3–5 minutes)

**Cosmos DB / CRDTs:** For session-like data. **Inventory:** Don't share single stock pool without reservation protocol.

**DNS:** Geo route to nearest. **Compliance:** EU data stays EU.

### Architecture Perspective

Active-active capstone shows you know conflict resolution cost.

### Follow-up Questions

1. **Split brain inventory? — Regional stock pools — transfer between regions async.**
2. **Global cart? — Replicate cart state — merge on conflict — last-write-wins SKU qty.**

### Common Mistakes in Interviews

- Single global inventory counter active-active
- No conflict resolution strategy
- Sync replication cross-region for all data

---

## Q049: DR RPO and RTO Targets

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DR |
| **Frequency** | Very Common |

### Question

Set RPO/RTO for e-commerce: payments vs catalog vs analytics.

### Short Answer (30 seconds)

Payments: RPO 0–1 min, RTO 15 min (sync/near-sync). Catalog: RPO 1h, RTO 4h. Analytics: RPO 24h, RTO 48h acceptable.

### Detailed Answer (3–5 minutes)

**RPO:** Max data loss tolerated. **RTO:** Max downtime tolerated.

**Mechanisms:** Sync repl for payments, async for catalog, rebuild analytics from raw events.

**Game day:** Quarterly failover drill measures actual RTO.

### Architecture Perspective

Tiered RPO/RTO by data class is mature DR answer.

### Follow-up Questions

1. **Backup encryption? — Separate keys per region.**
2. **Runbook automation? — Terraform failover — reduce human RTO.**

### Common Mistakes in Interviews

- Same RPO=0 for analytics warehouse
- Untested backup restore
- No business sign-off on RPO trade-offs

---

## Q050: Cost Model at Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

Build order-of-magnitude cost model for 10K orders/hour platform.

### Short Answer (30 seconds)

Compute: 20 API instances $2K/mo. DB: RDS multi-AZ $3K. Redis $800. Egress/CDN $1.5K. Messaging $400. Search cluster $2K. Total ~$10K/mo — validate with pricing calculator.

### Detailed Answer (3–5 minutes)

**Unit economics:** $/1000 orders — track as scale metric.

**Drivers:** DB and egress dominate — cache and CDN reduce both.

**Optimize:** Reserved instances baseline, spot for batch workers.

### Architecture Perspective

Cost model closes capstone — architects speak finance.

### Follow-up Questions

1. **Serverless checkout? — Compare step functions cost at volume.**
2. **FinOps tagging? — Cost per tenant/team allocation.**

### Common Mistakes in Interviews

- No egress in model
- On-demand only at steady high load
- Ignore messaging and search cost

---

## Q051: Observability SLO Dashboard

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Observability |
| **Frequency** | Common |

### Question

Design SLO dashboard for e-commerce platform launch.

### Short Answer (30 seconds)

Tiles: checkout success rate (SLO 99.5%), p99 checkout latency, payment provider error rate, order queue depth, error budget burn rate. RED metrics per service.

### Detailed Answer (3–5 minutes)

**Layers:** Business (orders/min), golden signals (latency, traffic, errors, saturation), infrastructure.

**Burn alert:** 2% budget burn in 1h pages on-call.

**Launch:** Compare canary vs baseline dashboard side-by-side.

### Architecture Perspective

SLO dashboard proves operability not just feature design.

### Follow-up Questions

1. **Synthetic checkout? — Probe every 1 min from 3 regions.**
2. **Trace sampling? — 100% on checkout path errors.**

### Common Mistakes in Interviews

- CPU dashboard only
- No error budget concept
- SLO measured after launch not before

---

## Q052: On-Call Escalation Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Common |

### Question

Design on-call escalation for payment failures spike.

### Short Answer (30 seconds)

L1 alert → primary on-call 5 min. Unacked → secondary 10 min. Sev1 → engineering manager + incident channel. Runbook link in alert. Auto-incident ticket.

### Detailed Answer (3–5 minutes)

**Severity matrix:** Sev1 payment down all users, Sev2 elevated errors, Sev3 single tenant.

**Noise reduction:** Alert on SLO burn not single error.

**Handoff:** Document timeline in status page.

### Architecture Perspective

Operations design completes production-ready capstone.

### Follow-up Questions

1. **PagerDuty vs Opsgenie? — Tool agnostic — workflow matters.**
2. **Post-incident review? — Blameless RCA within 48h mandatory.**

### Common Mistakes in Interviews

- Alert every error log line
- No runbook linked
- Escalation to wrong team no routing

---

## Q053: Launch Checklist Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Common |

### Question

Architecture items on go-live checklist for new marketplace?

### Short Answer (30 seconds)

Load test 2× peak passed, DR drill completed, secrets rotated, WAF rules active, rate limits configured, rollback tested, feature flags default safe, monitoring dashboards live, on-call schedule confirmed.

### Detailed Answer (3–5 minutes)

**Rollback:** Blue-green or canary — one-click revert validated.

**Data migration:** Verified row counts checksum.

**Compliance:** PCI scan, privacy policy updated.

### Architecture Perspective

Launch checklist separates architect from diagram-only designer.

### Follow-up Questions

1. **Dark launch? — Traffic mirror to new stack — compare responses.**
2. **Kill switch? — Feature flag disable checkout v2 instantly.**

### Common Mistakes in Interviews

- Go live Friday 5pm
- No rollback test
- Skip load test 'we'll monitor'

---

## Q054: Post-Launch Hypercare

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Common |

### Question

First 72 hours after launch — hypercare architecture focus?

### Short Answer (30 seconds)

War room dashboard, 2× on-call staffing, lowered alert thresholds, hourly error budget review, freeze non-critical deploys, capture top 10 errors for hotfix priority.

### Detailed Answer (3–5 minutes)

**Metrics watch:** Conversion funnel drop, p99 regression, new error types, queue depth trends.

**Feedback loop:** Support ticket tags → engineering triage daily.

**Exit criteria:** 48h within SLO → return to normal ops.

### Architecture Perspective

Hypercare plan shows you've shipped production systems.

### Follow-up Questions

1. **Canary metrics? — 5% traffic 24h before 100% ramp.**
2. **Rollback trigger? — Pre-defined: checkout success < 98% for 10 min.**

### Common Mistakes in Interviews

- Immediate feature deploys day 1
- Normal alert thresholds too noisy day 1
- No war room communication channel

---

## Q055: Technical Debt Paydown Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Evolution |
| **Frequency** | Common |

### Question

Year 2 platform — prioritize tech debt: monolith checkout, no tests, manual deploy.

### Short Answer (30 seconds)

Score by risk × pain: checkout modularity first (revenue), CI/CD second (deploy risk), test coverage on payment path third. 20% sprint capacity reserved.

### Detailed Answer (3–5 minutes)

**Strangler:** Extract payment service first — highest change frequency.

**ADR:** Document debt accepted vs scheduled paydown.

**Metrics:** Deploy frequency, MTTR, change failure rate — DORA metrics improve as debt pays down.

### Architecture Perspective

Debt strategy shows strategic architect not rewrite zealot.

### Follow-up Questions

1. **Boy scout rule? — Leave module better than found — incremental.**
2. **Debt budget negotiation? — Product buys 20% with velocity data.**

### Common Mistakes in Interviews

- Big bang rewrite year 2
- Pay down cosmetic debt first
- No measurable outcome for debt sprint

---

## Q056: Monolith to Services Evolution

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Evolution |
| **Frequency** | Very Common |

### Question

Extract services from e-commerce monolith — extraction order?

### Short Answer (30 seconds)

1) Notifications (low risk), 2) Search (read-only), 3) Catalog (read-heavy), 4) Checkout (high risk last). Strangler route traffic via gateway.

### Detailed Answer (3–5 minutes)

**Triggers:** Team size > 8 on monolith, deploy weekly → daily need, independent scale search.

**Data:** Start with shared DB anti-pattern acceptable briefly — split DB per service later.

**Events:** Introduce bus at first extraction — enables next.

### Architecture Perspective

Evolution order minimizes revenue risk — architects sequence carefully.

### Follow-up Questions

1. **Checkout first? — Highest risk — extract after pattern proven.**
2. **Shared database forever? — Interim — plan bounded context split.**

### Common Mistakes in Interviews

- Microservices day 1 for 5 devs
- Extract without integration tests
- Big bang database split

---

## Q057: ADR for Major Architecture Decisions

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

Write ADR outline for choosing SQL vs NoSQL for orders.

### Short Answer (30 seconds)

Title, status, context, decision, consequences. Orders: need ACID, relations, reporting → PostgreSQL. Consequences: shard later at write limit, team SQL skilled.

### Detailed Answer (3–5 minutes)

**ADR library:** Checkout SQL, catalog flexible attributes JSONB, search Elasticsearch.

**Review:** Architecture review board quarterly reads ADRs.

**Supersede:** ADR-012 replaces ADR-003 when migrate to Cockroach — link history.

### Architecture Perspective

ADR practice shows governance maturity in capstone.

### Follow-up Questions

1. **When not ADR? — Reversible trivial choices — library version bump.**
2. **Stakeholder sign-off? — ADR appendix with product/security approval.**

### Common Mistakes in Interviews

- Verbal decision no record
- ADR without rejected alternatives
- Decision without consequences listed

---

## Q058: Stakeholder Architecture Review

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Communication |
| **Frequency** | Common |

### Question

Present architecture to non-technical executives — structure?

### Short Answer (30 seconds)

Business outcome first (faster checkout → +2% conversion). One diagram max. Three risks with mitigations. Cost range not false precision. Decision needed from them.

### Detailed Answer (3–5 minutes)

**Avoid:** Technology alphabet soup. **Use:** Analogies, SLA in business terms (downtime = $X/hour).

**Q&A:** Prepare 'why not build in-house payment' answer.

### Architecture Perspective

Stakeholder communication is architect core skill tested in capstone.

### Follow-up Questions

1. **Technical deep-dive appendix? — Optional doc for CTO not in meeting.**
2. **Record decision? — Meeting notes → ADR status accepted.**

### Common Mistakes in Interviews

- 60-slide architecture deck
- No ask — meeting without decision
- Dismiss budget concerns

---

## Q059: 10x Growth Plan

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Evolution |
| **Frequency** | Very Common |

### Question

Platform at 1K orders/hour — plan for 10K (10x) without rewrite.

### Short Answer (30 seconds)

Phase 1: Redis cache catalog (10× read relief). Phase 2: read replicas. Phase 3: checkout async notifications. Phase 4: DB shard by tenant. Metrics trigger each phase.

### Detailed Answer (3–5 minutes)

**Bottleneck order:** Usually read path → connection pool → write DB → external APIs.

**Cost:** Linear if cache effective; superlinear if skip cache and shard late.

**Team:** Don't extract microservices until org scale warrants.

### Architecture Perspective

10x plan shows measured evolution not premature scale.

### Follow-up Questions

1. **100x same plan? — Identify which phase breaks — Kafka, regional, etc.**
2. **Load test per phase? — Validate headroom before next growth wave.**

### Common Mistakes in Interviews

- Shard at 1K orders/hour
- 10x plan requires full rewrite
- No metrics-defined triggers between phases

---

## Q060: Whiteboard Mock Evaluation Rubric

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Interview Skill |
| **Frequency** | Common |

### Question

Self-evaluate whiteboard mock — scoring rubric categories?

### Short Answer (30 seconds)

Requirements (15%), estimation (10%), diagram (15%), deep dive (25%), failures (15%), evolution (10%), communication (10%). Score 0–5 each → /100. Target ≥75 pass.

### Detailed Answer (3–5 minutes)

**Deep dive:** Trade-offs named, schema shown, numbers used.

**Failures:** At least 3 scenarios with mitigation.

**Practice log:** Track weak category weekly — estimation common gap.

### Architecture Perspective

Rubric turns vague 'practice more' into measurable improvement.

### Follow-up Questions

1. **Peer review? — Partner scores blind — calibrate harshness.**
2. **Record replay? — Catch filler words and silent periods.**

### Common Mistakes in Interviews

- Score only 'felt ok'
- Skip failure section every time
- No timed 45-min practice

---

## Q061: E-Commerce Core Services

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | System Design Capstone |
| **Frequency** | Very Common |

### Question

Explain e-commerce core services for a system design or architecture interview.

### Short Answer (30 seconds)

Catalog, cart, checkout, payment, inventory, order, search — identify in any retail design.

### Detailed Answer (3–5 minutes)

**E-Commerce Core Services:**

Catalog, cart, checkout, payment, inventory, order, search — identify in any retail design.

**Production context (.NET/Azure):**
Apply in ASP.NET Core on Azure App Service or AKS with patterns from week 36.

**Key points:**
- When to use vs avoid
- Measurable outcome (latency, DORA, SLO)
- Common production pitfall and mitigation

**Example:** Instrument with Application Insights; track deployment in Azure DevOps.

**Architect:** Capture trade-offs in ADR when multiple valid approaches exist.

### Architecture Perspective

E-Commerce Core Services is foundational for week 36 — articulate clearly before tool names.

### Follow-up Questions

1. **How measure success? — Tie e-commerce core services to SLI, DORA metric, or business KPI.**
2. **Common anti-pattern? — Adopting tools before understanding e-commerce core services principles.**

### Common Mistakes in Interviews

- Define e-commerce core services with buzzwords only
- No concrete Azure/.NET example
- Cannot link concept to measurable outcome

---

## Q062: Checkout Saga Overview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | System Design Capstone |
| **Frequency** | Very Common |

### Question

Explain checkout saga overview for a system design or architecture interview.

### Short Answer (30 seconds)

Multi-step distributed flow with compensation; payment + inventory + shipping.

### Detailed Answer (3–5 minutes)

**Checkout Saga Overview:**

Multi-step distributed flow with compensation; payment + inventory + shipping.

**Production context (.NET/Azure):**
Apply in ASP.NET Core on Azure App Service or AKS with patterns from week 36.

**Key points:**
- When to use vs avoid
- Measurable outcome (latency, DORA, SLO)
- Common production pitfall and mitigation

**Example:** Instrument with Application Insights; track deployment in Azure DevOps.

**Architect:** Capture trade-offs in ADR when multiple valid approaches exist.

### Architecture Perspective

Checkout Saga Overview is foundational for week 36 — articulate clearly before tool names.

### Follow-up Questions

1. **How measure success? — Tie checkout saga overview to SLI, DORA metric, or business KPI.**
2. **Common anti-pattern? — Adopting tools before understanding checkout saga overview principles.**

### Common Mistakes in Interviews

- Define checkout saga overview with buzzwords only
- No concrete Azure/.NET example
- Cannot link concept to measurable outcome

---

## Q063: Uber Design Components

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | System Design Capstone |
| **Frequency** | Very Common |

### Question

Explain uber design components for a system design or architecture interview.

### Short Answer (30 seconds)

Riders, drivers, matching, geospatial, pricing, trip state machine.

### Detailed Answer (3–5 minutes)

**Uber Design Components:**

Riders, drivers, matching, geospatial, pricing, trip state machine.

**Production context (.NET/Azure):**
Apply in ASP.NET Core on Azure App Service or AKS with patterns from week 36.

**Key points:**
- When to use vs avoid
- Measurable outcome (latency, DORA, SLO)
- Common production pitfall and mitigation

**Example:** Instrument with Application Insights; track deployment in Azure DevOps.

**Architect:** Capture trade-offs in ADR when multiple valid approaches exist.

### Architecture Perspective

Uber Design Components is foundational for week 36 — articulate clearly before tool names.

### Follow-up Questions

1. **How measure success? — Tie uber design components to SLI, DORA metric, or business KPI.**
2. **Common anti-pattern? — Adopting tools before understanding uber design components principles.**

### Common Mistakes in Interviews

- Define uber design components with buzzwords only
- No concrete Azure/.NET example
- Cannot link concept to measurable outcome

---

## Q064: Notification System Channels

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | System Design Capstone |
| **Frequency** | Very Common |

### Question

Explain notification system channels for a system design or architecture interview.

### Short Answer (30 seconds)

Push, email, SMS — fanout, templates, preferences, rate limits.

### Detailed Answer (3–5 minutes)

**Notification System Channels:**

Push, email, SMS — fanout, templates, preferences, rate limits.

**Production context (.NET/Azure):**
Apply in ASP.NET Core on Azure App Service or AKS with patterns from week 36.

**Key points:**
- When to use vs avoid
- Measurable outcome (latency, DORA, SLO)
- Common production pitfall and mitigation

**Example:** Instrument with Application Insights; track deployment in Azure DevOps.

**Architect:** Capture trade-offs in ADR when multiple valid approaches exist.

### Architecture Perspective

Notification System Channels is foundational for week 36 — articulate clearly before tool names.

### Follow-up Questions

1. **How measure success? — Tie notification system channels to SLI, DORA metric, or business KPI.**
2. **Common anti-pattern? — Adopting tools before understanding notification system channels principles.**

### Common Mistakes in Interviews

- Define notification system channels with buzzwords only
- No concrete Azure/.NET example
- Cannot link concept to measurable outcome

---

## Q065: Search Architecture Basics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | System Design Capstone |
| **Frequency** | Very Common |

### Question

Explain search architecture basics for a system design or architecture interview.

### Short Answer (30 seconds)

Index pipeline, query service, ranking, autocomplete — ES common choice.

### Detailed Answer (3–5 minutes)

**Search Architecture Basics:**

Index pipeline, query service, ranking, autocomplete — ES common choice.

**Production context (.NET/Azure):**
Apply in ASP.NET Core on Azure App Service or AKS with patterns from week 36.

**Key points:**
- When to use vs avoid
- Measurable outcome (latency, DORA, SLO)
- Common production pitfall and mitigation

**Example:** Instrument with Application Insights; track deployment in Azure DevOps.

**Architect:** Capture trade-offs in ADR when multiple valid approaches exist.

### Architecture Perspective

Search Architecture Basics is foundational for week 36 — articulate clearly before tool names.

### Follow-up Questions

1. **How measure success? — Tie search architecture basics to SLI, DORA metric, or business KPI.**
2. **Common anti-pattern? — Adopting tools before understanding search architecture basics principles.**

### Common Mistakes in Interviews

- Define search architecture basics with buzzwords only
- No concrete Azure/.NET example
- Cannot link concept to measurable outcome

---

## Q066: Capstone Time Boxing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | System Design Capstone |
| **Frequency** | Very Common |

### Question

Explain capstone time boxing for a system design or architecture interview.

### Short Answer (30 seconds)

45 minutes: clarify 5, diagram 10, deep dive 20, trade-offs 5, buffer 5.

### Detailed Answer (3–5 minutes)

**Capstone Time Boxing:**

45 minutes: clarify 5, diagram 10, deep dive 20, trade-offs 5, buffer 5.

**Production context (.NET/Azure):**
Apply in ASP.NET Core on Azure App Service or AKS with patterns from week 36.

**Key points:**
- When to use vs avoid
- Measurable outcome (latency, DORA, SLO)
- Common production pitfall and mitigation

**Example:** Instrument with Application Insights; track deployment in Azure DevOps.

**Architect:** Capture trade-offs in ADR when multiple valid approaches exist.

### Architecture Perspective

Capstone Time Boxing is foundational for week 36 — articulate clearly before tool names.

### Follow-up Questions

1. **How measure success? — Tie capstone time boxing to SLI, DORA metric, or business KPI.**
2. **Common anti-pattern? — Adopting tools before understanding capstone time boxing principles.**

### Common Mistakes in Interviews

- Define capstone time boxing with buzzwords only
- No concrete Azure/.NET example
- Cannot link concept to measurable outcome

---

## Q067: Idempotency in Checkout

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | System Design Capstone |
| **Frequency** | Common |

### Question

Explain idempotency in checkout for a system design or architecture interview.

### Short Answer (30 seconds)

Idempotency-Key on place-order; prevent double charge on retry.

### Detailed Answer (3–5 minutes)

**Idempotency in Checkout:**

Idempotency-Key on place-order; prevent double charge on retry.

**Production context (.NET/Azure):**
Apply in ASP.NET Core on Azure App Service or AKS with patterns from week 36.

**Key points:**
- When to use vs avoid
- Measurable outcome (latency, DORA, SLO)
- Common production pitfall and mitigation

**Example:** Instrument with Application Insights; track deployment in Azure DevOps.

**Architect:** Capture trade-offs in ADR when multiple valid approaches exist.

### Architecture Perspective

Idempotency in Checkout is foundational for week 36 — articulate clearly before tool names.

### Follow-up Questions

1. **How measure success? — Tie idempotency in checkout to SLI, DORA metric, or business KPI.**
2. **Common anti-pattern? — Adopting tools before understanding idempotency in checkout principles.**

### Common Mistakes in Interviews

- Define idempotency in checkout with buzzwords only
- No concrete Azure/.NET example
- Cannot link concept to measurable outcome

---

## Q068: Inventory Reservation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | System Design Capstone |
| **Frequency** | Common |

### Question

Explain inventory reservation for a system design or architecture interview.

### Short Answer (30 seconds)

Soft reserve on checkout start; TTL releases; prevent oversell.

### Detailed Answer (3–5 minutes)

**Inventory Reservation:**

Soft reserve on checkout start; TTL releases; prevent oversell.

**Production context (.NET/Azure):**
Apply in ASP.NET Core on Azure App Service or AKS with patterns from week 36.

**Key points:**
- When to use vs avoid
- Measurable outcome (latency, DORA, SLO)
- Common production pitfall and mitigation

**Example:** Instrument with Application Insights; track deployment in Azure DevOps.

**Architect:** Capture trade-offs in ADR when multiple valid approaches exist.

### Architecture Perspective

Inventory Reservation is foundational for week 36 — articulate clearly before tool names.

### Follow-up Questions

1. **How measure success? — Tie inventory reservation to SLI, DORA metric, or business KPI.**
2. **Common anti-pattern? — Adopting tools before understanding inventory reservation principles.**

### Common Mistakes in Interviews

- Define inventory reservation with buzzwords only
- No concrete Azure/.NET example
- Cannot link concept to measurable outcome

---

## Q069: Observability in Capstone

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | System Design Capstone |
| **Frequency** | Common |

### Question

Explain observability in capstone for a system design or architecture interview.

### Short Answer (30 seconds)

Always close with metrics, traces, SLO — checkout p99 alert example.

### Detailed Answer (3–5 minutes)

**Observability in Capstone:**

Always close with metrics, traces, SLO — checkout p99 alert example.

**Production context (.NET/Azure):**
Apply in ASP.NET Core on Azure App Service or AKS with patterns from week 36.

**Key points:**
- When to use vs avoid
- Measurable outcome (latency, DORA, SLO)
- Common production pitfall and mitigation

**Example:** Instrument with Application Insights; track deployment in Azure DevOps.

**Architect:** Capture trade-offs in ADR when multiple valid approaches exist.

### Architecture Perspective

Observability in Capstone is foundational for week 36 — articulate clearly before tool names.

### Follow-up Questions

1. **How measure success? — Tie observability in capstone to SLI, DORA metric, or business KPI.**
2. **Common anti-pattern? — Adopting tools before understanding observability in capstone principles.**

### Common Mistakes in Interviews

- Define observability in capstone with buzzwords only
- No concrete Azure/.NET example
- Cannot link concept to measurable outcome

---

## Q070: Phased Capstone Evolution

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | System Design Capstone |
| **Frequency** | Common |

### Question

Explain phased capstone evolution for a system design or architecture interview.

### Short Answer (30 seconds)

Phase 1 monolith+SQL; Phase 2 cache+queue; Phase 3 shard+multi-region.

### Detailed Answer (3–5 minutes)

**Phased Capstone Evolution:**

Phase 1 monolith+SQL; Phase 2 cache+queue; Phase 3 shard+multi-region.

**Production context (.NET/Azure):**
Apply in ASP.NET Core on Azure App Service or AKS with patterns from week 36.

**Key points:**
- When to use vs avoid
- Measurable outcome (latency, DORA, SLO)
- Common production pitfall and mitigation

**Example:** Instrument with Application Insights; track deployment in Azure DevOps.

**Architect:** Capture trade-offs in ADR when multiple valid approaches exist.

### Architecture Perspective

Phased Capstone Evolution is foundational for week 36 — articulate clearly before tool names.

### Follow-up Questions

1. **How measure success? — Tie phased capstone evolution to SLI, DORA metric, or business KPI.**
2. **Common anti-pattern? — Adopting tools before understanding phased capstone evolution principles.**

### Common Mistakes in Interviews

- Define phased capstone evolution with buzzwords only
- No concrete Azure/.NET example
- Cannot link concept to measurable outcome

---
