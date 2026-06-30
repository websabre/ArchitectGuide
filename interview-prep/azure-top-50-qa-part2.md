# Azure Top 50 — Part 2 (Q009–Q030)

> Compute, Data, Identity & Security | [Part 1](azure-top-50-qa-part1.md) | [Part 3](azure-top-50-qa-part3.md)

---

## Section 2: Compute

## Q009: App Service vs Azure Functions

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Azure Compute |
| **Frequency** | Very Common |
| **Week** | 10 |

### Question

When would you choose App Service over Azure Functions, and vice versa?

### Short Answer (30 seconds)

App Service for always-on HTTP APIs and web apps with predictable traffic. Functions for event-driven, short-lived, sporadic workloads. Use Functions for queue triggers; App Service for primary REST API surface.

### Detailed Answer (3–5 minutes)

**App Service:**
- Always-on web hosting (PaaS)
- Deployment slots, custom domains, VNet integration
- Best for: .NET 8 REST APIs, background always-on services, WebSockets
- Scaling: manual rules or autoscale on CPU/memory/HTTP queue

**Azure Functions:**
- Event-driven (HTTP, timer, queue, blob, Event Grid)
- Consumption plan: pay per execution, scale to zero
- Premium plan: pre-warmed instances, VNet, longer timeouts
- Durable Functions for workflows (saga orchestration)

| Factor | App Service | Functions |
|--------|-------------|-----------|
| Cold start | Minimal (always on) | Consumption: yes |
| Max duration | Unlimited | Consumption: 5–10 min |
| Cost at low traffic | Fixed plan cost | Near zero (consumption) |
| Cost at high steady traffic | Predictable | Can exceed App Service |

**Hybrid pattern:** App Service as public API; Functions process Service Bus messages, nightly batch jobs, file uploads.

### Architecture Perspective

Don't put entire monolith on Functions — HTTP trigger limits and cold starts hurt UX. Don't run App Service for once-per-hour timer job — waste money.

### Follow-up Questions

1. **Durable Functions for sagas?** Yes — orchestration with compensating transactions; alternative to custom saga coordinator.
2. **Functions in VNet?** Premium or Dedicated plan required for Private Link to SQL.

### Common Mistakes in Interviews

- "Serverless for everything" — ignores steady high traffic economics
- Ignoring cold start impact on user-facing APIs

---

## Q010: App Service vs AKS vs Container Apps

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Azure Compute |
| **Frequency** | Common |
| **Week** | 10, 26 |

### Question

Compare App Service, AKS, and Azure Container Apps for microservices.

### Short Answer

App Service: simplest, least ops. Container Apps: containers without K8s complexity. AKS: full Kubernetes when you need service mesh, operators, multi-tenant clusters.

### Detailed Answer

| Criteria | App Service | Container Apps | AKS |
|----------|-------------|----------------|-----|
| Ops burden | Low | Low-Medium | High |
| K8s features | None | Subset (KEDA) | Full |
| Scale to zero | No | Yes | HPA (not zero by default) |
| Service mesh | No | Limited | Istio/Linkerd |
| Team skill | .NET devs | Container basics | K8s experts |
| Multi-service | Multiple apps | Multiple containers | Full cluster |

**Decision framework:**
- 1–5 services, .NET focus → **App Service** or **Container Apps**
- 10+ services, GitOps, service mesh → **AKS**
- Event-driven scale (queue depth) → **Container Apps** with KEDA

### Architecture Perspective

Start App Service/Container Apps. Move to AKS when operational maturity and feature needs justify K8s tax — not because "microservices need Kubernetes."

### Common Mistakes in Interviews

- AKS as default for all microservices
- Ignoring platform team's ability to operate K8s

---

## Q011: Deployment Slots and Blue-Green on App Service

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DevOps |
| **Frequency** | Common |
| **Week** | 10 |

### Question

How do App Service deployment slots enable blue-green deployments?

### Short Answer

Deploy to staging slot, warm up, swap with production — instant traffic switch with rollback via reverse swap.

### Detailed Answer

1. Production slot serves live traffic
2. Deploy new version to `staging` slot
3. Test staging URL (`myapp-staging.azurewebsites.net`)
4. `az webapp deployment slot swap` — swaps hostnames
5. Rollback: swap again if issues detected

