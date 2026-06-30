# Week 16 — Intermediate Q&A

> Q031–Q070: Premium format (Week 1 quality).

---


## Q031: Production WAF Review — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Production WAF Review using all WAF pillars in a Azure Production Capstone architecture review?

### Short Answer (30 seconds)

Use all WAF pillars with review checklist; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Lead production architecture review using waf scorecard.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Context:** Production WAF Review is core to Azure Solution Architect interviews covering all WAF pillars, review checklist, ranked findings.

**Architect approach:**
1. Map business requirement to all WAF pillars — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Lead production architecture review using waf scorecard.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect lead production architecture review using WAF scorecard — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to all WAF pillars?**
2. **What KPI proves production waf review adoption succeeded?**

### Common Mistakes in Interviews

- Listing all WAF pillars without explaining trade-offs
- No Policy or IaC enforcement for production waf review
- Skipping operational runbook for all WAF pillars

---

## Q032: Production WAF Review — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Capstone |
| **Frequency** | Common |

### Question

**Intermediate:** Design production production waf review for a 10-subscription enterprise (Azure Production Capstone).

### Short Answer (30 seconds)

Platform hosts shared all WAF pillars; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Design:** Multi-subscription estate with platform vs application separation.
Shared all WAF pillars and review checklist in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Lead production architecture review using waf scorecard.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize production waf review.

### Follow-up Questions

1. **How do Policy exemptions work during production waf review migration?**
2. **What FinOps tag strategy supports production waf review chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for all WAF pillars testing
- Policies only at resource group — not MG

---

## Q033: Composite SLA Calculation — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reliability |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Composite SLA Calculation using Front Door in a Azure Production Capstone architecture review?

### Short Answer (30 seconds)

Use Front Door with App Service; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Composite sla math and weakest-link mitigation.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Context:** Composite SLA Calculation is core to Azure Solution Architect interviews covering Front Door, App Service, SQL SLA multiplication.

**Architect approach:**
1. Map business requirement to Front Door — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Composite sla math and weakest-link mitigation.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect composite SLA math and weakest-link mitigation — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to Front Door?**
2. **What KPI proves composite sla calculation adoption succeeded?**

### Common Mistakes in Interviews

- Listing Front Door without explaining trade-offs
- No Policy or IaC enforcement for composite sla calculation
- Skipping operational runbook for Front Door

---

## Q034: Composite SLA Calculation — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reliability |
| **Frequency** | Common |

### Question

**Intermediate:** Design production composite sla calculation for a 10-subscription enterprise (Azure Production Capstone).

### Short Answer (30 seconds)

Platform hosts shared Front Door; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Design:** Multi-subscription estate with platform vs application separation.
Shared Front Door and App Service in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Composite sla math and weakest-link mitigation.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize composite sla calculation.

### Follow-up Questions

1. **How do Policy exemptions work during composite sla calculation migration?**
2. **What FinOps tag strategy supports composite sla calculation chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for Front Door testing
- Policies only at resource group — not MG

---

## Q035: DR Runbook and Game Day — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DR |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply DR Runbook and Game Day using failover group runbook in a Azure Production Capstone architecture review?

### Short Answer (30 seconds)

Use failover group runbook with RTO/RPO validation; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Tested dr runbook with quarterly game days.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Context:** DR Runbook and Game Day is core to Azure Solution Architect interviews covering failover group runbook, RTO/RPO validation, communication.

**Architect approach:**
1. Map business requirement to failover group runbook — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Tested dr runbook with quarterly game days.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect tested DR runbook with quarterly game days — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to failover group runbook?**
2. **What KPI proves dr runbook and game day adoption succeeded?**

### Common Mistakes in Interviews

- Listing failover group runbook without explaining trade-offs
- No Policy or IaC enforcement for dr runbook and game day
- Skipping operational runbook for failover group runbook

---

## Q036: DR Runbook and Game Day — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DR |
| **Frequency** | Common |

### Question

**Intermediate:** Design production dr runbook and game day for a 10-subscription enterprise (Azure Production Capstone).

### Short Answer (30 seconds)

Platform hosts shared failover group runbook; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Design:** Multi-subscription estate with platform vs application separation.
Shared failover group runbook and RTO/RPO validation in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Tested dr runbook with quarterly game days.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize dr runbook and game day.

