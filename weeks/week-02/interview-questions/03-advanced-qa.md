# Week 02 — Advanced Q&A

> Q071–Q100: Premium format (Week 1 quality).

---


## Q071: System.Text.Json vs Newtonsoft — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Serialization |
| **Frequency** | Common |

### Question

What are the advanced trade-offs and failure modes of System.Text.Json vs Newtonsoft at scale in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

At scale, System.Text.Json vs Newtonsoft trades default asp.net serialization against operational complexity. Primary failure mode: mixing serializers.

### Detailed Answer (3–5 minutes)

**Advanced analysis of System.Text.Json vs Newtonsoft:**

**Strengths at scale:** Default ASP.NET serialization

**Failure modes:**
- Misapplication when mixing serializers
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** STJ source gen for AOT

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose System.Text.Json vs Newtonsoft if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated System.Text.Json vs Newtonsoft — not just defined it.

### Follow-up Questions

1. **What monitoring proves System.Text.Json vs Newtonsoft healthy? — SLI tied to stj source gen for aot.**
2. **When would you remove or replace System.Text.Json vs Newtonsoft? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating System.Text.Json vs Newtonsoft as set-and-forget
- No load test before enabling System.Text.Json vs Newtonsoft in production
- Ignoring cost/ops overhead of System.Text.Json vs Newtonsoft

---

## Q072: Source generators overview — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Modern C# |
| **Frequency** | Uncommon |

### Question

What are the advanced trade-offs and failure modes of Source generators overview at scale in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

At scale, Source generators overview trades compile-time codegen against operational complexity. Primary failure mode: runtime reflection heavy paths.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Source generators overview:**

**Strengths at scale:** Compile-time codegen

**Failure modes:**
- Misapplication when runtime reflection heavy paths
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** Mapperly for DTO mapping

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Source generators overview if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Source generators overview — not just defined it.

### Follow-up Questions

1. **What monitoring proves Source generators overview healthy? — SLI tied to mapperly for dto mapping.**
2. **When would you remove or replace Source generators overview? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Source generators overview as set-and-forget
- No load test before enabling Source generators overview in production
- Ignoring cost/ops overhead of Source generators overview

---

## Q073: Activity and diagnostics — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Observability |
| **Frequency** | Common |

### Question

What are the advanced trade-offs and failure modes of Activity and diagnostics at scale in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

At scale, Activity and diagnostics trades distributed tracing against operational complexity. Primary failure mode: string-only logs.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Activity and diagnostics:**

**Strengths at scale:** Distributed tracing

**Failure modes:**
- Misapplication when string-only logs
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** ActivitySource spans per handler

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Activity and diagnostics if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Activity and diagnostics — not just defined it.

### Follow-up Questions

1. **What monitoring proves Activity and diagnostics healthy? — SLI tied to activitysource spans per handler.**
2. **When would you remove or replace Activity and diagnostics? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Activity and diagnostics as set-and-forget
- No load test before enabling Activity and diagnostics in production
- Ignoring cost/ops overhead of Activity and diagnostics

---

## Q074: Metrics with System.Diagnostics.Metrics — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Observability |
| **Frequency** | Uncommon |

### Question

What are the advanced trade-offs and failure modes of Metrics with System.Diagnostics.Metrics at scale in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

At scale, Metrics with System.Diagnostics.Metrics trades custom business metrics against operational complexity. Primary failure mode: log parsing for metrics.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Metrics with System.Diagnostics.Metrics:**

**Strengths at scale:** Custom business metrics

**Failure modes:**
- Misapplication when log parsing for metrics
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** Counter for orders_placed

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Metrics with System.Diagnostics.Metrics if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Metrics with System.Diagnostics.Metrics — not just defined it.

### Follow-up Questions

1. **What monitoring proves Metrics with System.Diagnostics.Metrics healthy? — SLI tied to counter for orders_placed.**
2. **When would you remove or replace Metrics with System.Diagnostics.Metrics? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Metrics with System.Diagnostics.Metrics as set-and-forget
- No load test before enabling Metrics with System.Diagnostics.Metrics in production
- Ignoring cost/ops overhead of Metrics with System.Diagnostics.Metrics

