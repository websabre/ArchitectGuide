#!/usr/bin/env python3
"""Generate missing lab files for weeks 4, 13, 16, 33-36, 41-52."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

LABS = {
    4: ("lab-04-pattern-refactoring.md", """# Lab 04: Refactor with Strategy and Factory Patterns

| **Week** | 04 | **Duration** | 120 min |

## Objectives

- [ ] Refactor switch-based shipping calculator to Strategy pattern
- [ ] Add new shipping method without modifying existing code (OCP)
- [ ] Write unit tests per strategy
- [ ] Document pattern choice in ADR

## Setup

```bash
dotnet new sln -n ShippingPatterns
dotnet new classlib -n Shipping.Domain -o src/Domain
dotnet new classlib -n Shipping.Application -o src/Application
dotnet new xunit -n Shipping.Tests -o tests/Tests
dotnet sln add src/* tests/Tests
dotnet add src/Application reference src/Domain
dotnet add tests/Tests reference src/Application
```

## Step 1: Legacy Code (Intentional Violation)

```csharp
public decimal Calculate(string method, Order order) => method switch
{
    "standard" => order.Weight * 0.5m,
    "express" => order.Weight * 1.2m + 10m,
    "overnight" => order.Weight * 2.0m + 25m,
    _ => throw new ArgumentException("Unknown method")
};
```

## Step 2: Strategy Interface

```csharp
public interface IShippingStrategy
{
    string Name { get; }
    decimal Calculate(Order order);
}
```

Implement `StandardShipping`, `ExpressShipping`, `OvernightShipping`.

## Step 3: Factory / DI Registration

```csharp
services.AddKeyed<IShippingStrategy>("standard", (sp, _) => new StandardShipping());
services.AddKeyed<IShippingStrategy>("express", (sp, _) => new ExpressShipping());
```

## Step 4: Add `InternationalShipping` Without Editing Switch

New class + DI registration only — proves OCP.

## Verification

- [ ] 4+ unit tests (one per strategy + factory resolution)
- [ ] No `switch` on shipping type in application layer
- [ ] ADR: Strategy vs Chain of Responsibility

## Lab Report

1. What would break if you added crypto payments to a switch-based payment service?
2. When is Strategy overkill?
3. Link to [Month 1 Top 50 Q031](../../../interview-prep/month-01-top-50-part3.md)

## Cleanup

Remove solution or archive in `~/labs/week-04/`.
"""),
    13: ("lab-13-hub-spoke-network.md", """# Lab 13: Azure Hub-Spoke Network with Private Link

| **Week** | 13 | **Duration** | 120 min | **Requires** | Azure subscription

## Objectives

- [ ] Deploy hub VNet with Azure Firewall subnet (or NSG-only for cost)
- [ ] Deploy spoke VNet peered to hub
- [ ] Deploy SQL with Private Endpoint in spoke
- [ ] Configure Private DNS zone for `privatelink.database.windows.net`

## Architecture

```mermaid
flowchart TB
    Hub[Hub VNet 10.0.0.0/16]
    Spoke[Spoke VNet 10.1.0.0/16]
    PE[Private Endpoint]
    SQL[(Azure SQL)]
    Hub -->|Peering| Spoke
    Spoke --> PE --> SQL
```

## Step 1: Hub VNet

```bash
az group create -n rg-net-lab-13 -l eastus
az network vnet create -g rg-net-lab-13 -n vnet-hub \\
  --address-prefix 10.0.0.0/16 \\
  --subnet-name AzureFirewallSubnet --subnet-prefix 10.0.1.0/26
az network vnet subnet create -g rg-net-lab-13 --vnet-name vnet-hub \\
  -n snet-shared --address-prefix 10.0.2.0/24
```

## Step 2: Spoke VNet + Peering

```bash
az network vnet create -g rg-net-lab-13 -n vnet-spoke-app \\
  --address-prefix 10.1.0.0/16 --subnet-name snet-app --subnet-prefix 10.1.1.0/24
az network vnet peering create -g rg-net-lab-13 -n hub-to-spoke \\
  --vnet-name vnet-hub --remote-vnet vnet-spoke-app --allow-vnet-access
az network vnet peering create -g rg-net-lab-13 -n spoke-to-hub \\
  --vnet-name vnet-spoke-app --remote-vnet vnet-hub --allow-vnet-access
```

