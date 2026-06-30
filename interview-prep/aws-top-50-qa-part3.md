# AWS Top 50 — Part 3 (Q031–Q050)

> Multi-Cloud & Architecture Scenarios | [Part 1](aws-top-50-qa-part1.md) | [Part 2](aws-top-50-qa-part2.md)

---

## Q031: Azure App Service vs AWS Elastic Beanstalk

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Multi-Cloud |
| **Frequency** | Common |
| **Week** | 20 |

### Question

Compare Azure App Service and AWS Elastic Beanstalk for hosting .NET 8 APIs.

### Short Answer (30 seconds)

Both are PaaS for web apps. App Service has richer deployment slots, VNet integration, and tighter Entra ID integration. Beanstalk is simpler but less feature-rich — good for AWS-native .NET migration.

### Detailed Answer (3–5 minutes)

| Feature | App Service | Elastic Beanstalk |
|---------|-------------|-------------------|
| Deployment slots | Built-in blue-green | Rolling deploy |
| Autoscale | Rich rules | ASG-based |
| Identity | Managed Identity | IAM instance profile |
| .NET support | Excellent | Good |
| Private networking | VNet integration | VPC private subnets |
| Cost model | Plan-based | EC2 underlying cost |

**Architect recommendation for .NET shop on Azure:** App Service. **Migrating Azure → AWS with minimal change:** Beanstalk first, then containers (ECS) when needed.

### Common Mistakes

- Assuming feature parity — slots, Private Link patterns differ
- Not comparing underlying compute cost (Beanstalk = EC2 bill)

---

## Q032: Azure Service Bus vs Amazon SQS/SNS

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Multi-Cloud Messaging |
| **Frequency** | Common |
| **Week** | 20 |

### Question

Map Azure messaging to AWS equivalents.

### Short Answer

Service Bus Queue ≈ SQS. Service Bus Topic ≈ SNS + SQS fan-out. Event Grid ≈ EventBridge. Event Hubs ≈ Kinesis.

### Detailed Answer

| Azure | AWS | Key Difference |
|-------|-----|----------------|
| Service Bus | SQS + SNS | SB: sessions, transactions, larger messages (Premium) |
| Event Grid | EventBridge | Both push event routers |
| Event Hubs | Kinesis | EH: Kafka API available |
| Queue storage | SQS | Legacy, use SQS |

**Portability:** Abstract with MassTransit, NServiceBus, or custom interface — swap transport via config.

---

## Q033: Entra ID vs AWS IAM Identity Center

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Multi-Cloud Identity |
| **Frequency** | Occasional |
| **Week** | 20 |

### Question

How do enterprises manage identity across Azure and AWS?

### Short Answer

Entra ID as central IdP. AWS IAM Identity Center (SSO) federated to Entra ID. Single sign-on to both clouds. Separate RBAC per cloud — no unified RBAC across clouds.

### Detailed Answer

**Pattern:**
1. Entra ID — source of truth for users/groups
2. SAML/OIDC federation → AWS IAM Identity Center
3. Permission sets map groups to AWS accounts/roles
4. Azure RBAC assignments for same groups in Entra ID

**Architect:** Document identity architecture in ADR. Regular access reviews both clouds.

---

## Q034: Vendor Lock-In — What Is Portable?

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Multi-Cloud Strategy |
| **Frequency** | Common |
| **Week** | 20 |

### Question

What is portable across Azure and AWS? What creates lock-in?

### Short Answer

Portable: Kubernetes, Terraform, PostgreSQL, .NET code, OpenTelemetry, Docker. Locked: proprietary PaaS APIs (Cosmos DB API, DynamoDB API), managed service-specific features, identity integrations.

### Detailed Answer

**Portable stack:**
- .NET 8 microservices in containers
- PostgreSQL (RDS / Azure PostgreSQL)
- Redis (ElastiCache / Azure Cache)
- Terraform modules (with provider abstraction)
- OpenTelemetry → any backend

**Accept lock-in consciously:**
- Cosmos DB multi-region consistency
- Azure OpenAI / Bedrock specific APIs
- Deep Entra Conditional Access

**Architect:** "Portable where it matters, managed where it wins" — document decision per service.

---

## Q035: Multi-Cloud Disaster Recovery

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | DR |
| **Frequency** | Occasional |
| **Week** | 20 |

### Question

Design DR using Azure primary and AWS secondary.

### Short Answer

