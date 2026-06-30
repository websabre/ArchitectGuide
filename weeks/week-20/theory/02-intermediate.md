# Multi-Cloud Architecture — Intermediate

> **Week 20** | **Level:** Intermediate

## Azure ↔ AWS Service Mapping

| Capability | Azure | AWS |
|------------|-------|-----|
| VM | Virtual Machines | EC2 |
| PaaS API | App Service | Elastic Beanstalk / App Runner |
| Kubernetes | AKS | EKS |
| Serverless | Functions | Lambda |
| SQL | Azure SQL | RDS / Aurora |
| NoSQL | Cosmos DB | DynamoDB |
| Object storage | Blob | S3 |
| Identity | Entra ID | IAM + Cognito |
| Secrets | Key Vault | Secrets Manager |
| Messaging | Service Bus | SQS/SNS |

## What's Actually Portable

| Portable | Locked-in |
|----------|-----------|
| Containers + K8s | PaaS-specific bindings |
| Terraform (with caveats) | Native serverless triggers |
| OpenTelemetry | Proprietary AI services |
| PostgreSQL | Cosmos DB specific APIs |



## Architect Deep Dive: Abstraction Patterns

### Active-active pitfalls
Split-brain data, conflicting writes, doubled operational runbooks. Prefer active-passive per cloud with clear failover runbook until team proves multi-master competence.

**Next:** [03-advanced.md](03-advanced.md)
