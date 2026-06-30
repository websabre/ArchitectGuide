# Week 02 — Intermediate Q&A

> Q031–Q070: Premium format (Week 1 quality).

---


## Q031: GC generations tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | GC |
| **Frequency** | Very Common |

### Question

What is GC generations tuning and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use GC generations tuning when monitor gen2 collections. Avoid when manual gc.collect everywhere. Production example: dotnet-counters % Time in GC.

### Detailed Answer (3–5 minutes)

**Concept:** GC generations tuning

**When to use:** Monitor Gen2 collections

**When to avoid:** Manual GC.Collect everywhere

**Production example:** dotnet-counters % Time in GC

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect GC generations tuning to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify GC generations tuning with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is GC generations tuning overkill? — Manual GC.Collect everywhere**
2. **How measure success after adopting GC generations tuning? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting GC generations tuning without production example
- Using GC generations tuning when manual gc.collect everywhere
- No rollback plan when GC generations tuning misconfigured

---

## Q032: Thread pool starvation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Async |
| **Frequency** | Common |

### Question

What is Thread pool starvation and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use Thread pool starvation when detect sync-over-async. Avoid when ignore thread pool queue length. Production example: Thread pool starvation events in logs.

### Detailed Answer (3–5 minutes)

**Concept:** Thread pool starvation

**When to use:** Detect sync-over-async

**When to avoid:** Ignore thread pool queue length

**Production example:** Thread pool starvation events in logs

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Thread pool starvation to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Thread pool starvation with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is Thread pool starvation overkill? — Ignore thread pool queue length**
2. **How measure success after adopting Thread pool starvation? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Thread pool starvation without production example
- Using Thread pool starvation when ignore thread pool queue length
- No rollback plan when Thread pool starvation misconfigured

---

## Q033: HttpClientFactory

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | HTTP |
| **Frequency** | Occasional |

### Question

What is HttpClientFactory and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use HttpClientFactory when managed httpclient lifetime. Avoid when new httpclient per request. Production example: IHttpClientFactory typed clients.

### Detailed Answer (3–5 minutes)

**Concept:** HttpClientFactory

**When to use:** Managed HttpClient lifetime

**When to avoid:** new HttpClient per request

**Production example:** IHttpClientFactory typed clients

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect HttpClientFactory to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify HttpClientFactory with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is HttpClientFactory overkill? — new HttpClient per request**
2. **How measure success after adopting HttpClientFactory? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting HttpClientFactory without production example
- Using HttpClientFactory when new httpclient per request
- No rollback plan when HttpClientFactory misconfigured

---

## Q034: Polly resilience

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Resilience |
| **Frequency** | Very Common |

### Question

What is Polly resilience and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use Polly resilience when retry circuit breaker timeout. Avoid when infinite retry on 500. Production example: Polly pipeline on Refit client.

### Detailed Answer (3–5 minutes)

**Concept:** Polly resilience

**When to use:** Retry circuit breaker timeout

**When to avoid:** Infinite retry on 500

**Production example:** Polly pipeline on Refit client

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Polly resilience to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Polly resilience with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is Polly resilience overkill? — Infinite retry on 500**
2. **How measure success after adopting Polly resilience? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Polly resilience without production example
- Using Polly resilience when infinite retry on 500
- No rollback plan when Polly resilience misconfigured

---

## Q035: OpenTelemetry .NET

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Observability |
| **Frequency** | Common |

### Question

What is OpenTelemetry .NET and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use OpenTelemetry .NET when traces metrics logs. Avoid when proprietary agent only. Production example: OTel → Azure Monitor exporter.

### Detailed Answer (3–5 minutes)

**Concept:** OpenTelemetry .NET

**When to use:** Traces metrics logs

**When to avoid:** Proprietary agent only

**Production example:** OTel → Azure Monitor exporter

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect OpenTelemetry .NET to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify OpenTelemetry .NET with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is OpenTelemetry .NET overkill? — Proprietary agent only**
2. **How measure success after adopting OpenTelemetry .NET? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting OpenTelemetry .NET without production example
- Using OpenTelemetry .NET when proprietary agent only
- No rollback plan when OpenTelemetry .NET misconfigured

