# Week 10 — Intermediate Q&A

> Q031–Q070: Premium format (Week 1 quality).

---


## Q031: App Service Plan SKUs — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply App Service Plan SKUs using App Service plans in a Azure Compute & App Services architecture review?

### Short Answer (30 seconds)

Use App Service plans with Premium v3; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Select app service sku based on load test.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Context:** App Service Plan SKUs is core to Azure Solution Architect interviews covering App Service plans, Premium v3, Isolated, reserved capacity.

**Architect approach:**
1. Map business requirement to App Service plans — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Select app service sku based on load test, ha, and feature requirements.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect select App Service SKU based on load test, HA, and feature requirements — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to App Service plans?**
2. **What KPI proves app service plan skus adoption succeeded?**

### Common Mistakes in Interviews

- Listing App Service plans without explaining trade-offs
- No Policy or IaC enforcement for app service plan skus
- Skipping operational runbook for App Service plans

---

## Q032: App Service Plan SKUs — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Common |

### Question

**Intermediate:** Design production app service plan skus for a 10-subscription enterprise (Azure Compute & App Services).

### Short Answer (30 seconds)

Platform hosts shared App Service plans; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Design:** Multi-subscription estate with platform vs application separation.
Shared App Service plans and Premium v3 in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Select app service sku based on load test, ha, and feature requirements.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize app service plan skus.

### Follow-up Questions

1. **How do Policy exemptions work during app service plan skus migration?**
2. **What FinOps tag strategy supports app service plan skus chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for App Service plans testing
- Policies only at resource group — not MG

---

## Q033: Deployment Slots Production — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DevOps |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Deployment Slots Production using deployment slots in a Azure Compute & App Services architecture review?

### Short Answer (30 seconds)

Use deployment slots with sticky settings; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Zero-downtime release with slots and backward-compatible migrations.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Context:** Deployment Slots Production is core to Azure Solution Architect interviews covering deployment slots, sticky settings, swap, rollback.

**Architect approach:**
1. Map business requirement to deployment slots — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Zero-downtime release with slots and backward-compatible migrations.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect zero-downtime release with slots and backward-compatible migrations — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to deployment slots?**
2. **What KPI proves deployment slots production adoption succeeded?**

### Common Mistakes in Interviews

- Listing deployment slots without explaining trade-offs
- No Policy or IaC enforcement for deployment slots production
- Skipping operational runbook for deployment slots

---

## Q034: Deployment Slots Production — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DevOps |
| **Frequency** | Common |

### Question

**Intermediate:** Design production deployment slots production for a 10-subscription enterprise (Azure Compute & App Services).

### Short Answer (30 seconds)

Platform hosts shared deployment slots; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Design:** Multi-subscription estate with platform vs application separation.
Shared deployment slots and sticky settings in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Zero-downtime release with slots and backward-compatible migrations.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize deployment slots production.

### Follow-up Questions

1. **How do Policy exemptions work during deployment slots production migration?**
2. **What FinOps tag strategy supports deployment slots production chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for deployment slots testing
- Policies only at resource group — not MG

---

## Q035: Azure Functions Plans — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Serverless |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Azure Functions Plans using Consumption in a Azure Compute & App Services architecture review?

### Short Answer (30 seconds)

Use Consumption with Premium; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Choose functions plan based on latency.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Context:** Azure Functions Plans is core to Azure Solution Architect interviews covering Consumption, Premium, Dedicated plans, cold start.

**Architect approach:**
1. Map business requirement to Consumption — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Choose functions plan based on latency, vnet, and traffic pattern.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect choose Functions plan based on latency, VNet, and traffic pattern — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to Consumption?**
2. **What KPI proves azure functions plans adoption succeeded?**

### Common Mistakes in Interviews

- Listing Consumption without explaining trade-offs
- No Policy or IaC enforcement for azure functions plans
- Skipping operational runbook for Consumption

---

## Q036: Azure Functions Plans — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Serverless |
| **Frequency** | Common |

### Question

**Intermediate:** Design production azure functions plans for a 10-subscription enterprise (Azure Compute & App Services).

### Short Answer (30 seconds)

Platform hosts shared Consumption; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Design:** Multi-subscription estate with platform vs application separation.
Shared Consumption and Premium in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Choose functions plan based on latency, vnet, and traffic pattern.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize azure functions plans.

