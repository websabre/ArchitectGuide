# Week 44 — Expert Scenario Q&A

> Q101–Q120: Premium format (Week 1 quality).

---


## Q101: Scenario HIPAA Breach Cloud Misconfig

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Enterprise Case Studies |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Monday 06:00: Security alert — public S3-equivalent blob container exposed patient PDFs 72 hours. Media not yet aware. CISO, legal, and engineering on bridge. Architect immediate actions and remediation architecture?

### Short Answer (30 seconds)

Contain exposure, preserve forensics, notify legal for breach assessment timeline, rotate keys, audit access logs, fix IAM, implement policy-as-code prevention — document for OCR if reportable.

### Detailed Answer

**First 4 hours:**
1. **Contain** — remove public access, block exfil IPs if suspicious
2. **Preserve** — snapshot logs, don't delete evidence
3. **Scope** — how many records, which patients, download audit
4. **Legal** — breach assessment 60-day OCR clock if >500 individuals likely
5. **Notify pipeline** — internal exec, prepare patient notification if required

**Root cause architecture:**
- Missing Azure Policy deny public storage
- No continuous compliance scan
- Dev copied prod export to wrong account

**Permanent controls:**
- Policy-as-code mandatory
- Data loss prevention scan outbound
- PHI classification tags enforced
- Break-glass export workflow with approval

**Comms:** Engineering facts to legal — legal owns external notification timing.

### Architecture Perspective

Expert HIPAA scenario tests breach response + preventive architecture — not only 'make bucket private'.

### Follow-up Questions

1. **BAA notification? — Notify cloud BA per contract timeline — separate from OCR.**
2. **Forensics? — Chain of custody — don't wipe logs prematurely.**

### Common Mistakes in Interviews

- Delete bucket to hide evidence
- Engineering sends patient emails before legal assessment
- Fix bucket only — no policy prevention

---

## Q102: Scenario PCI Scope Expansion

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Enterprise Case Studies |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

QSA discovers checkout server logged full payment API responses including masked PAN patterns — declares expanded PCI scope. Release freeze 3 weeks before holiday. Architect remediation path?

### Short Answer (30 seconds)

Stop logging payment payloads immediately; log scrubbing middleware; scope re-assessment with QSA; token-only architecture verification; SAQ reclassification plan; staged audit re-run.

### Detailed Answer

**Immediate (48h):**
1. Deploy log redaction — strip payment fields at ingest
2. Purge retained logs with PAN per retention policy (legal approved)
3. Verify no PAN in APM traces, error reports, support tickets

**Architecture remediation:**
- Never log request/response bodies payment endpoints
- Structured logging allowlist fields only
- PSP iframe confirmed — SAQ A/A-EP path
- Network segmentation evidence for QSA

**Timeline negotiation:**
- Critical fix before holiday
- Full re-audit Q1 — documented remediation plan for QSA sign-off on interim controls

**Stakeholders:** CFO cares audit cost; engineering owns technical fix.

### Architecture Perspective

PCI scope surprise is architect failure in logging design — expert covers containment and QSA relationship.

### Follow-up Questions

1. **Masked PAN in logs? — Still sensitive — QSA may still flag — full redaction.**
2. **Developer debug habit? — Architecture blocks body logging in prod via framework.**

### Common Mistakes in Interviews

- Encrypt logs instead of remove PAN
- Blame PSP for merchant logging
- Ignore QSA until after holiday

---

## Q103: Scenario Black Friday Checkout Meltdown

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Enterprise Case Studies |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Black Friday 10:00 ET: checkout error rate 40%, virtual queue not activated, inventory overselling, CEO demanding answers. Payment vendor green. Your architecture war room — priority actions?

### Short Answer (30 seconds)

Activate waiting room, enable degradation flags, scale payment bulkhead, freeze non-critical deploys, stop oversell via inventory reservation fix, war room comms — root cause after stabilization.

### Detailed Answer

**Stabilize (0–30 min):**
1. Enable **virtual waiting room** — cap checkout RPS to sustainable
2. Feature flags: off recommendations, personalization, reviews
3. Scale payment path nodes + connection pools pre-tested limits
4. **Inventory:** enable reservation hard lock — stop oversell immediately
5. Freeze all deploys except hotfix

