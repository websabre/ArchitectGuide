# Week 32 — Advanced Q&A

> Q071–Q100: Premium format (Week 1 quality).

---


## Q071: OpenTelemetry .NET SDK

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | OpenTelemetry |
| **Frequency** | Very Common |

### Question

How would you implement OpenTelemetry .NET SDK with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Add OTel to ASP.NET Core; auto-instrumentation; export to Azure Monitor via OTLP.

### Detailed Answer (3–5 minutes)

**OpenTelemetry .NET SDK** (Observability context)

Add OTel to ASP.NET Core; auto-instrumentation; export to Azure Monitor via OTLP.

**Production implementation:**
```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(t => t.AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation())
    .UseAzureMonitor();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

OpenTelemetry .NET SDK separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — OpenTelemetry-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q072: RED Metrics Method

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Metrics |
| **Frequency** | Very Common |

### Question

How would you implement RED Metrics Method with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Rate, Errors, Duration per service — dashboard template for each API.

### Detailed Answer (3–5 minutes)

**RED Metrics Method** (Observability context)

Rate, Errors, Duration per service — dashboard template for each API.

**Production implementation:**
```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(t => t.AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation())
    .UseAzureMonitor();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

RED Metrics Method separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Metrics-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q073: USE Metrics Infrastructure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Metrics |
| **Frequency** | Very Common |

### Question

How would you implement USE Metrics Infrastructure with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Utilization, Saturation, Errors for nodes, DB pools, queue depth.

### Detailed Answer (3–5 minutes)

**USE Metrics Infrastructure** (Observability context)

Utilization, Saturation, Errors for nodes, DB pools, queue depth.

**Production implementation:**
```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(t => t.AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation())
    .UseAzureMonitor();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

USE Metrics Infrastructure separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Metrics-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q074: Structured Logging Serilog

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Logging |
| **Frequency** | Very Common |

### Question

How would you implement Structured Logging Serilog with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

JSON logs with traceId, spanId, tenantId; sink to Log Analytics; no string concatenation.

### Detailed Answer (3–5 minutes)

**Structured Logging Serilog** (Observability context)

JSON logs with traceId, spanId, tenantId; sink to Log Analytics; no string concatenation.

**Production implementation:**
```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(t => t.AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation())
    .UseAzureMonitor();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Structured Logging Serilog separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Logging-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q075: Distributed Trace Propagation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Tracing |
| **Frequency** | Very Common |

### Question

How would you implement Distributed Trace Propagation with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

W3C tracecontext header across HTTP, Service Bus, background workers.

### Detailed Answer (3–5 minutes)

**Distributed Trace Propagation** (Observability context)

W3C tracecontext header across HTTP, Service Bus, background workers.

**Production implementation:**
```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(t => t.AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation())
    .UseAzureMonitor();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Distributed Trace Propagation separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Tracing-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q076: SLI SLO Definition

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | SLO |
| **Frequency** | Very Common |

### Question

How would you implement SLI SLO Definition with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

SLI: successful requests / total; SLO: 99.9% monthly; error budget policy documented.

### Detailed Answer (3–5 minutes)

**SLI SLO Definition** (Observability context)

SLI: successful requests / total; SLO: 99.9% monthly; error budget policy documented.

**Production implementation:**
```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(t => t.AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation())
    .UseAzureMonitor();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

SLI SLO Definition separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — SLO-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q077: Dashboard Design Hierarchy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Dashboards |
| **Frequency** | Very Common |

### Question

How would you implement Dashboard Design Hierarchy with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

L1 executive SLO; L2 service health; L3 diagnostic drill-down — avoid vanity metrics.

### Detailed Answer (3–5 minutes)

**Dashboard Design Hierarchy** (Observability context)

L1 executive SLO; L2 service health; L3 diagnostic drill-down — avoid vanity metrics.

