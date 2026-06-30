# Week 44 — Intermediate Q&A

> Q031–Q070: Premium format (Week 1 quality).

---


## Q031: HIPAA BAA Eligible Services

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | HIPAA |
| **Frequency** | Very Common |

### Question

How do you verify cloud services are HIPAA-eligible before architecture design?

### Short Answer (30 seconds)

Check provider BAA coverage list quarterly; only use eligible services for ePHI; document service eligibility matrix; legal executes BAA before PHI flows.

### Detailed Answer (3–5 minutes)

**Azure example:** Microsoft publishes HIPAA/HITRUST eligible services — not all AI or analytics services included.

**Architect checklist:**
- Service on eligible list?
- BAA executed?
- Region supports BAA?
- Subprocessors documented?

**Non-eligible workaround:** De-identify before processing or use on-prem alternative.

**Architect:** Eligibility matrix in repo — PR blocked if new non-eligible service stores PHI.

### Architecture Perspective

HIPAA architecture starts with BAA eligibility — not after build.

### Follow-up Questions

1. **AWS/Azure difference? — Each has own eligible list — multi-cloud doubles review.**
2. **Dev/test PHI? — Prohibited — synthetic/de-identified data only.**

### Common Mistakes in Interviews

- Assume all PaaS covered by default BAA
- PHI in logging service without eligibility check
- BAA signed but architecture uses preview AI feature

---

## Q032: HIPAA Minimum Necessary Access

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | HIPAA |
| **Frequency** | Very Common |

### Question

Implement minimum necessary access in healthcare system architecture.

### Short Answer (30 seconds)

Role-based access scoped to job function; break-glass audited; field-level masking in APIs; query filters enforce patient relationship; access reviews quarterly.

### Detailed Answer (3–5 minutes)

**Technical controls:**
- ABAC: clinician sees only assigned patients
- API returns masked SSN/MRN in lists
- Audit log every PHI read with purpose
- Emergency access workflow with retro review

**Architect:** Minimum necessary is API design — not only IAM group membership.

### Architecture Perspective

HIPAA interviews probe whether architects embed least privilege in data paths.

### Follow-up Questions

1. **Break-glass? — Pre-provisioned emergency role — 100% logged — review 24h.**
2. **Patient portal? — Patient sees own record only — scope token claim.**

### Common Mistakes in Interviews

- Admin role sees all patients by default
- PHI in admin search index unscoped
- No access review process automated

---

## Q033: PHI Zone Network Segmentation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | PHI Boundaries |
| **Frequency** | Very Common |

### Question

Segment network zones for PHI vs non-PHI workloads.

### Short Answer (30 seconds)

PHI zone: private subnets, Private Link, no public IPs, NSG deny outbound except allowlist. Non-PHI: marketing, public website. Integration via controlled API gateway with DLP.

### Detailed Answer (3–5 minutes)

**Diagram:**
```
[Internet] → [WAF Non-PHI Web]
[Clinical App PHI Zone] ←Private Link→ [EHR DB PHI Zone]
[Analytics De-ID Zone] ← batch ETL sanitized only
```

**Architect:** Every cross-zone flow in data flow diagram — auditor walks arrows.

### Architecture Perspective

PHI segmentation is foundational — flat network fails HIPAA technical safeguards.

### Follow-up Questions

1. **VPN to PHI? — Zero trust preferred — conditional access MFA.**
2. **Third-party integration? — BAA + IP allowlist + mTLS minimum.**

### Common Mistakes in Interviews

- PHI database with public endpoint 'temporarily'
- Flat VPC all services same subnet
- Analytics VPN into PHI zone for convenience

---

## Q034: PHI in Application Logs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | PHI Boundaries |
| **Frequency** | Very Common |

### Question

Prevent PHI from appearing in application and platform logs.

### Short Answer (30 seconds)

Structured logging with redaction middleware; prohibit logging request/response bodies with clinical data; log patientId as opaque token; SIEM alerts on SSN regex.

### Detailed Answer (3–5 minutes)

**Patterns:**
- Serilog destructuring policies redact `[PHI]` properties
- APM scrubbing rules (App Insights `TelemetryProcessor`)
- Developer lint rule: no log full `Patient` object

**Architect:** Logging standards mandatory in healthcare — violation is breach vector.

### Architecture Perspective

PHI in logs is common audit finding — architects design redaction at framework level.

### Follow-up Questions

1. **Debug prod? — Never full PHI — use synthetic repro.**
2. **Exception stack with patient name? — Sanitize exception enrichers.**

### Common Mistakes in Interviews

- Log entire JSON request body clinical API
- CloudWatch/App Insights retain PHI 30 days unencrypted
- No automated PHI pattern scan in logs

---

## Q035: PCI SAQ Type Selection

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | PCI Scope |
| **Frequency** | Very Common |

### Question

Determine PCI SAQ type based on payment architecture.

### Short Answer (30 seconds)

SAQ A: card data never touches merchant (iframe/hosted fields). SAQ A-EP: merchant website affects payment but no PAN storage. SAQ D: full card environment.

### Detailed Answer (3–5 minutes)

**Architecture mapping:**
| Flow | SAQ |
|------|-----|
| Stripe Elements iframe | A or A-EP |
| Server receives PAN | D |
| Token only stored | Reduced scope |