**Diagnose parallel:**
- DB connection pool exhaustion vs PSP timeout vs cart service memory
- Compare to load test baseline — what exceeded model

**Comms:**
- Every 15 min business metrics: conversion rate recovering?
- Post-mortem blameless after peak

**Prevention (already should exist):**
- Game day passed? If not — honest post-mortem finding
- Autoscale lag — pre-warm nodes next year

### Architecture Perspective

Retail peak expert scenario tests war room prioritization — revenue path first.

### Follow-up Questions

1. **PSP green but checkout fails? — Client-side or merchant server — don't fix wrong layer.**
2. **Oversell legal? — Stop sales channel if can't honor — exec decision documented.**

### Common Mistakes in Interviews

- Scale entire monolith blindly without bottleneck analysis
- Activate queue after hours of outage only
- Continue feature deploys during incident

---

## Q104: Scenario Cross-Tenant Data Leak

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Enterprise Case Studies |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Security researcher reports Tenant A API returns Tenant B invoice by changing UUID. Production SaaS 500 tenants. Architect containment and systemic fix?

### Short Answer (30 seconds)

Disable affected endpoint, forensics on access logs, notify legal/customers if confirmed, emergency patch tenant middleware, full cross-tenant integration test suite, external pen retest.

### Detailed Answer

**Containment:**
1. Feature flag off invoice export OR hotfix tenant filter
2. Access log review — any B data accessed by A tenants?
3. Customer notification if confirmed breach — legal drives

**Root cause classes:**
- Missing `WHERE tenantId` in repository
- Cache key without tenant prefix
- Background job wrong tenant context

**Systemic fix:**
- ORM interceptor mandatory tenant filter
- DB RLS as defense in depth
- CI cross-tenant negative tests required
- Pen test retest before reopen

**Governance:** ARB exception revoked — mandatory tenant middleware on all new APIs.

### Architecture Perspective

Cross-tenant leak is existential SaaS incident — expert covers forensics and prevention architecture.

### Follow-up Questions

1. **UUID security? — UUID not secret — always authorize tenant match.**
2. **Researcher bounty? — Coordinate disclosure timeline — fix before public.**

### Common Mistakes in Interviews

- Patch one query only without systemic test
- Notify all tenants before confirming scope
- Skip pen retest 'because one line fix'

---

## Q105: Scenario GDPR Erasure Partial Failure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Enterprise Case Studies |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

GDPR erasure request: CRM deleted user but analytics warehouse and backup tapes retain PII 30 days later. DPO escalates. Architect orchestration fix?

### Short Answer (30 seconds)

Map all processing systems in ROPA; event-driven erasure fan-out; backup crypto-shred or exclusion policy; erasure completion dashboard; vendor deletion API calls.

### Detailed Answer

**Immediate:**
1. Manual delete/anonymize analytics records
2. Mark backups for exclusion or accelerated expiry per legal
3. Respond DPO with remediation timeline

**Architecture:**
```
Erasure Orchestrator → CRM, Orders, Support, Analytics, Search, Backups, Vendors
```
- Idempotent `UserErased` event
- Per-system acknowledgment tracked
- SLA dashboard — none complete until all green

**Backup strategy:**
- Encrypted backups with key deletion on erasure (crypto-shred)
- Or legal hold exception documented

**Vendor:**
- Salesforce/Marketo deletion API in workflow

**Prevention:** ROPA linked to automated erasure subscribers list — new service must subscribe before prod.

### Architecture Perspective

Erasure partial failure is common — expert architects orchestration not single-system delete.

### Follow-up Questions

1. **Anonymize vs delete analytics? — Legal guidance — aggregates may remain if truly anonymized.**
2. **Legal hold? — Block erasure with documented reason — inform data subject.**

### Common Mistakes in Interviews

- CRM-only erasure workflow
- Backups ignored in erasure design
- No completion tracking per system

---

## Q106: Scenario SOX Emergency Prod Change

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Enterprise Case Studies |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Month-end close: GL export job failed. Developer wants direct prod DB fix tonight. SOX controls normally block. Architect decision framework?

### Short Answer (30 seconds)

