# Week 11 — Advanced Q&A

> Q071–Q100: Premium format (Week 1 quality).

---


## Q071: Azure SQL vs Cosmos DB — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Data |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling azure sql vs cosmos db across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for Azure SQL.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 11:** Azure Data Platform

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Azure SQL vs Cosmos DB must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full azure sql vs cosmos db immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** Azure SQL, Cosmos DB, bounded context, polyglot persistence. Mitigation: Policy exemptions with expiry; game day validation.
Choose sql vs cosmos per bounded context access pattern.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating azure sql vs cosmos db for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q072: Azure SQL vs Cosmos DB — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Data |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling azure sql vs cosmos db across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for Azure SQL.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 11:** Azure Data Platform

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Azure SQL vs Cosmos DB must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full azure sql vs cosmos db immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** Azure SQL, Cosmos DB, bounded context, polyglot persistence. Mitigation: Policy exemptions with expiry; game day validation.
Choose sql vs cosmos per bounded context access pattern.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating azure sql vs cosmos db for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q073: Cosmos Partition Key Design — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Cosmos DB |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling cosmos partition key design across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for partition key.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 11:** Azure Data Platform

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Cosmos Partition Key Design must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full cosmos partition key design immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** partition key, hot partitions, RU/s, 429 throttling. Mitigation: Policy exemptions with expiry; game day validation.
Partition key design for multi-tenant saas at scale.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating cosmos partition key design for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q074: Cosmos Partition Key Design — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Cosmos DB |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to cosmos partition key design without downtime?

### Short Answer (30 seconds)

Tier workloads, phase cosmos partition key design rollout, time-bound exemptions, golden-path IaC using partition key.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 11:** Azure Data Platform

**Scenario:** Migrating brownfield workloads to cosmos partition key design without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full cosmos partition key design on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** partition key, hot partitions, RU/s. Anchor: **partition key** + **hot partitions**.
Partition key design for multi-tenant saas at scale.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same cosmos partition key design strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q075: Azure SQL HA and DR — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | SQL |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to azure sql ha and dr without downtime?

### Short Answer (30 seconds)

Tier workloads, phase azure sql ha and dr rollout, time-bound exemptions, golden-path IaC using zone redundancy.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 11:** Azure Data Platform

**Scenario:** Migrating brownfield workloads to azure sql ha and dr without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full azure sql ha and dr on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** zone redundancy, geo-replication, failover groups. Anchor: **zone redundancy** + **geo-replication**.
Sql ha/dr options mapped to business rpo/rto.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same azure sql ha and dr strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q076: Azure SQL HA and DR — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | SQL |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling azure sql ha and dr across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for zone redundancy.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 11:** Azure Data Platform

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Azure SQL HA and DR must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full azure sql ha and dr immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** zone redundancy, geo-replication, failover groups, RPO/RTO. Mitigation: Policy exemptions with expiry; game day validation.
Sql ha/dr options mapped to business rpo/rto.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating azure sql ha and dr for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q077: Hyperscale and Elastic Pools — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | SQL |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling hyperscale and elastic pools across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for Hyperscale.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 11:** Azure Data Platform

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Hyperscale and Elastic Pools must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full hyperscale and elastic pools immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** Hyperscale, elastic pools, serverless SQL, vCore sizing. Mitigation: Policy exemptions with expiry; game day validation.
Elastic pools for saas with many small tenant databases.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating hyperscale and elastic pools for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q078: Hyperscale and Elastic Pools — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | SQL |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling hyperscale and elastic pools across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for Hyperscale.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 11:** Azure Data Platform

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Hyperscale and Elastic Pools must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full hyperscale and elastic pools immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** Hyperscale, elastic pools, serverless SQL, vCore sizing. Mitigation: Policy exemptions with expiry; game day validation.
Elastic pools for saas with many small tenant databases.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating hyperscale and elastic pools for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q079: Blob Storage Tiers — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Storage |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling blob storage tiers across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for Hot/Cool/Cold/Archive.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 11:** Azure Data Platform

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Blob Storage Tiers must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full blob storage tiers immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** Hot/Cool/Cold/Archive, lifecycle management, immutability. Mitigation: Policy exemptions with expiry; game day validation.
Blob tiering and lifecycle for cost and compliance retention.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating blob storage tiers for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q080: Blob Storage Tiers — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Storage |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to blob storage tiers without downtime?

### Short Answer (30 seconds)