Active-passive: DNS failover (Route 53/Front Door) to secondary region/cloud. Replicate data async (DB replication or event-driven sync). Runbooks for cross-cloud failover. Expensive — justify with regulatory or extreme SLA needs.

### Detailed Answer

**Challenges:**
- Data replication lag across clouds
- Different IaC (Bicep + Terraform)
- Identity federation complexity
- Egress costs for replication
- Operational skill on both platforms

**When justified:** Government, finance regulatory requirements. Not for cost optimization.

**Simpler alternative:** Multi-region single cloud (Azure East + West Europe) before multi-cloud DR.

---

## Q036: Cost Comparison Methodology

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | FinOps |
| **Frequency** | Common |
| **Week** | 20 |

### Question

How do you compare Azure vs AWS costs for the same workload?

### Short Answer

Same architecture diagram, equivalent SLA tier, both pricing calculators, include egress/data transfer, 1-year reserved pricing, operational labor cost, 3-year TCO.

### Detailed Answer

**Checklist:**
1. Normalize instance sizes (vCPU, RAM)
2. Multi-AZ / zone redundancy on both
3. Backup retention same
4. Data egress estimates (often surprise)
5. Support plan costs
6. Engineer hourly rate × ops complexity
7. Licensing (SQL Server AHUB on Azure/AWS)

**Result:** Often within 10-20% — decision rarely pure cost. Team skills and ecosystem matter more.

---

## Q037: Landing Zone — Azure vs AWS

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Cloud Governance |
| **Frequency** | Common |
| **Week** | 09, 17 |

### Question

Compare Azure Landing Zone and AWS Control Tower.

### Short Answer

Both automate multi-account/subscription governance. Azure: CAF + ALZ Bicep/Terraform. AWS: Control Tower + Organizations + SCPs. Same concepts: hierarchy, guardrails, network hub, identity.

### Detailed Answer

| Concept | Azure | AWS |
|---------|-------|-----|
| Hierarchy | Management Groups | OUs |
| Account unit | Subscription | Account |
| Guardrails | Azure Policy | SCP |
| Hub network | vWAN / Hub VNet | Transit Gateway |
| Identity | Entra ID | IAM Identity Center |
| Automation | ALZ Accelerator | Control Tower |

**Multi-cloud architect:** Learn both — enterprises increasingly have both.

---

## Q038: .NET on Azure vs .NET on AWS — Architect View

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | .NET Cloud |
| **Frequency** | Very Common |
| **Week** | 20 |

### Question

As a .NET architect, when recommend Azure vs AWS?

### Short Answer

Azure default for Microsoft shops (Entra, EA, Visual Studio, Azure OpenAI). AWS when client mandate, broader SaaS ecosystem, specific AWS services (Bedrock model choice), or team AWS expertise.

### Detailed Answer

**Lean Azure:**
- Microsoft EA / M365 / Entra already
- Azure OpenAI, Fabric, Synapse integration
- Team Visual Studio / Azure DevOps
- .NET + Azure documentation depth

**Lean AWS:**
- Startup with AWS-native culture
- Broader region/service catalog historically
- Specific ML services on Bedrock/SageMaker
- Acquisition brought AWS estate

**Interview answer:** "I'm cloud-agnostic at architecture level — I map requirements to services on either platform. For .NET enterprises, Azure is natural default, but I design for portability where strategic."

---

## Q039: API Management — Azure APIM vs AWS API Gateway

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | API Architecture |
| **Frequency** | Common |
| **Week** | 15, 20 |

### Question

Compare Azure API Management and AWS API Gateway.

### Short Answer

Both: auth, rate limit, versioning, developer portal. APIM richer policy language, self-hosted gateway option. API Gateway tighter Lambda integration, lower cost at scale for simple APIs.

### Detailed Answer

| Feature | APIM | API Gateway |
|---------|------|-------------|
| Developer portal | Built-in | Limited (third-party) |
| Self-hosted gateway | Yes | No |
| Lambda integration | Via HTTP | Native |
| Pricing | Tier-based | Per-request |
| WAF integration | Front Door | AWS WAF |

---

## Q040: Observability — App Insights vs CloudWatch

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Observability |
| **Frequency** | Common |
| **Week** | 32 |

### Question

Compare Azure Monitor/App Insights and AWS CloudWatch/X-Ray.

### Short Answer

Both cover logs, metrics, traces. App Insights stronger .NET integration out-of-box. CloudWatch universal for AWS services. Prefer OpenTelemetry for multi-cloud abstraction.