---

## Q075: Culture and localization — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Globalization |
| **Frequency** | Common |

### Question

What are the advanced trade-offs and failure modes of Culture and localization at scale in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

At scale, Culture and localization trades multi-region apis against operational complexity. Primary failure mode: hardcoded date formats.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Culture and localization:**

**Strengths at scale:** Multi-region APIs

**Failure modes:**
- Misapplication when hardcoded date formats
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** RequestLocalization middleware

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Culture and localization if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Culture and localization — not just defined it.

### Follow-up Questions

1. **What monitoring proves Culture and localization healthy? — SLI tied to requestlocalization middleware.**
2. **When would you remove or replace Culture and localization? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Culture and localization as set-and-forget
- No load test before enabling Culture and localization in production
- Ignoring cost/ops overhead of Culture and localization

---

## Q076: CORS architecture — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Security |
| **Frequency** | Uncommon |

### Question

What are the advanced trade-offs and failure modes of CORS architecture at scale in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

At scale, CORS architecture trades browser spa clients against operational complexity. Primary failure mode: allowanyorigin in prod.

### Detailed Answer (3–5 minutes)

**Advanced analysis of CORS architecture:**

**Strengths at scale:** Browser SPA clients

**Failure modes:**
- Misapplication when allowanyorigin in prod
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** Explicit origins per environment

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose CORS architecture if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated CORS architecture — not just defined it.

### Follow-up Questions

1. **What monitoring proves CORS architecture healthy? — SLI tied to explicit origins per environment.**
2. **When would you remove or replace CORS architecture? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating CORS architecture as set-and-forget
- No load test before enabling CORS architecture in production
- Ignoring cost/ops overhead of CORS architecture

---

## Q077: Anti-forgery and CSRF — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Security |
| **Frequency** | Common |

### Question

What are the advanced trade-offs and failure modes of Anti-forgery and CSRF at scale in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

At scale, Anti-forgery and CSRF trades cookie-based mvc against operational complexity. Primary failure mode: csrf on state-changing apis.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Anti-forgery and CSRF:**

**Strengths at scale:** Cookie-based MVC

**Failure modes:**
- Misapplication when csrf on state-changing apis
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** Antiforgery tokens on forms

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Anti-forgery and CSRF if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Anti-forgery and CSRF — not just defined it.

### Follow-up Questions

1. **What monitoring proves Anti-forgery and CSRF healthy? — SLI tied to antiforgery tokens on forms.**
2. **When would you remove or replace Anti-forgery and CSRF? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Anti-forgery and CSRF as set-and-forget
- No load test before enabling Anti-forgery and CSRF in production
- Ignoring cost/ops overhead of Anti-forgery and CSRF

---

## Q078: Certificate authentication — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Security |
| **Frequency** | Uncommon |

### Question

What are the advanced trade-offs and failure modes of Certificate authentication at scale in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

At scale, Certificate authentication trades mtls service mesh against operational complexity. Primary failure mode: password for service-to-service.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Certificate authentication:**

**Strengths at scale:** mTLS service mesh

**Failure modes:**
- Misapplication when password for service-to-service
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** Client cert auth middleware

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Certificate authentication if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Certificate authentication — not just defined it.

### Follow-up Questions

1. **What monitoring proves Certificate authentication healthy? — SLI tied to client cert auth middleware.**
2. **When would you remove or replace Certificate authentication? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Certificate authentication as set-and-forget
- No load test before enabling Certificate authentication in production
- Ignoring cost/ops overhead of Certificate authentication

---

## Q079: Kestrel HTTPS termination — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Hosting |
| **Frequency** | Common |

### Question

What are the advanced trade-offs and failure modes of Kestrel HTTPS termination at scale in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

At scale, Kestrel HTTPS termination trades tls at app against operational complexity. Primary failure mode: tls everywhere in app unnecessarily.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Kestrel HTTPS termination:**

**Strengths at scale:** TLS at app

**Failure modes:**
- Misapplication when tls everywhere in app unnecessarily
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** TLS at ingress terminate to HTTP

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Kestrel HTTPS termination if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Kestrel HTTPS termination — not just defined it.

### Follow-up Questions

