# Week 44 — Advanced Q&A

> Q071–Q100: Premium format (Week 1 quality).

---


## Q071: HIPAA BAA Subprocessor Chain

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | HIPAA |
| **Frequency** | Common |

### Question

Manage subprocessors in HIPAA cloud architecture.

### Short Answer (30 seconds)

Maintain subprocessor list from cloud provider; flow-down BAA terms; assess new subprocessors before enabling features; legal notification pipeline for provider changes.

### Detailed Answer (3–5 minutes)

**Architecture impact:**
- Disable features using non-covered subprocessors for PHI
- Azure OpenAI region/feature eligibility review
- Log analytics subprocessors documented

**Architect:** Subprocessor register linked to architecture service catalog — auto-flag risky service enablement.

### Architecture Perspective

Subprocessor chain is HIPAA due diligence — architects gate feature adoption.

### Follow-up Questions

1. **Business associate vs subprocessor? — Terminology — cloud provider is BA; their vendors subprocessors.**
2. **On-prem hybrid? — BAAs with each vendor touching PHI.**

### Common Mistakes in Interviews

- Enable new SaaS integration without subprocessor review
- Assume BAA covers unknown future services
- Subprocessor list never updated

---

## Q072: PHI Cross-Border Transfer

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | PHI Boundaries |
| **Frequency** | Common |

### Question

Architect PHI data flows crossing national borders.

### Short Answer (30 seconds)

Identify international transfers; BAA and legal agreements; prefer in-country processing; encryption in transit; document in data flow diagram for OCR audit.

### Detailed Answer (3–5 minutes)

**US healthcare:** OCR cares about offshore access even if stored US — support staff location matters.

**Mitigation:**
- US-only support tier for PHI systems
- No offshore backup replication without assessment

**Architect:** Data residency ADR for healthcare includes support and backup paths.

### Architecture Perspective

PHI cross-border is compliance and vendor architecture issue.

### Follow-up Questions

1. **Cloud region? — Deploy PHI in required region — admin access geo-restricted.**
2. **Encryption exception? — Encryption alone may not permit transfer — legal review.**

### Common Mistakes in Interviews

- Offshore dev team full PHI access
- Backup replicated internationally without assessment
- Undocumented offshore subprocessors

---

## Q073: PCI Point-to-Point Encryption

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | PCI Scope |
| **Frequency** | Uncommon |

### Question

Evaluate P2PE for retail point-of-sale architecture.

### Short Answer (30 seconds)

P2PE encrypts card at terminal; merchant never sees clear PAN; reduces PCI scope for store POS; integrate with payment processor P2PE solution.

### Detailed Answer (3–5 minutes)

**Architecture:**
```
Terminal (encrypt) → Processor (decrypt in CDE) → Authorization
Merchant POS sees token/reference only
```

**Architect:** Store POS and e-commerce PCI stories differ — document separately.

### Architecture Perspective

P2PE is retail store PCI architecture — complements e-commerce tokenization.

### Follow-up Questions

1. **EMV vs P2PE? — EMV chip — different layer — both may apply.**
2. **Key injection? — P2PE device lifecycle — physical security.**

### Common Mistakes in Interviews

- POS sends clear PAN to store server
- Same SAQ for web and store without analysis
- Mixed P2PE and legacy terminals undocumented

---

## Q074: Retail Peak War Room Operations

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Retail Peak |
| **Frequency** | Common |

### Question

Design war room operations architecture for retail peak.

### Short Answer (30 seconds)

Runbook, roles, dashboards, comms bridge, escalation tree, vendor contacts, feature flag owners, rollback authority pre-assigned.

### Detailed Answer (3–5 minutes)

**War room artifacts:**
- Single pane: traffic, errors, checkout rate, queue depth
- Pre-written status templates
- Decision log
- Post-incident review slot booked

**Architect:** Technical lead owns architecture decisions in war room — not ad hoc improvisation.

### Architecture Perspective

Peak war room is operational architecture — prepared before crisis.

### Follow-up Questions

1. **Game day? — Rehearse war room 4 weeks before peak.**
2. **Vendor bridge? — PSP, CDN, cloud TAM on speed dial list.**

### Common Mistakes in Interviews

- No runbook — scramble day-of
- Single engineer sole decision maker
- Dashboards first seen during incident

---

