# AWS Compute — EC2, Lambda, ECS, EKS

> **Week 18** | **Module:** [aws-fundamentals](../../../modules/aws-fundamentals/README.md)

## Compute Decision Matrix

| Service | Model | Best For |
|---------|-------|----------|
| **EC2** | IaaS VMs | Full control, legacy, custom AMIs |
| **Lambda** | Serverless functions | Event-driven, short tasks |
| **ECS** | Container orchestration | Docker without K8s complexity |
| **EKS** | Managed Kubernetes | Full K8s, multi-cloud |
| **Fargate** | Serverless containers | ECS/EKS without managing EC2 |
| **Elastic Beanstalk** | PaaS | Quick .NET deploy (like App Service) |
| **App Runner** | Container PaaS | Simple container web apps |

## Lambda
- Max timeout 15 minutes
- Cold starts — Provisioned Concurrency for latency-sensitive
- Triggers: API Gateway, S3, SQS, EventBridge, DynamoDB streams
- **.NET:** Native runtime, good for event processing

## ECS vs EKS
| Factor | ECS | EKS |
|--------|-----|-----|
| K8s API | No | Yes |
| Learning curve | Lower | Higher |
| Portability | AWS-only | Multi-cloud |
| Service mesh | App Mesh | App Mesh, Istio |

**Architect:** ECS Fargate for AWS-native containers. EKS when team has K8s skills or multi-cloud mandate.

## EC2 Purchasing
| Option | Savings | Commitment |
|--------|---------|------------|
| On-Demand | 0% | None |
| Reserved (1-3 yr) | ~40-60% | Instance type/region |
| Savings Plans | ~20-40% | Compute spend |
| Spot | ~70-90% | Interruptible workloads |

## .NET on AWS
- **Elastic Beanstalk:** Closest to Azure App Service
- **ECS/EKS:** Containerized .NET 8
- **Lambda:** Event handlers, lightweight APIs via API Gateway



## Architect Deep Dive: AWS Serverless & Containers

### Lambda + .NET
Use for async, bursty work — not latency-sensitive synchronous APIs at high QPS (cold starts). Provisioned concurrency for predictable latency.

### ECS vs EKS decision
Same as Container Apps vs AKS on Azure — start ECS Fargate, graduate to EKS when mesh/GitOps/custom operators required.

**Next:** Week 19 Networking & Data
