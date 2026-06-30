# Compute Architecture Patterns

## Multi-Region App Service
- Traffic Manager or Front Door for global routing
- Active-active or active-passive
- Geo-replicated storage for state

## Container Apps vs AKS
| Factor | Container Apps | AKS |
|--------|-----------------|-----|
| Ops burden | Low | High |
| K8s features | Subset | Full |
| Scale to zero | Yes | HPA |
| Service mesh | Limited | Istio/Linkerd |

## .NET on Azure
- App Service: simplest .NET 8 deploy
- Container Apps: Docker + scale rules
- AKS: microservices at scale

## Architect Deep Dive: App Service & Functions Production

### Slot swap safe sequence
1. Deploy to staging slot
2. Run smoke + integration tests against staging URL
3. Warm-up ping `/health` (validates SQL, Redis)
4. Swap — monitor 5xx for 15 minutes
5. Rollback = swap back (instant)

### Functions architecture patterns
- **HTTP trigger** → thin API, delegate to service layer
- **Queue trigger** → async processing, idempotent handler
- **Durable Functions** → saga/orchestration without Service Bus choreography complexity for medium workflows

### VNet integration
App Service and Functions Premium integrate into spoke VNet for Private Link to SQL, Service Bus, and internal APIs — required for many enterprise security reviews.

