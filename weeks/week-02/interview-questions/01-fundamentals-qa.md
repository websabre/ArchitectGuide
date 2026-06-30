# Week 02 — Fundamentals Interview Q&A

> Q001–Q030: Premium format (Week 1 quality).
> See also: [Interview prep hub](../../../interview-prep/README.md)

---


## Q001: CLR and Managed Runtime

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | .NET Runtime |
| **Frequency** | Very Common |

### Question

What is the CLR's role in a .NET architecture?

### Short Answer (30 seconds)

CLR loads assemblies, JIT-compiles IL to native code, manages GC, enforces type safety, handles exceptions. Architects care about GC behavior, assembly loading, and runtime version pinning.

### Detailed Answer (3–5 minutes)

**Hosting:** .NET 8 unified runtime — LTS for production APIs.

**Architect decisions:** Pin runtime in container images; test GC settings for high-RPS services; understand assembly load contexts for plugin architectures.

**Production:** `DOTNET_gcServer=1` default on ASP.NET — verify workstation GC not forced.

### Architecture Perspective

Runtime knowledge separates senior .NET architects.

### Follow-up Questions

1. **ReadyToRun vs JIT? — Faster startup; larger binaries — containers benefit.**
2. **Native AOT? — No JIT; constraints on reflection — microservices edge cases.**

### Common Mistakes in Interviews

- Mixing .NET Framework and .NET 8 without boundary
- Ignore runtime patch cadence in LTS planning
- Plugin load without AssemblyLoadContext isolation

---

## Q002: Hosting Models Compared

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Hosting |
| **Frequency** | Very Common |

### Question

Compare Kestrel+IIS, Kestrel-only, and container hosting for .NET APIs.

### Short Answer (30 seconds)

Kestrel is the actual server. IIS acts as reverse proxy on Windows. Containers: Kestrel behind ingress/ALB — preferred for cloud-native.

### Detailed Answer (3–5 minutes)

**Cloud default:** Linux container + Kestrel + Kubernetes/App Service/ECS.

**IIS:** Legacy Windows deployments, Windows Auth integration.

**Architect:** Kestrel at edge only behind reverse proxy in production — not exposed directly without hardening.

### Architecture Perspective

Hosting choice affects deploy pipeline and scaling.

### Follow-up Questions

1. **YARP reverse proxy? — Replace IIS ARR for .NET-native proxy.**
2. **HTTP.sys vs Kestrel? — HTTP.sys Windows-specific niche.**

### Common Mistakes in Interviews

- Expose Kestrel directly to internet without proxy
- Windows containers without cost analysis
- IIS and Kestrel misconfigured request limits

---

## Q003: Dependency Injection Lifetimes

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DI |
| **Frequency** | Very Common |

### Question

Explain Singleton, Scoped, Transient — and the captive dependency bug.

### Short Answer (30 seconds)

Singleton: one instance app lifetime. Scoped: per request/scope. Transient: new each resolve. Never inject Scoped into Singleton.

### Detailed Answer (3–5 minutes)

**Captive dependency:** `Singleton<Cache>` holding `Scoped<DbContext>` — DbContext never disposed per request.

**Fix:** Make cache Scoped, or use `IServiceScopeFactory` in singleton.

**Architect:** Document lifetime rules in coding standards; Roslyn analyzer or review checklist.

### Architecture Perspective

DI lifetime bugs cause production data corruption.

### Follow-up Questions

1. **ValidateOnBuild / ValidateScopes? — Enable in Development to catch early.**
2. **Keyed services .NET 8? — Multiple implementations same interface.**

### Common Mistakes in Interviews

- Singleton wrapping DbContext
- Transient for heavy objects in tight loop
- No scope in background service

---

## Q004: Configuration and Options Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Configuration |
| **Frequency** | Common |

### Question

How structure configuration in 12-factor .NET apps?

### Short Answer (30 seconds)

Hierarchy: appsettings.json → environment override → environment variables → Key Vault/secrets. `IOptions<T>` with validation at startup.

### Detailed Answer (3–5 minutes)

```csharp
services.AddOptions<PaymentOptions>()
    .BindConfiguration("Payment")
    .ValidateDataAnnotations()
    .ValidateOnStart();
```

