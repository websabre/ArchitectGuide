# Week 14 — Expert Scenario Q&A

> Q101–Q120: Premium format (Week 1 quality).

---


## Q101: Defense in Depth Layers — Expert Incident Response

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in defense in depth layers. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via identity → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 14:** Azure Security

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Defense in Depth Layers gap; Resource Graph inventory of identity, perimeter, network, compute.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on identity.
Map defense-in-depth layers to azure controls. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for defense in depth layers?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q102: Azure WAF Operations — Expert Audit Remediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in azure waf operations. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via WAF detection/prevention → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 14:** Azure Security

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Azure WAF Operations gap; Resource Graph inventory of WAF detection/prevention, false positives, custom rules.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on WAF detection/prevention.
Operate waf in detection then prevention with tuning. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for azure waf operations?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q103: Defender for Cloud — Expert Cost Redesign

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in defender for cloud. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via CSPM → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 14:** Azure Security

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Defender for Cloud gap; Resource Graph inventory of CSPM, CWP, secure score, regulatory compliance dashboard.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on CSPM.
Defender for cloud in continuous compliance governance. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for defender for cloud?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q104: Encryption Requirements — Expert Standards Mediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in encryption requirements. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via TLS 1.2+ → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 14:** Azure Security

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Encryption Requirements gap; Resource Graph inventory of TLS 1.2+, TDE, CMK, tokenization.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on TLS 1.2+.
Encryption strategy reducing compliance scope. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for encryption requirements?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q105: DevSecOps Pipeline — Expert Incident Response

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in devsecops pipeline. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via CodeQL → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 14:** Azure Security

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to DevSecOps Pipeline gap; Resource Graph inventory of CodeQL, secret scan, Bicep what-if, container scan.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on CodeQL.
Security gates in golden ci/cd pipeline template. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for devsecops pipeline?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q106: OWASP API Security — Expert Audit Remediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in owasp api security. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via BOLA → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 14:** Azure Security

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to OWASP API Security gap; Resource Graph inventory of BOLA, authZ, rate limiting, APIM policies.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on BOLA.
Api security beyond network perimeter with apim. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for owasp api security?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q107: Sentinel Incident Response — Expert Cost Redesign

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in sentinel incident response. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via Sentinel → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 14:** Azure Security

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Sentinel Incident Response gap; Resource Graph inventory of Sentinel, playbooks, SOAR, Key Vault exfiltration runbook.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on Sentinel.
Security incident response on azure with sentinel. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for sentinel incident response?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q108: Azure Policy Security — Expert Standards Mediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in azure policy security. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via deny public IP → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 14:** Azure Security

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Azure Policy Security gap; Resource Graph inventory of deny public IP, require TLS, DINE diagnostics, Private Link.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on deny public IP.
Security policy initiatives at management group. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for azure policy security?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q109: Secrets Rotation — Expert Incident Response

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in secrets rotation. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via Key Vault rotation → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 14:** Azure Security

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Secrets Rotation gap; Resource Graph inventory of Key Vault rotation, Entra SQL auth, dual-user pattern.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on Key Vault rotation.
Automated secrets rotation without downtime. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for secrets rotation?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q110: Managed Identity Blast Radius — Expert Audit Remediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in managed identity blast radius. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via MI RBAC scope → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 14:** Azure Security

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Managed Identity Blast Radius gap; Resource Graph inventory of MI RBAC scope, compromised app containment.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on MI RBAC scope.
Limit blast radius when compute is compromised. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for managed identity blast radius?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q111: Microsoft Purview — Expert Cost Redesign

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in microsoft purview. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via data classification → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 14:** Azure Security

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Microsoft Purview gap; Resource Graph inventory of data classification, DLP, compliance manager.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on data classification.
Data classification and compliance mapping. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for microsoft purview?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q112: Network Segmentation Security — Expert Standards Mediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in network segmentation security. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via micro-segmentation → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 14:** Azure Security

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Network Segmentation Security gap; Resource Graph inventory of micro-segmentation, Zero Trust network, Private Link.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on micro-segmentation.
Network segmentation as security architecture. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for network segmentation security?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q113: Threat Modeling STRIDE — Expert Incident Response

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in threat modeling stride. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via STRIDE → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 14:** Azure Security

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Threat Modeling STRIDE gap; Resource Graph inventory of STRIDE, trust boundaries, DFD, mitigation verification.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on STRIDE.
Stride threat modeling in architecture review. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for threat modeling stride?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q114: Security Benchmark Initiative — Expert Audit Remediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in security benchmark initiative. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via Azure Security Benchmark → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 14:** Azure Security

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Security Benchmark Initiative gap; Resource Graph inventory of Azure Security Benchmark, CIS, custom initiatives.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on Azure Security Benchmark.
Assign and remediate security benchmark policies. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for security benchmark initiative?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q115: Pen Test and Red Team — Expert Cost Redesign

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in pen test and red team. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via penetration testing → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 14:** Azure Security

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Pen Test and Red Team gap; Resource Graph inventory of penetration testing, Microsoft rules of engagement.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on penetration testing.
Pre-production security validation approach. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for pen test and red team?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q116: Container Security — Expert Standards Mediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in container security. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via ACR scanning → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 14:** Azure Security

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Container Security gap; Resource Graph inventory of ACR scanning, AKS Defender, pod security, network policies.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on ACR scanning.
Container supply chain and runtime security. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for container security?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q117: SIEM and Log Retention — Expert Incident Response

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in siem and log retention. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via Sentinel → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 14:** Azure Security

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to SIEM and Log Retention gap; Resource Graph inventory of Sentinel, Log Analytics retention, audit requirements.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on Sentinel.
Siem architecture meeting retention and detection needs. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for siem and log retention?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q118: Compliance Evidence — Expert Audit Remediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in compliance evidence. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via SOC2 evidence → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 14:** Azure Security

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Compliance Evidence gap; Resource Graph inventory of SOC2 evidence, policy assignment IDs, audit trail.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on SOC2 evidence.
Collect compliance evidence from azure controls. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for compliance evidence?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q119: Security vs Delivery Trade-off — Expert Cost Redesign

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in security vs delivery trade-off. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via risk-tiered reviews → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 14:** Azure Security

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Security vs Delivery Trade-off gap; Resource Graph inventory of risk-tiered reviews, phased controls, exceptions.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on risk-tiered reviews.
Balance security requirements with delivery velocity. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for security vs delivery trade-off?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q120: Ransomware Resilience — Expert Standards Mediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in ransomware resilience. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via immutable backup → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 14:** Azure Security

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Ransomware Resilience gap; Resource Graph inventory of immutable backup, soft delete, Key Vault purge protection.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on immutable backup.
Azure architecture resilient to ransomware. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for ransomware resilience?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---
