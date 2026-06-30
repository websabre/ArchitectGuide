# Week 14 — Intermediate Q&A

> Q001–Q050: Premium format (Week 1 quality).  
> **Topic:** Azure Security | **Count:** 50

---


## Q001: Defense in Depth on Azure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Map defense in depth layers for Azure web application.

### Short Answer (30 seconds)

Identity (Entra, CA) → Perimeter (Front Door, WAF) → Network (NSG, Private Link) → Compute (patching, Defender) → Data (TDE, CMK) → App (input validation).

### Detailed Answer (3–5 minutes)

Each layer independent failure — WAF bypass still hits NSG and authZ.

**Architect:** Threat model STRIDE per layer — document controls.

### Architecture Perspective

Layered security is WAF pillar implementation.

### Follow-up Questions

1. **Which layer stops SQL injection? — App validation + parameterized queries + WAF.**
2. **Shared responsibility model? — Customer secures app and data; Microsoft secures platform.**

### Common Mistakes in Interviews

- Single security product 'does it all'
- Ignore app layer validation
- Public data plane endpoints

---

## Q002: Azure WAF Rules

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

WAF false positives blocking legitimate traffic — approach?

### Short Answer (30 seconds)

Start detection mode, tune exclusions for known false positives, custom rules for rate limit, move to prevention after 2 weeks baseline.

### Detailed Answer (3–5 minutes)

**Managed rule sets:** OWASP 3.2 baseline. **Geo-block** if business allows.

**Architect:** WAF logs to Log Analytics — correlate blocked requests with support tickets.

### Architecture Perspective

WAF operations realism impresses interviewers.

### Follow-up Questions

1. **Custom rule example? — Block countries except operating regions.**
2. **Bot protection? — Front Door Premium bot manager.**

### Common Mistakes in Interviews

- Prevention mode day one — blocks customers
- Disable rules causing false positives globally
- No WAF log analysis

---

## Q003: Microsoft Defender for Cloud

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

How use Defender for Cloud in architecture governance?

### Short Answer (30 seconds)

Secure score tracks posture. Enable Defender plans (Servers, SQL, Storage, Key Vault). Regulatory compliance dashboard maps to SOC2/ISO.

### Detailed Answer (3–5 minutes)

**CI/CD:** Defender for DevOps scans IaC and secrets in repos.

**Architect:** Weekly secure score review in platform team — block deploy on critical findings.

### Architecture Perspective

Defender is continuous compliance monitoring.

### Follow-up Questions

1. **Agentless scanning? — VM scanning without agent — preview features evolve.**
2. **CSPM vs CWP? — Posture management vs workload protection.**

### Common Mistakes in Interviews

- Defender disabled for cost
- Critical alerts unmonitored
- No owner for recommendations

---

## Q004: Encryption at Rest and Transit

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Encryption requirements for PCI workload on Azure?

### Short Answer (30 seconds)

TLS 1.2+ in transit. TDE at rest all data stores. CMK if PCI DSS requires key custody. Always Encrypted for cardholder data fields if stored.

### Detailed Answer (3–5 minutes)

**Better:** tokenization — Stripe/Adyen — card data never touches your DB.

**Architect:** Scope reduction beats encryption complexity.

### Architecture Perspective

PCI scope reduction is architect-first answer.

### Follow-up Questions

1. **Certificate management? — Key Vault auto-renew or App Service managed cert.**
2. **Internal TLS? — mTLS service mesh for east-west.**

### Common Mistakes in Interviews

- PAN stored encrypted in your SQL
- TLS 1.0 enabled
- Self-signed certs production

---

## Q005: Managed Identity Security

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Common |

### Question

Compromised App Service — blast radius with managed identity?

### Short Answer (30 seconds)

MI limited to RBAC granted — scope MI to minimum resources. Separate MI per app. Monitor MI authentication logs in Entra sign-in logs.

### Detailed Answer (3–5 minutes)

**Rotation:** no secret to steal — attacker uses MI from compromised app — containment via RBAC scope and network isolation.

### Architecture Perspective

MI reduces but doesn't eliminate blast radius.

### Follow-up Questions

1. **Audit MI permissions? — Quarterly access review.**
2. **Disable MI when not needed? — Delete user-assigned MI explicitly.**

### Common Mistakes in Interviews

- MI Contributor on subscription
- Shared MI across unrelated apps
- No logging on MI token requests

---

## Q006: DevSecOps on Azure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DevSecOps |
| **Frequency** | Common |

### Question

Security scanning in GitHub Actions pipeline for Bicep and .NET?

### Short Answer (30 seconds)

CodeQL SAST, secret scanning, Bicep what-if + defender for IaC, container Trivy scan, deploy to staging, OWASP ZAP DAST optional.

### Detailed Answer (3–5 minutes)

**Quality gates:** block merge on critical CVE, failed secret scan, policy what-if deny.

**Architect:** Golden pipeline template all teams inherit.

### Architecture Perspective

Shift-left security is architect pipeline design.

### Follow-up Questions

1. **SBOM generation? — Supply chain security — export on release.**
2. **Signed commits? — Optional enhanced integrity.**

### Common Mistakes in Interviews

- Deploy without vulnerability scan
- Secrets in Bicep parameters file in git
- No IaC policy validation

---

## Q007: OWASP API Security Top 10

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Top API risks for Azure APIM-protected API?

### Short Answer (30 seconds)

BOLA (broken object level authZ), authN failures, excessive data exposure, rate limiting missing, misconfiguration.

### Detailed Answer (3–5 minutes)

**Mitigations:** authZ on every resource ID, APIM rate limits, JWT validation, response filtering, audit logging.