Tier workloads, phase blob storage tiers rollout, time-bound exemptions, golden-path IaC using Hot/Cool/Cold/Archive.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 11:** Azure Data Platform

**Scenario:** Migrating brownfield workloads to blob storage tiers without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full blob storage tiers on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** Hot/Cool/Cold/Archive, lifecycle management, immutability. Anchor: **Hot/Cool/Cold/Archive** + **lifecycle management**.
Blob tiering and lifecycle for cost and compliance retention.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same blob storage tiers strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q081: Synapse and Analytics Path — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Analytics |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to synapse and analytics path without downtime?

### Short Answer (30 seconds)

Tier workloads, phase synapse and analytics path rollout, time-bound exemptions, golden-path IaC using Synapse.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 11:** Azure Data Platform

**Scenario:** Migrating brownfield workloads to synapse and analytics path without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full synapse and analytics path on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** Synapse, serverless SQL, data lake. Anchor: **Synapse** + **serverless SQL**.
Analytics path that protects oltp from heavy reporting.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same synapse and analytics path strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q082: Synapse and Analytics Path — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Analytics |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling synapse and analytics path across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for Synapse.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 11:** Azure Data Platform

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Synapse and Analytics Path must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full synapse and analytics path immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** Synapse, serverless SQL, data lake, CDC. Mitigation: Policy exemptions with expiry; game day validation.
Analytics path that protects oltp from heavy reporting.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating synapse and analytics path for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q083: Event Hubs Ingestion — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Streaming |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling event hubs ingestion across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for Event Hubs.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 11:** Azure Data Platform

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Event Hubs Ingestion must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full event hubs ingestion immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** Event Hubs, partitions, capture, Kafka endpoint. Mitigation: Policy exemptions with expiry; game day validation.
High-volume telemetry ingest with event hubs architecture.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating event hubs ingestion for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q084: Event Hubs Ingestion — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Streaming |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling event hubs ingestion across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for Event Hubs.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 11:** Azure Data Platform

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Event Hubs Ingestion must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full event hubs ingestion immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** Event Hubs, partitions, capture, Kafka endpoint. Mitigation: Policy exemptions with expiry; game day validation.
High-volume telemetry ingest with event hubs architecture.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating event hubs ingestion for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q085: Data Encryption Strategy — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling data encryption strategy across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for TDE.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 11:** Azure Data Platform

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Data Encryption Strategy must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full data encryption strategy immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** TDE, CMK, Always Encrypted, double encryption. Mitigation: Policy exemptions with expiry; game day validation.
Encryption layers for healthcare and pci data classifications.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating data encryption strategy for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q086: Data Encryption Strategy — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Security |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to data encryption strategy without downtime?

### Short Answer (30 seconds)

Tier workloads, phase data encryption strategy rollout, time-bound exemptions, golden-path IaC using TDE.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 11:** Azure Data Platform

**Scenario:** Migrating brownfield workloads to data encryption strategy without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full data encryption strategy on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** TDE, CMK, Always Encrypted. Anchor: **TDE** + **CMK**.
Encryption layers for healthcare and pci data classifications.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same data encryption strategy strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q087: Cosmos Consistency Levels — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Cosmos DB |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to cosmos consistency levels without downtime?

### Short Answer (30 seconds)

Tier workloads, phase cosmos consistency levels rollout, time-bound exemptions, golden-path IaC using session.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 11:** Azure Data Platform

**Scenario:** Migrating brownfield workloads to cosmos consistency levels without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full cosmos consistency levels on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** session, bounded staleness, strong. Anchor: **session** + **bounded staleness**.
Consistency level selection per read pattern and region layout.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same cosmos consistency levels strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q088: Cosmos Consistency Levels — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Cosmos DB |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling cosmos consistency levels across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for session.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 11:** Azure Data Platform

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Cosmos Consistency Levels must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full cosmos consistency levels immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** session, bounded staleness, strong, eventual consistency. Mitigation: Policy exemptions with expiry; game day validation.
Consistency level selection per read pattern and region layout.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating cosmos consistency levels for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q089: SQL Performance Tuning — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | SQL |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling sql performance tuning across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for Query Store.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 11:** Azure Data Platform

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
SQL Performance Tuning must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full sql performance tuning immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** Query Store, indexes, DTU/vCore monitoring, read replicas. Mitigation: Policy exemptions with expiry; game day validation.
Sql performance architecture before scaling sku blindly.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating sql performance tuning for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q090: SQL Performance Tuning — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | SQL |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling sql performance tuning across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for Query Store.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 11:** Azure Data Platform

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
SQL Performance Tuning must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full sql performance tuning immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** Query Store, indexes, DTU/vCore monitoring, read replicas. Mitigation: Policy exemptions with expiry; game day validation.
Sql performance architecture before scaling sku blindly.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating sql performance tuning for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q091: Data Lake Architecture — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Analytics |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling data lake architecture across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for ADLS Gen2.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 11:** Azure Data Platform

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Data Lake Architecture must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full data lake architecture immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** ADLS Gen2, Parquet, medallion architecture, Synapse pipelines. Mitigation: Policy exemptions with expiry; game day validation.
Medallion lakehouse pattern on azure for analytics.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating data lake architecture for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q092: Redis Cache Patterns — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Caching |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to redis cache patterns without downtime?