**Production implementation:**
```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(t => t.AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation())
    .UseAzureMonitor();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Dashboard Design Hierarchy separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Dashboards-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q078: Alerting SLO Burn Rate

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Alerting |
| **Frequency** | Very Common |

### Question

How would you implement Alerting SLO Burn Rate with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Multi-window burn rate alerts; page on fast burn; ticket on slow burn.

### Detailed Answer (3–5 minutes)

**Alerting SLO Burn Rate** (Observability context)

Multi-window burn rate alerts; page on fast burn; ticket on slow burn.

**Production implementation:**
```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(t => t.AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation())
    .UseAzureMonitor();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Alerting SLO Burn Rate separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Alerting-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q079: Application Insights Sampling

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | App Insights |
| **Frequency** | Very Common |

### Question

How would you implement Application Insights Sampling with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Adaptive sampling in prod; 100% on errors; custom telemetry for business events always kept.

### Detailed Answer (3–5 minutes)

**Application Insights Sampling** (Observability context)

Adaptive sampling in prod; 100% on errors; custom telemetry for business events always kept.

**Production implementation:**
```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(t => t.AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation())
    .UseAzureMonitor();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Application Insights Sampling separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — App Insights-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q080: Metric Cardinality Control

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Metrics |
| **Frequency** | Very Common |

### Question

How would you implement Metric Cardinality Control with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Never label userId on metrics; use bounded labels; aggregate high-cardinality in logs.

### Detailed Answer (3–5 minutes)

**Metric Cardinality Control** (Observability context)

Never label userId on metrics; use bounded labels; aggregate high-cardinality in logs.

**Production implementation:**
```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(t => t.AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation())
    .UseAzureMonitor();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Metric Cardinality Control separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Metrics-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q081: Log Analytics KQL Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Logging |
| **Frequency** | Very Common |

### Question

How would you implement Log Analytics KQL Patterns with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

join traces to logs on operation_Id; parse JSON properties; summarize p99 by dependency.

### Detailed Answer (3–5 minutes)

**Log Analytics KQL Patterns** (Observability context)

join traces to logs on operation_Id; parse JSON properties; summarize p99 by dependency.

**Production implementation:**
```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(t => t.AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation())
    .UseAzureMonitor();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Log Analytics KQL Patterns separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Logging-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q082: Observability Cost Control

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | FinOps |
| **Frequency** | Very Common |

### Question

How would you implement Observability Cost Control with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Sampling, retention tiers, metric aggregation, drop debug in prod — budget alerts.

### Detailed Answer (3–5 minutes)

**Observability Cost Control** (Observability context)

Sampling, retention tiers, metric aggregation, drop debug in prod — budget alerts.

**Production implementation:**
```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(t => t.AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation())
    .UseAzureMonitor();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Observability Cost Control separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — FinOps-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q083: Service Map Dependency

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Tracing |
| **Frequency** | Very Common |

### Question

How would you implement Service Map Dependency with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

App Insights application map; identify sync call chains; async boundary gaps.

### Detailed Answer (3–5 minutes)

**Service Map Dependency** (Observability context)

App Insights application map; identify sync call chains; async boundary gaps.

**Production implementation:**
```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(t => t.AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation())
    .UseAzureMonitor();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Service Map Dependency separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Tracing-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q084: Custom Business Metrics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Metrics |
| **Frequency** | Very Common |

### Question

How would you implement Custom Business Metrics with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Track orders/min, payment failures — correlate with technical metrics in same dashboard.

### Detailed Answer (3–5 minutes)

**Custom Business Metrics** (Observability context)

Track orders/min, payment failures — correlate with technical metrics in same dashboard.

**Production implementation:**
```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(t => t.AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation())
    .UseAzureMonitor();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Custom Business Metrics separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Metrics-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q085: Health Check Endpoints

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Observability |
| **Frequency** | Very Common |

### Question

How would you implement Health Check Endpoints with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

/health/live vs /health/ready; include DB, cache, queue checks on ready only.

### Detailed Answer (3–5 minutes)

