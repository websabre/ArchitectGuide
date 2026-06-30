# Week 24 — Intermediate Q&A

> Q031–Q070: Premium format (Week 1 quality).

---


## Q031: Capstone Architecture Review

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Very Common |

### Question

Present your microservices e-commerce capstone in 10 minutes.

### Short Answer (30 seconds)

Structure: problem (2m), context diagram (3m), key ADRs — decomposition, saga, data (3m), failure modes (2m).

### Detailed Answer (3–5 minutes)

Cover: bounded context map, sync vs async choices, idempotency, observability (trace ID), deployment independence proof.

### Architecture Perspective

Capstone presentation is interview simulation.

### Follow-up Questions

1. **What if interviewer challenges service count? — Defend with scale and team drivers or concede merge.**
2. **Cost estimate? — Order of magnitude monthly cloud cost.**

### Common Mistakes in Interviews

- No failure scenarios
- Diagram without legend
- Cannot explain why 8 services not 3

---

## Q032: Saga Compensation Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Sagas |
| **Frequency** | Very Common |

### Question

Payment succeeds, shipping fails — compensate?

### Short Answer (30 seconds)

Compensating transaction: refund payment (idempotent refund API), release inventory, mark order cancelled. Log compensation steps for audit.

### Detailed Answer (3–5 minutes)

Each saga step has defined compensator. Compensators must be idempotent too — retry safe.

Manual intervention queue for compensation failure — human workflow.

### Architecture Perspective

Compensation design is where sagas succeed or fail.

### Follow-up Questions

1. **Poison saga state? — Persist saga state machine — Durable Functions or custom table.**
2. **Timeout on saga step? — Trigger compensation automatically.**

### Common Mistakes in Interviews

- No compensation for payment step
- Hope shipping never fails
- Non-idempotent refund handler

---

## Q033: Observability Across Services

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Observability |
| **Frequency** | Very Common |

### Question

Trace order request across 5 microservices.

### Short Answer (30 seconds)

W3C trace context propagation on HTTP and messages. Single trace ID in logs. OpenTelemetry → App Insights/Jaeger.

### Detailed Answer (3–5 minutes)

Every service adds span: order-api, payment, inventory. Dashboard: p99 per hop — find slow service.

Architect mandates OTel SDK in service template.

### Architecture Perspective

Distributed tracing is non-negotiable for microservices.

### Follow-up Questions

1. **Baggage attributes? — Pass tenantId on trace for filtering.**
2. **Log correlation without tracing? — Insufficient at scale — use traces.**

### Common Mistakes in Interviews

- No trace ID in logs
- Broken trace at message bus boundary
- Each service different logging format

---

## Q034: Independent Deployment Proof

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DevOps |
| **Frequency** | Common |

### Question

How prove services deploy independently?

### Short Answer (30 seconds)

Separate CI/CD pipeline per repo/service. Deploy order v2 without touching catalog. Contract tests gate breaking changes.

### Detailed Answer (3–5 minutes)

Versioned API — consumers pin compatibility. Feature flags decouple deploy from release.

Demonstrate in capstone: GitHub Actions workflow per service.

### Architecture Perspective

Independent deploy is defining microservices characteristic.

### Follow-up Questions

1. **Shared pipeline monolith? — Red flag for distributed monolith.**
2. **Database migration blocks all services? — Coupled deploy — fix boundaries.**

### Common Mistakes in Interviews

- Monorepo single deploy button for all
- Shared DB migration coupling
- No contract tests

---

## Q035: Data Consistency Across Services

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Data |
| **Frequency** | Very Common |

### Question

Customer updates address — order history shows old address?

### Short Answer (30 seconds)

Snapshot address on order at placement time — don't JOIN live customer for historical orders. Eventual sync for display-only views.

### Detailed Answer (3–5 minutes)

Order aggregate stores `ShippingAddress` value object at confirm — immutable history.

Customer service owns current address — orders own snapshot.

### Architecture Perspective

Temporal consistency is business rule — architect clarifies with stakeholders.

### Follow-up Questions

1. **Event-carried state transfer? — Include needed fields in event payload.**
2. **Read model projection lag? — Accept for catalog; not for financial snapshot.**

### Common Mistakes in Interviews

- Live JOIN customer address on old orders
- No snapshot on transactional records
- Assuming strong consistency everywhere

---

## Q036: API Versioning Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | API Design |
| **Frequency** | Common |

### Question

Version microservices APIs without breaking consumers.

### Short Answer (30 seconds)