**Architect:** Threat model each public API endpoint.

### Architecture Perspective

API security beyond network WAF.

### Follow-up Questions

1. **APIM validate JWT? — `validate-jwt` policy — issuer, audience, signature.**
2. **Subscription keys enough? — Not without per-user authZ — keys are coarse.**

### Common Mistakes in Interviews

- Trust client to filter data
- No object-level authZ
- APIM as only security layer

---

## Q008: Security Incident Response on Azure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Operations |
| **Frequency** | Common |

### Question

Suspected Key Vault secret exfiltration — steps?

### Short Answer (30 seconds)

Rotate secrets immediately, review Key Vault diagnostic logs, Entra sign-in logs for MI/SP, isolate compromised resource, Sentinel incident, preserve evidence.

### Detailed Answer (3–5 minutes)

**Runbook:** detection → containment → eradication → recovery → lessons learned.

**Architect:** Pre-document contacts, rotation automation, break-glass procedure.

### Architecture Perspective

Incident response shows operational maturity.

### Follow-up Questions

1. **Sentinel automation? — Playbooks automate containment.**
2. **Communication plan? — Legal/comms for breach notification.**

### Common Mistakes in Interviews

- No secret rotation runbook
- Delete logs during incident
- No forensic snapshot

---

## Q009: Azure Policy for Security

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

Policies to enforce security baseline?

### Short Answer (30 seconds)

Deny public IP on VMs, require TLS on Storage, deploy diagnostic settings, require Private Link for SQL, allowed locations only.

### Detailed Answer (3–5 minutes)

**Initiative:** assign 'Azure Security Benchmark' or custom SOC2 initiative to prod MG.

**Exemptions:** documented with expiry — not permanent bypass.

### Architecture Perspective

Policy encodes security architecture at scale.

### Follow-up Questions

1. **DeployIfNotExists diagnostic? — Auto-configure logging — critical for audit.**
2. **Guest configuration? — VM baseline settings — Azure Policy machine config.**

### Common Mistakes in Interviews

- Manual compliance checks quarterly
- Permanent policy exemptions
- Audit-only policies never remediated

---

## Q010: Secrets Rotation Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Automate SQL password rotation without downtime?

### Short Answer (30 seconds)

Dual-user pattern or Entra ID auth for SQL (no password). Key Vault rotation function updates secret, App Service picks up on restart/refresh.

### Detailed Answer (3–5 minutes)

**Best:** Entra authentication for SQL — eliminate SQL password entirely.

**Architect:** Rotation runbook tested — quarterly game day.

### Architecture Perspective

Rotation architecture prevents stale credential incidents.

### Follow-up Questions

1. **Event Grid Key Vault rotation? — Near-expiry cert alerts.**
2. **Blue-green for secret-dependent deploy? — Staging slot tests new secret.**

### Common Mistakes in Interviews

- Password never rotated 3 years
- Manual rotation during business hours only
- Single SQL login shared by all apps

---

## Q011: Microsoft Defender for Cloud

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

How integrate Defender for Cloud into architecture governance?

### Short Answer (30 seconds)

Enable Defender CSPM + workload plans (Servers, SQL, Storage, App Service). Secure score tracks posture. Critical recommendations block deploy via policy/CI gate.

### Detailed Answer (3–5 minutes)

**Architect workflow:**
- Weekly secure score review in platform team
- Regulatory compliance dashboard mapped to SOC2/ISO
- Agentless and agent-based scanning per workload

**Integration:** Export to Sentinel for correlation; assign recommendation owners in workload teams.

### Architecture Perspective

Defender for Cloud is continuous compliance not point-in-time audit.

### Follow-up Questions

1. **Defender CSPM vs CWP? — CSPM posture; CWP runtime threat protection per plan.**
2. **Defender for DevOps? — Scan IaC and secrets in GitHub/Azure DevOps repos.**

### Common Mistakes in Interviews

- Defender disabled in prod to save cost
- Critical findings with no owner
- Secure score ignored in architecture review

---

## Q012: Defender for App Service

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Defender for App Service detects what threats?

### Short Answer (30 seconds)

Cryptomining, suspicious IP access, MITM indicators, environment variable theft, communication with malicious IPs — runtime anomaly on App Service.

### Detailed Answer (3–5 minutes)

**Architect:** Enable on all internet-facing App Services. Pair with WAF and Private Link. Alerts to Sentinel playbook for auto-disable site on critical.

### Architecture Perspective

Runtime PaaS protection beyond network perimeter.

### Follow-up Questions

1. **Defender App Service vs WAF? — Defender runtime anomalies; WAF request inspection.**
2. **Enable on Functions? — Separate Defender plan for App Service covers Functions on same plan tier.**

### Common Mistakes in Interviews

- App Service public with Defender only defense
- Ignore Defender alerts as false positives
- No integration with incident response

---

## Q013: Defender for SQL

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Defender for SQL vulnerability assessment workflow?

### Short Answer (30 seconds)

Weekly scan for misconfigurations ( excessive permissions, TDE off), surface results in Defender portal, remediate via baseline template, track in secure score.

### Detailed Answer (3–5 minutes)

**Architect:** Enable Advanced Threat Protection alerts (SQL injection, anomalous access). VA results feed CI/CD — fail deploy if critical on prod.

**Managed Instance + SQL DB:** Same Defender SQL plan.

### Architecture Perspective

Database security is layered — TDE + Defender + network.

### Follow-up Questions

1. **ATP vs VA? — ATP real-time threats; VA configuration baseline.**
2. **Azure SQL vs SQL on VM? — Defender for SQL covers PaaS; Servers plan for IaaS.**