### Follow-up Questions

1. **How do Policy exemptions work during azure functions plans migration?**
2. **What FinOps tag strategy supports azure functions plans chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for Consumption testing
- Policies only at resource group — not MG

---

## Q037: Durable Functions Workflows — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Serverless |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Durable Functions Workflows using Durable Functions in a Azure Compute & App Services architecture review?

### Short Answer (30 seconds)

Use Durable Functions with sagas; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Stateful workflows with durable functions vs logic apps decision.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Context:** Durable Functions Workflows is core to Azure Solution Architect interviews covering Durable Functions, sagas, fan-out/fan-in, task hub.

**Architect approach:**
1. Map business requirement to Durable Functions — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Stateful workflows with durable functions vs logic apps decision.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect stateful workflows with Durable Functions vs Logic Apps decision — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to Durable Functions?**
2. **What KPI proves durable functions workflows adoption succeeded?**

### Common Mistakes in Interviews

- Listing Durable Functions without explaining trade-offs
- No Policy or IaC enforcement for durable functions workflows
- Skipping operational runbook for Durable Functions

---

## Q038: Durable Functions Workflows — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Serverless |
| **Frequency** | Common |

### Question

**Intermediate:** Design production durable functions workflows for a 10-subscription enterprise (Azure Compute & App Services).

### Short Answer (30 seconds)

Platform hosts shared Durable Functions; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Design:** Multi-subscription estate with platform vs application separation.
Shared Durable Functions and sagas in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Stateful workflows with durable functions vs logic apps decision.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize durable functions workflows.

### Follow-up Questions

1. **How do Policy exemptions work during durable functions workflows migration?**
2. **What FinOps tag strategy supports durable functions workflows chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for Durable Functions testing
- Policies only at resource group — not MG

---

## Q039: AKS Architecture — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply AKS Architecture using AKS in a Azure Compute & App Services architecture review?

### Short Answer (30 seconds)

Use AKS with node pools; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Aks cluster design with system/user node pools and upgrade strategy.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Context:** AKS Architecture is core to Azure Solution Architect interviews covering AKS, node pools, system pool, cluster autoscaler.

**Architect approach:**
1. Map business requirement to AKS — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Aks cluster design with system/user node pools and upgrade strategy.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect AKS cluster design with system/user node pools and upgrade strategy — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to AKS?**
2. **What KPI proves aks architecture adoption succeeded?**

### Common Mistakes in Interviews

- Listing AKS without explaining trade-offs
- No Policy or IaC enforcement for aks architecture
- Skipping operational runbook for AKS

---

## Q040: AKS Architecture — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Kubernetes |
| **Frequency** | Common |

### Question

**Intermediate:** Design production aks architecture for a 10-subscription enterprise (Azure Compute & App Services).

### Short Answer (30 seconds)

Platform hosts shared AKS; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Design:** Multi-subscription estate with platform vs application separation.
Shared AKS and node pools in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Aks cluster design with system/user node pools and upgrade strategy.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize aks architecture.

### Follow-up Questions

1. **How do Policy exemptions work during aks architecture migration?**
2. **What FinOps tag strategy supports aks architecture chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for AKS testing
- Policies only at resource group — not MG

---

## Q041: Container Apps Design — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Containers |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Container Apps Design using Container Apps in a Azure Compute & App Services architecture review?

### Short Answer (30 seconds)

Use Container Apps with KEDA; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Container apps for microservices without full k8s ops burden.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Context:** Container Apps Design is core to Azure Solution Architect interviews covering Container Apps, KEDA, Dapr, revisions.

**Architect approach:**
1. Map business requirement to Container Apps — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Container apps for microservices without full k8s ops burden.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect Container Apps for microservices without full K8s ops burden — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to Container Apps?**
2. **What KPI proves container apps design adoption succeeded?**

### Common Mistakes in Interviews

- Listing Container Apps without explaining trade-offs
- No Policy or IaC enforcement for container apps design
- Skipping operational runbook for Container Apps

---

## Q042: Container Apps Design — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Containers |
| **Frequency** | Common |

### Question

**Intermediate:** Design production container apps design for a 10-subscription enterprise (Azure Compute & App Services).