### Short Answer (30 seconds)

Tier workloads, phase redis cache patterns rollout, time-bound exemptions, golden-path IaC using Azure Cache for Redis.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 11:** Azure Data Platform

**Scenario:** Migrating brownfield workloads to redis cache patterns without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full redis cache patterns on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** Azure Cache for Redis, cache-aside, TTL. Anchor: **Azure Cache for Redis** + **cache-aside**.
Redis for session, catalog cache, and rate limiting.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same redis cache patterns strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q093: Backup and LTR — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | DR |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling backup and ltr across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for automated backup.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 11:** Azure Data Platform

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Backup and LTR must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full backup and ltr immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** automated backup, long-term retention, point-in-time restore. Mitigation: Policy exemptions with expiry; game day validation.
Backup retention aligned to compliance and restore testing.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating backup and ltr for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q094: Multi-Region Data — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Reliability |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling multi-region data across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for Cosmos multi-region.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 11:** Azure Data Platform

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Multi-Region Data must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full multi-region data immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** Cosmos multi-region, SQL geo-replica, conflict resolution. Mitigation: Policy exemptions with expiry; game day validation.
Multi-region data strategy with consistency trade-offs.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating multi-region data for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q095: Data Governance — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Governance |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to data governance without downtime?

### Short Answer (30 seconds)

Tier workloads, phase data governance rollout, time-bound exemptions, golden-path IaC using Purview.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 11:** Azure Data Platform

**Scenario:** Migrating brownfield workloads to data governance without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full data governance on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** Purview, classification, lineage. Anchor: **Purview** + **classification**.
Data governance for enterprise azure data estate.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same data governance strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q096: Migration to Azure SQL — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Migration |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling migration to azure sql across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for DMA.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 11:** Azure Data Platform

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Migration to Azure SQL must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full migration to azure sql immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** DMA, DMS, offline vs online migration, compatibility. Mitigation: Policy exemptions with expiry; game day validation.
Sql migration approach with downtime window analysis.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating migration to azure sql for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q097: NoSQL vs SQL Decision — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Architecture |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling nosql vs sql decision across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for decision matrix.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 11:** Azure Data Platform

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
NoSQL vs SQL Decision must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full nosql vs sql decision immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** decision matrix, CAP, access patterns, transactions. Mitigation: Policy exemptions with expiry; game day validation.
Structured decision framework for sql vs nosql on azure.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating nosql vs sql decision for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q098: Streaming to Warehouse — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Integration |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to streaming to warehouse without downtime?

### Short Answer (30 seconds)

Tier workloads, phase streaming to warehouse rollout, time-bound exemptions, golden-path IaC using Event Hubs.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 11:** Azure Data Platform

**Scenario:** Migrating brownfield workloads to streaming to warehouse without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full streaming to warehouse on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** Event Hubs, Stream Analytics, Synapse. Anchor: **Event Hubs** + **Stream Analytics**.
Real-time pipeline from events to warehouse.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same streaming to warehouse strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q099: Data FinOps — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling data finops across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for Cosmos RU optimization.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 11:** Azure Data Platform

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Data FinOps must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full data finops immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** Cosmos RU optimization, storage tiering, serverless options. Mitigation: Policy exemptions with expiry; game day validation.
Data platform cost optimization and ru/partition planning.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating data finops for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q100: Polyglot Reference Architecture — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Architecture |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling polyglot reference architecture across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for SQL.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 11:** Azure Data Platform

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Polyglot Reference Architecture must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full polyglot reference architecture immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** SQL, Cosmos, Redis, Blob. Mitigation: Policy exemptions with expiry; game day validation.
Synthesize polyglot data stores for capstone scenarios.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating polyglot reference architecture for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---