**Slot settings:** Some app settings can be "sticky" (don't swap) — e.g., connection strings per environment.

**With Front Door:** Route percentage traffic to staging for canary before full swap.

**Architect requirements:** Automated swap in CI/CD only after smoke tests pass. App Insights availability tests on staging pre-swap.

### Common Mistakes

- Swapping without testing staging
- Not configuring slot-specific connection strings

---

## Q012: Azure Functions Pricing Plans

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Cost / Compute |
| **Frequency** | Occasional |
| **Week** | 10 |

### Question

Compare Consumption, Premium, and Dedicated (App Service) Function plans.

### Short Answer

Consumption: pay-per-execution, cold starts. Premium: pre-warmed, VNet, longer runs. Dedicated: runs on App Service plan you already pay for.

### Detailed Answer

| Plan | Best For | Cold Start | VNet |
|------|----------|------------|------|
| Consumption | Sporadic, dev | Yes | No |
| Premium (EP) | Production events, low latency | Minimal | Yes |
| Dedicated (ASP) | Share plan with web apps | No | Yes |

**Cost trap:** High-volume steady Functions on Consumption can cost more than Premium EP1. Model costs before architecture sign-off.

---

## Q013: Scaling App Service — When to Upgrade SKU vs Scale Out

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Common |
| **Week** | 10 |

### Question

Your App Service is slow under load. Scale up (bigger SKU) or scale out (more instances)?

### Short Answer

Scale out first for HTTP workloads — horizontal scaling. Scale up if single-instance bottleneck (memory, CPU per instance maxed, or single-threaded constraint).

### Detailed Answer

**Scale out (autoscale):** Add instances behind load balancer. Requires stateless app, session affinity off or shared session store (Redis).

**Scale up:** P1v3 → P2v3 for more CPU/RAM per instance. Needed for memory-heavy operations or when instance count limit reached.

**Check first:** Database bottleneck (scaling app won't help), missing indexes, sync blocking code, no caching.

**Architect workflow:** Load test → identify bottleneck → scale appropriate tier → set autoscale rules (CPU > 70% for 5 min → add instance).

---

## Q014: .NET 8 on Azure — Hosting Recommendation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | .NET on Azure |
| **Frequency** | Common |
| **Week** | 10 |

### Question

What's your default Azure hosting recommendation for a new .NET 8 microservice?

### Short Answer

Azure App Service (Linux, .NET 8 runtime) for most APIs. Container Apps if already containerized or need KEDA scale. AKS only with clear K8s requirements.

### Detailed Answer

**Default stack:**
- App Service Linux P1v3 (nonprod B1)
- Managed Identity → Key Vault + Azure SQL
- Application Insights
- Deployment slots + GitHub Actions
- VNet integration for Private Link to database

**Move to containers when:** Multi-runtime cluster, custom OS packages, existing Docker pipeline, KEDA scaling on queue depth.

---

## Section 3: Data Platform

## Q015: Azure SQL Database vs SQL on VM

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Azure Data |
| **Frequency** | Very Common |
| **Week** | 11 |

### Question

Azure SQL Database vs SQL Server on Azure VM — when each?

### Short Answer

Azure SQL Database for new cloud-native apps (managed, auto-patch, built-in HA). SQL on VM for full instance control, unsupported features, or lift-and-shift with minimal changes.

### Detailed Answer

| Factor | Azure SQL Database | SQL on VM |
|--------|-------------------|-----------|
| Management | Fully managed | You patch OS + SQL |
| HA | Built-in (geo-replication) | You configure Always On |
| Feature gaps | Some SQL Server features | Full SQL Server |
| Cost | DTU/vCore predictable | VM + license + ops time |
| Best for | New .NET + EF Core apps | Legacy migration phase 1 |

**Architect path:** Migrate to Azure SQL when possible. Stay on VM temporarily for: SQL Agent heavy jobs, CLR assemblies, specific trace flags, third-party SQL tools.

### Follow-up Questions

1. **Hyperscale tier?** For 100TB+, rapid autoscale — large SaaS databases.
2. **Elastic pool?** Multiple databases sharing resources — multi-tenant SaaS.

### Common Mistakes

- SQL on VM "because we always used SQL Server" — ignores managed benefits
- Azure SQL without index tuning — performance still your responsibility

---

## Q016: Cosmos DB Partition Key Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Azure Data |
| **Frequency** | Common |
| **Week** | 11 |

### Question

How do you choose a Cosmos DB partition key?

### Short Answer

Choose a property with high cardinality, even distribution, and that appears in most queries. Wrong key = hot partitions and 10x cost/ throttling.

### Detailed Answer

**Good keys:** `tenantId`, `userId`, `deviceId` — high cardinality, spread requests.

**Bad keys:** `status`, `country` (low cardinality), `timestamp` alone (hot partition on writes).

**Rules:**
- Partition key is immutable after container creation
- Queries without partition key = cross-partition scan (expensive)
- 20 GB logical partition limit — design for even growth

**Example — multi-tenant SaaS:** Partition key = `tenantId`. All queries scoped to tenant. RU/s scales per workload.

**Architect process:** Model access patterns first, then partition key. Load test with realistic distribution.

### Common Mistakes

- Choosing partition key after container created without access pattern analysis
- `/id` for everything when queries use `customerId`

---

## Q017: Cosmos DB Consistency Levels

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Azure Data |
| **Frequency** | Occasional |
| **Week** | 11 |

### Question

Explain Cosmos DB consistency levels. Which would you choose for an e-commerce inventory system?

### Short Answer

Strong to Eventual — five levels trading latency vs consistency. Inventory checkout: Strong or Bounded Staleness in single region; Session for user-scoped reads; avoid Eventual for stock counts.

### Detailed Answer

| Level | Behavior | Use Case |
|-------|----------|----------|
| Strong | Linearizable | Financial, inventory deduction |
| Bounded Staleness | Lag-bound | Globally distributed reads |
| Session | Consistent within user session | Shopping cart |
| Consistent Prefix | See writes in order | Social feeds |
| Eventual | Lowest latency, stale reads | Metrics, analytics |

**E-commerce:** Strong for inventory decrement at purchase. Product catalog can use Session or Eventual. Multi-region: Bounded Staleness with conflict resolution policy documented.

---

## Q018: Blob Storage Tiers and Lifecycle

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Azure Storage |
| **Frequency** | Common |
| **Week** | 11 |

### Question

Explain Blob storage tiers and lifecycle management.

### Short Answer

Hot (frequent access), Cool (30+ days), Cold (90+ days), Archive (rare, retrieval hours). Lifecycle policies auto-transition to optimize cost.

### Detailed Answer

**Tier selection:**
- Hot: images served to users, active uploads
- Cool: backups < 1 year, monthly reports
- Archive: compliance retention 7 years, legal hold

**Lifecycle policy example:** Move to Cool after 30 days, Archive after 365 days, delete after 2555 days.

**Architect:** Enable soft delete + versioning for ransomware protection. Private endpoints — no public blob access.

---

## Q019: Polyglot Persistence on Azure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Data Architecture |
| **Frequency** | Common |
| **Week** | 11, 08 |

### Question

Design data stores for an e-commerce platform on Azure.

### Short Answer

Azure SQL for orders/transactions (ACID). Cosmos DB or Redis for session/cart. Blob for product images. Event Hubs for clickstream. Synapse for analytics.

### Detailed Answer

| Data | Store | Why |
|------|-------|-----|
| Orders, payments | Azure SQL | ACID, relational |
| Shopping cart | Redis Cache | Fast, TTL |
| Product catalog | SQL or Cosmos | Depends on scale/schema flexibility |
| Images | Blob + CDN | Cost, global delivery |
| Search | Azure AI Search | Full-text, facets |
| Analytics | Event Hubs → Synapse | Decouple OLTP from OLAP |

**Anti-pattern:** One Cosmos DB for everything because "NoSQL scales."

---

## Q020: Azure SQL Geo-Replication and Failover Groups

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | DR |
| **Frequency** | Common |
| **Week** | 11, 16 |

### Question

How does Azure SQL auto-failover group work?

### Short Answer

Primary + secondary in paired region, automatic failover on region outage, connection via read-write listener endpoint. RPO typically < 5 seconds.

### Detailed Answer

1. Create failover group spanning two regions
2. Apps connect to `<group-name>.database.windows.net`
3. DNS automatically points to primary
4. On failover, secondary promoted, DNS updates
5. Test failover quarterly — applications must handle brief disconnect

**Architect:** Use with Front Door regional failover for full-stack DR. Document RTO (failover time ~30 sec–2 min) in runbook.

---

## Section 4: Identity & Security

## Q021: Managed Identity — System vs User Assigned

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Very Common |
| **Week** | 12 |

### Question

System-assigned vs user-assigned managed identity?

### Short Answer

System-assigned: lifecycle tied to resource, auto-created/deleted. User-assigned: independent resource, shared across multiple apps, survives app deletion.

### Detailed Answer

| Type | Created | Deleted | Share |
|------|---------|---------|-------|
| System-assigned | With resource | With resource | One per resource |
| User-assigned | Standalone | Manual | Many resources |

**Use system-assigned:** Single app to Key Vault/SQL — simplest.

**Use user-assigned:** Multiple apps same identity, slot swap scenarios, identity must outlive app, AKS pod identity patterns.

**Never:** Connection strings with passwords in app settings when Managed Identity works.

```csharp
// DefaultAzureCredential in .NET
var credential = new DefaultAzureCredential();
var client = new SecretClient(new Uri(keyVaultUrl), credential);
```

---

## Q022: OAuth 2.0 Client Credentials vs Auth Code PKCE

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |
| **Week** | 12 |

### Question

When client credentials vs authorization code with PKCE?

### Short Answer

Client credentials: service-to-service, no user. Auth code + PKCE: user delegation, SPAs and mobile apps.

### Detailed Answer

**Client credentials:** App registration with secret/cert, app calls API as itself. Order service → Inventory API.

**Auth code + PKCE:** User logs in via Entra ID, app gets token for user context. Web app, SPA (no client secret in browser).

**On-behalf-of (OBO):** API exchanges user token for downstream API token. User context flows through microservices.

**Architect:** API Management validates tokens at edge. Microservices use Managed Identity service-to-service where user context not needed.

---

## Q023: Key Vault Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |
| **Week** | 12 |

### Question

How do you integrate Key Vault with App Service?

### Short Answer

Managed Identity grants App Service access to Key Vault. Reference secrets in app settings as `@Microsoft.KeyVault(SecretUri=...)`. Enable soft delete and purge protection.

### Detailed Answer

1. Create Key Vault with RBAC (Key Vault Secrets User role)
2. Enable system/user-assigned MI on App Service
3. Assign MI to Key Vault role
4. App setting: `ConnectionStrings--Sql=@Microsoft.KeyVault(SecretUri=https://kv.vault.azure.net/secrets/sql/)`
5. Private Endpoint for Key Vault in production

**Rotation:** Dual-secret pattern — two active secrets, rotate without downtime. Event Grid trigger on expiration.

---

## Q024: Zero Trust on Azure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Security |
| **Frequency** | Common |
| **Week** | 14 |

### Question

Implement Zero Trust for an Azure .NET application.

### Short Answer

Verify explicitly (Entra ID + Conditional Access), least privilege (RBAC + MI), assume breach (segmentation, Private Link, Sentinel monitoring).

### Detailed Answer

**Verify explicitly:**
- MFA via Conditional Access
- Managed Identity over secrets
- Token validation at API Management

**Least privilege:**
- RBAC scoped to resource group
- Just-in-time VM access (Defender for Cloud)
- No Contributor in production for developers

**Assume breach:**
- Hub-spoke networking, no public DB endpoints
- Private Link for PaaS
- Microsoft Sentinel SIEM with KQL detection rules
- Encryption: TLS 1.2+, TDE on SQL, CMK for compliance

---

## Q025: Private Link vs Service Endpoints

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking / Security |
| **Frequency** | Common |
| **Week** | 13, 14 |

### Question

Private Link vs Service Endpoints?

### Short Answer

Service Endpoints: traffic over Azure backbone, service still has public IP. Private Link: private IP in your VNet, no public internet exposure. Prefer Private Link for production PaaS.

### Detailed Answer

| Feature | Service Endpoint | Private Link |
|---------|------------------|--------------|
| Exposure | Public IP exists | Private IP only |
| DNS | Public FQDN | Private DNS zone required |
| On-prem access | Via ExpressRoute + endpoint | Via ExpressRoute + Private Link |
| Cost | Free | Private Link hourly + data |

**Architect default:** Private Link for SQL, Storage, Key Vault in production.

---

## Q026: Microsoft Defender for Cloud

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Occasional |
| **Week** | 14 |

### Question

What does Defender for Cloud provide?

### Short Answer

CSPM (secure score, recommendations), workload protection (Defender for App Service, SQL, Storage, Containers), regulatory compliance dashboards.

### Detailed Answer

Enable on all subscriptions. Review secure score weekly. Critical recommendations: MFA, NSG rules, public storage, unpatched VMs. Integrate with Sentinel for alert routing. Not a replacement for secure architecture — additive monitoring.

---

## Q027: WAF on Application Gateway vs Front Door

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |
| **Week** | 13, 14 |

### Question

Where do you place WAF for a global Azure application?

### Short Answer

Front Door Premium for global edge WAF + CDN. Application Gateway WAF for regional apps behind VNet. Often both: Front Door global, App Gateway regional.

### Detailed Answer

**Front Door WAF:** OWASP rules, bot protection, geo-filtering, DDoS at edge, global.

**App Gateway WAF:** Regional, VNet-integrated backends, cookie-based session affinity.

**Defense in depth:** Front Door → App Gateway WAF → NSG → App → Private Link SQL.

---

## Q028: Entra ID Conditional Access

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Identity |
| **Frequency** | Occasional |
| **Week** | 12, 14 |

### Question

Give examples of Conditional Access policies for production Azure access.

### Short Answer

Require MFA for all admins, block legacy auth, require compliant device for production subscription access, block sign-in from non-approved countries.

### Detailed Answer

Policies evaluate: user, app, location, device state, risk level.

Examples:
- Admin roles → MFA + Privileged Identity Management (JIT)
- Azure Portal prod subscription → compliant device + trusted location
- Block sign-ins from high-risk countries
- Require MFA for service principal secrets (prefer certs)

---

## Q029: OWASP Top 10 on Azure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |
| **Week** | 14 |

### Question

How do you address OWASP Top 10 for an Azure-hosted .NET API?

### Short Answer

Broken access control → Entra ID + RBAC. Injection → parameterized queries, EF Core. Misconfiguration → Policy, Defender. Logging → App Insights + Sentinel. Crypto → TLS, Key Vault.

### Detailed Answer

| OWASP Risk | Azure Mitigation |
|------------|------------------|
| Broken Access Control | Entra ID, APIM auth, RBAC |
| Cryptographic Failures | TLS 1.2+, Key Vault, TDE |
| Injection | EF Core, input validation, WAF |
| Insecure Design | Threat modeling, WAF review |
| Security Misconfiguration | Azure Policy, Defender |
| Vulnerable Components | Dependabot, Defender CVE |
| Auth Failures | Entra ID, MFA, PKCE |
| Software/Data Integrity | Signed deployments, SBOM |
| Logging Failures | App Insights, Sentinel |
| SSRF | VNet egress control, Firewall |

---

## Q030: Service Principal vs Managed Identity

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Identity |
| **Frequency** | Common |
| **Week** | 12 |

### Question

When service principal vs managed identity?

### Short Answer

Managed Identity for Azure resources (App Service, VM, Function). Service principal for CI/CD pipelines, external apps, on-prem systems calling Azure.

### Detailed Answer

**Managed Identity:** Azure manages credential rotation, no secret in code. Preferred for all Azure-hosted apps.

**Service principal:** App registration + client secret or certificate. GitHub Actions deploying to Azure, on-prem ETL to Blob Storage.

**Best practice:** Federated credentials (OIDC) for GitHub Actions — no long-lived secrets. Certificate over secret for SP when needed.

### Common Mistakes

- Client secrets in GitHub repos
- Service principal in App Service instead of Managed Identity

---

| Q# | Topic |
|----|-------|
| Q009–Q014 | Compute |
| Q015–Q020 | Data |
| Q021–Q030 | Identity & Security |

**Next:** [Part 3 — Q031–Q050](azure-top-50-qa-part3.md)
