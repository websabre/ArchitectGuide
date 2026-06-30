# Microservices Top 50 — Part 3 (Q031–Q050)

> **Sagas, Migration, Scenarios, Capstone** | Weeks 21–24 | [Part 1](microservices-top-50-qa-part1.md) | [Part 2](microservices-top-50-qa-part2.md) | [Index](microservices-top-50-index.md)

---


## Q031: Scenario — Payment Double Charge

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Scenario |
| **Week** | 24 |

### Question

A customer was charged twice when the mobile app retried checkout after a timeout. Design the fix.

### Short Answer (30 seconds)

Require `Idempotency-Key` header on payment API; store key→result mapping 24h; same key returns cached response without re-charging. Pair with saga compensation if partial failure after charge.

### Detailed Answer (3–5 minutes)

**Root cause:** Client timeout ≠ server failure — payment succeeded but client retried.

**Fix layers:**
1. **Client:** Generate UUID idempotency key per checkout attempt; retry with same key
2. **Payment API:**
```sql
INSERT INTO idempotency_keys (key, response, created_at)
VALUES (@key, @response, NOW())
ON CONFLICT (key) DO NOTHING RETURNING response;
```
3. **Store result** before returning 200 — include `transactionId`
4. **Saga:** If charge succeeded but order creation failed → compensating refund (idempotent refund API)

**Monitoring:** Alert on duplicate key hits > baseline — may indicate client bug.

**Architect:** Idempotency is mandatory for all money-moving POST endpoints — document in API standards.

### Follow-up Questions

1. **Idempotency key TTL? — 24h typical; 7d for B2B with slow retries.**
2. **Stripe-style approach? — Same pattern — `Idempotency-Key` header is industry standard.**

### Common Mistakes

- Relying on client to never retry
- Idempotency check after side effect executes

---

## Q032: Scenario — Inventory Oversell

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Scenario |
| **Week** | 24 |

### Question

During a flash sale, 100 units were sold to 150 customers. How do you prevent inventory oversell?

### Short Answer (30 seconds)

Use atomic reservation with optimistic or pessimistic concurrency — never read-then-write without version check. Reserve with TTL; confirm on payment; release on timeout.

### Detailed Answer (3–5 minutes)

**Anti-pattern:**
```sql
SELECT stock FROM products WHERE id = @id; -- reads 1
-- 150 concurrent requests all see stock >= 1
UPDATE products SET stock = stock - 1 WHERE id = @id;
```

**Fix — optimistic concurrency:**
```sql
UPDATE inventory SET quantity = quantity - 1, version = version + 1
WHERE product_id = @id AND quantity > 0 AND version = @expectedVersion;
-- rows affected = 0 → return 409 Conflict to client
```

**Reservation pattern:**
1. `Reserve(quantity)` → hold with 15-min TTL
2. Payment succeeds → `ConfirmReservation`
3. Payment fails / timeout → `ReleaseReservation`

**Overflow:** Queue excess orders; show "waitlisted" UX.

**Architect:** Flash sale = load test scenario — Redis atomic DECR or SQL row lock — pick based on consistency needs.

### Follow-up Questions

1. **Redis vs SQL for inventory? — Redis for speed with periodic reconciliation to SQL source of truth.**
2. **Oversell acceptable? — Some catalogs allow 2% oversell — business decision, not technical default.**

### Common Mistakes

- Read-then-write without locking or version column
- No reservation TTL — orphan holds block inventory

---

## Q033: Scenario — Cascading Failure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Scenario |
| **Week** | 21 |

### Question

A slow recommendation service took down the entire homepage. How do you contain the failure?

### Short Answer (30 seconds)

Circuit breaker + aggressive timeout + fallback (empty recommendations) + bulkhead isolation. Homepage must degrade gracefully — never fail because a non-critical dependency is slow.

### Detailed Answer (3–5 minutes)

**Failure chain:** Homepage → Recommendations (30s timeout) → thread pool exhausted → all requests queue → 503 everywhere.

**Containment:**
1. **Timeout:** 500ms for recommendations — not 30s
2. **Circuit breaker:** Open after 50% failures in 10s
3. **Fallback:** Return cached popular items or empty section
4. **Bulkhead:** Separate thread pool for recommendations vs core content
5. **Async load:** Fetch recommendations client-side or via edge cache

