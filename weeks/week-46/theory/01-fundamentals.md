# Technical Interview Intensive — Cloud & Data

> **Week 46** | Review Months 2–5 (Data, Azure, AWS)

## Daily Schedule

| Day | Focus |
|-----|-------|
| Mon | SQL, indexing, replication, CAP |
| Tue | Azure (compute, networking, identity) |
| Wed | Azure (data, messaging, security) |
| Thu | AWS equivalents & multi-cloud |
| Fri | Scenario: "Migrate on-prem SQL to cloud" |

---

## Cross-Cloud Comparison Drills

| Capability | Azure | AWS |
|------------|-------|-----|
| Managed K8s | AKS | EKS |
| Serverless | Functions | Lambda |
| API gateway | APIM | API Gateway |
| Message bus | Service Bus | SQS/SNS |
| NoSQL | Cosmos DB | DynamoDB |

**Interview tip:** Lead with requirements, then map to services. Don't name-drop without justification.

---

## Scenario Bank

1. **Multi-region active-passive** — RTO 1h, SQL geo-replication
2. **Cost optimization** — $50K/month Azure bill, cut 30%
3. **Zero-trust networking** — Private endpoints, no public SQL
4. **Event-driven order flow** — Service Bus vs Event Hubs

**Resources:** [Azure Top 50](../../../interview-prep/azure-top-50-index.md), [AWS Top 50](../../../interview-prep/aws-top-50-index.md)
