# Week 11 — Intermediate Q&A

> Q031–Q070: Premium format (Week 1 quality).

---


## Q031: Azure SQL vs Cosmos DB — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Data |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Azure SQL vs Cosmos DB using Azure SQL in a Azure Data Platform architecture review?

### Short Answer (30 seconds)

Use Azure SQL with Cosmos DB; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Choose sql vs cosmos per bounded context access pattern.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Context:** Azure SQL vs Cosmos DB is core to Azure Solution Architect interviews covering Azure SQL, Cosmos DB, bounded context, polyglot persistence.

**Architect approach:**
1. Map business requirement to Azure SQL — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Choose sql vs cosmos per bounded context access pattern.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect choose SQL vs Cosmos per bounded context access pattern — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to Azure SQL?**
2. **What KPI proves azure sql vs cosmos db adoption succeeded?**

### Common Mistakes in Interviews

- Listing Azure SQL without explaining trade-offs
- No Policy or IaC enforcement for azure sql vs cosmos db
- Skipping operational runbook for Azure SQL

---

## Q032: Azure SQL vs Cosmos DB — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Data |
| **Frequency** | Common |

### Question

**Intermediate:** Design production azure sql vs cosmos db for a 10-subscription enterprise (Azure Data Platform).

### Short Answer (30 seconds)

Platform hosts shared Azure SQL; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Design:** Multi-subscription estate with platform vs application separation.
Shared Azure SQL and Cosmos DB in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Choose sql vs cosmos per bounded context access pattern.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize azure sql vs cosmos db.

### Follow-up Questions

1. **How do Policy exemptions work during azure sql vs cosmos db migration?**
2. **What FinOps tag strategy supports azure sql vs cosmos db chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for Azure SQL testing
- Policies only at resource group — not MG

---

## Q033: Cosmos Partition Key Design — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Cosmos DB |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Cosmos Partition Key Design using partition key in a Azure Data Platform architecture review?

### Short Answer (30 seconds)

Use partition key with hot partitions; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Partition key design for multi-tenant saas at scale.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Context:** Cosmos Partition Key Design is core to Azure Solution Architect interviews covering partition key, hot partitions, RU/s, 429 throttling.

**Architect approach:**
1. Map business requirement to partition key — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Partition key design for multi-tenant saas at scale.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect partition key design for multi-tenant SaaS at scale — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to partition key?**
2. **What KPI proves cosmos partition key design adoption succeeded?**

### Common Mistakes in Interviews

- Listing partition key without explaining trade-offs
- No Policy or IaC enforcement for cosmos partition key design
- Skipping operational runbook for partition key

---

## Q034: Cosmos Partition Key Design — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Cosmos DB |
| **Frequency** | Common |

### Question

**Intermediate:** Design production cosmos partition key design for a 10-subscription enterprise (Azure Data Platform).

### Short Answer (30 seconds)

Platform hosts shared partition key; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Design:** Multi-subscription estate with platform vs application separation.
Shared partition key and hot partitions in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Partition key design for multi-tenant saas at scale.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize cosmos partition key design.

### Follow-up Questions

1. **How do Policy exemptions work during cosmos partition key design migration?**
2. **What FinOps tag strategy supports cosmos partition key design chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for partition key testing
- Policies only at resource group — not MG

---

## Q035: Azure SQL HA and DR — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SQL |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Azure SQL HA and DR using zone redundancy in a Azure Data Platform architecture review?

### Short Answer (30 seconds)

Use zone redundancy with geo-replication; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Sql ha/dr options mapped to business rpo/rto.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Context:** Azure SQL HA and DR is core to Azure Solution Architect interviews covering zone redundancy, geo-replication, failover groups, RPO/RTO.

**Architect approach:**
1. Map business requirement to zone redundancy — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Sql ha/dr options mapped to business rpo/rto.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect SQL HA/DR options mapped to business RPO/RTO — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to zone redundancy?**
2. **What KPI proves azure sql ha and dr adoption succeeded?**

### Common Mistakes in Interviews

- Listing zone redundancy without explaining trade-offs
- No Policy or IaC enforcement for azure sql ha and dr
- Skipping operational runbook for zone redundancy

---

## Q036: Azure SQL HA and DR — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SQL |
| **Frequency** | Common |

### Question

**Intermediate:** Design production azure sql ha and dr for a 10-subscription enterprise (Azure Data Platform).