### Follow-up Questions

1. **How do Policy exemptions work during dr runbook and game day migration?**
2. **What FinOps tag strategy supports dr runbook and game day chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for failover group runbook testing
- Policies only at resource group — not MG

---

## Q037: C4 Container Diagram — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Documentation |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply C4 Container Diagram using C4 context and container in a Azure Production Capstone architecture review?

### Short Answer (30 seconds)

Use C4 context and container with Azure service mapping; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. C4 diagrams mapping to azure resources for capstone.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Context:** C4 Container Diagram is core to Azure Solution Architect interviews covering C4 context and container, Azure service mapping.

**Architect approach:**
1. Map business requirement to C4 context and container — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
C4 diagrams mapping to azure resources for capstone.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect C4 diagrams mapping to Azure resources for capstone — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to C4 context and container?**
2. **What KPI proves c4 container diagram adoption succeeded?**

### Common Mistakes in Interviews

- Listing C4 context and container without explaining trade-offs
- No Policy or IaC enforcement for c4 container diagram
- Skipping operational runbook for C4 context and container

---

## Q038: C4 Container Diagram — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Documentation |
| **Frequency** | Common |

### Question

**Intermediate:** Design production c4 container diagram for a 10-subscription enterprise (Azure Production Capstone).

### Short Answer (30 seconds)

Platform hosts shared C4 context and container; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Design:** Multi-subscription estate with platform vs application separation.
Shared C4 context and container and Azure service mapping in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
C4 diagrams mapping to azure resources for capstone.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize c4 container diagram.

### Follow-up Questions

1. **How do Policy exemptions work during c4 container diagram migration?**
2. **What FinOps tag strategy supports c4 container diagram chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for C4 context and container testing
- Policies only at resource group — not MG

---

## Q039: ADR for Azure Decisions — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply ADR for Azure Decisions using ADR template in a Azure Production Capstone architecture review?

### Short Answer (30 seconds)

Use ADR template with App Service vs AKS; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Write adrs for significant azure service choices.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Context:** ADR for Azure Decisions is core to Azure Solution Architect interviews covering ADR template, App Service vs AKS, alternatives.

**Architect approach:**
1. Map business requirement to ADR template — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Write adrs for significant azure service choices.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect write ADRs for significant Azure service choices — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to ADR template?**
2. **What KPI proves adr for azure decisions adoption succeeded?**

### Common Mistakes in Interviews

- Listing ADR template without explaining trade-offs
- No Policy or IaC enforcement for adr for azure decisions
- Skipping operational runbook for ADR template

---

## Q040: ADR for Azure Decisions — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

**Intermediate:** Design production adr for azure decisions for a 10-subscription enterprise (Azure Production Capstone).

### Short Answer (30 seconds)

Platform hosts shared ADR template; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Design:** Multi-subscription estate with platform vs application separation.
Shared ADR template and App Service vs AKS in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Write adrs for significant azure service choices.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize adr for azure decisions.

### Follow-up Questions

1. **How do Policy exemptions work during adr for azure decisions migration?**
2. **What FinOps tag strategy supports adr for azure decisions chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for ADR template testing
- Policies only at resource group — not MG

---

## Q041: Security Controls Traceability — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compliance |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Security Controls Traceability using SOC2 matrix in a Azure Production Capstone architecture review?

### Short Answer (30 seconds)

Use SOC2 matrix with control to Azure implementation; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Map security controls to evidence for auditors.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Context:** Security Controls Traceability is core to Azure Solution Architect interviews covering SOC2 matrix, control to Azure implementation.

**Architect approach:**
1. Map business requirement to SOC2 matrix — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Map security controls to evidence for auditors.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect map security controls to evidence for auditors — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to SOC2 matrix?**
2. **What KPI proves security controls traceability adoption succeeded?**

### Common Mistakes in Interviews

- Listing SOC2 matrix without explaining trade-offs
- No Policy or IaC enforcement for security controls traceability
- Skipping operational runbook for SOC2 matrix

---

## Q042: Security Controls Traceability — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compliance |
| **Frequency** | Common |

### Question