Allow emergency change with break-glass, dual approval, ticket, logging, limited scope SQL, mandatory retrospective and control evidence within 48h — never bypass audit trail.

### Detailed Answer

**Framework:**
1. **Severity** — financial reporting deadline material? Yes → emergency path
2. **Break-glass** — PIM elevation + CFO delegate approval
3. **Scope** — read-only diagnosis first; write minimal fix script in version control
4. **Evidence** — record SQL, approvers, timestamp, before/after row counts
5. **Retrospective** — ARB/CAB 48h — root cause automation fix

**Architecture long-term:**
- Idempotent GL export replay job
- Monitoring alert before month-end deadline
- No standing prod DB access for developers

**Reject:** ad hoc undocumented SQL even under pressure.

### Architecture Perspective

SOX expert scenario balances business urgency vs control integrity.

### Follow-up Questions

1. **Automated replay? — Preferred over manual SQL — design for recovery.**
2. **Segregation? — Fix executor ≠ approver even emergency.**

### Common Mistakes in Interviews

- Undocumented prod SQL to save time
- Skip retrospective because month-end stress
- Disable pipeline permanently after one emergency

---

## Q107: Scenario Acquisition Identity Collision

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Enterprise Case Studies |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Post-acquisition: 40% users share email domain collision between acquirer and acquired Entra tenants. SSO project stalled 3 months. Architect integration path?

### Short Answer (30 seconds)

Phased B2B federation, UPN suffix strategy, guest vs migrated account policy, SCIM provisioning plan, customer communication for duplicate consumer emails separately.

### Detailed Answer

**Technical path:**
1. **B2B trust** — acquired users as guests initially
2. **UPN strategy** — `@acquired.legacy` suffix vs `@corp.com` migration waves
3. **Collision handling** — duplicate email different person — manual merge queue
4. **SCIM** — automate guest lifecycle
5. **Apps** — claims mapping unified groups

**Not:** force password hash import day one.

**Program:** Identity workstream lead + HR data for employee mapping.

**Timeline:** Guests month 1; migration waves months 2–6.

### Architecture Perspective

M&A identity is slow — expert resists big-bang unified directory.

### Follow-up Questions

1. **Customer vs employee identity? — Separate collision problem — B2C merge different project.**
2. **Divestiture? — Design reversible federation — exit plan.**

### Common Mistakes in Interviews

- Force unified tenant weekend cutover
- Ignore duplicate email different humans
- No guest access review process

---

## Q108: Scenario ARB Bypass Audit Finding

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Enterprise Case Studies |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

External audit finds Tier-0 payment system deployed without ARB approval. System live 8 months processing $50M/month. Architect remediation for auditors and prevention?

### Short Answer (30 seconds)

Retroactive architecture review, risk assessment, compensating controls, ADR backlog, exception documentation, pipeline gate blocks future bypass — honest timeline to auditors.

### Detailed Answer

**Remediation:**
1. **Retro ARB** within 30 days — full packet as-if pre-prod
2. **Risk assessment** — what controls missed — pen test if needed
3. **ADR** documenting as-is architecture and known gaps
4. **Compensating controls** for any ARB conditions
5. **Process fix** — service catalog blocks prod deploy without ARB ticket ID

**Auditor comms:**
- Acknowledge control failure
- Show remediation completed + monitoring
- No false claim ARB occurred

**Prevention:**
- CI/CD checks ARB approval artifact
- Quarterly compliance scan Tier-0 systems vs ARB log

### Architecture Perspective

Retroactive ARB is painful but required — expert handles audit honesty.

### Follow-up Questions

1. **Rip and replace? — Usually overreaction — assess risk first.**
2. **Blame team? — Blameless — fix system allowing bypass.**

### Common Mistakes in Interviews

- Fabricate retroactive ARB minutes
- Ignore finding as bureaucracy
- No pipeline gate after finding

---

## Q109: Scenario Vendor SaaS Outage Dependency

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Enterprise Case Studies |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Identity SaaS outage 4 hours — all internal and customer apps login broken. Single vendor Okta/Entra dependency. Board asks mitigation plan. Architect response?

### Short Answer (30 seconds)