### Common Mistakes in Interviews

- Public SQL endpoint with VA only
- VA critical findings unremediated months
- No alert routing for SQL injection attempt

---

## Q014: Defender for Storage

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Defender for Storage — key detections?

### Short Answer (30 seconds)

Unusual access patterns, malware upload, anonymous access enabled, suspicious IP geographies accessing blobs.

### Detailed Answer (3–5 minutes)

**Architect:** Enable on storage with sensitive data. Malware scanning on upload for user content buckets. Restrict to Private Link + disable public blob access via policy.

### Architecture Perspective

Storage is exfiltration target — Defender adds anomaly layer.

### Follow-up Questions

1. **Malware scanning vs Defender? — On-upload scan feature complement detections.**
2. **Storage analytics logs? — Enable for forensic correlation.**

### Common Mistakes in Interviews

- Public containers with sensitive data
- Defender Storage disabled for cost
- No alert on anonymous access detection

---

## Q015: Security Score Improvement

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

Raise secure score from 45% to 80% — prioritized approach?

### Short Answer (30 seconds)

Fix critical/high recommendations affecting score weight first: MFA, external exposure, unpatched CVEs, missing encryption. Assign owners per subscription.

### Detailed Answer (3–5 minutes)

**Architect:**
1. Export recommendations to spreadsheet/work item tracker
2. Quick wins: disable public access, enable MFA, diagnostic logs
3. Policy DeployIfNotExists for recurring gaps

Track weekly score trend — not one-time project.

### Architecture Perspective

Secure score prioritization shows operational security leadership.

### Follow-up Questions

1. **Score vs compliance? — Score is Microsoft best practices; compliance adds regulatory controls.**
2. **Exemptions? — Document risk acceptance for impossible fixes.**

### Common Mistakes in Interviews

- Chasing 100% score ignoring business risk
- Fix low-impact items first for vanity score
- No score tracking over time

---

## Q016: Regulatory Compliance Dashboard

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compliance |
| **Frequency** | Common |

### Question

Use Defender regulatory compliance dashboard for SOC 2?

### Short Answer (30 seconds)

Maps Azure Security Benchmark and regulatory standards to control pass/fail. Drill into failing controls → linked recommendations → remediation.

### Detailed Answer (3–5 minutes)

**Architect:** Export compliance PDF for auditors quarterly. Custom initiative for org-specific controls. Not replacement for formal audit — evidence accelerator.

### Architecture Perspective

Compliance dashboard bridges engineering and audit conversations.

### Follow-up Questions

1. **SOC2 vs ISO27001 in dashboard? — Select standard — overlapping controls deduplicated.**
2. **Custom compliance standard? — Import custom policy initiative mapped to controls.**

### Common Mistakes in Interviews

- Assume green dashboard equals audit pass
- No evidence collection for control
- Compliance only checked before audit season

---

## Q017: Key Vault Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Design Key Vault topology for 10 microservices?

### Short Answer (30 seconds)

Separate vault per environment (prod/nonprod) or per data classification — not one vault all secrets. RBAC not access policies. Private Link + diagnostic logs.

### Detailed Answer (3–5 minutes)

**Patterns:**
- Platform vault: infra secrets
- App vault per bounded context: app-specific connection strings
- Purge protection + soft delete on prod

**Architect:** Managed identity access only — no secrets in pipeline variables.

### Architecture Perspective

Key Vault topology prevents blast radius on compromise.

### Follow-up Questions

1. **Vault per app vs per env? — Trade isolation vs operational overhead — document standard.**
2. **HSM-backed keys? — Premium/Managed HSM for CMK requiring FIPS 140-2 Level 3.**

### Common Mistakes in Interviews

- Single vault all environments
- Access policies with broad secrets get/list
- Key Vault public endpoint production

---

## Q018: HSM vs Software Keys

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

When HSM-backed keys vs software keys in Key Vault?

### Short Answer (30 seconds)

HSM (Premium vault or Managed HSM): regulatory FIPS 140-2 Level 3, CMK for SQL/Storage with hardware protection. Software keys: dev, lower classification, cost sensitive.

### Detailed Answer (3–5 minutes)

**Architect:** PCI/HIPAA workloads → HSM CMK. Rotation and access audit identical — key material non-exportable for HSM.

**Cost:** HSM premium — justify per data classification policy.

### Architecture Perspective

Key backing choice is compliance architecture decision.

### Follow-up Questions

1. **Managed HSM vs Key Vault Premium HSM? — Managed HSM dedicated HSM pool; Premium shared.**
2. **BYOK? — Bring your own key to HSM — key never leaves your control.**

### Common Mistakes in Interviews

- Software keys for PCI CMK requirement
- Exportable private keys in production
- No key access audit logging

---

## Q019: Managed HSM

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Occasional |

### Question

Azure Managed HSM vs Key Vault Premium — selection?

### Short Answer (30 seconds)

Managed HSM: single-tenant HSM pool, FIPS 140-2 Level 3, PKCS#11, higher isolation for strict regulatory. Key Vault Premium: shared HSM, simpler integration with Azure PaaS CMK.

### Detailed Answer (3–5 minutes)

**Architect:** Managed HSM when auditor requires dedicated HSM or PKCS#11. Key Vault Premium sufficient for most Azure CMK scenarios.

**Integration:** Managed HSM supports fewer native PaaS integrations — validate service compatibility.

### Architecture Perspective

Managed HSM for top-tier key isolation requirements.

### Follow-up Questions