### Detailed Answer

**Architect standard:** OpenTelemetry SDK in .NET → export to App Insights OR X-Ray based on deployment cloud. Same instrumentation code, different exporter.

---

## Q041: Step Functions vs Durable Functions

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Orchestration |
| **Frequency** | Occasional |
| **Week** | 20 |

### Question

AWS Step Functions vs Azure Durable Functions for saga orchestration?

### Short Answer

Both orchestrate workflows. Durable Functions: C# code, familiar to .NET teams on Azure. Step Functions: JSON ASL or CDK, native AWS, visual workflow.

### Detailed Answer

**Durable Functions:** Write saga as async C# methods — easier for .NET developers.

**Step Functions:** Standard (exactly-once, 1 year) vs Express (high volume, at-least-once).

**Architect:** Match to cloud.primary. Abstract saga logic in domain layer where possible.

---

## Q042: RDS SQL Server vs Azure SQL

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Database |
| **Frequency** | Common |
| **Week** | 20 |

### Question

RDS SQL Server vs Azure SQL Database for .NET apps?

### Short Answer

Both managed SQL. Azure SQL tighter Entra auth, hybrid benefit for Microsoft licenses. RDS SQL Server familiar if already on AWS. Feature gaps differ — verify before migration.

### Detailed Answer

**.NET + EF Core:** Works identically on both.

**Decision factors:** Cloud affinity, licensing (AHUB), geo-replication features, DBA team familiarity.

---

## Q043: EKS vs AKS

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Kubernetes |
| **Frequency** | Common |
| **Week** | 27 |

### Question

EKS vs AKS — key differences for architects?

### Short Answer

Both managed K8s. AKS: Azure integration (Entra workload ID, Azure Monitor). EKS: AWS integration (IAM IRSA, CloudWatch). K8s API portable — workloads largely migrate.

### Detailed Answer

| Integration | AKS | EKS |
|-------------|-----|-----|
| Identity | Entra Workload ID | IRSA |
| Monitoring | Azure Monitor | CloudWatch |
| Ingress | App Gateway, NGINX | ALB Ingress |
| Cost | No control plane fee (Standard) | $0.10/hr control plane |

**Portable:** Helm charts, GitOps (ArgoCD), most K8s manifests.

---

## Q044: SaaS Multi-Tenant on AWS

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Architecture Scenario |
| **Frequency** | Common |
| **Week** | 20 |

### Question

Design multi-tenant SaaS on AWS for 5000 tenants.

### Short Answer

Pool: shared RDS with `tenantId` + RLS. Silo: database per tenant for enterprise tier. Bridge: shared app, isolated schemas. Route 53 + CloudFront at edge. Cognito user pools per tenant or custom attributes.

### Detailed Answer

| Model | Isolation | Cost | Complexity |
|-------|-----------|------|------------|
| Pooled | Row-level | Lowest | Lowest |
| Silo | DB per tenant | Highest | Highest |
| Bridge | Schema per tenant | Medium | Medium |

**Start pooled.** Offer silo as premium tier. DynamoDB `tenantId` partition key for NoSQL variant.

---

## Q045: Serverless .NET API — Lambda vs Azure Functions

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Serverless |
| **Frequency** | Common |
| **Week** | 18, 10 |

### Question

Compare AWS Lambda and Azure Functions for .NET 8.

### Short Answer

Both support .NET isolated worker. Functions: tighter Azure integration, Durable Functions. Lambda: larger ecosystem, API Gateway integration. Cold start similar — mitigate with provisioned concurrency / premium plans.

### Detailed Answer

Feature parity for basic HTTP triggers. Choose based on cloud.primary. Use ASP.NET Core minimal hosting model in both (.NET 8 isolated worker).

---

## Q046: Data Egress Cost Trap

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | FinOps |
| **Frequency** | Common |
| **Week** | 20 |

### Question

Why is data egress the hidden cost in cloud comparisons?

### Short Answer

Ingress usually free. Egress to internet or cross-region/cloud charged per GB. Multi-region active-active, CDN misconfiguration, cross-cloud replication — egress explodes.

### Detailed Answer

**Mitigation:**
- CloudFront/Front Door caching
- Keep data processing in same region as storage
- VPC endpoints (avoid NAT Gateway for AWS services)
- Compress API responses
- Monitor egress in Cost Explorer / Cost Management

**Architect:** Include egress in every architecture cost estimate.

---

