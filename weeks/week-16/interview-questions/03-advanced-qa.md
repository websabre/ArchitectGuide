# Week 16 — Advanced Q&A

> Q071–Q100: Premium format (Week 1 quality).

---


## Q071: Production WAF Review — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Capstone |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling production waf review across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for all WAF pillars.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 16:** Azure Production Capstone

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Production WAF Review must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full production waf review immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** all WAF pillars, review checklist, ranked findings. Mitigation: Policy exemptions with expiry; game day validation.
Lead production architecture review using waf scorecard.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating production waf review for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q072: Production WAF Review — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Capstone |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling production waf review across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for all WAF pillars.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 16:** Azure Production Capstone

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Production WAF Review must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full production waf review immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** all WAF pillars, review checklist, ranked findings. Mitigation: Policy exemptions with expiry; game day validation.
Lead production architecture review using waf scorecard.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating production waf review for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q073: Composite SLA Calculation — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Reliability |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling composite sla calculation across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for Front Door.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 16:** Azure Production Capstone

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Composite SLA Calculation must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full composite sla calculation immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** Front Door, App Service, SQL SLA multiplication. Mitigation: Policy exemptions with expiry; game day validation.
Composite sla math and weakest-link mitigation.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating composite sla calculation for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q074: Composite SLA Calculation — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Reliability |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to composite sla calculation without downtime?

### Short Answer (30 seconds)

Tier workloads, phase composite sla calculation rollout, time-bound exemptions, golden-path IaC using Front Door.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 16:** Azure Production Capstone

**Scenario:** Migrating brownfield workloads to composite sla calculation without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full composite sla calculation on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** Front Door, App Service, SQL SLA multiplication. Anchor: **Front Door** + **App Service**.
Composite sla math and weakest-link mitigation.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same composite sla calculation strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q075: DR Runbook and Game Day — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | DR |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to dr runbook and game day without downtime?

### Short Answer (30 seconds)

Tier workloads, phase dr runbook and game day rollout, time-bound exemptions, golden-path IaC using failover group runbook.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 16:** Azure Production Capstone

**Scenario:** Migrating brownfield workloads to dr runbook and game day without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full dr runbook and game day on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** failover group runbook, RTO/RPO validation, communication. Anchor: **failover group runbook** + **RTO/RPO validation**.
Tested dr runbook with quarterly game days.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same dr runbook and game day strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q076: DR Runbook and Game Day — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | DR |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling dr runbook and game day across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for failover group runbook.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 16:** Azure Production Capstone

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
DR Runbook and Game Day must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full dr runbook and game day immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** failover group runbook, RTO/RPO validation, communication. Mitigation: Policy exemptions with expiry; game day validation.
Tested dr runbook with quarterly game days.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating dr runbook and game day for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q077: C4 Container Diagram — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Documentation |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling c4 container diagram across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for C4 context and container.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 16:** Azure Production Capstone

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
C4 Container Diagram must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full c4 container diagram immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** C4 context and container, Azure service mapping. Mitigation: Policy exemptions with expiry; game day validation.
C4 diagrams mapping to azure resources for capstone.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating c4 container diagram for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q078: C4 Container Diagram — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Documentation |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling c4 container diagram across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for C4 context and container.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 16:** Azure Production Capstone

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
C4 Container Diagram must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full c4 container diagram immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** C4 context and container, Azure service mapping. Mitigation: Policy exemptions with expiry; game day validation.
C4 diagrams mapping to azure resources for capstone.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating c4 container diagram for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q079: ADR for Azure Decisions — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Governance |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling adr for azure decisions across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for ADR template.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 16:** Azure Production Capstone

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
ADR for Azure Decisions must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full adr for azure decisions immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** ADR template, App Service vs AKS, alternatives. Mitigation: Policy exemptions with expiry; game day validation.
Write adrs for significant azure service choices.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating adr for azure decisions for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q080: ADR for Azure Decisions — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Governance |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to adr for azure decisions without downtime?

### Short Answer (30 seconds)

Tier workloads, phase adr for azure decisions rollout, time-bound exemptions, golden-path IaC using ADR template.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 16:** Azure Production Capstone

**Scenario:** Migrating brownfield workloads to adr for azure decisions without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full adr for azure decisions on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** ADR template, App Service vs AKS, alternatives. Anchor: **ADR template** + **App Service vs AKS**.
Write adrs for significant azure service choices.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same adr for azure decisions strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q081: Security Controls Traceability — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Compliance |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to security controls traceability without downtime?

### Short Answer (30 seconds)

Tier workloads, phase security controls traceability rollout, time-bound exemptions, golden-path IaC using SOC2 matrix.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 16:** Azure Production Capstone