---

## Q036: Serilog structured logging

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Observability |
| **Frequency** | Occasional |

### Question

What is Serilog structured logging and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use Serilog structured logging when structured properties. Avoid when string concat logs. Production example: Serilog enrichers CorrelationId.

### Detailed Answer (3–5 minutes)

**Concept:** Serilog structured logging

**When to use:** Structured properties

**When to avoid:** String concat logs

**Production example:** Serilog enrichers CorrelationId

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Serilog structured logging to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Serilog structured logging with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is Serilog structured logging overkill? — String concat logs**
2. **How measure success after adopting Serilog structured logging? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Serilog structured logging without production example
- Using Serilog structured logging when string concat logs
- No rollback plan when Serilog structured logging misconfigured

---

## Q037: EF Core DbContext pooling

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | EF Core |
| **Frequency** | Very Common |

### Question

What is EF Core DbContext pooling and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use EF Core DbContext pooling when high throughput contexts. Avoid when pooling with stateful context. Production example: AddDbContextPool for read API.

### Detailed Answer (3–5 minutes)

**Concept:** EF Core DbContext pooling

**When to use:** High throughput contexts

**When to avoid:** Pooling with stateful context

**Production example:** AddDbContextPool for read API

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect EF Core DbContext pooling to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify EF Core DbContext pooling with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is EF Core DbContext pooling overkill? — Pooling with stateful context**
2. **How measure success after adopting EF Core DbContext pooling? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting EF Core DbContext pooling without production example
- Using EF Core DbContext pooling when pooling with stateful context
- No rollback plan when EF Core DbContext pooling misconfigured

---

## Q038: EF Core interceptors

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | EF Core |
| **Frequency** | Common |

### Question

What is EF Core interceptors and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use EF Core interceptors when cross-cutting data concerns. Avoid when override savechanges everywhere. Production example: Auditing interceptor.

### Detailed Answer (3–5 minutes)

**Concept:** EF Core interceptors

**When to use:** Cross-cutting data concerns

**When to avoid:** Override SaveChanges everywhere

**Production example:** Auditing interceptor

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect EF Core interceptors to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify EF Core interceptors with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is EF Core interceptors overkill? — Override SaveChanges everywhere**
2. **How measure success after adopting EF Core interceptors? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting EF Core interceptors without production example
- Using EF Core interceptors when override savechanges everywhere
- No rollback plan when EF Core interceptors misconfigured

---

## Q039: Minimal API filters

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | ASP.NET |
| **Frequency** | Occasional |

### Question

What is Minimal API filters and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use Minimal API filters when cross-cutting on endpoints. Avoid when duplicate middleware logic. Production example: IEndpointFilter validation.

### Detailed Answer (3–5 minutes)

**Concept:** Minimal API filters

**When to use:** Cross-cutting on endpoints

**When to avoid:** Duplicate middleware logic

**Production example:** IEndpointFilter validation

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Minimal API filters to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Minimal API filters with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is Minimal API filters overkill? — Duplicate middleware logic**
2. **How measure success after adopting Minimal API filters? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Minimal API filters without production example
- Using Minimal API filters when duplicate middleware logic
- No rollback plan when Minimal API filters misconfigured

---

## Q040: Rate limiting middleware

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | ASP.NET |
| **Frequency** | Very Common |

### Question

What is Rate limiting middleware and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use Rate limiting middleware when .net 7+ built-in limiter. Avoid when custom broken limiter. Production example: Fixed window on public API.

### Detailed Answer (3–5 minutes)

**Concept:** Rate limiting middleware

**When to use:** .NET 7+ built-in limiter

**When to avoid:** Custom broken limiter

**Production example:** Fixed window on public API

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Rate limiting middleware to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Rate limiting middleware with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is Rate limiting middleware overkill? — Custom broken limiter**
2. **How measure success after adopting Rate limiting middleware? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Rate limiting middleware without production example
- Using Rate limiting middleware when custom broken limiter
- No rollback plan when Rate limiting middleware misconfigured