**Health Check Endpoints** (Observability context)

/health/live vs /health/ready; include DB, cache, queue checks on ready only.

**Production implementation:**
```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(t => t.AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation())
    .UseAzureMonitor();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Health Check Endpoints separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Observability-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q086: Correlation ID Middleware

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Logging |
| **Frequency** | Very Common |

### Question

How would you implement Correlation ID Middleware with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

.NET middleware injects traceId; propagate to HttpClient, Service Bus message properties.

### Detailed Answer (3–5 minutes)

**Correlation ID Middleware** (Observability context)

.NET middleware injects traceId; propagate to HttpClient, Service Bus message properties.

**Production implementation:**
```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(t => t.AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation())
    .UseAzureMonitor();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Correlation ID Middleware separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Logging-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q087: Alert Fatigue Reduction

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Alerting |
| **Frequency** | Very Common |

### Question

How would you implement Alert Fatigue Reduction with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Alert on symptoms (SLO burn) not causes (CPU 80%); runbook link required per alert.

### Detailed Answer (3–5 minutes)

**Alert Fatigue Reduction** (Observability context)

Alert on symptoms (SLO burn) not causes (CPU 80%); runbook link required per alert.

**Production implementation:**
```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(t => t.AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation())
    .UseAzureMonitor();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Alert Fatigue Reduction separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Alerting-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q088: Synthetic Monitoring

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Observability |
| **Frequency** | Very Common |

### Question

How would you implement Synthetic Monitoring with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Availability tests from 5 regions; critical journey every 5 min; alert before users notice.

### Detailed Answer (3–5 minutes)

**Synthetic Monitoring** (Observability context)

Availability tests from 5 regions; critical journey every 5 min; alert before users notice.

**Production implementation:**
```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(t => t.AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation())
    .UseAzureMonitor();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Synthetic Monitoring separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Observability-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q089: OpenTelemetry Collector

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | OpenTelemetry |
| **Frequency** | Very Common |

### Question

How would you implement OpenTelemetry Collector with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Collector sidecar in AKS; batch, filter, export to multiple backends.

### Detailed Answer (3–5 minutes)

**OpenTelemetry Collector** (Observability context)

Collector sidecar in AKS; batch, filter, export to multiple backends.

**Production implementation:**
```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(t => t.AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation())
    .UseAzureMonitor();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

OpenTelemetry Collector separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — OpenTelemetry-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q090: Exception Tracking Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | App Insights |
| **Frequency** | Very Common |

### Question

How would you implement Exception Tracking Strategy with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

TrackException with custom properties; group by outer message; link to release version.

### Detailed Answer (3–5 minutes)

**Exception Tracking Strategy** (Observability context)

TrackException with custom properties; group by outer message; link to release version.

**Production implementation:**
```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(t => t.AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation())
    .UseAzureMonitor();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Exception Tracking Strategy separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — App Insights-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q091: Live Metrics Debug

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | App Insights |
| **Frequency** | Common |

### Question

How would you implement Live Metrics Debug with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Live Metrics Stream for deploy validation; compare error rate pre/post swap.

### Detailed Answer (3–5 minutes)

**Live Metrics Debug** (Observability context)

Live Metrics Stream for deploy validation; compare error rate pre/post swap.

**Production implementation:**
```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(t => t.AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation())
    .UseAzureMonitor();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Live Metrics Debug separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — App Insights-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q092: Profiler On Demand

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | App Insights |
| **Frequency** | Common |

### Question

How would you implement Profiler On Demand with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Trigger snapshot profiler on high CPU alert; capture stack traces in production.

### Detailed Answer (3–5 minutes)

**Profiler On Demand** (Observability context)

Trigger snapshot profiler on high CPU alert; capture stack traces in production.

**Production implementation:**
```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(t => t.AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation())
    .UseAzureMonitor();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Profiler On Demand separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — App Insights-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q093: Observability Maturity Model

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Observability |
| **Frequency** | Common |

### Question