1. **What monitoring proves Kestrel HTTPS termination healthy? — SLI tied to tls at ingress terminate to http.**
2. **When would you remove or replace Kestrel HTTPS termination? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Kestrel HTTPS termination as set-and-forget
- No load test before enabling Kestrel HTTPS termination in production
- Ignoring cost/ops overhead of Kestrel HTTPS termination

---

## Q080: Container image layering — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Containers |
| **Frequency** | Uncommon |

### Question

What are the advanced trade-offs and failure modes of Container image layering at scale in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

At scale, Container image layering trades fast ci builds against operational complexity. Primary failure mode: fat single-layer images.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Container image layering:**

**Strengths at scale:** Fast CI builds

**Failure modes:**
- Misapplication when fat single-layer images
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** Multi-stage SDK→runtime slim

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Container image layering if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Container image layering — not just defined it.

### Follow-up Questions

1. **What monitoring proves Container image layering healthy? — SLI tied to multi-stage sdk→runtime slim.**
2. **When would you remove or replace Container image layering? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Container image layering as set-and-forget
- No load test before enabling Container image layering in production
- Ignoring cost/ops overhead of Container image layering

---

## Q081: dotnet monitor diagnostics — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Operations |
| **Frequency** | Common |

### Question

What are the advanced trade-offs and failure modes of dotnet monitor diagnostics at scale in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

At scale, dotnet monitor diagnostics trades production diagnostics against operational complexity. Primary failure mode: attach debugger in prod.

### Detailed Answer (3–5 minutes)

**Advanced analysis of dotnet monitor diagnostics:**

**Strengths at scale:** Production diagnostics

**Failure modes:**
- Misapplication when attach debugger in prod
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** dotnet-monitor sidecar collection

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose dotnet monitor diagnostics if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated dotnet monitor diagnostics — not just defined it.

### Follow-up Questions

1. **What monitoring proves dotnet monitor diagnostics healthy? — SLI tied to dotnet-monitor sidecar collection.**
2. **When would you remove or replace dotnet monitor diagnostics? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating dotnet monitor diagnostics as set-and-forget
- No load test before enabling dotnet monitor diagnostics in production
- Ignoring cost/ops overhead of dotnet monitor diagnostics

---

## Q082: ReadyToRun images — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Performance |
| **Frequency** | Uncommon |

### Question

What are the advanced trade-offs and failure modes of ReadyToRun images at scale in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

At scale, ReadyToRun images trades cold start reduction against operational complexity. Primary failure mode: aot incompatible code paths.

### Detailed Answer (3–5 minutes)

**Advanced analysis of ReadyToRun images:**

**Strengths at scale:** Cold start reduction

**Failure modes:**
- Misapplication when aot incompatible code paths
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** PublishReadyToRun for APIs

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose ReadyToRun images if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated ReadyToRun images — not just defined it.

### Follow-up Questions

1. **What monitoring proves ReadyToRun images healthy? — SLI tied to publishreadytorun for apis.**
2. **When would you remove or replace ReadyToRun images? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating ReadyToRun images as set-and-forget
- No load test before enabling ReadyToRun images in production
- Ignoring cost/ops overhead of ReadyToRun images

---

## Q083: ThreadPool tuning — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Performance |
| **Frequency** | Common |

### Question

What are the advanced trade-offs and failure modes of ThreadPool tuning at scale in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

At scale, ThreadPool tuning trades sync-over-async incidents against operational complexity. Primary failure mode: default pool for batch+web mixed.

### Detailed Answer (3–5 minutes)

**Advanced analysis of ThreadPool tuning:**

**Strengths at scale:** Sync-over-async incidents

**Failure modes:**
- Misapplication when default pool for batch+web mixed
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** Min threads adjusted after profiling

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose ThreadPool tuning if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated ThreadPool tuning — not just defined it.

### Follow-up Questions

1. **What monitoring proves ThreadPool tuning healthy? — SLI tied to min threads adjusted after profiling.**
2. **When would you remove or replace ThreadPool tuning? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating ThreadPool tuning as set-and-forget
- No load test before enabling ThreadPool tuning in production
- Ignoring cost/ops overhead of ThreadPool tuning

