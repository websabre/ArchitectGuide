# Observability & PowerShell Automation

> **Week 32** | **Module:** [observability](../../../modules/observability/README.md)

## Learning Objectives
- Implement logs, metrics, traces (three pillars)
- Design SLIs, SLOs, and error budgets
- Automate Azure operations with PowerShell

---

## 1. Three Pillars of Observability

| Pillar | Question | Tools |
|--------|----------|-------|
| **Logs** | What happened? | App Insights, CloudWatch, ELK |
| **Metrics** | How much/how fast? | Prometheus, Azure Monitor |
| **Traces** | Where did time go? | OpenTelemetry, Jaeger, X-Ray |

**Fourth pillar (argued):** Profiling — why is code slow?

---

## 2. OpenTelemetry for .NET

```csharp
builder.Services.AddOpenTelemetry()
    .WithTracing(tracing => tracing
        .AddAspNetCoreInstrumentation()
        .AddHttpClientInstrumentation()
        .AddEntityFrameworkCoreInstrumentation()
        .AddAzureMonitorTraceExporter())
    .WithMetrics(metrics => metrics
        .AddAspNetCoreInstrumentation()
        .AddAzureMonitorMetricExporter());
```

**Architect mandate:** Every microservice exports OTel. Correlation ID in every log line.

---

## 3. SLIs, SLOs, Error Budgets

| Term | Definition | Example |
|------|------------|---------|
| **SLI** | Measurable indicator | p99 latency, availability % |
| **SLO** | Target for SLI | 99.9% availability, p99 < 200ms |
| **SLA** | Contract with penalties | 99.95% or credits |
| **Error budget** | Allowed failure | 0.1% = 43 min downtime/month |

**Architect:** If error budget exhausted → freeze features, focus reliability.

---

## 4. Structured Logging

```csharp
_logger.LogInformation("Order {OrderId} placed by {CustomerId} for {Total}",
    order.Id, order.CustomerId, order.Total);
```

**Anti-pattern:** `_logger.LogInformation($"Order {order.Id}")` — breaks structured query.

**Log levels:** Error (action needed), Warning (investigate), Information (business events), Debug (dev only).

---

## 5. Dashboards & Alerting

| Alert | Condition | Action |
|-------|-----------|--------|
| High error rate | 5xx > 1% for 5 min | Page on-call |
| Latency | p99 > 500ms for 10 min | Investigate |
| Saturation | CPU > 80% sustained | Scale out |

**Alert fatigue:** Alert on symptoms users feel, not every threshold breach.

---

## 6. PowerShell for Azure Architects

```powershell
# Connect
Connect-AzAccount
Set-AzContext -Subscription "Production"

# List resources by tag
Get-AzResource -Tag @{ Environment = "Production" } |
  Group-Object ResourceType |
  Select-Object Name, Count

# Cost by resource group
Get-AzConsumptionUsageDetail -StartDate (Get-Date).AddDays(-30) |
  Group-Object ResourceGroup |
  Select-Object Name, @{N='Cost';E={($_.Group | Measure-Object PretaxCost -Sum).Sum}}

# Restart app service (incident response)
Restart-AzWebApp -ResourceGroupName "rg-prod" -Name "order-api"
```

**Use cases:** FinOps reports, incident response, bulk tagging, compliance audits, environment provisioning scripts.

---

## 7. PowerShell vs Bash vs Azure CLI

| Task | Recommended |
|------|-------------|
| Azure automation (Windows shop) | PowerShell Az module |
| CI/CD on Linux agents | Azure CLI / Bash |
| AKS troubleshooting | kubectl + Bash |
| Complex Azure reporting | PowerShell |

**Next:** [labs/](../labs/)