### Short Answer (30 seconds)

Platform hosts shared Container Apps; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Design:** Multi-subscription estate with platform vs application separation.
Shared Container Apps and KEDA in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Container apps for microservices without full k8s ops burden.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize container apps design.

### Follow-up Questions

1. **How do Policy exemptions work during container apps design migration?**
2. **What FinOps tag strategy supports container apps design chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for Container Apps testing
- Policies only at resource group — not MG

---

## Q043: KEDA Event Scaling — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Scale |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply KEDA Event Scaling using KEDA in a Azure Compute & App Services architecture review?

### Short Answer (30 seconds)

Use KEDA with ScaledObject; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Scale on business signals not cpu alone with keda.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Context:** KEDA Event Scaling is core to Azure Solution Architect interviews covering KEDA, ScaledObject, queue depth, scale-to-zero.

**Architect approach:**
1. Map business requirement to KEDA — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Scale on business signals not cpu alone with keda.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect scale on business signals not CPU alone with KEDA — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to KEDA?**
2. **What KPI proves keda event scaling adoption succeeded?**

### Common Mistakes in Interviews

- Listing KEDA without explaining trade-offs
- No Policy or IaC enforcement for keda event scaling
- Skipping operational runbook for KEDA

---

## Q044: KEDA Event Scaling — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Scale |
| **Frequency** | Common |

### Question

**Intermediate:** Design production keda event scaling for a 10-subscription enterprise (Azure Compute & App Services).

### Short Answer (30 seconds)

Platform hosts shared KEDA; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Design:** Multi-subscription estate with platform vs application separation.
Shared KEDA and ScaledObject in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Scale on business signals not cpu alone with keda.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize keda event scaling.

### Follow-up Questions

1. **How do Policy exemptions work during keda event scaling migration?**
2. **What FinOps tag strategy supports keda event scaling chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for KEDA testing
- Policies only at resource group — not MG

---

## Q045: Azure Container Registry — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Containers |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Azure Container Registry using ACR in a Azure Compute & App Services architecture review?

### Short Answer (30 seconds)

Use ACR with geo-replication; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Acr strategy with geo-replication and supply chain security.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Context:** Azure Container Registry is core to Azure Solution Architect interviews covering ACR, geo-replication, tasks, vulnerability scanning.

**Architect approach:**
1. Map business requirement to ACR — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Acr strategy with geo-replication and supply chain security.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect ACR strategy with geo-replication and supply chain security — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to ACR?**
2. **What KPI proves azure container registry adoption succeeded?**

### Common Mistakes in Interviews

- Listing ACR without explaining trade-offs
- No Policy or IaC enforcement for azure container registry
- Skipping operational runbook for ACR

---

## Q046: Azure Container Registry — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Containers |
| **Frequency** | Common |

### Question

**Intermediate:** Design production azure container registry for a 10-subscription enterprise (Azure Compute & App Services).

### Short Answer (30 seconds)

Platform hosts shared ACR; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Design:** Multi-subscription estate with platform vs application separation.
Shared ACR and geo-replication in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Acr strategy with geo-replication and supply chain security.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize azure container registry.

### Follow-up Questions

1. **How do Policy exemptions work during azure container registry migration?**
2. **What FinOps tag strategy supports azure container registry chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for ACR testing
- Policies only at resource group — not MG

---

## Q047: VM Scale Sets — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply VM Scale Sets using VMSS in a Azure Compute & App Services architecture review?

### Short Answer (30 seconds)

Use VMSS with autoscale; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Vmss for stateful/stateless workloads needing iaas control.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Context:** VM Scale Sets is core to Azure Solution Architect interviews covering VMSS, autoscale, rolling upgrades, spot instances.

**Architect approach:**
1. Map business requirement to VMSS — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Vmss for stateful/stateless workloads needing iaas control.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect VMSS for stateful/stateless workloads needing IaaS control — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to VMSS?**
2. **What KPI proves vm scale sets adoption succeeded?**

### Common Mistakes in Interviews

- Listing VMSS without explaining trade-offs
- No Policy or IaC enforcement for vm scale sets
- Skipping operational runbook for VMSS

---

## Q048: VM Scale Sets — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Common |

