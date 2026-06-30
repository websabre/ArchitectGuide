# Week 32 — Fundamentals Interview Q&A

> Q001–Q030: Premium format (Week 1 quality).
> See also: [DevOps Top 50](../../../interview-prep/devops-top-50-index.md)

---


## Q001: Three Pillars of Observability

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Observability |
| **Frequency** | Very Common |

### Question

What are the three pillars of observability and how do they work together during incidents?

### Short Answer (30 seconds)

Logs (what), metrics (how much/fast), traces (where time went). Alert on metric → trace finds slow span → logs show exception. All linked by trace/correlation ID.

### Detailed Answer (3–5 minutes)

During checkout slowdown: metric alert on p99 → trace shows Payment API span 4.8s → log shows `PaymentTimeoutException` on correlation ID.

Architect mandate: every microservice exports all three via OpenTelemetry.

### Architecture Perspective

Observability is part of definition of done for every service.

### Follow-up Questions

1. Fourth pillar? — Profiling for CPU flame graphs.
2. Logs vs traces? — Complementary; traces show structure, logs add detail.

### Common Mistakes in Interviews

- Logs only, no metrics or traces
- String interpolation breaking structured query
- No correlation ID standard

---

## Q002: OpenTelemetry for .NET

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | OpenTelemetry |
| **Frequency** | Very Common |

### Question

How do you instrument ASP.NET Core 8 with OpenTelemetry?

### Short Answer (30 seconds)

Add OTel hosting extensions, enable ASP.NET Core/HttpClient/EF instrumentations, export to Azure Monitor or OTLP collector. Propagate W3C traceparent on all outbound calls.

### Detailed Answer (3–5 minutes)

Custom spans around payment processing. Service name matches deployment name. Version tag = container image tag for deploy correlation.

### Architecture Perspective

OTel is vendor-neutral — standardize on OTel, swap backends per environment.

### Follow-up Questions

1. Sampling? — 100% dev; tail-based or probabilistic prod keeping all errors.
2. Service Bus? — Inject trace context in message properties.

### Common Mistakes in Interviews

- Legacy App Insights SDK only for new services
- Broken trace propagation
- Missing EF Core instrumentation

---

## Q003: SLI SLO and Error Budget

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | SRE |
| **Frequency** | Very Common |

### Question

Define SLI, SLO, SLA, and error budget for an order API.

### Short Answer (30 seconds)

SLI: % successful requests. SLO: 99.9% availability (43 min/month budget). SLA: 99.95% with credits. Exhausted budget → freeze features, fix reliability.

### Detailed Answer (3–5 minutes)

Latency SLI: p99 < 300ms measured at load balancer.

Error budget policy: >50% budget → normal dev; <20% → reliability sprint; exhausted → exec escalation.

### Architecture Perspective

SLOs connect architecture to business risk with numbers.

### Follow-up Questions

1. 100% SLO? — Impossible and paralyzing.
2. Client vs server SLI? — User-facing synthetic + RUM beats server-only.

### Common Mistakes in Interviews

- Confusing SLO with SLA
- No error budget policy
- SLOs without measurement implementation

---

## Q004: RED vs USE Methods

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Monitoring |
| **Frequency** | Common |

### Question

Explain RED and USE monitoring methods.

### Short Answer (30 seconds)

RED (Rate, Errors, Duration) for request-driven services. USE (Utilization, Saturation, Errors) for resources like CPU, SQL DTU, Redis memory.

### Detailed Answer (3–5 minutes)

Order API → RED dashboard. SQL Server → USE dashboard (DTU utilization, connection saturation).

Alert on saturation before utilization hits 100% — thread pool starvation at 60% CPU.

### Architecture Perspective

Dashboard design reflects system thinking.

### Follow-up Questions

1. Google golden signals? — Latency, traffic, errors, saturation — overlaps RED+USE.
2. Service Bus? — USE on dead letter queue depth.

### Common Mistakes in Interviews

- CPU-only alerts missing saturation
- Wrong method for resource type
- No dashboards per component

---

## Q005: Structured Logging in .NET

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Logging |
| **Frequency** | Common |

### Question

Why use structured logging instead of string interpolation?