### Short Answer (30 seconds)

Platform hosts shared zone redundancy; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Design:** Multi-subscription estate with platform vs application separation.
Shared zone redundancy and geo-replication in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Sql ha/dr options mapped to business rpo/rto.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize azure sql ha and dr.

### Follow-up Questions

1. **How do Policy exemptions work during azure sql ha and dr migration?**
2. **What FinOps tag strategy supports azure sql ha and dr chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for zone redundancy testing
- Policies only at resource group — not MG

---

## Q037: Hyperscale and Elastic Pools — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SQL |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Hyperscale and Elastic Pools using Hyperscale in a Azure Data Platform architecture review?

### Short Answer (30 seconds)

Use Hyperscale with elastic pools; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Elastic pools for saas with many small tenant databases.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Context:** Hyperscale and Elastic Pools is core to Azure Solution Architect interviews covering Hyperscale, elastic pools, serverless SQL, vCore sizing.

**Architect approach:**
1. Map business requirement to Hyperscale — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Elastic pools for saas with many small tenant databases.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect elastic pools for SaaS with many small tenant databases — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to Hyperscale?**
2. **What KPI proves hyperscale and elastic pools adoption succeeded?**

### Common Mistakes in Interviews

- Listing Hyperscale without explaining trade-offs
- No Policy or IaC enforcement for hyperscale and elastic pools
- Skipping operational runbook for Hyperscale

---

## Q038: Hyperscale and Elastic Pools — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SQL |
| **Frequency** | Common |

### Question

**Intermediate:** Design production hyperscale and elastic pools for a 10-subscription enterprise (Azure Data Platform).

### Short Answer (30 seconds)

Platform hosts shared Hyperscale; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Design:** Multi-subscription estate with platform vs application separation.
Shared Hyperscale and elastic pools in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Elastic pools for saas with many small tenant databases.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize hyperscale and elastic pools.

### Follow-up Questions

1. **How do Policy exemptions work during hyperscale and elastic pools migration?**
2. **What FinOps tag strategy supports hyperscale and elastic pools chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for Hyperscale testing
- Policies only at resource group — not MG

---

## Q039: Blob Storage Tiers — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Storage |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Blob Storage Tiers using Hot/Cool/Cold/Archive in a Azure Data Platform architecture review?

### Short Answer (30 seconds)

Use Hot/Cool/Cold/Archive with lifecycle management; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Blob tiering and lifecycle for cost and compliance retention.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Context:** Blob Storage Tiers is core to Azure Solution Architect interviews covering Hot/Cool/Cold/Archive, lifecycle management, immutability.

**Architect approach:**
1. Map business requirement to Hot/Cool/Cold/Archive — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Blob tiering and lifecycle for cost and compliance retention.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect blob tiering and lifecycle for cost and compliance retention — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to Hot/Cool/Cold/Archive?**
2. **What KPI proves blob storage tiers adoption succeeded?**

### Common Mistakes in Interviews

- Listing Hot/Cool/Cold/Archive without explaining trade-offs
- No Policy or IaC enforcement for blob storage tiers
- Skipping operational runbook for Hot/Cool/Cold/Archive

---

## Q040: Blob Storage Tiers — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Storage |
| **Frequency** | Common |

### Question

**Intermediate:** Design production blob storage tiers for a 10-subscription enterprise (Azure Data Platform).

### Short Answer (30 seconds)

Platform hosts shared Hot/Cool/Cold/Archive; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Design:** Multi-subscription estate with platform vs application separation.
Shared Hot/Cool/Cold/Archive and lifecycle management in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Blob tiering and lifecycle for cost and compliance retention.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize blob storage tiers.

### Follow-up Questions

1. **How do Policy exemptions work during blob storage tiers migration?**
2. **What FinOps tag strategy supports blob storage tiers chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for Hot/Cool/Cold/Archive testing
- Policies only at resource group — not MG

---

## Q041: Synapse and Analytics Path — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Analytics |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Synapse and Analytics Path using Synapse in a Azure Data Platform architecture review?

### Short Answer (30 seconds)

Use Synapse with serverless SQL; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Analytics path that protects oltp from heavy reporting.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Context:** Synapse and Analytics Path is core to Azure Solution Architect interviews covering Synapse, serverless SQL, data lake, CDC.