### Question

**Intermediate:** Design production vm scale sets for a 10-subscription enterprise (Azure Compute & App Services).

### Short Answer (30 seconds)

Platform hosts shared VMSS; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Design:** Multi-subscription estate with platform vs application separation.
Shared VMSS and autoscale in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Vmss for stateful/stateless workloads needing iaas control.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize vm scale sets.

### Follow-up Questions

1. **How do Policy exemptions work during vm scale sets migration?**
2. **What FinOps tag strategy supports vm scale sets chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for VMSS testing
- Policies only at resource group — not MG

---

## Q049: Azure Arc Hybrid — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hybrid |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Azure Arc Hybrid using Azure Arc in a Azure Compute & App Services architecture review?

### Short Answer (30 seconds)

Use Azure Arc with Arc-enabled servers; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Extend azure governance to hybrid and multi-cloud with arc.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Context:** Azure Arc Hybrid is core to Azure Solution Architect interviews covering Azure Arc, Arc-enabled servers, Kubernetes, policy anywhere.

**Architect approach:**
1. Map business requirement to Azure Arc — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Extend azure governance to hybrid and multi-cloud with arc.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect extend Azure governance to hybrid and multi-cloud with Arc — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to Azure Arc?**
2. **What KPI proves azure arc hybrid adoption succeeded?**

### Common Mistakes in Interviews

- Listing Azure Arc without explaining trade-offs
- No Policy or IaC enforcement for azure arc hybrid
- Skipping operational runbook for Azure Arc

---

## Q050: Azure Arc Hybrid — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Hybrid |
| **Frequency** | Common |

### Question

**Intermediate:** Design production azure arc hybrid for a 10-subscription enterprise (Azure Compute & App Services).

### Short Answer (30 seconds)

Platform hosts shared Azure Arc; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Design:** Multi-subscription estate with platform vs application separation.
Shared Azure Arc and Arc-enabled servers in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Extend azure governance to hybrid and multi-cloud with arc.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize azure arc hybrid.

### Follow-up Questions

1. **How do Policy exemptions work during azure arc hybrid migration?**
2. **What FinOps tag strategy supports azure arc hybrid chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for Azure Arc testing
- Policies only at resource group — not MG

---

## Q051: Spot and Reserved Compute — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Spot and Reserved Compute using spot VMs in a Azure Compute & App Services architecture review?

### Short Answer (30 seconds)

Use spot VMs with reserved instances; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Mix spot.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Context:** Spot and Reserved Compute is core to Azure Solution Architect interviews covering spot VMs, reserved instances, savings plans, capacity reservation.

**Architect approach:**
1. Map business requirement to spot VMs — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Mix spot, on-demand, and reservations for cost and availability.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect mix spot, on-demand, and reservations for cost and availability — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to spot VMs?**
2. **What KPI proves spot and reserved compute adoption succeeded?**

### Common Mistakes in Interviews

- Listing spot VMs without explaining trade-offs
- No Policy or IaC enforcement for spot and reserved compute
- Skipping operational runbook for spot VMs

---

## Q052: Spot and Reserved Compute — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

**Intermediate:** Design production spot and reserved compute for a 10-subscription enterprise (Azure Compute & App Services).

### Short Answer (30 seconds)

Platform hosts shared spot VMs; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Design:** Multi-subscription estate with platform vs application separation.
Shared spot VMs and reserved instances in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Mix spot, on-demand, and reservations for cost and availability.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize spot and reserved compute.

### Follow-up Questions

1. **How do Policy exemptions work during spot and reserved compute migration?**
2. **What FinOps tag strategy supports spot and reserved compute chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for spot VMs testing
- Policies only at resource group — not MG

---

## Q053: Web App for Containers — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Web App for Containers using Web App for Containers in a Azure Compute & App Services architecture review?

### Short Answer (30 seconds)

Use Web App for Containers with custom Docker; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Containers on app service as middle ground before aks.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Context:** Web App for Containers is core to Azure Solution Architect interviews covering Web App for Containers, custom Docker, ACR integration.

**Architect approach:**
1. Map business requirement to Web App for Containers — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Containers on app service as middle ground before aks.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect containers on App Service as middle ground before AKS — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to Web App for Containers?**
2. **What KPI proves web app for containers adoption succeeded?**

