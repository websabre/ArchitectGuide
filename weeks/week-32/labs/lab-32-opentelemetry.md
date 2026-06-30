# Lab 32 — OpenTelemetry + Azure Monitor

**Duration:** 2–3 hours

## Objectives
- Instrument ASP.NET Core with OpenTelemetry
- View distributed traces in Application Insights
- Create alert on error rate SLO breach

## Setup

```csharp
builder.Services.AddOpenTelemetry()
    .ConfigureResource(r => r.AddService("order-api"))
    .WithTracing(t => t
        .AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation()
        .AddSqlClientInstrumentation()
        .AddAzureMonitorTraceExporter())
    .WithMetrics(m => m
        .AddAspNetCoreInstrumentation()
        .AddAzureMonitorMetricExporter());
```

## Exercises
1. Make cross-service call; verify single trace ID in App Insights
2. Add custom span around payment processing
3. Create workbook: p50/p95/p99 latency by endpoint
4. Alert: 5xx rate > 1% for 5 minutes

## PowerShell Bonus

```powershell
# Query recent failures
$query = 'exceptions | where timestamp > ago(1h) | summarize count() by problemId'
Invoke-AzOperationalInsightsQuery -WorkspaceId $wsId -Query $query
```

## Deliverables
- [ ] Traces visible end-to-end
- [ ] Custom metric `orders.placed` emitted
- [ ] Runbook for high-error-rate alert