**Architect approach:**
1. Map business requirement to Synapse — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Analytics path that protects oltp from heavy reporting.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect analytics path that protects OLTP from heavy reporting — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to Synapse?**
2. **What KPI proves synapse and analytics path adoption succeeded?**

### Common Mistakes in Interviews

- Listing Synapse without explaining trade-offs
- No Policy or IaC enforcement for synapse and analytics path
- Skipping operational runbook for Synapse

---

## Q042: Synapse and Analytics Path — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Analytics |
| **Frequency** | Common |

### Question

**Intermediate:** Design production synapse and analytics path for a 10-subscription enterprise (Azure Data Platform).

### Short Answer (30 seconds)

Platform hosts shared Synapse; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Design:** Multi-subscription estate with platform vs application separation.
Shared Synapse and serverless SQL in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Analytics path that protects oltp from heavy reporting.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize synapse and analytics path.

### Follow-up Questions

1. **How do Policy exemptions work during synapse and analytics path migration?**
2. **What FinOps tag strategy supports synapse and analytics path chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for Synapse testing
- Policies only at resource group — not MG

---

## Q043: Event Hubs Ingestion — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Streaming |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Event Hubs Ingestion using Event Hubs in a Azure Data Platform architecture review?

### Short Answer (30 seconds)

Use Event Hubs with partitions; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. High-volume telemetry ingest with event hubs architecture.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Context:** Event Hubs Ingestion is core to Azure Solution Architect interviews covering Event Hubs, partitions, capture, Kafka endpoint.

**Architect approach:**
1. Map business requirement to Event Hubs — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
High-volume telemetry ingest with event hubs architecture.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect high-volume telemetry ingest with Event Hubs architecture — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to Event Hubs?**
2. **What KPI proves event hubs ingestion adoption succeeded?**

### Common Mistakes in Interviews

- Listing Event Hubs without explaining trade-offs
- No Policy or IaC enforcement for event hubs ingestion
- Skipping operational runbook for Event Hubs

---

## Q044: Event Hubs Ingestion — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Streaming |
| **Frequency** | Common |

### Question

**Intermediate:** Design production event hubs ingestion for a 10-subscription enterprise (Azure Data Platform).

### Short Answer (30 seconds)

Platform hosts shared Event Hubs; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Design:** Multi-subscription estate with platform vs application separation.
Shared Event Hubs and partitions in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
High-volume telemetry ingest with event hubs architecture.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize event hubs ingestion.

### Follow-up Questions

1. **How do Policy exemptions work during event hubs ingestion migration?**
2. **What FinOps tag strategy supports event hubs ingestion chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for Event Hubs testing
- Policies only at resource group — not MG

---

## Q045: Data Encryption Strategy — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Data Encryption Strategy using TDE in a Azure Data Platform architecture review?

### Short Answer (30 seconds)

Use TDE with CMK; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Encryption layers for healthcare and pci data classifications.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Context:** Data Encryption Strategy is core to Azure Solution Architect interviews covering TDE, CMK, Always Encrypted, double encryption.

**Architect approach:**
1. Map business requirement to TDE — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Encryption layers for healthcare and pci data classifications.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect encryption layers for healthcare and PCI data classifications — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to TDE?**
2. **What KPI proves data encryption strategy adoption succeeded?**

### Common Mistakes in Interviews

- Listing TDE without explaining trade-offs
- No Policy or IaC enforcement for data encryption strategy
- Skipping operational runbook for TDE

---

## Q046: Data Encryption Strategy — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

**Intermediate:** Design production data encryption strategy for a 10-subscription enterprise (Azure Data Platform).

### Short Answer (30 seconds)

Platform hosts shared TDE; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Design:** Multi-subscription estate with platform vs application separation.
Shared TDE and CMK in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Encryption layers for healthcare and pci data classifications.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize data encryption strategy.

### Follow-up Questions

1. **How do Policy exemptions work during data encryption strategy migration?**
2. **What FinOps tag strategy supports data encryption strategy chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for TDE testing
- Policies only at resource group — not MG

---

## Q047: Cosmos Consistency Levels — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Cosmos DB |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Cosmos Consistency Levels using session in a Azure Data Platform architecture review?

### Short Answer (30 seconds)

Use session with bounded staleness; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Consistency level selection per read pattern and region layout.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Context:** Cosmos Consistency Levels is core to Azure Solution Architect interviews covering session, bounded staleness, strong, eventual consistency.