---

## Q041: Output caching

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | ASP.NET |
| **Frequency** | Common |

### Question

What is Output caching and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use Output caching when cache get responses. Avoid when cache personalized responses. Production example: Output cache on catalog GET.

### Detailed Answer (3–5 minutes)

**Concept:** Output caching

**When to use:** Cache GET responses

**When to avoid:** Cache personalized responses

**Production example:** Output cache on catalog GET

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Output caching to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Output caching with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is Output caching overkill? — Cache personalized responses**
2. **How measure success after adopting Output caching? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Output caching without production example
- Using Output caching when cache personalized responses
- No rollback plan when Output caching misconfigured

---

## Q042: Native AOT constraints

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Occasional |

### Question

What is Native AOT constraints and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use Native AOT constraints when startup and size wins. Avoid when aot with heavy reflection. Production example: AOT pilot on worker service.

### Detailed Answer (3–5 minutes)

**Concept:** Native AOT constraints

**When to use:** Startup and size wins

**When to avoid:** AOT with heavy reflection

**Production example:** AOT pilot on worker service

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Native AOT constraints to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Native AOT constraints with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is Native AOT constraints overkill? — AOT with heavy reflection**
2. **How measure success after adopting Native AOT constraints? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Native AOT constraints without production example
- Using Native AOT constraints when aot with heavy reflection
- No rollback plan when Native AOT constraints misconfigured

---

## Q043: Channels producer consumer

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Concurrency |
| **Frequency** | Very Common |

### Question

What is Channels producer consumer and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use Channels producer consumer when in-process async queues. Avoid when lock everywhere. Production example: Channel<T> for in-proc pipeline.

### Detailed Answer (3–5 minutes)

**Concept:** Channels producer consumer

**When to use:** In-process async queues

**When to avoid:** lock everywhere

**Production example:** Channel<T> for in-proc pipeline

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Channels producer consumer to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Channels producer consumer with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is Channels producer consumer overkill? — lock everywhere**
2. **How measure success after adopting Channels producer consumer? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Channels producer consumer without production example
- Using Channels producer consumer when lock everywhere
- No rollback plan when Channels producer consumer misconfigured

---

## Q044: IHostedService lifecycle

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hosting |
| **Frequency** | Common |

### Question

What is IHostedService lifecycle and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use IHostedService lifecycle when start stop cancellation. Avoid when ignore stopping token. Production example: BackgroundService with graceful drain.

### Detailed Answer (3–5 minutes)

**Concept:** IHostedService lifecycle

**When to use:** Start stop cancellation

**When to avoid:** Ignore stopping token

**Production example:** BackgroundService with graceful drain

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect IHostedService lifecycle to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify IHostedService lifecycle with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is IHostedService lifecycle overkill? — Ignore stopping token**
2. **How measure success after adopting IHostedService lifecycle? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting IHostedService lifecycle without production example
- Using IHostedService lifecycle when ignore stopping token
- No rollback plan when IHostedService lifecycle misconfigured

---

## Q045: Configuration providers chain

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Config |
| **Frequency** | Occasional |

### Question

What is Configuration providers chain and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use Configuration providers chain when layered config sources. Avoid when hardcoded prod strings. Production example: Key Vault + App Configuration.

### Detailed Answer (3–5 minutes)

**Concept:** Configuration providers chain

**When to use:** Layered config sources

**When to avoid:** Hardcoded prod strings

**Production example:** Key Vault + App Configuration

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Configuration providers chain to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Configuration providers chain with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is Configuration providers chain overkill? — Hardcoded prod strings**
2. **How measure success after adopting Configuration providers chain? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Configuration providers chain without production example
- Using Configuration providers chain when hardcoded prod strings
- No rollback plan when Configuration providers chain misconfigured

---

## Q046: Data protection API

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

What is Data protection API and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use Data protection API when cookie encryption keys. Avoid when custom crypto for cookies. Production example: Data Protection shared key ring.