---

## Q084: ArrayPool and memory — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Performance |
| **Frequency** | Uncommon |

### Question

What are the advanced trade-offs and failure modes of ArrayPool and memory at scale in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

At scale, ArrayPool and memory trades large buffer reuse against operational complexity. Primary failure mode: new byte[] per request.

### Detailed Answer (3–5 minutes)

**Advanced analysis of ArrayPool and memory:**

**Strengths at scale:** Large buffer reuse

**Failure modes:**
- Misapplication when new byte[] per request
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** ArrayPool<byte>.Shared in parser

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose ArrayPool and memory if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated ArrayPool and memory — not just defined it.

### Follow-up Questions

1. **What monitoring proves ArrayPool and memory healthy? — SLI tied to arraypool<byte>.shared in parser.**
2. **When would you remove or replace ArrayPool and memory? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating ArrayPool and memory as set-and-forget
- No load test before enabling ArrayPool and memory in production
- Ignoring cost/ops overhead of ArrayPool and memory

---

## Q085: Regex source generators — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Performance |
| **Frequency** | Common |

### Question

What are the advanced trade-offs and failure modes of Regex source generators at scale in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

At scale, Regex source generators trades hot path regex against operational complexity. Primary failure mode: compiled regex everywhere.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Regex source generators:**

**Strengths at scale:** Hot path regex

**Failure modes:**
- Misapplication when compiled regex everywhere
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** GeneratedRegex attribute

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Regex source generators if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Regex source generators — not just defined it.

### Follow-up Questions

1. **What monitoring proves Regex source generators healthy? — SLI tied to generatedregex attribute.**
2. **When would you remove or replace Regex source generators? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Regex source generators as set-and-forget
- No load test before enabling Regex source generators in production
- Ignoring cost/ops overhead of Regex source generators

---

## Q086: Hosting startup assemblies — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Hosting |
| **Frequency** | Uncommon |

### Question

What are the advanced trade-offs and failure modes of Hosting startup assemblies at scale in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

At scale, Hosting startup assemblies trades library middleware injection against operational complexity. Primary failure mode: copy-paste startup.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Hosting startup assemblies:**

**Strengths at scale:** Library middleware injection

**Failure modes:**
- Misapplication when copy-paste startup
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** IHostingStartup in shared lib

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Hosting startup assemblies if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Hosting startup assemblies — not just defined it.

### Follow-up Questions

1. **What monitoring proves Hosting startup assemblies healthy? — SLI tied to ihostingstartup in shared lib.**
2. **When would you remove or replace Hosting startup assemblies? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Hosting startup assemblies as set-and-forget
- No load test before enabling Hosting startup assemblies in production
- Ignoring cost/ops overhead of Hosting startup assemblies

---

## Q087: Endpoint routing vs conventional — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | ASP.NET |
| **Frequency** | Common |

### Question

What are the advanced trade-offs and failure modes of Endpoint routing vs conventional at scale in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

At scale, Endpoint routing vs conventional trades minimal apis attribute routing against operational complexity. Primary failure mode: legacy conventional only.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Endpoint routing vs conventional:**

**Strengths at scale:** Minimal APIs attribute routing

**Failure modes:**
- Misapplication when legacy conventional only
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** MapGroup for versioned APIs

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Endpoint routing vs conventional if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Endpoint routing vs conventional — not just defined it.

### Follow-up Questions

1. **What monitoring proves Endpoint routing vs conventional healthy? — SLI tied to mapgroup for versioned apis.**
2. **When would you remove or replace Endpoint routing vs conventional? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Endpoint routing vs conventional as set-and-forget
- No load test before enabling Endpoint routing vs conventional in production
- Ignoring cost/ops overhead of Endpoint routing vs conventional

---

## Q088: ProblemDetails correlation — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | API Design |
| **Frequency** | Uncommon |

### Question

What are the advanced trade-offs and failure modes of ProblemDetails correlation at scale in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

At scale, ProblemDetails correlation trades supportable errors against operational complexity. Primary failure mode: opaque 500 messages.

### Detailed Answer (3–5 minutes)

**Advanced analysis of ProblemDetails correlation:**

