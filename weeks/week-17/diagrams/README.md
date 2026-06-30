# Week 17 — AWS Fundamentals Diagrams

## 1. AWS Well-Architected Framework

```mermaid
flowchart TB
    WAF[AWS WAF] --> OPS[Operational Excellence]
    WAF --> SEC[Security]
    WAF --> REL[Reliability]
    WAF --> PERF[Performance]
    WAF --> COST[Cost Optimization]
    WAF --> SUS[Sustainability]
```

## 2. Account Structure

```mermaid
flowchart TD
    Org[AWS Organization] --> Prod[Prod Account]
    Org --> Dev[Dev Account]
    Org --> Sec[Security / Log Archive]
```

## 3. IAM — Least Privilege for .NET on ECS

```mermaid
flowchart LR
    Task[ECS Task Role] --> S3[S3 Read]
    Task --> SM[Secrets Manager]
    Exec[Execution Role] --> ECR[ECR Pull]
```

## 4. Regional Services Layout

```mermaid
flowchart TB
    subgraph Region["us-east-1"]
        ALB[ALB]
        ECS[ECS Fargate]
        RDS[(RDS SQL Server)]
    end
    R53[Route 53] --> ALB
```

## 5. Azure vs AWS Concept Map

```mermaid
flowchart LR
    AS[App Service] --- EB[Elastic Beanstalk / ECS]
    AKS[AKS] --- EKS[EKS]
    SQL[Azure SQL] --- RDS[RDS]
    SB[Service Bus] --- SQS[SQS/SNS]
```

## Practice Exercise

Map Week 9 Azure landing zone to equivalent AWS Organization OU structure.

---

[← Back to Week 17](../README.md)