**Architect approach:**
1. Map business requirement to session — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Consistency level selection per read pattern and region layout.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect consistency level selection per read pattern and region layout — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to session?**
2. **What KPI proves cosmos consistency levels adoption succeeded?**

### Common Mistakes in Interviews

- Listing session without explaining trade-offs
- No Policy or IaC enforcement for cosmos consistency levels
- Skipping operational runbook for session

---

## Q048: Cosmos Consistency Levels — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Cosmos DB |
| **Frequency** | Common |

### Question

**Intermediate:** Design production cosmos consistency levels for a 10-subscription enterprise (Azure Data Platform).

### Short Answer (30 seconds)

Platform hosts shared session; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Design:** Multi-subscription estate with platform vs application separation.
Shared session and bounded staleness in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Consistency level selection per read pattern and region layout.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize cosmos consistency levels.

### Follow-up Questions

1. **How do Policy exemptions work during cosmos consistency levels migration?**
2. **What FinOps tag strategy supports cosmos consistency levels chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for session testing
- Policies only at resource group — not MG

---

## Q049: SQL Performance Tuning — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SQL |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply SQL Performance Tuning using Query Store in a Azure Data Platform architecture review?

### Short Answer (30 seconds)

Use Query Store with indexes; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Sql performance architecture before scaling sku blindly.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Context:** SQL Performance Tuning is core to Azure Solution Architect interviews covering Query Store, indexes, DTU/vCore monitoring, read replicas.

**Architect approach:**
1. Map business requirement to Query Store — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Sql performance architecture before scaling sku blindly.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect SQL performance architecture before scaling SKU blindly — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to Query Store?**
2. **What KPI proves sql performance tuning adoption succeeded?**

### Common Mistakes in Interviews

- Listing Query Store without explaining trade-offs
- No Policy or IaC enforcement for sql performance tuning
- Skipping operational runbook for Query Store

---

## Q050: SQL Performance Tuning — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SQL |
| **Frequency** | Common |

### Question

**Intermediate:** Design production sql performance tuning for a 10-subscription enterprise (Azure Data Platform).

### Short Answer (30 seconds)

Platform hosts shared Query Store; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Design:** Multi-subscription estate with platform vs application separation.
Shared Query Store and indexes in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Sql performance architecture before scaling sku blindly.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize sql performance tuning.

### Follow-up Questions

1. **How do Policy exemptions work during sql performance tuning migration?**
2. **What FinOps tag strategy supports sql performance tuning chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for Query Store testing
- Policies only at resource group — not MG

---

## Q051: Data Lake Architecture — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Analytics |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Data Lake Architecture using ADLS Gen2 in a Azure Data Platform architecture review?

### Short Answer (30 seconds)

Use ADLS Gen2 with Parquet; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Medallion lakehouse pattern on azure for analytics.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Context:** Data Lake Architecture is core to Azure Solution Architect interviews covering ADLS Gen2, Parquet, medallion architecture, Synapse pipelines.

**Architect approach:**
1. Map business requirement to ADLS Gen2 — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Medallion lakehouse pattern on azure for analytics.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect medallion lakehouse pattern on Azure for analytics — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to ADLS Gen2?**
2. **What KPI proves data lake architecture adoption succeeded?**

### Common Mistakes in Interviews

- Listing ADLS Gen2 without explaining trade-offs
- No Policy or IaC enforcement for data lake architecture
- Skipping operational runbook for ADLS Gen2

---

## Q052: Data Lake Architecture — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Analytics |
| **Frequency** | Common |

### Question

**Intermediate:** Design production data lake architecture for a 10-subscription enterprise (Azure Data Platform).

### Short Answer (30 seconds)

Platform hosts shared ADLS Gen2; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Design:** Multi-subscription estate with platform vs application separation.
Shared ADLS Gen2 and Parquet in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Medallion lakehouse pattern on azure for analytics.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize data lake architecture.

### Follow-up Questions

1. **How do Policy exemptions work during data lake architecture migration?**
2. **What FinOps tag strategy supports data lake architecture chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for ADLS Gen2 testing
- Policies only at resource group — not MG

---

## Q053: Redis Cache Patterns — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Caching |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Redis Cache Patterns using Azure Cache for Redis in a Azure Data Platform architecture review?

### Short Answer (30 seconds)