## Q075: Multi-Tenant Encryption Keys

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Multi-Tenant |
| **Frequency** | Common |

### Question

Implement per-tenant encryption key strategy in SaaS.

### Short Answer (30 seconds)

CMK/customer-managed keys for enterprise tier; platform key for SMB; key rotation; tenant offboarding crypto-shred.

### Detailed Answer (3–5 minutes)

**Azure:** SQL TDE with AKV per-tenant key optional.

**Architecture:**
- Key vault access policy per tenant service principal
- Rotation automated with re-encrypt plan

**Architect:** BYOK enterprise feature — architecture must support key per tenant without code fork.

### Architecture Perspective

Per-tenant keys are enterprise sales requirement — plan key hierarchy early.

### Follow-up Questions

1. **Crypto-shred offboarding? — Delete tenant key renders data unrecoverable — GDPR helper.**
2. **Performance? — envelope encryption — DEK per row KEK per tenant.**

### Common Mistakes in Interviews

- Single master key all tenants
- No key rotation procedure
- Offboarded tenant data readable indefinitely

---

## Q076: ARB and Legal Privacy Review

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Architecture Review Board |
| **Frequency** | Common |

### Question

Integrate legal and privacy review into architecture review board.

### Short Answer (30 seconds)

Privacy delegate reviews data flows; legal reviews cross-border and contract terms; DPIA trigger checklist in Tier-0 review packet.

### Detailed Answer (3–5 minutes)

**Review triggers:**
- New personal data collection
- New third-party processor
- Profiling/automated decision
- Biometric/health data

**Architect:** Privacy review gate before ARB approval — not parallel optional.

### Architecture Perspective

ARB without privacy is incomplete for customer data systems.

### Follow-up Questions

1. **DPIA template? — Standard form linked from ARB portal.**
2. **Legal non-goals? — Document what product cannot do legally.**

### Common Mistakes in Interviews

- Privacy team sees architecture after launch
- Skip DPIA for 'internal analytics'
- Legal findings not tracked to closure

---

## Q077: Continuous Compliance Monitoring

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Compliance Audits |
| **Frequency** | Common |

### Question

Architect continuous compliance monitoring instead of point-in-time audit scramble.

### Short Answer (30 seconds)

Policy-as-code Azure Policy; drift detection; automated evidence collection; compliance dashboard; alert on control degradation.

### Detailed Answer (3–5 minutes)

**Examples:**
- Policy deny public storage account
- CI collect PR approval artifacts daily
- Drift: Terraform vs actual cloud scan

**Architect:** Continuous compliance reduces audit cost — evidence always fresh.

### Architecture Perspective

Compliance as continuous architecture — not annual fire drill.

### Follow-up Questions

1. **SOC2 continuous? — Some auditors accept continuous control monitoring evidence.**
2. **False positive policy? — Tune with exceptions registry.**

### Common Mistakes in Interviews

- Evidence gathered only pre-audit
- Manual compliance checks quarterly only
- Drift undetected for months

---

## Q078: Vendor Concentration Risk

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Vendor Risk |
| **Frequency** | Common |

### Question

Assess and mitigate vendor concentration risk in architecture.

### Short Answer (30 seconds)

Identify single points of vendor failure (identity, cloud, PSP); document exit cost; multi-vendor where justified; contractual SLAs and exit clauses.

### Detailed Answer (3–5 minutes)

**Concentration map:**
| Capability | Vendor | Alt | Exit cost |
| Cloud | Azure | AWS migration $X | High |
| Identity | Okta | Entra | Medium |

**Architect:** Board-level risk when concentration on one vendor for critical path.

### Architecture Perspective

Concentration risk is strategic architecture — SolarWinds/CrowdStrike lessons.

### Follow-up Questions

1. **Multi-cloud? — Expensive — selective critical workload portability.**
2. **Exit test? — Annual restore from vendor export — prove portability.**

### Common Mistakes in Interviews

- Single PSP identity cloud no plan
- Architecture assumes vendor eternal
- No SLA financial penalties

---

## Q079: GDPR DPIA High-Risk Processing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | GDPR |
| **Frequency** | Common |

### Question

Trigger and conduct DPIA for high-risk GDPR processing.

### Short Answer (30 seconds)

DPIA when systematic monitoring, special category data at scale, automated decisions with legal effect, or innovative technology — document risks and mitigations before build.

