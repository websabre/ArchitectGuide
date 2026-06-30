# Week 10 — Advanced Q&A

> Q071–Q100: Premium format (Week 1 quality).

---


## Q071: App Service Plan SKUs — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Compute |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling app service plan skus across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for App Service plans.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 10:** Azure Compute & App Services

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
App Service Plan SKUs must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full app service plan skus immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** App Service plans, Premium v3, Isolated, reserved capacity. Mitigation: Policy exemptions with expiry; game day validation.
Select app service sku based on load test, ha, and feature requirements.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating app service plan skus for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q072: App Service Plan SKUs — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Compute |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling app service plan skus across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for App Service plans.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 10:** Azure Compute & App Services

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
App Service Plan SKUs must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full app service plan skus immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** App Service plans, Premium v3, Isolated, reserved capacity. Mitigation: Policy exemptions with expiry; game day validation.
Select app service sku based on load test, ha, and feature requirements.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating app service plan skus for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q073: Deployment Slots Production — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | DevOps |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling deployment slots production across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for deployment slots.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 10:** Azure Compute & App Services

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Deployment Slots Production must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full deployment slots production immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** deployment slots, sticky settings, swap, rollback. Mitigation: Policy exemptions with expiry; game day validation.
Zero-downtime release with slots and backward-compatible migrations.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating deployment slots production for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q074: Deployment Slots Production — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | DevOps |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to deployment slots production without downtime?

### Short Answer (30 seconds)

Tier workloads, phase deployment slots production rollout, time-bound exemptions, golden-path IaC using deployment slots.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 10:** Azure Compute & App Services

**Scenario:** Migrating brownfield workloads to deployment slots production without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full deployment slots production on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** deployment slots, sticky settings, swap. Anchor: **deployment slots** + **sticky settings**.
Zero-downtime release with slots and backward-compatible migrations.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same deployment slots production strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q075: Azure Functions Plans — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Serverless |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to azure functions plans without downtime?

### Short Answer (30 seconds)

Tier workloads, phase azure functions plans rollout, time-bound exemptions, golden-path IaC using Consumption.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 10:** Azure Compute & App Services

**Scenario:** Migrating brownfield workloads to azure functions plans without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full azure functions plans on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** Consumption, Premium, Dedicated plans. Anchor: **Consumption** + **Premium**.
Choose functions plan based on latency, vnet, and traffic pattern.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same azure functions plans strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q076: Azure Functions Plans — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Serverless |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling azure functions plans across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for Consumption.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 10:** Azure Compute & App Services

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Azure Functions Plans must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full azure functions plans immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** Consumption, Premium, Dedicated plans, cold start. Mitigation: Policy exemptions with expiry; game day validation.
Choose functions plan based on latency, vnet, and traffic pattern.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating azure functions plans for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q077: Durable Functions Workflows — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Serverless |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling durable functions workflows across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for Durable Functions.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 10:** Azure Compute & App Services

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Durable Functions Workflows must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full durable functions workflows immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** Durable Functions, sagas, fan-out/fan-in, task hub. Mitigation: Policy exemptions with expiry; game day validation.
Stateful workflows with durable functions vs logic apps decision.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating durable functions workflows for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q078: Durable Functions Workflows — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Serverless |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling durable functions workflows across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for Durable Functions.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 10:** Azure Compute & App Services

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Durable Functions Workflows must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full durable functions workflows immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** Durable Functions, sagas, fan-out/fan-in, task hub. Mitigation: Policy exemptions with expiry; game day validation.
Stateful workflows with durable functions vs logic apps decision.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating durable functions workflows for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q079: AKS Architecture — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling aks architecture across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for AKS.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 10:** Azure Compute & App Services

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
AKS Architecture must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full aks architecture immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** AKS, node pools, system pool, cluster autoscaler. Mitigation: Policy exemptions with expiry; game day validation.
Aks cluster design with system/user node pools and upgrade strategy.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating aks architecture for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q080: AKS Architecture — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Kubernetes |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to aks architecture without downtime?

### Short Answer (30 seconds)

Tier workloads, phase aks architecture rollout, time-bound exemptions, golden-path IaC using AKS.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 10:** Azure Compute & App Services