URL `/v1/` or header `Api-Version`. Deprecation policy: 6 months notice. Additive changes in minor; breaking in major.

### Detailed Answer (3–5 minutes)

Document in consumer portal. Automated breaking change detection in CI against Pact contracts.

### Architecture Perspective

API lifecycle governance prevents consumer breakage.

### Follow-up Questions

1. **GraphQL schema deprecation? — `@deprecated` directive — similar lifecycle.**
2. **Parallel run v1 and v2? — Route traffic gradually — strangler for APIs.**

### Common Mistakes in Interviews

- Breaking change without version bump
- Unlimited backward compatibility burden
- No deprecation timeline

---

## Q037: Security East-West Traffic

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Secure service-to-service communication.

### Short Answer (30 seconds)

mTLS via service mesh OR managed identity + private network. Never basic auth over HTTP internal.

### Detailed Answer (3–5 minutes)

Azure: Managed Identity service A calls service B with token. Private Link — no public endpoints.

Validate JWT or mTLS on every internal call — zero trust.

### Architecture Perspective

Internal network not trusted — architect assumes breach.

### Follow-up Questions

1. **Service principal per service? — Least privilege — not shared SP.**
2. **Network policy K8s? — Deny all default — allowlist per namespace.**

### Common Mistakes in Interviews

- HTTP internal without TLS
- Shared API key all services
- Public endpoints for internal APIs

---

## Q038: Load Test Microservices Platform

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Common |

### Question

How load test microservices vs monolith?

### Short Answer (30 seconds)

Test each service SLO independently plus critical user journeys E2E. Chaos inject downstream failure during load.

### Detailed Answer (3–5 minutes)

k6 scenarios: checkout journey 5K RPS. Monitor per-service CPU, p99, error rate, queue depth.

Find bottleneck service — scale or optimize that hop.

### Architecture Perspective

Load test proves architecture claims.

### Follow-up Questions

1. **Soak test? — 24h run — memory leak detection.**
2. **Chaos during load? — Validate circuit breakers under real traffic shape.**

### Common Mistakes in Interviews

- Only test monolith entry point
- No downstream failure injection
- Ignore queue backlog metric

---

## Q039: When to Merge Services Back

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Pragmatism |
| **Frequency** | Occasional |

### Question

Signs microservices should be merged?

### Short Answer (30 seconds)

Always deployed together, chatty sync calls, shared DB, team same standup, network latency > compute time.

### Detailed Answer (3–5 minutes)

Merge into modular monolith or single service — reduce ops overhead.

Architect ego must not prevent re-merge when boundaries wrong.

### Architecture Perspective

Pragmatism impresses senior interviewers.

### Follow-up Questions

1. **Reverse strangler? — Route back to monolith module — valid.**
2. **Metrics to decide? — Deploy coupling score, call ratio, cost per transaction.**

### Common Mistakes in Interviews

- Never merge — ideology
- Ignore ops cost of tiny services
- Nano-service per endpoint

---

## Q040: Month 6 Readiness Checklist

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Career |
| **Frequency** | Common |

### Question

What proves readiness after microservices month?

### Short Answer (30 seconds)

Bounded context map, saga diagram, 3 ADRs, capstone presented, Microservices Top 50 ≥75%, lab 21-24 complete, trace demo recorded.

### Detailed Answer (3–5 minutes)

Self-assess: can whiteboard checkout saga with compensation in 15 minutes? Can defend service boundaries to skeptical principal?

### Architecture Perspective

Readiness is demonstrable artifacts — not videos watched.

### Follow-up Questions

1. **Weakest area? — Log in progress tracker — revisit week.**
2. **Mock interview? — mock-05 checkout design.**

### Common Mistakes in Interviews

- No hands-on lab completed
- Cannot draw context map from memory
- Only theoretical microservices knowledge

---

## Q041: End-to-End Order Flow Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Very Common |

### Question

Design end-to-end order flow across API gateway, order, payment, inventory, notification services.

### Short Answer (30 seconds)

Sync: client → gateway → order (create). Async choreography: OrderPlaced → inventory reserve → payment capture → OrderConfirmed → notification. Idempotency keys on every step.

### Detailed Answer (3–5 minutes)

**Flow:**
1. `POST /orders` — validate, persist Draft, return 202 + orderId
2. Publish `OrderSubmitted`
3. Inventory: reserve (compensate: release)
4. Payment: capture (compensate: refund)
5. Order: confirm — publish `OrderConfirmed`
6. Notification: email/SMS (best effort)

**Architect diagram:** Number sync vs async hops. Trace ID from gateway. DLQ per consumer.

