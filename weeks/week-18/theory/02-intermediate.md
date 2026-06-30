# AWS Compute — Intermediate

> **Week 18** | **Level:** Intermediate

## Compute Selection Matrix

| Workload | Service |
|----------|---------|
| .NET API always-on | ECS Fargate / EKS / Elastic Beanstalk |
| Spiky HTTP | Lambda + API Gateway |
| Long-running batch | EC2 / Batch |
| Containers without K8s ops | ECS Fargate |

## Lambda Cold Starts (.NET)

- Native AOT (where supported) reduces init time
- Provisioned concurrency for latency-sensitive paths
- Keep handlers small; reuse static clients

## ECS vs EKS

| | ECS | EKS |
|---|-----|-----|
| Ops burden | Lower | Higher |
| Portability | AWS-native | Kubernetes standard |
| Team skill | AWS-focused | K8s experience |



## Architect Deep Dive: Serverless Integration

### Event-driven AWS pattern
S3 upload → EventBridge → Lambda → DynamoDB metadata — mirror with Blob → Event Grid → Function → Cosmos.

**Next:** [03-advanced.md](03-advanced.md)