### Detailed Answer (3–5 minutes)

**Concept:** Data protection API

**When to use:** Cookie encryption keys

**When to avoid:** Custom crypto for cookies

**Production example:** Data Protection shared key ring

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Data protection API to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Data protection API with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is Data protection API overkill? — Custom crypto for cookies**
2. **How measure success after adopting Data protection API? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Data protection API without production example
- Using Data protection API when custom crypto for cookies
- No rollback plan when Data protection API misconfigured

---

## Q047: Authentication schemes

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

What is Authentication schemes and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use Authentication schemes when jwt + cookies multi-scheme. Avoid when one scheme hack. Production example: AddAuthentication multiple schemes.

### Detailed Answer (3–5 minutes)

**Concept:** Authentication schemes

**When to use:** JWT + cookies multi-scheme

**When to avoid:** One scheme hack

**Production example:** AddAuthentication multiple schemes

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Authentication schemes to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Authentication schemes with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is Authentication schemes overkill? — One scheme hack**
2. **How measure success after adopting Authentication schemes? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Authentication schemes without production example
- Using Authentication schemes when one scheme hack
- No rollback plan when Authentication schemes misconfigured

---

## Q048: Authorization policies

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Occasional |

### Question

What is Authorization policies and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use Authorization policies when policy-based rules. Avoid when role checks scattered. Production example: RequireClaim policy handler.

### Detailed Answer (3–5 minutes)

**Concept:** Authorization policies

**When to use:** Policy-based rules

**When to avoid:** Role checks scattered

**Production example:** RequireClaim policy handler

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Authorization policies to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Authorization policies with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is Authorization policies overkill? — Role checks scattered**
2. **How measure success after adopting Authorization policies? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Authorization policies without production example
- Using Authorization policies when role checks scattered
- No rollback plan when Authorization policies misconfigured

---

## Q049: ProblemDetails RFC7807

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | API |
| **Frequency** | Very Common |

### Question

What is ProblemDetails RFC7807 and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use ProblemDetails RFC7807 when standard error responses. Avoid when custom error shapes per endpoint. Production example: ProblemDetails middleware.

### Detailed Answer (3–5 minutes)

**Concept:** ProblemDetails RFC7807

**When to use:** Standard error responses

**When to avoid:** Custom error shapes per endpoint

**Production example:** ProblemDetails middleware

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect ProblemDetails RFC7807 to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify ProblemDetails RFC7807 with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is ProblemDetails RFC7807 overkill? — Custom error shapes per endpoint**
2. **How measure success after adopting ProblemDetails RFC7807? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting ProblemDetails RFC7807 without production example
- Using ProblemDetails RFC7807 when custom error shapes per endpoint
- No rollback plan when ProblemDetails RFC7807 misconfigured

---

## Q050: API versioning Asp.Versioning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | API |
| **Frequency** | Common |

### Question

What is API versioning Asp.Versioning and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use API versioning Asp.Versioning when version discovery. Avoid when break clients silently. Production example: Asp.Versioning.Mvc package.

### Detailed Answer (3–5 minutes)

**Concept:** API versioning Asp.Versioning

**When to use:** Version discovery

**When to avoid:** Break clients silently

**Production example:** Asp.Versioning.Mvc package

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect API versioning Asp.Versioning to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify API versioning Asp.Versioning with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is API versioning Asp.Versioning overkill? — Break clients silently**
2. **How measure success after adopting API versioning Asp.Versioning? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting API versioning Asp.Versioning without production example
- Using API versioning Asp.Versioning when break clients silently
- No rollback plan when API versioning Asp.Versioning misconfigured

---

## Q051: JIT vs AOT compilation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Runtime |
| **Frequency** | Occasional |

### Question

What is JIT vs AOT compilation and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use JIT vs AOT compilation when latency-sensitive apis. Avoid when heavy reflection plugins. Production example: Native AOT worker for edge inference.

### Detailed Answer (3–5 minutes)

**Concept:** JIT vs AOT compilation

**When to use:** Latency-sensitive APIs

**When to avoid:** Heavy reflection plugins

