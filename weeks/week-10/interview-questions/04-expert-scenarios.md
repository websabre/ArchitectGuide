# Week 10 — Expert Scenario Q&A

> Q101–Q120: Premium format (Week 1 quality).

---


## Q101: App Service Plan SKUs — Expert Incident Response

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in app service plan skus. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via App Service plans → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 10:** Azure Compute & App Services

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to App Service Plan SKUs gap; Resource Graph inventory of App Service plans, Premium v3, Isolated, reserved capacity.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on App Service plans.
Select app service sku based on load test, ha, and feature requirements. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for app service plan skus?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q102: Deployment Slots Production — Expert Audit Remediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in deployment slots production. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via deployment slots → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 10:** Azure Compute & App Services

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Deployment Slots Production gap; Resource Graph inventory of deployment slots, sticky settings, swap, rollback.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on deployment slots.
Zero-downtime release with slots and backward-compatible migrations. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for deployment slots production?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q103: Azure Functions Plans — Expert Cost Redesign

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in azure functions plans. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via Consumption → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 10:** Azure Compute & App Services

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Azure Functions Plans gap; Resource Graph inventory of Consumption, Premium, Dedicated plans, cold start.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on Consumption.
Choose functions plan based on latency, vnet, and traffic pattern. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for azure functions plans?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q104: Durable Functions Workflows — Expert Standards Mediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in durable functions workflows. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via Durable Functions → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 10:** Azure Compute & App Services

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Durable Functions Workflows gap; Resource Graph inventory of Durable Functions, sagas, fan-out/fan-in, task hub.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on Durable Functions.
Stateful workflows with durable functions vs logic apps decision. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for durable functions workflows?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q105: AKS Architecture — Expert Incident Response

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in aks architecture. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via AKS → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 10:** Azure Compute & App Services

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to AKS Architecture gap; Resource Graph inventory of AKS, node pools, system pool, cluster autoscaler.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on AKS.
Aks cluster design with system/user node pools and upgrade strategy. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for aks architecture?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q106: Container Apps Design — Expert Audit Remediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in container apps design. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via Container Apps → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 10:** Azure Compute & App Services

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Container Apps Design gap; Resource Graph inventory of Container Apps, KEDA, Dapr, revisions.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on Container Apps.
Container apps for microservices without full k8s ops burden. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for container apps design?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q107: KEDA Event Scaling — Expert Cost Redesign

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in keda event scaling. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via KEDA → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 10:** Azure Compute & App Services

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to KEDA Event Scaling gap; Resource Graph inventory of KEDA, ScaledObject, queue depth, scale-to-zero.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on KEDA.
Scale on business signals not cpu alone with keda. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for keda event scaling?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q108: Azure Container Registry — Expert Standards Mediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in azure container registry. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via ACR → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 10:** Azure Compute & App Services

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Azure Container Registry gap; Resource Graph inventory of ACR, geo-replication, tasks, vulnerability scanning.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on ACR.
Acr strategy with geo-replication and supply chain security. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for azure container registry?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q109: VM Scale Sets — Expert Incident Response

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in vm scale sets. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via VMSS → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 10:** Azure Compute & App Services

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to VM Scale Sets gap; Resource Graph inventory of VMSS, autoscale, rolling upgrades, spot instances.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on VMSS.
Vmss for stateful/stateless workloads needing iaas control. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for vm scale sets?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q110: Azure Arc Hybrid — Expert Audit Remediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in azure arc hybrid. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via Azure Arc → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 10:** Azure Compute & App Services

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Azure Arc Hybrid gap; Resource Graph inventory of Azure Arc, Arc-enabled servers, Kubernetes, policy anywhere.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on Azure Arc.
Extend azure governance to hybrid and multi-cloud with arc. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for azure arc hybrid?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q111: Spot and Reserved Compute — Expert Cost Redesign

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in spot and reserved compute. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via spot VMs → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 10:** Azure Compute & App Services

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Spot and Reserved Compute gap; Resource Graph inventory of spot VMs, reserved instances, savings plans, capacity reservation.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on spot VMs.
Mix spot, on-demand, and reservations for cost and availability. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for spot and reserved compute?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q112: Web App for Containers — Expert Standards Mediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in web app for containers. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via Web App for Containers → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 10:** Azure Compute & App Services

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Web App for Containers gap; Resource Graph inventory of Web App for Containers, custom Docker, ACR integration.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on Web App for Containers.
Containers on app service as middle ground before aks. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for web app for containers?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q113: GPU and HPC Compute — Expert Incident Response

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in gpu and hpc compute. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via NC-series VMs → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 10:** Azure Compute & App Services

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to GPU and HPC Compute gap; Resource Graph inventory of NC-series VMs, AKS GPU node pools, Azure Batch.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on NC-series VMs.
Gpu compute for ml inference and batch hpc workloads. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for gpu and hpc compute?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q114: App Service VNet Integration — Expert Audit Remediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in app service vnet integration. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via regional VNet integration → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 10:** Azure Compute & App Services

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to App Service VNet Integration gap; Resource Graph inventory of regional VNet integration, private endpoints, DNS.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on regional VNet integration.
Secure app service to private sql and internal apis. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for app service vnet integration?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q115: Managed Identity Compute — Expert Cost Redesign

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in managed identity compute. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via system/user-assigned MI → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 10:** Azure Compute & App Services

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Managed Identity Compute gap; Resource Graph inventory of system/user-assigned MI, Key Vault references, SQL Entra auth.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on system/user-assigned MI.
Eliminate secrets on compute with managed identity standard. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for managed identity compute?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q116: Multi-Region App Service — Expert Standards Mediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in multi-region app service. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via Front Door → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 10:** Azure Compute & App Services

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Multi-Region App Service gap; Resource Graph inventory of Front Door, Traffic Manager, geo-replication, Redis sessions.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on Front Door.
Multi-region app service with data consistency trade-offs. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for multi-region app service?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q117: Compute Migration Patterns — Expert Incident Response

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in compute migration patterns. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via App Service Migration Assistant → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 10:** Azure Compute & App Services

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Compute Migration Patterns gap; Resource Graph inventory of App Service Migration Assistant, containerize, re-platform.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on App Service Migration Assistant.
Migrate .net workloads to appropriate azure compute tier. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for compute migration patterns?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q118: Autoscale Design — Expert Audit Remediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in autoscale design. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via autoscale rules → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 10:** Azure Compute & App Services

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Autoscale Design gap; Resource Graph inventory of autoscale rules, cooldown, schedule scale, custom metrics.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on autoscale rules.
Autoscale policies from load test data not guesswork. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for autoscale design?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q119: Always On and Health Checks — Expert Cost Redesign

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in always on and health checks. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via Always On → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 10:** Azure Compute & App Services

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Always On and Health Checks gap; Resource Graph inventory of Always On, health check path, availability tests.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on Always On.
Production app service availability configuration. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for always on and health checks?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q120: Compute FinOps — Expert Standards Mediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in compute finops. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via right-size ASP → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 10:** Azure Compute & App Services

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Compute FinOps gap; Resource Graph inventory of right-size ASP, shutdown dev, DevTest pricing, cost per transaction.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on right-size ASP.
Compute cost optimization without breaking sla. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for compute finops?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---
