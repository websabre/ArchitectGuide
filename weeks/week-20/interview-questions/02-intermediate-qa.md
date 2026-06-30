# Week 20 — Intermediate Q&A

> Q031–Q070: Premium format (Week 1 quality).

---


## Q031: Portable Cloud Abstractions

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Multi-Cloud |
| **Frequency** | Very Common |

### Question

What abstractions are genuinely portable across Azure and AWS?

### Short Answer (30 seconds)

Kubernetes workloads, PostgreSQL, object storage (S3/Blob API via SDK abstraction), Terraform/Pulumi, OpenTelemetry, OAuth/OIDC — not proprietary PaaS lock-in without adapter.

### Detailed Answer (3–5 minutes)

**Portable:** Containers on K8s, standard SQL, message semantics (with adapter), IaC modules per cloud.

**Not portable:** App Service vs Elastic Beanstalk configs, Azure Service Bus vs SQS feature parity.

**Architect:** Portability where business requires; embrace managed services where one cloud is primary.

### Architecture Perspective

Pragmatic portability beats theoretical multi-cloud.

### Follow-up Questions

1. **MinIO for S3 API on-prem? — Hybrid object storage pattern.**
2. **Cross-cloud K8s? — EKS + AKS similar; networking/IAM differ.**

### Common Mistakes in Interviews

- Abstract every service behind lowest common denominator
- Multi-cloud day one without business driver
- Ignore operational cost of abstraction layer

---

## Q032: Azure vs AWS Service Mapping

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Multi-Cloud |
| **Frequency** | Very Common |

### Question

Map key services: compute, identity, messaging, data — Azure vs AWS?

### Short Answer (30 seconds)

Compute: App Service/AKS ↔ ECS/EKS/Lambda. Identity: Entra ID ↔ IAM/Cognito. Messaging: Service Bus ↔ SQS/SNS/EventBridge. Data: Azure SQL ↔ RDS/Aurora; Cosmos ↔ DynamoDB.

### Detailed Answer (3–5 minutes)

**Interview tip:** Know equivalents but explain *differences* — not 1:1.

**Example:** Azure MI vs AWS IAM roles — similar concept, different implementation.

**Architect:** Migration estimates need feature gap analysis per service.

### Architecture Perspective

Mapping shows breadth without shallow name-dropping.

### Follow-up Questions

1. **APIM vs API Gateway? — Feature and pricing differ.**
2. **Key Vault vs Secrets Manager? — Rotation patterns differ.**

### Common Mistakes in Interviews

- Assume feature parity across clouds
- Map only names not capabilities
- No gap analysis in migration plan

---

## Q033: Multi-Cloud Anti-Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Multi-Cloud |
| **Frequency** | Very Common |

### Question

Multi-cloud anti-patterns architects should call out?

### Short Answer (30 seconds)

Active-active multi-cloud without 2x ops team, lowest-common-denominator platform, split brain data writes, ignoring egress between clouds, compliance complexity multiplied.

### Detailed Answer (3–5 minutes)

**Valid multi-cloud:** Acquisition integration, regulatory residency, vendor negotiation, DR to second cloud.

**Invalid:** 'Avoid lock-in' on 3 services without TCO model.

**Architect:** Primary cloud + DR secondary is common; dual primary is rare and expensive.

### Architecture Perspective

Calling out anti-patterns shows senior judgment.

### Follow-up Questions

1. **Cloud-agnostic Terraform only? — Still need cloud-specific modules.**
2. **Anthos/Azure Arc? — Hybrid management — know positioning.**

### Common Mistakes in Interviews

- Dual write to Azure SQL and RDS
- Multi-cloud for 5-person startup
- No primary cloud designated

---

## Q034: Hybrid Connectivity Comparison

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

ExpressRoute vs AWS Direct Connect — hybrid design considerations?

### Short Answer (30 seconds)

Both: private dedicated connection to cloud, bypass internet, predictable latency. Design: redundant connections, separate providers, BGP routing, on-prem firewall inspection.

### Detailed Answer (3–5 minutes)

**Architect checklist:**
- Dual circuits different carriers
- Encryption in transit (MACsec optional)
- Bandwidth headroom for DR sync
- Split tunnel vs full tunnel from on-prem

**VPN backup:** Site-to-Site VPN as failover path.

### Architecture Perspective

Hybrid connectivity is enterprise architect bread and butter.

### Follow-up Questions

