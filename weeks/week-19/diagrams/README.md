# Week 19 — AWS Data & VPC Diagrams

## 1. VPC — 3-Tier Subnets

```mermaid
flowchart TB
    subgraph VPC
        Pub[Public Subnet - ALB]
        App[Private App Subnet - ECS]
        Data[Private Data Subnet - RDS]
    end
    IGW[Internet Gateway] --> Pub
    NAT[NAT Gateway] --> App
    App --> Data
```

## 2. RDS Multi-AZ

```mermaid
flowchart LR
    Primary[(RDS Primary AZ-a)] --> Standby[(Standby AZ-b)]
    App[.NET App] --> Primary
```

## 3. S3 + CloudFront Static Assets

```mermaid
flowchart LR
    User --> CF[CloudFront]
    CF --> S3[S3 Bucket OAI/OAC]
    User --> ALB[ALB API]
```

## 4. Read Replica Scaling

```mermaid
flowchart LR
    W[Write API] --> Primary[(RDS Primary)]
    Primary --> RR1[(Read Replica)]
    Primary --> RR2[(Read Replica)]
    R[Read API] --> RR1
```

## 5. VPC Endpoints — Private AWS API Access

```mermaid
flowchart LR
    App[Private Subnet] --> VPCE[VPC Endpoint]
    VPCE --> S3[S3 / DynamoDB]
```

> **Architect note:** NAT Gateway egress costs — use VPC endpoints for S3/Dynamo to reduce NAT traffic.

## Practice Exercise

Design VPC CIDR plan for 3 AZs with room for 4 environment expansions.

---

[← Back to Week 19](../README.md)