## Q047: Migration — Azure to AWS

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Migration Scenario |
| **Frequency** | Occasional |
| **Week** | 20 |

### Question

Outline migration plan for .NET app from Azure to AWS.

### Short Answer

Assess (6 Rs), map services, IaC on AWS, data migration (DMS), parallel run, DNS cutover, 3-6 months minimum for non-trivial app.

### Detailed Answer

| Azure | AWS Target |
|-------|------------|
| App Service | Beanstalk / ECS |
| Azure SQL | RDS SQL Server |
| Service Bus | SQS/SNS |
| Key Vault | Secrets Manager |
| Entra ID | Cognito + IAM Identity Center |
| App Insights | X-Ray + CloudWatch |

**Phases:** Rehost → Refactor identity/messaging → Optimize (Graviton, Spot).

---

## Q048: Hybrid Cloud Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Hybrid |
| **Frequency** | Occasional |
| **Week** | 19, 13 |

### Question

Design hybrid cloud connecting on-premises .NET apps to AWS.

### Short Answer

Direct Connect or VPN to VPC. RDS in VPC private subnet. On-prem AD federated to IAM Identity Center. No public database endpoints. Consider AWS Outposts for ultra-low latency.

### Detailed Answer

**Connectivity:** DX primary + VPN backup.

**Identity:** AD Connect → Entra → AWS SSO OR direct AD federation.

**Data:** Database Migration Service for phased migration.

**Architect:** Hybrid adds complexity — justify with compliance or migration transition, not permanent state.

---

## Q049: Architecture Scenario — Fintech on AWS

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Capstone |
| **Frequency** | Common |
| **Week** | 20 |

### Question

Design PCI-compliant payment API on AWS (.NET 8, 10K TPS, 99.99% SLA).

### Short Answer

VPC isolated payment subnet, ECS Fargate, RDS Multi-AZ, Secrets Manager, API Gateway + WAF, no card data stored (tokenization via Stripe), CloudTrail audit, encryption everywhere.

### Detailed Answer

**PCI scope reduction:** Use Stripe/payment processor — SAQ A, not full PCI DSS on your infrastructure.

**Architecture:**
- API Gateway (WAF, throttling) → ALB → Payment service (Fargate, private subnet)
- RDS PostgreSQL Multi-AZ (encrypted, CMK)
- SQS for async settlement notifications
- No card numbers in logs (structured logging with redaction)
- GuardDuty + Security Hub
- Multi-AZ mandatory, RTO < 15 min

**Cost estimate:** $3-5K/month at moderate scale.

---

## Q050: Multi-Cloud Capstone — Board Asks "Why Not Both?"

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Executive Scenario |
| **Frequency** | Common |
| **Week** | 20 |

### Question

Board mandates multi-cloud (Azure AND AWS). How do you respond as lead architect?

### Short Answer

Clarify objective: avoid lock-in, acquisition integration, or geopolitical? Propose targeted multi-cloud (specific workloads) not duplicate everything. Document 2x operational cost. Start with portable layer (K8s, Terraform, OTel).

### Detailed Answer

**Executive response framework:**
1. **Clarify goal** — risk reduction vs vendor negotiation vs regulatory
2. **Cost of multi-cloud** — 1.5-2.5x ops headcount, dual expertise, egress
3. **Propose strategy tiers:**
   - **Tier 1:** Portable apps on K8s — deployable either cloud
   - **Tier 2:** Cloud-specific managed services where they win (Azure OpenAI, AWS Bedrock)
   - **Tier 3:** Single-cloud primary, other cloud for DR only (if justified)
4. **Reject:** Running every workload twice "for redundancy"
5. **Metrics:** Track operational burden, incident MTTR per cloud

**Interview gold:** Shows executive communication, not just technical depth.

### Common Mistakes

- Blindly agreeing to run everything on both clouds
- No portable abstraction strategy
- Ignoring operational cost in ROI

---

## Master Index — AWS Top 50

| Q# | Topic | Week |
|----|-------|------|
| Q001-Q008 | WAF, IAM, Organizations | 17 |
| Q009-Q014 | Compute (EC2, Lambda, ECS) | 18 |
| Q015-Q020 | Data (S3, RDS, DynamoDB, VPC) | 19 |
| Q021-Q030 | Identity, Messaging, Security | 17-19 |
| Q031-Q040 | Multi-cloud comparison | 20 |
| Q041-Q046 | Service mapping, FinOps | 20 |
| Q047-Q050 | Migration & capstone scenarios | 20 |