### Architecture Perspective

E2E flow design is capstone centerpiece — practice 10-minute whiteboard.

### Follow-up Questions

1. **Orchestration vs choreography here? — Choreography for demo; orchestration if complex compensation.**
2. **Duplicate submit handling? — Idempotency-Key header + unique constraint.**

### Common Mistakes in Interviews

- Synchronous payment in create HTTP request
- No compensation on inventory failure after payment
- Missing correlation ID across hops

---

## Q042: Payment Integration Saga

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Very Common |

### Question

Design payment saga step with Stripe — success, timeout, and duplicate callback.

### Short Answer (30 seconds)

Saga state: PendingPayment → Paid | Failed. Call Stripe with idempotency key = orderId. Webhook `payment_intent.succeeded` is source of truth — API response may race webhook.

### Detailed Answer (3–5 minutes)

**Steps:**
1. Saga publishes `ChargePaymentCommand`
2. Payment service creates PaymentIntent (idempotent)
3. Webhook handler updates saga — idempotent on event ID
4. Timeout 30s → query Stripe → reconcile state

**Compensation:** `Refund` with idempotency key `refund-{orderId}`.

**Architect:** Never trust client-side payment success alone.

### Architecture Perspective

Payment saga is where money is lost or duplicated — depth matters.

### Follow-up Questions

1. **Exactly-once payment? — Impossible — idempotent at-least-once achieves effectively-once.**
2. **PCI scope? — Tokenize card client-side — payment service never stores PAN.**

### Common Mistakes in Interviews

- Double capture on webhook retry
- No reconciliation job for stuck PendingPayment
- Saga state only in memory

---

## Q043: Inventory Reservation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Very Common |

### Question

Design inventory reservation — optimistic vs pessimistic, oversell prevention.

### Short Answer (30 seconds)

Pessimistic: `UPDATE stock SET qty = qty - @n WHERE sku = @s AND qty >= @n` — row lock. Optimistic: version column — retry on conflict. Reserve holds stock with TTL; release on payment failure.

### Detailed Answer (3–5 minutes)

**Pattern:**
- `ReservedQuantity` + `AvailableQuantity` columns OR reservation table
- TTL job releases expired reservations
- Event: `InventoryReserved`, `InventoryReleased`, `InventoryDepleted`

**Architect:** Hot SKU may need shard by SKU or queue serialization — document contention plan.

### Architecture Perspective

Inventory is classic distributed consistency challenge.

### Follow-up Questions

1. **Oversell acceptable? — Business question — flash sale may allow 1% oversell with apology.**
2. **Read inventory from catalog cache? — Stale for display OK; never for reservation write.**

### Common Mistakes in Interviews

- Check-then-act race without transaction
- No reservation TTL
- Inventory and catalog share writable table

---

## Q044: Notification Async Path

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Common |

### Question

Order confirmed — design async notification path that never blocks checkout.

### Short Answer (30 seconds)

Subscribe to `OrderConfirmed` — enqueue notification job. Worker sends email via SendGrid, SMS via Twilio. Failures → retry with backoff → DLQ — order already committed.

### Detailed Answer (3–5 minutes)

**Design:**
- At-least-once delivery — template idempotency key `orderId-channel`
- Preference service: opt-out, channel choice
- Dead letter alerts ops — don't rollback order

**Architect:** Notifications are side effect — saga completes without waiting for email.

### Architecture Perspective

Async notification path teaches fire-and-forget done right.

### Follow-up Questions

1. **Transactional outbox to notification queue? — Yes — don't dual-write bus + DB.**
2. **User notification preferences? — Filter before send — GDPR marketing opt-out.**

### Common Mistakes in Interviews

- Sync SMTP in order confirm transaction
- Notification failure cancels order
- No idempotency on email send

---

## Q045: Observability Across Services

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Very Common |

### Question

Mandate observability standards for capstone microservices platform.

### Short Answer (30 seconds)

Every service: OpenTelemetry SDK, W3C `traceparent`, structured JSON logs with traceId, RED metrics (rate, errors, duration), health `/health/live` + `/health/ready`.

### Detailed Answer (3–5 minutes)

**Platform mandate:**
- Service template ships OTel + Serilog enricher
- Dashboard: checkout golden trace — p99 per hop
- Alert: error rate >1% 5m window

**Architect:** Observability is non-negotiable gate for production readiness review.

### Architecture Perspective

Cross-service observability separates toy from production architecture.

### Follow-up Questions

