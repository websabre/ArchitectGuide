# Week 10 — Intermediate Q&A

> Q001–Q050: Premium format (Week 1 quality).  
> **Topic:** Azure Compute & App Services | **Count:** 50

---


## Q001: App Service vs Azure Functions

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Very Common |

### Question

When App Service vs Functions for .NET HTTP API?

### Short Answer (30 seconds)

App Service: always-on APIs, WebSockets, long requests, predictable traffic. Functions: event-driven, spiky, short-lived, pay-per-execution.

### Detailed Answer (3–5 minutes)

**App Service:** full ASP.NET Core, deployment slots, Always On, VNet integration.

**Functions:** trigger-based (HTTP, Queue, Timer), consumption plan cold starts, Premium plan for pre-warmed.

**Architect:** Default App Service for primary REST API; Functions for async processors and webhooks.

### Architecture Perspective

Compute choice drives ops model and cost profile.

### Follow-up Questions

1. **Container Apps vs App Service? — Microservices with scale-to-zero — Container Apps.**
2. **Premium Functions plan? — When cold start unacceptable.**

### Common Mistakes in Interviews

- Functions for main CRUD API with steady traffic
- App Service Consumption tier confusion
- Ignoring cold start on user-facing HTTP

---

## Q002: AKS vs App Service Decision

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Very Common |

### Question

Team wants Kubernetes. You have 3 microservices and 4 developers. Recommendation?

### Short Answer (30 seconds)

App Service or Container Apps first — AKS when team has K8s ops skill, 10+ services, or need portable K8s APIs. AKS ops burden real for small teams.

### Detailed Answer (3–5 minutes)

**AKS when:** custom networking, service mesh, multi-cloud K8s, GPU workloads.

**App Service when:** .NET APIs, fast path to prod, built-in slots and autoscale.

**Architect:** Honest TCO — AKS needs platform team or managed add-ons (Istio, monitoring).

### Architecture Perspective

Right-sizing platform complexity is core architect judgment.

### Follow-up Questions

1. **AKS Automatic? — Reduced ops for node management — evaluate preview/GA status.**
2. **Web App for Containers? — Middle ground — containers without full K8s.**

### Common Mistakes in Interviews

- AKS for resume on 3-service system
- No observability plan for K8s
- Ignoring control plane cost

---

## Q003: Deployment Slots

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DevOps |
| **Frequency** | Very Common |

### Question

Explain App Service deployment slots for zero-downtime release.

### Short Answer (30 seconds)

Staging slot runs new version; warm up; swap with production — instant traffic flip. Rollback = swap back.

### Detailed Answer (3–5 minutes)

**Best practices:**
- Slot settings sticky (connection strings per slot)
- Run smoke tests on staging
- Auto-swap with webhook on CI success

**Architect:** Slots cheaper than blue/green second App Service. Pair with feature flags for release decoupling.

### Architecture Perspective

Slots are Azure PaaS advantage architects should mandate.

### Follow-up Questions

1. **Slot swap what travels? — Content swaps; some settings sticky per config.**
2. **Database migration with slot? — Backward-compatible migrations only during swap.**

### Common Mistakes in Interviews

- Deploy direct to production
- Swap without staging warm-up
- Breaking schema change during swap

---

## Q004: Autoscale Rules for App Service

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Scale |
| **Frequency** | Common |

### Question

Configure autoscale for .NET API — what metrics?

### Short Answer (30 seconds)

Scale on CPU > 70%, HTTP queue length, or custom App Insights metric (requests/sec). Scale-in cooldown 5+ min to prevent flapping.

### Detailed Answer (3–5 minutes)

**Example:** Min 2 instances prod (HA), max 10, scale out +1 when CPU > 70% for 5 min.

**Architect:** Load test to find saturation point — don't scale on CPU alone if I/O bound.

### Architecture Perspective

Autoscale policy is architecture not just ops config.

### Follow-up Questions

1. **Schedule-based scale? — Scale up before business hours — predictable traffic.**
2. **Per-instance connection limits? — Scale before connection exhaustion.**

### Common Mistakes in Interviews

- Min 1 instance production HA
- Instant scale-in on brief CPU dip
- No load test before max instance setting

---

## Q005: Azure Functions Cold Start

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Serverless |
| **Frequency** | Common |

### Question

Mitigate cold start for latency-sensitive Functions?

### Short Answer (30 seconds)

Premium plan with pre-warmed instances, always-ready instances count > 0, minimize assembly size, Native AOT where supported, avoid huge DI graph.

### Detailed Answer (3–5 minutes)

**Consumption plan:** cold start 1-10+ seconds .NET — unacceptable for sync user API.

**Architect:** Profile with Application Insights dependency tracking. Consider minimum instances on Premium or move to App Service.

### Architecture Perspective

Cold start is common Functions interview topic.

### Follow-up Questions

1. **Durable Functions cold start? — Orchestrator replay — separate consideration.**
2. **Place function in VNet? — Premium required — adds cold start complexity.**

### Common Mistakes in Interviews

- Consumption plan for checkout API
- Ignore startup trace in App Insights
- 500MB deployment package

---

## Q006: Container Apps on Azure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Containers |
| **Frequency** | Common |

### Question

When Azure Container Apps vs AKS?

### Short Answer (30 seconds)

Container Apps: serverless containers, KEDA scale, simpler ops, internal ingress. AKS: full K8s control, service mesh, complex networking.

### Detailed Answer (3–5 minutes)

**Container Apps:** microservices with scale-to-zero, Dapr built-in, revision management.

**Architect:** Container Apps for team without K8s expertise; AKS when need full Kubernetes API.

### Architecture Perspective

Container Apps fills gap between App Service and AKS.

### Follow-up Questions

1. **Dapr sidecar? — Service invocation, pub/sub, state — reduces custom glue code.**
2. **Consumption vs dedicated? — Dedicated for predictable performance isolation.**

### Common Mistakes in Interviews

- AKS for 2 container microservices
- No revision management strategy
- Public ingress without WAF

---

## Q007: App Service VNet Integration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

Why integrate App Service with VNet?

### Short Answer (30 seconds)

Reach private resources: SQL with private endpoint, internal APIs, on-prem via ExpressRoute. Outbound traffic through VNet for network isolation.

### Detailed Answer (3–5 minutes)

**Regional VNet Integration:** outbound to VNet. **Private Endpoint:** inbound to App Service.

**Architect:** Production APIs accessing private SQL must use VNet integration + private DNS zones.

### Architecture Perspective

Networking integration is production App Service requirement.

### Follow-up Questions

1. **DNS resolution in VNet? — Azure DNS private resolver or custom DNS.**
2. **NSG on integration subnet? — Required for App Service outbound.**

### Common Mistakes in Interviews

- Public SQL connection string from App Service prod
- Forget private DNS for private endpoint
- All traffic public internet

---

## Q008: Managed Identity for App Service

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Very Common |

### Question

Connect App Service to Key Vault and SQL without secrets?

### Short Answer (30 seconds)

Enable system-assigned managed identity on App Service. Grant MI access to Key Vault (RBAC) and SQL (Entra auth). Reference secrets via Key Vault references in app settings.

### Detailed Answer (3–5 minutes)

**No secrets in appsettings.json in repo.** CI/CD uses federated credential OIDC — not SP password.

**Architect:** Standard template for all App Services in platform.

### Architecture Perspective