1. **ExpressRoute Global Reach? — Cross-region private connectivity.**
2. **Direct Connect Gateway? — Multi-VPC/VIF aggregation.**

### Common Mistakes in Interviews

- Single circuit no redundancy
- No bandwidth monitoring
- Treat VPN as primary production path

---

## Q035: Cross-Cloud Disaster Recovery

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DR |
| **Frequency** | Common |

### Question

Design DR with primary Azure and secondary AWS?

### Short Answer (30 seconds)

Async replication, RPO measured in minutes-hours, runbook for DNS failover (Route 53/Traffic Manager), data sync via DB replication or event streaming, regular DR drills documented.

### Detailed Answer (3–5 minutes)

**Patterns:**
- Backup blobs cross-cloud (egress cost!)
- Kafka/Event Hubs replication niche
- Terraform dual-region modules

**Architect:** DR to different cloud is expensive — justify vs same-cloud region pair DR.

### Architecture Perspective

Cross-cloud DR is advanced scenario.

### Follow-up Questions

1. **RTO for DNS failover? — TTL + health check propagation.**
2. **Immutable backups? — Ransomware protection cross-cloud.**

### Common Mistakes in Interviews

- DR never tested
- Ignore cross-cloud egress in RPO math
- Assume automatic failover without runbook

---

## Q036: Identity Federation Multi-Cloud

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Common |

### Question

Single corporate identity accessing Azure and AWS?

### Short Answer (30 seconds)

Entra ID (or Okta) → SAML/OIDC federation to AWS IAM Identity Center and Azure native SSO. No duplicate user stores; conditional access policies unified where possible.

### Detailed Answer (3–5 minutes)

**AWS:** IAM Identity Center permission sets per account.

**Azure:** Entra ID app registrations and RBAC.

**Architect:** Central IdP; cloud-specific authorization; no long-lived cloud passwords for humans.

### Architecture Perspective

Identity is multi-cloud integration cornerstone.

### Follow-up Questions

1. **SCIM provisioning? — Automate user lifecycle to both clouds.**
2. **Break-glass accounts? — Separate process per cloud audited.**

### Common Mistakes in Interviews

- Duplicate IAM users per cloud manually
- Shared admin password in vault
- No MFA on federated access

---

## Q037: FinOps Across Cloud Providers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

CFO wants unified cloud cost view across Azure and AWS?

### Short Answer (30 seconds)

Tags/labels standardized (Environment, CostCenter), export CUR + Azure Cost Management to FinOps tool (CloudHealth, Finout), unit economics dashboard, anomaly alerts per provider.

### Detailed Answer (3–5 minutes)

**Architect:** Mandate tag policy both clouds before scale.

**Challenge:** Different billing granularity — normalize in warehouse.

**Governance:** Monthly review with engineering managers by CostCenter.

### Architecture Perspective

Multi-cloud FinOps requires discipline upfront.

### Follow-up Questions

1. **Reserved capacity strategy per cloud? — Separate RI/SP purchases.**
2. **Commitment exchange? — Provider-specific — no cross-cloud.**

### Common Mistakes in Interviews

- No tag standards across clouds
- Finance sees invoice surprise monthly
- Optimize one cloud while other bleeds

---

## Q038: Egress and Data Transfer Costs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Very Common |

### Question

Why is multi-cloud data transfer expensive? Mitigations?

### Short Answer (30 seconds)

Cross-cloud egress charged per GB both sides; cross-AZ also adds up. Mitigate: data locality, compression, CDN, batch sync off-peak, process data where stored.

### Detailed Answer (3–5 minutes)

**Architect modeling:** Include egress in TCO for replication, DR, and analytics pipelines.

**Azure:** Egress to internet and inter-region.

**AWS:** Data transfer out + cross-AZ.

**Pattern:** Analytics in same region as data lake.

### Architecture Perspective

Egress ignorance causes budget overruns.

### Follow-up Questions

1. **CloudFront/CDN reduce origin egress? — Cache hit ratio matters.**
2. **Private connectivity egress? — Still often charged — read fine print.**

### Common Mistakes in Interviews

- Replicate all data bidirectionally realtime
- No egress alerts
- Cross-cloud analytics without locality plan

---

## Q039: Vendor Lock-In Mitigation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Strategy |
| **Frequency** | Common |

### Question

Mitigate vendor lock-in without full multi-cloud?

### Short Answer (30 seconds)

Open formats (Parquet, Postgres), containerized workloads, IaC, avoid proprietary-only APIs in core domain, exit plan ADR per critical service, data export tested annually.