### Short Answer (30 seconds)

Named properties (`OrderId`, `CustomerId`) are queryable in Log Analytics. `$"Order {id}"` breaks field extraction and increases ingestion cost.

### Detailed Answer (3–5 minutes)

Wrap requests in correlation ID scope. Never log PII/passwords. Information for business events; Debug off in production.

### Architecture Perspective

Unstructured logs waste MTTR minutes during outages.

### Follow-up Questions

1. Serilog? — Rich sinks; built-in sufficient with App Insights exporter.
2. Log levels in prod? — Debug floods ingestion and cost.

### Common Mistakes in Interviews

- Interpolated strings in logs
- No correlation ID across services
- Logging PII/card numbers

---

## Q006: Alert Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Alerting |
| **Frequency** | Common |

### Question

How do you design alerts without causing alert fatigue?

### Short Answer (30 seconds)

Page on user-impacting symptoms (SLO burn, 5xx rate). Ticket for warnings. Every page alert needs runbook. Weekly alert review — delete noisy rules.

### Detailed Answer (3–5 minutes)

SLO multi-window burn rate: fast burn pages, slow burn tickets.

Anti-patterns: single failed health check, no runbook, 50 cascading alerts.

### Architecture Perspective

Alert design is on-call UX — bad alerts cause burnout and missed real incidents.

### Follow-up Questions

1. Who gets paged? — Service owner rotation, not entire platform team.
2. Flapping? — Require N consecutive failures before page.

### Common Mistakes in Interviews

- Alert on everything
- No page vs ticket distinction
- Alerts without runbook links

---

## Q007: Distributed Tracing Debug

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Tracing |
| **Frequency** | Common |

### Question

How do you use distributed tracing to debug a 5-second API response?

### Short Answer (30 seconds)

Find slow trace by duration, examine span waterfall, identify bottleneck span (Payment API, SQL), check logs on correlation ID.

### Detailed Answer (3–5 minutes)

Waterfall: checkout 5.2s → payment-api 4.8s → stripe.com 4.6s. Fix: circuit breaker, timeout tuning — not SQL index guesswork.

### Architecture Perspective

Tracing turns vague slowness into actionable service boundaries.

### Follow-up Questions

1. Broken traces? — Missing traceparent on HttpClient or Service Bus.
2. Regression detection? — Compare p99 before/after deploy.

### Common Mistakes in Interviews

- Adding cache without finding bottleneck
- grep logs across 15 services without traces
- No custom spans on critical paths

---

## Q008: PowerShell Azure Automation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Automation |
| **Frequency** | Occasional |

### Question

What Azure operations would you automate with PowerShell?

### Short Answer (30 seconds)

Cost reports by resource group, untagged resource audits, bulk diagnostic settings, incident scale-out/restart, certificate expiry reports.

### Detailed Answer (3–5 minutes)

Prefer Bash/Azure CLI on Linux CI agents; PowerShell for Windows-centric enterprise reporting and FinOps dashboards.

### Architecture Perspective

Automation scripts are operational runbooks — architects provide templates.

### Follow-up Questions

1. PowerShell in GitHub Actions? — Windows runners or Az CLI on ubuntu.
2. Idempotency? — Scripts safe to re-run.

### Common Mistakes in Interviews

- Manual portal clicks during incidents
- Non-idempotent scripts
- No documented runbooks

---

## Q009: Synthetic Monitoring

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Monitoring |
| **Frequency** | Common |

### Question

Why is synthetic monitoring critical for multi-region architectures?

### Short Answer (30 seconds)

Internal health checks in failed region show green while customers fail. Probes from multiple geographies detect user-facing outages — especially after failover.

### Detailed Answer (3–5 minutes)

Design: availability tests from US, EU, APAC every 60s on critical journeys (login, checkout). Alert when 2+ locations fail.

`/health` must check DB connectivity — not just process alive.

### Architecture Perspective

Validates user experience — internal metrics lie during partial failures.

### Follow-up Questions

1. Synthetic vs canary? — Synthetic is fixed probe traffic; canary is prod users to new version.
2. Post-failover? — Probes must follow traffic manager weights.

### Common Mistakes in Interviews