1. **Service map? — App Insights Application Map or Jaeger dependency view.**
2. **SLO-based alerts? — Burn rate on availability SLO — not CPU-only.**

### Common Mistakes in Interviews

- Logs without trace correlation
- Broken trace at message broker
- Each team custom metrics naming

---

## Q046: Centralized Logging

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Common |

### Question

Design centralized logging for 12 microservices — collection, retention, PII.

### Short Answer (30 seconds)

Agents: stdout JSON → Fluent Bit/Fluentd → OpenSearch or Log Analytics. Index by service, environment, traceId. Retention: 30d hot, 1y cold archive.

### Detailed Answer (3–5 minutes)

**Standards:**
- Mandatory fields: `timestamp`, `level`, `service`, `traceId`, `spanId`, `message`, `properties`
- PII scrubbing at ingest — regex card/email
- RBAC on log access — prod logs restricted

**Architect:** Central logging is compliance and incident requirement — budget storage.

### Architecture Perspective

Centralized logging enables cross-service incident response.

### Follow-up Questions

1. **Log volume cost control? — Sampling debug; structured INFO only prod.**
2. **Correlation without tracing? — traceId in logs minimum.**

### Common Mistakes in Interviews

- SSH to pod to tail logs
- Unredacted PII in centralized store
- No retention policy — unbounded cost

---

## Q047: SLO per Service

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Very Common |

### Question

Define SLOs for order, payment, and catalog services.

### Short Answer (30 seconds)

Order API: 99.9% availability, p99 latency <300ms. Payment: 99.95% (money path). Catalog read: 99.5%, p99 <100ms. Error budget policy: freeze features if budget exhausted.

### Detailed Answer (3–5 minutes)

**SLO template:**
- SLI: successful requests / total (exclude 4xx client errors optionally)
- Window: 30-day rolling
- Alert: multi-burn-rate — 14.4x burn page immediately

**Architect:** SLO per service — not one global — reflects business criticality.

### Architecture Perspective

Per-service SLO drives prioritization and error budget culture.

### Follow-up Questions

1. **Dependency SLO? — Order SLO can't exceed product of critical deps — document.**
2. **Synthetic probes? — Checkout canary every 1m — SLI supplement.**

### Common Mistakes in Interviews

- One 99.99% SLO for everything
- SLO without error budget policy
- Latency SLO on p50 only

---

## Q048: Deployment Independence

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Very Common |

### Question

Prove deployment independence — order v2.3 ships while catalog stays on v1.8.

### Short Answer (30 seconds)

Separate CI/CD per service repo. Contract tests in consumer pipeline. Backward-compatible API — v2 adds fields; catalog never calls order internal endpoints.

### Detailed Answer (3–5 minutes)

**Proof points:**
- GitHub Actions workflow scoped to service path
- Blue/green or rolling deploy per K8s deployment
- Feature flags decouple deploy from exposure
- Shared infra (K8s cluster) OK — shared *deploy button* not OK

**Architect:** Independent deploy is defining characteristic — demo in capstone.

### Architecture Perspective

Deployment independence must be demonstrable not asserted.

### Follow-up Questions

1. **Database migration blocks all services? — Coupled — fix schema ownership.**
2. **Monorepo deploy? — Path-filtered pipelines still independent.**

### Common Mistakes in Interviews

- Single release train all services
- Breaking API without consumer notice
- Shared library forces lockstep deploy

---

## Q049: Database Migration per Service

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Common |

### Question

Each microservice owns its database — migration strategy without coupling.

### Short Answer (30 seconds)

Flyway/Liquibase/EF migrations per service repo. Expand-contract for shared data elimination. No cross-service FK — use events for sync.

### Detailed Answer (3–5 minutes)

**Expand-contract example:**
1. Add nullable column (expand)
2. Dual-write both old and new
3. Backfill job
4. Switch reads
5. Drop old column (contract)

**Architect:** Migration runs in service pipeline pre-deploy — failed migration blocks only that service.

### Architecture Perspective

Per-service migrations enable true ownership.

### Follow-up Questions

1. **Shared DBA runs all migrations? — OK ops — scripts still owned by service team.**
2. **Breaking schema change on event payload? — Version event — parallel consumers.**

### Common Mistakes in Interviews

- Cross-service foreign keys
- Manual SQL in prod without version control
- Migration rollback untested

---

## Q050: API Composition vs Aggregation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Common |

### Question

Mobile app needs order + customer + product names — composition layer or client calls three APIs?

### Short Answer (30 seconds)