Immediate workarounds, comms, post-incident vendor review, architecture mitigations: cached session extension, break-glass local admin, multi-vendor strategy assessment, DR identity runbook.

### Detailed Answer

**Immediate:**
- Extend existing sessions if possible
- Break-glass emergency admin accounts (pre-staged, audited)
- Status page comms — ETA from vendor
- Delay non-critical maintenance

**Short-term architecture:**
- Session TTL balance — not infinite
- Critical apps evaluate offline mode read-only

**Long-term options (ADR):
1. Multi-region IdP config (same vendor)
2. Secondary IdP cold standby (expensive)
3. Federation to backup IdP for Tier-0 only
4. Accept risk with SLA credits — document board decision

**Board message:** Identity is Tier-0 — investment in resilience vs cost quantified.

### Architecture Perspective

Vendor concentration incident — expert balances immediate ops and strategic architecture.

### Follow-up Questions

1. **Cache sessions offline? — Limited — security vs availability trade-off.**
2. **Vendor SLA? — Financial credit doesn't restore login — technical mitigation needed.**

### Common Mistakes in Interviews

- No break-glass accounts ever created
- Promise multi-vendor next week unrealistic
- Hide single vendor dependency from board

---

## Q110: Scenario EU Customer US Processing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Enterprise Case Studies |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

EU enterprise customer audit finds their data processed in US Azure region despite contract EU-only. $2M ARR at risk. Architect remediation timeline?

### Short Answer (30 seconds)

Stop new EU processing US immediately, data migration plan to EU stamp, Transfer Impact Assessment, SCCs update, geo-routing fix, customer communication with verified timeline.

### Detailed Answer

**Week 1:**
- **Contain** — route EU tenants EU region only
- Inventory all EU customer data locations — CMDB + billing

**Month 1–3:**
- Migrate data EU region — downtime windows per tenant
- Update IaC policy deny EU customer US deploy
- Gateway geo-routing enforcement

**Legal:**
- TIA documentation Schrems II
- DPA amendment

**Architecture:**
- Tenant metadata `region=EU` drives deploy
- Global control plane no PII

**Customer:** Verified migration schedule + third-party audit letter.

### Architecture Perspective

GDPR residency violation is revenue-threatening — expert gives phased technical+legal plan.

### Follow-up Questions

1. **Backup US? — EU backups EU region only — verify restore paths.**
2. **Support US staff? — Access controls — EU data accessed from EU or SCC-covered.**

### Common Mistakes in Interviews

- Hide US processing from customer
- Migrate without geo-routing enforcement — reoccurrence
- Promise 48h migration unrealistic

---

## Q111: Scenario Omnichannel Inventory Oversell Crisis

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Enterprise Case Studies |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Viral product launch: web shows 500 available, 2000 orders placed, WMS shows 300 units. Social media outrage. Architect immediate and structural fix?

### Short Answer (30 seconds)

Pause sales, honor policy decision, fix reservation architecture, event-driven ATP, disable stale cache, communicate — structural hard reservation at add-to-cart.

### Detailed Answer

**Immediate:**
1. **Stop sale** — feature flag product unavailable
2. **Allocate** — business decides fulfill partial cancel rest compensation
3. **Fix** — enable hard reservation decrement on add-to-cart commit
4. **Cache** — invalidate ATP cache; reduce TTL to 30s until stable

**Structural:**
```
AddToCart → Reserve API (sync) → WMS/Inventory lock → Confirm on payment
```
- Idempotent reservation tokens
- Event sync ERP/WMS
- Oversell monitoring alert

**Post-mortem:** Batch inventory sync inadequate for hype SKU — ADR event-driven ATP.

### Architecture Perspective

Omnichannel oversell is architecture failure — reservation sync expert answer.

### Follow-up Questions

1. **Soft reservation? — Cart hold vs hard — hard for low stock hype products.**
2. **Store inventory? — Include in ATP — BOPIS race conditions.**

### Common Mistakes in Interviews

- Honor 2000 orders with 300 units without business exec decision
- Blame WMS only — web oversold independently
- Increase cache TTL to reduce load — worsens stale

---

