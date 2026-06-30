# AWS Data & Networking — Intermediate

> **Week 19** | **Level:** Intermediate

## VPC Design

```
VPC 10.0.0.0/16
├── Public subnets (ALB, NAT Gateway)
├── Private subnets (ECS, RDS)
└── Isolated subnets (RDS only, no NAT)
```

## RDS vs DynamoDB

| | RDS/Aurora | DynamoDB |
|---|------------|----------|
| Model | SQL | Key-value/document |
| Scale | Read replicas, Aurora Serverless | On-demand or provisioned RCU/WCU |
| Use | Transactions, joins | High scale key access |

## S3 Storage Classes

- Standard → IA → Glacier Instant → Glacier Deep Archive
- Intelligent-Tiering for unknown access patterns



## Architect Deep Dive: Cross-Cloud Networking

Private connectivity between Azure and AWS for replication or hybrid apps — VPN or partner interconnect; architect documents bandwidth, latency, and operational ownership.

**Next:** [03-advanced.md](03-advanced.md)