API aggregation (BFF): single `GET /mobile/orders/{id}` composes three service calls server-side — reduces chattiness, controls response shape. Not full GraphQL unless needed.

### Detailed Answer (3–5 minutes)

**Composition (API gateway):** route + light transform — no heavy logic.

**Aggregation (BFF):** fan-out parallel `Task.WhenAll`, timeout per dependency, partial response policy.

**Architect:** BFF per client type (mobile, web) — not per microservice.

### Architecture Perspective

Composition vs aggregation terminology often confused — clarify in interview.

### Follow-up Questions

1. **BFF god object? — Only presentation logic — no domain rules.**
2. **Cache composed response? — Short TTL — invalidate on order event.**

### Common Mistakes in Interviews

- Mobile calls 8 microservices directly
- BFF writes to multiple service DBs
- No timeout on fan-out composition

---

## Q051: GraphQL Federation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Occasional |

### Question

Evaluate GraphQL federation for order + catalog + customer supergraph.

### Short Answer (30 seconds)

Each service owns subgraph schema — gateway federates. Order subgraph extends `Customer` with `orders` field — resolved via reference.

### Detailed Answer (3–5 minutes)

**Pros:** Single query mobile, typed schema, team-owned subgraphs.

**Cons:** Operational complexity, N+1 at scale (dataloader), caching harder than REST CDN.

**Architect:** Federation when many client-driven field combinations — not default for simple CRUD.

### Architecture Perspective

Federation is product-facing aggregation pattern.

### Follow-up Questions

1. **Schema governance? — Rover checks breaking changes in CI.**
2. **Federation vs BFF? — Federation client-driven; BFF server-curated payloads.**

### Common Mistakes in Interviews

- Monolithic GraphQL schema one team
- No query depth/complexity limits
- Federation without performance testing

---

## Q052: Event Schema Governance

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Very Common |

### Question

Govern integration event schemas across 8 teams.

### Short Answer (30 seconds)

Schema registry (Avro/JSON Schema) with BACKWARD compatibility. PR checks: additive fields only in minor. `{Event}V{n}` naming. Owning team publishes schema repo.

### Detailed Answer (3–5 minutes)

**Process:**
1. Propose schema change in ADR
2. CI compatibility check
3. Register new version
4. Consumers regenerate stubs
5. Deprecation window 90 days

**Architect:** Schema council reviews breaking changes — platform team enforces registry.

### Architecture Perspective

Event schema governance prevents distributed monolith breakage.

### Follow-up Questions

1. **Optional vs required fields? — New fields optional with default — Avro unions.**
2. **Unknown producer event? — Reject at registry — no ad hoc topics.**

### Common Mistakes in Interviews

- Unversioned JSON blobs on bus
- Breaking rename without major version
- No consumer contract tests

---

## Q053: Breaking Change Policy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Common |

### Question

Microservice API breaking change policy — steps before removing field.

### Short Answer (30 seconds)

1. Announce deprecation in changelog + `Sunset` header. 2. Maintain parallel v1/v2 minimum 6 months. 3. Metrics on v1 traffic — notify stragglers. 4. Remove only at zero consumers (Pact verification).

### Detailed Answer (3–5 minutes)

**Breaking:** remove field, rename, change type, narrow enum.

**Non-breaking:** add optional field, add endpoint.

**Architect:** Policy in platform handbook — automated breaking change detection in CI.

### Architecture Perspective

Breaking change discipline protects internal API consumers.

### Follow-up Questions

1. **Consumer-driven contracts? — Pact — provider verifies before deploy.**
2. **Sunset header? — `Sunset: Sat, 01 Jan 2027` — HTTP standard.**

### Common Mistakes in Interviews

- Remove field because unused (unmeasured)
- No version bump
- Break mobile app without coordination

---

## Q054: On-Call Ownership

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Common |

### Question

Define on-call ownership model for order and payment services.

### Short Answer (30 seconds)

Each service has primary owning team on-call rotation. Platform team on-call for K8s/ingress. Escalation: L1 service → L2 domain architect → vendor (Stripe).

### Detailed Answer (3–5 minutes)

**Runbook link in PagerDuty service.** SLO pages go to owning team — not centralized ops only.

**Architect:** Conway's Law — team that builds runs — no throw-over-wall ops.

### Architecture Perspective

On-call ownership is production architecture concern.

### Follow-up Questions

1. **Shared on-call for all microservices? — Ownership blur — slow incident response.**
2. **Follow-the-sun? — For global product — handoff documented.**

### Common Mistakes in Interviews