Managed identity is non-negotiable for modern Azure apps.

### Follow-up Questions

1. **User-assigned vs system-assigned? — User-assigned shared across slots/resources.**
2. **DefaultAzureCredential chain? — Local dev uses VS credentials; prod uses MI.**

### Common Mistakes in Interviews

- Connection string with SQL password in config
- SP client secret in GitHub Actions
- MI without RBAC on Key Vault

---

## Q009: App Service Plan Sizing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Cost |
| **Frequency** | Common |

### Question

Choose App Service Plan SKU for 2K RPS .NET API?

### Short Answer (30 seconds)

Load test first. Start P1v3 (2 cores) × 2 instances, scale out. Premium v3 for deployment slots and autoscale. Isolated only for compliance isolation needs.

### Detailed Answer (3–5 minutes)

**Tiers:** Free/Shared dev only. Basic no slots. Standard slots. Premium v3 zone balance + autoscale.

**Architect:** Right-size with load test — P2v3 vs P1v3 × 2 often similar cost, better HA.

### Architecture Perspective

SKU choice affects SLA and features — not just CPU.

### Follow-up Questions

1. **Linux vs Windows plan? — .NET 8 Linux often preferred cost/perf.**
2. **Reserved instances on ASP? — 1-3 year commit for stable baseline.**

### Common Mistakes in Interviews

- Premium for dev environment waste
- Single instance production
- No load test before SKU selection

---

## Q010: Multi-Region App Service

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reliability |
| **Frequency** | Common |

### Question

Design multi-region active-active for App Service API.

### Short Answer (30 seconds)

Front Door or Traffic Manager → regional App Services. Session state external (Redis). SQL geo-replication or Cosmos multi-region. Health probes per region.

### Detailed Answer (3–5 minutes)

**Challenges:** Data consistency across regions, deployment coordination, config drift.

**Architect:** Active-passive simpler for relational data; active-active for read-heavy stateless APIs.

### Architecture Perspective

Multi-region is reliability architecture with data trade-offs.

### Follow-up Questions

1. **Front Door vs Traffic Manager? — Front Door L7 + WAF; TM DNS-level.**
2. **Sticky sessions multi-region? — Prefer external session store.**

### Common Mistakes in Interviews

- Active-active without data strategy
- Deploy regions manually divergent
- No health probe on Front Door

---

## Q011: App Service Plans SKUs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Very Common |

### Question

Compare App Service Plan SKUs and select for production .NET API.

### Short Answer (30 seconds)

Free/Shared dev only. Basic: no slots. Standard: slots, autoscale. Premium v3: zone balance, better CPU, VNet. Isolated v2: dedicated hardware for compliance isolation.

### Detailed Answer (3–5 minutes)

**SKU tiers:**
| Tier | Slots | Autoscale | Zone | Use |
|------|-------|-----------|------|-----|
| B1+ | No | Manual | No | Dev/test |
| S1+ | Yes | Yes | No | Small prod |
| P1v3+ | Yes | Yes | Yes | Production |
| I1v2 | Yes | Yes | Yes | Isolated compliance |

**Architect:** Start P1v3 × 2 instances for HA. Load test before P2v3 vs scale-out. Linux plans often better price/perf for .NET 8.

**Reserved instances:** 1-3 year commit on ASP for FinOps savings.

### Architecture Perspective

SKU choice affects SLA, features, and cost — not just vCPU count.

### Follow-up Questions

1. **P0v3 tier? — Entry Premium v3 — evaluate for lighter prod workloads.**
2. **ASE required when? — VNet isolation at plan level, legacy compliance — often replaced by Private Link.**

### Common Mistakes in Interviews

- Premium v3 for dev sandboxes — wasted cost
- Single B1 instance in production
- Choosing SKU without load test data

---

## Q012: Deployment Slots

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DevOps |
| **Frequency** | Very Common |

### Question

Deep dive: deployment slot configuration for zero-downtime .NET releases.

### Short Answer (30 seconds)

Use staging slot for pre-swap validation; configure sticky settings; warm up with health check; auto-swap on CI success; database changes must be backward compatible.

### Detailed Answer (3–5 minutes)

**Sticky settings (slot-specific):**
- Connection strings (staging DB vs prod)
- `ASPNETCORE_ENVIRONMENT`
- Application Insights instrumentation key

**Swap flow:**
1. Deploy to staging
2. Warm-up requests / smoke tests
3. Swap (instant DNS/traffic flip)
4. Monitor App Insights for 15 min
5. Rollback = swap back if needed

**Architect:** Slots share ASP compute — cost-effective blue/green. Pair with feature flags for decoupled releases.

### Architecture Perspective

Slot mastery is expected for Azure PaaS architect interviews.

### Follow-up Questions

1. **Traffic routing before swap? — Route 5% production traffic to staging for canary testing.**
2. **Slot density limits? — Standard allows 5 slots; Premium 20 — plan accordingly.**

### Common Mistakes in Interviews

- Deploy directly to production slot
- Non-sticky connection string breaks swap
- Breaking DB migration during slot swap

---

## Q013: Always On

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Common |

### Question

Why enable Always On for App Service and when can you disable it?

### Short Answer (30 seconds)

Always On keeps worker process loaded — prevents idle shutdown that causes cold starts on first request. Required for WebJobs, timer triggers on same plan, and consistent API latency.

### Detailed Answer (3–5 minutes)

**Without Always On (Basic+ can enable):**
- App unloaded after ~20 min idle
- First request slow (5-30+ seconds .NET startup)
- WebJobs continuous mode fails

**Can disable when:** Dev/test apps tolerating cold start, Consumption Functions (different service), aggressive cost savings on nonprod with scheduled access.

**Architect:** Mandate Always On for production APIs. Monitor with availability test hitting `/health` every 5 minutes.

### Architecture Perspective

Always On is free setting with major latency impact — often overlooked.

### Follow-up Questions

1. **Always On on Free tier? — Not available — another reason Free is dev-only.**
2. **Always On vs availability test? — Availability test pings app; Always On prevents unload — use both.**

### Common Mistakes in Interviews

- Production API without Always On
- WebJobs on plan without Always On
- Confusing with 'Keep Alive' custom hack instead of native setting

---

## Q014: App Service Environment

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

When deploy App Service Environment (ASE) vs standard multi-tenant App Service?

### Short Answer (30 seconds)

ASE for legacy VNet-isolated dedicated App Service, fine-grained scale unit control, and ILB internal-only access. Most new designs use Premium v3 + Private Link instead of ASE v3 cost/complexity.

### Detailed Answer (3–5 minutes)

**ASE v3 characteristics:**
- Dedicated compute isolated in your VNet
- Internal or external deployment
- Higher cost and operational overhead
- Longer deploy time (hours)

**Modern alternative:**
- App Service Premium v3
- Regional VNet Integration + Private Endpoint inbound
- Front Door for WAF

**Architect:** ASE when regulatory mandate requires dedicated infrastructure boundary or existing ASE investment.

### Architecture Perspective

ASE vs Private Link App Service is common modernization decision.

### Follow-up Questions

1. **ASE scaling? — Front-end and worker scale independently — plan IP space.**
2. **ASE deprecation concerns? — Evaluate Microsoft guidance — many migrate to standard + Private Link.**

### Common Mistakes in Interviews

- ASE for small internal CRUD app — massive overkill
- ASE without IP planning for subnet
- Choosing ASE without cost analysis vs Premium + PE