**Production example:** Native AOT worker for edge inference

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect JIT vs AOT compilation to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify JIT vs AOT compilation with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is JIT vs AOT compilation overkill? — Heavy reflection plugins**
2. **How measure success after adopting JIT vs AOT compilation? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting JIT vs AOT compilation without production example
- Using JIT vs AOT compilation when heavy reflection plugins
- No rollback plan when JIT vs AOT compilation misconfigured

---

## Q052: AssemblyLoadContext

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Runtime |
| **Frequency** | Very Common |

### Question

What is AssemblyLoadContext and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use AssemblyLoadContext when plugin isolation. Avoid when simple single-app deploy. Production example: Plugin host with collectible ALC.

### Detailed Answer (3–5 minutes)

**Concept:** AssemblyLoadContext

**When to use:** Plugin isolation

**When to avoid:** Simple single-app deploy

**Production example:** Plugin host with collectible ALC

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect AssemblyLoadContext to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify AssemblyLoadContext with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is AssemblyLoadContext overkill? — Simple single-app deploy**
2. **How measure success after adopting AssemblyLoadContext? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting AssemblyLoadContext without production example
- Using AssemblyLoadContext when simple single-app deploy
- No rollback plan when AssemblyLoadContext misconfigured

---

## Q053: Middleware pipeline order

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | ASP.NET |
| **Frequency** | Common |

### Question

What is Middleware pipeline order and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use Middleware pipeline order when cross-cutting concerns. Avoid when random middleware registration. Production example: Exception handler before auth.

### Detailed Answer (3–5 minutes)

**Concept:** Middleware pipeline order

**When to use:** Cross-cutting concerns

**When to avoid:** Random middleware registration

**Production example:** Exception handler before auth

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Middleware pipeline order to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Middleware pipeline order with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is Middleware pipeline order overkill? — Random middleware registration**
2. **How measure success after adopting Middleware pipeline order? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Middleware pipeline order without production example
- Using Middleware pipeline order when random middleware registration
- No rollback plan when Middleware pipeline order misconfigured

---

## Q054: Kestrel limits tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hosting |
| **Frequency** | Occasional |

### Question

What is Kestrel limits tuning and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use Kestrel limits tuning when high-concurrency apis. Avoid when default limits blindly. Production example: MaxConcurrentConnections tuned per instance.

### Detailed Answer (3–5 minutes)

**Concept:** Kestrel limits tuning

**When to use:** High-concurrency APIs

**When to avoid:** Default limits blindly

**Production example:** MaxConcurrentConnections tuned per instance

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Kestrel limits tuning to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Kestrel limits tuning with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is Kestrel limits tuning overkill? — Default limits blindly**
2. **How measure success after adopting Kestrel limits tuning? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Kestrel limits tuning without production example
- Using Kestrel limits tuning when default limits blindly
- No rollback plan when Kestrel limits tuning misconfigured

---

## Q055: Generic host builder

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hosting |
| **Frequency** | Very Common |

### Question

What is Generic host builder and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use Generic host builder when unified worker/web hosting. Avoid when duplicate program.cs patterns. Production example: Host.CreateDefaultBuilder shared template.

### Detailed Answer (3–5 minutes)

**Concept:** Generic host builder

**When to use:** Unified worker/web hosting

**When to avoid:** Duplicate Program.cs patterns

**Production example:** Host.CreateDefaultBuilder shared template

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Generic host builder to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Generic host builder with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is Generic host builder overkill? — Duplicate Program.cs patterns**
2. **How measure success after adopting Generic host builder? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Generic host builder without production example
- Using Generic host builder when duplicate program.cs patterns
- No rollback plan when Generic host builder misconfigured

---

## Q056: Options validation on start

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Configuration |
| **Frequency** | Common |

### Question

What is Options validation on start and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use Options validation on start when fail-fast config. Avoid when runtime null reference from config. Production example: ValidateOnStart for payment settings.

### Detailed Answer (3–5 minutes)

**Concept:** Options validation on start

**When to use:** Fail-fast config