## Step 3: SQL + Private Endpoint

```bash
az sql server create -g rg-net-lab-13 -n sql-lab-13-$RANDOM \\
  -l eastus -u sqladmin -p 'ComplexP@ssw0rd!' 
az sql db create -g rg-net-lab-13 -s sql-lab-13-* -n ordersdb --service-objective S0
# Create private endpoint in snet-app (see Azure Portal or Bicep module)
```

## Step 4: Private DNS

Link private DNS zone `privatelink.database.windows.net` to spoke VNet. Verify `nslookup sql-lab-13.database.windows.net` resolves to private IP from jump box in spoke.

## Lab Report

1. Service Endpoint vs Private Link — which did you use and why?
2. Draw traffic flow: App in spoke → SQL
3. Hub-spoke vs single VNet for 3 teams

## Cleanup

```bash
az group delete -n rg-net-lab-13 --yes --no-wait
```
"""),
    16: ("lab-16-azure-production-capstone.md", """# Lab 16: Azure Production Architecture Capstone

| **Week** | 16 | **Duration** | 8–12 hours (spread across week) |

## Capstone Brief

Design and document a **production-grade multi-tier SaaS** on Azure. This integrates Weeks 9–15: landing zone, compute, data, identity, networking, security, and messaging.

**Deliverable:** Architecture package (not full implementation) suitable for executive review.

## Requirements

| NFR | Target |
|-----|--------|
| Availability | 99.95% |
| Users | 50K MAU, 2K peak concurrent |
| Tenancy | Multi-tenant B2B SaaS |
| Compliance | SOC 2 ready (encryption, audit logs) |
| RPO / RTO | 1 hour / 4 hours |

## Deliverables Checklist

- [ ] C4 Context diagram
- [ ] C4 Container diagram
- [ ] Hub-spoke or simplified network diagram
- [ ] Identity flow (Entra ID + MI + Key Vault)
- [ ] Data platform choice (SQL vs Cosmos) with ADR
- [ ] Integration pattern (Service Bus or Event Grid) for async workflows
- [ ] Security controls mapped to WAF pillars
- [ ] Cost estimate (order of magnitude, monthly USD)
- [ ] DR runbook outline (1 page)
- [ ] 3 failure scenarios + mitigations

## Suggested Azure Services

- App Service (or AKS if justified in ADR)
- Azure SQL or Cosmos DB
- Service Bus
- Application Gateway or Front Door
- Key Vault, App Configuration
- Application Insights + Log Analytics
- Entra ID app registration

## Presentation (30 min)

1. Problem & tenants (5 min)
2. Architecture walkthrough (15 min)
3. Trade-offs & ADRs (7 min)
4. Roadmap if 6 more months (3 min)

## Rubric

| Criteria | Points |
|----------|--------|
| Requirements coverage | 20 |
| Architecture quality | 25 |
| Security & identity | 20 |
| Operability (observability, DR) | 20 |
| Documentation & ADRs | 15 |

**Pass:** ≥ 70/100

← [Month 4 capstone](../../program/phase-04-month-04/capstone.md)
"""),
    33: ("lab-33-whiteboard-url-shortener.md", """# Lab 33: Whiteboard — URL Shortener (Timed)

| **Week** | 33 | **Duration** | 45 min (strict timer) |

## Exercise

Design a URL shortener: 100M URLs, 10K writes/sec, 100K reads/sec. Use [RESHADED](../../../interview-prep/whiteboard/README.md).

## Timer Blocks

| Block | Min | Task |
|-------|-----|------|
| Requirements | 5 | Custom aliases, TTL, analytics |
| Estimation | 5 | Storage, QPS, cache size |
| High-level | 10 | API, DB, cache, redirect flow |
| Deep dive | 15 | Cache strategy + ID generation |
| Failure/scale | 10 | Hot URL, DB down |

## Self-Score Rubric

| Criteria | /25 |
|----------|-----|
| Requirements | |
| Estimation | |
| Design | |
| Deep dive | |