---

## Q015: Azure Functions Bindings

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Serverless |
| **Frequency** | Very Common |

### Question

Explain Azure Functions bindings and triggers for event-driven architecture.

### Short Answer (30 seconds)

Triggers start execution (HTTP, Queue, Timer, Blob). Bindings connect to data sources read/write without boilerplate SDK code — input bindings inject data, output bindings persist results.

### Detailed Answer (3–5 minutes)

**Example pattern:**
- **Trigger:** Service Bus queue message
- **Input binding:** Blob `{orderId}.json`
- **Output binding:** Cosmos DB document + Service Bus reply queue

**Architect:** Bindings accelerate development but hide complexity — understand retry, poison queue, and idempotency. Extension bundles version-lock dependencies.

**Isolated worker (.NET):** Preferred for .NET 8 — align binding extensions with host version.

### Architecture Perspective

Bindings show Functions depth beyond 'small HTTP method'.

### Follow-up Questions

1. **Binding vs SDK manual? — Bindings for standard paths; SDK when fine control needed.**
2. **Durable Functions bindings? — Orchestrator uses async calls — different programming model.**

### Common Mistakes in Interviews

- Non-idempotent output binding on retry
- Wrong extension bundle version in host.json
- HTTP trigger for long batch — wrong trigger choice

---

## Q016: Durable Functions

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Serverless |
| **Frequency** | Common |

### Question

When use Durable Functions vs standard Functions or Logic Apps?

### Short Answer (30 seconds)

Durable Functions for stateful workflows in code — fan-out/fan-in, human approval, sagas with compensation. Logic Apps for visual integration; standard Functions for stateless event handlers.

### Detailed Answer (3–5 minutes)

**Patterns:**
- **Function chaining** — sequential steps
- **Fan-out/fan-in** — parallel processing aggregate
- **Human interaction** — wait for external event (approval webhook)
- **Eternal orchestrator** — periodic polling

**Storage:** Requires Azure Storage (task hub) for state. Premium plan recommended for production orchestrations.

**Architect:** Order fulfillment saga — reserve inventory → charge payment → ship — with compensation on failure — ideal Durable Functions case.

### Architecture Perspective

Durable Functions fills gap between stateless Functions and BPM engines.

### Follow-up Questions

1. **Durable vs Step Functions? — AWS equivalent — similar orchestration concept.**
2. **Sub-orchestrations? — Compose large workflows from smaller orchestrators.**

### Common Mistakes in Interviews

- Long workflow on Consumption plan — timeout and cold start issues
- No idempotency in activity functions
- Durable for simple 2-step flow — over-engineering

---

## Q017: Container Apps

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Containers |
| **Frequency** | Very Common |

### Question

Architect Azure Container Apps for microservices with scale-to-zero.

### Short Answer (30 seconds)

Container Apps provides serverless Kubernetes abstraction — KEDA autoscale, Dapr sidecars, revisions, internal/external ingress — ideal for event-driven microservices without full AKS ops.

### Detailed Answer (3–5 minutes)

**Architecture:**
- One Container App per microservice
- Environment shared VNet integration
- KEDA scale on HTTP, queue depth, custom metrics
- Secrets from Key Vault references

**vs AKS:** Container Apps when team lacks K8s platform engineers. AKS when need full K8s API, service mesh, GPU node pools.

**Architect:** Start Container Apps for 3-10 microservices; revisit AKS at scale/complexity threshold.

### Architecture Perspective

Container Apps is the modern answer between App Service and AKS.

### Follow-up Questions

1. **Consumption vs dedicated environment? — Dedicated for workload isolation and predictable perf.**
2. **Jobs in Container Apps? — Event-driven jobs with scale-to-zero — batch processing.**

### Common Mistakes in Interviews

- AKS for two simple containers
- No revision management — deploy over production
- Public ingress without WAF/Front Door

---

## Q018: AKS Node Pools

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

Design AKS node pool strategy for mixed workload cluster.

### Short Answer (30 seconds)

System node pool (critical addons only) + user node pools by workload profile — general compute, memory-optimized, GPU — with cluster autoscaler and availability zones.

### Detailed Answer (3–5 minutes)

**Best practices:**
- **System pool:** 3 nodes min, zone spread, taints prevent app scheduling
- **User pools:** Separate pools for windows/linux, spot for batch, on-demand for API
- **Node size:** Standard_D4s_v5 general; E-series for memory

**Architect:** One cluster per environment (nonprod/prod). Namespace isolation + RBAC for teams — not cluster per team unless strong isolation need.

**Upgrade strategy:** Surge node pool upgrade with maxUnavailable tuning.

### Architecture Perspective

Node pool design affects cost, availability, and upgrade safety.

### Follow-up Questions

1. **Spot node pool for API? — Batch/CI only — use on-demand for user-facing.**
2. **Cluster autoscaler vs HPA? — CA adds nodes; HPA adds pods — both needed.**

### Common Mistakes in Interviews

- Single node pool for everything including system pods
- No zone spread on production pool
- System pool running application workloads

---

## Q019: KEDA Autoscaling

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Scale |
| **Frequency** | Common |

### Question

Explain KEDA autoscaling on Azure Container Apps and AKS.

### Short Answer (30 seconds)

KEDA scales workloads based on event sources (queue length, HTTP rate, Prometheus metrics) including scale-to-zero — Event-driven autoscaling beyond CPU-only HPA.

### Detailed Answer (3–5 minutes)

**ScaledObject examples:**
- Azure Service Bus queue > 10 messages → scale out
- HTTP concurrent requests > 100
- Cron scaler for business hours

**On Container Apps:** Built-in KEDA integration — configure scale rules in Bicep/portal.

**On AKS:** Install KEDA addon — ScaledObject CRD references Deployment.

**Architect:** CPU-only autoscale misses queue backlog signals — KEDA for event-driven services.

### Architecture Perspective

KEDA is essential for serverless container and Functions Premium patterns.

### Follow-up Questions

1. **KEDA vs HPA? — KEDA extends HPA with external metrics and scale-to-zero.**
2. **Cooldown period? — Set scale-in stabilization to prevent flapping.**

### Common Mistakes in Interviews

- CPU autoscale only on queue processor
- Scale to zero on latency-critical sync API
- No max replica limit — runaway scale cost

---

## Q020: Azure Container Registry

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Containers |
| **Frequency** | Very Common |

### Question

Design Azure Container Registry strategy for enterprise CI/CD.

### Short Answer (30 seconds)

Premium ACR for geo-replication, private link, content trust; separate registry per environment or single with repo naming; managed identity pull from AKS/App Service; retention policies for untagged images.

### Detailed Answer (3–5 minutes)

**Tiers:**
- **Basic:** Dev only
- **Standard:** Prod single region
- **Premium:** Geo-rep, private link, higher throughput

**Architect patterns:**
- `acme.azurecr.io/orders-api:1.2.3` semver tags
- ACR tasks for image build in cloud
- Defender for Containers scan on push
- Retention: keep last 10 tags, delete untagged >30 days

### Architecture Perspective

ACR is supply chain security chokepoint — architect it deliberately.

### Follow-up Questions

1. **ACR vs Docker Hub? — ACR private, integrated RBAC, geo-rep — no rate limits.**
2. **Anonymous pull? — Disable in prod — MI authentication only.**