**Architect:** Fail fast on misconfiguration; no secret files in repo; reload carefully for non-secret options only.

### Architecture Perspective

Configuration errors should crash at startup not runtime.

### Follow-up Questions

1. **IOptions vs IOptionsSnapshot vs IOptionsMonitor? — Scoped vs singleton reload needs.**
2. **Azure App Configuration? — Feature flags + centralized config.**

### Common Mistakes in Interviews

- Secrets in appsettings.Production.json committed
- No validation on connection strings
- Hot reload secrets unsafely

---

## Q005: Minimal APIs vs Controllers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | API Design |
| **Frequency** | Common |

### Question

When Minimal APIs vs MVC Controllers in enterprise?

### Short Answer (30 seconds)

Minimal APIs: microservices, simple endpoints, AOT-friendly. Controllers: complex conventions, filters, large teams familiar with MVC patterns.

### Detailed Answer (3–5 minutes)

**Enterprise:** Controllers still common in large codebases — consistency matters.

**Minimal:** Gateway BFFs, internal tools, serverless functions style.

**Architect:** Pick per service; don't mix arbitrarily within one bounded context.

### Architecture Perspective

API style is team consistency decision.

### Follow-up Questions

1. **Endpoint filters vs action filters? — Minimal API has endpoint filters .NET 7+.**
2. **OpenAPI generation both? — Swashbuckle works with both.**

### Common Mistakes in Interviews

- Minimal APIs everywhere without structure
- Controllers for 2-line health check only
- No versioning strategy either style

---

## Q006: gRPC vs REST

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | API Design |
| **Frequency** | Common |

### Question

When gRPC vs REST for internal service communication?

### Short Answer (30 seconds)

gRPC: internal east-west, high performance, streaming, contract-first protobuf. REST: public APIs, browser clients, human debugging with curl.

### Detailed Answer (3–5 minutes)

**.NET:** First-class gRPC with HTTP/2. Needs load balancer HTTP/2 support.

**Architect:** REST/JSON at edge (BFF); gRPC inside mesh between services.

**Tooling:** Contract versioning critical — backward compatible field adds.

### Architecture Perspective

Protocol choice affects gateway and observability.

### Follow-up Questions

1. **gRPC-Web? — Browser clients through proxy.**
2. **Json transcoding? — gRPC exposed as REST for transition.**

### Common Mistakes in Interviews

- gRPC public without gateway hardening
- Breaking proto changes without versioning
- REST between every internal hop at scale

---

## Q007: .NET Versioning and LTS Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Strategy |
| **Frequency** | Common |

### Question

Enterprise policy for .NET version adoption?

### Short Answer (30 seconds)

Adopt LTS (even years) for production within 6 months of release. STS for tooling only. Pin SDK in global.json; container base images on LTS.

### Detailed Answer (3–5 minutes)

**.NET 8 LTS** until Nov 2026 — standard for new services.

**Architect:** Central template repo; automated Dependabot for patch; major upgrade wave planned quarterly.

### Architecture Perspective

Version strategy prevents security and support debt.

### Follow-up Questions

1. **.NET Framework 4.8 extended support? — Legacy isolation plan required.**
2. **Central Package Management? — Consistent versions across solution.**

### Common Mistakes in Interviews

- STS in production without upgrade plan
- Mixed .NET versions uncontrolled per repo
- No global.json — SDK drift in CI

---

## Q008: Assembly Versioning and Breaking Changes

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Packaging |
| **Frequency** | Occasional |

### Question

SemVer for internal NuGet packages — architect rules?

### Short Answer (30 seconds)

Major: breaking API. Minor: backward compatible features. Patch: fixes. Consumers pin major; CI detects breaking changes.

### Detailed Answer (3–5 minutes)

**Architect:**
- API compatibility checks (Microsoft.CodeAnalysis.PublicApiAnalyzers)
- Single internal feed
- Document deprecation cycle (2 minors before remove)

**Avoid:** Shared kernel NuGet becoming god package.

### Architecture Perspective

Package graph affects build and deploy coupling.

### Follow-up Questions

1. **Source linking vs NuGet for shared code? — Prefer project reference in monorepo.**
2. **MinVer vs Nerdbank.GitVersioning? — Automate semver from git.**

### Common Mistakes in Interviews

