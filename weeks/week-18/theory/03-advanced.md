# AWS Compute — Advanced

> **Week 18** | **Level:** Advanced

## Multi-AZ and Auto Scaling

- ALB across 2+ AZs — health checks, deregistration delay
- ASG: target tracking on CPU or custom CloudWatch metric
- Blue/green with CodeDeploy or separate target groups

## Serverless Architecture Limits

- Lambda 15 min timeout — not for long jobs
- API Gateway payload limits — use S3 presigned for uploads
- Step Functions for orchestration across Lambdas

## Architect Scenario

Migrate .NET Framework monolith on EC2 to modern .NET on AWS — phased approach with ALB path-based routing.

## Architect Deep Dive: Multi-Region AWS

Route 53 health checks + failover routing — equivalent to Azure Front Door priority pools. Validate data replication separately.

