# Azure Compute Options

## Decision Matrix
| Service | Best For | Avoid When |
|---------|----------|------------|
| **App Service** | Web APIs, standard hosting | Need K8s features |
| **Functions** | Event-driven, sporadic load | Long-running HTTP |
| **Container Apps** | Containers without K8s ops | Complex service mesh |
| **AKS** | Full Kubernetes | Small team, simple app |
| **VMs** | Full control, legacy | Want managed PaaS |

## App Service Tiers
| Tier | Use Case |
|------|----------|
| Free/Shared | Dev/test only |
| Basic | Low-traffic production |
| Standard | Production with autoscale |
| Premium | High perf, VNet integration |
| Isolated | Dedicated hardware, compliance |

## App Service Features
- Deployment slots (blue-green)
- Autoscale rules
- VNet integration
- Managed identity
- Custom domains + SSL

## Azure Functions
- Consumption plan (serverless)
- Premium plan (pre-warmed, VNet)
- Durable Functions for workflows

## Architect Deep Dive: Compute Selection

### Decision workflow
1. **Latency & scale pattern** — steady HTTP vs event bursts vs long-running
2. **Team ops capacity** — can they run K8s control plane?
3. **Compliance** — VNet isolation, dedicated hardware (Isolated tier)
4. **Cost model** — always-on vs consumption

### .NET workload mapping
| Pattern | First choice | Escalation path |
|---------|--------------|-----------------|
| REST API, predictable load | App Service Standard+ | Premium + autoscale |
| Sporadic events | Azure Functions Premium | Durable Functions workflows |
| Containerized, no K8s team | Container Apps | AKS when mesh/GitOps needed |
| Legacy .NET Framework | VM or App Service Windows | Containerize later |

### App Service production checklist
- [ ] Deployment slots + health check path hits DB/cache
- [ ] Managed Identity to Key Vault and SQL
- [ ] Autoscale on CPU **and** HTTP queue length
- [ ] Always On disabled only on non-prod cost saves
- [ ] ARR affinity off unless session state requires it

### Anti-pattern
Running AKS for a single stateless API because "it's cloud native" — 2 platform engineers worth of ops for no architectural benefit.