- Health check returns 200 without dependencies
- Single-region probes only
- No alert on synthetic failure

---

## Q010: Observability Cost Control

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | FinOps |
| **Frequency** | Occasional |

### Question

Application Insights costs grew 40% month-over-month. How do you optimize?

### Short Answer (30 seconds)

Trace sampling (keep 100% errors), reduce verbose logging in prod, daily cap alerts, drop unused custom metrics, archive old data to Storage.

### Detailed Answer (3–5 minutes)

Tail-based sampling at OTel collector — central control. Don't sample so aggressively you cannot debug incidents.

### Architecture Perspective

FinOps applies to observability — set standards in platform templates.

### Follow-up Questions

1. Collector filtering? — Drop health check traces before export.
2. Retention? — 30 days hot, archive cold.

### Common Mistakes in Interviews

- 100% trace sampling at high RPS
- No observability because too expensive
- Debug logging enabled in production

---




## Q011: Three Pillars Working Together

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Observability |
| **Frequency** | Very Common |

### Question

During a checkout slowdown incident, how do metrics, logs, and traces work together?

### Short Answer (30 seconds)

Metric alert on p99 latency → distributed trace identifies slow Payment API span → logs on correlation ID show `PaymentTimeoutException`. Each pillar answers different question.

### Detailed Answer (3–5 minutes)

**Workflow:**
1. **Metrics** — `checkout_latency_p99` breaches SLO → page on-call
2. **Traces** — filter traces > 3s, waterfall shows `payment-api` span 4.8s
3. **Logs** — query `correlationId == abc` → stack trace and request payload metadata

**Correlation:** W3C `traceparent` propagated to logs via `Activity.Current.TraceId`.

**Architect:** Mandate all three pillars in service scaffold — not optional App Insights checkbox.

### Architecture Perspective

Pillar integration is incident response pattern — not three disconnected tools.

### Follow-up Questions

1. **Fourth pillar profiling? — Continuous profiler for CPU — complements during perf incidents.**
2. **Single pane? — Azure Monitor links trace to logs — configure workspace integration.**

### Common Mistakes in Interviews

- Logs only shop — grep across 20 services during outage
- Metrics without traces — cannot localize bottleneck
- No correlation ID between logs and traces

---

## Q012: OpenTelemetry Collector Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | OpenTelemetry |
| **Frequency** | Very Common |

### Question

Design OpenTelemetry Collector deployment for .NET microservices on Azure.

### Short Answer (30 seconds)

Deploy collector as sidecar or centralized DaemonSet/Container App. Receivers (OTLP) → processors (batch, filter, tail sampling) → exporters (Azure Monitor, Prometheus).

### Detailed Answer (3–5 minutes)

**Pipeline:**
```
.NET App → OTLP gRPC → Collector → processors → Azure Monitor exporter
```

**Processors:**
- `batch` — reduce export chatter
- `attributes` — add `environment`, `region`
- `tail_sampling` — keep errors 100%, sample success 10%

**Architect:** Collector centralizes sampling and PII filtering — apps stay vendor-neutral.

### Architecture Perspective

Collector is observability control plane — architects own deployment topology.

### Follow-up Questions

1. **Agent vs collector? — Legacy App Insights agent vs OTel SDK + collector — migrate to OTel.**
2. **HA collector? — Multiple replicas behind load balancer for OTLP ingress.**

### Common Mistakes in Interviews

- Each service exports directly with different sampling rates
- No tail sampling — cost explosion
- PII filtered per service inconsistently

---

## Q013: Distributed Tracing Correlation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Tracing |
| **Frequency** | Very Common |

### Question

How do you propagate trace context across HTTP, Service Bus, and background jobs in .NET?

### Short Answer (30 seconds)

W3C Trace Context (`traceparent`, `tracestate`) on HTTP headers; inject into Service Bus message application properties; restore context in `IHostedService` from message.

### Detailed Answer (3–5 minutes)

**HTTP:** `Activity` auto-instrumented on `HttpClient`.

**Service Bus:**
```csharp
message.ApplicationProperties["traceparent"] = Activity.Current?.Id;
```
Consumer links child span to parent.