**Scenario:** Migrating brownfield workloads to security controls traceability without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full security controls traceability on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** SOC2 matrix, control to Azure implementation. Anchor: **SOC2 matrix** + **control to Azure implementation**.
Map security controls to evidence for auditors.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same security controls traceability strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q082: Security Controls Traceability — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Compliance |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling security controls traceability across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for SOC2 matrix.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 16:** Azure Production Capstone

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Security Controls Traceability must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full security controls traceability immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** SOC2 matrix, control to Azure implementation. Mitigation: Policy exemptions with expiry; game day validation.
Map security controls to evidence for auditors.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating security controls traceability for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q083: Capstone Cost Estimate — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | FinOps |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling capstone cost estimate across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for pricing calculator.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 16:** Azure Production Capstone

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Capstone Cost Estimate must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full capstone cost estimate immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** pricing calculator, assumptions, sensitivity analysis. Mitigation: Policy exemptions with expiry; game day validation.
Defensible order-of-magnitude azure cost estimate.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating capstone cost estimate for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q084: Capstone Cost Estimate — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | FinOps |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling capstone cost estimate across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for pricing calculator.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 16:** Azure Production Capstone

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Capstone Cost Estimate must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full capstone cost estimate immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** pricing calculator, assumptions, sensitivity analysis. Mitigation: Policy exemptions with expiry; game day validation.
Defensible order-of-magnitude azure cost estimate.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating capstone cost estimate for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q085: Integration Capstone Synthesis — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Integration |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling integration capstone synthesis across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for sync API.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 16:** Azure Production Capstone

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Integration Capstone Synthesis must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full integration capstone synthesis immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** sync API, async events, outbox, APIM. Mitigation: Policy exemptions with expiry; game day validation.
Integration architecture for capstone e-commerce.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating integration capstone synthesis for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q086: Integration Capstone Synthesis — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Integration |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to integration capstone synthesis without downtime?

### Short Answer (30 seconds)

Tier workloads, phase integration capstone synthesis rollout, time-bound exemptions, golden-path IaC using sync API.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 16:** Azure Production Capstone

**Scenario:** Migrating brownfield workloads to integration capstone synthesis without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full integration capstone synthesis on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** sync API, async events, outbox. Anchor: **sync API** + **async events**.
Integration architecture for capstone e-commerce.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same integration capstone synthesis strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q087: Observability Stack — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Operations |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to observability stack without downtime?

### Short Answer (30 seconds)

Tier workloads, phase observability stack rollout, time-bound exemptions, golden-path IaC using OpenTelemetry.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 16:** Azure Production Capstone

**Scenario:** Migrating brownfield workloads to observability stack without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full observability stack on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** OpenTelemetry, App Insights, SLO alerts. Anchor: **OpenTelemetry** + **App Insights**.
Production observability stack for capstone.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same observability stack strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q088: Observability Stack — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Operations |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling observability stack across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for OpenTelemetry.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 16:** Azure Production Capstone

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Observability Stack must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full observability stack immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** OpenTelemetry, App Insights, SLO alerts, runbooks. Mitigation: Policy exemptions with expiry; game day validation.
Production observability stack for capstone.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating observability stack for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q089: Capstone Defense Communication — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Communication |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling capstone defense communication across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for trade-off defense.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 16:** Azure Production Capstone

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Capstone Defense Communication must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full capstone defense communication immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** trade-off defense, MVP vs target state. Mitigation: Policy exemptions with expiry; game day validation.
Defend architecture decisions under interviewer challenge.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating capstone defense communication for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q090: Capstone Defense Communication — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Communication |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling capstone defense communication across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for trade-off defense.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 16:** Azure Production Capstone

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Capstone Defense Communication must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full capstone defense communication immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** trade-off defense, MVP vs target state. Mitigation: Policy exemptions with expiry; game day validation.
Defend architecture decisions under interviewer challenge.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating capstone defense communication for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q091: Multi-Region Capstone Design — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Reliability |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling multi-region capstone design across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for active-active.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 16:** Azure Production Capstone

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Multi-Region Capstone Design must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full multi-region capstone design immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** active-active, data consistency, Front Door. Mitigation: Policy exemptions with expiry; game day validation.
Multi-region capstone when business justifies complexity.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating multi-region capstone design for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q092: Identity Capstone Checklist — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Identity |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to identity capstone checklist without downtime?

### Short Answer (30 seconds)

Tier workloads, phase identity capstone checklist rollout, time-bound exemptions, golden-path IaC using MI everywhere.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 16:** Azure Production Capstone

**Scenario:** Migrating brownfield workloads to identity capstone checklist without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full identity capstone checklist on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** MI everywhere, CA, Key Vault. Anchor: **MI everywhere** + **CA**.
Identity security checklist for production capstone.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same identity capstone checklist strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q093: Network Capstone Checklist — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Networking |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling network capstone checklist across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for hub-spoke.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 16:** Azure Production Capstone

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Network Capstone Checklist must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full network capstone checklist immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** hub-spoke, Private Link, no public data endpoints. Mitigation: Policy exemptions with expiry; game day validation.
Network security checklist for capstone review.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating network capstone checklist for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q094: Data Capstone Checklist — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Data |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling data capstone checklist across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for SQL HA.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 16:** Azure Production Capstone

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Data Capstone Checklist must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full data capstone checklist immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** SQL HA, Cosmos partition key, backup tested restore. Mitigation: Policy exemptions with expiry; game day validation.
Data platform checklist for capstone sign-off.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating data capstone checklist for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q095: Performance Validation — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Performance |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to performance validation without downtime?