- No owning team for service
- Platform team pages for app bugs
- On-call without runbook access

---

## Q055: Runbook per Service

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Common |

### Question

What belongs in a microservice runbook? Example for payment service.

### Short Answer (30 seconds)

Architecture diagram, dependencies, SLO, alert catalog, common failures (webhook delay, Stripe outage), rollback steps, escalation contacts, useful queries/dashboards.

### Detailed Answer (3–5 minutes)

**Payment runbook sections:**
1. **Overview** — purpose, team, repo
2. **Dependencies** — Stripe, SQL, Service Bus
3. **Alerts** — `PaymentErrorRateHigh` → check Stripe status page
4. **Procedures** — replay DLQ, reconcile stuck sagas
5. **Rollback** — Helm revision `helm rollback`

**Architect:** Runbook tested in game day — not shelfware.

### Architecture Perspective

Runbooks convert architecture knowledge to incident action.

### Follow-up Questions

1. **Runbook as code? — Markdown in repo — PR reviewed.**
2. **Game day? — Quarterly simulate Stripe down — measure MTTR.**

### Common Mistakes in Interviews

- Runbook only 'restart pod'
- No dependency list
- Outdated runbook after redesign

---

## Q056: Chaos Test Microservices

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Common |

### Question

Design chaos experiments for order checkout path.

### Short Answer (30 seconds)

Hypothesis: when inventory latency +2s, checkout p99 stays <2s due to timeout + circuit breaker. Experiment: Litmus/Gremlin inject latency on inventory pod 5% traffic.

### Detailed Answer (3–5 minutes)

**Experiments:**
- Kill payment pod — verify retry + no double charge
- Partition Service Bus — orders queue but recover
- DNS failure to Stripe — fail gracefully

**Architect:** Start staging — prod blast radius controlled — one service one experiment.

### Architecture Perspective

Chaos validates resilience architecture claims.

### Follow-up Questions

1. **Blast radius? — Single AZ, single pod, 5% traffic — expand gradually.**
2. **Steady state hypothesis? — Define measurable before experiment.**

### Common Mistakes in Interviews

- Chaos only on CPU — not dependencies
- Prod chaos without approval
- No rollback on experiment failure

---

## Q057: Load Test Distributed

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Very Common |

### Question

Load test distributed checkout — approach and metrics.

### Short Answer (30 seconds)

k6/Gatling scenarios: realistic think time, ramp to target RPS, run from multiple regions. Monitor per-service CPU, p99, error rate, queue depth, DB connections.

### Detailed Answer (3–5 minutes)

**Phases:**
1. Baseline single service
2. Integration path 10% target
3. Full target + soak 4h
4. Chaos + load combined

**Bottleneck service:** scale or optimize that hop — document in ADR.

**Architect:** Load test proves SLO achievability — not checkbox.

### Architecture Perspective

Distributed load test finds weakest service in chain.

### Follow-up Questions

1. **Coordinated omission? — k6 handles — validate tool.**
2. **Test data isolation? — Dedicated load tenant — don't corrupt prod-like shared data.**

### Common Mistakes in Interviews

- Load only API gateway
- Ignore message queue backlog
- Single-region test for global app

---

## Q058: Cost Allocation Microservices

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Occasional |

### Question

Allocate cloud cost per microservice team.

### Short Answer (30 seconds)

Tag every resource: `service`, `team`, `environment`. Cost explorer / FinOps dashboard per team monthly. Showback before chargeback.

### Detailed Answer (3–5 minutes)

**Tags:** AKS namespaces labeled, SQL per service account, Service Bus topics named by owner.

**Architect:** Cost visibility drives right-sizing — orphan services get retired.

### Architecture Perspective

FinOps is part of architecture governance.

### Follow-up Questions

1. **Untagged shared cluster cost? — Split by CPU/memory request ratio.**
2. **Cost anomaly alert? — 30% week-over-week spike.**

### Common Mistakes in Interviews

- No tagging standards
- One shared mega-SQL for all
- Teams blind to their cloud bill

---

## Q059: Team Topology Team Topologies

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Common |

### Question

Map Team Topologies to your microservices capstone teams.

### Short Answer (30 seconds)

Stream-aligned: Order team, Payment team (own E2E features). Platform: internal developer portal, K8s, CI templates. Enabling: DDD coach/adoption. Complicated-subsystem: fraud ML if needed.

### Detailed Answer (3–5 minutes)

**Interaction modes:** Collaboration (discovery) → X-as-a-Service (platform APIs) → Facilitating (enablement).