**When to avoid:** Runtime null reference from config

**Production example:** ValidateOnStart for payment settings

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Options validation on start to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Options validation on start with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is Options validation on start overkill? — Runtime null reference from config**
2. **How measure success after adopting Options validation on start? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Options validation on start without production example
- Using Options validation on start when runtime null reference from config
- No rollback plan when Options validation on start misconfigured

---

## Q057: Secret management Key Vault

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Configuration |
| **Frequency** | Occasional |

### Question

What is Secret management Key Vault and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use Secret management Key Vault when production secrets. Avoid when secrets in env without rotation. Production example: Azure Key Vault provider + managed identity.

### Detailed Answer (3–5 minutes)

**Concept:** Secret management Key Vault

**When to use:** Production secrets

**When to avoid:** Secrets in env without rotation

**Production example:** Azure Key Vault provider + managed identity

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Secret management Key Vault to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Secret management Key Vault with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is Secret management Key Vault overkill? — Secrets in env without rotation**
2. **How measure success after adopting Secret management Key Vault? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Secret management Key Vault without production example
- Using Secret management Key Vault when secrets in env without rotation
- No rollback plan when Secret management Key Vault misconfigured

---

## Q058: DI keyed services

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DI |
| **Frequency** | Very Common |

### Question

What is DI keyed services and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use DI keyed services when multi-tenant providers. Avoid when factory anti-pattern everywhere. Production example: Keyed IPaymentGateway per region.

### Detailed Answer (3–5 minutes)

**Concept:** DI keyed services

**When to use:** Multi-tenant providers

**When to avoid:** Factory anti-pattern everywhere

**Production example:** Keyed IPaymentGateway per region

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect DI keyed services to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify DI keyed services with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is DI keyed services overkill? — Factory anti-pattern everywhere**
2. **How measure success after adopting DI keyed services? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting DI keyed services without production example
- Using DI keyed services when factory anti-pattern everywhere
- No rollback plan when DI keyed services misconfigured

---

## Q059: Scoped factory pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DI |
| **Frequency** | Common |

### Question

What is Scoped factory pattern and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use Scoped factory pattern when singleton needing scoped deps. Avoid when captive dependency. Production example: IServiceScopeFactory in background worker.

### Detailed Answer (3–5 minutes)

**Concept:** Scoped factory pattern

**When to use:** Singleton needing scoped deps

**When to avoid:** Captive dependency

**Production example:** IServiceScopeFactory in background worker

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Scoped factory pattern to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Scoped factory pattern with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is Scoped factory pattern overkill? — Captive dependency**
2. **How measure success after adopting Scoped factory pattern? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Scoped factory pattern without production example
- Using Scoped factory pattern when captive dependency
- No rollback plan when Scoped factory pattern misconfigured

---

## Q060: BackgroundService graceful stop

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hosting |
| **Frequency** | Occasional |

### Question

What is BackgroundService graceful stop and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use BackgroundService graceful stop when long-running consumers. Avoid when kill -9 without drain. Production example: StoppingToken honored in poll loop.

### Detailed Answer (3–5 minutes)

**Concept:** BackgroundService graceful stop

**When to use:** Long-running consumers

**When to avoid:** Kill -9 without drain

**Production example:** StoppingToken honored in poll loop

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect BackgroundService graceful stop to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify BackgroundService graceful stop with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is BackgroundService graceful stop overkill? — Kill -9 without drain**
2. **How measure success after adopting BackgroundService graceful stop? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting BackgroundService graceful stop without production example
- Using BackgroundService graceful stop when kill -9 without drain
- No rollback plan when BackgroundService graceful stop misconfigured

---

## Q061: Health check liveness readiness

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Very Common |

### Question

What is Health check liveness readiness and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use Health check liveness readiness when k8s probes. Avoid when db check in liveness. Production example: Separate /health/live and /ready.

### Detailed Answer (3–5 minutes)

**Concept:** Health check liveness readiness

**When to use:** K8s probes

**When to avoid:** DB check in liveness