### Common Mistakes in Interviews

- Latest tag in production deploys
- Basic ACR for prod without geo-rep
- No image scanning in pipeline

---

## Q021: Web App for Containers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Containers |
| **Frequency** | Common |

### Question

When use Web App for Containers vs Container Apps or AKS?

### Short Answer (30 seconds)

Web App for Containers runs custom Docker on App Service — best when team knows App Service ops model and needs slots/VNet integration without Kubernetes.

### Detailed Answer (3–5 minutes)

**Choose Web App for Containers when:**
- Existing App Service expertise
- Need deployment slots with container
- Simple single-container web app
- Built-in CI/CD from ACR webhook

**Choose Container Apps/AKS when:**
- Multi-container sidecars
- KEDA scale-to-zero
- Full K8s APIs

**Architect:** Middle ground — containerize without K8s tax. Set `WEBSITES_PORT` and health check path in Dockerfile.

### Architecture Perspective

Web App for Containers is underrated migration path from VM IIS.

### Follow-up Questions

1. **Multi-container App Service? — Compose supported limited — sidecars better on Container Apps.**
2. **Pull from ACR? — Managed identity AcrPull role on App Service.**

### Common Mistakes in Interviews

- AKS for single container blog app
- Wrong WEBSITES_PORT — app unreachable
- Huge container image — slow deploy and cold start

---

## Q022: App Service VNet Integration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

Regional VNet Integration vs Private Endpoint for App Service — architect both.

### Short Answer (30 seconds)

VNet Integration: outbound from App Service to private resources (SQL PE, internal API). Private Endpoint: inbound to App Service on private IP. Production private backends need both.

### Detailed Answer (3–5 minutes)

**Outbound (Regional VNet Integration):**
- App → private SQL, Storage, on-prem via ExpressRoute
- Requires delegated subnet `Microsoft.Web/serverFarms`
- Route all outbound through VNet optional

**Inbound (Private Endpoint):**
- Users/internal clients → App Service via private IP
- DNS: `privatelink.azurewebsites.net`

**Architect checklist:** NSG on integration subnet, private DNS zones linked to VNet, disable public network access when PE enabled.

### Architecture Perspective

Bidirectional private App Service is production baseline for enterprise.

### Follow-up Questions

1. **Gateway-required VNet Integration? — Legacy — use regional integration.**
2. **DNS private resolver? — On-prem resolves privatelink zones via hybrid DNS.**

### Common Mistakes in Interviews

- Public SQL from App Service in prod
- Integration subnet without NSG rules
- Private endpoint without disabling public access

---

## Q023: Custom Domains and TLS

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

Configure custom domain and TLS for production App Service API.

### Short Answer (30 seconds)

Map CNAME/A record to App Service; enable managed certificate (free) or import Key Vault cert; enforce HTTPS only; TLS 1.2 minimum; consider Front Door for apex domain and WAF.

### Detailed Answer (3–5 minutes)

**Steps:**
1. Verify domain ownership (TXT/CNAME)
2. Bind `api.company.com` to App Service
3. App Service Managed Certificate or Key Vault reference
4. `minimumTlsVersion`: 1.2
5. HSTS header in app or Front Door

**Architect:** Apex domain (`company.com`) often needs Front Door or DNS ALIAS — App Service alone prefers subdomain CNAME.

**Renewal:** Managed certs auto-renew; Key Vault certs need renewal automation.

### Architecture Perspective

TLS and domain architecture affects SEO, security scanners, and mobile apps.

### Follow-up Questions

1. **Wildcard cert? — Key Vault or purchase — managed cert is per-domain.**
2. **Cert on slot? — Bind cert before swap — or use Front Door single endpoint.**

### Common Mistakes in Interviews

- HTTP allowed in production
- Expired cert without monitoring
- Self-signed cert in prod mobile app API

---

## Q024: Autoscale Rules App Service

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Scale |
| **Frequency** | Very Common |

### Question

Design autoscale profile for App Service handling daily traffic spikes.

### Short Answer (30 seconds)

Combine metric rules (CPU, HTTP queue length, memory) with schedule rules (pre-scale before 9 AM); min 2 instances prod; cooldown 5-10 min; validate with load test.

### Detailed Answer (3–5 minutes)

**Example profile:**
```
Min: 2, Max: 12, Default: 2
Rule 1: CPU > 70% avg 5 min → +2 instances
Rule 2: HTTP queue > 100 → +1 instance
Schedule: Mon-Fri 8 AM → min 4 instances
Scale-in: CPU < 30% for 10 min → -1 (slow scale-in)
```

**Architect:** HTTP queue catches I/O bound before CPU spikes. Custom metric from App Insights (requests/sec) often best signal.

### Architecture Perspective

Autoscale tuning separates architect from checkbox configurator.

### Follow-up Questions

1. **Per-app vs plan autoscale? — Scale App Service Plan instance count — all apps on plan scale together.**
2. **Predictive autoscale? — ML-based pre-scale — evaluate for predictable patterns.**

### Common Mistakes in Interviews

- Min 1 instance in production
- Scale-in immediately on CPU dip — flapping
- Autoscale without load test baseline

---

## Q025: Local Cache App Service

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Common |

### Question

When enable App Service local cache for .NET deployments?

### Short Answer (30 seconds)

Local cache copies site content to worker local SSD — faster cold start after scale-out and reduces storage latency — enable for large deployments or frequent scale events.

### Detailed Answer (3–5 minutes)

**How it works:**
- `WEBSITE_LOCAL_CACHE_OPTION` = Always
- Content synced from `/home` to local disk on startup
- Survives scale-out instance boot faster

**Use when:**
- Large wwwroot (many static files)
- Frequent autoscale events
- Read-heavy content (not write-heavy local files)

**Architect:** Pair with Run From Package — package read-only; local cache accelerates reads. Don't rely on local disk for persistent writes.

### Architecture Perspective

Local cache optimizes scale-out performance on App Service.

### Follow-up Questions

1. **Local cache vs CDN? — CDN for static public assets; local cache for app file system perf.**
2. **Write to local cache disk? — Ephemeral — lost on restart — use Blob Storage.**

### Common Mistakes in Interviews

- Persistent file uploads to App Service local disk
- Local cache without understanding read-only semantics
- Huge mutable log files on local cache volume

---

## Q026: ARR Affinity

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Common |

### Question

Explain ARR affinity (session affinity) on App Service — enable or disable?

### Short Answer (30 seconds)

ARR affinity routes returning clients to same instance via cookie — enable only for legacy in-memory session state; disable for stateless APIs and enable proper load distribution.

### Detailed Answer (3–5 minutes)

**When ON:**
- Legacy app stores session in memory
- WebSocket sticky connections (sometimes)

**When OFF (default for modern apps):**
- Stateless REST APIs
- Session in Redis/SQL/Cosmos
- Better load balance across instances

**Architect:** Default OFF. If enabling, document instance failure impact — users lose session. Migration path: externalize session then disable affinity.

### Architecture Perspective

ARR affinity is technical debt indicator in modern architectures.

### Follow-up Questions

1. **Affinity and deployment slots? — Affinity cookie may route to specific instance after swap — test carefully.**
2. **Affinity vs Front Door session affinity? — Layer on layer — avoid double affinity.**

### Common Mistakes in Interviews

- Affinity on with in-memory session — instance failure logout
- Affinity enabled 'just in case' on stateless API
- No plan to externalize session before scaling