1. **MHSM clustering? — Multi-region MHSM for DR — plan key replication.**
2. **Cost model? — Managed HSM higher base cost — capacity planning required.**

### Common Mistakes in Interviews

- Managed HSM without PKCS#11 need — overkill
- Assume all PaaS supports MHSM CMK
- No HSM access logging to SIEM

---

## Q020: Key Rotation Automation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Automate Key Vault secret and certificate rotation?

### Short Answer (30 seconds)

Event Grid notification on near-expiry; Azure Automation or Functions rotation function; dual-secret pattern for zero-downtime app refresh.

### Detailed Answer (3–5 minutes)

**Certificates:** Auto-renew via App Service managed cert or Key Vault integration.

**Architect:** Prefer Entra ID auth over SQL passwords — eliminates rotation. Test rotation game day quarterly.

### Architecture Perspective

Automated rotation beats manual ticket-driven expiry incidents.

### Follow-up Questions

1. **Rotation function template? — Microsoft sample rotation function for Storage/SQL.**
2. **CMK rotation? — Create new key version; re-encrypt or use latest automatically.**

### Common Mistakes in Interviews

- Secrets with no expiry date
- Rotation breaks prod without staging test
- Manual rotation only documented in wiki

---

## Q021: Azure Sentinel SIEM

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Design Sentinel deployment for multi-subscription Azure estate?

### Short Answer (30 seconds)

Central Log Analytics workspace in security subscription, Sentinel enabled, data connectors per source, RBAC for SOC analysts, watchlists and bookmarks.

### Detailed Answer (3–5 minutes)

**Architect:** Data ingestion cost model — filter verbose logs at source. Retention tiering: hot 90 days, archive longer for compliance.

**Workbooks:** Executive dashboard + tier-1 analyst triage view.

### Architecture Perspective

Sentinel is cloud-native SIEM for Azure-first estates.

### Follow-up Questions

1. **Sentinel vs Defender portal alerts? — Sentinel correlates cross-source; Defender is workload-centric.**
2. **Multi-workspace? — Single primary SOC workspace with LA agent — avoid sprawl.**

### Common Mistakes in Interviews

- Every subscription separate workspace
- No ingestion cost monitoring
- Sentinel enabled without use cases defined

---

## Q022: Data Connectors Sentinel

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Essential Sentinel data connectors for Azure landing zone?

### Short Answer (30 seconds)

Azure Activity, Azure AD (Entra ID), Defender for Cloud, DNS, Firewall, NSG flow (via LA), Key Vault diagnostics, Office 365 if applicable.

### Detailed Answer (3–5 minutes)

**Architect:** Prioritize connectors mapping to MITRE tactics — identity, network, endpoint. Custom logs via AMA for third-party apps.

**Validate:** Connector health blade — stale data equals blind SOC.

### Architecture Perspective

Connector strategy defines detection coverage.

### Follow-up Questions

1. **AMA vs Log Analytics agent? — Azure Monitor Agent is current standard.**
2. **CEF/Syslog connectors? — On-prem firewall and network gear.**

### Common Mistakes in Interviews

- Sentinel with only Activity Log
- Connectors enabled without parsing rules
- No connector failure alerting

---

## Q023: KQL Detection Rules

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Write Sentinel detection strategy beyond built-in analytics?

### Short Answer (30 seconds)

Custom scheduled query rules for org-specific TTPs: impossible travel, mass Key Vault access, new external forwarding rule, spike in failed auth.

### Detailed Answer (3–5 minutes)

**Example KQL pattern:**
```kql
SigninLogs | where ResultType != 0 | summarize Failed=count() by UserPrincipalName, bin(TimeGenerated, 5m) | where Failed > 20
```

**Architect:** Tune false positives in staging rule mode. Map each rule to MITRE technique and incident severity.

### Architecture Perspective

Custom KQL shows hands-on SOC architecture skill.

### Follow-up Questions

1. **NRT vs scheduled rules? — Near-real-time for high-severity; scheduled for batch patterns.**
2. **Fusion ML? — Built-in multi-stage attack detection — enable.**

### Common Mistakes in Interviews

- Copy generic KQL without tuning
- No suppression for known maintenance windows
- Rules without entity mapping for investigation

---

## Q024: SOAR Playbooks

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Sentinel automation playbook — disable compromised user scenario?

### Short Answer (30 seconds)

Trigger: Sentinel incident with high-confidence identity compromise. Actions: Entra disable user, revoke sessions, reset password, notify SOC, create ServiceNow ticket.

### Detailed Answer (3–5 minutes)

**Architect:** Human-in-the-loop approval for destructive actions in prod. Managed identity for playbook RBAC — least privilege.

**Test:** Simulation in nonprod tenant before auto-containment prod.

### Architecture Perspective

SOAR reduces MTTR when designed with guardrails.

### Follow-up Questions

1. **Logic Apps vs Automation? — Sentinel playbooks are Logic Apps ARM templates.**
2. **Webhook vs native connector? — Prefer native Entra connector over custom API.**

### Common Mistakes in Interviews

- Auto-disable user without approval on medium confidence
- Playbook service principal Contributor scope
- No playbook run history retention

---

## Q025: Microsoft Purview Compliance

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compliance |
| **Frequency** | Common |

### Question

Microsoft Purview for data governance architecture?

### Short Answer (30 seconds)

Purview scans Azure SQL, Storage, Synapse — classifies sensitive data, lineage maps ETL flows, compliance manager tracks control assessment.

### Detailed Answer (3–5 minutes)

**Architect:** Register data sources in Purview account per environment. Auto-labeling policies push classifications to M365 and Azure.

