# Week 14 — Intermediate Q&A

> Q031–Q070: Premium format (Week 1 quality).

---


## Q031: Defense in Depth Layers — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Defense in Depth Layers using identity in a Azure Security architecture review?

### Short Answer (30 seconds)

Use identity with perimeter; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Map defense-in-depth layers to azure controls.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Context:** Defense in Depth Layers is core to Azure Solution Architect interviews covering identity, perimeter, network, compute.

**Architect approach:**
1. Map business requirement to identity — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Map defense-in-depth layers to azure controls.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect map defense-in-depth layers to Azure controls — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to identity?**
2. **What KPI proves defense in depth layers adoption succeeded?**

### Common Mistakes in Interviews

- Listing identity without explaining trade-offs
- No Policy or IaC enforcement for defense in depth layers
- Skipping operational runbook for identity

---

## Q032: Defense in Depth Layers — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

**Intermediate:** Design production defense in depth layers for a 10-subscription enterprise (Azure Security).

### Short Answer (30 seconds)

Platform hosts shared identity; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Design:** Multi-subscription estate with platform vs application separation.
Shared identity and perimeter in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Map defense-in-depth layers to azure controls.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize defense in depth layers.

### Follow-up Questions

1. **How do Policy exemptions work during defense in depth layers migration?**
2. **What FinOps tag strategy supports defense in depth layers chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for identity testing
- Policies only at resource group — not MG

---

## Q033: Azure WAF Operations — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Azure WAF Operations using WAF detection/prevention in a Azure Security architecture review?

### Short Answer (30 seconds)

Use WAF detection/prevention with false positives; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Operate waf in detection then prevention with tuning.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Context:** Azure WAF Operations is core to Azure Solution Architect interviews covering WAF detection/prevention, false positives, custom rules.

**Architect approach:**
1. Map business requirement to WAF detection/prevention — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Operate waf in detection then prevention with tuning.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect operate WAF in detection then prevention with tuning — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to WAF detection/prevention?**
2. **What KPI proves azure waf operations adoption succeeded?**

### Common Mistakes in Interviews

- Listing WAF detection/prevention without explaining trade-offs
- No Policy or IaC enforcement for azure waf operations
- Skipping operational runbook for WAF detection/prevention

---

## Q034: Azure WAF Operations — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

**Intermediate:** Design production azure waf operations for a 10-subscription enterprise (Azure Security).

### Short Answer (30 seconds)

Platform hosts shared WAF detection/prevention; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Design:** Multi-subscription estate with platform vs application separation.
Shared WAF detection/prevention and false positives in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Operate waf in detection then prevention with tuning.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize azure waf operations.

### Follow-up Questions

1. **How do Policy exemptions work during azure waf operations migration?**
2. **What FinOps tag strategy supports azure waf operations chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for WAF detection/prevention testing
- Policies only at resource group — not MG

---

## Q035: Defender for Cloud — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Defender for Cloud using CSPM in a Azure Security architecture review?

### Short Answer (30 seconds)

Use CSPM with CWP; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Defender for cloud in continuous compliance governance.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Context:** Defender for Cloud is core to Azure Solution Architect interviews covering CSPM, CWP, secure score, regulatory compliance dashboard.

**Architect approach:**
1. Map business requirement to CSPM — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Defender for cloud in continuous compliance governance.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect Defender for Cloud in continuous compliance governance — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to CSPM?**
2. **What KPI proves defender for cloud adoption succeeded?**

### Common Mistakes in Interviews

- Listing CSPM without explaining trade-offs
- No Policy or IaC enforcement for defender for cloud
- Skipping operational runbook for CSPM

---

## Q036: Defender for Cloud — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

**Intermediate:** Design production defender for cloud for a 10-subscription enterprise (Azure Security).

### Short Answer (30 seconds)

Platform hosts shared CSPM; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Design:** Multi-subscription estate with platform vs application separation.
Shared CSPM and CWP in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Defender for cloud in continuous compliance governance.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize defender for cloud.

### Follow-up Questions

1. **How do Policy exemptions work during defender for cloud migration?**
2. **What FinOps tag strategy supports defender for cloud chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for CSPM testing
- Policies only at resource group — not MG

---

