# Multi-Cloud Architecture — Azure vs AWS

> **Week 20** | **Module:** [aws-architecture](../../../modules/aws-architecture/README.md)

## Service Mapping Reference

| Capability | Azure | AWS |
|------------|-------|-----|
| VM | Virtual Machines | EC2 |
| PaaS Web | App Service | Elastic Beanstalk / App Runner |
| Serverless | Functions | Lambda |
| Containers | AKS / Container Apps | EKS / ECS Fargate |
| SQL | Azure SQL | RDS SQL Server / Aurora |
| NoSQL | Cosmos DB | DynamoDB |
| Object Storage | Blob Storage | S3 |
| Messaging Queue | Service Bus | SQS |
| Pub/Sub | Event Grid | SNS + EventBridge |
| Streaming | Event Hubs | Kinesis |
| API Gateway | API Management | API Gateway |
| CDN + WAF | Front Door | CloudFront + WAF |
| Identity | Entra ID | IAM + Cognito |
| Secrets | Key Vault | Secrets Manager |
| Monitoring | App Insights | CloudWatch + X-Ray |
| IaC | Bicep / ARM | CloudFormation / CDK |
| Multi-cloud IaC | Terraform | Terraform |

## Multi-Cloud Strategies

| Strategy | Description | When |
|----------|-------------|------|
| **Single cloud** | Azure OR AWS | Default — most enterprises |
| **Multi-cloud active** | Workloads on both | Regulatory, acquisition, avoid lock-in |
| **Cloud-agnostic abstractions** | K8s, Terraform, Postgres | Portability with overhead |
| **Best-of-breed** | AI on Azure OpenAI, data on AWS | Specific service superiority |

## Avoiding Lock-In

**Portable:**
- Kubernetes workloads
- Terraform modules (with provider abstraction)
- Open-source databases (PostgreSQL)
- Container images
- OpenTelemetry for observability

**Locked (accept consciously):**
- Azure Service Bus → SQS migration effort
- Cosmos DB specific APIs
- Entra ID Conditional Access depth
- Lambda-specific triggers

## Same Workload — Side by Side

**.NET 8 Order API:**

| Layer | Azure | AWS |
|-------|-------|-----|
| Edge | Front Door + WAF | CloudFront + WAF |
| Compute | App Service P1v3 | Elastic Beanstalk / ECS |
| Auth | Entra ID + MI | Cognito + IAM Role |
| Database | Azure SQL S3 | RDS SQL Server db.t3.medium |
| Cache | Redis Cache | ElastiCache Redis |
| Queue | Service Bus | SQS |
| Secrets | Key Vault | Secrets Manager |
| Monitor | App Insights | X-Ray + CloudWatch |

## Cost Comparison Methodology
1. Use pricing calculators (both clouds)
2. Model same SLA tier (multi-AZ, backup retention)
3. Include data egress (often surprise cost)
4. Factor Reserved Instance / Savings Plan vs Azure Reserved
5. Include operational cost (team expertise)

## Capstone Exercise
Design the same SaaS on Azure and AWS. Document:
- Architecture diagrams (both)
- Monthly cost estimate (both)
- 5 trade-offs per cloud
- Your recommendation for a .NET shop vs neutral shop

**Case study:** [cs20-multicloud-comparison.md](../case-studies/cs20-multicloud-comparison.md)

## Architect Deep Dive: Multi-Cloud Strategy

### Valid reasons
- Acquisition integration timeline
- Best-of-breed service (specific AI, specific region)
- Avoid single-vendor negotiation lock-in (with eyes open on operational cost)

### Invalid reasons
- "Avoid vendor lock-in" without quantifying portability cost — you will be multi-cloud operational forever

### Portable layer
Kubernetes, Terraform, OpenTelemetry, PostgreSQL, S3-compatible APIs — abstract where ROI clear; embrace managed services where team velocity matters.