### Detailed Answer (3–5 minutes)

**DPIA sections:**
- Processing description
- Necessity/proportionality
- Risk to data subjects
- Mitigations
- DPO sign-off

**Architect:** DPIA gate in project lifecycle — no prod without DPO clearance for high-risk.

### Architecture Perspective

DPIA is privacy architecture review — blocks non-compliant designs early.

### Follow-up Questions

1. **Facial recognition retail? — High-risk example — DPIA mandatory.**
2. **Re-DPIA? — When processing changes materially.**

### Common Mistakes in Interviews

- Skip DPIA because startup speed
- DPIA after production launch
- No DPO involvement documented

---

## Q080: SOX IT Dependency Mapping

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | SOX |
| **Frequency** | Common |

### Question

Map IT dependencies for SOX in-scope financial reporting chain.

### Short Answer (30 seconds)

Diagram data flow from source systems to GL; identify all services touching revenue recognition; control points at each hop; single system of record per financial entity.

### Detailed Answer (3–5 minutes)

**Diagram elements:**
- Order capture → billing → revenue recognition → GL export
- Control: reconciliation job, audit trail, access control per hop

**Architect:** SOX dependency map updated on every new billing microservice.

### Architecture Perspective

SOX auditors follow data to GL — architects document chain completely.

### Follow-up Questions

1. **Manual journal entries? — Control for manual adjustment path too.**
2. **Third-party billing? — Vendor SOC2 + interface controls in scope.**

### Common Mistakes in Interviews

- Revenue service not in SOX inventory
- Undocumented GL export batch job
- Shadow spreadsheet outside system

---

## Q081: Acquisition Technical Due Diligence

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Acquisition Integration |
| **Frequency** | Common |

### Question

Lead technical due diligence architecture assessment pre-acquisition.

### Short Answer (30 seconds)

Inventory systems, security debt, license compliance, scalability, integration complexity, key person risk, estimated integration cost — report to M&A team influences price.

### Detailed Answer (3–5 minutes)

**Assessment areas:**
- Security incidents history
- Cloud vs on-prem
- Data classification gaps
- Technical debt quantification
- API documentation quality

**Architect:** DD findings become integration roadmap input — not shelfware.

### Architecture Perspective

Pre-acquisition DD prevents surprise integration cost post-close.

### Follow-up Questions

1. **Red flag? — Unsupported EOL database — immediate cost line item.**
2. **Culture? — Engineering velocity assessment — integration timeline.**

### Common Mistakes in Interviews

- Skip DD trust seller deck
- DD report not shared with integration team
- Underestimate identity merge complexity

---

## Q082: Board Cyber Risk Dashboard

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Executive Briefings |
| **Frequency** | Common |

### Question

Design technology risk dashboard for board consumption.

### Short Answer (30 seconds)

Top enterprise cyber risks trend, control maturity, open critical findings, MTTR, program RAG, peer benchmark — non-technical visuals quarterly.

### Detailed Answer (3–5 minutes)

**Metrics board cares about:**
- Material incident count
- Critical vuln mean age
- DR test pass rate
- Major program status
- Regulatory examination status

**Architect/CIO:** Honest trend lines — remediation velocity not only open count.

### Architecture Perspective

Board dashboard translates architecture risk to fiduciary language.

### Follow-up Questions

1. **Material incident definition? — Legal counsel defines disclosure threshold.**
2. **Benchmark? — Industry peer comparison contextualizes posture.**

### Common Mistakes in Interviews

- CVE list to board without business framing
- Hide worsening trend until audit
- Dashboard never updated quarterly

---

## Q083: TOGAF vs Agile Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Reference Architectures |
| **Frequency** | Uncommon |

### Question

Reconcile TOGAF enterprise architecture with agile delivery teams.

### Short Answer (30 seconds)

Use TOGAF for portfolio, standards, reference models; agile teams consume architecture runway — ADRs not big upfront design; Architecture Development Method light touch.

### Detailed Answer (3–5 minutes)

**Pragmatic blend:**
- **EA team:** Standards, landing zone, ARB
- **Squads:** ADRs per significant decision
- **Avoid:** 6-month EA document before code

**Architect:** TOGAF vocabulary for executives; ADR/RFC for engineers.

### Architecture Perspective