### Detailed Answer (3–5 minutes)

**Pragmatic:** Lock-in is trade-off for velocity — document accepted lock-in.

**High lock-in:** DynamoDB-specific queries, Step Functions orchestration, Cosmos DB RU model.

**Architect:** ADR: 'We accept Azure Service Bus lock-in because...'

### Architecture Perspective

Mature architects document lock-in decisions.

### Follow-up Questions

1. **Abstraction layer cost? — Team maintains adapters — budget for it.**
2. **Open source on cloud? — Still operational lock-in on that cloud.**

### Common Mistakes in Interviews

- Fear lock-in blocks all managed services
- No export test of critical data
- Abstraction without business justification

---

## Q040: Choosing Primary Cloud per Workload

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Strategy |
| **Frequency** | Very Common |

### Question

Framework for assigning workloads to Azure vs AWS in enterprise?

### Short Answer (30 seconds)

Team skill, existing commitments, service feature fit, compliance region availability, commercial EA/discounts, acquisition inherited estate, latency to users.

### Detailed Answer (3–5 minutes)

**Decision matrix:** Score each workload 1-5 on criteria; weighted sum.

**Example:** .NET team on Azure EA → new .NET APIs on Azure; acquired Java shop on AWS stays until migration wave.

**Architect:** Polite truth — two clouds have cost; consolidate when possible.

### Architecture Perspective

Workload placement is political and technical.

### Follow-up Questions

1. **Landing zone both clouds? — Only if business requires — cost it.**
2. **Exit criteria? — When to consolidate clouds — define upfront.**

### Common Mistakes in Interviews

- Religious one-cloud-only without assessment
- Split monolith across two clouds randomly
- No documented placement criteria

---

## Q041: Cloud Bursting / Cloud Bursting Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hybrid |
| **Frequency** | Very Common |

### Question

What must architects know about Cloud Bursting / Cloud Bursting?

### Short Answer (30 seconds)

Overflow burst capacity from on-premises to public cloud

### Detailed Answer (3–5 minutes)

**Topic:** Cloud Bursting / Cloud Bursting
**Focus:** Overflow burst capacity from on-premises to public cloud

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 20 context:** What must architects know about Cloud Bursting / Cloud Bursting?

### Architecture Perspective

Cloud Bursting / Cloud Bursting is essential Week 20 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Cloud Bursting / Cloud Bursting?**
2. **Common production mistake with Cloud Bursting / Cloud Bursting?**

### Common Mistakes in Interviews

- Confusing Cloud Bursting / Cloud Bursting with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Cloud Bursting / Cloud Bursting failures

---

## Q042: Cloud Bursting / Cloud Bursting Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hybrid |
| **Frequency** | Very Common |

### Question

How deploy Cloud Bursting / Cloud Bursting in production enterprise workloads?

### Short Answer (30 seconds)

Overflow burst capacity from on-premises to public cloud

### Detailed Answer (3–5 minutes)

**Topic:** Cloud Bursting / Cloud Bursting
**Focus:** Overflow burst capacity from on-premises to public cloud

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 20 context:** How deploy Cloud Bursting / Cloud Bursting in production enterprise workloads?

### Architecture Perspective

Cloud Bursting / Cloud Bursting is essential Week 20 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Cloud Bursting / Cloud Bursting?**
2. **Common production mistake with Cloud Bursting / Cloud Bursting?**

### Common Mistakes in Interviews

- Confusing Cloud Bursting / Cloud Bursting with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Cloud Bursting / Cloud Bursting failures

---

## Q043: Cloud Bursting / Cloud Bursting Advanced Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hybrid |
| **Frequency** | Common |

### Question

Advanced Cloud Bursting / Cloud Bursting tuning and edge cases?

### Short Answer (30 seconds)

Overflow burst capacity from on-premises to public cloud

### Detailed Answer (3–5 minutes)

**Topic:** Cloud Bursting / Cloud Bursting
**Focus:** Overflow burst capacity from on-premises to public cloud

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 20 context:** Advanced Cloud Bursting / Cloud Bursting tuning and edge cases?

### Architecture Perspective

Cloud Bursting / Cloud Bursting is essential Week 20 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Cloud Bursting / Cloud Bursting?**
2. **Common production mistake with Cloud Bursting / Cloud Bursting?**

### Common Mistakes in Interviews

- Confusing Cloud Bursting / Cloud Bursting with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Cloud Bursting / Cloud Bursting failures

---