## Q037: Encryption Requirements — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Encryption Requirements using TLS 1.2+ in a Azure Security architecture review?

### Short Answer (30 seconds)

Use TLS 1.2+ with TDE; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Encryption strategy reducing compliance scope.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Context:** Encryption Requirements is core to Azure Solution Architect interviews covering TLS 1.2+, TDE, CMK, tokenization.

**Architect approach:**
1. Map business requirement to TLS 1.2+ — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Encryption strategy reducing compliance scope.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect encryption strategy reducing compliance scope — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to TLS 1.2+?**
2. **What KPI proves encryption requirements adoption succeeded?**

### Common Mistakes in Interviews

- Listing TLS 1.2+ without explaining trade-offs
- No Policy or IaC enforcement for encryption requirements
- Skipping operational runbook for TLS 1.2+

---

## Q038: Encryption Requirements — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

**Intermediate:** Design production encryption requirements for a 10-subscription enterprise (Azure Security).

### Short Answer (30 seconds)

Platform hosts shared TLS 1.2+; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Design:** Multi-subscription estate with platform vs application separation.
Shared TLS 1.2+ and TDE in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Encryption strategy reducing compliance scope.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize encryption requirements.

### Follow-up Questions

1. **How do Policy exemptions work during encryption requirements migration?**
2. **What FinOps tag strategy supports encryption requirements chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for TLS 1.2+ testing
- Policies only at resource group — not MG

---

## Q039: DevSecOps Pipeline — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DevSecOps |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply DevSecOps Pipeline using CodeQL in a Azure Security architecture review?

### Short Answer (30 seconds)

Use CodeQL with secret scan; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Security gates in golden ci/cd pipeline template.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Context:** DevSecOps Pipeline is core to Azure Solution Architect interviews covering CodeQL, secret scan, Bicep what-if, container scan.

**Architect approach:**
1. Map business requirement to CodeQL — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Security gates in golden ci/cd pipeline template.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect security gates in golden CI/CD pipeline template — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to CodeQL?**
2. **What KPI proves devsecops pipeline adoption succeeded?**

### Common Mistakes in Interviews

- Listing CodeQL without explaining trade-offs
- No Policy or IaC enforcement for devsecops pipeline
- Skipping operational runbook for CodeQL

---

## Q040: DevSecOps Pipeline — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DevSecOps |
| **Frequency** | Common |

### Question

**Intermediate:** Design production devsecops pipeline for a 10-subscription enterprise (Azure Security).

### Short Answer (30 seconds)

Platform hosts shared CodeQL; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Design:** Multi-subscription estate with platform vs application separation.
Shared CodeQL and secret scan in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Security gates in golden ci/cd pipeline template.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize devsecops pipeline.

### Follow-up Questions

1. **How do Policy exemptions work during devsecops pipeline migration?**
2. **What FinOps tag strategy supports devsecops pipeline chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for CodeQL testing
- Policies only at resource group — not MG

---

## Q041: OWASP API Security — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply OWASP API Security using BOLA in a Azure Security architecture review?

### Short Answer (30 seconds)

Use BOLA with authZ; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Api security beyond network perimeter with apim.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Context:** OWASP API Security is core to Azure Solution Architect interviews covering BOLA, authZ, rate limiting, APIM policies.

**Architect approach:**
1. Map business requirement to BOLA — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Api security beyond network perimeter with apim.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect API security beyond network perimeter with APIM — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to BOLA?**
2. **What KPI proves owasp api security adoption succeeded?**

### Common Mistakes in Interviews

- Listing BOLA without explaining trade-offs
- No Policy or IaC enforcement for owasp api security
- Skipping operational runbook for BOLA

---

## Q042: OWASP API Security — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

**Intermediate:** Design production owasp api security for a 10-subscription enterprise (Azure Security).

### Short Answer (30 seconds)

Platform hosts shared BOLA; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Design:** Multi-subscription estate with platform vs application separation.
Shared BOLA and authZ in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Api security beyond network perimeter with apim.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize owasp api security.

### Follow-up Questions

1. **How do Policy exemptions work during owasp api security migration?**
2. **What FinOps tag strategy supports owasp api security chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for BOLA testing
- Policies only at resource group — not MG

---

