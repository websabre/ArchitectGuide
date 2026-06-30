# Week 12 — Expert Scenario Q&A

> Q101–Q120: Premium format (Week 1 quality).

---


## Q101: Entra ID Architecture — Expert Incident Response

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in entra id architecture. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via Entra ID → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 12:** Azure Identity

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Entra ID Architecture gap; Resource Graph inventory of Entra ID, hybrid identity, Entra Connect, cloud-only.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on Entra ID.
Entra id as identity plane for all new azure applications. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for entra id architecture?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q102: Managed Identity Patterns — Expert Audit Remediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in managed identity patterns. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via system vs user-assigned → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 12:** Azure Identity

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Managed Identity Patterns gap; Resource Graph inventory of system vs user-assigned, cross-resource, slot swap.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on system vs user-assigned.
Managed identity standard for all azure compute resources. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for managed identity patterns?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q103: OAuth and OIDC Flows — Expert Cost Redesign

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in oauth and oidc flows. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via auth code PKCE → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 12:** Azure Identity

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to OAuth and OIDC Flows gap; Resource Graph inventory of auth code PKCE, client credentials, OBO, token validation.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on auth code PKCE.
Correct oauth flow per client type and service chain. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for oauth and oidc flows?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q104: Conditional Access Design — Expert Standards Mediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in conditional access design. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via CA policies → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 12:** Azure Identity

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Conditional Access Design gap; Resource Graph inventory of CA policies, MFA, compliant device, sign-in risk.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on CA policies.
Conditional access policies by persona with break-glass monitoring. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for conditional access design?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q105: Key Vault Architecture — Expert Incident Response

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in key vault architecture. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via vault per environment → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 12:** Azure Identity

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Key Vault Architecture gap; Resource Graph inventory of vault per environment, RBAC, soft delete, private endpoint.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on vault per environment.
Key vault topology with rotation and purge protection. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for key vault architecture?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q106: Zero Trust on Azure — Expert Audit Remediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in zero trust on azure. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via verify explicitly → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 12:** Azure Identity

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Zero Trust on Azure gap; Resource Graph inventory of verify explicitly, least privilege, assume breach, Private Link.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on verify explicitly.
Zero trust implementation on landing zone. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for zero trust on azure?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q107: PIM and JIT Access — Expert Cost Redesign

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in pim and jit access. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via PIM → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 12:** Azure Identity

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to PIM and JIT Access gap; Resource Graph inventory of PIM, eligible assignments, approval workflow, audit.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on PIM.
Just-in-time admin access replacing standing privileges. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for pim and jit access?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q108: CI/CD OIDC Federation — Expert Standards Mediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in ci/cd oidc federation. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via GitHub Actions OIDC → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 12:** Azure Identity

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to CI/CD OIDC Federation gap; Resource Graph inventory of GitHub Actions OIDC, federated credentials, workload identity.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on GitHub Actions OIDC.
Eliminate long-lived sp secrets in pipelines with oidc. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for ci/cd oidc federation?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q109: B2B and B2C Identity — Expert Incident Response

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in b2b and b2c identity. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via Entra External ID → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 12:** Azure Identity

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to B2B and B2C Identity gap; Resource Graph inventory of Entra External ID, B2C, guest users, tenant isolation.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on Entra External ID.
Separate workforce and customer identity architectures. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for b2b and b2c identity?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q110: On-Behalf-Of Flow — Expert Audit Remediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in on-behalf-of flow. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via OBO → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 12:** Azure Identity

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to On-Behalf-Of Flow gap; Resource Graph inventory of OBO, downstream API, token cache, chained calls.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on OBO.
Obo for microservices preserving user context. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for on-behalf-of flow?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q111: App Registration Governance — Expert Cost Redesign

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in app registration governance. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via app registrations → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 12:** Azure Identity

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to App Registration Governance gap; Resource Graph inventory of app registrations, API permissions, admin consent.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on app registrations.
Govern app registrations and permission grants at scale. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for app registration governance?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q112: Entra ID Protection — Expert Standards Mediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in entra id protection. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via risk policies → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 12:** Azure Identity

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Entra ID Protection gap; Resource Graph inventory of risk policies, passwordless, FIDO2, MFA fatigue.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on risk policies.
Identity protection against credential attacks. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for entra id protection?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q113: Service Principal vs MI — Expert Incident Response

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in service principal vs mi. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via service principals → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 12:** Azure Identity

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Service Principal vs MI gap; Resource Graph inventory of service principals, managed identity, workload identity.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on service principals.
When sp vs mi for automation and application identity. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for service principal vs mi?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q114: Hybrid Identity Sync — Expert Audit Remediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in hybrid identity sync. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via Entra Connect → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 12:** Azure Identity

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Hybrid Identity Sync gap; Resource Graph inventory of Entra Connect, cloud sync, password hash sync, PTA.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on Entra Connect.
Hybrid identity for enterprises with on-prem ad. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for hybrid identity sync?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q115: Certificate Management — Expert Cost Redesign

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in certificate management. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via Key Vault certificates → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 12:** Azure Identity

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Certificate Management gap; Resource Graph inventory of Key Vault certificates, auto-renew, App Service certs.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on Key Vault certificates.
Tls certificate lifecycle on azure. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for certificate management?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q116: Entra Domain Services — Expert Standards Mediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in entra domain services. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via Entra DS → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 12:** Azure Identity

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Entra Domain Services gap; Resource Graph inventory of Entra DS, LDAP apps, lift-and-shift legacy auth.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on Entra DS.
Entra domain services for legacy ldap without new ad ds vms. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for entra domain services?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q117: Identity for APIM — Expert Incident Response

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in identity for apim. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via JWT validation → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 12:** Azure Identity

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Identity for APIM gap; Resource Graph inventory of JWT validation, OAuth at gateway, subscription keys.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on JWT validation.
Identity enforcement at apim edge. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for identity for apim?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q118: Privileged Access Workstations — Expert Audit Remediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in privileged access workstations. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via PAW → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 12:** Azure Identity

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Privileged Access Workstations gap; Resource Graph inventory of PAW, admin separation, Conditional Access for admins.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on PAW.
Secure admin access architecture. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for privileged access workstations?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q119: Token Lifetime and Refresh — Expert Cost Redesign

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in token lifetime and refresh. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via refresh tokens → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 12:** Azure Identity

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Token Lifetime and Refresh gap; Resource Graph inventory of refresh tokens, session management, CAE.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on refresh tokens.
Token lifecycle design for spas and mobile apps. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for token lifetime and refresh?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---

## Q120: Identity Incident Response — Expert Standards Mediation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

**Expert scenario:** You are lead architect: a Sev-1 incident exposes gaps in identity incident response. Executives want remediation in 30 days with zero downtime.

### Short Answer (30 seconds)

Stabilize → root-cause via token revocation → IaC + Policy fix → governance update; weekly exec comms.

### Detailed Answer

**Difficulty:** Expert | **Week 12:** Azure Identity

**Day 1–3:** Incident command; preserve Activity Log; contain blast radius; customer comms.
**Week 1:** Root-cause mapped to Identity Incident Response gap; Resource Graph inventory of token revocation, CA policy, session invalidate.
**Weeks 2–3:** IaC fix via pipeline; Policy DeployIfNotExists; nonprod load/failover test; phased prod rollout.
**Week 4+:** Update review checklist; supersede ADR; game day; train teams on token revocation.
Identity incident containment runbook. Weekly executive risk burndown.

### Architecture Perspective

Expert scenarios test leadership under pressure.

### Follow-up Questions

1. **Rollback plan if fix causes regression?**
2. **Policy deny vs runbook-only for identity incident response?**

### Common Mistakes in Interviews

- Big-bang production change under deadline
- Symptom fix without governance update
- No stakeholder communication plan

---