**Architect:** SAQ type is architecture outcome — document in payment ADR.

### Architecture Perspective

PCI scope drives SAQ cost — architects design toward SAQ A where possible.

### Follow-up Questions

1. **SAQ A-EP still? — Merchant server in scope for CDE influence — segment network.**
2. **Annual revalidation? — Architecture change triggers SAQ reassessment.**

### Common Mistakes in Interviews

- Custom card form to own API — full scope surprise
- SAQ A claimed but server logs PAN
- Scope not reassessed after payment refactor

---

## Q036: PCI Network Segmentation CDE

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | PCI Scope |
| **Frequency** | Common |

### Question

Segment Cardholder Data Environment from rest of network.

### Short Answer (30 seconds)

CDE isolated VLAN/subnet; firewall deny by default; jump host for admin; no dev access to CDE; quarterly scan ASV on external CDE.

### Detailed Answer (3–5 minutes)

**Architecture:**
```
[CDE: Payment API + HSM] ←firewall→ [App Tier no PAN]
[Dev/Test] ✗ no route to CDE
```

**Tokenization:** PAN only in PSP iframe — merchant CDE minimal or empty.

**Architect:** CDE diagram required for QSA — keep updated.

### Architecture Perspective

Segmentation reduces PCI audit surface — even token-only architectures benefit.

### Follow-up Questions

1. **Shared services in CDE? — DNS, NTP exceptions documented — minimize.**
2. **Container CDE? — K8s network policy namespace isolation.**

### Common Mistakes in Interviews

- CDE DB reachable from corporate LAN
- Developers SSH to CDE for debugging
- No network diagram for QSA

---

## Q037: Black Friday Capacity Planning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Retail Peak |
| **Frequency** | Very Common |

### Question

Plan capacity for predictable retail peak events.

### Short Answer (30 seconds)

Load test 3× peak 6 weeks ahead; pre-scale AKS node pools; Redis pre-warm; CDN cache product pages; autoscale policies tested; runbook and war room roster.

### Detailed Answer (3–5 minutes)

**Capacity checklist:**
- Traffic forecast from marketing + YoY growth
- Bottleneck analysis last peak incidents
- Pre-provisioned min nodes + max caps raised temporarily
- Database connection pool sizing
- Third-party rate limits confirmed (PSP, fraud)

**Architect:** Peak capacity ADR with signed headroom metrics — not guess day-of.

### Architecture Perspective

Retail peak is planned event — architecture prepares months ahead.

### Follow-up Questions

1. **Cost of over-provision? — Cheaper than revenue loss — scale down after.**
2. **Synthetic load? — k6/Gatling scripts in CI monthly before peak season.**

### Common Mistakes in Interviews

- First load test week of event
- Autoscale max unchanged from normal
- Single region global traffic

---

## Q038: Virtual Waiting Room Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Retail Peak |
| **Frequency** | Common |

### Question

Implement virtual waiting room during checkout overload.

### Short Answer (30 seconds)

Queue users at CDN/edge when origin capacity exceeded; fair FIFO token; release at sustainable rate; communicate wait time; bypass for returning customers optional.

### Detailed Answer (3–5 minutes)

**Implementation:**
- Azure Front Door Premium waiting room
- Custom queue service issues `queue_token` cookie
- Origin accepts only valid tokens

**UX:** Branded wait page; auto-refresh into checkout.

**Architect:** Waiting room protects payment path — browse may stay open while checkout queued.

### Architecture Perspective

Waiting room is graceful degradation architecture for revenue protection.

### Follow-up Questions

1. **Bot bypass? — CAPTCHA at queue entry — protect inventory.**
2. **VIP customers? — Controversial — document fairness policy.**

### Common Mistakes in Interviews

- Unbounded checkout crashes origin
- Queue with no ETA — user abandonment
- Waiting room on static CDN pages unnecessarily

---

## Q039: Multi-Tenant Row-Level Security

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Multi-Tenant |
| **Frequency** | Very Common |

### Question

Implement row-level tenant isolation in shared database.

### Short Answer (30 seconds)

Every table has `tenantId`; ORM interceptor injects filter; integration tests attempt cross-tenant access; DB RLS policy as defense in depth.

### Detailed Answer (3–5 minutes)

**Implementation:**
```sql
CREATE POLICY tenant_isolation ON orders
  USING (tenant_id = current_setting('app.tenant_id')::uuid);
```

**App sets** `SET app.tenant_id` per request from JWT.

**Architect:** Cross-tenant leak test in CI — security gate.

### Architecture Perspective

Row-level isolation is default SaaS — one missing filter is breach.

### Follow-up Questions

1. **RLS vs app-only? — Both — defense in depth for regulated tenants.**
2. **Shared schema migration? — Tenant-aware flyway — test all tenants.**

### Common Mistakes in Interviews

- Manual tenantId in queries — one forgets
- Admin report without tenant filter
- Cache key missing tenantId

---

## Q040: Database Per Tenant Model

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Multi-Tenant |
| **Frequency** | Common |

### Question

When choose database-per-tenant isolation model?

### Short Answer (30 seconds)

Enterprise/regulated customers, noisy neighbor intolerance, custom schema per tenant, or contractual isolation requirement — trade higher ops cost for strongest boundary.

### Detailed Answer (3–5 minutes)