## Q043: Sentinel Incident Response — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Sentinel Incident Response using Sentinel in a Azure Security architecture review?

### Short Answer (30 seconds)

Use Sentinel with playbooks; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Security incident response on azure with sentinel.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Context:** Sentinel Incident Response is core to Azure Solution Architect interviews covering Sentinel, playbooks, SOAR, Key Vault exfiltration runbook.

**Architect approach:**
1. Map business requirement to Sentinel — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Security incident response on azure with sentinel.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect security incident response on Azure with Sentinel — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to Sentinel?**
2. **What KPI proves sentinel incident response adoption succeeded?**

### Common Mistakes in Interviews

- Listing Sentinel without explaining trade-offs
- No Policy or IaC enforcement for sentinel incident response
- Skipping operational runbook for Sentinel

---

## Q044: Sentinel Incident Response — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Common |

### Question

**Intermediate:** Design production sentinel incident response for a 10-subscription enterprise (Azure Security).

### Short Answer (30 seconds)

Platform hosts shared Sentinel; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Design:** Multi-subscription estate with platform vs application separation.
Shared Sentinel and playbooks in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Security incident response on azure with sentinel.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize sentinel incident response.

### Follow-up Questions

1. **How do Policy exemptions work during sentinel incident response migration?**
2. **What FinOps tag strategy supports sentinel incident response chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for Sentinel testing
- Policies only at resource group — not MG

---

## Q045: Azure Policy Security — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Azure Policy Security using deny public IP in a Azure Security architecture review?

### Short Answer (30 seconds)

Use deny public IP with require TLS; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Security policy initiatives at management group.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Context:** Azure Policy Security is core to Azure Solution Architect interviews covering deny public IP, require TLS, DINE diagnostics, Private Link.

**Architect approach:**
1. Map business requirement to deny public IP — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Security policy initiatives at management group.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect security policy initiatives at management group — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to deny public IP?**
2. **What KPI proves azure policy security adoption succeeded?**

### Common Mistakes in Interviews

- Listing deny public IP without explaining trade-offs
- No Policy or IaC enforcement for azure policy security
- Skipping operational runbook for deny public IP

---

## Q046: Azure Policy Security — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

**Intermediate:** Design production azure policy security for a 10-subscription enterprise (Azure Security).

### Short Answer (30 seconds)

Platform hosts shared deny public IP; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Design:** Multi-subscription estate with platform vs application separation.
Shared deny public IP and require TLS in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Security policy initiatives at management group.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize azure policy security.

### Follow-up Questions

1. **How do Policy exemptions work during azure policy security migration?**
2. **What FinOps tag strategy supports azure policy security chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for deny public IP testing
- Policies only at resource group — not MG

---

## Q047: Secrets Rotation — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Secrets Rotation using Key Vault rotation in a Azure Security architecture review?

### Short Answer (30 seconds)

Use Key Vault rotation with Entra SQL auth; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Automated secrets rotation without downtime.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Context:** Secrets Rotation is core to Azure Solution Architect interviews covering Key Vault rotation, Entra SQL auth, dual-user pattern.

**Architect approach:**
1. Map business requirement to Key Vault rotation — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Automated secrets rotation without downtime.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect automated secrets rotation without downtime — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to Key Vault rotation?**
2. **What KPI proves secrets rotation adoption succeeded?**

### Common Mistakes in Interviews

- Listing Key Vault rotation without explaining trade-offs
- No Policy or IaC enforcement for secrets rotation
- Skipping operational runbook for Key Vault rotation

---

## Q048: Secrets Rotation — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

**Intermediate:** Design production secrets rotation for a 10-subscription enterprise (Azure Security).

### Short Answer (30 seconds)

Platform hosts shared Key Vault rotation; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Design:** Multi-subscription estate with platform vs application separation.
Shared Key Vault rotation and Entra SQL auth in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Automated secrets rotation without downtime.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize secrets rotation.

### Follow-up Questions

1. **How do Policy exemptions work during secrets rotation migration?**
2. **What FinOps tag strategy supports secrets rotation chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for Key Vault rotation testing
- Policies only at resource group — not MG

---

## Q049: Managed Identity Blast Radius — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Managed Identity Blast Radius using MI RBAC scope in a Azure Security architecture review?