---

## Q027: Health Check App Service

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reliability |
| **Frequency** | Very Common |

### Question

Configure App Service health check for autoscale and load balancer integration.

### Short Answer (30 seconds)

Health check path (e.g., `/health`) — unhealthy instances removed from load balancer rotation; enables automatic instance replacement during platform issues.

### Detailed Answer (3–5 minutes)

**Configuration:**
- Path returns 200 with quick DB ping optional
- Unhealthy threshold removes instance from rotation
- Works with autoscale — unhealthy instances don't receive traffic

**Architect:** Health endpoint checks critical dependencies (SQL, Redis) with timeout budget < 5 seconds. Don't check every downstream — cascading false unhealthy.

**Pair with:** App Insights availability tests for external monitoring.

### Architecture Perspective

Health checks connect app readiness to platform routing decisions.

### Follow-up Questions

1. **Liveness vs readiness? — Single App Service health check — design combined endpoint.**
2. **Health check during deployment slot swap? — Ensure staging healthy before swap.**

### Common Mistakes in Interviews

- Health check returns 200 without checking dependencies
- Slow health check causing timeout removals
- No health check configured on production

---

## Q028: Run From Package

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DevOps |
| **Frequency** | Common |

### Question

Benefits of Run From Package (WEBSITE_RUN_FROM_PACKAGE) on App Service?

### Short Answer (30 seconds)

Deploys app as read-only zip/blob mount — faster deployments, fewer file lock issues, atomic updates, reduced storage corruption risk.

### Detailed Answer (3–5 minutes)

**Settings:**
- `WEBSITE_RUN_FROM_PACKAGE=1` (local package)
- `WEBSITE_RUN_FROM_PACKAGE=URL` (Blob SAS or MI to Storage)

**Benefits:**
- Atomic deploy — all files updated simultaneously
- No Kudu file copy slow sync
- Read-only filesystem reduces tampering

**Architect:** Standard for CI/CD — pipeline uploads zip to Blob, sets URL with MI auth. Pair with deployment slots.

### Architecture Perspective

Run From Package is CI/CD best practice for App Service.

### Follow-up Questions

1. **Run From Package vs ZIP deploy? — Run From Package mounts zip; traditional deploy extracts to wwwroot.**
2. **Package size limits? — Large packages slow cold start — trim dependencies.**

### Common Mistakes in Interviews

- Kudu manual file edits in production
- SAS URL expiring without rotation
- Writable app expecting local file persistence

---

## Q029: Function Premium Plan

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Serverless |
| **Frequency** | Very Common |

### Question

When choose Azure Functions Premium plan over Consumption?

### Short Answer (30 seconds)

Premium plan for pre-warmed instances (no cold start), VNet integration, unlimited duration, higher memory — production HTTP APIs and Durable Functions orchestrations.

### Detailed Answer (3–5 minutes)

**Premium features:**
- **Always Ready instances** — min 1+ warm workers
- **Elastic Premium (EP1-EP3)** — scale 0 to N with pre-warm
- VNet integration for private resources
- Max 60 min execution (vs 5-10 min consumption)

**Architect decision matrix:**
| Requirement | Plan |
|-------------|------|
| Spiky batch, cold OK | Consumption |
| Sync API <500ms | Premium |
| VNet + private SQL | Premium |
| Durable production | Premium |

### Architecture Perspective

Premium plan is the architect answer to Consumption cold start limitations.

### Follow-up Questions

1. **Premium vs App Service? — Premium Functions when event-driven + scale-to-zero; App Service for always-on API.**
2. **EP1 sizing? — Start EP1 with 1 pre-warmed; load test before EP2.**

### Common Mistakes in Interviews

- Consumption for customer-facing checkout API
- Premium with 0 always-ready instances — defeats purpose
- Durable Functions on Consumption in production

---

## Q030: Logic Apps Standard

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Integration |
| **Frequency** | Common |

### Question

Logic Apps Standard vs Consumption — architect integration platform choice.

### Short Answer (30 seconds)

Standard (single-tenant, App Service plan hosted) for VNet integration, predictable performance, higher throughput. Consumption for low-volume, pay-per-action, no VNet requirement.

### Detailed Answer (3–5 minutes)

**Logic Apps Standard:**
- Hosted in App Service Environment or dedicated plan
- VNet integration for private connectors
- Fixed pricing via WS1/WS2/WS3 workflow service plan
- Stateful workflows with better isolation

**Consumption:**
- Serverless pricing per action
- Public connectors default
- Quick prototypes and low-volume B2B

**Architect:** Enterprise integrations touching SAP/on-prem via hybrid connector → Standard. Simple SaaS webhook fan-out → Consumption.

### Architecture Perspective

Logic Apps tier choice affects networking, cost, and compliance.

### Follow-up Questions

1. **Logic Apps vs Functions for integration? — Logic Apps visual, connectors; Functions code-first complex logic.**
2. **Durable Functions vs Logic Apps? — Durable for dev team in C#; Logic Apps for integration specialists.**

### Common Mistakes in Interviews

- Consumption Logic Apps for private SAP integration
- Standard without VNet when connectors need private access
- No error handling / dead letter on critical workflows

---

## Q031: API Management Integration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Integration |
| **Frequency** | Very Common |

### Question

Place Azure API Management in front of App Service and Functions — why and how?

### Short Answer (30 seconds)

APIM provides API gateway: authentication, rate limiting, versioning, caching, analytics, WAF integration — decouples public API contract from backend implementation.

### Detailed Answer (3–5 minutes)

**Architecture:**
```
Client → APIM (api.company.com) → App Service / Functions (private)
```

**Features:**
- OAuth/JWT validation at gateway
- Rate limit per subscription key
- Revision-based API versioning
- Request/response transformation

**Architect:** Backends use Private Endpoint; APIM in VNet or External with IP restrictions. Don't expose App Service public URL when APIM is front door.

### Architecture Perspective

APIM is standard API façade pattern for enterprise Azure.

### Follow-up Questions

1. **APIM vs Front Door? — APIM API management; Front Door global L7 load balance + WAF — often combined.**
2. **Consumption vs Premium APIM? — Premium for VNet injection and multi-region.**

### Common Mistakes in Interviews

- Public App Service URL bypassing APIM
- No rate limiting on public API
- API keys as only auth for sensitive data

---

## Q032: Windows vs Linux App Service

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Common |

### Question

Choose Windows vs Linux App Service for .NET 8 workload?

### Short Answer (30 seconds)

Linux App Service preferred for .NET 8+ — better performance, lower cost, smaller footprint. Windows when needing full Framework 4.x, COM components, or legacy IIS modules.

### Detailed Answer (3–5 minutes)

**Linux advantages (.NET 8):**
- Lower ASP cost for same tier
- Faster container-like isolation
- Better CI/CD with Oryx build

**Windows required when:**
- .NET Framework 4.8 legacy
- Windows-specific dependencies (COM, GAC)
- Team only has IIS expertise short-term

**Architect:** Default Linux for new .NET Core/8. Document migration path for Framework apps (Azure Migrate App Service assessment).

### Architecture Perspective

OS choice affects cost, performance, and migration strategy.

### Follow-up Questions

1. **Mixed plan? — One ASP is Windows OR Linux — not mixed on same plan.**
2. **.NET on Linux containers? — Web App for Containers alternative on Linux plan.**