**Ops architecture:**
- Provisioning pipeline creates DB + credentials
- Catalog service maps tenant→connection string
- Backup per tenant for SLA
- Patch automation across fleet

**Architect:** Hybrid pool — SMB shared DB; enterprise silo — pricing reflects cost.

### Architecture Perspective

DB-per-tenant is sales-driven architecture — ops automation mandatory.

### Follow-up Questions

1. **Elastic pools? — Azure SQL elastic pool cost efficiency for many small DBs.**
2. **Cross-tenant analytics? — ETL to warehouse with tenant dimension — not live cross-DB query.**

### Common Mistakes in Interviews

- Enterprise customer on shared row without contract review
- Manual DB provisioning 2-week delay
- 1000 DBs without patch automation

---

## Q041: Architecture Review Board Charter

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Architecture Review Board |
| **Frequency** | Very Common |

### Question

Define charter for enterprise architecture review board.

### Short Answer (30 seconds)

Purpose, scope, membership, tiered review triggers, decision authority, SLA, relationship to ARB/CAB, exception process, meeting cadence, artifact requirements.

### Detailed Answer (3–5 minutes)

**Charter sections:**
1. **Mission** — Quality, compliance, cost alignment
2. **Scope** — Tier-0/1/2 systems definitions
3. **Members** — EA, security, data, ops, legal delegate
4. **Inputs** — ADR, RFC, diagrams, threat model
5. **Outputs** — Approved / conditions / rejected
6. **SLA** — Decision within 10 business days

**Architect:** Published charter prevents 'ARB is optional'.

### Architecture Perspective

ARB charter makes governance real — interviewers test operating model not just diagrams.

### Follow-up Questions

1. **Quorum? — Minimum security + EA for Tier-0 decision.**
2. **Escalation? — Unresolved conflict to CTO within 5 days.**

### Common Mistakes in Interviews

- ARB with no authority — recommendations ignored
- No tier definitions — everything or nothing reviewed
- Charter not accessible to engineers

---

## Q042: Tiered Architecture Review

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Architecture Review Board |
| **Frequency** | Very Common |

### Question

Define tiered architecture review requirements by system criticality.

### Short Answer (30 seconds)

Tier-0: full ARB + threat model + pen test plan. Tier-1: abbreviated checklist. Tier-2: team self-certification with spot audit.

### Detailed Answer (3–5 minutes)

**Tier examples:**
| Tier | Systems | Review |
|------|---------|--------|
| 0 | Payment, PHI, auth | Full ARB + compliance |
| 1 | Customer-facing non-PCI | Standard checklist |
| 2 | Internal tools | Lightweight self-review |

**Architect:** Tier assignment in service catalog — auto-routes review workflow.

### Architecture Perspective

Tiering scales governance — not every tool needs 40-person review.

### Follow-up Questions

1. **Tier creep? — Annual recertification of tier assignment.**
2. **Promotion tier? — Internal tool becomes external — re-tier trigger.**

### Common Mistakes in Interviews

- Same heavyweight review for POC and payment
- Tier-0 system skips security
- No documented tier criteria

---

## Q043: SOC2 Evidence Architecture Pack

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compliance Audits |
| **Frequency** | Very Common |

### Question

Assemble architecture evidence pack for SOC2 Type II audit.

### Short Answer (30 seconds)

C4 diagrams, ADRs, access matrices, change records, DR drill logs, vendor assessments, pen test remediation — mapped to Trust Services Criteria.

### Detailed Answer (3–5 minutes)

**Mapping:**
- CC6.1 Logical access → IAM architecture + PIM screenshots
- CC7.2 Monitoring → SLO dashboards + alert rules
- CC8.1 Change management → PR samples + pipeline gates

**Maintenance:** Living folder updated each sprint — not annual scramble.

**Architect:** Auditors sample systems — evidence must match production reality.

### Architecture Perspective

SOC2 is continuous evidence — architecture docs are audit artifacts.

### Follow-up Questions

1. **Type I vs II? — Type II proves operating effectiveness over period.**
2. **Bridge letter? — Gap coverage between audit periods for customers.**

### Common Mistakes in Interviews

- Diagrams from 2 years ago
- ADR missing for major migration during audit window
- Evidence scattered personal drives

---

## Q044: ISO 27001 Architecture Controls

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compliance Audits |
| **Frequency** | Common |

### Question

Map system architecture to ISO 27001 Annex A controls.

### Short Answer (30 seconds)

A.8 asset management, A.9 access control, A.12 operations, A.14 acquisition — architecture delivers network diagrams, crypto standards, logging, SDLC gates as control evidence.

### Detailed Answer (3–5 minutes)

**Architect deliverables:**
- Asset inventory linked to CMDB
- Data classification per service
- Encryption standards ADR
- Vulnerability management integration
- Supplier security assessments

**Architect:** ISO gap assessment before claiming alignment — controls need implementation not checkbox.

### Architecture Perspective

ISO mapping shows architect understands control frameworks beyond SOC2.

### Follow-up Questions

1. **Statement of Applicability? — Documents excluded controls with justification.**
2. **Internal audit? — Pre-audit before external certification.**

### Common Mistakes in Interviews

- Controls documented but not implemented
- No link between ADR and ISO control
- Ignore supplier control A.15

---

## Q045: Vendor Security Questionnaire

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Vendor Risk |
| **Frequency** | Very Common |