TOGAF agile coexistence is common EA interview topic.

### Follow-up Questions

1. **Architecture runway? — Just-enough ahead of PI planning — not waterfall spec.**
2. **ArchiMate? — Optional modeling — value if kept current.**

### Common Mistakes in Interviews

- Full TOGAF phases for single microservice
- EA documents nobody reads
- Agile team ignores all standards

---

## Q084: Emergency Change Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Regulated Change Control |
| **Frequency** | Common |

### Question

Design emergency change process preserving audit trail under outage pressure.

### Short Answer (30 seconds)

Pre-authorized break-glass roles; deploy with ticket; notify stakeholders; mandatory retrospective ARB within 48h; automated capture of who/when/what.

### Detailed Answer (3–5 minutes)

**Architecture supports:**
- Pipeline break-glass with extra logging
- Feature flag kill switch faster than emergency deploy
- Runbook changes pre-written for known scenarios

**Architect:** Prefer flag over emergency code deploy when possible.

### Architecture Perspective

Emergency change architecture balances speed and compliance.

### Follow-up Questions

1. **GxP emergency? — QA notified immediately — impact assessment next business day.**
2. **Post-incident? — Emergency change reviewed same as planned — no free pass.**

### Common Mistakes in Interviews

- Emergency bypasses all logging
- Retrospective never happens
- Emergency becomes normal path

---

## Q085: Omnichannel Pricing Consistency

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Omnichannel |
| **Frequency** | Common |

### Question

Architect consistent pricing and promotions across omnichannel.

### Short Answer (30 seconds)

Single promo engine; price cache fed from ERP; channel-specific rules explicit; effective datetime synchronization; test matrix web/store/call center.

### Detailed Answer (3–5 minutes)

**Anti-pattern:** Store manager markdown not visible online — customer anger.

**Architecture:**
```
Pricing Service ← ERP events → Web, POS, CallCenter APIs
```

**Architect:** Pricing is system of record debate — usually ERP master with real-time cache.

### Architecture Perspective

Omnichannel pricing errors are brand incidents — central engine architecture.

### Follow-up Questions

1. **Flash sale? — Coordinated start time all channels UTC sync.**
2. **Price override audit? — Manager override logged store and online.**

### Common Mistakes in Interviews

- Separate promo databases per channel
- Store price differs silently from web
- No effective date on price changes

---

## Q086: Supply Chain Control Tower

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Supply Chain |
| **Frequency** | Uncommon |

### Question

Design supply chain control tower visibility architecture.

### Short Answer (30 seconds)

Aggregate ERP, WMS, TMS, supplier EDI into operational dashboard; exception alerts (delay, stockout); predictive ETA; not synchronous dependency for checkout.

### Detailed Answer (3–5 minutes)

**Data pipeline:**
Batch + event hybrid → data lake → control tower UI for ops — separate from customer path.

**Architect:** Control tower is read/analytics — don't put on checkout critical path.

### Architecture Perspective

Control tower is ops architecture — visibility without blocking transactions.

### Follow-up Questions

1. **Digital twin? — Advanced — simulation for disruption scenarios.**
2. **Supplier EDI failure? — Alert + fallback safety stock rules.**

### Common Mistakes in Interviews

- Ops dashboard queries SAP synchronously
- No exception alerting
- Control tower confused with customer inventory API

---

## Q087: HIPAA Disaster Recovery PHI

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | HIPAA |
| **Frequency** | Common |

### Question

Design disaster recovery for HIPAA systems with PHI.

### Short Answer (30 seconds)

Encrypted backups; BAA-covered DR region; RTO/RPO defined; DR test without PHI leak to non-prod; runbook includes breach notification if DR failover compromised.

### Detailed Answer (3–5 minutes)

**Requirements:**
- DR site under same BAA coverage
- Failover audit logging continues
- Access controls replicated

**Architect:** DR drill evidence required HIPAA audits — document annually.

### Architecture Perspective

HIPAA DR adds BAA and encryption constraints beyond generic DR.

### Follow-up Questions

1. **Failover to non-BAA region? — Prohibited for PHI — architect blocks.**
2. **DR test data? — Synthetic — never copy prod PHI to DR test ad hoc.**

### Common Mistakes in Interviews

- DR backups unencrypted
- Failover opens PHI to wider access
- DR never tested with compliance observer