**Integration:** DLP policies use Purview sensitivity labels.

### Architecture Perspective

Purview connects data discovery to compliance posture.

### Follow-up Questions

1. **Purview vs Defender? — Purview data governance; Defender threat protection.**
2. **Lineage for ADF? — Purview captures copy activity lineage automatically.**

### Common Mistakes in Interviews

- Scan prod without sampling strategy — cost
- Classifications without owner remediation workflow
- Purview deployed without label policy adoption

---

## Q026: Information Protection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Sensitivity labels architecture for hybrid organization?

### Short Answer (30 seconds)

Labels defined in Purview/Compliance center — encrypt, mark headers, control sharing. Auto-labeling rules on SQL/Storage scanned data.

### Detailed Answer (3–5 minutes)

**Architect:** Label taxonomy aligned to data classification policy (Public, Internal, Confidential, Restricted). Mandatory labeling for email/docs via policy.

### Architecture Perspective

Information protection extends beyond network perimeter.

### Follow-up Questions

1. **Labels vs DLP? — Labels classify; DLP enforces actions on classified content.**
2. **Double key encryption? — Hold your own key for highest confidentiality.**

### Common Mistakes in Interviews

- Too many labels — user confusion
- Labels optional not enforced
- No training on label application

---

## Q027: DLP Policies

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

DLP policy for preventing credit card exfiltration?

### Short Answer (30 seconds)

Purview DLP detects PCI patterns in Exchange, SharePoint, Teams, endpoints — block external share, alert SOC, require justification.

### Detailed Answer (3–5 minutes)

**Architect:** Start in audit mode, tune false positives, enforce block. Endpoint DLP covers USB/upload paths.

**Scope reduction:** Tokenize payments — no PAN in email/files to begin with.

### Architecture Perspective

DLP is detective and preventive control for data exfil.

### Follow-up Questions

1. **Azure DLP vs M365 DLP? — Unified Purview DLP across services.**
2. **Custom sensitive info types? — Org-specific regex patterns.**

### Common Mistakes in Interviews

- DLP block day one without tuning
- DLP only on email not endpoints
- No exception workflow for false positives

---

## Q028: Insider Risk

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Occasional |

### Question

Defender Insider Risk Management use cases?

### Short Answer (30 seconds)

Detect data hoarding before departure, risky browser usage, anomaly volume download, policy violations on sensitive files.

### Detailed Answer (3–5 minutes)

**Architect:** Privacy/legal review before enable — scope policies to high-risk roles. Integrate with HR offboarding triggers.

**Not surveillance:** Transparent policy communication to employees.

### Architecture Perspective

Insider risk complements external threat detection.

### Follow-up Questions

1. **Insider risk vs DLP? — Insider risk behavioral analytics; DLP content pattern match.**
2. **Case triage workflow? — Analyst review before punitive action.**

### Common Mistakes in Interviews

- Enable broad monitoring without legal review
- No HR integration for termination triggers
- Treat all alerts as termination events

---

## Q029: Attack Surface Reduction

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Reduce attack surface for Azure-hosted .NET API?

### Short Answer (30 seconds)

Private Link only, no public IP, WAF+Front Door, Defender enabled, JIT admin, minimal RBAC, disable unused endpoints, API Management authZ.

### Detailed Answer (3–5 minutes)

**Architect:** ASR rules on VMs (block Office macros, child process create). Regular exposure scan — Defender CSPM 'attack path' analysis.

### Architecture Perspective

Attack surface reduction is continuous architecture discipline.

### Follow-up Questions

1. **Defender attack path analysis? — Graph shows lateral movement chains — remediate critical paths.**
2. **External scanning? — Authorized pen test + Defender EASM if licensed.**

### Common Mistakes in Interviews

- Public management ports open
- Unused legacy public endpoints
- Over-permissive NSG 'allow all'

---

## Q030: Just Enough Access

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Identity |
| **Frequency** | Very Common |

### Question

Implement Just Enough Access (JEA) on Azure?

### Short Answer (30 seconds)

PIM eligible assignments — no standing admin. Time-bound elevation with approval. Custom roles scoped to resource group not subscription.

### Detailed Answer (3–5 minutes)

**Architect:** Break-glass accounts sealed in vault — audited quarterly use only. CI/CD SP gets deploy role not Owner.

**Measure:** % admin actions via PIM vs permanent.

### Architecture Perspective

JEA is Zero Trust identity pillar on Azure.

### Follow-up Questions

1. **JEA vs JIT VM access? — JEA is RBAC elevation; JIT is NSG port opening.**
2. **Access reviews? — Quarterly Entra access review on privileged roles.**

### Common Mistakes in Interviews

- Permanent Owner on production subscription
- PIM without approval workflow
- Shared break-glass password

---

## Q031: Zero Trust Architecture Azure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Map Microsoft Zero Trust pillars to Azure services?

### Short Answer (30 seconds)

Verify explicitly (Entra CA, MFA), Least privilege (RBAC, PIM), Assume breach (Defender, Sentinel), Secure data (Purview, encryption), Secure infrastructure (Policy, Private Link).

### Detailed Answer (3–5 minutes)

**Architect:** Zero Trust assessment tool in Defender scores maturity per pillar. Roadmap by gap — identity first, then network, then data.

### Architecture Perspective

Zero Trust is framework — map to concrete Azure controls.

### Follow-up Questions

1. **Zero Trust vs perimeter? — Perimeter supports but identity is primary gate.**
2. **Micro-segmentation role? — Network leg of Zero Trust.**

### Common Mistakes in Interviews

- Zero Trust as single product purchase
- Network location trust only
- No measurement of Zero Trust maturity