- Breaking change without major bump
- Shared library with domain logic for all teams
- No deprecation notices

---

## Q009: Health Checks Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Observability |
| **Frequency** | Common |

### Question

Design health endpoints for Kubernetes/App Service?

### Short Answer (30 seconds)

Liveness: process up. Readiness: can serve traffic (DB reachable). Startup: slow initialization. Don't include external deps in liveness.

### Detailed Answer (3–5 minutes)

```csharp
builder.Services.AddHealthChecks()
    .AddSqlServer(conn)
    .AddRedis(redis);
```

**Architect:** Readiness fails remove from load balancer; liveness fail restarts pod — wrong check causes restart storm.

### Architecture Perspective

Health check design prevents cascading failures.

### Follow-up Questions

1. **Health Checks UI? — Dev only — not expose prod details publicly.**
2. **Tags for checks? — `ready` vs `live` endpoints separate.**

### Common Mistakes in Interviews

- HTTP call to payment provider in liveness
- Single /health does everything
- Detailed exception stack in health response

---

## Q010: Worker Services vs Web Apps

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Hosting |
| **Frequency** | Common |

### Question

When `Worker Service` template vs ASP.NET Core for background work?

### Short Answer (30 seconds)

Worker Service: queue consumers, scheduled jobs, long-running hosts without HTTP. Web + hosted service: light background in same process as API — caution scaling.

### Detailed Answer (3–5 minutes)

**Architect:** Separate worker deployment when CPU/memory profile differs from API — independent scale.

**Patterns:** Generic Host, `BackgroundService`, cancellation on shutdown.

**Avoid:** Heavy processing in API process — competes with request threads.

### Architecture Perspective

Process boundary is scaling boundary.

### Follow-up Questions

1. **IHostedService vs Worker template? — Worker is template with DI defaults.**
2. **Azure WebJobs vs separate Worker? — WebJobs coupled to App Service.**

### Common Mistakes in Interviews

- Scale API replicas to process queue backlog
- No graceful shutdown on worker
- Ignore duplicate message processing

---

## Q011: Server GC vs Workstation GC

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | GC |
| **Frequency** | Common |

### Question

When configure Server GC vs Workstation GC for .NET APIs?

### Short Answer (30 seconds)

Server GC: high-throughput multi-core servers (default ASP.NET). Workstation GC: lower latency, fewer cores — client apps, some consoles.

### Detailed Answer (3–5 minutes)

**ASP.NET Core on Linux containers:** Server GC default — optimize throughput.

**When Workstation:** Interactive apps, Unity, scenarios prioritizing pause latency over total throughput.

**Architect:** Measure `% Time in GC` and P99 latency before tuning. `DOTNET_gcServer` and `DOTNET_GCRetainVM` env vars for containers.

### Architecture Perspective

GC mode affects latency SLOs at scale.

### Follow-up Questions

1. **DATAS GC? — Dynamic adaptation — .NET 9+ options — evaluate per workload.**
2. **GC in containers limits? — Set memory limits; GC respects cgroup.**

### Common Mistakes in Interviews

- Workstation GC on 16-core API server
- GC.Collect() in production code
- No GC metrics in dashboards

---

## Q012: Thread Pool Starvation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Async |
| **Frequency** | Very Common |

### Question

Symptoms and fixes for thread pool starvation in ASP.NET Core?

### Short Answer (30 seconds)

Symptoms: slow responses, Kestrel queue growth, `ThreadPool starvation` events. Causes: sync-over-async, blocking I/O, long-running tasks on thread pool.

### Detailed Answer (3–5 minutes)

**Detect:** `dotnet-counters` ThreadPool queue length, App Insights dependency duration spikes.

**Fix:** async all the way, `Task.Run` only for CPU offload with limits, dedicated worker for long jobs.

**Architect:** Ban `.Wait()`/`.Result` in web projects via analyzer.

### Architecture Perspective

Thread pool is shared resource — architects protect it.

### Follow-up Questions

1. **Min threads configuration? — Last resort — find root cause first.**
2. **IOCompletionPort threads? — Separate from worker threads — know distinction.**

### Common Mistakes in Interviews

- sync-over-async in library used by API
- Blocking HttpClient.GetStringAsync().Result
- Ignore ThreadPool starvation warnings