---

## Q088: PCI ASV Scan Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | PCI Scope |
| **Frequency** | Common |

### Question

Prepare architecture for quarterly PCI ASV external vulnerability scans.

### Short Answer (30 seconds)

Stable external IPs; no surprise open ports; CDE scope documented; remediate critical findings before scan; re-scan until pass.

### Detailed Answer (3–5 minutes)

**Architect responsibilities:**
- Accurate CDE boundary diagram for ASV scope
- WAF not hiding unscanned vulnerabilities falsely
- Change control notifies before external surface changes

**Fail ASV:** Block certification — revenue impact for payment merchants.

### Architecture Perspective

ASV scan is architecture validation of external attack surface.

### Follow-up Questions

1. **WAF vs scan? — ASV scans origin or through WAF per program rules — document.**
2. **Container egress? — Unexpected open services fail scan.**

### Common Mistakes in Interviews

- Shadow IT service on public IP
- Ignore ASV findings as false positive without proof
- CDE boundary wrong — false compliance sense

---

## Q089: Retail Multi-Region Active-Active

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Retail Peak |
| **Frequency** | Uncommon |

### Question

Design active-active multi-region for global retail peak.

### Short Answer (30 seconds)

Geo-DNS route to nearest region; data replication async with conflict rules; cart sticky to region or global cart service; payment idempotency cross-region.

### Detailed Answer (3–5 minutes)

**Challenges:**
- Inventory split-brain — partition tolerance
- Session affinity vs global state
- Regulatory data residency

**Architect:** Active-active complexity justified at revenue scale — not default for mid retailer.

### Architecture Perspective

Multi-region active-active is expert retail architecture — CAP trade-offs explicit.

### Follow-up Questions

1. **CRDT cart? — Advanced merge for cart cross-region — rare.**
2. **Failover? — DNS health check — automated regional drain.**

### Common Mistakes in Interviews

- Active-active without conflict resolution
- Cross-region sync SAP in checkout
- GDPR violation US-EU active replication

---

## Q090: Multi-Tenant Compliance Tiering

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Multi-Tenant |
| **Frequency** | Common |

### Question

Offer compliance tiering (HIPAA, PCI) within multi-tenant SaaS.

### Short Answer (30 seconds)

Compliance tier maps to isolation model: shared pool SMB; dedicated DB HIPAA; silo infra PCI; pricing and architecture align; tier enforced at provisioning.

### Detailed Answer (3–5 minutes)

**Provisioning:**
```
tenant.tier=hipaa → dedicated DB + BAA features + audit pack
```

**Architect:** Cannot claim HIPAA on shared row without controls — tier drives architecture template.

### Architecture Perspective

Compliance tiering is product architecture — sales promises need technical backing.

### Follow-up Questions

1. **Upgrade tier? — Migration pipeline pooled → silo with downtime plan.**
2. **Feature flags per tier? — Disable non-compliant features on lower tier.**

### Common Mistakes in Interviews

- Sell HIPAA tier on shared schema
- Same audit log retention all tiers
- Tier not enforced in provisioning automation

---

## Q091: ARB Metrics and SLAs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Architecture Review Board |
| **Frequency** | Common |

### Question

Measure architecture review board effectiveness with metrics.

### Short Answer (30 seconds)

Review SLA compliance, exception rate, finding recurrence, time-to-decision, post-implementation divergence from approved design.

### Detailed Answer (3–5 minutes)

**Metrics:**
- % reviews decided within SLA
- % projects with ADR before prod
- Critical findings open >90 days
- Repeat waiver count per system

**Architect:** Metrics justify ARB investment — or reveal bureaucracy without value.

### Architecture Perspective

ARB metrics prevent governance theater — data-driven improvement.

### Follow-up Questions

1. **Divergence tracking? — Compare prod architecture to approved ADR quarterly.**
2. **Developer NPS? — ARB satisfaction survey — friction vs value.**

### Common Mistakes in Interviews

- ARB meets but no metrics
- SLA ignored without consequence
- Same finding repeated every review

---

## Q092: Internal Audit Architecture Interview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Compliance Audits |
| **Frequency** | Common |

### Question

Prepare for internal audit architecture interviews.

### Short Answer (30 seconds)

Know system context, data flows, controls, recent changes, open risks, evidence locations — consistent story with documentation.

