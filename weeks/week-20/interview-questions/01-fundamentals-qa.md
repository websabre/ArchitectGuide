# Week 20 — Fundamentals Q&A

> Q001–Q030: Premium format (Week 1 quality).
> Cross-reference: [Interview prep hub](../../../interview-prep/README.md)

---


## Q001: Portable Cloud Abstractions

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q002: Azure vs AWS Service Mapping

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q003: Multi-Cloud Anti-Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q004: Hybrid Connectivity Comparison

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q005: Cross-Cloud Disaster Recovery

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q006: Identity Federation Multi-Cloud

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q007: FinOps Across Cloud Providers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q008: Egress and Data Transfer Costs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q009: Vendor Lock-In Mitigation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q010: Choosing Primary Cloud per Workload

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
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

## Q011: Terraform Multi-Cloud Modules

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | IaC |
| **Frequency** | Common |

### Question

Structure Terraform for Azure and AWS modules?

### Short Answer (30 seconds)

Root modules `env/prod/azure`, `env/prod/aws`; shared `modules/networking` with provider-specific submodules; remote state per env.

### Detailed Answer (3–5 minutes)

**Architect:** DRY where safe — don't force identical module interface where clouds differ.

**CI:** `terraform plan` on PR both providers.

### Architecture Perspective

IaC structure enables multi-cloud ops.

### Follow-up Questions

1. **Terragrunt wrappers? — DRY backend config.**
2. **State locking? — DynamoDB AWS; blob Azure.**

### Common Mistakes in Interviews

- One state file all clouds
- No plan review
- Copy-paste modules diverge

---

## Q012: Pulumi vs Terraform Team Choice

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | IaC |
| **Frequency** | Common |

### Question

Pulumi (.NET) vs Terraform (HCL) for dual-cloud team?

### Short Answer (30 seconds)

Pulumi: C# infrastructure, IDE support, unit test IaC. Terraform: HCL standard, larger module ecosystem.

### Detailed Answer (3–5 minutes)

**Architect:** All-.NET platform team may prefer Pulumi. Multi-team org often standardizes Terraform.

### Architecture Perspective

Team skill drives IaC language choice.

### Follow-up Questions

1. **CDKTF? — Terraform from TypeScript/C#.**
2. **Import existing resources? — Both support.**

### Common Mistakes in Interviews

- Two IaC languages no standard
- IaC not in CI
- Manual hotfix drift

---

## Q013: Kubernetes Portability EKS/AKS

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Containers |
| **Frequency** | Common |

### Question

Portable Kubernetes between EKS and AKS?

### Short Answer (30 seconds)

Standard K8s APIs portable; ingress, storage class, IAM differ — abstract with Helm values per cloud.

### Detailed Answer (3–5 minutes)

**Architect:** Avoid cloud-specific operators in portable core. GitOps (Argo CD) same workflow both.

### Architecture Perspective

K8s portability is partial not absolute.

### Follow-up Questions

1. **CSI drivers? — Per-cloud storage plugin.**
2. **Cluster autoscaling differs? — Karpenter vs CA.**

### Common Mistakes in Interviews

- Cloud lock-in CRDs everywhere
- No Helm values per env
- kubectl prod from laptop

---

## Q014: PostgreSQL Portable Across Clouds

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Data |
| **Frequency** | Common |

### Question

Run PostgreSQL portable on RDS and Azure Flexible Server?

### Short Answer (30 seconds)

Stick to portable SQL features; avoid vendor extensions; use standard connection pooling; migration via pg_dump/logical replication.

### Detailed Answer (3–5 minutes)

**Architect:** ORM and migrations tool (Flyway) cloud-agnostic. Test on both before claiming portable.

### Architecture Perspective

Database portability limits ORM features used.

### Follow-up Questions

1. **Citus/Azure-specific? — Breaks portability.**
2. **Connection string abstraction? — Config per cloud.**

### Common Mistakes in Interviews

- PL/pgSQL cloud-specific functions
- No compatibility test CI
- Assume identical performance

---

## Q015: Object Storage Abstraction SDK

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Integration |
| **Frequency** | Common |

### Question