### Question

Evaluate vendor security questionnaire responses architecturally.

### Short Answer (30 seconds)

Validate SOC2 type, data residency, encryption, subprocessors, incident notification SLA, API export, pen test summary — score gaps; require mitigations or alternate vendor.

### Detailed Answer (3–5 minutes)

**Red flags:**
- No SOC2 Type II
- Vague subprocessor list
- No encryption at rest
- 48h breach notification only email
- Proprietary export format

**Mitigation architecture:**
- Abstraction layer service
- Data minimization to vendor
- Contractual audit rights

**Architect:** High-risk vendor ADR documents dependency and exit plan.

### Architecture Perspective

Vendor questionnaire is architecture input — bad answers change design.

### Follow-up Questions

1. **Fourth parties? — Require vendor disclose subprocessors — chain risk.**
2. **Re-assessment cadence? — Annual for Tier-1 vendors.**

### Common Mistakes in Interviews

- Skip review for 'known brand' vendor
- Accept vendor claims without SOC2 report
- No exit plan in architecture

---

## Q046: Vendor Lock-In Mitigation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Vendor Risk |
| **Frequency** | Common |

### Question

Architect mitigations for vendor lock-in risk.

### Short Answer (30 seconds)

Abstraction interfaces, standard data formats, periodic export tests, multi-vendor strategy for critical capabilities, escrow for source if applicable.

### Detailed Answer (3–5 minutes)

**Patterns:**
- **Anti-corruption layer** around vendor SDK
- **S3-compatible** storage abstraction
- **OpenTelemetry** not vendor APM proprietary agent only
- **Kubernetes** portable workloads

**Architect:** Lock-in ADR quantifies switching cost — executive accepts or funds mitigation.

### Architecture Perspective

Lock-in is business risk — architects document exit cost honestly.

### Follow-up Questions

1. **Dual write migration? — Temporary sync to new vendor — cutover plan.**
2. **Contract terms? — Data portability and deletion on exit clauses.**

### Common Mistakes in Interviews

- Deep proprietary API without wrapper
- Never tested export restore
- Single vendor identity payment database all-in

---

## Q047: GDPR Lawful Basis Documentation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | GDPR |
| **Frequency** | Very Common |

### Question

Document lawful basis for processing in architecture artifacts.

### Short Answer (30 seconds)

Each processing purpose maps to lawful basis (contract, consent, legitimate interest); ROPA maintained; DPIA for high-risk; technical measures support basis (consent management, erasure).

### Detailed Answer (3–5 minutes)

**ROPA row example:**
| Purpose | Data | Basis | Retention | System |
| Marketing email | Email | Consent | Until withdraw | CRM |

**Architect:** Services tagged with processing purpose in service catalog — privacy team reviews new services.

### Architecture Perspective

GDPR lawful basis is architecture metadata — not legal doc only.

### Follow-up Questions

1. **Legitimate interest assessment? — LIA document for analytics without consent.**
2. **Special category health data? — Explicit consent or healthcare legal basis.**

### Common Mistakes in Interviews

- No basis documented per microservice
- Consent bundled non-negotiable
- Analytics ignores withdrawn consent

---

## Q048: GDPR Right to Erasure Pipeline

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | GDPR |
| **Frequency** | Very Common |

### Question

Design cross-system erasure workflow for GDPR Article 17.

### Short Answer (30 seconds)

Orchestrated `UserDeleted` event; each service subscribes and deletes/anonymizes; idempotent handlers; audit trail of erasure completion; exceptions documented (legal hold).

### Detailed Answer (3–5 minutes)

**Architecture:**
```
Privacy Portal → Erasure Service → Event Bus → [CRM, Orders, Analytics, Backups]
```

**Challenges:**
- Backups immutable — crypto-shred or retention policy
- Analytics anonymize not delete aggregates
- Third-party vendor deletion API calls

**Architect:** Erasure SLA 30 days — track per-system completion dashboard.

### Architecture Perspective

Erasure is distributed workflow — architects orchestrate not single DELETE.

### Follow-up Questions

1. **Legal hold? — Block erasure flag per user — audit reason.**
2. **Pseudonymization vs delete? — Jurisdiction and purpose dependent.**

### Common Mistakes in Interviews

- Delete user in CRM only — ghost data elsewhere
- No erasure audit trail
- Backups retain PII indefinitely

---

## Q049: SOX Segregation of Duties

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SOX |
| **Frequency** | Very Common |

### Question

Implement segregation of duties for SOX in-scope systems.

### Short Answer (30 seconds)

Developer cannot deploy to prod; separate approver; PIM for prod access; CI/CD environment gates; audit log immutable.

### Detailed Answer (3–5 minutes)

**Controls:**
- Git: PR approval required — author ≠ approver
- Pipeline: prod stage needs CAB/change ticket
- IAM: no standing prod admin — PIM elevation
- DB: dev/test/prod network isolation

**Architect:** SOX systems identified in inventory — controls applied by tier not ad hoc.

### Architecture Perspective

SOX ITGC drives pipeline architecture — not optional for finance systems.

### Follow-up Questions

1. **Emergency change? — Break glass with retrospective approval 48h.**
2. **In-scope system? — Touches financial reporting — GL interface triggers SOX.**

### Common Mistakes in Interviews

