# Week 09 — Azure Fundamentals & WAF Diagrams

## 1. Well-Architected Pillars

```mermaid
flowchart TB
    WAF[Azure WAF] --> R[Reliability]
    WAF --> S[Security]
    WAF --> CO[Cost Optimization]
    WAF --> OP[Operational Excellence]
    WAF --> P[Performance Efficiency]
```

## 2. Landing Zone — Management Groups

```mermaid
flowchart TD
    MG[Management Group Root] --> Prod[Production]
    MG --> NonProd[Non-Production]
    Prod --> SubProd[Subscription: Prod Workloads]
    NonProd --> SubDev[Subscription: Dev/Test]
```

## 3. Hub-Spoke (Intro)

```mermaid
flowchart TB
    Hub[Hub VNet - Firewall VPN] --> Spoke1[Spoke: App]
    Hub --> Spoke2[Spoke: Data]
```

## 4. .NET App on Azure — Baseline

```mermaid
flowchart LR
    User --> FD[Front Door]
    FD --> App[App Service]
    App --> MI[Managed Identity]
    MI --> SQL[(Azure SQL)]
    App --> AI[App Insights]
```

## 5. Resilience — Availability Zones

```mermaid
flowchart TB
    subgraph Region["Azure Region"]
        Z1[Zone 1]
        Z2[Zone 2]
        Z3[Zone 3]
    end
    LB[Load Balancer] --> Z1
    LB --> Z2
    LB --> Z3
```

> **Architect note:** Zone-redundant ≠ region-redundant. Document RTO/RPO per tier.

## Practice Exercise

Sketch a 3-subscription landing zone for a 50-person startup scaling to enterprise.

---

[← Back to Week 09](../README.md)
