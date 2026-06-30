# AWS Top 50 — Part 2 (Q009–Q030)

> Compute, VPC, Identity | [Part 1](aws-top-50-qa-part1.md) | [Part 3](aws-top-50-qa-part3.md)

---

## Q009: EC2 vs Lambda vs ECS Fargate

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | AWS Compute |
| **Frequency** | Very Common |
| **Week** | 18 |

### Question

When EC2 vs Lambda vs ECS Fargate for a .NET workload?

### Short Answer (30 seconds)

EC2 for full control and steady high traffic. Lambda for event-driven short tasks. Fargate for containers without managing servers. Default .NET API: Fargate or Elastic Beanstalk; Lambda for async handlers.

### Detailed Answer (3–5 minutes)

| Factor | EC2 | Lambda | ECS Fargate |
|--------|-----|--------|-------------|
| Ops burden | High (patching) | Low | Medium |
| Cold start | No | Yes (unless provisioned) | Minimal |
| Max duration | Unlimited | 15 min | Unlimited |
| Cost at low traffic | Fixed | Near zero | Per-task pricing |
| Cost at steady high | RI/SP savings | Can exceed EC2 | Competitive |

**.NET patterns:**
- **Elastic Beanstalk** — fastest PaaS-like .NET deploy (Azure App Service equivalent)
- **Lambda** — S3 upload trigger, SQS consumer, scheduled job
- **Fargate** — containerized .NET 8 microservices without K8s
- **EC2** — legacy, custom AMIs, Windows-specific needs

**Architect:** Start Beanstalk or Fargate. Lambda for events. EC2 only with justification.

### Follow-up Questions

1. **Lambda .NET cold start?** Mitigate with Provisioned Concurrency, Native AOT (where supported), smaller deployment package.
2. **Fargate vs EKS?** Fargate = no node management. EKS = full K8s when needed.

### Common Mistakes in Interviews

- Lambda for always-on REST API with steady traffic
- EC2 without considering patching burden

---

## Q010: Lambda Event Sources and Limits

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | AWS Lambda |
| **Frequency** | Common |
| **Week** | 18 |

### Question

What are key Lambda limits and common event sources?

### Short Answer

15-min timeout, 10GB memory, 250MB deployment package (zipped), 1000 concurrent executions default (soft limit). Triggers: API Gateway, SQS, SNS, S3, DynamoDB Streams, EventBridge.

### Detailed Answer

**Design constraints:**
- No persistent local disk — use /tmp (512MB-10GB)
- Stateless — store state in DynamoDB/S3
- VPC Lambda adds cold start latency (ENI setup) — avoid unless PrivateLink required

**Event sources:**
| Source | Pattern |
|--------|---------|
| API Gateway | HTTP API (v2) preferred over REST for cost |
| SQS | Batch processing, partial batch failure reporting |
| EventBridge | Event-driven architecture hub |
| DynamoDB Streams | CDC, trigger on table changes |

**Architect:** SQS + Lambda for backpressure — queue depth triggers scaling.

---

## Q011: ECS vs EKS Decision

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | AWS Containers |
| **Frequency** | Common |
| **Week** | 18 |

### Question

ECS vs EKS — when would you choose each?

### Short Answer

ECS for AWS-native container orchestration with lower ops. EKS for Kubernetes API, multi-cloud portability, service mesh ecosystem.

### Detailed Answer

| Criteria | ECS + Fargate | EKS |
|----------|---------------|-----|
| K8s skills required | No | Yes |
| Portability | AWS | Multi-cloud |
| Service mesh | App Mesh | Istio, Linkerd |
| Community tooling | AWS-centric | Full K8s ecosystem |
| Control plane cost | Free (Fargate per task) | $0.10/hr per cluster |

**Choose ECS:** Team knows Docker, AWS-only, simpler ops, 5-20 services.

**Choose EKS:** Existing K8s investment, Helm charts, GitOps (ArgoCD), multi-cloud mandate.

**Azure mapping:** ECS ≈ Container Apps. EKS ≈ AKS.

---

## Q012: Elastic Beanstalk for .NET

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | AWS PaaS |
| **Frequency** | Common |
| **Week** | 18 |

### Question

What is Elastic Beanstalk and when use it for .NET?

### Short Answer

PaaS that provisions EC2, load balancer, auto-scaling from your deployment package. Closest AWS equivalent to Azure App Service for .NET.