Use Azure Cache for Redis with cache-aside; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Redis for session.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Context:** Redis Cache Patterns is core to Azure Solution Architect interviews covering Azure Cache for Redis, cache-aside, TTL, session store.

**Architect approach:**
1. Map business requirement to Azure Cache for Redis — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Redis for session, catalog cache, and rate limiting.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect Redis for session, catalog cache, and rate limiting — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to Azure Cache for Redis?**
2. **What KPI proves redis cache patterns adoption succeeded?**

### Common Mistakes in Interviews

- Listing Azure Cache for Redis without explaining trade-offs
- No Policy or IaC enforcement for redis cache patterns
- Skipping operational runbook for Azure Cache for Redis

---

## Q054: Redis Cache Patterns — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Caching |
| **Frequency** | Common |

### Question

**Intermediate:** Design production redis cache patterns for a 10-subscription enterprise (Azure Data Platform).

### Short Answer (30 seconds)

Platform hosts shared Azure Cache for Redis; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Design:** Multi-subscription estate with platform vs application separation.
Shared Azure Cache for Redis and cache-aside in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Redis for session, catalog cache, and rate limiting.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize redis cache patterns.

### Follow-up Questions

1. **How do Policy exemptions work during redis cache patterns migration?**
2. **What FinOps tag strategy supports redis cache patterns chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for Azure Cache for Redis testing
- Policies only at resource group — not MG

---

## Q055: Backup and LTR — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DR |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Backup and LTR using automated backup in a Azure Data Platform architecture review?

### Short Answer (30 seconds)

Use automated backup with long-term retention; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Backup retention aligned to compliance and restore testing.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Context:** Backup and LTR is core to Azure Solution Architect interviews covering automated backup, long-term retention, point-in-time restore.

**Architect approach:**
1. Map business requirement to automated backup — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Backup retention aligned to compliance and restore testing.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect backup retention aligned to compliance and restore testing — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to automated backup?**
2. **What KPI proves backup and ltr adoption succeeded?**

### Common Mistakes in Interviews

- Listing automated backup without explaining trade-offs
- No Policy or IaC enforcement for backup and ltr
- Skipping operational runbook for automated backup

---

## Q056: Backup and LTR — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DR |
| **Frequency** | Common |

### Question

**Intermediate:** Design production backup and ltr for a 10-subscription enterprise (Azure Data Platform).

### Short Answer (30 seconds)

Platform hosts shared automated backup; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Design:** Multi-subscription estate with platform vs application separation.
Shared automated backup and long-term retention in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Backup retention aligned to compliance and restore testing.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize backup and ltr.

### Follow-up Questions

1. **How do Policy exemptions work during backup and ltr migration?**
2. **What FinOps tag strategy supports backup and ltr chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for automated backup testing
- Policies only at resource group — not MG

---

## Q057: Multi-Region Data — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reliability |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Multi-Region Data using Cosmos multi-region in a Azure Data Platform architecture review?

### Short Answer (30 seconds)

Use Cosmos multi-region with SQL geo-replica; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Multi-region data strategy with consistency trade-offs.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Context:** Multi-Region Data is core to Azure Solution Architect interviews covering Cosmos multi-region, SQL geo-replica, conflict resolution.

**Architect approach:**
1. Map business requirement to Cosmos multi-region — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Multi-region data strategy with consistency trade-offs.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect multi-region data strategy with consistency trade-offs — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to Cosmos multi-region?**
2. **What KPI proves multi-region data adoption succeeded?**

### Common Mistakes in Interviews

- Listing Cosmos multi-region without explaining trade-offs
- No Policy or IaC enforcement for multi-region data
- Skipping operational runbook for Cosmos multi-region

---

## Q058: Multi-Region Data — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reliability |
| **Frequency** | Common |

### Question

**Intermediate:** Design production multi-region data for a 10-subscription enterprise (Azure Data Platform).

### Short Answer (30 seconds)

Platform hosts shared Cosmos multi-region; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Design:** Multi-subscription estate with platform vs application separation.
Shared Cosmos multi-region and SQL geo-replica in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Multi-region data strategy with consistency trade-offs.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize multi-region data.

### Follow-up Questions

1. **How do Policy exemptions work during multi-region data migration?**
2. **What FinOps tag strategy supports multi-region data chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for Cosmos multi-region testing
- Policies only at resource group — not MG