**UX:** Hide recommendations section vs show skeleton — A/B test; empty is better than spinner forever.

**Architect:** Classify dependencies Tier 1 (must work) vs Tier 3 (nice to have) — different resilience policies per tier.

### Follow-up Questions

1. **Chaos engineering validation? — Inject latency on recommendations in staging — verify homepage SLO holds.**
2. **Retry storm? — Don't retry slow dependency when circuit open — amplifies load.**

### Common Mistakes

- Same timeout for payment and recommendations
- No fallback — 500 when non-critical service fails

---

## Q034: Scenario — Schema Migration Zero Downtime

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Scenario |
| **Week** | 23 |

### Question

You must add a non-null column to the orders table in production with zero downtime. Walk through the approach.

### Short Answer (30 seconds)

Use expand-contract: add nullable column → deploy code that writes both old and new → backfill → enforce NOT NULL → remove old column. Never breaking schema + code in same deploy.

### Detailed Answer (3–5 minutes)

**Expand-contract phases:**
1. **Expand:** `ALTER TABLE orders ADD new_status VARCHAR(20) NULL`
2. **Deploy app v1:** Writes to both `status` and `new_status`; reads from `status`
3. **Backfill:** `UPDATE orders SET new_status = status WHERE new_status IS NULL` (batched)
4. **Deploy app v2:** Reads from `new_status`; still writes both
5. **Contract:** `ALTER TABLE orders ALTER COLUMN new_status SET NOT NULL`
6. **Deploy app v3:** Drop `status` column reference
7. **Cleanup:** `ALTER TABLE orders DROP COLUMN status`

**Rolling deploy:** Old and new pods coexist — schema must support both versions.

**EF Core:** Multiple migrations across releases, not one big migration.

**Architect:** Document in ADR; run during low traffic; monitor replication lag on backfill.

### Follow-up Questions

1. **Rename column? — Add new → copy → switch reads → drop old — never `RENAME` in one step with live traffic.**
2. **Blue/green DB? — Dual-write to both databases during migration — higher cost, faster cutover.**

### Common Mistakes

- NOT NULL column added and populated in single deploy
- Breaking rename without dual-write period

---

## Q035: Scenario — 90-Day Microservices Plan

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Scenario |
| **Week** | 23 |

### Question

You inherit a .NET monolith. Outline a 90-day plan to extract the first microservice safely.

### Short Answer (30 seconds)

Days 1–30: domain discovery, CI/CD, observability, pick extraction candidate. Days 31–60: strangler routing, build service, 5% traffic. Days 61–90: ramp to 100%, retire legacy path, document playbook for service #2.

### Detailed Answer (3–5 minutes)

**Days 1–30:** Domain discovery (event storming), DORA baseline, CI/CD + observability on monolith, pick extraction candidate (highest pain module), ADR for boundaries.

**Days 31–60:** Strangler proxy routing, build new service with contract tests, dual-write/CDC data sync, deploy to production behind feature flag at 5% traffic.

**Days 61–90:** Ramp to 100%, retire monolith path, postmortem retrospective, document playbook for service #2.

**Prerequisites before day 1 extract:** Automated deploy, centralized logging, distributed tracing, on-call rotation.