### Detailed Answer

Upload .NET publish zip → Beanstalk handles capacity, health monitoring, rolling deploy.

**Pros:** Fastest .NET on AWS path, familiar to App Service users.

**Cons:** Less flexible than ECS/EKS, AWS-specific, limited compared to App Service deployment slots.

**Architect:** Good for migration from Azure App Service to AWS with minimal container investment.

---

## Q013: Auto Scaling Groups

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | AWS Compute |
| **Frequency** | Common |
| **Week** | 18 |

### Question

How do EC2 Auto Scaling Groups work?

### Short Answer

Maintain desired capacity across AZs. Scale on CloudWatch alarms (CPU, custom metrics, ALB request count). Launch template defines instance config.

### Detailed Answer

**Policies:**
- Target tracking — maintain 50% CPU
- Step scaling — add 2 instances when CPU > 70%
- Scheduled — scale up before known peak

**Architect:** Combine ASG with ALB health checks. Grace period for app warmup. Use mixed instances policy (On-Demand + Spot) for cost.

---

## Q014: Graviton Instances

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Cost / Performance |
| **Frequency** | Occasional |
| **Week** | 18 |

### Question

What are AWS Graviton instances and when use them?

### Short Answer

ARM-based AWS processors — up to 40% better price-performance. Use for .NET 8 (ARM supported), Linux workloads, ElastiCache, RDS.

### Detailed Answer

**.NET 8** runs on ARM64 Linux. Test compatibility before migration. Graviton2/3/4 generations.

**WAF Sustainability pillar:** Graviton uses less energy — dual cost + sustainability win.

**Caveat:** Verify all native dependencies support ARM.

---

## Q015: S3 Storage Classes

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | AWS Storage |
| **Frequency** | Very Common |
| **Week** | 19 |

### Question

Explain S3 storage classes and lifecycle policies.

### Short Answer

Standard (frequent), IA (infrequent), Glacier Instant/Flexible/Deep Archive (archive). Lifecycle rules auto-transition. Intelligent-Tiering for unknown patterns.

### Detailed Answer

| Class | Retrieval | Min Duration | Use |
|-------|-----------|--------------|-----|
| Standard | Immediate | — | Active data |
| Standard-IA | Immediate | 30 days | Backups |
| Glacier Instant | Milliseconds | 90 days | Archive with rare access |
| Glacier Flexible | Minutes-hours | 90 days | Compliance archive |
| Deep Archive | 12 hours | 180 days | Long-term retention |

**Security:** Block public access account-wide. Versioning + MFA Delete. S3 Object Lock for compliance.

**Azure mapping:** Standard ≈ Hot, IA ≈ Cool, Glacier ≈ Archive.

---

## Q016: RDS Multi-AZ vs Read Replicas

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | AWS RDS |
| **Frequency** | Very Common |
| **Week** | 19 |

### Question

RDS Multi-AZ vs Read Replicas?

### Short Answer

Multi-AZ: synchronous standby for HA failover (not for reads). Read Replicas: async copies for read scaling and cross-region DR.

### Detailed Answer

**Multi-AZ:** Automatic failover, same region, ~60-120 sec failover, doubles cost.

**Read Replica:** Scale read traffic, can promote to standalone, cross-region for DR.

**Architect:** Production OLTP: Multi-AZ mandatory. Add read replicas when read/write ratio > 10:1.

**Azure mapping:** Multi-AZ ≈ zone redundant. Read replica ≈ Azure SQL geo-secondary (readable).

---

## Q017: DynamoDB Partition Key Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | AWS NoSQL |
| **Frequency** | Common |
| **Week** | 19 |

### Question

How do you design DynamoDB partition keys?

### Short Answer

High cardinality, even distribution, known in most queries. Bad keys cause hot partitions and throttling.

### Detailed Answer

Same principles as Cosmos DB partition key.

**Patterns:**
- `userId` — user-scoped data
- Composite: `tenantId#orderId`
- Write sharding: add random suffix for hot keys (`userId#shard{N}`)

**GSI/LSI:** Secondary access patterns — design GSIs upfront (limited 20 GSIs).

**Capacity:** On-demand for unpredictable. Provisioned for steady with auto-scaling.

---

## Q018: VPC Subnet Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | AWS Networking |
| **Frequency** | Very Common |
| **Week** | 19 |

