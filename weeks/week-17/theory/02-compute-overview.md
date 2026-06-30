# AWS Compute Overview

> **Week 17** — EC2, Lambda, ECS, EKS comparison

See [01-fundamentals.md](01-fundamentals.md).

## Architect Deep Dive: AWS Compute for .NET

| AWS service | .NET fit |
|-------------|----------|
| ECS Fargate | Containers without K8s |
| EKS | Full K8s — same trade-offs as AKS |
| Lambda | Event handlers — cold start awareness |
| Elastic Beanstalk | Closest to App Service simplicity |

**Architect tip:** Prefer managed PaaS/container service until K8s operational maturity proven.