### Short Answer (30 seconds)

Use MI RBAC scope with compromised app containment; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Limit blast radius when compute is compromised.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Context:** Managed Identity Blast Radius is core to Azure Solution Architect interviews covering MI RBAC scope, compromised app containment.

**Architect approach:**
1. Map business requirement to MI RBAC scope — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Limit blast radius when compute is compromised.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect limit blast radius when compute is compromised — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to MI RBAC scope?**
2. **What KPI proves managed identity blast radius adoption succeeded?**

### Common Mistakes in Interviews

- Listing MI RBAC scope without explaining trade-offs
- No Policy or IaC enforcement for managed identity blast radius
- Skipping operational runbook for MI RBAC scope

---

## Q050: Managed Identity Blast Radius — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

**Intermediate:** Design production managed identity blast radius for a 10-subscription enterprise (Azure Security).

### Short Answer (30 seconds)

Platform hosts shared MI RBAC scope; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Design:** Multi-subscription estate with platform vs application separation.
Shared MI RBAC scope and compromised app containment in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Limit blast radius when compute is compromised.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize managed identity blast radius.

### Follow-up Questions

1. **How do Policy exemptions work during managed identity blast radius migration?**
2. **What FinOps tag strategy supports managed identity blast radius chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for MI RBAC scope testing
- Policies only at resource group — not MG

---

## Q051: Microsoft Purview — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compliance |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Microsoft Purview using data classification in a Azure Security architecture review?

### Short Answer (30 seconds)

Use data classification with DLP; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Data classification and compliance mapping.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Context:** Microsoft Purview is core to Azure Solution Architect interviews covering data classification, DLP, compliance manager.

**Architect approach:**
1. Map business requirement to data classification — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Data classification and compliance mapping.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect data classification and compliance mapping — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to data classification?**
2. **What KPI proves microsoft purview adoption succeeded?**

### Common Mistakes in Interviews

- Listing data classification without explaining trade-offs
- No Policy or IaC enforcement for microsoft purview
- Skipping operational runbook for data classification

---

## Q052: Microsoft Purview — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compliance |
| **Frequency** | Common |

### Question

**Intermediate:** Design production microsoft purview for a 10-subscription enterprise (Azure Security).

### Short Answer (30 seconds)

Platform hosts shared data classification; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Design:** Multi-subscription estate with platform vs application separation.
Shared data classification and DLP in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Data classification and compliance mapping.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize microsoft purview.

### Follow-up Questions

1. **How do Policy exemptions work during microsoft purview migration?**
2. **What FinOps tag strategy supports microsoft purview chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for data classification testing
- Policies only at resource group — not MG

---

## Q053: Network Segmentation Security — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Network Segmentation Security using micro-segmentation in a Azure Security architecture review?

### Short Answer (30 seconds)

Use micro-segmentation with Zero Trust network; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Network segmentation as security architecture.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Context:** Network Segmentation Security is core to Azure Solution Architect interviews covering micro-segmentation, Zero Trust network, Private Link.

**Architect approach:**
1. Map business requirement to micro-segmentation — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Network segmentation as security architecture.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect network segmentation as security architecture — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to micro-segmentation?**
2. **What KPI proves network segmentation security adoption succeeded?**

### Common Mistakes in Interviews

- Listing micro-segmentation without explaining trade-offs
- No Policy or IaC enforcement for network segmentation security
- Skipping operational runbook for micro-segmentation

---

## Q054: Network Segmentation Security — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

**Intermediate:** Design production network segmentation security for a 10-subscription enterprise (Azure Security).

### Short Answer (30 seconds)

Platform hosts shared micro-segmentation; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Design:** Multi-subscription estate with platform vs application separation.
Shared micro-segmentation and Zero Trust network in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Network segmentation as security architecture.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize network segmentation security.

### Follow-up Questions

1. **How do Policy exemptions work during network segmentation security migration?**
2. **What FinOps tag strategy supports network segmentation security chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for micro-segmentation testing
- Policies only at resource group — not MG

---

## Q055: Threat Modeling STRIDE — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Threat Modeling STRIDE using STRIDE in a Azure Security architecture review?

### Short Answer (30 seconds)