**Architect deliverables:** Bounded context map, context integration diagram, saga/outbox decision, team topology alignment (Conway's Law).

### Follow-up Questions

1. **Which service first? — Highest business value + clearest boundary — often notifications or catalog read path.**
2. **Team structure? — Stream-aligned team owns extracted service before extraction completes.**

### Common Mistakes

- Extracting without observability baseline
- Big-bang rewrite in 90 days instead of strangler

---

## Q036: Strangler Fig Success Metrics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Migration |
| **Week** | 23 |

### Question

What metrics prove a strangler fig migration is succeeding and ready for legacy retirement?

### Short Answer (30 seconds)

Track traffic % on new path, error rate parity, p95 latency delta, data reconciliation drift, and monolith code deletion progress. Retire legacy only when all SLOs match for 2+ weeks at 100% traffic.

### Detailed Answer (3–5 minutes)

**Migration dashboard:**
| Metric | Target |
|--------|--------|
| Traffic on new service | → 100% |
| Error rate vs monolith | ≤ monolith baseline |
| p95 latency | ≤ monolith + 10% |
| Data reconciliation | 0 drift rows |
| Monolith LOC removed | Increasing weekly |

**Data sync:** Nightly job compares monolith vs new service row counts and checksums — alert on mismatch.

**Rollback criteria:** Error rate 2× baseline for 15 min → flip feature flag to 0%.

**Architect:** Define retirement ceremony — delete routing rule, archive monolith module, update CMDB.

### Follow-up Questions

1. **Canary analysis? — Compare golden signals (errors, latency, throughput) between old and new during ramp.**
2. **Business metrics? — Conversion rate parity — technical metrics aren't sufficient alone.**

### Common Mistakes

- Retiring legacy at 95% traffic with known edge cases
- No data reconciliation between old and new stores

---

## Q037: Scenario — Homepage Fan-Out

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Scenario |
| **Week** | 22 |

### Question

The homepage calls 20 microservices synchronously and is slow. Redesign the architecture.

### Short Answer (30 seconds)

Introduce BFF with aggregated endpoint, materialized read model, or GraphQL federation. Target ≤3 network calls from client; parallelize server-side fetches with bounded concurrency.

### Detailed Answer (3–5 minutes)

**Current:** Mobile → 20 sequential HTTP calls → 3s page load.

**Redesign options:**
1. **BFF `/home` endpoint** — server parallelizes 20 fetches with `Task.WhenAll`, 200ms internal budget
2. **Materialized view** — `HomepageProjection` updated by `ProductUpdated`, `PromoChanged` events — single DB read
3. **Edge cache** — CDN caches `/home` JSON 60s for anonymous users
4. **GraphQL** — single request, resolver batching (DataLoader)

**Anti-patterns to eliminate:**
- Sequential awaits in BFF
- No timeout per downstream
- Fetching full objects when IDs suffice

**Architect:** CQRS read model is best for high-traffic homepage; BFF is faster to ship.

### Follow-up Questions

1. **GraphQL vs BFF REST? — GraphQL flexible for web; BFF REST simpler for mobile teams.**
2. **Cache invalidation? — Event-driven purge on product/price change.**

### Common Mistakes

- BFF that sequentially calls 20 services
- No caching on read-heavy homepage

---

## Q038: Build vs Buy Framework

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Architecture Decision |
| **Week** | 24 |

### Question

Present a framework for build vs buy decisions when adding capability to a microservices platform.

### Short Answer (30 seconds)

Score on strategic differentiation, team capacity, TCO (3-year), time-to-market, and exit risk. Buy commodity (auth, email, payments); build core domain differentiators.

### Detailed Answer (3–5 minutes)

**Decision matrix:**
| Factor | Build | Buy |
|--------|-------|-----|
| Competitive advantage | Core domain | Commodity |
| Team expertise | Strong | Weak |
| Time to market | Months OK | Days matter |
| Customization need | High | Standard fits |
| Compliance | Full control needed | Vendor certified |

**Examples:**
- **Buy:** SendGrid (email), Stripe (payments), Auth0 (identity)
- **Build:** Pricing engine, fraud rules, product catalog with domain logic

**Platform middle ground:** Buy vendor, wrap in internal ACL + anti-corruption layer — swap vendor without domain pollution.

**Architect:** Document ADR with 3-year TCO including integration maintenance, not just license fee.

### Follow-up Questions

1. **Open source vs SaaS? — OSS reduces license cost, increases ops burden — factor SRE headcount.**
2. **When regret buy? — Vendor roadmap misaligns — ACL enables migration.**

### Common Mistakes

- Build everything — NIH syndrome
- Buy core domain logic — lose differentiation

---

## Q039: Event Ordering Guarantees

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Messaging |
| **Week** | 21 |

### Question

How do you guarantee event ordering per customer in a distributed event system?

### Short Answer (30 seconds)

Partition messages by `customerId` — single consumer per partition preserves order. Use sequence numbers for cross-partition total order only when strictly required.

### Detailed Answer (3–5 minutes)

**Kafka / Event Hubs:**
```
Producer: partition key = customerId
Consumer: one consumer instance per partition
→ Order of events for customer A is preserved
```

**When global order needed (rare):** Single partition (limits throughput) or sequence number with ordered processing buffer.

**Out-of-order handling:** Consumers should be idempotent; use `sequenceNumber` to detect gaps and defer processing.

**Cloud:** Azure Event Hubs with partition key; Service Bus sessions (`SessionId = customerId`) for ordered delivery.

**Architect:** Order per aggregate, not per system — `orderId` partition for order events, `customerId` for customer profile events.

### Follow-up Questions

1. **FIFO queue vs partitioned log? — SQS FIFO limited throughput; partitioned log scales with partition count.**
2. **Clock-based ordering? — Never sort events by `DateTime.UtcNow` from different producers.**

### Common Mistakes

- Global ordering requirement on all events — throughput bottleneck
- Multiple consumers on same partition — order broken

---

## Q040: Multi-Tenant — Silo vs Pool

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Architecture |
| **Week** | 24 |

### Question

Compare silo and pool multi-tenancy models for microservices. When do you choose each?

### Short Answer (30 seconds)

Pool: shared infrastructure, `tenantId` column — cost-efficient, ops simple. Silo: dedicated DB/compute per tenant — isolation for compliance and noisy-neighbor protection. Hybrid for enterprise tier.

### Detailed Answer (3–5 minutes)

**Pool model:**
- One deployment, shared DB with `tenantId` discriminator
- Row-level security or application-level filter
- Cost: $ per tenant low; risk: data leak if filter bug

**Silo model:**
- Dedicated database or schema per tenant
- Dedicated App Service plan or namespace for large tenants
- Cost: high; isolation: strong (SOC2, HIPAA)

**Hybrid (common in SaaS):**
| Tier | Model |
|------|-------|
| Free/Pro | Pool |
| Enterprise | Silo |

**Architect:** Tenant context middleware injects `tenantId` from JWT; integration tests verify cross-tenant isolation. Never trust client-supplied tenant ID without auth.

### Follow-up Questions

1. **Bridge model? — Shared app, separate DB per tenant — middle ground.**
2. **Noisy neighbor? — Silo or rate limits per tenant in pool.**

### Common Mistakes

- Pool without row-level security tests
- Silo for all tenants — unsustainable unit economics

---

## Q041: Observability Maturity Model

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Observability |
| **Week** | 21 |

### Question

Describe observability maturity levels for a microservices platform. What should exist before scaling to 20+ services?

### Short Answer (30 seconds)

Level 1: centralized logs. Level 2: metrics + dashboards per service. Level 3: distributed tracing with SLOs. Level 4: proactive alerting, runbooks, error budgets. Don't extract service 10 without Level 2 minimum.

### Detailed Answer (3–5 minutes)

**Maturity stages:**
| Level | Capabilities |
|-------|-------------|
| 0 | SSH and grep |
| 1 | Structured logs → Log Analytics / ELK |
| 2 | RED/USE metrics, service dashboards |
| 3 | OpenTelemetry traces, correlation IDs |
| 4 | SLOs, error budgets, synthetic monitoring |
| 5 | AIOps anomaly detection, auto-remediation |

**Before 20+ services:**
- Every service exports logs, metrics, traces with `service.name`
- Golden signals dashboard per service
- On-call runbook linked in service catalog
- Alert routing — not email to entire company

**Architect:** Observability is not optional infrastructure — budget 10–15% of platform team capacity.

### Follow-up Questions

1. **RED vs USE? — RED (Rate, Errors, Duration) for services; USE (Utilization, Saturation, Errors) for resources.**
2. **Cardinality explosion? — Avoid high-cardinality labels (userId) in metrics.**

### Common Mistakes

- Scaling services before centralized logging exists
- Alerts with no runbook — on-call pages with no action

---

## Q042: Team Topology for Microservices

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Organization |
| **Week** | 23 |

### Question

How does team topology align with microservices boundaries per Team Topologies?

### Short Answer (30 seconds)

Stream-aligned teams own end-to-end business capabilities (one or few services). Platform team provides paved road. Enabling team coaches on DDD. Complexity team handles legacy ACL integrations.

### Detailed Answer (3–5 minutes)

**Team Topologies mapping:**
- **Stream-aligned** → Order team owns Order + Fulfillment services
- **Platform** → Internal developer platform (templates, CI/CD, observability)
- **Enabling** → Temporary DDD/event storming coaching
- **Complicated-subsystem** → Legacy ERP ACL team

**Conway's Law:** Architecture will mirror communication structure — design teams before drawing service boxes.

**Anti-pattern:** Feature team touches 8 services — no ownership, no on-call accountability.

**Architect:** Two-pizza team per stream; clear service catalog ownership in Backstage.

### Follow-up Questions

1. **One team per service? — Too granular — team owns a bounded context (1–3 services).**
2. **Shared on-call rotation across all services? — Stream team owns their services' pages.**

### Common Mistakes

- Organizing by technology layer (all DB teams)
- No platform team — every stream reinvents CI/CD

---

## Q043: Platform Engineering for Microservices

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Platform |
| **Week** | 22 |

### Question

What should an Internal Developer Platform include for .NET microservices teams?

### Short Answer (30 seconds)

Golden-path templates: .NET 8 API with health checks, OpenTelemetry, Polly resilience, EF migrations, GitHub Actions OIDC deploy, Bicep modules, and service catalog entry. Measure time-to-first-production-deploy.

### Detailed Answer (3–5 minutes)

**IDP components:**
1. **Templates** — `dotnet new microservice` scaffolds structure
2. **Pipelines** — reusable workflow: build, test, contract verify, deploy to AKS/App Service
3. **Observability** — App Insights wired, standard dashboards
4. **Secrets** — Key Vault integration, no secrets in repo
5. **Catalog** — Backstage with owner, runbook, SLO links

**Metrics:** Time-to-first-deploy < 1 day; developer satisfaction survey; % services on golden path.

**Architect:** Platform team owns the paved road; product teams can go off-road but assume ops burden. Encode security defaults (Managed Identity, mTLS option).

### Follow-up Questions

1. **Platform vs enablement? — Platform builds tools; enablement team coaches adoption temporarily.**
2. **Build vs buy IDP? — Backstage + custom templates is common; avoid over-building K8s abstractions early.**

### Common Mistakes

- Platform team approving every deploy — bottleneck
- Golden path so rigid teams can't ship

---

## Q044: Data Consistency Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Data |
| **Week** | 24 |

### Question

Compare strong consistency, eventual consistency, and read-your-writes patterns across microservices.

### Short Answer (30 seconds)

Strong consistency within one service/aggregate (ACID). Eventual consistency across services via sagas and events. Read-your-writes via session affinity, version tokens, or synchronous read-after-write to owning service.

### Detailed Answer (3–5 minutes)

**Pattern selection:**
| Use case | Pattern |
|----------|--------|
| Payment debit | Strong (single service TX) |
| Product catalog | Eventual (minutes OK) |
| User sees own order after submit | Read-your-writes |
| Cross-service balance | Saga + eventual |

**Read-your-writes techniques:**
- Route read to primary replica
- Return entity version in write response; client sends `If-None-Match`
- Short TTL cache keyed by user session
- Sticky sessions (fragile — prefer version token)

**Architect:** Document consistency level per integration in context map — interviewers want business-aware trade-offs, not "always strong."

### Follow-up Questions

1. **CAP during partition? — Choose availability with eventual consistency for catalog; CP for ledger.**
2. **CRDTs? — Conflict-free types for collaborative editing — niche in microservices.**

### Common Mistakes

- Strong consistency required everywhere — kills availability
- Eventual consistency without UX strategy for stale reads

---

## Q045: Service Discovery

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Infrastructure |
| **Week** | 21 |

### Question

How does service discovery work in Kubernetes vs traditional VM deployments?

### Short Answer (30 seconds)

K8s: DNS (`order-service.namespace.svc.cluster.local`) + kube-proxy load balances to healthy pods. VMs: consul/etcd registry or load balancer with health-checked backend pool. Client-side vs server-side discovery trade-offs.

### Detailed Answer (3–5 minutes)

**Kubernetes (server-side):**
- Service resource → ClusterIP → kube-proxy routes to ready endpoints
- Readiness probe controls endpoint list
- No client-side registry needed for internal calls

**VM / hybrid:**
- **Client-side:** Service queries Consul → gets instance list → load balances (Ribbon pattern)
- **Server-side:** ALB/App Gateway → static or dynamic backend pool

**.NET in K8s:**
```csharp
// HttpClient factory with K8s DNS
services.AddHttpClient("OrderService")
    .ConfigureHttpClient(c => c.BaseAddress = new Uri("http://order-service:8080/"));
```

**Architect:** Prefer platform-native discovery (K8s DNS) over custom registry unless multi-cluster or multi-cloud mesh required.

### Follow-up Questions

1. **Headless service? — DNS returns pod IPs directly — for StatefulSets.**
2. **Service mesh discovery? — Sidecar intercepts — transparent to app.**

### Common Mistakes

- Hardcoded IP addresses in service config
- Discovery without health check integration — routes to dead instances

---

## Q046: Configuration Drift

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Week** | 23 |

### Question

How do you detect and prevent configuration drift across 15 microservice environments?

### Short Answer (30 seconds)

GitOps for desired state, automated drift detection, immutable infrastructure, and config validation at deploy. Alert when runtime config differs from declared manifest.

### Detailed Answer (3–5 minutes)

**Drift sources:** Manual kubectl edit, portal hotfix, secret rotated without repo update, feature flag changed without ticket.

**Prevention:**
1. **GitOps** — Argo CD / Flux reconciles cluster to Git manifest
2. **IaC** — Bicep/Terraform for Azure resources; PR review for changes
3. **App config** — Azure App Configuration with audit log
4. **Immutable deploys** — new image + config bundle, not SSH patch

**Detection:**
- Argo CD `OutOfSync` alert
- Nightly config diff job: running vs Git
- Policy-as-code (OPA/Kyverno) rejects non-compliant deploys

**Architect:** Drift is a security risk — unauthorized config change = incident.

### Follow-up Questions

1. **Config vs secret drift? — Secrets rotate more often — automate sync from Key Vault.**
2. **Emergency break-glass? — Allow manual change with mandatory post-incident Git reconcile.**

### Common Mistakes

- Production config changed only in portal — Git stale
- No audit trail on configuration changes

---

## Q047: Zero-Downtime Deployment

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Week** | 22 |

### Question

What deployment strategies enable zero-downtime releases for stateful .NET microservices?

### Short Answer (30 seconds)

Rolling update with readiness probes, blue/green for instant cutover, canary for risk reduction. Schema changes use expand-contract. Drain connections on shutdown.

### Detailed Answer (3–5 minutes)

**Strategies:**
| Strategy | Downtime | Risk | Use when |
|----------|----------|------|----------|
| Rolling | None* | Medium | Default K8s |
| Blue/green | None | Low | DB migration cutover |
| Canary | None | Lowest | High-risk payment change |

**Rolling deploy requirements:**
- `preStop` hook drains in-flight requests (30s grace)
- Readiness only true when warmed up
- Backward-compatible API during roll

**Stateful concerns:**
- EF migrations run as init container or job before new pods serve traffic
- Message consumers: cooperative rebalance — finish in-flight before partition move

**Feature flags:** Dark deploy new logic; enable after pods healthy.

**Architect:** Define max unavailable (1) and max surge (1) for critical services.

### Follow-up Questions

1. **Database migration job ordering? — Migrate schema → deploy new code reading new column — never reverse.**
2. **IIS vs K8s? — App Service deployment slots = blue/green for PaaS.**

### Common Mistakes

- Breaking schema + code in same release
- No connection draining — in-flight requests killed on pod terminate

---

## Q048: Capstone Review — Month 6 Readiness

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Capstone |
| **Week** | 24 |

### Question

What should a Month 6 microservices capstone demonstrate to prove architect readiness?

### Short Answer (30 seconds)

Bounded context map, saga/outbox diagram for one workflow, 4+ weeks study ≥70%, independent deploy of 2+ services, observability dashboard, and ability to whiteboard strangler migration for legacy system.

### Detailed Answer (3–5 minutes)

**Capstone checklist:**
- [ ] Context map with 4+ bounded contexts and integration patterns
- [ ] One saga (orchestrated or choreographed) with compensation documented
- [ ] Outbox or inbox pattern implemented in code or detailed design
- [ ] Contract test between two services
- [ ] Distributed trace screenshot for multi-hop request
- [ ] ADR for one significant decision (DB choice, sync vs async)
- [ ] Verbal 2-minute microservices pitch with trade-offs

**Rubric:** Can explain when NOT to use microservices. Can design flash-sale inventory without oversell. Can contain cascading failure scenario.

**Architect:** Capstone is communication proof — diagrams + spoken defense, not just code.

### Follow-up Questions

1. **Portfolio structure? — 3 ADRs, 1 context map, 1 sequence diagram, 1 postmortem writeup.**
2. **Mock interview? — 45-min system design: decompose e-commerce monolith.**

### Common Mistakes

- Capstone that's only slides without trade-off discussion
- Cannot articulate downsides of microservices

---

## Q049: Production Readiness Checklist

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Operations |
| **Week** | 24 |

### Question

What belongs on a production readiness review before launching a new microservice?

### Short Answer (30 seconds)

SLOs defined, runbook written, on-call rotation assigned, load tested at 2× expected peak, security review (auth, secrets, OWASP), backup/restore tested, rollback verified, and dashboards/alerts configured.

### Detailed Answer (3–5 minutes)

**Production readiness gates:**
| Area | Requirement |
|------|-------------|
| Reliability | SLO, error budget, load test report |
| Observability | Logs, metrics, traces, dashboards |
| Security | Threat model, pen test or scan, secrets in Key Vault |
| Operations | Runbook, on-call, escalation path |
| Data | Backup RPO/RTO tested, migration plan |
| Resilience | Timeouts, circuit breakers, bulkheads configured |
| Compliance | PII handling, audit log, retention policy |

**Go/no-go meeting:** Service owner presents; platform SRE signs off.

**Architect:** PRR is not bureaucracy — it's how you avoid being paged on launch night for missing health checks.

### Follow-up Questions

1. **SRE engagement when? — At design phase, not week before launch.**
2. **Progressive rollout? — 1% → 10% → 50% → 100% with metric gates.**

### Common Mistakes

- Launch without load test
- No rollback tested — forward-only deploy hope

---

## Q050: Graduation Scenarios — Architect Interview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Capstone |
| **Week** | 24 |

### Question

Deliver a 2-minute architect pitch: why microservices, when to avoid them, and your top three lessons from this program.

### Short Answer (30 seconds)

Microservices trade organizational autonomy and independent deploy for operational complexity. Use when team scale, deployment pain, and domain clarity justify the cost. Avoid for small teams, unclear boundaries, or immature DevOps. Top lessons: start modular monolith, invest in observability first, database-per-service is non-negotiable.

### Detailed Answer (3–5 minutes)

**2-minute pitch structure:**
1. **Why:** Autonomous teams, scale independent components, technology fit per context (15 sec)
2. **When not:** <10 engineers, shared unclear domain, no CI/CD — modular monolith first (20 sec)
3. **Lessons:**
   - Observability before service #5
   - Sagas/outbox over distributed 2PC
   - Conway's Law — align teams to contexts (30 sec)
4. **Trade-off close:** "I choose microservices when deployment coupling hurts business velocity more than ops overhead hurts reliability" (15 sec)

**Graduation scenarios to practice:**
- Board asks why not stay on monolith — quantify deploy frequency and incident blast radius
- CTO wants 50 services in 6 months — push back with team topology and ops capacity
- Production double-charge incident — walk through idempotency fix calmly

**Architect:** Graduation is demonstrating judgment under ambiguity — not pattern name-dropping.

### Follow-up Questions

1. **Favorite pattern? — Pick one with war story — outbox after production dual-write incident.**
2. **What's next after graduation? — Platform engineering, multi-region, or AI service mesh — tie to career goal.**

### Common Mistakes

- Pitch that's only benefits — no trade-offs
- Cannot whiteboard a saga compensation flow

---

**Complete:** [Index](microservices-top-50-index.md)