**Scenario:** Migrating brownfield workloads to aks architecture without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full aks architecture on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** AKS, node pools, system pool. Anchor: **AKS** + **node pools**.
Aks cluster design with system/user node pools and upgrade strategy.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same aks architecture strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q081: Container Apps Design — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Containers |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to container apps design without downtime?

### Short Answer (30 seconds)

Tier workloads, phase container apps design rollout, time-bound exemptions, golden-path IaC using Container Apps.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 10:** Azure Compute & App Services

**Scenario:** Migrating brownfield workloads to container apps design without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full container apps design on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** Container Apps, KEDA, Dapr. Anchor: **Container Apps** + **KEDA**.
Container apps for microservices without full k8s ops burden.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same container apps design strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q082: Container Apps Design — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Containers |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling container apps design across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for Container Apps.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 10:** Azure Compute & App Services

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Container Apps Design must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full container apps design immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** Container Apps, KEDA, Dapr, revisions. Mitigation: Policy exemptions with expiry; game day validation.
Container apps for microservices without full k8s ops burden.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating container apps design for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q083: KEDA Event Scaling — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Scale |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling keda event scaling across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for KEDA.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 10:** Azure Compute & App Services

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
KEDA Event Scaling must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full keda event scaling immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** KEDA, ScaledObject, queue depth, scale-to-zero. Mitigation: Policy exemptions with expiry; game day validation.
Scale on business signals not cpu alone with keda.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating keda event scaling for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q084: KEDA Event Scaling — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Scale |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling keda event scaling across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for KEDA.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 10:** Azure Compute & App Services

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
KEDA Event Scaling must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full keda event scaling immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** KEDA, ScaledObject, queue depth, scale-to-zero. Mitigation: Policy exemptions with expiry; game day validation.
Scale on business signals not cpu alone with keda.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating keda event scaling for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q085: Azure Container Registry — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Containers |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling azure container registry across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for ACR.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 10:** Azure Compute & App Services

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Azure Container Registry must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full azure container registry immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** ACR, geo-replication, tasks, vulnerability scanning. Mitigation: Policy exemptions with expiry; game day validation.
Acr strategy with geo-replication and supply chain security.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating azure container registry for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q086: Azure Container Registry — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Containers |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to azure container registry without downtime?

### Short Answer (30 seconds)

Tier workloads, phase azure container registry rollout, time-bound exemptions, golden-path IaC using ACR.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 10:** Azure Compute & App Services

**Scenario:** Migrating brownfield workloads to azure container registry without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full azure container registry on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** ACR, geo-replication, tasks. Anchor: **ACR** + **geo-replication**.
Acr strategy with geo-replication and supply chain security.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same azure container registry strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q087: VM Scale Sets — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Compute |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to vm scale sets without downtime?

### Short Answer (30 seconds)

Tier workloads, phase vm scale sets rollout, time-bound exemptions, golden-path IaC using VMSS.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 10:** Azure Compute & App Services

**Scenario:** Migrating brownfield workloads to vm scale sets without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full vm scale sets on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** VMSS, autoscale, rolling upgrades. Anchor: **VMSS** + **autoscale**.
Vmss for stateful/stateless workloads needing iaas control.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same vm scale sets strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q088: VM Scale Sets — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Compute |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling vm scale sets across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for VMSS.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 10:** Azure Compute & App Services

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
VM Scale Sets must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full vm scale sets immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** VMSS, autoscale, rolling upgrades, spot instances. Mitigation: Policy exemptions with expiry; game day validation.
Vmss for stateful/stateless workloads needing iaas control.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating vm scale sets for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q089: Azure Arc Hybrid — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Hybrid |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling azure arc hybrid across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for Azure Arc.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 10:** Azure Compute & App Services

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Azure Arc Hybrid must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full azure arc hybrid immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** Azure Arc, Arc-enabled servers, Kubernetes, policy anywhere. Mitigation: Policy exemptions with expiry; game day validation.
Extend azure governance to hybrid and multi-cloud with arc.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating azure arc hybrid for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q090: Azure Arc Hybrid — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Hybrid |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling azure arc hybrid across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for Azure Arc.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 10:** Azure Compute & App Services

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Azure Arc Hybrid must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full azure arc hybrid immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** Azure Arc, Arc-enabled servers, Kubernetes, policy anywhere. Mitigation: Policy exemptions with expiry; game day validation.
Extend azure governance to hybrid and multi-cloud with arc.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating azure arc hybrid for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q091: Spot and Reserved Compute — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | FinOps |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling spot and reserved compute across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for spot VMs.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 10:** Azure Compute & App Services

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Spot and Reserved Compute must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full spot and reserved compute immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** spot VMs, reserved instances, savings plans, capacity reservation. Mitigation: Policy exemptions with expiry; game day validation.
Mix spot, on-demand, and reservations for cost and availability.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating spot and reserved compute for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q092: Web App for Containers — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Compute |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to web app for containers without downtime?