Use STRIDE with trust boundaries; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Stride threat modeling in architecture review.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Context:** Threat Modeling STRIDE is core to Azure Solution Architect interviews covering STRIDE, trust boundaries, DFD, mitigation verification.

**Architect approach:**
1. Map business requirement to STRIDE — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Stride threat modeling in architecture review.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect STRIDE threat modeling in architecture review — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to STRIDE?**
2. **What KPI proves threat modeling stride adoption succeeded?**

### Common Mistakes in Interviews

- Listing STRIDE without explaining trade-offs
- No Policy or IaC enforcement for threat modeling stride
- Skipping operational runbook for STRIDE

---

## Q056: Threat Modeling STRIDE — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

**Intermediate:** Design production threat modeling stride for a 10-subscription enterprise (Azure Security).

### Short Answer (30 seconds)

Platform hosts shared STRIDE; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Design:** Multi-subscription estate with platform vs application separation.
Shared STRIDE and trust boundaries in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Stride threat modeling in architecture review.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize threat modeling stride.

### Follow-up Questions

1. **How do Policy exemptions work during threat modeling stride migration?**
2. **What FinOps tag strategy supports threat modeling stride chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for STRIDE testing
- Policies only at resource group — not MG

---

## Q057: Security Benchmark Initiative — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Security Benchmark Initiative using Azure Security Benchmark in a Azure Security architecture review?

### Short Answer (30 seconds)

Use Azure Security Benchmark with CIS; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Assign and remediate security benchmark policies.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Context:** Security Benchmark Initiative is core to Azure Solution Architect interviews covering Azure Security Benchmark, CIS, custom initiatives.

**Architect approach:**
1. Map business requirement to Azure Security Benchmark — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Assign and remediate security benchmark policies.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect assign and remediate security benchmark policies — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to Azure Security Benchmark?**
2. **What KPI proves security benchmark initiative adoption succeeded?**

### Common Mistakes in Interviews

- Listing Azure Security Benchmark without explaining trade-offs
- No Policy or IaC enforcement for security benchmark initiative
- Skipping operational runbook for Azure Security Benchmark

---

## Q058: Security Benchmark Initiative — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

**Intermediate:** Design production security benchmark initiative for a 10-subscription enterprise (Azure Security).

### Short Answer (30 seconds)

Platform hosts shared Azure Security Benchmark; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Design:** Multi-subscription estate with platform vs application separation.
Shared Azure Security Benchmark and CIS in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Assign and remediate security benchmark policies.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize security benchmark initiative.

### Follow-up Questions

1. **How do Policy exemptions work during security benchmark initiative migration?**
2. **What FinOps tag strategy supports security benchmark initiative chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for Azure Security Benchmark testing
- Policies only at resource group — not MG

---

## Q059: Pen Test and Red Team — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Pen Test and Red Team using penetration testing in a Azure Security architecture review?

### Short Answer (30 seconds)

Use penetration testing with Microsoft rules of engagement; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Pre-production security validation approach.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Context:** Pen Test and Red Team is core to Azure Solution Architect interviews covering penetration testing, Microsoft rules of engagement.

**Architect approach:**
1. Map business requirement to penetration testing — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Pre-production security validation approach.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect pre-production security validation approach — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to penetration testing?**
2. **What KPI proves pen test and red team adoption succeeded?**

### Common Mistakes in Interviews

- Listing penetration testing without explaining trade-offs
- No Policy or IaC enforcement for pen test and red team
- Skipping operational runbook for penetration testing

---

## Q060: Pen Test and Red Team — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

**Intermediate:** Design production pen test and red team for a 10-subscription enterprise (Azure Security).

### Short Answer (30 seconds)

Platform hosts shared penetration testing; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Design:** Multi-subscription estate with platform vs application separation.
Shared penetration testing and Microsoft rules of engagement in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Pre-production security validation approach.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize pen test and red team.

### Follow-up Questions

1. **How do Policy exemptions work during pen test and red team migration?**
2. **What FinOps tag strategy supports pen test and red team chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for penetration testing testing
- Policies only at resource group — not MG

---

## Q061: Container Security — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DevSecOps |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Container Security using ACR scanning in a Azure Security architecture review?