### Common Mistakes in Interviews

- Windows plan for new .NET 8 API without reason
- Linux plan with Windows-only dependency discovered late
- No load test comparing OS options

---

## Q033: App Service Certificates

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Manage TLS certificates for App Service at enterprise scale.

### Short Answer (30 seconds)

App Service Managed Certificate for public apps; Key Vault integration for wildcard and internal certs; automate renewal; Front Door for centralized cert management multi-app.

### Detailed Answer (3–5 minutes)

**Options:**
1. **Free managed cert** — single domain, auto-renew, public apps only
2. **Key Vault reference** — import PFX, RBAC to App Service MI
3. **Front Door managed cert** — apex + subdomains at edge

**Architect:** Central team owns Key Vault `prod-tls-certs`. Pipeline imports renewed cert. Alert 30 days before expiry on non-auto-renew certs.

### Architecture Perspective

Certificate lifecycle failures cause production outages — automate.

### Follow-up Questions

1. **Managed cert limitations? — No wildcard, no internal/private App Service.**
2. **Cert per slot? — Each hostname binding needs cert — automate in swap pipeline.**

### Common Mistakes in Interviews

- Manual cert upload every year
- Expired cert without Azure Monitor alert
- Wildcard cert private key in app settings

---

## Q034: Diagnostic Settings App Service

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Observability |
| **Frequency** | Very Common |

### Question

Configure diagnostic settings for App Service production monitoring.

### Short Answer (30 seconds)

Send AppServiceHTTPLogs, AppServiceConsoleLogs, AppServiceAppLogs to Log Analytics; enable AllMetrics; configure retention and daily cap; alert on HTTP 5xx spike.

### Detailed Answer (3–5 minutes)

**Enable via Bicep:**
```bicep
resource diag 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = {
  // AppServiceHTTPLogs, AppServicePlatformLogs → Log Analytics
}
```

**Architect:** Platform team deploys diagnostic settings via Policy DeployIfNotExists — app teams don't opt-in manually.

**Tables:** `AppServiceHTTPLogs` for W3C request analytics; `AppServiceConsoleLogs` for startup failures.

### Architecture Perspective

Diagnostic settings are prerequisite for troubleshooting App Service incidents.

### Follow-up Questions

1. **App Insights vs diagnostic logs? — App Insights APM; diagnostics platform and HTTP raw logs.**
2. **Log scrubbing? — Don't log PII/card data — configure sampling and app log levels.**

### Common Mistakes in Interviews

- No HTTP logs in production
- Verbose logging without daily cap
- Diagnostics only to Storage — slow query in incidents

---

## Q035: CPU Profiling App Service

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Common |

### Question

Diagnose high CPU on App Service using profiling tools.

### Short Answer (30 seconds)

Use App Service Profiler (App Insights) for production CPU flame graphs; Kudu `dotnet-trace` for deeper analysis; correlate with autoscale metrics and slow dependencies.

### Detailed Answer (3–5 minutes)

**Workflow:**
1. Enable Profiler on App Insights
2. Capture during high CPU window
3. Identify hot methods (JSON serialization, regex, sync-over-async)
4. Fix code path or scale out temporarily

**Architect:** Profiler overhead minimal — leave enabled prod. Pair with `ServerException` and dependency tracking in App Insights.

**Common .NET causes:** Sync `HttpClient`, missing `AsNoTracking`, large object heap pressure.

### Architecture Perspective

Profiling connects performance architecture to code reality.

### Follow-up Questions

1. **Profiler vs snapshot debugger? — Profiler for CPU; Snapshot for exception moment variables.**
2. **Load test before profiling? — Reproduce under known load for clearer flame graph.**

### Common Mistakes in Interviews

- Scale out indefinitely without profiling root cause
- Profiler never enabled — flying blind
- Profiling only in dev — issue doesn't reproduce locally

---

## Q036: Zone Redundancy App Service

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reliability |
| **Frequency** | Common |

### Question

Enable zone redundancy for App Service Premium v3 — requirements and benefits.

### Short Answer (30 seconds)

Premium v3 plan with minimum 3 instances spread across availability zones — protects against datacenter failure within region — improves SLA beyond single-datacenter deployment.

### Detailed Answer (3–5 minutes)

**Requirements:**
- Premium v3 App Service Plan
- `zoneRedundant: true` in Bicep
- Min 3 instances for zone spread
- Supported regions with AZ

**Architect:** Zone-redundant ASP + zone-redundant SQL + Front Door health probes = strong single-region HA. Not substitute for multi-region DR.

**Cost:** ~3 instances minimum — budget accordingly vs 2-instance non-zonal HA.

### Architecture Perspective

Zone redundancy is within-region HA — architects distinguish from geo-DR.

### Follow-up Questions

1. **Zonal vs zone-redundant storage for app? — App state external — zone-redundant ASP handles compute.**
2. **Deploy zone-redundant in region without AZ? — Fails — verify region capability.**

### Common Mistakes in Interviews

- Two instances claiming zone redundancy
- Zone-redundant without multi-instance minimum
- Assuming zone-redundant replaces backup region

---

## Q037: App Service Backup

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reliability |
| **Frequency** | Common |

### Question

App Service backup strategy — what is backed up and what is not?

### Short Answer (30 seconds)

App Service backup captures app content, config, connection strings — NOT the database. Schedule daily backup to Storage account; include slot settings; test restore to staging slot.

### Detailed Answer (3–5 minutes)

**Backed up:**
- wwwroot files
- App settings and connection strings
- Custom domains bindings (partial)

**NOT backed up:**
- Azure SQL data — use SQL backup
- External Blob content
- DNS records outside Azure

**Architect:** Backup is DR for app config/code — pair with IaC (Bicep) as primary source of truth; backup as safety net.

### Architecture Perspective

App Service backup scope limits catch teams in disaster recovery drills.

### Follow-up Questions

1. **Backup vs snapshot slot? — Backup scheduled; slot is deployment strategy — complementary.**
2. **Geo-redundant backup storage? — Store backups in paired region for regional disaster.**

### Common Mistakes in Interviews

- Assuming App Service backup includes SQL database
- Never tested restore procedure
- No backup on production because 'we have Git'

---

## Q038: Easy Auth

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Implement App Service Authentication (Easy Auth) vs app-level auth?

### Short Answer (30 seconds)

Easy Auth handles OAuth/OIDC at platform layer before request hits app — quick Entra ID, Google, Facebook integration — app receives authenticated headers (`X-MS-CLIENT-PRINCIPAL`).

### Detailed Answer (3–5 minutes)

**When Easy Auth:**
- Internal tools with Entra ID only
- Quick protection without code changes
- Multi-tenant SaaS with platform SSO

**When app-level:**
- Complex authorization (ABAC, custom claims)
- Multi-idp with unified token format
- API returning JWT to mobile clients

**Architect:** Easy Auth for internal admin sites; ASP.NET Core Identity + Entra for product APIs with fine-grained RBAC.

### Architecture Perspective

Easy Auth vs DIY auth is common App Service security question.

### Follow-up Questions

1. **Easy Auth v2? — Current version — configure via app settings or portal Authentication blade.**
2. **Easy Auth on API + APIM? — APIM validates JWT; Easy Auth may duplicate — choose one layer.**

### Common Mistakes in Interviews

- Easy Auth for complex custom RBAC without evaluation
- Authentication disabled on staging slot publicly exposed
- Trusting client-sent user headers without Easy Auth