### Short Answer (30 seconds)

Tier workloads, phase web app for containers rollout, time-bound exemptions, golden-path IaC using Web App for Containers.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 10:** Azure Compute & App Services

**Scenario:** Migrating brownfield workloads to web app for containers without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full web app for containers on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** Web App for Containers, custom Docker, ACR integration. Anchor: **Web App for Containers** + **custom Docker**.
Containers on app service as middle ground before aks.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same web app for containers strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q093: GPU and HPC Compute — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Compute |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling gpu and hpc compute across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for NC-series VMs.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 10:** Azure Compute & App Services

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
GPU and HPC Compute must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full gpu and hpc compute immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** NC-series VMs, AKS GPU node pools, Azure Batch. Mitigation: Policy exemptions with expiry; game day validation.
Gpu compute for ml inference and batch hpc workloads.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating gpu and hpc compute for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q094: App Service VNet Integration — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling app service vnet integration across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for regional VNet integration.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 10:** Azure Compute & App Services

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
App Service VNet Integration must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full app service vnet integration immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** regional VNet integration, private endpoints, DNS. Mitigation: Policy exemptions with expiry; game day validation.
Secure app service to private sql and internal apis.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating app service vnet integration for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q095: Managed Identity Compute — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Identity |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to managed identity compute without downtime?

### Short Answer (30 seconds)

Tier workloads, phase managed identity compute rollout, time-bound exemptions, golden-path IaC using system/user-assigned MI.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 10:** Azure Compute & App Services

**Scenario:** Migrating brownfield workloads to managed identity compute without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full managed identity compute on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** system/user-assigned MI, Key Vault references, SQL Entra auth. Anchor: **system/user-assigned MI** + **Key Vault references**.
Eliminate secrets on compute with managed identity standard.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same managed identity compute strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q096: Multi-Region App Service — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Reliability |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling multi-region app service across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for Front Door.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 10:** Azure Compute & App Services

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Multi-Region App Service must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full multi-region app service immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** Front Door, Traffic Manager, geo-replication, Redis sessions. Mitigation: Policy exemptions with expiry; game day validation.
Multi-region app service with data consistency trade-offs.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating multi-region app service for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q097: Compute Migration Patterns — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Migration |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling compute migration patterns across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for App Service Migration Assistant.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 10:** Azure Compute & App Services

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Compute Migration Patterns must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full compute migration patterns immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** App Service Migration Assistant, containerize, re-platform. Mitigation: Policy exemptions with expiry; game day validation.
Migrate .net workloads to appropriate azure compute tier.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating compute migration patterns for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q098: Autoscale Design — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Scale |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to autoscale design without downtime?

### Short Answer (30 seconds)

Tier workloads, phase autoscale design rollout, time-bound exemptions, golden-path IaC using autoscale rules.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 10:** Azure Compute & App Services

**Scenario:** Migrating brownfield workloads to autoscale design without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full autoscale design on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** autoscale rules, cooldown, schedule scale. Anchor: **autoscale rules** + **cooldown**.
Autoscale policies from load test data not guesswork.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same autoscale design strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q099: Always On and Health Checks — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Operations |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling always on and health checks across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for Always On.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 10:** Azure Compute & App Services

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Always On and Health Checks must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full always on and health checks immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** Always On, health check path, availability tests. Mitigation: Policy exemptions with expiry; game day validation.
Production app service availability configuration.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating always on and health checks for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q100: Compute FinOps — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | FinOps |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling compute finops across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for right-size ASP.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 10:** Azure Compute & App Services

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Compute FinOps must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full compute finops immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** right-size ASP, shutdown dev, DevTest pricing, cost per transaction. Mitigation: Policy exemptions with expiry; game day validation.
Compute cost optimization without breaking sla.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating compute finops for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---
