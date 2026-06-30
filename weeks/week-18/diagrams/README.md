# Week 18 — AWS Compute Diagrams

## 1. ECS Fargate — .NET API

```mermaid
flowchart LR
    User --> ALB[Application Load Balancer]
    ALB --> TG[Target Group]
    TG --> Task1[Fargate Task]
    TG --> Task2[Fargate Task]
    Task1 --> RDS[(RDS)]
```

## 2. EKS Ingress

```mermaid
flowchart LR
    Internet --> ALB[AWS LB Controller]
    ALB --> Ing[Ingress]
    Ing --> Svc[Service]
    Svc --> Pod[.NET Pod]
```

## 3. Lambda — Event-Driven

```mermaid
flowchart LR
    S3[S3 Upload] --> SQS[SQS]
    SQS --> Lambda[Lambda .NET 8]
    Lambda --> DDB[(DynamoDB)]
```

## 4. Auto Scaling

```mermaid
flowchart TD
    CW[CloudWatch CPU] --> ASG[Auto Scaling Group]
    ASG --> Add[Scale Out]
    ASG --> Rem[Scale In]
```

## 5. Blue/Green on ECS

```mermaid
sequenceDiagram
    participant CICD
    participant Blue as Blue Service
    participant Green as Green Service
    participant ALB

    CICD->>Green: Deploy new task def
    CICD->>ALB: Shift traffic to Green
    Note over Blue: Drain then decommission
```

## Practice Exercise

When is Lambda wrong for a .NET order API with 200ms p99 SLA and 2K RPS steady state?

---

[← Back to Week 18](../README.md)
