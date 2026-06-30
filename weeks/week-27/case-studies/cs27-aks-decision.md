# Case Study: Monolith to AKS Migration

| **Week** | 25-27 | **Difficulty** | Advanced |

## Context
.NET monolith on App Service. Team containerized app. Leadership wants AKS for "cloud native." 8 microservices planned, 12 developers, limited K8s experience.

## Your Task
Recommend container strategy: App Service containers vs AKS vs Container Apps.

## Reference Solution

| Option | Verdict |
|--------|---------|
| App Service for Linux containers | Good interim — minimal change |
| Container Apps | **Recommended** — containers + scale-to-zero + lower ops than AKS |
| AKS | Defer until 15+ services, K8s-skilled platform team |

**Migration path:**
1. Month 1-2: Dockerize all services, run on App Service containers
2. Month 3-4: Move to Container Apps with Dapr for service invocation
3. Month 6+: Evaluate AKS if service mesh, GitOps at scale needed

**Risk of premature AKS:** Platform team of 0, 6-month productivity loss.

## Interview Angle
"Pushed back on AKS, proposed Container Apps, saved 2 platform engineer hires."