---

## Q032: Secure Score vs Compliance

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

Explain secure score vs regulatory compliance in Defender?

### Short Answer (30 seconds)

Secure score: weighted Microsoft security recommendations best practice. Compliance: mapped controls (SOC2, PCI) pass/fail — overlapping but not identical.

### Detailed Answer (3–5 minutes)

**Architect:** Use both — compliance for audit evidence, secure score for continuous improvement. Custom initiative for org controls not in defaults.

### Architecture Perspective

Distinguishing score and compliance avoids audit surprises.

### Follow-up Questions

1. **100% secure score means compliant? — Not necessarily — regulatory controls may exceed recommendations.**
2. **Compliance only Azure policies? — Includes identity and data controls beyond ARM.**

### Common Mistakes in Interviews

- Ignore compliance dashboard if score high
- Compliance pass without evidence artifacts
- No custom initiative for internal standards

---

## Q033: Vulnerability Scanning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Vulnerability management architecture on Azure?

### Short Answer (30 seconds)

Defender for Cloud VA on SQL/VM/containers, Qualys extension optional on VMs, container registry scan on push, CI/CD Trivy on images.

### Detailed Answer (3–5 minutes)

**Architect:** Severity SLA — Critical patch 7 days. Integrate findings to Azure DevOps work items. Block deploy on critical unmitigated in prod pipeline.

### Architecture Perspective

Vulnerability scanning spans runtime and build-time.

### Follow-up Questions

1. **Agentless VM scanning? — Defender agentless scanner — no agent install.**
2. **ACR vulnerability scan? — Microsoft Defender for Containers on registry.**

### Common Mistakes in Interviews

- Scan only quarterly
- Critical CVE no SLA
- Scanner findings not routed to owners

---

## Q034: Container Security Defender

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Defender for Containers on AKS — what is protected?

### Short Answer (30 seconds)

Runtime threat detection on nodes, K8s audit log analysis, registry image scan, misconfiguration (privileged pods, hostPath mounts).

### Detailed Answer (3–5 minutes)

**Architect:** Enable Defender plan, deploy DaemonSet agent, restrict privileged containers via Azure Policy for Kubernetes. Network policy default deny.

### Architecture Perspective

Container security is orchestrator + image + runtime.

### Follow-up Questions

1. **Defender vs admission controller? — Defender detects runtime; Gatekeeper prevents bad deploys.**
2. **AKS free tier Defender? — Per-node licensing — budget accordingly.**

### Common Mistakes in Interviews

- Privileged pods allowed in prod
- No image scan on CI push
- Defender enabled without K8s audit logs

---

## Q035: DevSecOps Pipeline Gates

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DevSecOps |
| **Frequency** | Very Common |

### Question

Security gates in Azure DevOps pipeline for Bicep deploy?

### Short Answer (30 seconds)

1. Secret scan (CredScan) 2. Bicep linter + what-if 3. Defender for IaC / Checkov 4. Policy compliance scan 5. Deploy staging 6. VA scan post-deploy.

### Detailed Answer (3–5 minutes)

**Architect:** Golden pipeline template — teams inherit gates. Fail on Critical; warn on Medium with ticket.

**Break glass:** Document override with CAB approval.

### Architecture Perspective

Pipeline gates encode security architecture at scale.

### Follow-up Questions

1. **What-if vs deploy? — What-if catches policy deny before ARM submission.**
2. **Progressive deployment? — Canary with Defender continuous assessment post-deploy.**

### Common Mistakes in Interviews

- Deploy direct to prod no gates
- Secret in repo undetected
- Policy violations ignored in what-if

---

## Q036: Secret Scanning GitHub

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DevSecOps |
| **Frequency** | Very Common |

### Question

Prevent secrets in Git — GitHub and Azure DevOps?

### Short Answer (30 seconds)

GitHub secret scanning + push protection; Azure DevOps CredScan in pipeline; pre-commit hooks locally; rotate if leaked.

### Detailed Answer (3–5 minutes)

**Architect:** Block merge on detected secret. Use Key Vault references in appsettings — never commit connection strings.

**If leaked:** Rotate immediately — secret in git history forever even if deleted.

### Architecture Perspective

Secret scanning is minimum DevSecOps bar.

### Follow-up Questions

1. **Push protection? — Prevent commit containing known secret patterns.**
2. **GitHub Advanced Security? — Required org-wide for private repos policy.**

### Common Mistakes in Interviews

- Secrets in Bicep parameters committed
- Scan only on main branch
- Leaked key not rotated — assume compromised

---

## Q037: SAST DAST Integration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | DevSecOps |
| **Frequency** | Common |

### Question

Integrate SAST and DAST in release pipeline?

### Short Answer (30 seconds)

SAST: CodeQL/SonarQube on PR — block Critical. DAST: OWASP ZAP against staging URL post-deploy — auth-aware scan.

### Detailed Answer (3–5 minutes)

**Architect:** SAST in PR fast feedback; DAST nightly on staging. Separate dev noise from prod gate rules.

**Limitation:** DAST misses authZ logic bugs — complement with threat modeling.

### Architecture Perspective

SAST+DAST shift-left and validate running app.

### Follow-up Questions

1. **CodeQL vs Sonar? — CodeQL deep semantic; Sonar broad language support.**
2. **Authenticated DAST? — Script login flow in ZAP context.**

### Common Mistakes in Interviews

- SAST only on release branch
- DAST against production
- Ignore SAST findings as false positive always

---

## Q038: Threat Modeling STRIDE

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Apply STRIDE to Azure order API architecture?