### Detailed Answer (3–5 minutes)

**Preparation:**
- Review ADRs for audit period
- Align with ops on actual vs documented
- Bring diagrams current to prod
- Acknowledge gaps with remediation plan

**Architect:** Honesty builds trust — 'we discovered X and fixed Y' better than bluff.

### Architecture Perspective

Internal audit rehearsal prevents external audit surprises.

### Follow-up Questions

1. **Sample systems? — Auditors pick — all systems must be defensible.**
2. **Interview vs evidence? — Both — narrative must match artifacts.**

### Common Mistakes in Interviews

- Document contradicts production — caught in interview
- Architect absent — dev guesses controls
- No remediation plan for known gaps

---

## Q093: Fourth-Party Vendor Risk

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Vendor Risk |
| **Frequency** | Uncommon |

### Question

Assess fourth-party risk when vendor uses critical subprocessors.

### Short Answer (30 seconds)

Require vendor disclose subprocessors; assess same criteria; contractual flow-down; monitor vendor SOC2 subservice org section; architecture abstraction where fourth-party fails.

### Detailed Answer (3–5 minutes)

**Example chain:**
You → SaaS vendor → AWS → CDN subprocessor

**Architect:** Critical path fourth-party failure modes in DR and vendor risk register.

### Architecture Perspective

Fourth-party risk exploded with SaaS — architects map full chain.

### Follow-up Questions

1. **SOC2 Carve-out? — Subservice org controls — understand what vendor vs subprocessor owns.**
2. **Notification? — Contract require subprocessor change notice 30 days.**

### Common Mistakes in Interviews

- Ignore subprocessor section SOC2 report
- Critical feature depends on unknown fourth party
- No fallback if subprocessor discontinued

---

## Q094: GDPR Privacy by Design Checklist

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | GDPR |
| **Frequency** | Common |

### Question

Apply privacy by design checklist in architecture reviews.

### Short Answer (30 seconds)

Data minimization, purpose limitation, storage limitation, accuracy, integrity, confidentiality — each new feature scored against checklist before build.

### Detailed Answer (3–5 minutes)

**Checklist items:**
- Collect only necessary fields?
- Retention TTL defined?
- Erasure path exists?
- Encryption in transit/at rest?
- Access logged?

**Architect:** Privacy checklist in ARB Tier-1 packet — DPO spot audit.

### Architecture Perspective

Privacy by design operationalized via checklist — not slogan.

### Follow-up Questions

1. **Pseudonymization default? — Analytics uses pseudonym IDs — reversible separately.**
2. **Default privacy? — Opt-in not opt-out for non-essential processing.**

### Common Mistakes in Interviews

- Collect 'just in case' fields
- No retention deletion job
- Privacy review skipped for MVP

---

## Q095: SOX Automated Control Testing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | SOX |
| **Frequency** | Uncommon |

### Question

Automate SOX control testing where possible.

### Short Answer (30 seconds)

CI verifies PR approvals, branch protection, prod deploy gates; continuous access review scripts; automated evidence to GRC tool.

### Detailed Answer (3–5 minutes)

**Automated controls:**
- Branch protection enabled scan
- Prod deploy without approval alert
- PIM activation logged

**Architect:** Automation reduces manual SOX testing cost — architecture enables observability of controls.

### Architecture Perspective

SOX automation is mature enterprise architecture — GRC integration.

### Follow-up Questions

1. **ITGC vs application controls? — Both — automated where repeatable.**
2. **Exception workflow? — Automated ticket when control fails scan.**

### Common Mistakes in Interviews

- Manual screenshot collection each quarter
- Control fails silently
- GRC tool disconnected from reality

---

## Q096: Acquisition Strangler Integration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Acquisition Integration |
| **Frequency** | Common |

### Question

Apply strangler fig pattern to acquired product integration.

### Short Answer (30 seconds)

Facade routes traffic to acquired or acquirer systems incrementally; anti-corruption layer; retire acquired modules as replacements ready — no big-bang.

### Detailed Answer (3–5 minutes)

**Phases:**
1. SSO + read-only sync
2. New features on acquirer platform
3. Migrate customers in waves
4. Decommission acquired stack

**Architect:** Strangler metrics — % traffic on new stack — executive visibility.

### Architecture Perspective