**Background job:** Start span from enqueued trace context — don't orphan jobs.

**Architect:** Broken propagation = broken waterfall — test in integration tests.

### Architecture Perspective

Trace propagation is cross-cutting architecture requirement for microservices.

### Follow-up Questions

1. **Baggage vs trace context? — Baggage propagates business metadata — use sparingly.**
2. **Legacy SOAP? — Custom correlation header mapping to Activity.**

### Common Mistakes in Interviews

- New trace per Service Bus message
- HttpClient without instrumentation
- Background job spans disconnected from HTTP request

---

## Q014: SLI Definition Examples

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | SRE |
| **Frequency** | Very Common |

### Question

Define three SLIs for a .NET order API with measurement points.

### Short Answer (30 seconds)

**Availability SLI:** `(successful requests / total requests)` measured at App Gateway — excludes 4xx client errors.

**Latency SLI:** `% requests < 300ms` at load balancer.

**Freshness SLI (async):** `% order confirmations within 60s of payment` — for queue-backed flow.

### Detailed Answer (3–5 minutes)

**Good SLI properties:**
- User-centric (not CPU)
- Measurable at boundary user experiences
- Stable definition over time

**Bad SLI:** CPU < 80% — not user-facing.

**Architect:** Document SLI definitions in SLO doc before building dashboards — prevents metric debates during incidents.

### Architecture Perspective

Concrete SLI examples prove SRE literacy beyond acronym definitions.

### Follow-up Questions

1. **Numerator/denominator? — Define explicitly — include or exclude 4xx.**
2. **Synthetic SLI? — Availability from probes complements server-side.**

### Common Mistakes in Interviews

- CPU utilization as primary SLI
- SLI measured inside service ignoring gateway timeouts
- Changing SLI definition monthly

---

## Q015: SLO Error Budget Policy Document

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | SRE |
| **Frequency** | Very Common |

### Question

What belongs in a written SLO error budget policy for engineering teams?

### Short Answer (30 seconds)

SLO targets, measurement window, budget calculation, actions at 50%/20%/0% remaining, escalation path, exception process for planned maintenance.

### Detailed Answer (3–5 minutes)

**Policy template:**
1. **SLO:** 99.9% availability monthly
2. **Budget:** 43.2 min downtime/month
3. **50% remaining:** normal development
4. **20% remaining:** reliability work prioritized in sprint
5. **0%:** feature freeze, exec notified
6. **Exclusions:** planned maintenance with comms (counts against budget transparently)

**Architect:** Policy signed by eng director and product — not SRE dictat.

### Architecture Perspective

Written policy makes error budgets enforceable — not theoretical.

### Follow-up Questions

1. **Multi-window burn? — Fast burn pages, slow burn tickets — add to policy.**
2. **SLO review cadence? — Quarterly — adjust targets based on user needs.**

### Common Mistakes in Interviews

- SLO in wiki never referenced
- No action defined when budget exhausted
- 100% availability target

---

## Q016: Alerting on User Symptoms

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Alerting |
| **Frequency** | Very Common |

### Question

Why alert on symptoms (SLO burn, 5xx rate) instead of causes (CPU, disk)?

### Short Answer (30 seconds)

Cause-based alerts fire before user impact (noisy) or after (late). Symptom alerts page when users suffer — CPU 90% may be fine if latency healthy.

### Detailed Answer (3–5 minutes)

**Symptom alerts:**
- SLO multi-window burn rate
- `5xx / total` > 1% for 5 min
- Synthetic checkout failure 2+ regions

**Cause alerts (ticket not page):**
- Disk 80% — scale before symptom
- Certificate expires in 30 days

**Architect:** Every page alert links to runbook answering 'what user impact?'

### Architecture Perspective

Symptom-based alerting is SRE best practice — reduces false pages.

### Follow-up Questions

1. **Saturation alerting? — USE method — page when saturation affects latency.**
2. **Composite alerts? — `(5xx elevated) AND (latency elevated)` reduce noise.**

### Common Mistakes in Interviews

- CPU > 80% pages on-call at 3am
- Alert on single failed health check
- No distinction page vs ticket

---

## Q017: Alert Fatigue Reduction Program

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Alerting |
| **Frequency** | Common |