- Developer SSH prod for hotfix routinely
- Shared admin credentials
- Pipeline deploy prod on merge to main

---

## Q050: SOX Change Management Evidence

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | SOX |
| **Frequency** | Common |

### Question

Produce change management evidence for SOX auditors.

### Short Answer (30 seconds)

PR history, approval records, test results, deployment logs, CAB minutes, emergency change forms — linked to change ticket ID in ITSM.

### Detailed Answer (3–5 minutes)

**Evidence chain:**
```
JIRA CHANGE-123 → PR #456 approvals → CI test pass → Pipeline deploy log → Post-deploy verification
```

**Architect:** IaC changes same rigor as app code — Terraform plan in PR.

### Architecture Perspective

Auditors trace sample changes end-to-end — broken chain fails control.

### Follow-up Questions

1. **Automated vs manual deploy? — Both need approval artifact — automate collection.**
2. **Config drift? — Detect and remediate — drift is unauthorized change.**

### Common Mistakes in Interviews

- Deploy without ticket reference
- Approvals after deploy timestamp
- Infrastructure changed outside pipeline

---

## Q051: Acquisition Day One Connectivity

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Acquisition Integration |
| **Frequency** | Very Common |

### Question

Plan Day One technical connectivity after acquisition.

### Short Answer (30 seconds)

SSO federation, network VPN/ExpressRoute, security baseline assessment, data classification, no production merge — coexist with controlled integration paths.

### Detailed Answer (3–5 minutes)

**Day 1 priorities:**
1. Identity federation (Entra trust)
2. Secure network connectivity
3. Security scan acquired assets
4. Communication tools integration
5. Freeze risky changes both sides

**Architect:** Integration factory playbook — not bespoke per acquisition panic.

### Architecture Perspective

Day One is connectivity and security — not data merge.

### Follow-up Questions

1. **Data merge timeline? — Months — MDM golden record ADR first.**
2. **Cultural? — Separate standups initially — integration fatigue real.**

### Common Mistakes in Interviews

- Big-bang merge databases Day 1
- Skip security assessment acquired systems
- No integration program office

---

## Q052: Acquisition Identity Federation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Acquisition Integration |
| **Frequency** | Common |

### Question

Federate identity between acquirer and acquired company.

### Short Answer (30 seconds)

Entra ID cross-tenant B2B; SAML trust to acquired IdP; unified email optional later; SCIM provisioning where possible; guest lifecycle policy.

### Detailed Answer (3–5 minutes)

**Architecture:**
```
Acquired IdP ←SAML/OIDC→ Acquirer Entra (broker) → Apps
```

**Phased:** Guest access first; migrated accounts later.

**Architect:** Identity is first integration — enables tool access without password sync.

### Architecture Perspective

Identity federation reduces Day One friction — architects prioritize.

### Follow-up Questions

1. **Duplicate mailboxes? — UPN conflict resolution plan.**
2. **Offboarding acquired users? — Lifecycle sync on divestiture too.**

### Common Mistakes in Interviews

- Password hash export/import
- Permanent dual identity no consolidation plan
- No guest access review quarterly

---

## Q053: Executive Briefing One-Pager

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Executive Briefings |
| **Frequency** | Very Common |

### Question

Structure one-page executive brief for architecture decision.

### Short Answer (30 seconds)

Problem, recommendation, investment, timeline, risks, decision needed — max one page; visual optional single diagram; no jargon.

### Detailed Answer (3–5 minutes)

**Sections:**
1. **Decision needed by [date]**
2. **Problem** (2 sentences business impact)
3. **Recommendation** (1 sentence)
4. **Investment** Year 1 / 3-year TCO
5. **Top 3 risks** + mitigation one-liner
6. **Alternatives considered** (table 3 rows)

**Architect:** One-pager sent 24h before meeting — meeting for decision.

### Architecture Perspective

Executives read one page — architects respect time.

### Follow-up Questions

1. **Appendix? — Technical depth separate — available if asked.**
2. **Metric? — '$2M revenue at risk' beats 'latency bad'.**

### Common Mistakes in Interviews

- 10-page architecture doc as 'executive summary'
- No explicit decision ask
- Only technical option presented

---

## Q054: Executive Trade-off Table

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Executive Briefings |
| **Frequency** | Common |

### Question

Present architecture options as executive trade-off table.

### Short Answer (30 seconds)

Columns: Option, Cost, Time, Risk, Strategic fit; highlight recommended row; quantify where possible.

### Detailed Answer (3–5 minutes)

**Example:**
| Option | Cost Y1 | Time | Risk | Fit |
| Buy SaaS | $400K | 3mo | Vendor lock | Fast |
| Build | $1.2M | 12mo | Delivery | Control |
| Extend legacy | $200K | 6mo | Tech debt ↑ | Short-term |

**Architect:** Facilitate decision — not overwhelm with 10 options.

### Architecture Perspective

Trade-off tables enable informed executive choice.

### Follow-up Questions

1. **Do nothing option? — Include cost of inaction — often strongest motivator.**
2. **Sensitivity? — 'If traffic 2×, Option A breaks' — scenario row.**

### Common Mistakes in Interviews

- Single option masquerading as choice
- Unquantified 'high risk' labels
- Recommendation buried page 8

---

## Q055: Azure Well-Architected Review

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reference Architectures |
| **Frequency** | Very Common |