### Question

Design VPC subnets for a 3-tier .NET application.

### Short Answer

Public subnets: ALB only. Private app subnets: EC2/ECS/Lambda. Private data subnets: RDS (no internet route). NAT Gateway for outbound from private subnets.

### Detailed Answer

```
VPC 10.0.0.0/16
├── Public 10.0.1.0/24 (AZ-a) — ALB, NAT GW
├── Public 10.0.2.0/24 (AZ-b) — ALB, NAT GW
├── Private App 10.0.10.0/24 (AZ-a) — ECS tasks
├── Private App 10.0.11.0/24 (AZ-b) — ECS tasks
├── Private Data 10.0.20.0/24 (AZ-a) — RDS primary
└── Private Data 10.0.21.0/24 (AZ-b) — RDS standby
```

**Security Groups:** Stateful — allow ALB → app on 443, app → RDS on 1433.

**NACLs:** Stateless subnet firewall — optional extra layer.

**Cost:** NAT Gateway ~$32/month + data processing — consider NAT instance for dev only.

---

## Q019: ALB vs NLB vs API Gateway

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | AWS Networking |
| **Frequency** | Common |
| **Week** | 19 |

### Question

ALB vs NLB vs API Gateway?

### Short Answer

ALB: L7 HTTP routing. NLB: L4 TCP ultra-low latency, static IP. API Gateway: managed API edge with auth, throttling, serverless integration.

### Detailed Answer

| LB | Layer | Use |
|----|-------|-----|
| ALB | L7 | Web APIs, path routing, WebSocket |
| NLB | L4 | TCP, millions RPS, static IP |
| API Gateway | L7 API | Serverless, API management features |

**Pattern:** API Gateway → Lambda (serverless). ALB → ECS (containers). CloudFront → ALB (global).

---

## Q020: Route 53 Routing Policies

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | AWS DNS |
| **Frequency** | Occasional |
| **Week** | 19 |

### Question

Route 53 routing policies for DR?

### Short Answer

Failover: active-passive health check failover. Weighted: canary traffic split. Geolocation: route by user location. Latency: lowest latency region.

### Detailed Answer

**Failover DR:** Primary ALB health check fails → DNS routes to secondary region.

**Limitation:** DNS TTL propagation delay (60-300 sec). Use CloudFront or Global Accelerator for faster failover.

---

## Q021: Cognito vs IAM for User Auth

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | AWS Identity |
| **Frequency** | Common |
| **Week** | 17, 12 |

### Question

Cognito vs IAM for application user authentication?

### Short Answer

Cognito for end users (sign-up, MFA, social login, JWT). IAM for AWS service access and developers. Never use IAM users for app customers.

### Detailed Answer

**Cognito User Pools:** User directory, OAuth/OIDC, JWT for API Gateway/App.

**Cognito Identity Pools:** Federated AWS credentials for direct S3/DynamoDB access from mobile.

**Azure mapping:** Cognito User Pool ≈ Entra ID B2C / External ID.

---

## Q022: Secrets Manager vs Parameter Store

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | AWS Secrets |
| **Frequency** | Common |
| **Week** | 19 |

### Question

Secrets Manager vs Systems Manager Parameter Store?

### Short Answer

Secrets Manager: automatic rotation, higher cost, secrets/credentials. Parameter Store: config values, SecureString, free tier, manual rotation.

### Detailed Answer

**Secrets Manager:** RDS password auto-rotation, Lambda rotation functions.

**Parameter Store:** Feature flags, connection strings (if manual rotation OK).

**Azure mapping:** Both ≈ Key Vault (Secrets Manager closer for rotation).

---

## Q023: SQS vs SNS vs EventBridge

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | AWS Messaging |
| **Frequency** | Very Common |
| **Week** | 15, 19 |

### Question

SQS vs SNS vs EventBridge?

### Short Answer

SQS: queue, one consumer per message, pull. SNS: pub/sub fan-out, push. EventBridge: event bus, routing rules, schema registry, SaaS integrations.

### Detailed Answer

| Service | Pattern | Azure Equivalent |
|---------|---------|------------------|
| SQS | Queue | Service Bus Queue |
| SNS | Pub/sub | Event Grid / Service Bus Topic |
| EventBridge | Event router | Event Grid |

**Fan-out:** SNS → multiple SQS queues (each service gets copy).