---

## Q013: HttpClientFactory Deep Dive

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | HTTP |
| **Frequency** | Very Common |

### Question

Why `IHttpClientFactory` over static or injected HttpClient?

### Short Answer (30 seconds)

Factory manages handler lifetime — avoids socket exhaustion from disposing HttpClient wrong. Named/typed clients centralize config.

### Detailed Answer (3–5 minutes)

**Socket exhaustion:** `new HttpClient()` per request or singleton with infinite DNS cache — both fail at scale.

**Pattern:**
```csharp
services.AddHttpClient<IPaymentClient, PaymentClient>(c =>
    c.BaseAddress = new Uri(...));
```

**Architect:** Polly handlers on factory pipeline; standard timeout and retry policy.

### Architecture Perspective

HttpClient misuse is classic production outage cause.

### Follow-up Questions

1. **SocketsHttpHandler PooledConnectionLifetime? — Rotate connections for DNS.**
2. **Primary HttpMessageHandler? — Test with mock handler.**

### Common Mistakes in Interviews

- new HttpClient() per request
- Static HttpClient never refreshed DNS
- No timeout on outbound calls

---

## Q014: Polly Resilience Policies

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Resilience |
| **Frequency** | Common |

### Question

Design Polly policies for payment gateway HttpClient?

### Short Answer (30 seconds)

Retry (transient 5xx/408), circuit breaker (cascade prevention), timeout (end-to-end bound), bulkhead (isolate dependency).

### Detailed Answer (3–5 minutes)

**Order matters:** timeout outermost or innermost depending on semantics — document choice.

**Architect:** Retry only idempotent operations or with idempotency key. Circuit breaker opens → fail fast → half-open probe.

**.NET 8+:** `Microsoft.Extensions.Resilience` standardized pipelines.

### Architecture Perspective

Resilience policies are architect-level contracts.

### Follow-up Questions

1. **Jitter in retry? — Prevent thundering herd on recovery.**
2. **Fallback policy? — Return cached quote when pricing API down.**

### Common Mistakes in Interviews

- Infinite retry on POST payment
- Circuit breaker never half-opens
- Same policy all dependencies

---

## Q015: OpenTelemetry in .NET

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Observability |
| **Frequency** | Common |

### Question

Instrument .NET microservice with OpenTelemetry?

### Short Answer (30 seconds)

Add OTel SDK: traces (AspNetCore, HttpClient, EF), metrics (runtime, custom counters), logs correlation. Export to Azure Monitor / Jaeger / Prometheus.

### Detailed Answer (3–5 minutes)

**Architect standard:** W3C trace context propagation across services. ActivitySource for custom spans.

**Sampling:** Head-based in high traffic — adjust sample rate for cost.

**Avoid:** Vendor lock-in proprietary agents only.

### Architecture Perspective

OTel is architect's portability play for observability.

### Follow-up Questions

1. **Baggage vs tags? — Baggage propagates context — use sparingly.**
2. **OTel logs bridge? — Correlate logs to traceId.**

### Common Mistakes in Interviews

- No distributed tracing across services
- 100% trace sampling at 50K RPS
- Custom metrics without SLO mapping

---

## Q016: Serilog Structured Logging

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Observability |
| **Frequency** | Common |

### Question

Structured logging standards for enterprise .NET?

### Short Answer (30 seconds)

`LogInformation("Order {OrderId} placed", orderId)` — searchable properties not string concat.

### Detailed Answer (3–5 minutes)

**Architect mandates:** CorrelationId enricher, log levels per namespace, JSON to stdout in containers, PII redaction middleware.

**Sinks:** Console for K8s, Application Insights sink, Seq for dev.

**Anti-pattern:** `LogInformation($"Order {id}")` — loses structured property.

### Architecture Perspective

Logs are production debugging backbone.

### Follow-up Questions

1. **LogContext.PushProperty? — Scoped properties in request.**
2. **Sensitive data masking? — Custom destructuring policies.**

### Common Mistakes in Interviews

- String concat logging only
- Debug logs in production always on
- Log PII card numbers

---

## Q017: EF Core DbContext Pooling

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | EF Core |
| **Frequency** | Common |

### Question

When use `AddDbContextPool` vs `AddDbContext`?