### Question

Use Azure Well-Architected Framework to assess workload architecture.

### Short Answer (30 seconds)

Review five pillars: reliability, security, cost, operational excellence, performance; identify high-risk findings; prioritize remediation; document in WAF assessment report.

### Detailed Answer (3–5 minutes)

**Process:**
1. Workshop per pillar with checklist
2. Score risks High/Medium/Low
3. Remediation backlog with owners
4. Re-assess quarterly

**Architect:** WAF assessment linked to ADRs — findings become tracked work.

### Architecture Perspective

WAF is common enterprise reference — architects speak pillar language.

### Follow-up Questions

1. **Reliability pillar? — HA, DR, SLO — maps to Week 42 DR topics.**
2. **Cost pillar? — FinOps right-sizing — not afterthought.**

### Common Mistakes in Interviews

- WAF once at launch never revisited
- Checklist without system-specific context
- Findings not tracked to closure

---

## Q056: Cloud Adoption Framework Landing Zone

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Reference Architectures |
| **Frequency** | Common |

### Question

Explain Microsoft CAF landing zone architecture for enterprise Azure.

### Short Answer (30 seconds)

Enterprise-scale foundation: management groups, policy, hub-spoke network, identity, logging, security baseline — workloads deploy into landing zone not raw subscriptions.

### Detailed Answer (3–5 minutes)

**Components:**
- **Identity** — Entra tenant structure
- **Network** — Hub firewall, spoke VNets
- **Governance** — Azure Policy, RBAC
- **Security** — Defender, Key Vault

**Architect:** New workloads inherit landing zone — custom VPC per project anti-pattern.

### Architecture Perspective

Landing zone is enterprise reference architecture — accelerates compliant deploys.

### Follow-up Questions

1. **Platform team? — Owns landing zone; app teams deploy spokes.**
2. **Policy exceptions? — Documented waiver with expiry.**

### Common Mistakes in Interviews

- Every team custom subscription no policies
- No central logging subscription
- Hub-spoke bypassed for 'speed'

---

## Q057: Regulated CAB Change Process

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Regulated Change Control |
| **Frequency** | Very Common |

### Question

Describe Change Advisory Board process for regulated production changes.

### Short Answer (30 seconds)

Standard change pre-approved; normal change CAB review; emergency change post-review; all linked to ticket; segregation of duties; deployment window restrictions.

### Detailed Answer (3–5 minutes)

**CAB packet:**
- Risk assessment
- Rollback plan
- Test evidence
- Affected systems
- Communication plan

**Architect:** Architecture changes affecting SOX/PHI systems require enhanced CAB tier.

### Architecture Perspective

CAB is operational governance — architects supply rollback and test evidence.

### Follow-up Questions

1. **Emergency CAB? — Smaller quorum — retrospective within 48h mandatory.**
2. **Standard changes? — Pipeline deploy infra template — pre-authorized catalog.**

### Common Mistakes in Interviews

- CAB approves without rollback plan
- Emergency change no retrospective
- Developer presents own change as sole approver

---

## Q058: GxP Validated System Changes

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Regulated Change Control |
| **Frequency** | Common |

### Question

Manage architecture changes in GxP validated systems.

### Short Answer (30 seconds)

Change categorized by validation impact; IQ/OQ/PQ re-execution scope determined; CSV documentation; QA approval; audit trail; no uncontrolled prod changes.

### Detailed Answer (3–5 minutes)

**Impact assessment:**
- **Low** — documentation update only
- **Medium** — partial revalidation
- **High** — full revalidation cycle

**Architect:** GxP systems flagged in catalog — pipeline blocks deploy without QA gate.

### Architecture Perspective

Pharma/med device architects must know CSV impact on changes.

### Follow-up Questions

1. **21 CFR Part 11? — Electronic records/signatures — audit trail architecture.**
2. **Cloud in GxP? — Vendor qualification + intended use documentation.**

### Common Mistakes in Interviews

- Deploy GxP app like consumer SaaS
- Skip impact assessment
- No QA sign-off in pipeline

---

## Q059: Omnichannel Customer Identity

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Omnichannel |
| **Frequency** | Very Common |

### Question

Unify customer identity across web, mobile, store, and call center.

### Short Answer (30 seconds)

Customer MDM golden profile; single customer ID; link loyalty, online account, POS profile; consent and preference center unified.

### Detailed Answer (3–5 minutes)

**Architecture:**
```
Web/Mobile/POS/CallCenter → Customer API → MDM Golden Record
```

**Challenges:**
- Guest checkout merge on account create
- Store loyalty card link online
- GDPR consent sync all channels

**Architect:** Identity is omnichannel foundation — without it channels stay silos.

### Architecture Perspective

Omnichannel breaks at identity — architects prioritize MDM early.

### Follow-up Questions

1. **Identity resolution? — Probabilistic match — manual review queue for conflicts.**
2. **Call center auth? — Out-of-band verify before show order history.**

### Common Mistakes in Interviews

- Separate customer IDs per channel forever
- Store can't lookup online order
- Merge accounts without verification

---

## Q060: Omnichannel Inventory ATP

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Omnichannel |
| **Frequency** | Common |

### Question

Provide accurate available-to-promise inventory across channels.

### Short Answer (30 seconds)