**Intermediate:** Design production security controls traceability for a 10-subscription enterprise (Azure Production Capstone).

### Short Answer (30 seconds)

Platform hosts shared SOC2 matrix; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Design:** Multi-subscription estate with platform vs application separation.
Shared SOC2 matrix and control to Azure implementation in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Map security controls to evidence for auditors.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize security controls traceability.

### Follow-up Questions

1. **How do Policy exemptions work during security controls traceability migration?**
2. **What FinOps tag strategy supports security controls traceability chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for SOC2 matrix testing
- Policies only at resource group — not MG

---

## Q043: Capstone Cost Estimate — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Capstone Cost Estimate using pricing calculator in a Azure Production Capstone architecture review?

### Short Answer (30 seconds)

Use pricing calculator with assumptions; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Defensible order-of-magnitude azure cost estimate.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Context:** Capstone Cost Estimate is core to Azure Solution Architect interviews covering pricing calculator, assumptions, sensitivity analysis.

**Architect approach:**
1. Map business requirement to pricing calculator — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Defensible order-of-magnitude azure cost estimate.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect defensible order-of-magnitude Azure cost estimate — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to pricing calculator?**
2. **What KPI proves capstone cost estimate adoption succeeded?**

### Common Mistakes in Interviews

- Listing pricing calculator without explaining trade-offs
- No Policy or IaC enforcement for capstone cost estimate
- Skipping operational runbook for pricing calculator

---

## Q044: Capstone Cost Estimate — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

**Intermediate:** Design production capstone cost estimate for a 10-subscription enterprise (Azure Production Capstone).

### Short Answer (30 seconds)

Platform hosts shared pricing calculator; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Design:** Multi-subscription estate with platform vs application separation.
Shared pricing calculator and assumptions in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Defensible order-of-magnitude azure cost estimate.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize capstone cost estimate.

### Follow-up Questions

1. **How do Policy exemptions work during capstone cost estimate migration?**
2. **What FinOps tag strategy supports capstone cost estimate chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for pricing calculator testing
- Policies only at resource group — not MG

---

## Q045: Integration Capstone Synthesis — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Integration |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Integration Capstone Synthesis using sync API in a Azure Production Capstone architecture review?

### Short Answer (30 seconds)

Use sync API with async events; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Integration architecture for capstone e-commerce.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Context:** Integration Capstone Synthesis is core to Azure Solution Architect interviews covering sync API, async events, outbox, APIM.

**Architect approach:**
1. Map business requirement to sync API — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Integration architecture for capstone e-commerce.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect integration architecture for capstone e-commerce — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to sync API?**
2. **What KPI proves integration capstone synthesis adoption succeeded?**

### Common Mistakes in Interviews

- Listing sync API without explaining trade-offs
- No Policy or IaC enforcement for integration capstone synthesis
- Skipping operational runbook for sync API

---

## Q046: Integration Capstone Synthesis — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Integration |
| **Frequency** | Common |

### Question

**Intermediate:** Design production integration capstone synthesis for a 10-subscription enterprise (Azure Production Capstone).

### Short Answer (30 seconds)

Platform hosts shared sync API; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Design:** Multi-subscription estate with platform vs application separation.
Shared sync API and async events in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Integration architecture for capstone e-commerce.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize integration capstone synthesis.

### Follow-up Questions

1. **How do Policy exemptions work during integration capstone synthesis migration?**
2. **What FinOps tag strategy supports integration capstone synthesis chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for sync API testing
- Policies only at resource group — not MG

---

## Q047: Observability Stack — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Observability Stack using OpenTelemetry in a Azure Production Capstone architecture review?

### Short Answer (30 seconds)

Use OpenTelemetry with App Insights; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Production observability stack for capstone.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Context:** Observability Stack is core to Azure Solution Architect interviews covering OpenTelemetry, App Insights, SLO alerts, runbooks.

**Architect approach:**
1. Map business requirement to OpenTelemetry — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Production observability stack for capstone.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect production observability stack for capstone — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to OpenTelemetry?**
2. **What KPI proves observability stack adoption succeeded?**

### Common Mistakes in Interviews

- Listing OpenTelemetry without explaining trade-offs
- No Policy or IaC enforcement for observability stack
- Skipping operational runbook for OpenTelemetry