---

## Q039: Managed Identity App Service

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Very Common |

### Question

Implement managed identity patterns for App Service accessing Azure services.

### Short Answer (30 seconds)

Enable system-assigned or user-assigned MI; grant least-privilege RBAC (Key Vault Secrets User, Storage Blob Data Reader); use Key Vault references; DefaultAzureCredential in .NET.

### Detailed Answer (3–5 minutes)

**Pattern:**
```csharp
// .NET — no secrets in config
var credential = new DefaultAzureCredential();
var client = new SecretClient(vaultUri, credential);
```

**Slot consideration:** User-assigned MI can stay constant across slot swap; system-assigned differs per slot — plan Key Vault access accordingly.

**Architect:** Ban connection strings with passwords in app settings — Policy audit non-compliant apps.

### Architecture Perspective

Managed identity is mandatory pattern for production Azure apps.

### Follow-up Questions

1. **System vs user-assigned MI? — User-assigned for shared identity across slots/regions.**
2. **Federated credential CI/CD? — GitHub Actions OIDC to Entra — no SP secret.**

### Common Mistakes in Interviews

- SQL connection string password in app settings
- Contributor MI on subscription
- System-assigned MI breaks after slot swap without planning

---

## Q040: Sidecar Pattern Containers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Containers |
| **Frequency** | Common |

### Question

Explain sidecar pattern in Azure Container Apps and AKS.

### Short Answer (30 seconds)

Sidecar containers share pod/network namespace with main app — handle logging, proxy, mesh, secrets — without modifying application container.

### Detailed Answer (3–5 minutes)

**Examples:**
- **Dapr sidecar** — service invocation, pub/sub, state store
- **Envoy/Istio** — service mesh mTLS, traffic split
- **Log forwarder** — Fluent Bit shipping to Log Analytics

**Container Apps:** Dapr enabled per app — sidecar injected automatically.

**Architect:** Sidecars add resource overhead — size CPU/memory accordingly. Prefer Dapr over custom sidecar glue when patterns match.

### Architecture Perspective

Sidecar pattern shows container architecture maturity beyond single-container apps.

### Follow-up Questions

1. **Sidecar vs init container? — Init runs before app starts (migration); sidecar runs alongside.**
2. **Multiple sidecars? — Supported in K8s — watch total pod resource limits.**

### Common Mistakes in Interviews

- Monolithic container doing app + proxy + logging
- Sidecar without resource limits starving main app
- Custom sidecar reinventing Dapr features

---

## Q041: Batch vs Real-Time Compute

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Architecture |
| **Frequency** | Common |

### Question

Choose batch vs real-time compute on Azure for order processing.

### Short Answer (30 seconds)

Real-time (App Service, Functions, Container Apps HTTP) for user-facing order submission. Batch (Azure Batch, Functions queue trigger, Container Apps Jobs) for end-of-day settlement, reporting, ETL.

### Detailed Answer (3–5 minutes)

**Decision matrix:**
| Pattern | Azure service | Latency |
|---------|---------------|--------|
| Sync API | App Service | <500ms |
| Event async | Functions + SB Queue | Seconds |
| Large parallel batch | Azure Batch / ACA Jobs | Minutes-hours |
| Stream | Event Hubs + Stream Analytics | Sub-second ingest |

**Architect:** Hybrid — API accepts order (real-time), publishes event, batch processor settles payments overnight.

### Architecture Perspective

Batch vs real-time split is fundamental compute architecture decision.

### Follow-up Questions

1. **Batch on Consumption Functions? — 10 min timeout limit — use Batch service for HPC.**
2. **Spark on Synapse for batch? — Big data analytics batch — different scale tier.**

### Common Mistakes in Interviews

- Batch job in synchronous HTTP request
- Real-time Functions for 6-hour ETL
- No queue between API and batch processor

---

## Q042: SignalR Service

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Real-Time |
| **Frequency** | Common |

### Question

When use Azure SignalR Service vs self-hosted SignalR on App Service?

### Short Answer (30 seconds)

Azure SignalR Service offloads connection management — scales to 100K+ concurrent connections — App Service hosts hub logic only — required for large fan-out real-time apps.

### Detailed Answer (3–5 minutes)

**Tiers:**
- **Free:** Dev only (20 connections)
- **Standard:** Production scale
- **Premium:** Large enterprise, geo-scale, SLA

**Architecture:**
```
Browser ←→ Azure SignalR Service ←→ App Service (hub code)
```

**Architect:** Live dashboards, collaborative editing, notification push — SignalR Service prevents connection exhaustion on App Service.

### Architecture Perspective

SignalR Service solves WebSocket scale limits on App Service.

### Follow-up Questions

1. **SignalR vs Web PubSub? — Web PubSub general pub/sub; SignalR .NET hub model.**
2. **Serverless mode? — SignalR Service serverless with Functions triggers.**

### Common Mistakes in Interviews

- Self-hosted SignalR at 10K concurrent users on small ASP
- Sticky sessions instead of SignalR Service at scale
- Free tier in production

---

## Q043: Static Web Apps

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Common |

### Question

Azure Static Web Apps vs App Service for React front-end and API?

### Short Answer (30 seconds)

Static Web Apps for Jamstack — static front-end from GitHub, serverless API via Functions, global CDN, free SSL — ideal SPA + API. App Service when need full .NET server, WebSockets, long-running API.

### Detailed Answer (3–5 minutes)

**Static Web Apps strengths:**
- CI/CD from GitHub Actions built-in
- Staging environments per PR
- Azure Functions integrated API routes
- Custom domain + managed cert free tier

**App Service when:**
- Full ASP.NET Core MVC/server rendering
- Deployment slots with complex backend
- VNet integration to private SQL

**Architect:** SWA for marketing site + lightweight API; App Service for core enterprise API.

### Architecture Perspective

SWA vs App Service is common front-end architecture fork.

### Follow-up Questions

1. **SWA Standard vs Free? — Standard for custom domains without SWA subdomain limits in enterprise.**
2. **SWA + APIM? — API behind APIM while static on SWA CDN.**

### Common Mistakes in Interviews

- App Service for static-only React site — overpaying
- SWA API for heavy VNet-private SQL without networking plan
- No PR preview environments for front-end

---

## Q044: App Service Hybrid Connections

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

Use App Service Hybrid Connections to reach on-premises resources.

### Short Answer (30 seconds)

Hybrid Connection Manager agent on-prem relays TCP traffic to App Service — reach legacy SQL, SOAP APIs without VPN/ExpressRoute — good for dev/test or small integrations.

### Detailed Answer (3–5 minutes)

**Limits:**
- TCP only — not UDP
- Not for production high-throughput (use ExpressRoute/VPN)
- Requires Hybrid Connection Manager installed on-prem

**Architect:** Migration bridge — cloud App Service calls on-prem DB during phased migration. Plan cutover to VPN/ExpressRoute + private connectivity for prod.

### Architecture Perspective

Hybrid Connections are stepping stone — not enterprise production networking.

### Follow-up Questions

1. **Hybrid vs VNet Integration? — Hybrid reaches on-prem TCP by name; VNet Integration routes through Azure VNet.**
2. **Relay vs Hybrid Connection? — Azure Relay underpins Hybrid Connections feature.**

### Common Mistakes in Interviews