Real-time inventory service fed by ERP/WMS events; reservation on add-to-cart; ATP = on-hand − reserved − safety stock; store-level granularity for BOPIS.

### Detailed Answer (3–5 minutes)

**Event flow:**
```
WMS adjustment → Service Bus → Inventory Service → Cache → Channels
```

**Architect:** Never synchronous SAP query in checkout — cache with TTL and event refresh.

### Architecture Perspective

ATP wrong = oversell or lost sale — architecture event-driven.

### Follow-up Questions

1. **BOPIS reservation? — TTL 30 min hold — release on timeout.**
2. **Ship-from-store? — Store inventory decrements on ship confirm not web order.**

### Common Mistakes in Interviews

- Nightly batch inventory sync only
- Separate ATP web vs store
- No reservation — oversell at peak

---

## Q061: ERP Integration Anti-Corruption Layer

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Supply Chain |
| **Frequency** | Very Common |

### Question

Place anti-corruption layer between e-commerce and ERP (SAP).

### Short Answer (30 seconds)

Canonical domain model in integration layer; ERP adapter translates; e-commerce never imports SAP IDoc structures; version ERP adapter independently.

### Detailed Answer (3–5 minutes)

**Pattern:**
```
Order Service → Canonical Order → ACL → SAP BAPI/IDoc
```

**Benefits:**
- ERP upgrade isolates impact
- Testable translation logic
- Clear system of record boundaries

**Architect:** ACL is strangler enabler for ERP replacement.

### Architecture Perspective

ACL prevents ERP model leaking into customer experience services.

### Follow-up Questions

1. **iPaaS vs custom ACL? — Logic Apps/MuleSoft for standard; custom for complex mapping.**
2. **Idempotency? — ERP post duplicate detection keys.**

### Common Mistakes in Interviews

- SAP structures in React frontend DTOs
- Synchronous BAPI in checkout path
- No ACL — direct ERP coupling

---

## Q062: Supply Chain Event-Driven Sync

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Supply Chain |
| **Frequency** | Very Common |

### Question

Sync supply chain master data event-driven instead of batch-only.

### Short Answer (30 seconds)

Product/price/inventory changes publish events; subscribers update caches and search index; batch reconciliation nightly catches drift.

### Detailed Answer (3–5 minutes)

**Events:**
- `ProductUpdated`, `PriceChanged`, `InventoryAdjusted`, `ShipmentDispatched`

**Hub:** Kafka or Service Bus topics with schema registry.

**Architect:** Async default — batch for historical backfill only.

### Architecture Perspective

Event-driven supply chain reduces staleness vs nightly batch.

### Follow-up Questions

1. **Ordering? — Partition by productId — per-product sequence.**
2. **Poison message? — DLQ + alert — don't block pipeline.**

### Common Mistakes in Interviews

- Only nightly ETL — intraday price stale
- No reconciliation job
- Events without schema versioning

---

## Q063: HIPAA Audit Log Retention

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | HIPAA |
| **Frequency** | Common |

### Question

Architect audit log retention for HIPAA compliance.

### Short Answer (30 seconds)

Immutable audit logs 6+ years; tamper-evident storage; who accessed what PHI when; SIEM correlation; legal hold capability.

### Detailed Answer (3–5 minutes)

**Implementation:**
- WORM storage or append-only log analytics
- Cloud audit logs + app-level PHI access log
- Time sync NTP across systems

**Architect:** Retention policy in ADR — deletion schedules must not apply to audit logs prematurely.

### Architecture Perspective

Audit retention is HIPAA Security Rule requirement — architects specify years.

### Follow-up Questions

1. **Break-glass logs? — Higher scrutiny retention and review SLA.**
2. **Log integrity? — Hash chain or immutable blob storage.**

### Common Mistakes in Interviews

- Audit logs deletable by admin
- 90-day retention only
- Clock skew breaks audit timeline

---

## Q064: PHI De-Identification Pipeline

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | PHI Boundaries |
| **Frequency** | Common |

### Question

Build de-identification pipeline before analytics zone.

### Short Answer (30 seconds)

Apply HIPAA Safe Harbor or Expert Determination; strip 18 identifiers; k-anonymity for datasets; separate analytics account with no PHI network path.

### Detailed Answer (3–5 minutes)

**Pipeline:**
```
PHI DB → ETL De-ID → Analytics Lake (no re-identification keys stored together)
```

**Architect:** Re-identification risk assessment before sharing datasets externally.

### Architecture Perspective

De-ID is boundary enabler — analytics without PHI zone access.

### Follow-up Questions

1. **Expert Determination? — Statistician sign-off for retained fields.**
2. **Tokenization for analytics? — Reversible tokens stored separately with access control.**

### Common Mistakes in Interviews

- Raw PHI copied to Power BI
- Zip code + DOB retained — re-identification easy
- Analytics team VPN into PHI DB

---

## Q065: PCI Token Vault Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | PCI Scope |
| **Frequency** | Common |

### Question

Design token vault interaction without merchant storing PAN.

### Short Answer (30 seconds)

PSP vault tokenizes at capture; merchant stores PSP token reference; charge API uses token; vault HSM in CDE if self-hosted — rare for merchants.

### Detailed Answer (3–5 minutes)

**Flows:**
- Create token via PSP.js
- Server charges `pm_xxx` off-session
- Webhooks confirm payment state