---

## Q048: Observability Stack — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Common |

### Question

**Intermediate:** Design production observability stack for a 10-subscription enterprise (Azure Production Capstone).

### Short Answer (30 seconds)

Platform hosts shared OpenTelemetry; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Design:** Multi-subscription estate with platform vs application separation.
Shared OpenTelemetry and App Insights in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Production observability stack for capstone.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize observability stack.

### Follow-up Questions

1. **How do Policy exemptions work during observability stack migration?**
2. **What FinOps tag strategy supports observability stack chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for OpenTelemetry testing
- Policies only at resource group — not MG

---

## Q049: Capstone Defense Communication — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Communication |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Capstone Defense Communication using trade-off defense in a Azure Production Capstone architecture review?

### Short Answer (30 seconds)

Use trade-off defense with MVP vs target state; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Defend architecture decisions under interviewer challenge.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Context:** Capstone Defense Communication is core to Azure Solution Architect interviews covering trade-off defense, MVP vs target state.

**Architect approach:**
1. Map business requirement to trade-off defense — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Defend architecture decisions under interviewer challenge.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect defend architecture decisions under interviewer challenge — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to trade-off defense?**
2. **What KPI proves capstone defense communication adoption succeeded?**

### Common Mistakes in Interviews

- Listing trade-off defense without explaining trade-offs
- No Policy or IaC enforcement for capstone defense communication
- Skipping operational runbook for trade-off defense

---

## Q050: Capstone Defense Communication — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Communication |
| **Frequency** | Common |

### Question

**Intermediate:** Design production capstone defense communication for a 10-subscription enterprise (Azure Production Capstone).

### Short Answer (30 seconds)

Platform hosts shared trade-off defense; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Design:** Multi-subscription estate with platform vs application separation.
Shared trade-off defense and MVP vs target state in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Defend architecture decisions under interviewer challenge.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize capstone defense communication.

### Follow-up Questions

1. **How do Policy exemptions work during capstone defense communication migration?**
2. **What FinOps tag strategy supports capstone defense communication chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for trade-off defense testing
- Policies only at resource group — not MG

---

## Q051: Multi-Region Capstone Design — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reliability |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Multi-Region Capstone Design using active-active in a Azure Production Capstone architecture review?

### Short Answer (30 seconds)

Use active-active with data consistency; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Multi-region capstone when business justifies complexity.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Context:** Multi-Region Capstone Design is core to Azure Solution Architect interviews covering active-active, data consistency, Front Door.

**Architect approach:**
1. Map business requirement to active-active — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Multi-region capstone when business justifies complexity.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect multi-region capstone when business justifies complexity — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to active-active?**
2. **What KPI proves multi-region capstone design adoption succeeded?**

### Common Mistakes in Interviews

- Listing active-active without explaining trade-offs
- No Policy or IaC enforcement for multi-region capstone design
- Skipping operational runbook for active-active

---

## Q052: Multi-Region Capstone Design — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reliability |
| **Frequency** | Common |

### Question

**Intermediate:** Design production multi-region capstone design for a 10-subscription enterprise (Azure Production Capstone).

### Short Answer (30 seconds)

Platform hosts shared active-active; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Design:** Multi-subscription estate with platform vs application separation.
Shared active-active and data consistency in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Multi-region capstone when business justifies complexity.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize multi-region capstone design.

### Follow-up Questions

1. **How do Policy exemptions work during multi-region capstone design migration?**
2. **What FinOps tag strategy supports multi-region capstone design chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for active-active testing
- Policies only at resource group — not MG

---

## Q053: Identity Capstone Checklist — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Identity Capstone Checklist using MI everywhere in a Azure Production Capstone architecture review?

### Short Answer (30 seconds)

Use MI everywhere with CA; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Identity security checklist for production capstone.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Context:** Identity Capstone Checklist is core to Azure Solution Architect interviews covering MI everywhere, CA, Key Vault, no secrets in Git.

**Architect approach:**
1. Map business requirement to MI everywhere — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Identity security checklist for production capstone.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect identity security checklist for production capstone — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to MI everywhere?**
2. **What KPI proves identity capstone checklist adoption succeeded?**

### Common Mistakes in Interviews