How would you implement Observability Maturity Model with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Level 1 uptime ping → Level 4 SLO-driven auto-rollback — assess and roadmap.

### Detailed Answer (3–5 minutes)

**Observability Maturity Model** (Observability context)

Level 1 uptime ping → Level 4 SLO-driven auto-rollback — assess and roadmap.

**Production implementation:**
```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(t => t.AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation())
    .UseAzureMonitor();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Observability Maturity Model separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Observability-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q094: Trace Sampling Tail

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Tracing |
| **Frequency** | Common |

### Question

How would you implement Trace Sampling Tail with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Tail-based sampling in collector — keep all errors, sample 1% success.

### Detailed Answer (3–5 minutes)

**Trace Sampling Tail** (Observability context)

Tail-based sampling in collector — keep all errors, sample 1% success.

**Production implementation:**
```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(t => t.AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation())
    .UseAzureMonitor();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Trace Sampling Tail separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Tracing-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q095: Log PII Redaction

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Logging |
| **Frequency** | Common |

### Question

How would you implement Log PII Redaction with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Serilog destructuring policy; never log card numbers; compliance scan on log fields.

### Detailed Answer (3–5 minutes)

**Log PII Redaction** (Observability context)

Serilog destructuring policy; never log card numbers; compliance scan on log fields.

**Production implementation:**
```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(t => t.AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation())
    .UseAzureMonitor();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Log PII Redaction separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Logging-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q096: Dashboard as Code

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Dashboards |
| **Frequency** | Common |

### Question

How would you implement Dashboard as Code with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Grafana/Azure Workbooks in Git; PR review for dashboard changes.

### Detailed Answer (3–5 minutes)

**Dashboard as Code** (Observability context)

Grafana/Azure Workbooks in Git; PR review for dashboard changes.

**Production implementation:**
```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(t => t.AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation())
    .UseAzureMonitor();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Dashboard as Code separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Dashboards-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q097: On-Call Runbook Integration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Alerting |
| **Frequency** | Common |

### Question

How would you implement On-Call Runbook Integration with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Alert links to runbook in wiki; auto-page includes last 5 deploys.

### Detailed Answer (3–5 minutes)

**On-Call Runbook Integration** (Observability context)

Alert links to runbook in wiki; auto-page includes last 5 deploys.

**Production implementation:**
```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(t => t.AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation())
    .UseAzureMonitor();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

On-Call Runbook Integration separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Alerting-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q098: Observability Testing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Observability |
| **Frequency** | Common |

### Question

How would you implement Observability Testing with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Chaos test verifies alerts fire; synthetic failure in staging monthly.

### Detailed Answer (3–5 minutes)

**Observability Testing** (Observability context)

Chaos test verifies alerts fire; synthetic failure in staging monthly.

**Production implementation:**
```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(t => t.AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation())
    .UseAzureMonitor();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Observability Testing separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Observability-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q099: Multi-Tenant Observability

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Observability |
| **Frequency** | Common |

### Question

How would you implement Multi-Tenant Observability with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

tenantId dimension on logs/traces; per-tenant SLO for enterprise tier.

### Detailed Answer (3–5 minutes)

**Multi-Tenant Observability** (Observability context)

tenantId dimension on logs/traces; per-tenant SLO for enterprise tier.

**Production implementation:**
```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(t => t.AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation())
    .UseAzureMonitor();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Multi-Tenant Observability separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Observability-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q100: Legacy App Instrumentation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Observability |
| **Frequency** | Common |

### Question

How would you implement Legacy App Instrumentation with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

OpenTelemetry auto-instrument without code change where possible; manual spans for critical paths.

### Detailed Answer (3–5 minutes)

**Legacy App Instrumentation** (Observability context)

OpenTelemetry auto-instrument without code change where possible; manual spans for critical paths.

**Production implementation:**
```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(t => t.AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation())
    .UseAzureMonitor();
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Legacy App Instrumentation separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Observability-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---