## Q112: Scenario Supply Chain ERP Blocking Checkout

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Enterprise Case Studies |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Checkout p99 8s because team added synchronous SAP pricing call in payment path. Peak season 2 weeks away. Architect refactor under time pressure?

### Short Answer (30 seconds)

Remove sync SAP from hot path immediately; use cached price with TTL; async price validation post-order; anti-corruption layer already should exist — hotfix then proper event-driven pricing.

### Detailed Answer

**Hotfix (this week):**
1. Read price from Redis cache populated by nightly + event incremental
2. Checkout uses cache price — disclaimer rare sync validation async
3. Post-order job validates price — refund/adjust if mismatch policy

**Proper (next sprint):**
- Pricing Service subscribes `PriceChanged` events from ERP ACL
- SLA: price freshness <5 min
- Monitoring stale price age

**Never:** synchronous SAP in user request path — architect should have blocked in review.

### Architecture Perspective

SAP-in-checkout is classic anti-pattern — expert removes from path under pressure.

### Follow-up Questions

1. **Price mismatch? — Business rule honor cached or cancel — legal/commercial decision.**
2. **Load test? — Prove p99 <300ms before peak with cache path.**

### Common Mistakes in Interviews

- Optimize SAP call instead of remove from path
- Skip load test due to time pressure
- Direct SAP coupling accepted in ARB

---

## Q113: Scenario Executive Rejects Architecture Recommendation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Enterprise Case Studies |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

You recommended BFF + OIDC cookie pattern. CTO chose SPA direct-to-microservices with tokens in memory for speed. Security and you disagree. How proceed as architect?

### Short Answer (30 seconds)

Document dissent in ADR, implement requested design with compensating controls, define metrics and review trigger, maintain professional relationship — not block silently or sabotage.

### Detailed Answer

**Actions:**
1. **ADR** records decision, your recommendation, risks accepted by CTO sign-off
2. **Compensating controls** — short TTL, aggressive CSP, pen test scope expanded
3. **Metrics** — XSS incidents, token theft simulations, auth failure rates
4. **Review trigger** — 'Revisit if microservices >8 or pen test critical XSS'
5. **Delivery** — implement decision fully — no passive resistance

**Escalation:** If regulatory Tier-0 (PCI/PHI), escalate to CISO with written risk — architect duty.

**Interview point:** Influence without authority — document and measure.

### Architecture Perspective

Expert tests architect professionalism when overruled — document dissent not deadlock.

### Follow-up Questions

1. **Regulated tier? — Some decisions aren't CTO-only — know escalation path.**
2. **Sabotage? — Never — destroys trust and career.**

### Common Mistakes in Interviews

- Refuse to implement CTO decision
- No written record of risk acceptance
- Implement half BFF half direct silently

---

## Q114: Scenario Reference Architecture Mandated Wrong Fit

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Enterprise Case Studies |
| **Frequency** | Uncommon |
| **Type** | Scenario |

### Question

Enterprise EA mandates CAF landing zone hub-spoke for 3-person startup acquisition product needing rapid iteration. Product VP revolts. Architect mediation?

### Short Answer (30 seconds)

Propose tiered governance: acquisition product on lightweight subscription with core policies only; roadmap to landing zone alignment; document exceptions with expiry; don't apply full EA tax day one.

### Detailed Answer

**Mediation framework:**
1. **Acknowledge EA value** at enterprise scale
2. **Assess acquisition context** — speed to market, team size, revenue timeline
3. **Proposal:** Tier-2 landing zone lite — security baseline policies, not full hub-spoke day 1
4. **Exception registry** — 12 month convergence plan
5. **Metrics** — when triggers full landing zone (revenue, data class, team size)

**Deliverable:** Gap analysis + phased adoption ADR — EA and product both sign.

**Avoid:** political victory only for one side.

### Architecture Perspective

Expert scenario tests pragmatic EA — standards with proportionality.

### Follow-up Questions

1. **Startup in enterprise? — Common acquisition pattern — integration factory handles tiers.**
2. **Security minimum? — Non-negotiable baseline even lite — MFA, no public DB.**

### Common Mistakes in Interviews

- Force full landing zone blocking launch 6 months
- Abandon all standards — acquisition wild west
- No expiry on exception — permanent shadow IT