**Target:** ≥ 75/100

## After Action

- [ ] Compare with [mock-02 URL shortener](../../../interview-prep/mock-interviews/mock-02-system-design-url-shortener.md)
- [ ] Record weak areas in [progress tracker](../../../templates/progress-tracker.md)
"""),
    34: ("lab-34-caching-redis.md", """# Lab 34: Caching Layer with Redis (.NET)

| **Week** | 34 | **Duration** | 90 min |

## Objectives

- [ ] Implement cache-aside pattern for product catalog API
- [ ] Configure TTL and cache stampede mitigation
- [ ] Measure hit ratio with metrics

## Setup

```bash
docker run -d -p 6379:6379 redis:7-alpine
dotnet new webapi -n CacheLab
dotnet add package Microsoft.Extensions.Caching.StackExchangeRedis
dotnet add package StackExchange.Redis
```

## Cache-Aside Pattern

```csharp
public async Task<Product?> GetAsync(string id, CancellationToken ct)
{
    var cached = await _cache.GetStringAsync($"product:{id}", ct);
    if (cached != null) return JsonSerializer.Deserialize<Product>(cached);

    var product = await _db.Products.FindAsync(id);
    if (product != null)
        await _cache.SetStringAsync($"product:{id}", JsonSerializer.Serialize(product),
            new DistributedCacheEntryOptions { AbsoluteExpirationRelativeToNow = TimeSpan.FromMinutes(5) }, ct);
    return product;
}
```

## Stampede Mitigation

Use `HybridCache` (.NET 9) or lock per key for popular product refresh.

## Load Test

```bash
# Use bombardier or k6 — compare with cache disabled vs enabled
```

## Report

1. Cache hit ratio achieved?
2. When would you use write-through instead?
3. CDN vs Redis for this workload
"""),
    35: ("lab-35-outbox-pattern.md", """# Lab 35: Transactional Outbox Pattern

| **Week** | 35 | **Duration** | 120 min |

## Objectives

- [ ] Implement outbox table in EF Core
- [ ] Background worker publishes to message bus
- [ ] Verify atomic order create + event publish

## Schema

```csharp
public class OutboxMessage
{
    public Guid Id { get; set; }
    public string Type { get; set; } = "";
    public string Payload { get; set; } = "";
    public DateTime CreatedAt { get; set; }
    public DateTime? ProcessedAt { get; set; }
}
```

## Flow

1. `SaveChanges` writes Order + OutboxMessage in same transaction
2. `OutboxProcessor` polls unprocessed messages
3. Publish to Service Bus / in-memory queue for lab
4. Mark `ProcessedAt`

## Chaos Test

Kill publisher mid-batch — messages must not duplicate on retry (use message Id dedup).

## Report

1. Outbox vs dual-write — why outbox wins
2. Polling vs log-based (Debezium) outbox
3. Link to [Week 15 messaging theory](../theory/01-fundamentals.md)
"""),
    36: ("lab-36-system-design-capstone.md", """# Lab 36: System Design Capstone — E-Commerce Platform

| **Week** | 36 | **Duration** | 6–8 hours |

## Brief

Whiteboard + document a high-traffic e-commerce platform: catalog, cart, checkout, payments, notifications.

## Scale

- 5K orders/minute peak
- 10M products
- 99.9% availability target

## Required Diagrams

1. High-level components
2. Checkout sequence (sync + async)
3. Data stores per bounded context

## Required ADRs (minimum 3)

- SQL vs NoSQL per service
- Saga orchestration vs choreography
- Cache strategy

## Failure Scenarios

Document mitigations for:
- Payment timeout after inventory reserved
- Double-click on Pay button
- Hot product crashing cache

## Self-Assessment

| Mock | Score | Pass? |
|------|-------|-------|
| [Checkout mock](../../../interview-prep/mock-interviews/mock-05-system-design-checkout.md) | /100 | |