## Q044: Cloud Bursting / Cloud Bursting Architecture Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hybrid |
| **Frequency** | Common |

### Question

Architecture trade-offs for Cloud Bursting / Cloud Bursting?

### Short Answer (30 seconds)

Overflow burst capacity from on-premises to public cloud

### Detailed Answer (3–5 minutes)

**Topic:** Cloud Bursting / Cloud Bursting
**Focus:** Overflow burst capacity from on-premises to public cloud

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 20 context:** Architecture trade-offs for Cloud Bursting / Cloud Bursting?

### Architecture Perspective

Cloud Bursting / Cloud Bursting is essential Week 20 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Cloud Bursting / Cloud Bursting?**
2. **Common production mistake with Cloud Bursting / Cloud Bursting?**

### Common Mistakes in Interviews

- Confusing Cloud Bursting / Cloud Bursting with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Cloud Bursting / Cloud Bursting failures

---

## Q045: Azure Arc Hybrid Control Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hybrid |
| **Frequency** | Very Common |

### Question

What must architects know about Azure Arc Hybrid Control?

### Short Answer (30 seconds)

Manage on-premises and multi-cloud from Azure control plane

### Detailed Answer (3–5 minutes)

**Topic:** Azure Arc Hybrid Control
**Focus:** Manage on-premises and multi-cloud from Azure control plane

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 20 context:** What must architects know about Azure Arc Hybrid Control?

### Architecture Perspective

Azure Arc Hybrid Control is essential Week 20 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Azure Arc Hybrid Control?**
2. **Common production mistake with Azure Arc Hybrid Control?**

### Common Mistakes in Interviews

- Confusing Azure Arc Hybrid Control with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Azure Arc Hybrid Control failures

---

## Q046: Azure Arc Hybrid Control Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hybrid |
| **Frequency** | Very Common |

### Question

How deploy Azure Arc Hybrid Control in production enterprise workloads?

### Short Answer (30 seconds)

Manage on-premises and multi-cloud from Azure control plane

### Detailed Answer (3–5 minutes)

**Topic:** Azure Arc Hybrid Control
**Focus:** Manage on-premises and multi-cloud from Azure control plane

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 20 context:** How deploy Azure Arc Hybrid Control in production enterprise workloads?

### Architecture Perspective

Azure Arc Hybrid Control is essential Week 20 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Azure Arc Hybrid Control?**
2. **Common production mistake with Azure Arc Hybrid Control?**

### Common Mistakes in Interviews

- Confusing Azure Arc Hybrid Control with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Azure Arc Hybrid Control failures

---

## Q047: Azure Arc Hybrid Control Advanced Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hybrid |
| **Frequency** | Common |

### Question

Advanced Azure Arc Hybrid Control tuning and edge cases?

### Short Answer (30 seconds)

Manage on-premises and multi-cloud from Azure control plane

### Detailed Answer (3–5 minutes)

**Topic:** Azure Arc Hybrid Control
**Focus:** Manage on-premises and multi-cloud from Azure control plane

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 20 context:** Advanced Azure Arc Hybrid Control tuning and edge cases?

### Architecture Perspective

Azure Arc Hybrid Control is essential Week 20 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Azure Arc Hybrid Control?**
2. **Common production mistake with Azure Arc Hybrid Control?**

### Common Mistakes in Interviews

- Confusing Azure Arc Hybrid Control with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Azure Arc Hybrid Control failures

---

## Q048: Azure Arc Hybrid Control Architecture Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hybrid |
| **Frequency** | Common |

### Question

Architecture trade-offs for Azure Arc Hybrid Control?

### Short Answer (30 seconds)

Manage on-premises and multi-cloud from Azure control plane

### Detailed Answer (3–5 minutes)

**Topic:** Azure Arc Hybrid Control
**Focus:** Manage on-premises and multi-cloud from Azure control plane

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 20 context:** Architecture trade-offs for Azure Arc Hybrid Control?

### Architecture Perspective

Azure Arc Hybrid Control is essential Week 20 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Azure Arc Hybrid Control?**
2. **Common production mistake with Azure Arc Hybrid Control?**

### Common Mistakes in Interviews

- Confusing Azure Arc Hybrid Control with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Azure Arc Hybrid Control failures

---

## Q049: Google Anthos Fleet Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Multi-Cloud |
| **Frequency** | Very Common |

### Question

What must architects know about Google Anthos Fleet?

### Short Answer (30 seconds)

Unified Kubernetes management across clouds and on-prem