**Architect:** Team boundaries align with service boundaries — reduce cognitive load per team (2-pizza).

### Architecture Perspective

Team Topologies vocabulary shows organizational architecture fluency.

### Follow-up Questions

1. **Platform as product? — Golden paths, self-service deploy — not ticket ops.**
2. **Too many stream-aligned teams? — Thinnest viable stream.**

### Common Mistakes in Interviews

- One team owns 15 services
- Platform team does all deploys
- Conway ignored in service split

---

## Q060: Production Readiness Review Microservices

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Very Common |

### Question

Production readiness review checklist before capstone go-live.

### Short Answer (30 seconds)

SLO defined, dashboards, alerts, runbooks, on-call rotation, security scan, pen test items closed, load test passed, chaos done, DR tested, migration rollback, feature flags, incident response drill.

### Detailed Answer (3–5 minutes)

**PRR gate items:**
- [ ] OTel traces E2E demo recorded
- [ ] Secrets in Key Vault — no .env in image
- [ ] Pact contracts green
- [ ] Error budget policy acknowledged
- [ ] Data backup RPO/RTO documented

**Architect:** PRR is formal sign-off — not informal 'looks good'.

### Architecture Perspective

PRR demonstrates you ship responsibly not just design.

### Follow-up Questions

1. **Gradual rollout? — Canary 5% → 25% → 100% with metric gates.**
2. **Rollback tested? — One-click verified in staging.**

### Common Mistakes in Interviews

- Skip PRR for demo
- No on-call before launch
- Load test never run at target RPS

---

## Q061: Capstone Context Diagram

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: Capstone Context Diagram — what do you need to know and decide?

### Short Answer (30 seconds)

Capstone Context Diagram requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 24 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 24 — Capstone):**
- Scenario: production system at scale needs a decision involving *Capstone Context Diagram*
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

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect Capstone Context Diagram to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove Capstone Context Diagram is healthy in production?**
2. **What is the rollback plan if Capstone Context Diagram change fails?**

### Common Mistakes in Interviews

- Treating Capstone Context Diagram as set-and-forget with no monitoring
- No ADR documenting trade-offs for Capstone Context Diagram
- Copying Capstone Context Diagram pattern from blog without context fit

---

## Q062: Capstone Container Diagram

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: Capstone Container Diagram — what do you need to know and decide?

### Short Answer (30 seconds)

Capstone Container Diagram requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 24 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 24 — Capstone):**
- Scenario: production system at scale needs a decision involving *Capstone Container Diagram*
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

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect Capstone Container Diagram to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove Capstone Container Diagram is healthy in production?**
2. **What is the rollback plan if Capstone Container Diagram change fails?**

### Common Mistakes in Interviews

- Treating Capstone Container Diagram as set-and-forget with no monitoring
- No ADR documenting trade-offs for Capstone Container Diagram
- Copying Capstone Container Diagram pattern from blog without context fit

---

## Q063: Capstone Deployment View

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: Capstone Deployment View — what do you need to know and decide?

### Short Answer (30 seconds)

Capstone Deployment View requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 24 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 24 — Capstone):**
- Scenario: production system at scale needs a decision involving *Capstone Deployment View*
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

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect Capstone Deployment View to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove Capstone Deployment View is healthy in production?**
2. **What is the rollback plan if Capstone Deployment View change fails?**

### Common Mistakes in Interviews

- Treating Capstone Deployment View as set-and-forget with no monitoring
- No ADR documenting trade-offs for Capstone Deployment View
- Copying Capstone Deployment View pattern from blog without context fit

---

## Q064: Capstone NFR Matrix

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: Capstone NFR Matrix — what do you need to know and decide?

### Short Answer (30 seconds)

Capstone NFR Matrix requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 24 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 24 — Capstone):**
- Scenario: production system at scale needs a decision involving *Capstone NFR Matrix*
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

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect Capstone NFR Matrix to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove Capstone NFR Matrix is healthy in production?**
2. **What is the rollback plan if Capstone NFR Matrix change fails?**

### Common Mistakes in Interviews

- Treating Capstone NFR Matrix as set-and-forget with no monitoring
- No ADR documenting trade-offs for Capstone NFR Matrix
- Copying Capstone NFR Matrix pattern from blog without context fit

---

## Q065: Capstone Threat Model Summary

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: Capstone Threat Model Summary — what do you need to know and decide?

### Short Answer (30 seconds)