### Short Answer (30 seconds)

Tier workloads, phase performance validation rollout, time-bound exemptions, golden-path IaC using load test k6.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 16:** Azure Production Capstone

**Scenario:** Migrating brownfield workloads to performance validation without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full performance validation on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** load test k6, performance budget, autoscale validation. Anchor: **load test k6** + **performance budget**.
Validate performance nfrs before production gate.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same performance validation strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q096: Operational Readiness Review — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Operations |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling operational readiness review across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for runbooks.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 16:** Azure Production Capstone

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Operational Readiness Review must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full operational readiness review immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** runbooks, on-call, alert routing, deployment pipeline. Mitigation: Policy exemptions with expiry; game day validation.
Orr gate before production launch.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating operational readiness review for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q097: Risk Register Capstone — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Governance |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling risk register capstone across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for architecture risks.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 16:** Azure Production Capstone

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Risk Register Capstone must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full risk register capstone immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** architecture risks, mitigation owners, residual risk. Mitigation: Policy exemptions with expiry; game day validation.
Capstone risk register for executive visibility.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating risk register capstone for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q098: Phased Delivery Roadmap — Advanced Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Strategy |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise when migrating brownfield workloads to phased delivery roadmap without downtime?

### Short Answer (30 seconds)

Tier workloads, phase phased delivery roadmap rollout, time-bound exemptions, golden-path IaC using MVP phase 1.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 16:** Azure Production Capstone

**Scenario:** Migrating brownfield workloads to phased delivery roadmap without downtime. 15+ subscriptions, regulated data, weekly deployments.

**Trade-off matrix:**
| Approach | Pros | Cons |
|----------|------|------|
| Central deny Policy | Strong compliance | Blocks migration |
| Audit-only transition | Faster adoption | Temporary gap |
| Per-team exemptions | Team autonomy | Fragmented audit |
| Golden-path IaC module | Consistency | Release bottleneck |

**Recommendation:** Tier workloads (Tier-0/1/2). Full phased delivery roadmap on Tier-0 immediately.
Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

**Services:** MVP phase 1, target state phase 2, metric triggers. Anchor: **MVP phase 1** + **target state phase 2**.
Phased roadmap when capstone is over-engineered for mvp.

**Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.

### Architecture Perspective

Advanced architects deliver decision matrices and phased roadmaps.

### Follow-up Questions

1. **How handle team blocked by deny Policy mid-sprint?**
2. **What exception process prevents permanent waiver drift?**

### Common Mistakes in Interviews

- Same phased delivery roadmap strictness for sandbox and Tier-0
- Big-bang migration without audit-mode transition
- No brownfield migration runbook

---

## Q099: Executive Architecture Summary — Advanced Scale

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Communication |
| **Frequency** | Common |

### Question

**Advanced:** What trade-offs arise scaling executive architecture summary across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for one-page exec summary.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 16:** Azure Production Capstone

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Executive Architecture Summary must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full executive architecture summary immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** one-page exec summary, cost, risk, timeline. Mitigation: Policy exemptions with expiry; game day validation.
Communicate capstone to non-technical stakeholders.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating executive architecture summary for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---

## Q100: Graduation Scenario Panel — Advanced DR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Scenario |
| **Frequency** | Very Common |

### Question

**Advanced:** What trade-offs arise scaling graduation scenario panel across 20+ subscriptions and regions?

### Short Answer (30 seconds)

Tier workloads Tier-0/1/2; phase rollout; audit-mode Policy before deny; golden-path IaC for full-stack Azure review under time pressure.

### Detailed Answer (3–5 minutes)

**Difficulty:** Advanced | **Week 16:** Azure Production Capstone

**Enterprise scenario:** 20 subscriptions, multi-region, regulated data, weekly deployments.
Graduation Scenario Panel must scale without blocking delivery or fragmenting audit evidence.

**Trade-offs:** Central deny vs federate; strict Policy vs migration window; multi-region cost vs DR.
Tier-0 gets full graduation scenario panel immediately; Tier-2 gets 90-day migration with audit Policy.

**Services:** full-stack Azure review under time pressure. Mitigation: Policy exemptions with expiry; game day validation.
Synthesize weeks 9–16 in expert scenario defense.

### Architecture Perspective

Advanced architects quantify trade-offs and phase adoption.

### Follow-up Questions

1. **How handle team pushback on central standards?**
2. **Exception process with compensating controls?**

### Common Mistakes in Interviews

- Mandating graduation scenario panel for all tiers equally
- No exemption sunset process
- Advanced design without brownfield migration path

---