**Production example:** Separate /health/live and /ready

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Health check liveness readiness to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Health check liveness readiness with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is Health check liveness readiness overkill? — DB check in liveness**
2. **How measure success after adopting Health check liveness readiness? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Health check liveness readiness without production example
- Using Health check liveness readiness when db check in liveness
- No rollback plan when Health check liveness readiness misconfigured

---

## Q062: YARP reverse proxy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hosting |
| **Frequency** | Common |

### Question

What is YARP reverse proxy and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use YARP reverse proxy when api gateway on .net. Avoid when custom proxy from scratch. Production example: YARP routes to microservices.

### Detailed Answer (3–5 minutes)

**Concept:** YARP reverse proxy

**When to use:** API gateway on .NET

**When to avoid:** Custom proxy from scratch

**Production example:** YARP routes to microservices

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect YARP reverse proxy to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify YARP reverse proxy with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is YARP reverse proxy overkill? — Custom proxy from scratch**
2. **How measure success after adopting YARP reverse proxy? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting YARP reverse proxy without production example
- Using YARP reverse proxy when custom proxy from scratch
- No rollback plan when YARP reverse proxy misconfigured

---

## Q063: gRPC streaming patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | API Design |
| **Frequency** | Occasional |

### Question

What is gRPC streaming patterns and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use gRPC streaming patterns when bidirectional streams. Avoid when rest for bulk binary. Production example: Server streaming for log tail.

### Detailed Answer (3–5 minutes)

**Concept:** gRPC streaming patterns

**When to use:** Bidirectional streams

**When to avoid:** REST for bulk binary

**Production example:** Server streaming for log tail

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect gRPC streaming patterns to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify gRPC streaming patterns with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is gRPC streaming patterns overkill? — REST for bulk binary**
2. **How measure success after adopting gRPC streaming patterns? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting gRPC streaming patterns without production example
- Using gRPC streaming patterns when rest for bulk binary
- No rollback plan when gRPC streaming patterns misconfigured

---

## Q064: SignalR backplane

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Real-time |
| **Frequency** | Very Common |

### Question

What is SignalR backplane and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use SignalR backplane when multi-instance hubs. Avoid when sticky sessions only. Production example: Redis backplane for scale-out.

### Detailed Answer (3–5 minutes)

**Concept:** SignalR backplane

**When to use:** Multi-instance hubs

**When to avoid:** Sticky sessions only

**Production example:** Redis backplane for scale-out

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect SignalR backplane to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify SignalR backplane with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is SignalR backplane overkill? — Sticky sessions only**
2. **How measure success after adopting SignalR backplane? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting SignalR backplane without production example
- Using SignalR backplane when sticky sessions only
- No rollback plan when SignalR backplane misconfigured

---

## Q065: EF Core compiled queries

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | EF Core |
| **Frequency** | Common |

### Question

What is EF Core compiled queries and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use EF Core compiled queries when hot path queries. Avoid when linq recompile every call. Production example: EF.CompileQuery for catalog lookup.

### Detailed Answer (3–5 minutes)

**Concept:** EF Core compiled queries

**When to use:** Hot path queries

**When to avoid:** LINQ recompile every call

**Production example:** EF.CompileQuery for catalog lookup

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect EF Core compiled queries to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify EF Core compiled queries with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is EF Core compiled queries overkill? — LINQ recompile every call**
2. **How measure success after adopting EF Core compiled queries? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting EF Core compiled queries without production example
- Using EF Core compiled queries when linq recompile every call
- No rollback plan when EF Core compiled queries misconfigured

---

## Q066: EF Core split queries

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | EF Core |
| **Frequency** | Occasional |

### Question

What is EF Core split queries and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use EF Core split queries when cartesian explosion joins. Avoid when always single query. Production example: AsSplitQuery on order+lines+payments.

### Detailed Answer (3–5 minutes)

**Concept:** EF Core split queries

**When to use:** Cartesian explosion joins

**When to avoid:** Always single query