**Strengths at scale:** Supportable errors

**Failure modes:**
- Misapplication when opaque 500 messages
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** traceId extension in ProblemDetails

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose ProblemDetails correlation if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated ProblemDetails correlation — not just defined it.

### Follow-up Questions

1. **What monitoring proves ProblemDetails correlation healthy? — SLI tied to traceid extension in problemdetails.**
2. **When would you remove or replace ProblemDetails correlation? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating ProblemDetails correlation as set-and-forget
- No load test before enabling ProblemDetails correlation in production
- Ignoring cost/ops overhead of ProblemDetails correlation

---

## Q089: OpenAPI document filters — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | API Design |
| **Frequency** | Common |

### Question

What are the advanced trade-offs and failure modes of OpenAPI document filters at scale in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

At scale, OpenAPI document filters trades consistent api docs against operational complexity. Primary failure mode: manual swagger edits.

### Detailed Answer (3–5 minutes)

**Advanced analysis of OpenAPI document filters:**

**Strengths at scale:** Consistent API docs

**Failure modes:**
- Misapplication when manual swagger edits
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** IDocumentFilter for security schemes

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose OpenAPI document filters if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated OpenAPI document filters — not just defined it.

### Follow-up Questions

1. **What monitoring proves OpenAPI document filters healthy? — SLI tied to idocumentfilter for security schemes.**
2. **When would you remove or replace OpenAPI document filters? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating OpenAPI document filters as set-and-forget
- No load test before enabling OpenAPI document filters in production
- Ignoring cost/ops overhead of OpenAPI document filters

---

## Q090: Integration test WebApplicationFactory — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Testing |
| **Frequency** | Uncommon |

### Question

What are the advanced trade-offs and failure modes of Integration test WebApplicationFactory at scale in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

At scale, Integration test WebApplicationFactory trades full pipeline tests against operational complexity. Primary failure mode: mock everything unit only.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Integration test WebApplicationFactory:**

**Strengths at scale:** Full pipeline tests

**Failure modes:**
- Misapplication when mock everything unit only
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** WAF with Testcontainers SQL

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Integration test WebApplicationFactory if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Integration test WebApplicationFactory — not just defined it.

### Follow-up Questions

1. **What monitoring proves Integration test WebApplicationFactory healthy? — SLI tied to waf with testcontainers sql.**
2. **When would you remove or replace Integration test WebApplicationFactory? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Integration test WebApplicationFactory as set-and-forget
- No load test before enabling Integration test WebApplicationFactory in production
- Ignoring cost/ops overhead of Integration test WebApplicationFactory

---

## Q091: Testcontainers for SQL — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Testing |
| **Frequency** | Common |

### Question

What are the advanced trade-offs and failure modes of Testcontainers for SQL at scale in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

At scale, Testcontainers for SQL trades realistic integration tests against operational complexity. Primary failure mode: in-memory ef only.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Testcontainers for SQL:**

**Strengths at scale:** Realistic integration tests

**Failure modes:**
- Misapplication when in-memory ef only
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** MsSql container in CI

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Testcontainers for SQL if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Testcontainers for SQL — not just defined it.

### Follow-up Questions

1. **What monitoring proves Testcontainers for SQL healthy? — SLI tied to mssql container in ci.**
2. **When would you remove or replace Testcontainers for SQL? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Testcontainers for SQL as set-and-forget
- No load test before enabling Testcontainers for SQL in production
- Ignoring cost/ops overhead of Testcontainers for SQL

---

## Q092: Roslyn analyzers in CI — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Quality |
| **Frequency** | Uncommon |

### Question

What are the advanced trade-offs and failure modes of Roslyn analyzers in CI at scale in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

At scale, Roslyn analyzers in CI trades enforce architecture rules against operational complexity. Primary failure mode: review-only conventions.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Roslyn analyzers in CI:**

**Strengths at scale:** Enforce architecture rules

**Failure modes:**
- Misapplication when review-only conventions
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** NetArchTest + analyzers fail build

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Roslyn analyzers in CI if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Roslyn analyzers in CI — not just defined it.

### Follow-up Questions