### Question

Run a quarterly program to reduce alert fatigue — what steps?

### Short Answer (30 seconds)

Export all alerts fired last 90 days; classify: actionable, noisy, redundant; delete or downgrade; require runbook for every remaining page alert.

### Detailed Answer (3–5 minutes)

**Steps:**
1. **Inventory** — alert name, fire count, MTTA, was it actionable?
2. **Top 10 noisy** — fix or delete
3. **Deduplicate** — 15 alerts for same symptom → 1 SLO burn alert
4. **Runbook audit** — no runbook = downgrade to ticket
5. **Review meeting** — on-call rotation feedback

**Target:** < 2 pages per on-call shift per week for healthy system.

### Architecture Perspective

Alert hygiene is ongoing architecture responsibility — not one-time setup.

### Follow-up Questions

1. **Alert grouping? — Azure Monitor alert grouping reduces notification storm.**
2. **Flapping? — Require 3 consecutive breaches before page.**

### Common Mistakes in Interviews

- 50 alerts fire per incident — no grouping
- Alerts never reviewed after creation
- On-call burnout ignored

---

## Q018: Structured Logging with Serilog

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Logging |
| **Frequency** | Common |

### Question

Configure Serilog for structured logging in ASP.NET Core 8 with Log Analytics.

### Short Answer (30 seconds)

Serilog with `WriteTo.Console(new CompactJsonFormatter())` and Azure Analytics sink. Enrich with `CorrelationId`, `Environment`, `ServiceVersion`.

### Detailed Answer (3–5 minutes)

**Setup:**
```csharp
Log.Logger = new LoggerConfiguration()
  .Enrich.FromLogContext()
  .Enrich.WithProperty("Service", "order-api")
  .WriteTo.ApplicationInsights(telemetryConfig, TelemetryConverter.Traces)
  .CreateLogger();
```

**Query:** `traces | where customDimensions.OrderId == '12345'`

**Never:** `Log.Information($"Order {id} placed")` — use `Log.Information("Order placed {OrderId}", id)`.

### Architecture Perspective

Serilog structured patterns are .NET observability baseline.

### Follow-up Questions

1. **Serilog vs built-in? — Serilog richer sinks; built-in ILogger sufficient with App Insights exporter.**
2. **Log scopes? — `using (_logger.BeginScope(...))` for request context.**

### Common Mistakes in Interviews

- String interpolation in log messages
- PII in structured fields
- Debug level enabled in production

---

## Q019: Log Aggregation with Log Analytics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Logging |
| **Frequency** | Common |

### Question

Design log aggregation architecture for 15 .NET microservices in Azure Monitor.

### Short Answer (30 seconds)

All services export to single Log Analytics workspace per environment. Standard schema: `serviceName`, `correlationId`, `traceId`, `severity`. Retention 90 days hot; archive to Storage.

### Detailed Answer (3–5 minutes)

**Workspace strategy:**
- `law-contoso-prod` — all prod services
- Resource-specific tables or unified `AppTraces`/`AppRequests`

**Cross-service query:**
```kusto
traces
| where correlationId == "abc-123"
| order by timestamp asc
```

**Architect:** Workspace per env not per service — enables correlation; RBAC via table filters if needed.

### Architecture Perspective

Centralized log aggregation enables cross-service incident queries.

### Follow-up Questions

1. **Multiple workspaces per service? — Fragments correlation — avoid unless regulatory isolation.**
2. **Ingestion cost? — Sampling and log level discipline.**

### Common Mistakes in Interviews

- 15 separate workspaces — cannot correlate
- Unstructured logs in workspace
- No retention policy — unbounded cost

---

## Q020: Metrics Cardinality Explosion

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Metrics |
| **Frequency** | Common |

### Question

What causes metrics cardinality explosion and how do you prevent it?

### Short Answer (30 seconds)

High-cardinality labels (userId, orderId) on Prometheus/custom metrics explode time series count — ingestion cost and query slowdown. Use bounded labels only.

### Detailed Answer (3–5 minutes)

**Safe labels:** `service`, `environment`, `region`, `http_route` (templated `/orders/{id}`).