### Detailed Answer (3–5 minutes)

**Topic:** Google Anthos Fleet
**Focus:** Unified Kubernetes management across clouds and on-prem

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 20 context:** What must architects know about Google Anthos Fleet?

### Architecture Perspective

Google Anthos Fleet is essential Week 20 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Google Anthos Fleet?**
2. **Common production mistake with Google Anthos Fleet?**

### Common Mistakes in Interviews

- Confusing Google Anthos Fleet with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Google Anthos Fleet failures

---

## Q050: Google Anthos Fleet Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Multi-Cloud |
| **Frequency** | Very Common |

### Question

How deploy Google Anthos Fleet in production enterprise workloads?

### Short Answer (30 seconds)

Unified Kubernetes management across clouds and on-prem

### Detailed Answer (3–5 minutes)

**Topic:** Google Anthos Fleet
**Focus:** Unified Kubernetes management across clouds and on-prem

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 20 context:** How deploy Google Anthos Fleet in production enterprise workloads?

### Architecture Perspective

Google Anthos Fleet is essential Week 20 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Google Anthos Fleet?**
2. **Common production mistake with Google Anthos Fleet?**

### Common Mistakes in Interviews

- Confusing Google Anthos Fleet with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Google Anthos Fleet failures

---

## Q051: Google Anthos Fleet Advanced Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Multi-Cloud |
| **Frequency** | Common |

### Question

Advanced Google Anthos Fleet tuning and edge cases?

### Short Answer (30 seconds)

Unified Kubernetes management across clouds and on-prem

### Detailed Answer (3–5 minutes)

**Topic:** Google Anthos Fleet
**Focus:** Unified Kubernetes management across clouds and on-prem

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 20 context:** Advanced Google Anthos Fleet tuning and edge cases?

### Architecture Perspective

Google Anthos Fleet is essential Week 20 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Google Anthos Fleet?**
2. **Common production mistake with Google Anthos Fleet?**

### Common Mistakes in Interviews

- Confusing Google Anthos Fleet with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Google Anthos Fleet failures

---

## Q052: Google Anthos Fleet Architecture Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Multi-Cloud |
| **Frequency** | Common |

### Question

Architecture trade-offs for Google Anthos Fleet?

### Short Answer (30 seconds)

Unified Kubernetes management across clouds and on-prem

### Detailed Answer (3–5 minutes)

**Topic:** Google Anthos Fleet
**Focus:** Unified Kubernetes management across clouds and on-prem

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 20 context:** Architecture trade-offs for Google Anthos Fleet?

### Architecture Perspective

Google Anthos Fleet is essential Week 20 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Google Anthos Fleet?**
2. **Common production mistake with Google Anthos Fleet?**

### Common Mistakes in Interviews

- Confusing Google Anthos Fleet with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Google Anthos Fleet failures

---

## Q053: Crossplane Control Plane Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | IaC |
| **Frequency** | Very Common |

### Question

What must architects know about Crossplane Control Plane?

### Short Answer (30 seconds)

Kubernetes-native declarative cloud resource management

### Detailed Answer (3–5 minutes)

**Topic:** Crossplane Control Plane
**Focus:** Kubernetes-native declarative cloud resource management

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 20 context:** What must architects know about Crossplane Control Plane?

### Architecture Perspective

Crossplane Control Plane is essential Week 20 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Crossplane Control Plane?**
2. **Common production mistake with Crossplane Control Plane?**

### Common Mistakes in Interviews

- Confusing Crossplane Control Plane with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Crossplane Control Plane failures

---

## Q054: Crossplane Control Plane Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | IaC |
| **Frequency** | Very Common |

### Question

How deploy Crossplane Control Plane in production enterprise workloads?

### Short Answer (30 seconds)

Kubernetes-native declarative cloud resource management

### Detailed Answer (3–5 minutes)

**Topic:** Crossplane Control Plane
**Focus:** Kubernetes-native declarative cloud resource management

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 20 context:** How deploy Crossplane Control Plane in production enterprise workloads?

### Architecture Perspective

Crossplane Control Plane is essential Week 20 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Crossplane Control Plane?**
2. **Common production mistake with Crossplane Control Plane?**

### Common Mistakes in Interviews

- Confusing Crossplane Control Plane with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Crossplane Control Plane failures

---

## Q055: Crossplane Control Plane Advanced Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | IaC |
| **Frequency** | Common |

### Question

Advanced Crossplane Control Plane tuning and edge cases?