**EventBridge:** Route `order.placed` to Lambda + SQS + Step Functions based on rules.

---

## Q024: Kinesis vs SQS

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | AWS Streaming |
| **Frequency** | Occasional |
| **Week** | 19 |

### Question

Kinesis vs SQS for event processing?

### Short Answer

Kinesis: high-throughput streaming, multiple consumers read same stream, ordering per partition key. SQS: task queue, one consumer per message, simpler.

### Detailed Answer

**Kinesis Data Streams:** Real-time analytics, clickstream, replay capability.

**Kinesis Firehose:** Load stream to S3/Redshift/OpenSearch without code.

**Azure mapping:** Kinesis ≈ Event Hubs.

---

## Q025: AWS WAF and Shield

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | AWS Security |
| **Frequency** | Common |
| **Week** | 19 |

### Question

AWS WAF vs Shield?

### Short Answer

WAF: application layer rules (OWASP, rate limit, geo block). Shield Standard: free DDoS protection L3/L4. Shield Advanced: enhanced DDoS + cost protection + SA support.

### Detailed Answer

Attach WAF to CloudFront, ALB, API Gateway.

**Architect:** WAF on all public endpoints. Managed rule groups (AWSManagedRulesCommonRuleSet). Rate-based rules for brute force.

---

## Q026: Transit Gateway

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | AWS Networking |
| **Frequency** | Occasional |
| **Week** | 19 |

### Question

What is AWS Transit Gateway?

### Short Answer

Hub for VPC connectivity at scale — replaces full mesh VPC peering. Connect VPCs, VPN, Direct Connect to central hub.

### Detailed Answer

**vs VPC Peering:** N VPCs = N(N-1)/2 peerings. Transit Gateway = N attachments.

**Azure mapping:** Transit Gateway ≈ Azure Virtual WAN hub.

**Use:** Enterprise with 10+ VPCs, shared services account pattern.

---

## Q027: Direct Connect vs VPN

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hybrid |
| **Frequency** | Occasional |
| **Week** | 19 |

### Question

Direct Connect vs Site-to-Site VPN?

### Short Answer

VPN: IPsec over internet, hours to setup, low cost. Direct Connect: dedicated private connection, predictable latency, weeks-months, higher cost.

### Detailed Answer

**Architect:** VPN for migration POC. Direct Connect for production hybrid at scale. Use both: DX primary, VPN backup.

**Azure mapping:** Direct Connect ≈ ExpressRoute. VPN ≈ VPN Gateway.

---

## Q028: CloudFormation vs CDK vs Terraform

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | IaC |
| **Frequency** | Common |
| **Week** | 31 |

### Question

CloudFormation vs CDK vs Terraform on AWS?

### Short Answer

CloudFormation: native AWS JSON/YAML. CDK: code (C#/TypeScript) generates CloudFormation. Terraform: multi-cloud HCL.

### Detailed Answer

**.NET shop:** CDK with C# — type-safe IaC, generates CloudFormation.

**Multi-cloud:** Terraform with AWS provider.

**Architect:** Pick one standard per org. Store in Git, PR review, drift detection.

---

## Q029: X-Ray and Distributed Tracing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Observability |
| **Frequency** | Common |
| **Week** | 32 |

### Question

How does AWS X-Ray help microservices?

### Short Answer

Distributed tracing — visualize request flow across Lambda, ECS, API Gateway. Service map, latency analysis, error root cause.

### Detailed Answer

**OpenTelemetry:** Preferred modern approach — vendor-neutral, export to X-Ray or others.

**.NET:** `AWSXRayRecorder` or OpenTelemetry SDK with X-Ray exporter.

**Azure mapping:** X-Ray ≈ Application Insights distributed tracing.

---

## Q030: ECR and Container Image Security

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | AWS Containers |
| **Frequency** | Occasional |
| **Week** | 18 |

### Question

How do you secure container images in ECR?

### Short Answer

Scan on push (Basic/Enhanced), immutable tags, lifecycle policies, least-privilege IAM, sign with Notation/Cosign.

### Detailed Answer

**Pipeline:** Build → scan → block deploy on Critical CVE → deploy to ECS/EKS.

**Architect:** No `latest` tag in production — use digest or semver tags.

---

**Next:** [Part 3 — Q031–Q050](aws-top-50-qa-part3.md)