← [Month 9 capstone](../../program/phase-09-month-09/capstone.md)
"""),
}

# Weeks 41-52: interview and enterprise labs
for week, (title, brief, steps) in [
    (41, ("ADR Workshop", "Write 3 ADRs for a legacy modernization proposal.",
          ["Pick legacy monolith scenario from case study", "ADR-001: Strangler vs rewrite", "ADR-002: Data migration", "ADR-003: Identity migration", "Peer review with rubric"])),
    (42, ("FinOps Cost Model", "Build cost model spreadsheet for Azure workload.",
          ["List all resources with SKUs", "Estimate monthly cost at 10K and 100K users", "Identify top 3 cost drivers", "Propose 3 optimizations with savings %", "Present to mock CFO in 5 min"])),
    (43, ("BFF vs Micro-Frontend", "Design API layer for React + Angular clients.",
          ["Draw BFF per client type", "Document GraphQL vs REST trade-off", "Auth token flow SPA → BFF → API", "CORS and CSP checklist"])),
    (44, ("Case Study Review", "Complete architecture review for CS44-A healthcare case.",
          ["Read case study in case-studies/", "Score against WAF pillars", "Write 5 findings + recommendations", "Present 15-min review"])),
    (45, ("Technical Drill", "60-min timed Q&A from Month 1 Top 50.",
          ["Random 20 questions from Top 50", "Record answers on phone", "Self-score ≥70%", "Log weak topics"])),
    (46, ("Cloud Comparison Lab", "Map same workload to Azure and AWS side-by-side.",
          ["Draw both diagrams", "Comparison table 15 services", "ADR: primary cloud", "Migration path outline"])),
    (47, ("System Design Drill", "45-min checkout design timed.",
          ["Use RESHADED", "Self-score with rubric", "Compare mock-05 solution"])),
    (48, ("Whiteboard Marathon 1", "3 designs × 45 min: chat, feed, notifications.",
          ["No breaks between designs", "Self-score each", "Identify slowest section"])),
    (49, ("Whiteboard Marathon 2", "3 designs × 45 min: multi-tenant, migration, rate limiter.",
          ["Focus on estimation speed", "Document assumptions"])),
    (50, ("STAR Story Writing", "Write and rehearse 5 behavioral stories.",
          ["Technical leadership", "Conflict", "Failure", "Executive comms", "Cost optimization", "Record 3-min each"])),
    (51, ("STAR Refinement", "Polish 10 stories with metrics in Results.",
          ["Peer review", "Remove 'we' without 'I'", "Add numbers to every Result"])),
    (52, ("Graduation Panel Mock", "Full 3-round panel mock.",
          ["mock-06-panel-loop.md", "Portfolio walkthrough", "Feedback log", "Graduation checklist"])),
]:
    slug = title.lower().replace(" ", "-").replace("+", "plus")
    step_md = "\n".join(f"{i+1}. {s}" for i, s in enumerate(steps))
    LABS[week] = (f"lab-{week:02d}-{slug}.md", f"""# Lab {week:02d}: {title}

| **Week** | {week:02d} | **Duration** | See steps |

## Objectives

{brief}

## Steps

{step_md}

## Deliverables

- [ ] Completed exercises documented in personal notes or portfolio
- [ ] Weak areas logged in [progress tracker](../../../templates/progress-tracker.md)

## Related

- [Week {week:02d} theory](../theory/README.md)
- [Interview prep](../../../interview-prep/README.md)
""")


def update_lab_readme(week: int, lab_file: str):
    readme = ROOT / f"weeks/week-{week:02d}/labs/README.md"
    if not readme.exists():
        return
    text = readme.read_text(encoding="utf-8")
    if lab_file in text:
        return
    text = text.replace(
        "*Lab content coming soon.*",
        f"- [{lab_file}]({lab_file})",
    )
    if lab_file not in text:
        text = text.replace(
            "## Hands-on Labs\n",
            f"## Hands-on Labs\n\n- [{lab_file}]({lab_file})\n",
        )
    readme.write_text(text, encoding="utf-8")


def main():
    for week, (filename, content) in LABS.items():
        lab_dir = ROOT / f"weeks/week-{week:02d}/labs"
        lab_dir.mkdir(parents=True, exist_ok=True)
        path = lab_dir / filename
        path.write_text(content.strip() + "\n", encoding="utf-8")
        update_lab_readme(week, filename)
        print(f"Wrote {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