---

## Q115: Scenario Regulated Change Pipeline Bypass

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Enterprise Case Studies |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Auditor samples 10 prod changes — 4 deployed via kubectl direct bypassing pipeline. SOX finding imminent. Architect remediation?

### Short Answer (30 seconds)

Disable direct prod kubectl, enforce pipeline-only deploy, RBAC remove prod write from developers, collect retro change evidence, automated compliance scan, training.

### Detailed Answer

**Technical enforcement:**
- Remove prod cluster admin from dev roles
- PIM just-in-time prod access logged
- Pipeline only service account deploy prod
- Azure Policy / OPA deny manual resource changes
- GitOps ArgoCD sync only

**Retroactive:**
- Document 4 changes — map to tickets post-facto if possible
- Root cause why bypass happened — speed? ignorance? incident?

**Culture:** Blameless — fix system making bypass easy.

### Architecture Perspective

Pipeline bypass is SOX killer — expert enforces technical blocks not policy PDF only.

### Follow-up Questions

1. **GitOps? — Desired state in Git — drift auto-reverted.**
2. **Emergency? — Break-glass still logged — not kubectl default.**

### Common Mistakes in Interviews

- Policy email 'don't bypass' only
- Punish developers without fixing access
- Auditor shown fake pipeline logs

---

## Q116: Scenario Multi-Tenant Whale Tenant Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Enterprise Case Studies |
| **Frequency** | Uncommon |
| **Type** | Scenario |

### Question

Enterprise whale tenant ($5M ARR) requires dedicated infrastructure mid-contract on shared SaaS. Zero downtime demanded. Architect migration?

### Short Answer (30 seconds)

Dual-write period, tenant routing switch, dedicated DB/cluster provisioning automation, replication sync, cutover window with rollback, validation cross-tenant leak tests post-migration.

### Detailed Answer

**Phases:**
1. Provision dedicated stack — DB, app stamp, keys
2. **Dual-write** — writes go to both old and new (short period) OR CDC replication
3. **Sync verify** — row counts, checksums
4. **Cutover** — flip tenant routing config — seconds downtime max
5. **Rollback plan** — flip back if error rate spike

**Routing:**
```
Gateway reads tenant.tier → route pool shared vs dedicated
```

**Validation:** Pen test cross-tenant from whale dedicated adjacent.

### Architecture Perspective

Whale silo migration is high-stakes — expert plans dual-write and rollback.

### Follow-up Questions

1. **Downtime zero marketing? — Define acceptable seconds — honest SLAs.**
2. **Pricing? — Architecture cost passed to account — FinOps model.**

### Common Mistakes in Interviews

- Big-bang copy weekend without replication verify
- Whale still on shared cache keys
- No post-migration leak test

---

## Q117: Scenario Compliance Audit Diagram Mismatch

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Enterprise Case Studies |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Auditor onsite: production architecture differs materially from submitted C4 diagrams — shadow API integration discovered. Audit at risk. Architect response?

### Short Answer (30 seconds)

Disclose immediately, document as-is architecture, risk assess shadow integration, remediate or formalize with ADR, update all evidence, demonstrate change control going forward.

### Detailed Answer

**Immediate honesty:**
- 'Diagram outdated — here is as-is discovered today'
- Auditors respect disclosure over concealment

**Shadow integration:**
- Assess data classification and security controls
- Formalize with ADR + ARB retro OR retire integration
- Add to CMDB and monitoring

**Process fix:**
- Quarterly architecture drift detection — compare CMDB/APM to diagrams
- ADR required for new integrations

**Audit outcome:** Finding likely — remediation plan reduces severity.

### Architecture Perspective

Shadow IT discovery during audit — expert handles transparency and remediation.

### Follow-up Questions

1. **Conceal? — Career and legal risk — always disclose.**
2. **Drift detection? — Service mesh topology export vs diagram diff automated.**

### Common Mistakes in Interviews

- Backdate diagram to match without change
- Blame departed architect only
- Retire shadow integration without business assessment

---

## Q118: Scenario Board Asks Cloud Exit

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Enterprise Case Studies |
| **Frequency** | Uncommon |
| **Type** | Scenario |