Strangler is default M&A integration — big-bang is high risk.

### Follow-up Questions

1. **Customer communication? — Migration windows per cohort — architecture supports dual-run period.**
2. **Data sync? — Event-driven CDC — not overnight batch only.**

### Common Mistakes in Interviews

- Force all users migrated weekend one
- Run acquired stack forever duplicate cost
- No metrics on migration progress

---

## Q097: Executive Cost of Delay

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Executive Briefings |
| **Frequency** | Common |

### Question

Quantify cost of delay for executive architecture decisions.

### Short Answer (30 seconds)

Translate delayed decision to revenue loss, compliance fine risk, engineering rework cost, opportunity cost — dollar ranges with assumptions stated.

### Detailed Answer (3–5 minutes)

**Example framing:**
'Delaying PCI scope fix 6 months: $400K audit remediation + potential processor fine + 2 sprint rework $150K.'

**Architect:** Cost of delay makes urgency tangible — not fear mongering with data.

### Architecture Perspective

Executives decide with money and risk — architects quantify delay.

### Follow-up Questions

1. **Opportunity cost? — Competitor launch window — market share estimate.**
2. **Rework cost? — Building on wrong architecture — multiplier if delayed ADR.**

### Common Mistakes in Interviews

- Vague 'we should decide soon'
- Inflated numbers without assumptions
- Only technical consequences listed

---

## Q098: BIAN Banking Reference Alignment

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Reference Architectures |
| **Frequency** | Uncommon |

### Question

Align banking architecture to BIAN service landscape.

### Short Answer (30 seconds)

Map microservices to BIAN service domains (Customer Offer, Payment Execution); gaps documented; accelerates regulator and partner dialogue.

### Detailed Answer (3–5 minutes)

**Use case:**
- Standard vocabulary with core banking vendors
- Identify duplicate capabilities across silos

**Architect:** BIAN alignment optional but valuable in financial services EA roles.

### Architecture Perspective

Industry reference accelerates banking architecture communication.

### Follow-up Questions

1. **HL7 vs BIAN? — Healthcare FHIR; banking BIAN — sector references differ.**
2. **Over-alignment? — Don't force fit non-banking capabilities into BIAN boxes.**

### Common Mistakes in Interviews

- BIAN diagram never mapped to actual services
- Force reorganize teams to BIAN prematurely
- Reference used without gap analysis

---

## Q099: Validated Environment Promotion

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Regulated Change Control |
| **Frequency** | Common |

### Question

Promote changes through validated environments in GxP context.

### Short Answer (30 seconds)

Dev → QA (validated) → Prod with IQ/OQ evidence; environment parity; configuration managed; no skip-level deploy.

### Detailed Answer (3–5 minutes)

**Pipeline gates:**
- QA sign-off artifact required for prod
- Environment config diff reviewed
- Test evidence attached to change record

**Architect:** Non-validated prod hotfix in GxP triggers revalidation assessment — not casual.

### Architecture Perspective

GxP environment promotion is rigid — architects design pipeline accordingly.

### Follow-up Questions

1. **Blue/green in GxP? — Possible with validation scope defined for parallel environment.**
2. **Config drift QA prod? — Violates validation — automated drift block.**

### Common Mistakes in Interviews

- Skip QA for urgent prod fix
- Prod config edited manually
- Undocumented environment differences

---

## Q100: Omnichannel Fraud Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Omnichannel |
| **Frequency** | Uncommon |

### Question

Architect fraud detection across omnichannel transactions.

### Short Answer (30 seconds)

Unified fraud scoring service; signals from web, mobile, store, call center; device fingerprint; velocity rules; ML model feedback loop; block/challenge/review decisions.

### Detailed Answer (3–5 minutes)

**Signals:**
- Account takeover patterns
- BOPIS fraud
- Return abuse cross-channel

**Architect:** Fraud service async in checkout — don't block p99 — step-up auth on risk.

### Architecture Perspective

Omnichannel fraud requires unified signal architecture — siloed rules fail.

### Follow-up Questions

1. **False positive? — Customer friction cost — tune thresholds per channel.**
2. **PSP fraud tools? — Layer with merchant rules — coordinate scores.**

### Common Mistakes in Interviews

- Fraud check synchronous 2s SAP-style
- Store fraud separate from online
- No review queue for challenged orders

---