### Short Answer (30 seconds)

Kubernetes-native declarative cloud resource management

### Detailed Answer (3–5 minutes)

**Topic:** Crossplane Control Plane
**Focus:** Kubernetes-native declarative cloud resource management

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 20 context:** Advanced Crossplane Control Plane tuning and edge cases?

### Architecture Perspective

Crossplane Control Plane is essential Week 20 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Crossplane Control Plane?**
2. **Common production mistake with Crossplane Control Plane?**

### Common Mistakes in Interviews

- Confusing Crossplane Control Plane with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Crossplane Control Plane failures

---

## Q056: Crossplane Control Plane Architecture Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | IaC |
| **Frequency** | Common |

### Question

Architecture trade-offs for Crossplane Control Plane?

### Short Answer (30 seconds)

Kubernetes-native declarative cloud resource management

### Detailed Answer (3–5 minutes)

**Topic:** Crossplane Control Plane
**Focus:** Kubernetes-native declarative cloud resource management

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 20 context:** Architecture trade-offs for Crossplane Control Plane?

### Architecture Perspective

Crossplane Control Plane is essential Week 20 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Crossplane Control Plane?**
2. **Common production mistake with Crossplane Control Plane?**

### Common Mistakes in Interviews

- Confusing Crossplane Control Plane with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Crossplane Control Plane failures

---

## Q057: Pulumi Multi-Language IaC Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | IaC |
| **Frequency** | Very Common |

### Question

What must architects know about Pulumi Multi-Language IaC?

### Short Answer (30 seconds)

TypeScript, Python, Go infrastructure as real code

### Detailed Answer (3–5 minutes)

**Topic:** Pulumi Multi-Language IaC
**Focus:** TypeScript, Python, Go infrastructure as real code

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 20 context:** What must architects know about Pulumi Multi-Language IaC?

### Architecture Perspective

Pulumi Multi-Language IaC is essential Week 20 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Pulumi Multi-Language IaC?**
2. **Common production mistake with Pulumi Multi-Language IaC?**

### Common Mistakes in Interviews

- Confusing Pulumi Multi-Language IaC with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Pulumi Multi-Language IaC failures

---

## Q058: Pulumi Multi-Language IaC Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | IaC |
| **Frequency** | Very Common |

### Question

How deploy Pulumi Multi-Language IaC in production enterprise workloads?

### Short Answer (30 seconds)

TypeScript, Python, Go infrastructure as real code

### Detailed Answer (3–5 minutes)

**Topic:** Pulumi Multi-Language IaC
**Focus:** TypeScript, Python, Go infrastructure as real code

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 20 context:** How deploy Pulumi Multi-Language IaC in production enterprise workloads?

### Architecture Perspective

Pulumi Multi-Language IaC is essential Week 20 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Pulumi Multi-Language IaC?**
2. **Common production mistake with Pulumi Multi-Language IaC?**

### Common Mistakes in Interviews

- Confusing Pulumi Multi-Language IaC with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Pulumi Multi-Language IaC failures

---

## Q059: Pulumi Multi-Language IaC Advanced Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | IaC |
| **Frequency** | Common |

### Question

Advanced Pulumi Multi-Language IaC tuning and edge cases?

### Short Answer (30 seconds)

TypeScript, Python, Go infrastructure as real code

### Detailed Answer (3–5 minutes)

**Topic:** Pulumi Multi-Language IaC
**Focus:** TypeScript, Python, Go infrastructure as real code

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 20 context:** Advanced Pulumi Multi-Language IaC tuning and edge cases?

### Architecture Perspective

Pulumi Multi-Language IaC is essential Week 20 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Pulumi Multi-Language IaC?**
2. **Common production mistake with Pulumi Multi-Language IaC?**

### Common Mistakes in Interviews

- Confusing Pulumi Multi-Language IaC with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Pulumi Multi-Language IaC failures

---

## Q060: Pulumi Multi-Language IaC Architecture Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | IaC |
| **Frequency** | Common |

### Question

Architecture trade-offs for Pulumi Multi-Language IaC?

### Short Answer (30 seconds)

TypeScript, Python, Go infrastructure as real code

### Detailed Answer (3–5 minutes)

**Topic:** Pulumi Multi-Language IaC
**Focus:** TypeScript, Python, Go infrastructure as real code

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 20 context:** Architecture trade-offs for Pulumi Multi-Language IaC?

### Architecture Perspective