**Production example:** AsSplitQuery on order+lines+payments

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect EF Core split queries to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify EF Core split queries with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is EF Core split queries overkill? — Always single query**
2. **How measure success after adopting EF Core split queries? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting EF Core split queries without production example
- Using EF Core split queries when always single query
- No rollback plan when EF Core split queries misconfigured

---

## Q067: EF Core global query filters

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | EF Core |
| **Frequency** | Very Common |

### Question

What is EF Core global query filters and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use EF Core global query filters when soft delete multi-tenant. Avoid when filter in every repository. Production example: HasQueryFilter on tenantId.

### Detailed Answer (3–5 minutes)

**Concept:** EF Core global query filters

**When to use:** Soft delete multi-tenant

**When to avoid:** Filter in every repository

**Production example:** HasQueryFilter on tenantId

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect EF Core global query filters to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify EF Core global query filters with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is EF Core global query filters overkill? — Filter in every repository**
2. **How measure success after adopting EF Core global query filters? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting EF Core global query filters without production example
- Using EF Core global query filters when filter in every repository
- No rollback plan when EF Core global query filters misconfigured

---

## Q068: Dapper vs EF Core

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Data Access |
| **Frequency** | Common |

### Question

What is Dapper vs EF Core and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use Dapper vs EF Core when read-heavy hot paths. Avoid when orm for everything. Production example: Dapper for reporting read models.

### Detailed Answer (3–5 minutes)

**Concept:** Dapper vs EF Core

**When to use:** Read-heavy hot paths

**When to avoid:** ORM for everything

**Production example:** Dapper for reporting read models

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Dapper vs EF Core to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Dapper vs EF Core with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is Dapper vs EF Core overkill? — ORM for everything**
2. **How measure success after adopting Dapper vs EF Core? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Dapper vs EF Core without production example
- Using Dapper vs EF Core when orm for everything
- No rollback plan when Dapper vs EF Core misconfigured

---

## Q069: Connection resiliency

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Data Access |
| **Frequency** | Occasional |

### Question

What is Connection resiliency and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use Connection resiliency when transient sql errors. Avoid when no retry on failover. Production example: EnableRetryOnFailure with backoff.

### Detailed Answer (3–5 minutes)

**Concept:** Connection resiliency

**When to use:** Transient SQL errors

**When to avoid:** No retry on failover

**Production example:** EnableRetryOnFailure with backoff

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect Connection resiliency to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify Connection resiliency with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is Connection resiliency overkill? — No retry on failover**
2. **How measure success after adopting Connection resiliency? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting Connection resiliency without production example
- Using Connection resiliency when no retry on failover
- No rollback plan when Connection resiliency misconfigured

---

## Q070: MemoryCache vs distributed cache

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Caching |
| **Frequency** | Very Common |

### Question

What is MemoryCache vs distributed cache and when would you apply it in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Use MemoryCache vs distributed cache when single instance cache. Avoid when redis for tiny app. Production example: IMemoryCache + IDistributedCache tiered.

### Detailed Answer (3–5 minutes)

**Concept:** MemoryCache vs distributed cache

**When to use:** Single instance cache

**When to avoid:** Redis for tiny app

**Production example:** IMemoryCache + IDistributedCache tiered

**Architect workflow:**
1. Map the access pattern or runtime behavior to this concept
2. Validate with metrics (latency, throughput, memory, IO)
3. Document the choice in team standards or ADR when cross-cutting

**Interview tip:** Connect MemoryCache vs distributed cache to a real system you operated — not textbook definitions only.

### Architecture Perspective

Interviewers expect architects to justify MemoryCache vs distributed cache with production trade-offs in .NET Runtime & Ecosystem.

### Follow-up Questions

1. **When is MemoryCache vs distributed cache overkill? — Redis for tiny app**
2. **How measure success after adopting MemoryCache vs distributed cache? — Define before/after metric on the hot path.**

### Common Mistakes in Interviews

- Quoting MemoryCache vs distributed cache without production example
- Using MemoryCache vs distributed cache when redis for tiny app
- No rollback plan when MemoryCache vs distributed cache misconfigured

---