### Short Answer (30 seconds)

Use ACR scanning with AKS Defender; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Container supply chain and runtime security.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Context:** Container Security is core to Azure Solution Architect interviews covering ACR scanning, AKS Defender, pod security, network policies.

**Architect approach:**
1. Map business requirement to ACR scanning — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Container supply chain and runtime security.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect container supply chain and runtime security — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to ACR scanning?**
2. **What KPI proves container security adoption succeeded?**

### Common Mistakes in Interviews

- Listing ACR scanning without explaining trade-offs
- No Policy or IaC enforcement for container security
- Skipping operational runbook for ACR scanning

---

## Q062: Container Security — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DevSecOps |
| **Frequency** | Common |

### Question

**Intermediate:** Design production container security for a 10-subscription enterprise (Azure Security).

### Short Answer (30 seconds)

Platform hosts shared ACR scanning; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Design:** Multi-subscription estate with platform vs application separation.
Shared ACR scanning and AKS Defender in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Container supply chain and runtime security.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize container security.

### Follow-up Questions

1. **How do Policy exemptions work during container security migration?**
2. **What FinOps tag strategy supports container security chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for ACR scanning testing
- Policies only at resource group — not MG

---

## Q063: SIEM and Log Retention — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply SIEM and Log Retention using Sentinel in a Azure Security architecture review?

### Short Answer (30 seconds)

Use Sentinel with Log Analytics retention; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Siem architecture meeting retention and detection needs.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Context:** SIEM and Log Retention is core to Azure Solution Architect interviews covering Sentinel, Log Analytics retention, audit requirements.

**Architect approach:**
1. Map business requirement to Sentinel — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Siem architecture meeting retention and detection needs.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect SIEM architecture meeting retention and detection needs — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to Sentinel?**
2. **What KPI proves siem and log retention adoption succeeded?**

### Common Mistakes in Interviews

- Listing Sentinel without explaining trade-offs
- No Policy or IaC enforcement for siem and log retention
- Skipping operational runbook for Sentinel

---

## Q064: SIEM and Log Retention — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Common |

### Question

**Intermediate:** Design production siem and log retention for a 10-subscription enterprise (Azure Security).

### Short Answer (30 seconds)

Platform hosts shared Sentinel; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Design:** Multi-subscription estate with platform vs application separation.
Shared Sentinel and Log Analytics retention in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Siem architecture meeting retention and detection needs.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize siem and log retention.

### Follow-up Questions

1. **How do Policy exemptions work during siem and log retention migration?**
2. **What FinOps tag strategy supports siem and log retention chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for Sentinel testing
- Policies only at resource group — not MG

---

## Q065: Compliance Evidence — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compliance |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Compliance Evidence using SOC2 evidence in a Azure Security architecture review?

### Short Answer (30 seconds)

Use SOC2 evidence with policy assignment IDs; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Collect compliance evidence from azure controls.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Context:** Compliance Evidence is core to Azure Solution Architect interviews covering SOC2 evidence, policy assignment IDs, audit trail.

**Architect approach:**
1. Map business requirement to SOC2 evidence — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Collect compliance evidence from azure controls.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect collect compliance evidence from Azure controls — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to SOC2 evidence?**
2. **What KPI proves compliance evidence adoption succeeded?**

### Common Mistakes in Interviews

- Listing SOC2 evidence without explaining trade-offs
- No Policy or IaC enforcement for compliance evidence
- Skipping operational runbook for SOC2 evidence

---

## Q066: Compliance Evidence — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compliance |
| **Frequency** | Common |

### Question

**Intermediate:** Design production compliance evidence for a 10-subscription enterprise (Azure Security).

### Short Answer (30 seconds)

Platform hosts shared SOC2 evidence; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Design:** Multi-subscription estate with platform vs application separation.
Shared SOC2 evidence and policy assignment IDs in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Collect compliance evidence from azure controls.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize compliance evidence.

### Follow-up Questions

1. **How do Policy exemptions work during compliance evidence migration?**
2. **What FinOps tag strategy supports compliance evidence chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for SOC2 evidence testing
- Policies only at resource group — not MG

---

## Q067: Security vs Delivery Trade-off — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Security vs Delivery Trade-off using risk-tiered reviews in a Azure Security architecture review?