- Listing MI everywhere without explaining trade-offs
- No Policy or IaC enforcement for identity capstone checklist
- Skipping operational runbook for MI everywhere

---

## Q054: Identity Capstone Checklist — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Common |

### Question

**Intermediate:** Design production identity capstone checklist for a 10-subscription enterprise (Azure Production Capstone).

### Short Answer (30 seconds)

Platform hosts shared MI everywhere; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Design:** Multi-subscription estate with platform vs application separation.
Shared MI everywhere and CA in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Identity security checklist for production capstone.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize identity capstone checklist.

### Follow-up Questions

1. **How do Policy exemptions work during identity capstone checklist migration?**
2. **What FinOps tag strategy supports identity capstone checklist chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for MI everywhere testing
- Policies only at resource group — not MG

---

## Q055: Network Capstone Checklist — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Network Capstone Checklist using hub-spoke in a Azure Production Capstone architecture review?

### Short Answer (30 seconds)

Use hub-spoke with Private Link; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Network security checklist for capstone review.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Context:** Network Capstone Checklist is core to Azure Solution Architect interviews covering hub-spoke, Private Link, no public data endpoints.

**Architect approach:**
1. Map business requirement to hub-spoke — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Network security checklist for capstone review.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect network security checklist for capstone review — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to hub-spoke?**
2. **What KPI proves network capstone checklist adoption succeeded?**

### Common Mistakes in Interviews

- Listing hub-spoke without explaining trade-offs
- No Policy or IaC enforcement for network capstone checklist
- Skipping operational runbook for hub-spoke

---

## Q056: Network Capstone Checklist — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Networking |
| **Frequency** | Common |

### Question

**Intermediate:** Design production network capstone checklist for a 10-subscription enterprise (Azure Production Capstone).

### Short Answer (30 seconds)

Platform hosts shared hub-spoke; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Design:** Multi-subscription estate with platform vs application separation.
Shared hub-spoke and Private Link in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Network security checklist for capstone review.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize network capstone checklist.

### Follow-up Questions

1. **How do Policy exemptions work during network capstone checklist migration?**
2. **What FinOps tag strategy supports network capstone checklist chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for hub-spoke testing
- Policies only at resource group — not MG

---

## Q057: Data Capstone Checklist — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Data |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Data Capstone Checklist using SQL HA in a Azure Production Capstone architecture review?

### Short Answer (30 seconds)

Use SQL HA with Cosmos partition key; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Data platform checklist for capstone sign-off.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Context:** Data Capstone Checklist is core to Azure Solution Architect interviews covering SQL HA, Cosmos partition key, backup tested restore.

**Architect approach:**
1. Map business requirement to SQL HA — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Data platform checklist for capstone sign-off.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect data platform checklist for capstone sign-off — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to SQL HA?**
2. **What KPI proves data capstone checklist adoption succeeded?**

### Common Mistakes in Interviews

- Listing SQL HA without explaining trade-offs
- No Policy or IaC enforcement for data capstone checklist
- Skipping operational runbook for SQL HA

---

## Q058: Data Capstone Checklist — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Data |
| **Frequency** | Common |

### Question

**Intermediate:** Design production data capstone checklist for a 10-subscription enterprise (Azure Production Capstone).

### Short Answer (30 seconds)

Platform hosts shared SQL HA; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Design:** Multi-subscription estate with platform vs application separation.
Shared SQL HA and Cosmos partition key in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Data platform checklist for capstone sign-off.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize data capstone checklist.

### Follow-up Questions

1. **How do Policy exemptions work during data capstone checklist migration?**
2. **What FinOps tag strategy supports data capstone checklist chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for SQL HA testing
- Policies only at resource group — not MG

---

## Q059: Performance Validation — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Performance Validation using load test k6 in a Azure Production Capstone architecture review?

### Short Answer (30 seconds)

Use load test k6 with performance budget; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Validate performance nfrs before production gate.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Context:** Performance Validation is core to Azure Solution Architect interviews covering load test k6, performance budget, autoscale validation.

**Architect approach:**
1. Map business requirement to load test k6 — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Validate performance nfrs before production gate.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect validate performance NFRs before production gate — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to load test k6?**
2. **What KPI proves performance validation adoption succeeded?**