### Short Answer (30 seconds)

Spoofing: Entra JWT validation. Tampering: HTTPS, signed payloads. Repudiation: audit logs. Info disclosure: minimize response fields. DoS: rate limits, autoscale. Elevation: object-level authZ on orderId.

### Detailed Answer (3–5 minutes)

**Architect:** Threat model per major feature at design phase. Document mitigations in ADR. Revisit on architecture change.

**Tool:** Microsoft Threat Modeling Tool or OWASP.

### Architecture Perspective

STRIDE connects threats to concrete Azure controls.

### Follow-up Questions

1. **STRIDE vs PASTA? — STRIDE categorization; PASTA risk-centric process.**
2. **Trust boundaries? — Draw API, DB, queue as boundaries.**

### Common Mistakes in Interviews

- Threat model after prod launch only
- Generic threats not mapped to mitigations
- Skip repudiation/logging threats

---

## Q039: Security Review Checklist

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Governance |
| **Frequency** | Common |

### Question

Architecture security review checklist items?

### Short Answer (30 seconds)

Identity model, data classification, encryption transit/rest, network diagram, secrets management, logging/monitoring, DR, compliance controls, threat model reference.

### Detailed Answer (3–5 minutes)

**Architect:** Review gate before prod deploy — signed checklist in ADO work item. Red team findings tracked to closure.

### Architecture Perspective

Checklist institutionalizes security in design process.

### Follow-up Questions

1. **Review cadence? — Major release + annual per system.**
2. **Who attends? — Architect, security, ops, product owner.**

### Common Mistakes in Interviews

- Checklist checkbox exercise no depth
- No threat model attached
- Findings not tracked post-review

---

## Q040: Incident Response Azure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Azure security incident response phases for Key Vault breach?

### Short Answer (30 seconds)

1. Detect (Sentinel alert) 2. Contain (disable SP, rotate secrets) 3. Eradicate (remove persistence) 4. Recover (restore from backup) 5. Lessons learned.

### Detailed Answer (3–5 minutes)

**Architect:** Pre-document runbooks in Sentinel playbooks. Preserve Key Vault diagnostic logs before rotation. Legal notification timeline per regulation.

### Architecture Perspective

IR runbooks show operational security maturity.

### Follow-up Questions

1. **Forensic subscription? — Isolated subscription for snapshot analysis.**
2. **Communication plan? — Exec, legal, customer notification templates.**

### Common Mistakes in Interviews

- Delete logs during incident cleanup
- No secret rotation runbook
- Incident without postmortem

---

## Q041: Forensics Blob Immutability

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Immutable blob storage for forensic evidence retention?

### Short Answer (30 seconds)

Time-based immutability policy on evidence container — WORM compliance. Legal hold for litigation. Separate storage account air-gapped RBAC.

### Detailed Answer (3–5 minutes)

**Architect:** Sentinel incident exports, VM disk snapshots, packet captures land in immutable container. Retention matches regulatory minimum (e.g., 7 years finance).

### Architecture Perspective

Immutability prevents attacker or admin tampering evidence chain.

### Follow-up Questions

1. **Immutability vs soft delete? — Immutability cannot delete until retention expires.**
2. **Version-level immutability? — Finer control per blob version.**

### Common Mistakes in Interviews

- Mutable forensic storage
- Same account as operational logs — attacker deletes
- Retention shorter than legal requirement

---

## Q042: Ransomware Protection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Azure ransomware resilience architecture?

### Short Answer (30 seconds)

Backup with immutability, MFA on backup admin, Private Link backups, Defender alerts, least privilege, tested restore, multi-region backup copies.

### Detailed Answer (3–5 minutes)

**Architect:** 3-2-1 rule — 3 copies, 2 media, 1 offsite. Azure Backup soft delete + immutability. Regular restore drills — untested backup is hope not strategy.

### Architecture Perspective

Ransomware architecture is backup + identity + detection.

### Follow-up Questions

1. **Azure Backup immutability? — Vault immutability prevents backup deletion.**
2. **Multi-user authorization on backup? — Critical operations require second approver.**

### Common Mistakes in Interviews

- Single backup copy same region
- Backup admin same as prod admin
- Never tested restore

---

## Q043: Backup Encryption

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Backup encryption on Azure — keys and scope?

### Short Answer (30 seconds)

Azure Backup encrypts at rest by default with Microsoft-managed keys. CMK optional via Key Vault for regulatory custody.

### Detailed Answer (3–5 minutes)

**Architect:** CMK for finance/health backups. Encrypt backup traffic in transit TLS. Separate backup RG RBAC from workload admins.

### Architecture Perspective

Backup encryption is often assumed not verified.

### Follow-up Questions

1. **CMK rotation impact? — New backups use new key version.**
2. **On-prem MARS agent? — Passphrase + Azure encryption.**

### Common Mistakes in Interviews

- Assume backup unencrypted acceptable
- CMK without key recovery plan
- Backup operators can delete backups

---

## Q044: Customer-Managed Keys PaaS

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

Enable CMK for Azure SQL and Storage — architecture steps?

### Short Answer (30 seconds)

Create HSM or software key in Key Vault, grant SQL/Storage service identity unwrap permissions, configure CMK on resource, verify encryption status.

### Detailed Answer (3–5 minutes)

**Architect:** Key in same region as data. Document key revocation procedure — revocation makes data inaccessible immediately.

### Architecture Perspective

CMK is customer custody vs Microsoft-managed default.

### Follow-up Questions

1. **Double encryption? — CMK plus platform encryption layer.**
2. **Key revocation drill? — Test annually — understand data lockout.**