### Question

Board directive: evaluate exit from primary cloud vendor within 18 months due to geopolitical risk. Architect approach to assess feasibility?

### Short Answer (30 seconds)

Portfolio inventory, dependency mapping, exit cost TCO, phased portability plan, multi-cloud vs repatriation options, honest timeline — not yes/no slogan.

### Detailed Answer

**Assessment deliverables (90 days):**
1. **Inventory** — all services by cloud PaaS vs portable K8s
2. **Dependency heat map** — locked-in serverless, proprietary AI, managed DB
3. **Exit cost model** — rewrite, dual-run, data egress fees
4. **Options paper:**
   - A: Second cloud passive DR (+cost $X)
   - B: Kubernetes abstraction layer (+effort Y)
   - C: Full migration 36mo (+$Z)
   - D: Accept risk mitigated (+controls)
5. **Recommendation** with board decision ask

**Architect honesty:** Full exit 18mo likely unrealistic for deep PaaS — present data.

### Architecture Perspective

Cloud exit board question tests architect honesty and portfolio thinking — not cheerleading.

### Follow-up Questions

1. **Egress cost? — Often underestimated — include in model.**
2. **Portable architecture? — OpenTelemetry, K8s, S3-compatible — gradual investment.**

### Common Mistakes in Interviews

- Promise 18mo full exit without assessment
- Ignore proprietary service lock-in
- Single slide 'too hard' without options

---

## Q119: Scenario Omnichannel BOPIS Race Condition

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Enterprise Case Studies |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

BOPIS: two customers reserve last unit simultaneously online for same store. Both show confirmation. Store chaos. Architect fix reservation isolation?

### Short Answer (30 seconds)

Store-level inventory partition locks; reserve API serializes per SKU-store; TTL hold; second customer gets waitlist or alternate store; idempotent reservation IDs.

### Detailed Answer

**Architecture:**
```
Reserve(storeId, skuId) → distributed lock per (store,sku) → decrement available → return reservationId + expiry
```

**On conflict:** HTTP 409 `INVENTORY_UNAVAILABLE` + suggest nearby stores

**Confirm:** Payment converts reservation to pick ticket; timeout releases stock

**Testing:** Chaos concurrent reserve load test — exactly-one success invariant.

### Architecture Perspective

BOPIS race is distributed lock problem — expert architect serializes per store-SKU.

### Follow-up Questions

1. **Global inventory? — Reserve at fulfilling node — not global counter only.**
2. **Customer UX? — Clear expiry 'hold until 3pm' — reduce no-show.**

### Common Mistakes in Interviews

- Optimistic UI confirm before reserve API returns
- No TTL — ghost reservations block stock
- Test single user only

---

## Q120: Scenario Supply Chain Port Strike Disruption

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Enterprise Case Studies |
| **Frequency** | Uncommon |
| **Type** | Scenario |

### Question

Port strike disrupts 40% inbound inventory for 3 weeks. E-commerce must adjust ATP, customer messaging, and sourcing. Architect adaptive architecture response?

### Short Answer (30 seconds)

ATP recalculation with inbound delay signals, substitute SKU rules, extended delivery promises, supplier alternate routing events, control tower exception mode — not hardcoded static stock.

### Detailed Answer

**Adaptive architecture:**
1. **Inbound delay events** from TMS feed ATP recalc
2. **Dynamic lead time** on product pages — API driven not static
3. **Sourcing rules engine** — alternate DC fulfill when port SKU delayed
4. **Customer comms** — order service triggers proactive delay notification
5. **Merchandising** — deprioritize affected SKUs in search ranking

**Control tower:** Ops dashboard exception queue — not customer checkout dependency

**Post-crisis:** Scenario playbook ADR for supply disruption.

### Architecture Perspective

Supply chain disruption expert tests event-driven adaptive commerce architecture.

### Follow-up Questions

1. **Cancel orders? — Business policy — architecture supports batch reroute first.**
2. **Manual spreadsheet? — Temporary ops tool — not architecture endpoint.**

### Common Mistakes in Interviews

- Static delivery promises on website
- Checkout still promises 2-day ship port-delayed SKU
- No event feed from TMS to commerce

---