Abstract S3 and Blob storage in application?

### Short Answer (30 seconds)

Interface `IObjectStorage` with put/get/presign; implementations AWSS3, AzureBlob; or MinIO API compatible.

### Detailed Answer (3–5 minutes)

**Architect:** Don't leak provider SDK types to domain. Test with local MinIO container.

**Cost:** Egress when moving between clouds — model carefully.

### Architecture Perspective

Abstraction trade-off worth for true multi-cloud storage.

### Follow-up Questions

1. **S3 API compatibility? — Many tools S3-compatible.**
2. **Multipart upload abstracted? — Large file API design.**

### Common Mistakes in Interviews

- Provider SDK in domain layer
- Abstraction without integration test
- Ignore egress on migration

---

## Q016: Message Bus Abstraction

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Integration |
| **Frequency** | Common |

### Question

Abstract SQS and Service Bus?

### Short Answer (30 seconds)

Port interface publish/subscribe; adapters per cloud; accept lowest common denominator or feature flags per provider.

### Detailed Answer (3–5 minutes)

**Architect:** Map semantics — visibility timeout vs lock duration. DLQ both sides.

**Alternative:** Kafka/MSK self-managed portable layer.

### Architecture Perspective

Messaging abstraction is hard — document gaps.

### Follow-up Questions

1. **CloudEvents standard? — Payload envelope portable.**
2. **Outbox still recommended? — Yes per cloud DB.**

### Common Mistakes in Interviews

- Lowest common denominator kills features
- No DLQ abstracted
- Sync HTTP instead async both

---

## Q017: OpenTelemetry Portable Observability

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Observability |
| **Frequency** | Common |

### Question

Single OTel instrumentation both clouds?

### Short Answer (30 seconds)

OTel SDK in app → exporter per env (X-Ray, Azure Monitor, vendor-neutral collector → Grafana).

### Detailed Answer (3–5 minutes)

**Architect:** One dashboard tool (Grafana/Datadog) aggregates both clouds — unified SLO view.

### Architecture Perspective

OTel is multi-cloud observability win.

### Follow-up Questions

1. **Collector agent per node? — DaemonSet pattern.**
2. **Trace correlation cross-cloud? — Propagate trace context.**

### Common Mistakes in Interviews

- Two proprietary agents
- Different metric names unnormalized
- No unified on-call

---

## Q018: CI/CD Multi-Cloud Pipelines

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DevOps |
| **Frequency** | Common |

### Question

GitHub Actions deploy to Azure and AWS?

### Short Answer (30 seconds)

OIDC federation both clouds — no secrets. Reusable workflows; environment protection rules prod.

### Detailed Answer (3–5 minutes)

**Architect:** Separate jobs parallel; shared build artifact container image; cloud-specific deploy job assumes role.

### Architecture Perspective

Pipeline design prevents credential sprawl.

### Follow-up Questions

1. **Matrix strategy? — Test both clouds PR.**
2. **Deployment environments? — Approval gates.**

### Common Mistakes in Interviews

- Long-lived keys GitHub secrets
- Deploy both one job tangled
- No rollback workflow

---

## Q019: Secret Management Both Clouds

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Security |
| **Frequency** | Common |

### Question

Unified secrets strategy Azure Key Vault + AWS Secrets Manager?

### Short Answer (30 seconds)

External Secrets Operator syncs to K8s; or HashiCorp Vault central; or duplicate secrets with rotation automation each cloud.

### Detailed Answer (3–5 minutes)

**Architect:** Prefer single Vault for multi-cloud central; accept operational cost. Document rotation ownership.

### Architecture Perspective

Secrets multiply in multi-cloud — plan early.

### Follow-up Questions

1. **Vault on K8s? — HA cluster required.**
2. **Never replicate secrets manual**

### Common Mistakes in Interviews

- Secrets in git encrypted sloppy
- Different secret names chaos
- No rotation schedule

---

## Q020: Compliance Mapping Azure/AWS

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Compliance |
| **Frequency** | Common |

### Question

Map SOC 2 controls across Azure and AWS?

### Short Answer (30 seconds)

