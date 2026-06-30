# AWS Data, Storage & VPC Networking

> **Week 19** | **Module:** [aws-architecture](../../../modules/aws-architecture/README.md)

## Data Services

| Service | Type | Azure Equivalent |
|---------|------|----------------|
| **RDS** | Managed SQL (SQL Server, PostgreSQL, MySQL) | Azure SQL / PostgreSQL |
| **Aurora** | Cloud-native SQL (MySQL/PostgreSQL compatible) | — |
| **DynamoDB** | Key-value/document NoSQL | Cosmos DB |
| **S3** | Object storage | Blob Storage |
| **ElastiCache** | Redis/Memcached | Azure Cache for Redis |
| **Redshift** | Data warehouse | Synapse |
| **DocumentDB** | MongoDB-compatible | Cosmos DB Mongo API |

## S3 Architecture
- **Buckets** — global unique name
- **Storage classes:** Standard, IA, Glacier, Intelligent-Tiering
- **Versioning + MFA Delete** — ransomware protection
- **Lifecycle policies** — auto-tier transitions
- **Pre-signed URLs** — temporary access

## DynamoDB
- Partition key + optional sort key
- On-demand vs provisioned capacity
- Global tables for multi-region
- DAX for caching
- **Design:** Same partition key principles as Cosmos DB

## VPC Networking

```
VPC (10.0.0.0/16)
├── Public Subnet (10.0.1.0/24) — ALB, NAT Gateway
├── Private Subnet (10.0.2.0/24) — App servers
└── Private Subnet (10.0.3.0/24) — RDS (isolated)
```

| Component | Purpose |
|-----------|---------|
| **Internet Gateway** | Public internet access |
| **NAT Gateway** | Outbound internet for private subnets |
| **Security Group** | Stateful firewall per resource |
| **NACL** | Stateless subnet firewall |
| **Route 53** | DNS, health checks, routing policies |
| **CloudFront** | CDN |
| **ALB** | L7 load balancing |
| **NLB** | L4 load balancing |

## Hybrid Connectivity
- **Site-to-Site VPN** — IPsec over internet
- **Direct Connect** — Dedicated private connection (like ExpressRoute)
- **Transit Gateway** — Hub for VPC peering at scale



## Architect Deep Dive: AWS Data & Networking

### VPC design parallels
AWS VPC ≈ Azure VNet — public/private subnets, NAT gateway (cost awareness — ~$32/mo+ per NAT), security groups ≈ NSG.

### RDS vs Aurora
RDS for standard SQL Server/MySQL/Postgres. Aurora when AWS-native scale and fast failover needed — evaluate cost vs Azure SQL BC tier equivalent.

**Next:** Week 20 Multi-Cloud