**Architect:** Vault boundary diagram for QSA — merchant never persists PAN.

### Architecture Perspective

Token vault architecture is PCI scope minimization core.

### Follow-up Questions

1. **Network tokens? — Scheme-level — higher auth rates mobile wallets.**
2. **Token reuse? — Merchant-scoped — can't use across merchants.**

### Common Mistakes in Interviews

- Encrypt PAN instead of tokenize
- Tokens in mobile app logs
- Webhook events not verified

---

## Q066: Retail Graceful Degradation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Retail Peak |
| **Frequency** | Common |

### Question

Define graceful degradation priorities during retail overload.

### Short Answer (30 seconds)

Protect checkout and payment first; disable recommendations, reviews, personalization; serve cached catalog; simplify product pages.

### Detailed Answer (3–5 minutes)

**Priority tiers:**
1. Checkout + payment (never degrade)
2. Add to cart + cart view
3. Product detail
4. Search (cached)
5. Recommendations (off first)

**Architect:** Feature flags pre-configured degradation playbook — ops flip in war room.

### Architecture Perspective

Graceful degradation preserves revenue path — architects pre-rank features.

### Follow-up Questions

1. **Kill switch tested? — Game day disables tier 5 — verify checkout OK.**
2. **Browse-only mode? — Queue checkout but allow browse — revenue partial.**

### Common Mistakes in Interviews

- Disable checkout before recommendations
- Degradation decided ad hoc in incident
- No flags for non-critical features

---

## Q067: Multi-Tenant Noisy Neighbor

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Multi-Tenant |
| **Frequency** | Common |

### Question

Mitigate noisy neighbor tenant in shared infrastructure.

### Short Answer (30 seconds)

Per-tenant rate limits; fair queue scheduling; dedicated pool for enterprise tier; monitor tenant QPS/storage outliers; auto-throttle abuser.

### Detailed Answer (3–5 minutes)

**Controls:**
- API gateway quota per tenantId
- K8s ResourceQuota per tenant namespace
- DB connection pool cap per tenant

**Architect:** Noisy neighbor detection dashboard — SRE alerts on tenant skew.

### Architecture Perspective

Multi-tenant fairness is reliability architecture — one tenant can DDOS others.

### Follow-up Questions

1. **Enterprise silo? — Move hot tenant to dedicated shard automatically.**
2. **Billing tie-in? — Usage metrics feed billing and limits.**

### Common Mistakes in Interviews

- Unlimited API calls all tenants
- Single tenant batch job starves others
- No per-tenant monitoring

---

## Q068: ARB Exception Registry

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Architecture Review Board |
| **Frequency** | Common |

### Question

Maintain architecture review exception registry.

### Short Answer (30 seconds)

Exception ID, system, control waived, compensating control, approver, expiry date, review cadence — no permanent exceptions without re-approval.

### Detailed Answer (3–5 minutes)

**Example:**
| EX-042 | Legacy API no mTLS | IP allowlist + VPN | CISO | 2025-12-31 |

**Architect:** Expired exceptions block deploy pipeline — automated check.

### Architecture Perspective

Exception registry prevents 'temporary' waivers becoming permanent risk.

### Follow-up Questions

1. **Compensating control? — Must be measurable — not 'we'll watch it'.**
2. **Audit? — Quarterly exception review in ARB minutes.**

### Common Mistakes in Interviews

- Verbal waiver no record
- Permanent exception no expiry
- Exception registry not linked to CMDB

---

## Q069: Pen Test Remediation Tracking

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | Compliance Audits |
| **Frequency** | Common |

### Question

Track penetration test findings in architecture governance.

### Short Answer (30 seconds)

Findings logged risk register; severity SLA (critical 30d); ADR for architectural fixes; retest verification; evidence for next audit.

### Detailed Answer (3–5 minutes)

**Critical finding example:** IDOR cross-tenant orders → fix tenant middleware → pen test retest pass → close finding.

**Architect:** Pen test is architecture validation — findings feed roadmap priority.

### Architecture Perspective

Open critical pen findings block production for regulated tiers.

### Follow-up Questions

1. **Dev pen test vs prod? — Prod rules of engagement — staging mirrors prod.**
2. **False positive? — Document accepted risk with CISO sign-off.**

### Common Mistakes in Interviews

- Pen test PDF shelved
- Critical open 6 months
- Fix in app only not architecture root cause

---

## Q070: GDPR Data Portability Export

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Intermediate |
| **Category** | GDPR |
| **Frequency** | Common |

### Question

Implement GDPR data portability export API.

### Short Answer (30 seconds)

Machine-readable export (JSON); all personal data across services orchestrated; user-authenticated request; SLA 30 days; secure download link expires.

### Detailed Answer (3–5 minutes)

**Orchestration:**
```
Export Service → parallel fetch CRM, Orders, Support → zip JSON → signed URL
```

**Architect:** Export is cross-service workflow — not manual support ticket.

### Architecture Perspective

Portability proves data architecture visibility — can you find all PII?

### Follow-up Questions

1. **Format? — JSON common; XML if sector standard.**
2. **Third-party data? — Include processed data; note non-exportable derived analytics.**

### Common Mistakes in Interviews

- PDF only export — not machine-readable
- Partial export missing microservices
- Unauthenticated export endpoint

---