**Dangerous:** `customerId`, `sessionId`, `url` full path.

**Prevention:**
- Code review metric registration
- OTel collector drops high-cardinality attributes
- Use logs/traces for high-cardinality debugging

**Architect:** Platform lint rule banning `userId` in custom metrics.

### Architecture Perspective

Cardinality is observability FinOps — architects set labeling standards.

### Follow-up Questions

1. **Histogram cardinality? — Buckets multiply series — limit custom histograms.**
2. **Azure Monitor custom metrics? — Same rules — dimensions are cardinality.**

### Common Mistakes in Interviews

- userId as metric dimension
- Unbounded HTTP path label
- No review of custom metric registration

---

## Q021: RED Method for Microservices

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Monitoring |
| **Frequency** | Common |

### Question

Apply the RED method to design dashboards for a .NET payment API.

### Short Answer (30 seconds)

**Rate** — requests/sec by endpoint. **Errors** — 5xx rate, payment decline rate. **Duration** — p50/p95/p99 latency histogram.

### Detailed Answer (3–5 minutes)

**Dashboard panels:**
1. `sum(rate(http_requests_total[5m]))` by service
2. `sum(rate(http_requests_total{status=~"5.."}[5m])) / sum(rate(...))`
3. `histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))`

**Per dependency:** RED on outbound HttpClient calls to Stripe.

**Architect:** RED dashboard per service in golden path — auto-created from OTel export.

### Architecture Perspective

RED is request-driven service monitoring standard — know the three letters.

### Follow-up Questions

1. **RED vs golden signals? — Golden adds saturation — use USE for resources alongside RED.**
2. **gRPC RED? — Rate, gRPC status codes, duration from OTel grpc instrumentation.**

### Common Mistakes in Interviews

- CPU dashboard only for API service
- No error rate panel
- Duration as average only hiding p99 outliers

---

## Q022: USE Method for Infrastructure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Monitoring |
| **Frequency** | Common |

### Question

Apply USE method to monitor Azure SQL and Redis backing a .NET API.

### Short Answer (30 seconds)

**Utilization** — SQL DTU %, Redis memory %. **Saturation** — SQL connection pool waits, Redis evicted keys. **Errors** — SQL deadlocks, Redis connection timeouts.

### Detailed Answer (3–5 minutes)

**SQL USE:**
- Utilization: DTU percentage
- Saturation: `connection_pool_pending` metric
- Errors: deadlock count, failed connections

**Redis USE:**
- Utilization: `used_memory / maxmemory`
- Saturation: evicted_keys rate
- Errors: rejected_connections

**Alert:** Saturation before utilization hits 100% — pool exhaustion at 70% DTU.

### Architecture Perspective

USE complements RED — resources vs requests.

### Follow-up Questions

1. **App Service Plan USE? — CPU utilization, HTTP queue length (saturation), 5xx (errors).**
2. **Service Bus? — USE on active messages (saturation), dead letter count (errors).**

### Common Mistakes in Interviews

- Only SQL CPU alert
- Ignore connection pool saturation
- Redis memory 100% before alert

---

## Q023: Observability Dashboard Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Monitoring |
| **Frequency** | Common |

### Question

Design an executive and engineering dashboard hierarchy for e-commerce platform.

### Short Answer (30 seconds)

L1 executive: revenue-impacting SLOs, error budget remaining. L2 on-call: RED per service, dependency health. L3 deep-dive: USE per resource, trace explorer link.

### Detailed Answer (3–5 minutes)

**Hierarchy:**
- **Executive (1 screen):** Checkout SLO, orders/min, budget burn
- **Service owner:** Order API RED, recent deploys, top errors
- **Incident:** Trace search, log query templates, runbook links

**Principles:** < 10 panels per dashboard; consistent color thresholds; annotation for deploys.

### Architecture Perspective

Dashboard hierarchy serves different audiences — architects design both.

### Follow-up Questions

1. **Deploy annotations? — Vertical line on dashboard at deploy time — correlates regressions.**
2. **Dashboard sprawl? — Catalog in Backstage — discoverable golden dashboards.**

### Common Mistakes in Interviews

- Single 40-panel dashboard
- No SLO on executive view
- Different threshold colors per team