Pulumi Multi-Language IaC is essential Week 20 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of Pulumi Multi-Language IaC?**
2. **Common production mistake with Pulumi Multi-Language IaC?**

### Common Mistakes in Interviews

- Confusing Pulumi Multi-Language IaC with adjacent service
- Console-only knowledge without design rationale
- No monitoring for Pulumi Multi-Language IaC failures

---

## Q061: CloudEvents Portability Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Integration |
| **Frequency** | Very Common |

### Question

What must architects know about CloudEvents Portability?

### Short Answer (30 seconds)

Vendor-neutral event envelope format

### Detailed Answer (3–5 minutes)

**Topic:** CloudEvents Portability
**Focus:** Vendor-neutral event envelope format

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 20 context:** What must architects know about CloudEvents Portability?

### Architecture Perspective

CloudEvents Portability is essential Week 20 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of CloudEvents Portability?**
2. **Common production mistake with CloudEvents Portability?**

### Common Mistakes in Interviews

- Confusing CloudEvents Portability with adjacent service
- Console-only knowledge without design rationale
- No monitoring for CloudEvents Portability failures

---

## Q062: CloudEvents Portability Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Integration |
| **Frequency** | Very Common |

### Question

How deploy CloudEvents Portability in production enterprise workloads?

### Short Answer (30 seconds)

Vendor-neutral event envelope format

### Detailed Answer (3–5 minutes)

**Topic:** CloudEvents Portability
**Focus:** Vendor-neutral event envelope format

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 20 context:** How deploy CloudEvents Portability in production enterprise workloads?

### Architecture Perspective

CloudEvents Portability is essential Week 20 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of CloudEvents Portability?**
2. **Common production mistake with CloudEvents Portability?**

### Common Mistakes in Interviews

- Confusing CloudEvents Portability with adjacent service
- Console-only knowledge without design rationale
- No monitoring for CloudEvents Portability failures

---

## Q063: CloudEvents Portability Advanced Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Integration |
| **Frequency** | Common |

### Question

Advanced CloudEvents Portability tuning and edge cases?

### Short Answer (30 seconds)

Vendor-neutral event envelope format

### Detailed Answer (3–5 minutes)

**Topic:** CloudEvents Portability
**Focus:** Vendor-neutral event envelope format

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 20 context:** Advanced CloudEvents Portability tuning and edge cases?

### Architecture Perspective

CloudEvents Portability is essential Week 20 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of CloudEvents Portability?**
2. **Common production mistake with CloudEvents Portability?**

### Common Mistakes in Interviews

- Confusing CloudEvents Portability with adjacent service
- Console-only knowledge without design rationale
- No monitoring for CloudEvents Portability failures

---

## Q064: CloudEvents Portability Architecture Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Integration |
| **Frequency** | Common |

### Question

Architecture trade-offs for CloudEvents Portability?

### Short Answer (30 seconds)

Vendor-neutral event envelope format

### Detailed Answer (3–5 minutes)

**Topic:** CloudEvents Portability
**Focus:** Vendor-neutral event envelope format

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 20 context:** Architecture trade-offs for CloudEvents Portability?

### Architecture Perspective

CloudEvents Portability is essential Week 20 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of CloudEvents Portability?**
2. **Common production mistake with CloudEvents Portability?**

### Common Mistakes in Interviews

- Confusing CloudEvents Portability with adjacent service
- Console-only knowledge without design rationale
- No monitoring for CloudEvents Portability failures

---

## Q065: OIDC Federation Portability Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Very Common |

### Question

What must architects know about OIDC Federation Portability?

### Short Answer (30 seconds)

Standard OAuth/OIDC across Azure, AWS, and GCP

### Detailed Answer (3–5 minutes)

**Topic:** OIDC Federation Portability
**Focus:** Standard OAuth/OIDC across Azure, AWS, and GCP

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 20 context:** What must architects know about OIDC Federation Portability?

### Architecture Perspective

OIDC Federation Portability is essential Week 20 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of OIDC Federation Portability?**
2. **Common production mistake with OIDC Federation Portability?**

### Common Mistakes in Interviews

- Confusing OIDC Federation Portability with adjacent service
- Console-only knowledge without design rationale
- No monitoring for OIDC Federation Portability failures

---

## Q066: OIDC Federation Portability Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Very Common |

### Question

How deploy OIDC Federation Portability in production enterprise workloads?

### Short Answer (30 seconds)

Standard OAuth/OIDC across Azure, AWS, and GCP

### Detailed Answer (3–5 minutes)