### Common Mistakes in Interviews

- Listing Web App for Containers without explaining trade-offs
- No Policy or IaC enforcement for web app for containers
- Skipping operational runbook for Web App for Containers

---

## Q054: Web App for Containers — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Common |

### Question

**Intermediate:** Design production web app for containers for a 10-subscription enterprise (Azure Compute & App Services).

### Short Answer (30 seconds)

Platform hosts shared Web App for Containers; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Design:** Multi-subscription estate with platform vs application separation.
Shared Web App for Containers and custom Docker in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Containers on app service as middle ground before aks.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize web app for containers.

### Follow-up Questions

1. **How do Policy exemptions work during web app for containers migration?**
2. **What FinOps tag strategy supports web app for containers chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for Web App for Containers testing
- Policies only at resource group — not MG

---

## Q055: GPU and HPC Compute — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply GPU and HPC Compute using NC-series VMs in a Azure Compute & App Services architecture review?

### Short Answer (30 seconds)

Use NC-series VMs with AKS GPU node pools; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Gpu compute for ml inference and batch hpc workloads.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Context:** GPU and HPC Compute is core to Azure Solution Architect interviews covering NC-series VMs, AKS GPU node pools, Azure Batch.

**Architect approach:**
1. Map business requirement to NC-series VMs — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Gpu compute for ml inference and batch hpc workloads.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect GPU compute for ML inference and batch HPC workloads — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to NC-series VMs?**
2. **What KPI proves gpu and hpc compute adoption succeeded?**

### Common Mistakes in Interviews

- Listing NC-series VMs without explaining trade-offs
- No Policy or IaC enforcement for gpu and hpc compute
- Skipping operational runbook for NC-series VMs

---

## Q056: GPU and HPC Compute — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compute |
| **Frequency** | Common |

### Question

**Intermediate:** Design production gpu and hpc compute for a 10-subscription enterprise (Azure Compute & App Services).

### Short Answer (30 seconds)

Platform hosts shared NC-series VMs; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Design:** Multi-subscription estate with platform vs application separation.
Shared NC-series VMs and AKS GPU node pools in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Gpu compute for ml inference and batch hpc workloads.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize gpu and hpc compute.

### Follow-up Questions

1. **How do Policy exemptions work during gpu and hpc compute migration?**
2. **What FinOps tag strategy supports gpu and hpc compute chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for NC-series VMs testing
- Policies only at resource group — not MG

---

## Q057: App Service VNet Integration — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply App Service VNet Integration using regional VNet integration in a Azure Compute & App Services architecture review?

### Short Answer (30 seconds)

Use regional VNet integration with private endpoints; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Secure app service to private sql and internal apis.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Context:** App Service VNet Integration is core to Azure Solution Architect interviews covering regional VNet integration, private endpoints, DNS.

**Architect approach:**
1. Map business requirement to regional VNet integration — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Secure app service to private sql and internal apis.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect secure App Service to private SQL and internal APIs — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to regional VNet integration?**
2. **What KPI proves app service vnet integration adoption succeeded?**

### Common Mistakes in Interviews

- Listing regional VNet integration without explaining trade-offs
- No Policy or IaC enforcement for app service vnet integration
- Skipping operational runbook for regional VNet integration

---

## Q058: App Service VNet Integration — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

**Intermediate:** Design production app service vnet integration for a 10-subscription enterprise (Azure Compute & App Services).

### Short Answer (30 seconds)

Platform hosts shared regional VNet integration; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Design:** Multi-subscription estate with platform vs application separation.
Shared regional VNet integration and private endpoints in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Secure app service to private sql and internal apis.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize app service vnet integration.

### Follow-up Questions

1. **How do Policy exemptions work during app service vnet integration migration?**
2. **What FinOps tag strategy supports app service vnet integration chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for regional VNet integration testing
- Policies only at resource group — not MG

---

## Q059: Managed Identity Compute — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Managed Identity Compute using system/user-assigned MI in a Azure Compute & App Services architecture review?

### Short Answer (30 seconds)

Use system/user-assigned MI with Key Vault references; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Eliminate secrets on compute with managed identity standard.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Context:** Managed Identity Compute is core to Azure Solution Architect interviews covering system/user-assigned MI, Key Vault references, SQL Entra auth.