### Short Answer (30 seconds)

Pooling: high-throughput read-heavy APIs — reuses context instances. Non-pooling: contexts with heavy state or non-standard lifetime.

### Detailed Answer (3–5 minutes)

**Caveat:** Reset state on return to pool — don't stash request data on context fields.

**Architect:** Pool size default 1024 — validate against connection pool limits.

**Measure:** Benchmark before/after on hot read endpoints.

### Architecture Perspective

Pooling is performance tool with constraints.

### Follow-up Questions

1. **DbContext factory pattern? — Blazor and background jobs.**
2. **Multiple DbContext types pooled? — Each registered separately.**

### Common Mistakes in Interviews

- Stateful fields on pooled DbContext
- Pool size × instances > SQL max connections
- Pooling without understanding reset

---

## Q018: EF Core Interceptors

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | EF Core |
| **Frequency** | Occasional |

### Question

Use cases for EF Core interceptors?

### Short Answer (30 seconds)

Auditing (CreatedBy, UpdatedAt), soft delete global filter, slow query logging, multi-tenant connection routing.

### Detailed Answer (3–5 minutes)

**Architect:** Cross-cutting data concerns in interceptors — not copy-paste in every repository.

**Example:** `SaveChangesInterceptor` sets audit fields from `IHttpContextAccessor`.

**Test:** Interceptors covered in integration tests.

### Architecture Perspective

Interceptors centralize data policies.

### Follow-up Questions

1. **IDbConnectionInterceptor? — Connection-level logging.**
2. **Query tagging interceptor? — Tag SQL with request ID.**

### Common Mistakes in Interviews

- Audit logic duplicated per entity
- Interceptor throws swallows root error
- No test coverage on interceptors

---

## Q019: Minimal API Endpoint Filters

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | ASP.NET |
| **Frequency** | Common |

### Question

Endpoint filters vs middleware — when which?

### Short Answer (30 seconds)

Middleware: cross-cutting pipeline order (auth, exception). Endpoint filters: per-route or per-group validation, logging — closer to handler.

### Detailed Answer (3–5 minutes)

**Architect:** Validation filter on command endpoints; middleware for correlation ID and ProblemDetails.

**.NET 7+:** `IEndpointFilter` chain like middleware mini-pipeline.

### Architecture Perspective

Right abstraction layer reduces duplication.

### Follow-up Questions

1. **Filter vs action filter MVC? — Parallel concepts different stacks.**
2. **Antiforgery on minimal APIs? — Form posts need tokens.**

### Common Mistakes in Interviews

- Duplicate validation filter and middleware
- Business logic in endpoint filter
- No filter ordering documentation

---

## Q020: Rate Limiting Middleware

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | ASP.NET |
| **Frequency** | Common |

### Question

Implement rate limiting for public .NET API?

### Short Answer (30 seconds)

.NET 7+ `AddRateLimiter` — fixed window, sliding window, token bucket, concurrency limiter.

### Detailed Answer (3–5 minutes)

**Architect:** Per-API-key or per-IP partitioning. Return 429 with `Retry-After`. Gateway-level (APIM) + app-level defense in depth.

**Distributed:** Redis-backed limiter for multi-instance consistency.

### Architecture Perspective

Rate limiting protects availability and cost.

### Follow-up Questions

1. **Global vs per-endpoint limits? — Stricter on expensive endpoints.**
2. **Rate limit bypass for internal callers? — IP allowlist or mTLS.**

### Common Mistakes in Interviews

- No rate limit on login endpoint
- In-memory limiter only multi-instance
- 429 without Retry-After header

---

## Q021: Output Caching ASP.NET

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Performance |
| **Frequency** | Common |

### Question

When use ASP.NET output caching vs Redis?

### Short Answer (30 seconds)

Output caching: HTTP response cache for identical GETs on same instance/fleet with cache policy. Redis: shared cache across services, cache-aside pattern.

### Detailed Answer (3–5 minutes)

**Output cache:** `[OutputCache(PolicyName = "Catalog")]` — VaryByQueryKeys.

**Architect:** Don't output-cache personalized/authenticated responses without VaryByUser.

**Invalidate:** Tag-based eviction .NET 8+.

### Architecture Perspective

Cache layer choice affects consistency.

### Follow-up Questions

