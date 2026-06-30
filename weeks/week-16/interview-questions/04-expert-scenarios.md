# Week 16 — Expert Scenario Q&A

> Q101–Q120: Premium format (Week 1 quality).

---


## Q101: Production WAF Review — Expert Incident Response

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in production waf review. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via all WAF pillars → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 16:** Azure Production Capstone

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Production WAF Review gap; Resource Graph inventory of all WAF pillars, review checklist, ranked findings.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on all WAF pillars.
Lead production architecture review using waf scorecard. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for production waf review?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q102: Composite SLA Calculation — Expert Audit Remediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in composite sla calculation. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via Front Door → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 16:** Azure Production Capstone

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Composite SLA Calculation gap; Resource Graph inventory of Front Door, App Service, SQL SLA multiplication.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on Front Door.
Composite sla math and weakest-link mitigation. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for composite sla calculation?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q103: DR Runbook and Game Day — Expert Cost Redesign

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in dr runbook and game day. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via failover group runbook → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 16:** Azure Production Capstone

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to DR Runbook and Game Day gap; Resource Graph inventory of failover group runbook, RTO/RPO validation, communication.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on failover group runbook.
Tested dr runbook with quarterly game days. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for dr runbook and game day?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q104: C4 Container Diagram — Expert Standards Mediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in c4 container diagram. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via C4 context and container → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 16:** Azure Production Capstone

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to C4 Container Diagram gap; Resource Graph inventory of C4 context and container, Azure service mapping.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on C4 context and container.
C4 diagrams mapping to azure resources for capstone. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for c4 container diagram?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q105: ADR for Azure Decisions — Expert Incident Response

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in adr for azure decisions. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via ADR template → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 16:** Azure Production Capstone

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to ADR for Azure Decisions gap; Resource Graph inventory of ADR template, App Service vs AKS, alternatives.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on ADR template.
Write adrs for significant azure service choices. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for adr for azure decisions?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q106: Security Controls Traceability — Expert Audit Remediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in security controls traceability. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via SOC2 matrix → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 16:** Azure Production Capstone

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Security Controls Traceability gap; Resource Graph inventory of SOC2 matrix, control to Azure implementation.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on SOC2 matrix.
Map security controls to evidence for auditors. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for security controls traceability?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q107: Capstone Cost Estimate — Expert Cost Redesign

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in capstone cost estimate. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via pricing calculator → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 16:** Azure Production Capstone

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Capstone Cost Estimate gap; Resource Graph inventory of pricing calculator, assumptions, sensitivity analysis.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on pricing calculator.
Defensible order-of-magnitude azure cost estimate. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for capstone cost estimate?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q108: Integration Capstone Synthesis — Expert Standards Mediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in integration capstone synthesis. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via sync API → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 16:** Azure Production Capstone

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Integration Capstone Synthesis gap; Resource Graph inventory of sync API, async events, outbox, APIM.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on sync API.
Integration architecture for capstone e-commerce. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for integration capstone synthesis?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q109: Observability Stack — Expert Incident Response

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in observability stack. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via OpenTelemetry → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 16:** Azure Production Capstone

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Observability Stack gap; Resource Graph inventory of OpenTelemetry, App Insights, SLO alerts, runbooks.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on OpenTelemetry.
Production observability stack for capstone. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for observability stack?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q110: Capstone Defense Communication — Expert Audit Remediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in capstone defense communication. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via trade-off defense → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 16:** Azure Production Capstone

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Capstone Defense Communication gap; Resource Graph inventory of trade-off defense, MVP vs target state.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on trade-off defense.
Defend architecture decisions under interviewer challenge. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for capstone defense communication?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q111: Multi-Region Capstone Design — Expert Cost Redesign

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in multi-region capstone design. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via active-active → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 16:** Azure Production Capstone

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Multi-Region Capstone Design gap; Resource Graph inventory of active-active, data consistency, Front Door.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on active-active.
Multi-region capstone when business justifies complexity. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for multi-region capstone design?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q112: Identity Capstone Checklist — Expert Standards Mediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in identity capstone checklist. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via MI everywhere → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 16:** Azure Production Capstone

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Identity Capstone Checklist gap; Resource Graph inventory of MI everywhere, CA, Key Vault, no secrets in Git.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on MI everywhere.
Identity security checklist for production capstone. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for identity capstone checklist?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q113: Network Capstone Checklist — Expert Incident Response

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in network capstone checklist. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via hub-spoke → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 16:** Azure Production Capstone

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Network Capstone Checklist gap; Resource Graph inventory of hub-spoke, Private Link, no public data endpoints.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on hub-spoke.
Network security checklist for capstone review. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for network capstone checklist?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q114: Data Capstone Checklist — Expert Audit Remediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in data capstone checklist. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via SQL HA → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 16:** Azure Production Capstone

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Data Capstone Checklist gap; Resource Graph inventory of SQL HA, Cosmos partition key, backup tested restore.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on SQL HA.
Data platform checklist for capstone sign-off. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for data capstone checklist?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q115: Performance Validation — Expert Cost Redesign

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in performance validation. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via load test k6 → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 16:** Azure Production Capstone

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Performance Validation gap; Resource Graph inventory of load test k6, performance budget, autoscale validation.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on load test k6.
Validate performance nfrs before production gate. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for performance validation?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q116: Operational Readiness Review — Expert Standards Mediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in operational readiness review. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via runbooks → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 16:** Azure Production Capstone

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Operational Readiness Review gap; Resource Graph inventory of runbooks, on-call, alert routing, deployment pipeline.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on runbooks.
Orr gate before production launch. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for operational readiness review?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q117: Risk Register Capstone — Expert Incident Response

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in risk register capstone. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via architecture risks → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 16:** Azure Production Capstone

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Risk Register Capstone gap; Resource Graph inventory of architecture risks, mitigation owners, residual risk.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on architecture risks.
Capstone risk register for executive visibility. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for risk register capstone?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q118: Phased Delivery Roadmap — Expert Audit Remediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in phased delivery roadmap. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via MVP phase 1 → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 16:** Azure Production Capstone

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Phased Delivery Roadmap gap; Resource Graph inventory of MVP phase 1, target state phase 2, metric triggers.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on MVP phase 1.
Phased roadmap when capstone is over-engineered for mvp. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for phased delivery roadmap?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q119: Executive Architecture Summary — Expert Cost Redesign

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in executive architecture summary. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via one-page exec summary → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 16:** Azure Production Capstone

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Executive Architecture Summary gap; Resource Graph inventory of one-page exec summary, cost, risk, timeline.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on one-page exec summary.
Communicate capstone to non-technical stakeholders. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for executive architecture summary?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q120: Graduation Scenario Panel — Expert Standards Mediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in graduation scenario panel. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via full-stack Azure review under time pressure → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 16:** Azure Production Capstone

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Graduation Scenario Panel gap; Resource Graph inventory of full-stack Azure review under time pressure.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on full-stack Azure review under time pressure.
Synthesize weeks 9–16 in expert scenario defense. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for graduation scenario panel?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---