---

## Q059: Data Governance — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Data Governance using Purview in a Azure Data Platform architecture review?

### Short Answer (30 seconds)

Use Purview with classification; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Data governance for enterprise azure data estate.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Context:** Data Governance is core to Azure Solution Architect interviews covering Purview, classification, lineage, data catalog.

**Architect approach:**
1. Map business requirement to Purview — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Data governance for enterprise azure data estate.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect data governance for enterprise Azure data estate — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to Purview?**
2. **What KPI proves data governance adoption succeeded?**

### Common Mistakes in Interviews

- Listing Purview without explaining trade-offs
- No Policy or IaC enforcement for data governance
- Skipping operational runbook for Purview

---

## Q060: Data Governance — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

**Intermediate:** Design production data governance for a 10-subscription enterprise (Azure Data Platform).

### Short Answer (30 seconds)

Platform hosts shared Purview; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Design:** Multi-subscription estate with platform vs application separation.
Shared Purview and classification in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Data governance for enterprise azure data estate.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize data governance.

### Follow-up Questions

1. **How do Policy exemptions work during data governance migration?**
2. **What FinOps tag strategy supports data governance chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for Purview testing
- Policies only at resource group — not MG

---

## Q061: Migration to Azure SQL — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Migration |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Migration to Azure SQL using DMA in a Azure Data Platform architecture review?

### Short Answer (30 seconds)

Use DMA with DMS; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Sql migration approach with downtime window analysis.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Context:** Migration to Azure SQL is core to Azure Solution Architect interviews covering DMA, DMS, offline vs online migration, compatibility.

**Architect approach:**
1. Map business requirement to DMA — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Sql migration approach with downtime window analysis.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect SQL migration approach with downtime window analysis — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to DMA?**
2. **What KPI proves migration to azure sql adoption succeeded?**

### Common Mistakes in Interviews

- Listing DMA without explaining trade-offs
- No Policy or IaC enforcement for migration to azure sql
- Skipping operational runbook for DMA

---

## Q062: Migration to Azure SQL — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Migration |
| **Frequency** | Common |

### Question

**Intermediate:** Design production migration to azure sql for a 10-subscription enterprise (Azure Data Platform).

### Short Answer (30 seconds)

Platform hosts shared DMA; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Design:** Multi-subscription estate with platform vs application separation.
Shared DMA and DMS in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Sql migration approach with downtime window analysis.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize migration to azure sql.

### Follow-up Questions

1. **How do Policy exemptions work during migration to azure sql migration?**
2. **What FinOps tag strategy supports migration to azure sql chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for DMA testing
- Policies only at resource group — not MG

---

## Q063: NoSQL vs SQL Decision — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Architecture |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply NoSQL vs SQL Decision using decision matrix in a Azure Data Platform architecture review?

### Short Answer (30 seconds)

Use decision matrix with CAP; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Structured decision framework for sql vs nosql on azure.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Context:** NoSQL vs SQL Decision is core to Azure Solution Architect interviews covering decision matrix, CAP, access patterns, transactions.

**Architect approach:**
1. Map business requirement to decision matrix — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Structured decision framework for sql vs nosql on azure.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect structured decision framework for SQL vs NoSQL on Azure — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to decision matrix?**
2. **What KPI proves nosql vs sql decision adoption succeeded?**

### Common Mistakes in Interviews

- Listing decision matrix without explaining trade-offs
- No Policy or IaC enforcement for nosql vs sql decision
- Skipping operational runbook for decision matrix

---

## Q064: NoSQL vs SQL Decision — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Architecture |
| **Frequency** | Common |

### Question

**Intermediate:** Design production nosql vs sql decision for a 10-subscription enterprise (Azure Data Platform).

### Short Answer (30 seconds)

Platform hosts shared decision matrix; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Design:** Multi-subscription estate with platform vs application separation.
Shared decision matrix and CAP in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Structured decision framework for sql vs nosql on azure.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize nosql vs sql decision.

### Follow-up Questions

1. **How do Policy exemptions work during nosql vs sql decision migration?**
2. **What FinOps tag strategy supports nosql vs sql decision chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for decision matrix testing
- Policies only at resource group — not MG

---

## Q065: Streaming to Warehouse — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Integration |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Streaming to Warehouse using Event Hubs in a Azure Data Platform architecture review?

### Short Answer (30 seconds)

