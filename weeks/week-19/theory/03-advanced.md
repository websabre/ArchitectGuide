# AWS Data & Networking — Advanced

> **Week 19** | **Level:** Advanced

## Hybrid Connectivity

- **Site-to-Site VPN:** Quick, limited bandwidth
- **Direct Connect:** Dedicated, predictable latency, higher setup
- **Transit Gateway:** Hub for VPC + on-prem connectivity

## PrivateLink vs VPC Endpoints

- **Gateway endpoint:** S3, DynamoDB (route table)
- **Interface endpoint:** Most other services (ENI in subnet)

## Route 53 Patterns

- Failover routing with health checks
- Latency-based routing for global users
- Weighted routing for blue/green

**Cross-cutting:** [Networking fundamentals](../../../docs/cross-cutting/networking-fundamentals/README.md)

## Architect Deep Dive: Data Sovereignty Multi-Cloud

When data must stay in EU: pin Azure West Europe **and** AWS eu-west-1 — document which system of record lives where to avoid compliance gaps.