Capstone Threat Model Summary requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 24 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 24 — Capstone):**
- Scenario: production system at scale needs a decision involving *Capstone Threat Model Summary*
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

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect Capstone Threat Model Summary to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove Capstone Threat Model Summary is healthy in production?**
2. **What is the rollback plan if Capstone Threat Model Summary change fails?**

### Common Mistakes in Interviews

- Treating Capstone Threat Model Summary as set-and-forget with no monitoring
- No ADR documenting trade-offs for Capstone Threat Model Summary
- Copying Capstone Threat Model Summary pattern from blog without context fit

---

## Q066: Capstone Cost Estimate

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: Capstone Cost Estimate — what do you need to know and decide?

### Short Answer (30 seconds)

Capstone Cost Estimate requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 24 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 24 — Capstone):**
- Scenario: production system at scale needs a decision involving *Capstone Cost Estimate*
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

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect Capstone Cost Estimate to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove Capstone Cost Estimate is healthy in production?**
2. **What is the rollback plan if Capstone Cost Estimate change fails?**

### Common Mistakes in Interviews

- Treating Capstone Cost Estimate as set-and-forget with no monitoring
- No ADR documenting trade-offs for Capstone Cost Estimate
- Copying Capstone Cost Estimate pattern from blog without context fit

---

## Q067: Capstone Demo Script

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: Capstone Demo Script — what do you need to know and decide?

### Short Answer (30 seconds)

Capstone Demo Script requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 24 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 24 — Capstone):**
- Scenario: production system at scale needs a decision involving *Capstone Demo Script*
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

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect Capstone Demo Script to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove Capstone Demo Script is healthy in production?**
2. **What is the rollback plan if Capstone Demo Script change fails?**

### Common Mistakes in Interviews

- Treating Capstone Demo Script as set-and-forget with no monitoring
- No ADR documenting trade-offs for Capstone Demo Script
- Copying Capstone Demo Script pattern from blog without context fit

---

## Q068: Capstone Rollback Plan

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: Capstone Rollback Plan — what do you need to know and decide?

### Short Answer (30 seconds)

Capstone Rollback Plan requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 24 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 24 — Capstone):**
- Scenario: production system at scale needs a decision involving *Capstone Rollback Plan*
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

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect Capstone Rollback Plan to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove Capstone Rollback Plan is healthy in production?**
2. **What is the rollback plan if Capstone Rollback Plan change fails?**

### Common Mistakes in Interviews

- Treating Capstone Rollback Plan as set-and-forget with no monitoring
- No ADR documenting trade-offs for Capstone Rollback Plan
- Copying Capstone Rollback Plan pattern from blog without context fit

---

## Q069: Capstone Feature Flag Plan

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: Capstone Feature Flag Plan — what do you need to know and decide?

### Short Answer (30 seconds)

Capstone Feature Flag Plan requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 24 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 24 — Capstone):**
- Scenario: production system at scale needs a decision involving *Capstone Feature Flag Plan*
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

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect Capstone Feature Flag Plan to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove Capstone Feature Flag Plan is healthy in production?**
2. **What is the rollback plan if Capstone Feature Flag Plan change fails?**

### Common Mistakes in Interviews

- Treating Capstone Feature Flag Plan as set-and-forget with no monitoring
- No ADR documenting trade-offs for Capstone Feature Flag Plan
- Copying Capstone Feature Flag Plan pattern from blog without context fit

---

## Q070: Capstone Data Flow Diagram

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Very Common |

### Question

Architect-level Intermediate: Capstone Data Flow Diagram — what do you need to know and decide?

### Short Answer (30 seconds)

Capstone Data Flow Diagram requires understanding trade-offs, production failure modes, and clear ADR documentation for Week 24 (Intermediate tier).

### Detailed Answer (3–5 minutes)

**Context (Week 24 — Capstone):**
- Scenario: production system at scale needs a decision involving *Capstone Data Flow Diagram*
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

**Interview tip:** Lead with business impact, then mechanism, then operational guardrails.

### Architecture Perspective

Intermediate interviewers expect you to connect Capstone Data Flow Diagram to real operations — not definitions alone. Show governance and measurable outcomes.

### Follow-up Questions

1. **What metrics prove Capstone Data Flow Diagram is healthy in production?**
2. **What is the rollback plan if Capstone Data Flow Diagram change fails?**

### Common Mistakes in Interviews

- Treating Capstone Data Flow Diagram as set-and-forget with no monitoring
- No ADR documenting trade-offs for Capstone Data Flow Diagram
- Copying Capstone Data Flow Diagram pattern from blog without context fit

---