1. **CDN + output cache? — CDN edge for static; output cache origin.**
2. **Cache stampede? — Lock or stale-while-revalidate.**

### Common Mistakes in Interviews

- Cache user-specific JSON without Vary
- Output cache on POST
- No cache invalidation on update

---

## Q022: Native AOT Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Performance |
| **Frequency** | Occasional |

### Question

When recommend Native AOT for .NET services?

### Short Answer (30 seconds)

Fast startup, small footprint — edge, serverless cold start, CLI tools. Constraints: no dynamic reflection, limited EF/serialization.

### Detailed Answer (3–5 minutes)

**Architect pilot criteria:** Measure startup and size win vs feature restrictions.

**Not default:** Full EF Core app with heavy reflection — validate compatibility.

**.NET 8+:** Improving but architect signs off per service.

### Architecture Perspective

AOT is strategic not default.

### Follow-up Questions

1. **Trimming vs AOT? — Trimming reduces size; AOT eliminates JIT.**
2. **Source generators replace reflection? — Required for AOT paths.**

### Common Mistakes in Interviews

- AOT entire monolith day one
- EF Core heavy app without AOT test
- Ignore trimming warnings

---

## Q023: System.Threading.Channels

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Concurrency |
| **Frequency** | Common |

### Question

When use `Channel<T>` in .NET architecture?

### Short Answer (30 seconds)

In-process producer-consumer with backpressure — decouple stages without full message broker for single-process pipelines.

### Detailed Answer (3–5 minutes)

**Bounded channel:** `FullMode.Wait` applies backpressure.

**Architect:** Use broker (Service Bus) cross-process; Channel within single worker process pipeline.

**Reader:** `await foreach` async enumeration.

### Architecture Perspective

Channels bridge async and producer-consumer.

### Follow-up Questions

1. **Channel vs BlockingCollection? — Prefer Channel async-native.**
2. **SingleReader optimization? — Performance flag when true.**

### Common Mistakes in Interviews

- Unbounded channel hides memory leak
- Channel cross-service boundary
- No cancellation in reader loop

---

## Q024: IAsyncDisposable Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Resource Mgmt |
| **Frequency** | Common |

### Question

When implement `IAsyncDisposable` vs `IDisposable`?

### Short Answer (30 seconds)

Async disposal when cleanup does I/O — database flush, async file write, gRPC channel shutdown.

### Detailed Answer (3–5 minutes)

**Pattern:**
```csharp
await using var conn = await OpenAsync();
```

**Architect:** `BackgroundService` dispose async resources on shutdown token.

**Implement both:** `DisposeAsync` calls sync Dispose when no async work needed.

### Architecture Perspective

Async disposal prevents thread blocking on teardown.

### Follow-up Questions

1. **ConfigureAwait in DisposeAsync? — Usually ConfigureAwait(false).**
2. **GC.SuppressFinalize? — Still apply in hybrid dispose pattern.**

### Common Mistakes in Interviews

- Block on DisposeAsync().GetAwaiter().GetResult()
- Only IDisposable on async resource
- No disposal in scoped services

---

## Q025: Data Protection API

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Security |
| **Frequency** | Occasional |

### Question

ASP.NET Data Protection for multi-instance apps?

### Short Answer (30 seconds)

Encrypts cookies, antiforgery tokens, temp data. Keys must be shared across instances — Redis, Azure Blob, registry.

### Detailed Answer (3–5 minutes)

**Architect:** Persist key ring to shared storage — else each instance invalidates cookies on deploy rotation.

**Kubernetes:** Mount key ring secret or use Redis key ring.

**Rotation:** Default 90-day — plan seamless rotation.

### Architecture Perspective

Cookie auth breaks without shared key ring.

### Follow-up Questions

1. **IDataProtectionProvider scope? — Per-app purpose strings isolate.**
2. **Encrypt at rest keys? — Azure Key Vault protector.**

### Common Mistakes in Interviews

- Ephemeral keys per container restart
- Same app name different environments sharing keys
- No key rotation plan

---

## Q026: JWT Authentication Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Design JWT auth for SPA + .NET API?

### Short Answer (30 seconds)

Entra ID / Auth0 issues JWT. API validates issuer, audience, signature, lifetime. Short access token + refresh token rotation.