- Hybrid Connection as permanent prod path for high traffic
- No HA on Hybrid Connection Manager agent
- Confusing with Site-to-Site VPN architecture

---

## Q045: Compute Quota Planning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Common |

### Question

Plan Azure compute quota before large migration or product launch.

### Short Answer (30 seconds)

Request vCPU quota increases per region/SKU family early; use Azure Capacity Reservation for scarce SKUs; distribute across regions; monitor `Microsoft.Compute/locations/usages`.

### Detailed Answer (3–5 minutes)

**Process:**
1. Inventory target VM/SKU needs from Migrate assessment
2. Check current quota vs required in target region
3. Submit quota increase ticket 2-4 weeks before deploy
4. Consider alternate SKU or region if quota delayed

**Architect:** Quota is deployment blocker equal to architecture approval — include in migration timeline. AKS node pools consume multiple VM family quotas.

### Architecture Perspective

Quota planning prevents launch-day 'InsufficientQuota' failures.

### Follow-up Questions

1. **Quota vs capacity reservation? — Quota is ceiling; reservation guarantees availability within quota.**
2. **Subscription vs region quota? — Regional vCPU limits per subscription — request per sub/region.**

### Common Mistakes in Interviews

- Assume unlimited Azure capacity in any region
- Quota increase request day before go-live
- Wrong SKU family in quota request

---

## Q046: Image Hardening Containers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Container image hardening checklist for ACR and AKS production.

### Short Answer (30 seconds)

Non-root user, minimal base image (distroless/alpine), no secrets in layers, scan with Defender for Containers, pin digests not tags, sign with Notation/Cosign.

### Detailed Answer (3–5 minutes)

**Checklist:**
- Multi-stage Dockerfile — build vs runtime separation
- `USER nonroot` in final stage
- Patch base image weekly in CI
- ACR retention + quarantine policy on CVE critical
- Admission controller deny `:latest` and unscanned images

**Architect:** Supply chain security — only deploy images passing scan gate in CI/CD.

### Architecture Perspective

Image hardening is container security foundation — expected in architect interviews.

### Follow-up Questions

1. **Distroless vs Alpine? — Distroless smaller attack surface; Alpine musl compatibility issues for .NET.**
2. **ACR Tasks scan on build? — Integrate Trivy/Defender in pipeline.**

### Common Mistakes in Interviews

- Root container in production K8s
- Latest tag deploys from public Docker Hub
- Secrets baked into image layers in Git history

---

## Q047: Startup Probes Kubernetes

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Common |

### Question

Configure startup, liveness, and readiness probes for AKS workloads.

### Short Answer (30 seconds)

Startup probe allows slow-starting containers before liveness kills them. Readiness removes pod from Service until ready. Liveness restarts hung containers.

### Detailed Answer (3–5 minutes)

**Example:**
```yaml
startupProbe:
  httpGet: { path: /health/startup, port: 8080 }
  failureThreshold: 30
  periodSeconds: 10
readinessProbe:
  httpGet: { path: /health/ready, port: 8080 }
livenessProbe:
  httpGet: { path: /health/live, port: 8080 }
```

**Architect:** .NET apps need generous startupProbe — JIT and EF migrations slow boot. Readiness checks DB connection; liveness only checks process responsive.

### Architecture Perspective

Probe design prevents cascading pod restart death spirals.

### Follow-up Questions

1. **Probe and App Service health check? — Same concept — K8s native on AKS.**
2. **exec vs httpGet probe? — Prefer httpGet; exec adds shell dependency.**

### Common Mistakes in Interviews

- Liveness probe hits database — restart loops on DB blip
- No startup probe on 60-second .NET boot
- Readiness same as liveness — wrong semantics

---

## Q048: Resource Limits Containers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

Set CPU and memory requests/limits for AKS pod resource management.

### Short Answer (30 seconds)

Requests guarantee scheduling capacity; limits cap usage — set requests ≈ average usage, limits ≈ peak — prevents noisy neighbor and OOM kills.

### Detailed Answer (3–5 minutes)

**Guidelines:**
```yaml
resources:
  requests: { cpu: 250m, memory: 512Mi }
  limits:   { cpu: 1000m, memory: 1Gi }
```

**Architect:** Start from load test metrics. .NET apps: watch LOH — memory limit too low causes GC thrashing/OOMKill. Use Vertical Pod Autoscaler recommendation mode before enforcing.

**Namespace quotas:** Prevent one team consuming entire cluster.

### Architecture Perspective

Resource limits translate performance architecture to K8s scheduling.

### Follow-up Questions

1. **Limit without request? — Bad practice — request required for scheduling.**
2. **CPU limit throttling? — .NET can throttle under low CPU limit — tune carefully.**

### Common Mistakes in Interviews

- No limits — pod consumes node memory crash neighbors
- Limits equal requests with no burst room
- Copy-paste limits without load test validation

---

## Q049: Multi-Region App Service

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reliability |
| **Frequency** | Very Common |

### Question

Design multi-region App Service for 99.99% API availability.

### Short Answer (30 seconds)

Front Door Premium routes to regional App Services; externalize session state (Redis); SQL geo-replication or Cosmos multi-write; coordinated deployment pipeline; health probes per origin.

### Detailed Answer (3–5 minutes)

**Active-active challenges:**
- Data consistency across regions
- Deployment synchronization
- Config drift between regions

**Architect patterns:**
- **Active-passive:** Simpler data — secondary warm standby
- **Active-active:** Stateless API + Cosmos/SQL read replicas

**Runbook:** Failover = Front Door origin priority change + DNS if needed.

### Architecture Perspective

Multi-region App Service requires data architecture not just duplicate deploy.

### Follow-up Questions

1. **Traffic Manager vs Front Door? — Front Door L7 + WAF; TM DNS-level weighted routing.**
2. **Regional ASP scaling? — Each region independent autoscale profile.**

### Common Mistakes in Interviews

- Active-active without shared session store
- Manual deploy causing region config drift
- No Front Door health probe per region origin

---

## Q050: Cost Optimize Idle Compute

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Very Common |

### Question

Reduce Azure compute cost for idle and non-production workloads.

### Short Answer (30 seconds)

Auto-shutdown dev VMs/App Service nights/weekends; scale Functions/Container Apps to zero; right-size SKUs; DevTest subscriptions; Azure Advisor recommendations; reserved instances for stable prod baseline only.

### Detailed Answer (3–5 minutes)

**Tactics:**
| Workload | Optimization |
|----------|-------------|
| Dev VMs | Auto-shutdown 7 PM |
| Nonprod ASP | Scale to 1 off-hours |
| Batch | Spot instances / ACA Jobs scale-to-zero |
| Prod | RI/Savings Plan on baseline |

**Architect:** Tag `AutoShutdown=true` + Automation account. FinOps dashboard shows idle CPU <5% for 7 days — right-size ticket.

**Balance:** Cost vs developer experience — don't shutdown shared staging during release week.

### Architecture Perspective

Idle compute optimization is recurring FinOps architect responsibility.

### Follow-up Questions

1. **Azure Automation vs Logic Apps shutdown? — Automation runbooks common for VM schedule.**
2. **Start/Stop v2? — Managed feature for VM schedules without custom scripts.**

### Common Mistakes in Interviews

- Production Premium ASP 3 instances overnight for dev traffic
- No budget alerts on nonprod subscriptions
- Reserved instances on workloads planned to decommission

---