**Topic:** OIDC Federation Portability
**Focus:** Standard OAuth/OIDC across Azure, AWS, and GCP

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 20 context:** How deploy OIDC Federation Portability in production enterprise workloads?

### Architecture Perspective

OIDC Federation Portability is essential Week 20 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of OIDC Federation Portability?**
2. **Common production mistake with OIDC Federation Portability?**

### Common Mistakes in Interviews

- Confusing OIDC Federation Portability with adjacent service
- Console-only knowledge without design rationale
- No monitoring for OIDC Federation Portability failures

---

## Q067: OIDC Federation Portability Advanced Tuning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Common |

### Question

Advanced OIDC Federation Portability tuning and edge cases?

### Short Answer (30 seconds)

Standard OAuth/OIDC across Azure, AWS, and GCP

### Detailed Answer (3–5 minutes)

**Topic:** OIDC Federation Portability
**Focus:** Standard OAuth/OIDC across Azure, AWS, and GCP

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 20 context:** Advanced OIDC Federation Portability tuning and edge cases?

### Architecture Perspective

OIDC Federation Portability is essential Week 20 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of OIDC Federation Portability?**
2. **Common production mistake with OIDC Federation Portability?**

### Common Mistakes in Interviews

- Confusing OIDC Federation Portability with adjacent service
- Console-only knowledge without design rationale
- No monitoring for OIDC Federation Portability failures

---

## Q068: OIDC Federation Portability Architecture Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Common |

### Question

Architecture trade-offs for OIDC Federation Portability?

### Short Answer (30 seconds)

Standard OAuth/OIDC across Azure, AWS, and GCP

### Detailed Answer (3–5 minutes)

**Topic:** OIDC Federation Portability
**Focus:** Standard OAuth/OIDC across Azure, AWS, and GCP

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 20 context:** Architecture trade-offs for OIDC Federation Portability?

### Architecture Perspective

OIDC Federation Portability is essential Week 20 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of OIDC Federation Portability?**
2. **Common production mistake with OIDC Federation Portability?**

### Common Mistakes in Interviews

- Confusing OIDC Federation Portability with adjacent service
- Console-only knowledge without design rationale
- No monitoring for OIDC Federation Portability failures

---

## Q069: PostgreSQL Cross-Cloud Portability Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Data |
| **Frequency** | Very Common |

### Question

What must architects know about PostgreSQL Cross-Cloud Portability?

### Short Answer (30 seconds)

Same relational engine on RDS, Azure Flexible, Cloud SQL

### Detailed Answer (3–5 minutes)

**Topic:** PostgreSQL Cross-Cloud Portability
**Focus:** Same relational engine on RDS, Azure Flexible, Cloud SQL

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 20 context:** What must architects know about PostgreSQL Cross-Cloud Portability?

### Architecture Perspective

PostgreSQL Cross-Cloud Portability is essential Week 20 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of PostgreSQL Cross-Cloud Portability?**
2. **Common production mistake with PostgreSQL Cross-Cloud Portability?**

### Common Mistakes in Interviews

- Confusing PostgreSQL Cross-Cloud Portability with adjacent service
- Console-only knowledge without design rationale
- No monitoring for PostgreSQL Cross-Cloud Portability failures

---

## Q070: PostgreSQL Cross-Cloud Portability Production Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Data |
| **Frequency** | Very Common |

### Question

How deploy PostgreSQL Cross-Cloud Portability in production enterprise workloads?

### Short Answer (30 seconds)

Same relational engine on RDS, Azure Flexible, Cloud SQL

### Detailed Answer (3–5 minutes)

**Topic:** PostgreSQL Cross-Cloud Portability
**Focus:** Same relational engine on RDS, Azure Flexible, Cloud SQL

**Architect depth:**
- Requirements and NFR alignment
- Security, HA, and FinOps
- Monitoring, runbooks, and ADR documentation

**Week 20 context:** How deploy PostgreSQL Cross-Cloud Portability in production enterprise workloads?

### Architecture Perspective

PostgreSQL Cross-Cloud Portability is essential Week 20 solution architect knowledge.

### Follow-up Questions

1. **Azure or hybrid equivalent of PostgreSQL Cross-Cloud Portability?**
2. **Common production mistake with PostgreSQL Cross-Cloud Portability?**

### Common Mistakes in Interviews

- Confusing PostgreSQL Cross-Cloud Portability with adjacent service
- Console-only knowledge without design rationale
- No monitoring for PostgreSQL Cross-Cloud Portability failures

---