**Architect approach:**
1. Map business requirement to system/user-assigned MI — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Eliminate secrets on compute with managed identity standard.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect eliminate secrets on compute with managed identity standard — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to system/user-assigned MI?**
2. **What KPI proves managed identity compute adoption succeeded?**

### Common Mistakes in Interviews

- Listing system/user-assigned MI without explaining trade-offs
- No Policy or IaC enforcement for managed identity compute
- Skipping operational runbook for system/user-assigned MI

---

## Q060: Managed Identity Compute — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Common |

### Question

**Intermediate:** Design production managed identity compute for a 10-subscription enterprise (Azure Compute & App Services).

### Short Answer (30 seconds)

Platform hosts shared system/user-assigned MI; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Design:** Multi-subscription estate with platform vs application separation.
Shared system/user-assigned MI and Key Vault references in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Eliminate secrets on compute with managed identity standard.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize managed identity compute.

### Follow-up Questions

1. **How do Policy exemptions work during managed identity compute migration?**
2. **What FinOps tag strategy supports managed identity compute chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for system/user-assigned MI testing
- Policies only at resource group — not MG

---

## Q061: Multi-Region App Service — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reliability |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Multi-Region App Service using Front Door in a Azure Compute & App Services architecture review?

### Short Answer (30 seconds)

Use Front Door with Traffic Manager; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Multi-region app service with data consistency trade-offs.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Context:** Multi-Region App Service is core to Azure Solution Architect interviews covering Front Door, Traffic Manager, geo-replication, Redis sessions.

**Architect approach:**
1. Map business requirement to Front Door — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Multi-region app service with data consistency trade-offs.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect multi-region App Service with data consistency trade-offs — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to Front Door?**
2. **What KPI proves multi-region app service adoption succeeded?**

### Common Mistakes in Interviews

- Listing Front Door without explaining trade-offs
- No Policy or IaC enforcement for multi-region app service
- Skipping operational runbook for Front Door

---

## Q062: Multi-Region App Service — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reliability |
| **Frequency** | Common |

### Question

**Intermediate:** Design production multi-region app service for a 10-subscription enterprise (Azure Compute & App Services).

### Short Answer (30 seconds)

Platform hosts shared Front Door; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Design:** Multi-subscription estate with platform vs application separation.
Shared Front Door and Traffic Manager in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Multi-region app service with data consistency trade-offs.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize multi-region app service.

### Follow-up Questions

1. **How do Policy exemptions work during multi-region app service migration?**
2. **What FinOps tag strategy supports multi-region app service chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for Front Door testing
- Policies only at resource group — not MG

---

## Q063: Compute Migration Patterns — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Migration |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Compute Migration Patterns using App Service Migration Assistant in a Azure Compute & App Services architecture review?

### Short Answer (30 seconds)

Use App Service Migration Assistant with containerize; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Migrate .net workloads to appropriate azure compute tier.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Context:** Compute Migration Patterns is core to Azure Solution Architect interviews covering App Service Migration Assistant, containerize, re-platform.

**Architect approach:**
1. Map business requirement to App Service Migration Assistant — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Migrate .net workloads to appropriate azure compute tier.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect migrate .NET workloads to appropriate Azure compute tier — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to App Service Migration Assistant?**
2. **What KPI proves compute migration patterns adoption succeeded?**

### Common Mistakes in Interviews

- Listing App Service Migration Assistant without explaining trade-offs
- No Policy or IaC enforcement for compute migration patterns
- Skipping operational runbook for App Service Migration Assistant

---

## Q064: Compute Migration Patterns — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Migration |
| **Frequency** | Common |

### Question

**Intermediate:** Design production compute migration patterns for a 10-subscription enterprise (Azure Compute & App Services).

### Short Answer (30 seconds)

Platform hosts shared App Service Migration Assistant; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Design:** Multi-subscription estate with platform vs application separation.
Shared App Service Migration Assistant and containerize in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Migrate .net workloads to appropriate azure compute tier.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize compute migration patterns.

### Follow-up Questions

1. **How do Policy exemptions work during compute migration patterns migration?**
2. **What FinOps tag strategy supports compute migration patterns chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for App Service Migration Assistant testing
- Policies only at resource group — not MG