Control matrix: logging (CloudTrail/Activity Log), encryption (KMS/Key Vault), access (IAM/Entra), network (FW/NSG).

### Detailed Answer (3–5 minutes)

**Architect:** Unified compliance dashboard both providers. Gap analysis per control not per checkbox vendor doc.

### Architecture Perspective

Compliance is mapped controls not logos.

### Follow-up Questions

1. **ISO 27001 similar mapping? — Same approach.**
2. **Shared audit evidence? — Central SIEM.**

### Common Mistakes in Interviews

- Separate compliance silos
- Assume certified so compliant
- No unified control matrix

---

## Q021: Acquisition Cloud Consolidation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Strategy |
| **Frequency** | Common |

### Question

Acquired company on different cloud — architect plan?

### Short Answer (30 seconds)

Assess workloads, contract commitments, skills, data gravity, regulatory, integration timeline — migrate vs federate vs leave.

### Detailed Answer (3–5 minutes)

**Architect:** 12-month consolidation roadmap with waves; don't force day-one unless M&A requires.

### Architecture Perspective

M&A cloud strategy is common principal scenario.

### Follow-up Questions

1. **Data export legal? — Contract and privacy review.**
2. **Retain both 2 years? — Often realistic interim.**

### Common Mistakes in Interviews

- Big-bang migration weekend
- Ignore acquired team's expertise
- No TCO comparison

---

## Q022: Negotiating Cloud Contracts

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | FinOps |
| **Frequency** | Occasional |

### Question

Enterprise Agreement vs EDP negotiation tips?

### Short Answer (30 seconds)

Commit based on steady baseline not peak; volume discounts; MAP migration funding; BYOL options; support tier included.

### Detailed Answer (3–5 minutes)

**Architect:** Provide engineering usage forecast to finance for negotiation — credible data.

### Architecture Perspective

Commercial awareness complements technical depth.

### Follow-up Questions

1. **CSP vs direct? — Partner discounts vs enterprise direct.**
2. **True-up risk? — Overcommit penalty.**

### Common Mistakes in Interviews

- Sign 3-year day one startup
- No engineering input commit
- Ignore support tier value

---

## Q023: Reserved Capacity Both Providers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

RI/SP on AWS and Reservations on Azure together?

### Short Answer (30 seconds)

Separate commitment per cloud — no cross-cloud credit. Track utilization dashboards each.

### Detailed Answer (3–5 minutes)

**Architect:** Commit only after 6+ months stable usage per cloud. Finance consolidated view both.

### Architecture Perspective

Dual cloud doubles commitment complexity.

### Follow-up Questions

1. **Flexibility exchange? — Provider-specific policies.**
2. **Savings plan unused? — Waste both sides.**

### Common Mistakes in Interviews

- Max commit both clouds speculative
- No utilization alerts
- Forgot Azure reservation expiry

---

## Q024: Carbon and Sustainability Compare

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Sustainability |
| **Frequency** | Occasional |

### Question

Compare cloud sustainability for workload placement?

### Short Answer (30 seconds)

AWS Customer Carbon Footprint Tool; Azure Emissions Impact Dashboard; region grid carbon intensity varies.

### Detailed Answer (3–5 minutes)

**Architect:** Sustainability pillar in WAF — batch jobs schedule low-carbon hours; Graviton/ARM efficiency.

### Architecture Perspective

Sustainability increasingly in RFPs.

### Follow-up Questions

1. **Carbon aware scheduling? — Emerging practice.**
2. **Marketing green without metrics**

### Common Mistakes in Interviews

- Ignore region carbon data
- Over-provisioned resources waste
- No sustainability review

---

## Q025: SaaS Multi-Tenant Multi-Cloud

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Architecture |
| **Frequency** | Common |

### Question

Offer SaaS on customer-choice cloud?

### Short Answer (30 seconds)

Single codebase, config per cloud deployment; tenant isolation; data residency per customer region/cloud.

### Detailed Answer (3–5 minutes)

**Architect:** Massive ops burden — justify premium pricing. Shared control plane; isolated data plane per cloud option.

### Architecture Perspective

Customer-choice cloud is hardest SaaS model.