### Common Mistakes in Interviews

- Listing load test k6 without explaining trade-offs
- No Policy or IaC enforcement for performance validation
- Skipping operational runbook for load test k6

---

## Q060: Performance Validation — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Performance |
| **Frequency** | Common |

### Question

**Intermediate:** Design production performance validation for a 10-subscription enterprise (Azure Production Capstone).

### Short Answer (30 seconds)

Platform hosts shared load test k6; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Design:** Multi-subscription estate with platform vs application separation.
Shared load test k6 and performance budget in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Validate performance nfrs before production gate.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize performance validation.

### Follow-up Questions

1. **How do Policy exemptions work during performance validation migration?**
2. **What FinOps tag strategy supports performance validation chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for load test k6 testing
- Policies only at resource group — not MG

---

## Q061: Operational Readiness Review — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Operational Readiness Review using runbooks in a Azure Production Capstone architecture review?

### Short Answer (30 seconds)

Use runbooks with on-call; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Orr gate before production launch.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Context:** Operational Readiness Review is core to Azure Solution Architect interviews covering runbooks, on-call, alert routing, deployment pipeline.

**Architect approach:**
1. Map business requirement to runbooks — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Orr gate before production launch.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect ORR gate before production launch — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to runbooks?**
2. **What KPI proves operational readiness review adoption succeeded?**

### Common Mistakes in Interviews

- Listing runbooks without explaining trade-offs
- No Policy or IaC enforcement for operational readiness review
- Skipping operational runbook for runbooks

---

## Q062: Operational Readiness Review — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Common |

### Question

**Intermediate:** Design production operational readiness review for a 10-subscription enterprise (Azure Production Capstone).

### Short Answer (30 seconds)

Platform hosts shared runbooks; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Design:** Multi-subscription estate with platform vs application separation.
Shared runbooks and on-call in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Orr gate before production launch.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize operational readiness review.

### Follow-up Questions

1. **How do Policy exemptions work during operational readiness review migration?**
2. **What FinOps tag strategy supports operational readiness review chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for runbooks testing
- Policies only at resource group — not MG

---

## Q063: Risk Register Capstone — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Risk Register Capstone using architecture risks in a Azure Production Capstone architecture review?

### Short Answer (30 seconds)

Use architecture risks with mitigation owners; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Capstone risk register for executive visibility.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Context:** Risk Register Capstone is core to Azure Solution Architect interviews covering architecture risks, mitigation owners, residual risk.

**Architect approach:**
1. Map business requirement to architecture risks — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Capstone risk register for executive visibility.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect capstone risk register for executive visibility — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to architecture risks?**
2. **What KPI proves risk register capstone adoption succeeded?**

### Common Mistakes in Interviews

- Listing architecture risks without explaining trade-offs
- No Policy or IaC enforcement for risk register capstone
- Skipping operational runbook for architecture risks

---

## Q064: Risk Register Capstone — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

**Intermediate:** Design production risk register capstone for a 10-subscription enterprise (Azure Production Capstone).

### Short Answer (30 seconds)

Platform hosts shared architecture risks; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Design:** Multi-subscription estate with platform vs application separation.
Shared architecture risks and mitigation owners in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Capstone risk register for executive visibility.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize risk register capstone.

### Follow-up Questions

1. **How do Policy exemptions work during risk register capstone migration?**
2. **What FinOps tag strategy supports risk register capstone chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for architecture risks testing
- Policies only at resource group — not MG

---

## Q065: Phased Delivery Roadmap — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Strategy |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Phased Delivery Roadmap using MVP phase 1 in a Azure Production Capstone architecture review?

### Short Answer (30 seconds)

Use MVP phase 1 with target state phase 2; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Phased roadmap when capstone is over-engineered for mvp.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Context:** Phased Delivery Roadmap is core to Azure Solution Architect interviews covering MVP phase 1, target state phase 2, metric triggers.

**Architect approach:**
1. Map business requirement to MVP phase 1 — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Phased roadmap when capstone is over-engineered for mvp.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect phased roadmap when capstone is over-engineered for MVP — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to MVP phase 1?**
2. **What KPI proves phased delivery roadmap adoption succeeded?**

### Common Mistakes in Interviews