---

## Q024: On-Call Runbooks Linked to Alerts

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Operations |
| **Frequency** | Common |

### Question

What makes an effective on-call runbook linked from Azure Monitor alerts?

### Short Answer (30 seconds)

Runbook: symptom description, impact, diagnostic steps (KQL queries), remediation commands, escalation criteria, rollback procedure — tested quarterly.

### Detailed Answer (3–5 minutes)

**Template sections:**
1. **Alert meaning** — what user impact
2. **Quick checks** — 3 KQL queries copy-paste ready
3. **Fix steps** — slot swap command, scale SQL tier
4. **Escalate if** — unresolved 15 min → page SRE lead
5. **Post-incident** — postmortem link

**Storage:** ADO Wiki or Backstage — URL in alert description field.

### Architecture Perspective

Runbooks reduce MTTR — DORA metric — architects provide templates.

### Follow-up Questions

1. **Executable runbooks? — Azure Automation hybrid runbook linked from alert.**
2. **Runbook drill? — Quarterly game day executes runbook blindly.**

### Common Mistakes in Interviews

- Alert with no runbook link
- Runbook outdated after architecture change
- Runbook only says 'call expert'

---

## Q025: Synthetic Monitoring Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Monitoring |
| **Frequency** | Common |

### Question

Design synthetic availability tests for multi-region .NET e-commerce.

### Short Answer (30 seconds)

Availability tests from 3+ regions every 60s on critical paths: login, search, add-to-cart, checkout. Alert when 2+ locations fail consecutive 3 runs.

### Detailed Answer (3–5 minutes)

**Configuration:**
- Application Insights web tests or Playwright synthetic
- `/health` insufficient — test real user journey
- Validate SSL cert expiry in test

**Post-deploy:** Synthetic runs as smoke gate — failure blocks promotion.

**Architect:** Synthetic measures user-visible availability — complements server-side metrics.

### Architecture Perspective

Synthetic catches regional DNS and CDN failures server metrics miss.

### Follow-up Questions

1. **Private endpoints? — Synthetic from inside VNet or use Azure Functions ping.**
2. **Maintenance window? — Suppress alerts with scheduled downtime.**

### Common Mistakes in Interviews

- Single-region synthetic only
- Health endpoint returns 200 without DB check
- No synthetic on checkout path

---

## Q026: Real User Monitoring RUM

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Monitoring |
| **Frequency** | Common |

### Question

How does RUM complement synthetic monitoring for a Blazor/React frontend?

### Short Answer (30 seconds)

RUM captures actual user browser performance: Core Web Vitals (LCP, INP, CLS), JS errors, API latency from client perspective. Synthetic cannot replicate all devices and networks.

### Detailed Answer (3–5 minutes)

**Implementation:**
- Application Insights JavaScript SDK or OTel browser
- Track page views, AJAX failures, client-side exceptions
- Segment by geography, browser, device

**Use cases:**
- Synthetic green but RUM shows India users 8s LCP → CDN issue
- JS error spike after deploy → bad frontend bundle

**Architect:** SLO on client-side latency for critical flows — not just server p99.

### Architecture Perspective

RUM is user-ground-truth — server metrics lie about client experience.

### Follow-up Questions

1. **PII in RUM? — Hash user IDs; GDPR consent for tracking.**
2. **Blazor WASM? — Client-side error tracking essential — exceptions silent to server.**

### Common Mistakes in Interviews

- Server-only monitoring for SPA
- No Core Web Vitals tracking
- RUM sample rate 0% to save cost

---

## Q027: PowerShell Azure Observability Automation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Automation |
| **Frequency** | Occasional |

### Question

Automate observability hygiene with PowerShell for Azure estate.

### Short Answer (30 seconds)

Scripts: enable diagnostic settings on all App Services, audit missing App Insights connection, export cost by resource group, report certificates expiring < 30 days.

### Detailed Answer (3–5 minutes)

**Example:**
```powershell
Get-AzWebApp | ForEach-Object {
  if (-not $_.SiteConfig.AppSettings['APPLICATIONINSIGHTS_CONNECTION_STRING']) {
    Write-Warning "Missing App Insights: $($_.Name)"
  }
}
```