1. **What monitoring proves Roslyn analyzers in CI healthy? — SLI tied to netarchtest + analyzers fail build.**
2. **When would you remove or replace Roslyn analyzers in CI? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Roslyn analyzers in CI as set-and-forget
- No load test before enabling Roslyn analyzers in CI in production
- Ignoring cost/ops overhead of Roslyn analyzers in CI

---

## Q093: Central package management — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Build |
| **Frequency** | Common |

### Question

What are the advanced trade-offs and failure modes of Central package management at scale in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

At scale, Central package management trades consistent package versions against operational complexity. Primary failure mode: per-project drift.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Central package management:**

**Strengths at scale:** Consistent package versions

**Failure modes:**
- Misapplication when per-project drift
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** Directory.Packages.props

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Central package management if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Central package management — not just defined it.

### Follow-up Questions

1. **What monitoring proves Central package management healthy? — SLI tied to directory.packages.props.**
2. **When would you remove or replace Central package management? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Central package management as set-and-forget
- No load test before enabling Central package management in production
- Ignoring cost/ops overhead of Central package management

---

## Q094: NuGet vulnerability audit — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Security |
| **Frequency** | Uncommon |

### Question

What are the advanced trade-offs and failure modes of NuGet vulnerability audit at scale in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

At scale, NuGet vulnerability audit trades supply chain hygiene against operational complexity. Primary failure mode: ignore nu190 warnings.

### Detailed Answer (3–5 minutes)

**Advanced analysis of NuGet vulnerability audit:**

**Strengths at scale:** Supply chain hygiene

**Failure modes:**
- Misapplication when ignore nu190 warnings
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** Audit in CI gate

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose NuGet vulnerability audit if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated NuGet vulnerability audit — not just defined it.

### Follow-up Questions

1. **What monitoring proves NuGet vulnerability audit healthy? — SLI tied to audit in ci gate.**
2. **When would you remove or replace NuGet vulnerability audit? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating NuGet vulnerability audit as set-and-forget
- No load test before enabling NuGet vulnerability audit in production
- Ignoring cost/ops overhead of NuGet vulnerability audit

---

## Q095: Globalization invariant mode — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Deployment |
| **Frequency** | Common |

### Question

What are the advanced trade-offs and failure modes of Globalization invariant mode at scale in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

At scale, Globalization invariant mode trades container size wins against operational complexity. Primary failure mode: apps needing all cultures.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Globalization invariant mode:**

**Strengths at scale:** Container size wins

**Failure modes:**
- Misapplication when apps needing all cultures
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** InvariantGlobalization in slim images

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Globalization invariant mode if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Globalization invariant mode — not just defined it.

### Follow-up Questions

1. **What monitoring proves Globalization invariant mode healthy? — SLI tied to invariantglobalization in slim images.**
2. **When would you remove or replace Globalization invariant mode? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Globalization invariant mode as set-and-forget
- No load test before enabling Globalization invariant mode in production
- Ignoring cost/ops overhead of Globalization invariant mode

---

## Q096: Quartz.NET scheduling — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Background Jobs |
| **Frequency** | Uncommon |

### Question

What are the advanced trade-offs and failure modes of Quartz.NET scheduling at scale in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

At scale, Quartz.NET scheduling trades cron in .net against operational complexity. Primary failure mode: while(true) thread.sleep.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Quartz.NET scheduling:**

**Strengths at scale:** Cron in .NET

**Failure modes:**
- Misapplication when while(true) thread.sleep
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** Quartz hosted service cluster

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Quartz.NET scheduling if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Quartz.NET scheduling — not just defined it.

### Follow-up Questions

1. **What monitoring proves Quartz.NET scheduling healthy? — SLI tied to quartz hosted service cluster.**
2. **When would you remove or replace Quartz.NET scheduling? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Quartz.NET scheduling as set-and-forget
- No load test before enabling Quartz.NET scheduling in production
- Ignoring cost/ops overhead of Quartz.NET scheduling

---

## Q097: Hangfire vs native workers — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Background Jobs |
| **Frequency** | Common |

### Question

What are the advanced trade-offs and failure modes of Hangfire vs native workers at scale in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

At scale, Hangfire vs native workers trades dashboard job ops against operational complexity. Primary failure mode: hangfire for 2 jobs.