### Short Answer (30 seconds)

Use risk-tiered reviews with phased controls; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Balance security requirements with delivery velocity.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Context:** Security vs Delivery Trade-off is core to Azure Solution Architect interviews covering risk-tiered reviews, phased controls, exceptions.

**Architect approach:**
1. Map business requirement to risk-tiered reviews — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Balance security requirements with delivery velocity.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect balance security requirements with delivery velocity — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to risk-tiered reviews?**
2. **What KPI proves security vs delivery trade-off adoption succeeded?**

### Common Mistakes in Interviews

- Listing risk-tiered reviews without explaining trade-offs
- No Policy or IaC enforcement for security vs delivery trade-off
- Skipping operational runbook for risk-tiered reviews

---

## Q068: Security vs Delivery Trade-off — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

**Intermediate:** Design production security vs delivery trade-off for a 10-subscription enterprise (Azure Security).

### Short Answer (30 seconds)

Platform hosts shared risk-tiered reviews; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Design:** Multi-subscription estate with platform vs application separation.
Shared risk-tiered reviews and phased controls in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Balance security requirements with delivery velocity.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize security vs delivery trade-off.

### Follow-up Questions

1. **How do Policy exemptions work during security vs delivery trade-off migration?**
2. **What FinOps tag strategy supports security vs delivery trade-off chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for risk-tiered reviews testing
- Policies only at resource group — not MG

---

## Q069: Ransomware Resilience — Fundamentals

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

**Intermediate:** How do you apply Ransomware Resilience using immutable backup in a Azure Security architecture review?

### Short Answer (30 seconds)

Use immutable backup with soft delete; document trade-offs in ADR; verify via load test, Policy scan, or DR drill. Azure architecture resilient to ransomware.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Context:** Ransomware Resilience is core to Azure Solution Architect interviews covering immutable backup, soft delete, Key Vault purge protection.

**Architect approach:**
1. Map business requirement to immutable backup — reject alternatives with explicit rationale
2. Evaluate cost, security, and operational complexity in decision matrix
3. Enforce via Bicep module + Azure Policy at management group scope
4. Define verification: metrics, compliance dashboard, or game day

**Production pattern:** Platform golden-path IaC module; app teams deploy via pipeline.
Azure architecture resilient to ransomware.

**Anti-pattern:** Portal-only configuration without IaC, Policy, or runbook ownership.

### Architecture Perspective

Interviewers expect Azure architecture resilient to ransomware — not generic 'use Azure' answers.

### Follow-up Questions

1. **When would you choose an alternative to immutable backup?**
2. **What KPI proves ransomware resilience adoption succeeded?**

### Common Mistakes in Interviews

- Listing immutable backup without explaining trade-offs
- No Policy or IaC enforcement for ransomware resilience
- Skipping operational runbook for immutable backup

---

## Q070: Ransomware Resilience — Production Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

**Intermediate:** Design production ransomware resilience for a 10-subscription enterprise (Azure Security).

### Short Answer (30 seconds)

Platform hosts shared immutable backup; workload subs inherit Policy; RBAC least privilege for CI/CD; central Log Analytics for audit.

### Detailed Answer (3–5 minutes)

**Difficulty:** Intermediate | **Week 14:** Azure Security

**Design:** Multi-subscription estate with platform vs application separation.
Shared immutable backup and soft delete in platform subscription; spokes consume via private connectivity.

**Governance:** Mandatory tags (Environment, CostCenter, Owner); Policy initiative at prod MG;
custom RBAC roles for pipeline service principals — not Contributor on subscription.

**Trade-offs:** Central control improves audit evidence; time-bound ADR exceptions for urgent delivery.
Azure architecture resilient to ransomware.

**Deliverables:** Reference architecture, IaC module, review checklist item, on-call runbook stub.

### Architecture Perspective

Production design questions test whether you can operationalize ransomware resilience.

### Follow-up Questions

1. **How do Policy exemptions work during ransomware resilience migration?**
2. **What FinOps tag strategy supports ransomware resilience chargeback?**

### Common Mistakes in Interviews

- Single subscription for all prod workloads
- No nonprod isolation for immutable backup testing
- Policies only at resource group — not MG

---