- Listing MVP phase 1 without explaining trade-offs
- No Policy or IaC enforcement for phased delivery roadmap
- Skipping operational runbook for MVP phase 1

---

## Q066: Phased Delivery Roadmap — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Strategy |
| **Frequency** | Common |

### Question

**Intermediate:** Design production phased delivery roadmap for a 10-subscription enterprise (Azure Production Capstone).

### Short Answer (30 seconds)

Platform hosts shared MVP phase 1; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Design:** Multi-subscription estate with platform vs application separation.
Shared MVP phase 1 and target state phase 2 in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Phased roadmap when capstone is over-engineered for mvp.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize phased delivery roadmap.

### Follow-up Questions

1. **How do Policy exemptions work during phased delivery roadmap migration?**
2. **What FinOps tag strategy supports phased delivery roadmap chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for MVP phase 1 testing
- Policies only at resource group — not MG

---

## Q067: Executive Architecture Summary — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Communication |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Executive Architecture Summary using one-page exec summary in a Azure Production Capstone architecture review?

### Short Answer (30 seconds)

Use one-page exec summary with cost; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Communicate capstone to non-technical stakeholders.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Context:** Executive Architecture Summary is core to Azure Solution Architect interviews covering one-page exec summary, cost, risk, timeline.

**Architect approach:**
1. Map business requirement to one-page exec summary — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Communicate capstone to non-technical stakeholders.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect communicate capstone to non-technical stakeholders — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to one-page exec summary?**
2. **What KPI proves executive architecture summary adoption succeeded?**

### Common Mistakes in Interviews

- Listing one-page exec summary without explaining trade-offs
- No Policy or IaC enforcement for executive architecture summary
- Skipping operational runbook for one-page exec summary

---

## Q068: Executive Architecture Summary — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Communication |
| **Frequency** | Common |

### Question

**Intermediate:** Design production executive architecture summary for a 10-subscription enterprise (Azure Production Capstone).

### Short Answer (30 seconds)

Platform hosts shared one-page exec summary; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Design:** Multi-subscription estate with platform vs application separation.
Shared one-page exec summary and cost in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Communicate capstone to non-technical stakeholders.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize executive architecture summary.

### Follow-up Questions

1. **How do Policy exemptions work during executive architecture summary migration?**
2. **What FinOps tag strategy supports executive architecture summary chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for one-page exec summary testing
- Policies only at resource group — not MG

---

## Q069: Graduation Scenario Panel — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Scenario |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Graduation Scenario Panel using full-stack Azure review under time pressure in a Azure Production Capstone architecture review?

### Short Answer (30 seconds)

Use full-stack Azure review under time pressure with full-stack Azure review under time pressure; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Synthesize weeks 9–16 in expert scenario defense.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Context:** Graduation Scenario Panel is core to Azure Solution Architect interviews covering full-stack Azure review under time pressure.

**Architect approach:**
1. Map business requirement to full-stack Azure review under time pressure — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Synthesize weeks 9–16 in expert scenario defense.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect synthesize weeks 9–16 in expert scenario defense — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to full-stack Azure review under time pressure?**
2. **What KPI proves graduation scenario panel adoption succeeded?**

### Common Mistakes in Interviews

- Listing full-stack Azure review under time pressure without explaining trade-offs
- No Policy or IaC enforcement for graduation scenario panel
- Skipping operational runbook for full-stack Azure review under time pressure

---

## Q070: Graduation Scenario Panel — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Scenario |
| **Frequency** | Common |

### Question

**Intermediate:** Design production graduation scenario panel for a 10-subscription enterprise (Azure Production Capstone).

### Short Answer (30 seconds)

Platform hosts shared full-stack Azure review under time pressure; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 16:** Azure Production Capstone

**Design:** Multi-subscription estate with platform vs application separation.
Shared full-stack Azure review under time pressure and full-stack Azure review under time pressure in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Synthesize weeks 9–16 in expert scenario defense.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize graduation scenario panel.

### Follow-up Questions

1. **How do Policy exemptions work during graduation scenario panel migration?**
2. **What FinOps tag strategy supports graduation scenario panel chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for full-stack Azure review under time pressure testing
- Policies only at resource group — not MG

---