### Follow-up Questions

1. **Terraform modules per cloud tenant? — Automation required.**
2. **Support SLA per cloud? — Different capabilities.**

### Common Mistakes in Interviews

- Underestimate ops 3x
- Same SLA all clouds unrealistic
- No automated tenant provisioning

---

## Q026: Edge Computing Both Clouds

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Edge |
| **Frequency** | Occasional |

### Question

Azure IoT Edge vs AWS Greengrass — architect view?

### Short Answer (30 seconds)

Edge run modules/lambda offline sync cloud — factory, retail, CDN PoP scenarios.

### Detailed Answer (3–5 minutes)

**Architect:** Edge when latency/regulations require local processing; manage fleet updates OTA securely.

### Architecture Perspective

Edge extends hybrid architecture.

### Follow-up Questions

1. **Azure Stack HCI? — On-prem Azure services.**
2. **Wavelength 5G edge? — Ultra-low latency mobile.**

### Common Mistakes in Interviews

- Edge without update strategy
- Same security model cloud assumed
- No offline mode design

---

## Q027: AI/ML Services Portability

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | AI |
| **Frequency** | Occasional |

### Question

Portable AI architecture across Azure OpenAI and Bedrock?

### Short Answer (30 seconds)

Abstract LLM provider interface; prompt templates versioned; evaluate vendor lock on fine-tuning and embeddings.

### Detailed Answer (3–5 minutes)

**Architect:** Open models on portable K8s GPU if lock-in concern high. Cost per token compare both.

### Architecture Perspective

AI portability is emerging architect concern.

### Follow-up Questions

1. **LangChain multi-provider? — Abstraction layer example.**
2. **Embedding model lock-in? — Re-index cost high.**

### Common Mistakes in Interviews

- Single vendor prompts hardcoded
- No fallback model outage
- PII to cloud AI no review

---

## Q028: Data Gravity Decision

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Strategy |
| **Frequency** | Very Common |

### Question

How does data gravity affect multi-cloud?

### Short Answer (30 seconds)

Large datasets expensive/slow to move — analytics stay near data; apps migrate to data not reverse.

### Detailed Answer (3–5 minutes)

**Architect:** Place compute in cloud holding primary data lake. Egress costs dominate TCO.

### Architecture Perspective

Data gravity is physics of cloud architecture.

### Follow-up Questions

1. **Snowball/Device transfer? — Bulk migration.**
2. **Replication not migration? — Hybrid access both.**

### Common Mistakes in Interviews

- Move 5PB monthly over internet
- Ignore egress in business case
- Analytics cloud different no plan

---

## Q029: Exit Strategy Documentation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Strategy |
| **Frequency** | Common |

### Question

Document cloud exit strategy without paranoia?

### Short Answer (30 seconds)

Export procedures, data formats, contract terms, alternative providers, transition timeline, acceptable lock-in list.

### Detailed Answer (3–5 minutes)

**Architect:** Exit doesn't mean leave — means negotiable posture and risk management.

### Architecture Perspective

Exit strategy is mature governance.

### Follow-up Questions

1. **Escrow for SaaS vendor? — Different but related.**
2. **Open formats mandate? — Parquet, Postgres dumps.**

### Common Mistakes in Interviews

- No data export tested
- 100% proprietary formats
- Exit strategy never reviewed

---

## Q030: Architecture Board Multi-Cloud Governance

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Governance |
| **Frequency** | Very Common |

### Question

Architecture review board for multi-cloud estate?

### Short Answer (30 seconds)

Standards: tagging, IaC, security baseline, approved services list per cloud, exception process, quarterly landscape review.

### Detailed Answer (3–5 minutes)

**Architect:** Board approves new cloud services and cross-cloud patterns — not every deploy.

**Output:** Decision log ADRs searchable.

### Architecture Perspective

Governance enables speed with guardrails.

### Follow-up Questions

1. **RFC process? — Lightweight proposal before adopt.**
2. **Tech radar? — Assess/Hold/Trial/Adopt per service.**

### Common Mistakes in Interviews

- No standards each team freestyle
- Board blocks without alternatives
- ADRs written never read

---