Use Event Hubs with Stream Analytics; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Real-time pipeline from events to warehouse.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Context:** Streaming to Warehouse is core to Azure Solution Architect interviews covering Event Hubs, Stream Analytics, Synapse, Delta Lake.

**Architect approach:**
1. Map business requirement to Event Hubs — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Real-time pipeline from events to warehouse.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect real-time pipeline from events to warehouse — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to Event Hubs?**
2. **What KPI proves streaming to warehouse adoption succeeded?**

### Common Mistakes in Interviews

- Listing Event Hubs without explaining trade-offs
- No Policy or IaC enforcement for streaming to warehouse
- Skipping operational runbook for Event Hubs

---

## Q066: Streaming to Warehouse — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Integration |
| **Frequency** | Common |

### Question

**Intermediate:** Design production streaming to warehouse for a 10-subscription enterprise (Azure Data Platform).

### Short Answer (30 seconds)

Platform hosts shared Event Hubs; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Design:** Multi-subscription estate with platform vs application separation.
Shared Event Hubs and Stream Analytics in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Real-time pipeline from events to warehouse.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize streaming to warehouse.

### Follow-up Questions

1. **How do Policy exemptions work during streaming to warehouse migration?**
2. **What FinOps tag strategy supports streaming to warehouse chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for Event Hubs testing
- Policies only at resource group — not MG

---

## Q067: Data FinOps — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Data FinOps using Cosmos RU optimization in a Azure Data Platform architecture review?

### Short Answer (30 seconds)

Use Cosmos RU optimization with storage tiering; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Data platform cost optimization and ru/partition planning.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Context:** Data FinOps is core to Azure Solution Architect interviews covering Cosmos RU optimization, storage tiering, serverless options.

**Architect approach:**
1. Map business requirement to Cosmos RU optimization — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Data platform cost optimization and ru/partition planning.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect data platform cost optimization and RU/partition planning — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to Cosmos RU optimization?**
2. **What KPI proves data finops adoption succeeded?**

### Common Mistakes in Interviews

- Listing Cosmos RU optimization without explaining trade-offs
- No Policy or IaC enforcement for data finops
- Skipping operational runbook for Cosmos RU optimization

---

## Q068: Data FinOps — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

**Intermediate:** Design production data finops for a 10-subscription enterprise (Azure Data Platform).

### Short Answer (30 seconds)

Platform hosts shared Cosmos RU optimization; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Design:** Multi-subscription estate with platform vs application separation.
Shared Cosmos RU optimization and storage tiering in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Data platform cost optimization and ru/partition planning.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize data finops.

### Follow-up Questions

1. **How do Policy exemptions work during data finops migration?**
2. **What FinOps tag strategy supports data finops chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for Cosmos RU optimization testing
- Policies only at resource group — not MG

---

## Q069: Polyglot Reference Architecture — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Architecture |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Polyglot Reference Architecture using SQL in a Azure Data Platform architecture review?

### Short Answer (30 seconds)

Use SQL with Cosmos; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Synthesize polyglot data stores for capstone scenarios.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Context:** Polyglot Reference Architecture is core to Azure Solution Architect interviews covering SQL, Cosmos, Redis, Blob.

**Architect approach:**
1. Map business requirement to SQL — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Synthesize polyglot data stores for capstone scenarios.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect synthesize polyglot data stores for capstone scenarios — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to SQL?**
2. **What KPI proves polyglot reference architecture adoption succeeded?**

### Common Mistakes in Interviews

- Listing SQL without explaining trade-offs
- No Policy or IaC enforcement for polyglot reference architecture
- Skipping operational runbook for SQL

---

## Q070: Polyglot Reference Architecture — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Architecture |
| **Frequency** | Common |

### Question

**Intermediate:** Design production polyglot reference architecture for a 10-subscription enterprise (Azure Data Platform).

### Short Answer (30 seconds)

Platform hosts shared SQL; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 11:** Azure Data Platform

**Design:** Multi-subscription estate with platform vs application separation.
Shared SQL and Cosmos in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Synthesize polyglot data stores for capstone scenarios.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize polyglot reference architecture.

### Follow-up Questions

1. **How do Policy exemptions work during polyglot reference architecture migration?**
2. **What FinOps tag strategy supports polyglot reference architecture chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for SQL testing
- Policies only at resource group — not MG

---