### Detailed Answer (3–5 minutes)

**Advanced analysis of Hangfire vs native workers:**

**Strengths at scale:** Dashboard job ops

**Failure modes:**
- Misapplication when hangfire for 2 jobs
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** IHostedService for simple queue drain

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose Hangfire vs native workers if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated Hangfire vs native workers — not just defined it.

### Follow-up Questions

1. **What monitoring proves Hangfire vs native workers healthy? — SLI tied to ihostedservice for simple queue drain.**
2. **When would you remove or replace Hangfire vs native workers? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating Hangfire vs native workers as set-and-forget
- No load test before enabling Hangfire vs native workers in production
- Ignoring cost/ops overhead of Hangfire vs native workers

---

## Q098: MassTransit on .NET — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Messaging |
| **Frequency** | Uncommon |

### Question

What are the advanced trade-offs and failure modes of MassTransit on .NET at scale in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

At scale, MassTransit on .NET trades abstracted messaging against operational complexity. Primary failure mode: raw sdk everywhere.

### Detailed Answer (3–5 minutes)

**Advanced analysis of MassTransit on .NET:**

**Strengths at scale:** Abstracted messaging

**Failure modes:**
- Misapplication when raw sdk everywhere
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** MassTransit + outbox pattern

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose MassTransit on .NET if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated MassTransit on .NET — not just defined it.

### Follow-up Questions

1. **What monitoring proves MassTransit on .NET healthy? — SLI tied to masstransit + outbox pattern.**
2. **When would you remove or replace MassTransit on .NET? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating MassTransit on .NET as set-and-forget
- No load test before enabling MassTransit on .NET in production
- Ignoring cost/ops overhead of MassTransit on .NET

---

## Q099: MediatR in minimal APIs — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Patterns |
| **Frequency** | Common |

### Question

What are the advanced trade-offs and failure modes of MediatR in minimal APIs at scale in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

At scale, MediatR in minimal APIs trades thin endpoints against operational complexity. Primary failure mode: fat minimal lambdas.

### Detailed Answer (3–5 minutes)

**Advanced analysis of MediatR in minimal APIs:**

**Strengths at scale:** Thin endpoints

**Failure modes:**
- Misapplication when fat minimal lambdas
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** Send command from MapPost

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose MediatR in minimal APIs if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated MediatR in minimal APIs — not just defined it.

### Follow-up Questions

1. **What monitoring proves MediatR in minimal APIs healthy? — SLI tied to send command from mappost.**
2. **When would you remove or replace MediatR in minimal APIs? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating MediatR in minimal APIs as set-and-forget
- No load test before enabling MediatR in minimal APIs in production
- Ignoring cost/ops overhead of MediatR in minimal APIs

---

## Q100: FluentValidation async rules — Advanced

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Validation |
| **Frequency** | Uncommon |

### Question

What are the advanced trade-offs and failure modes of FluentValidation async rules at scale in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

At scale, FluentValidation async rules trades remote validation against operational complexity. Primary failure mode: sync validation blocking.

### Detailed Answer (3–5 minutes)

**Advanced analysis of FluentValidation async rules:**

**Strengths at scale:** Remote validation

**Failure modes:**
- Misapplication when sync validation blocking
- Missing observability on the hot path
- Team skill gap operating the pattern

**Production reference:** MustAsync for uniqueness check

**Mitigations:**
- Load test at 2× expected peak before production
- Define rollback/feature-flag path
- Add dashboards for the metrics this concept affects

**Architecture review question:** Would we still choose FluentValidation async rules if traffic 10× or team shrinks 50%?

### Architecture Perspective

Advanced questions probe whether you have operated FluentValidation async rules — not just defined it.

### Follow-up Questions

1. **What monitoring proves FluentValidation async rules healthy? — SLI tied to mustasync for uniqueness check.**
2. **When would you remove or replace FluentValidation async rules? — Context change triggers ADR supersede.**

### Common Mistakes in Interviews

- Treating FluentValidation async rules as set-and-forget
- No load test before enabling FluentValidation async rules in production
- Ignoring cost/ops overhead of FluentValidation async rules

---