### Detailed Answer (3–5 minutes)

**Architect:** Never store JWT in localStorage if XSS risk — BFF or HttpOnly cookie pattern.

**Validate:** `AddJwtBearer` with authority metadata.

**Claims:** Map to policies not hardcoded role strings in controllers.

### Architecture Perspective

Auth architecture is security foundation.

### Follow-up Questions

1. **Token introspection? — Opaque tokens reference — different pattern.**
2. **mTLS service-to-service? — Complement JWT internal east-west.**

### Common Mistakes in Interviews

- Long-lived JWT months
- No audience validation
- Custom crypto instead of standard library

---

## Q027: Policy-Based Authorization

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Security |
| **Frequency** | Common |

### Question

Policy-based authorization vs role checks in controllers?

### Short Answer (30 seconds)

`[Authorize(Policy = "CanRefund")]` with requirement/handler — scales better than role strings.

### Detailed Answer (3–5 minutes)

**Architect:** Policies encode business capabilities. Handlers check database permissions dynamically.

**Test:** Authorization handler unit tests per policy.

**Resource-based:** `IAuthorizationService.AuthorizeAsync(user, order, "Owner")`.

### Architecture Perspective

Authorization model must evolve with product.

### Follow-up Questions

1. **FallbackPolicy? — Default deny — secure by default.**
2. **Combine policies? — Require multiple policies on endpoint.**

### Common Mistakes in Interviews

- [Authorize(Roles = "Admin")] everywhere
- Authorization logic in controller body
- No test on custom handlers

---

## Q028: ProblemDetails RFC 7807

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | API Design |
| **Frequency** | Common |

### Question

Standardize API errors with ProblemDetails?

### Short Answer (30 seconds)

Consistent JSON error shape: type, title, status, detail, instance, extensions for validation errors.

### Detailed Answer (3–5 minutes)

**ASP.NET:** `AddProblemDetails()` + exception handler middleware.

**Architect:** Never leak stack traces in prod. Correlation ID in `extensions`.

**Client:** Predictable parsing for UI error display.

### Architecture Perspective

Error contract is public API surface.

### Follow-up Questions

1. **ValidationProblemDetails? — 400 with field errors dictionary.**
2. **ProblemDetails in gRPC? — Rich error model equivalent.**

### Common Mistakes in Interviews

- Different error JSON per endpoint
- 500 returns exception.Message only
- No correlation ID in errors

---

## Q029: API Versioning Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | API Design |
| **Frequency** | Common |

### Question

URL vs header vs query API versioning for .NET?

### Short Answer (30 seconds)

URL path (`/v2/orders`) most visible and cache-friendly. Header for strict REST purists. Query `?api-version=` acceptable.

### Detailed Answer (3–5 minutes)

**Architect:** Version public APIs from day one. Deprecation policy: 6-12 months notice.

**Package:** `Asp.Versioning.Mvc` with sunset headers.

**Internal services:** May skip versioning early — document when to add.

### Architecture Perspective

Versioning prevents breaking mobile clients.

### Follow-up Questions

1. **Combine versioning with OpenAPI? — Separate Swagger doc per version.**
2. **Version internal gRPC? — Package proto versioning.**

### Common Mistakes in Interviews

- Breaking change without version bump
- Three versions supported forever
- No deprecation communication

---

## Q030: BenchmarkDotNet for Architects

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Performance |
| **Frequency** | Occasional |

### Question

When require BenchmarkDotNet before architectural change?

### Short Answer (30 seconds)

Before claiming Span vs string, pooling vs allocate, serialization library choice — measure with BenchmarkDotNet.

### Detailed Answer (3–5 minutes)

**Architect:** Engineers bring benchmarks to design reviews — not opinions.

**CI:** Benchmark in nightly not every PR — flaky in shared runners.

**MemoryDiagnoser:** Allocation counts matter for hot paths.

### Architecture Perspective

Data-driven performance decisions.

### Follow-up Questions

1. **Microbenchmark trap? — Benchmark representative workload not toy loop.**
2. **Profiler vs benchmark? — Profiler finds hotspots; benchmark compares fixes.**

### Common Mistakes in Interviews

- Optimize without measuring
- Benchmark debug build
- Ignore allocation in API hot path

---