**Schedule:** Azure Automation runbook weekly; output to Log Analytics custom table.

**Architect:** Compliance automation — no App Insights = no deploy approval.

### Architecture Perspective

PowerShell automation scales observability governance across subscriptions.

### Follow-up Questions

1. **Az CLI vs PowerShell? — PowerShell for Windows-centric ops reporting; CLI on Linux agents.**
2. **What not to automate? — Alert threshold tuning — requires human judgment initially.**

### Common Mistakes in Interviews

- Manual portal audit of 200 App Services
- Non-idempotent diagnostic enable script
- No scheduled execution

---

## Q028: Hybrid Runbook Automation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Automation |
| **Frequency** | Common |

### Question

Design hybrid runbook automation for incident response across Azure and on-prem.

### Short Answer (30 seconds)

Azure Automation Hybrid Runbook Worker on-prem executes AD DNS flush, load balancer drain, while Azure runbooks scale App Service and swap slots — orchestrated from single alert.

### Detailed Answer (3–5 minutes)

**Architecture:**
- Alert fires → Logic App or Automation webhook
- Parallel jobs: cloud scale-out + on-prem connection pool reset
- Results logged to Log Analytics custom log
- Failure path escalates to on-call

**Security:** Hybrid worker uses Managed Identity; least privilege on-prem service account.

### Architecture Perspective

Hybrid automation reflects real enterprise — not 100% cloud.

### Follow-up Questions

1. **Runbook vs GitHub Action? — Runbook for incident response; Action for deploy pipeline.**
2. **Testing? — Monthly dry-run in staging hybrid worker.**

### Common Mistakes in Interviews

- Manual on-prem steps during every Sev1
- Hybrid worker with domain admin — overprivileged
- Automation with no failure notification

---

## Q029: Observability Cost Control Tactics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

Application Insights bill grew 60% after OTel rollout. Optimization plan?

### Short Answer (30 seconds)

Implement tail-based sampling at collector (100% errors, 10% success), drop health check traces, reduce verbose logging, set daily cap alert, review custom metric cardinality.

### Detailed Answer (3–5 minutes)

**Tactics ranked:**
1. Tail sampling at OTel collector
2. Log level Information in prod (not Debug)
3. Filter `/health` traces before export
4. Drop duplicate IIS logs if App Insights captures requests
5. 30-day retention hot; archive older to Storage

**Governance:** Platform sets default sampling in scaffold — teams opt-in to higher sampling with cost approval.

### Architecture Perspective

Observability FinOps is architect responsibility as telemetry grows.

### Follow-up Questions

1. **Daily cap? — Safety net only — not primary cost control.**
2. **Sampling too aggressive? — Cannot debug — keep 100% error traces.**

### Common Mistakes in Interviews

- 100% trace sampling at 10K RPS
- Disable observability to cut costs
- No cost alert on Log Analytics workspace

---

## Q030: Production Debugging Workflow

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Operations |
| **Frequency** | Very Common |

### Question

Describe your systematic production debugging workflow for intermittent 5xx errors.

### Short Answer (30 seconds)

1) Check SLO dashboard and recent deploys. 2) Query 5xx rate by endpoint. 3) Find exemplar trace. 4) Correlate logs on traceId. 5) Reproduce in staging with feature flag. 6) Fix with test, canary deploy.

### Detailed Answer (3–5 minutes)

**KQL starting point:**
```kusto
requests
| where timestamp > ago(1h) and resultCode startswith "5"
| summarize count() by operation_Name, resultCode
| order by count_ desc
```

Then: `join` to `exceptions` on `operation_Id`.

**Avoid:** Random log grep without hypothesis. **Do:** Time-box investigation; escalate if > 30 min without theory.

### Architecture Perspective

Structured debugging workflow demonstrates senior operational maturity.

### Follow-up Questions

1. **Live debugging prod? — Last resort — use snapshot debugger or dump analysis.**
2. **Chaos reproduction? — Replay production trace payload in staging.**

### Common Mistakes in Interviews

- Restart service without investigation
- Debug logging enabled in prod as first step
- No deploy correlation when errors started

---