---

## Q065: Autoscale Design — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Scale |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Autoscale Design using autoscale rules in a Azure Compute & App Services architecture review?

### Short Answer (30 seconds)

Use autoscale rules with cooldown; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Autoscale policies from load test data not guesswork.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Context:** Autoscale Design is core to Azure Solution Architect interviews covering autoscale rules, cooldown, schedule scale, custom metrics.

**Architect approach:**
1. Map business requirement to autoscale rules — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Autoscale policies from load test data not guesswork.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect autoscale policies from load test data not guesswork — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to autoscale rules?**
2. **What KPI proves autoscale design adoption succeeded?**

### Common Mistakes in Interviews

- Listing autoscale rules without explaining trade-offs
- No Policy or IaC enforcement for autoscale design
- Skipping operational runbook for autoscale rules

---

## Q066: Autoscale Design — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Scale |
| **Frequency** | Common |

### Question

**Intermediate:** Design production autoscale design for a 10-subscription enterprise (Azure Compute & App Services).

### Short Answer (30 seconds)

Platform hosts shared autoscale rules; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Design:** Multi-subscription estate with platform vs application separation.
Shared autoscale rules and cooldown in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Autoscale policies from load test data not guesswork.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize autoscale design.

### Follow-up Questions

1. **How do Policy exemptions work during autoscale design migration?**
2. **What FinOps tag strategy supports autoscale design chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for autoscale rules testing
- Policies only at resource group — not MG

---

## Q067: Always On and Health Checks — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Always On and Health Checks using Always On in a Azure Compute & App Services architecture review?

### Short Answer (30 seconds)

Use Always On with health check path; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Production app service availability configuration.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Context:** Always On and Health Checks is core to Azure Solution Architect interviews covering Always On, health check path, availability tests.

**Architect approach:**
1. Map business requirement to Always On — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Production app service availability configuration.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect production App Service availability configuration — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to Always On?**
2. **What KPI proves always on and health checks adoption succeeded?**

### Common Mistakes in Interviews

- Listing Always On without explaining trade-offs
- No Policy or IaC enforcement for always on and health checks
- Skipping operational runbook for Always On

---

## Q068: Always On and Health Checks — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Common |

### Question

**Intermediate:** Design production always on and health checks for a 10-subscription enterprise (Azure Compute & App Services).

### Short Answer (30 seconds)

Platform hosts shared Always On; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Design:** Multi-subscription estate with platform vs application separation.
Shared Always On and health check path in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Production app service availability configuration.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize always on and health checks.

### Follow-up Questions

1. **How do Policy exemptions work during always on and health checks migration?**
2. **What FinOps tag strategy supports always on and health checks chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for Always On testing
- Policies only at resource group — not MG

---

## Q069: Compute FinOps — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Compute FinOps using right-size ASP in a Azure Compute & App Services architecture review?

### Short Answer (30 seconds)

Use right-size ASP with shutdown dev; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Compute cost optimization without breaking sla.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Context:** Compute FinOps is core to Azure Solution Architect interviews covering right-size ASP, shutdown dev, DevTest pricing, cost per transaction.

**Architect approach:**
1. Map business requirement to right-size ASP — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Compute cost optimization without breaking sla.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect compute cost optimization without breaking SLA — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to right-size ASP?**
2. **What KPI proves compute finops adoption succeeded?**

### Common Mistakes in Interviews

- Listing right-size ASP without explaining trade-offs
- No Policy or IaC enforcement for compute finops
- Skipping operational runbook for right-size ASP

---

## Q070: Compute FinOps — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

**Intermediate:** Design production compute finops for a 10-subscription enterprise (Azure Compute & App Services).

### Short Answer (30 seconds)

Platform hosts shared right-size ASP; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 10:** Azure Compute & App Services

**Design:** Multi-subscription estate with platform vs application separation.
Shared right-size ASP and shutdown dev in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Compute cost optimization without breaking sla.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize compute finops.

### Follow-up Questions

1. **How do Policy exemptions work during compute finops migration?**
2. **What FinOps tag strategy supports compute finops chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for right-size ASP testing
- Policies only at resource group — not MG

---