### Common Mistakes in Interviews

- CMK key in wrong region
- No wrap/unwrap permission for service
- Revoke key without DR plan

---

## Q045: Double Encryption

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Occasional |

### Question

Double encryption on Azure — when required?

### Short Answer (30 seconds)

Platform encryption + customer-managed key on Storage/SQL/Disks — defense in depth for highest classification data.

### Detailed Answer (3–5 minutes)

**Architect:** Evaluate performance and cost. Required by some government contracts. Managed HSM for key material isolation.

### Architecture Perspective

Double encryption for regulatory maximum assurance.

### Follow-up Questions

1. **Which services support? — Storage, SQL, managed disks — verify current list.**
2. **Performance impact? — Minimal for most — benchmark write-heavy workloads.**

### Common Mistakes in Interviews

- Double encryption without CMK need
- Ignore Microsoft-managed layer in threat model
- Key and data different compliance zones

---

## Q046: Confidential Computing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Occasional |

### Question

Azure confidential computing use cases?

### Short Answer (30 seconds)

Encrypt data in use — SGX enclaves or AMD SEV-SNP on DCsv3/DCasv5 VMs for multi-party compute, encrypted SQL Always Encrypted with enclave.

### Detailed Answer (3–5 minutes)

**Architect:** When threat model includes malicious admin or host compromise — enclave protects data during processing. Higher cost SKUs.

**SGX enclaves:** Intel SGX trusted execution for small memory enclaves — attestation proves code integrity.

### Architecture Perspective

Confidential computing protects data in use — third encryption state.

### Follow-up Questions

1. **SGX vs SEV-SNP? — SGX enclave app model; SEV encrypts entire VM memory.**
2. **Attestation? — Verify enclave identity before secrets release.**

### Common Mistakes in Interviews

- Confidential VM for all workloads — cost
- SGX without understanding memory limits
- No attestation in secret release flow

---

## Q047: Trusted Launch VMs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

Trusted Launch for Azure VMs — benefits?

### Short Answer (30 seconds)

Secure Boot, vTPM, boot integrity attestation — prevents rootkits and boot-level malware. Required baseline for many compliance frameworks.

### Detailed Answer (3–5 minutes)

**Architect:** Enable Trusted Launch on new VM templates. Boot diagnostics to Azure Storage encrypted. Pair with Defender for Servers.

### Architecture Perspective

Trusted Launch is firmware/boot integrity layer.

### Follow-up Questions

1. **Trusted Launch vs Confidential VM? — Trusted Launch boot integrity; Confidential VM memory encryption.**
2. **Gen2 VMs required? — Trusted Launch requires Gen2 images.**

### Common Mistakes in Interviews

- Gen1 VMs in new deployments
- Secure Boot disabled
- No boot integrity monitoring alerts

---

## Q048: Firmware Integrity

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Occasional |

### Question

How Azure addresses firmware-level threats?

### Short Answer (30 seconds)

Project Cerberus-inspired platform integrity, Trusted Launch attestation, Defender alerts on boot anomalies, Azure-hosted hardware root of trust.

### Detailed Answer (3–5 minutes)

**Architect:** Specify Trusted Launch in VMSS and AKS node pools. Monitor Defender recommendations for firmware-related findings.

### Architecture Perspective

Firmware integrity is emerging architect concern for regulated VMs.

### Follow-up Questions

1. **Measured boot? — vTPM records boot measurements for attestation.**
2. **On-prem comparison? — Azure manages hardware integrity customer enables VM features.**

### Common Mistakes in Interviews

- Ignore boot-level threats as hypothetical
- Custom images without integrity verification
- No attestation in compliance evidence

---

## Q049: Security Baselines AKS

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Security |
| **Frequency** | Common |

### Question

AKS security baseline — top controls?

### Short Answer (30 seconds)

Private cluster, Azure CNI network policy, Defender for Containers, Azure Policy add-on (no privileged pods), managed identity, API server authorized IP ranges or private.

### Detailed Answer (3–5 minutes)

**Architect:** CIS Azure benchmark mapping for AKS — enable policy initiative 'Kubernetes cluster pod security baseline standards for Azure Kubernetes Service'. Regular kube-bench assessment.

### Architecture Perspective

AKS baseline combines K8s and Azure platform controls.

### Follow-up Questions

1. **Private cluster? — API server private endpoint — no public kube-apiserver.**
2. **Pod Security Standards? — Replace deprecated PSP with built-in PSS labels.**

### Common Mistakes in Interviews

- Public AKS API with wide IP allow list
- kubenet without network policy
- No CIS assessment in CI

---

## Q050: CIS Benchmark Azure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compliance |
| **Frequency** | Common |

### Question

Implement CIS Microsoft Azure Foundations Benchmark?

### Short Answer (30 seconds)

Assign CIS Azure Policy initiative in audit then deny mode. Defender regulatory dashboard tracks CIS controls. Remediate identity and logging gaps first.

### Detailed Answer (3–5 minutes)

**Architect:** Not every CIS control applies — document exceptions. Automate DeployIfNotExists for diagnostic settings and MFA requirements.

**Evidence:** Export compliance reports for auditors quarterly.

### Architecture Perspective

CIS benchmark is practical hardening standard for Azure estates.

### Follow-up Questions

1. **CIS vs Azure Security Benchmark? — Overlap — ASB is Microsoft superset mapping.**
2. **Level 1 vs Level 2 CIS? — Level 2 stricter — phased adoption.**

### Common Mistakes in Interviews

- CIS audit-only forever
- No exception documentation process
- CIS compliance without technical remediation owners

---
