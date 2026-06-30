# Week 44 — Fundamentals Interview Q&A

> Q001–Q030: Premium format (Week 1 quality).  
> See also: [Interview prep hub](../../../interview-prep/README.md)

---


## Q001: Healthcare Architecture Constraints

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Enterprise |
| **Frequency** | Very Common |

### Question

What architectural constraints apply when designing systems that handle protected health information (PHI)?

### Short Answer (30 seconds)

Healthcare architecture requires BAA with cloud provider, PHI encryption at rest and in transit, minimum-necessary access, audit logging (6+ years), private networking, no prod PHI in dev, de-identified test data, and breach notification runbooks. HIPAA is law — technical and administrative controls both mandatory.

### Detailed Answer (3–5 minutes)

**Key constraints:**
| Domain | Requirement |
|--------|-------------|
| Cloud | BAA only with HIPAA-eligible services |
| Network | Private endpoints; no public PHI APIs |
| Identity | MFA, RBAC, break-glass access audited |
| Data | Encryption AES-256; field-level PHI tagging |
| Audit | Immutable logs; who accessed what PHI when |
| Dev/test | De-identified or synthetic data only |

**Architecture zones:**
```
[PHI Zone: EHR API, Clinical DB] ←private link→ [Integration]
[Non-PHI: Marketing site] — no PHI data paths
[Analytics: De-identified warehouse only]
```

**Azure specifics:** Verify service HIPAA eligibility before design — not all services covered under BAA.

**Architect:** Document PHI data flows on context diagram; every external integration gets DLP review. HIPAA violation cost >> architecture review time.

### Architecture Perspective

Healthcare interviews test PHI boundaries and BAA — architects design zones, not just encrypt databases.

### Follow-up Questions

1. **HIPAA vs HITRUST? — HIPAA is legal requirement; HITRUST certifies control implementation — both may apply.**
2. **ePHI in logs? — Redact at ingestion — logging PHI is common violation vector.**

### Common Mistakes in Interviews

- HIPAA-eligible service used without signed BAA
- Production PHI copied to developer laptops for debugging
- Analytics data lake contains raw PHI for convenience

---

## Q002: Fintech PCI Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Enterprise |
| **Frequency** | Very Common |

### Question

How does PCI DSS influence payment system architecture?

### Short Answer (30 seconds)

PCI architecture minimizes Cardholder Data Environment (CDE) scope: tokenization, hosted payment fields (iframe/JS SDK), no PAN/CVV on merchant servers, network segmentation, no PAN in logs, and annual SAQ or audit based on scope level. Design goal: SAQ A or A-EP instead of full SAQ D.

### Detailed Answer (3–5 minutes)

**Scope reduction patterns:**
```
Browser → PSP hosted fields (PAN never touches merchant)
Merchant server receives token only → reduced PCI scope
```

**Architecture layers:**
- **Out of scope** — Systems handling only tokens, never PAN
- **CDE** — Any system storing, processing, or transmitting card data
- **Connected to** — Systems on same network segment as CDE — may inherit scope

**Controls regardless of scope:**
- TLS 1.2+ for all payment traffic
- No PAN storage post-authorization (token vault only)
- Webhook signature verification on payment events
- Segmented network; WAF on payment-facing endpoints

**SAQ types:**
| SAQ | When |
|-----|------|
| A | Fully outsourced card entry (iframe) |
| A-EP | Merchant website affects payment security |
| D | Full card data environment |

**Architect:** PCI scope directly drives cost — custom card forms posting PAN to your API triggers full audit.

### Architecture Perspective

PCI scope minimization is primary fintech architecture skill — tokenization beats encryption-in-your-DB.

### Follow-up Questions

1. **PAN in logs? — Automatic PCI failure — structured logging must redact payment payloads.**
2. **Network segmentation? — CDE isolated VLAN; firewall rules documented and reviewed annually.**

### Common Mistakes in Interviews

- Custom card form posting PAN to merchant API
- Encrypted PAN stored in application database instead of PSP token
- Full PCI audit triggered for entire datacenter unnecessarily

---

## Q003: Retail Peak Scale Patterns

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Enterprise |
| **Frequency** | Very Common |

### Question

What architecture patterns prepare retail e-commerce for predictable peak traffic (e.g., Black Friday)?

### Short Answer (30 seconds)

Peak retail patterns: pre-scale capacity weeks ahead, CDN for product pages, read replicas, checkout queue/virtual waiting room, autoscale with tested caps, feature freeze, degrade non-critical paths, synthetic monitoring, and load test at 3× expected peak.

### Detailed Answer (3–5 minutes)

**Peak preparation playbook:**
1. **Capacity** — Pre-warm AKS nodes, Redis, connection pools 4–6 weeks prior
2. **CDN/edge** — Static product catalog, ISR, long TTL on fingerprinted assets
3. **Read scaling** — DB read replicas; cache hot product/inventory queries
4. **Checkout protection** — Virtual waiting room when origin overload; bulkhead thread pool for payment path
5. **Degradation** — Disable recommendations, reviews, non-critical personalization first
6. **Operational** — War room, feature freeze 2 weeks before, synthetic monitors every 60s

**Load validation:**
- k6 stress test at 3× peak — 6 weeks before event
- Measure p99 checkout latency and error budget consumption
- Document headroom in peak architecture ADR

**Architect:** Peak is predictable chaos — architecture plans months ahead; day-before load test is malpractice.

### Architecture Perspective

Retail peak architecture is rehearsed reliability — interviewers want specific patterns, not 'we'll autoscale.'

### Follow-up Questions

1. **Virtual waiting room? — Azure Front Door or custom queue — protects origin from stampede.**
2. **Multi-region for peak? — Active-active or warm DR region for geographic traffic distribution.**

### Common Mistakes in Interviews

- First load test the day before Black Friday
- Autoscale limits never validated at 3× expected traffic
- Single region serving global retail customers

---

## Q004: Multi-Tenant SaaS Isolation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Enterprise |
| **Frequency** | Very Common |

### Question

How do you design tenant isolation in a multi-tenant SaaS architecture?

### Short Answer (30 seconds)

Tenant isolation models range from pooled (shared DB, row-level tenantId) to siloed (database per tenant). Choose based on compliance, noisy-neighbor tolerance, and cost. Defense in depth: middleware enforces tenant context on every query, integration tests for cross-tenant leaks, and rate limits per tenant.

### Detailed Answer (3–5 minutes)

**Isolation models:**
| Model | Isolation | Cost | Best for |
|-------|-----------|------|----------|
| Pooled (shared schema) | Low | Lowest | SMB SaaS |
| Schema per tenant | Medium | Medium | Mid-market |
| Database per tenant | High | High | Enterprise/regulated |
| Silo per tenant (dedicated stack) | Highest | Highest | Government, healthcare |

**Defense in depth:**
- Tenant context from JWT claim — middleware injects `tenantId` into every DB query
- Row-level security (PostgreSQL RLS) as safety net
- Separate encryption keys per tenant for regulated data
- No shared cache keys without tenant prefix
- Automated cross-tenant penetration tests in CI

**Noisy neighbor:**
- Per-tenant rate limits and fair-queue scheduling
- Dedicated resource pool for whale tenants

**Architect:** Cross-tenant data leak is company-ending — isolation model is Tier-0 ADR with rejected alternatives documented.

### Architecture Perspective

Tenant isolation is trust architecture — architects choose model from compliance and blast radius, not convenience.

### Follow-up Questions

1. **Tenant in subdomain vs JWT? — Subdomain routing + JWT claim double-validation for defense in depth.**
2. **Migration between models? — Pooled to silo is multi-year event — choose early for regulated verticals.**

### Common Mistakes in Interviews

- tenantId passed only from client query parameter without server validation
- Shared Redis cache keys without tenant prefix
- No automated test proving Tenant A cannot read Tenant B data

---

## Q005: Enterprise Architecture Review Process

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Enterprise |
| **Frequency** | Very Common |

### Question

Describe a structured enterprise architecture review process before production approval.

### Short Answer (30 seconds)

Enterprise review process: tiered intake → pre-read package (C4, ADRs, NFR matrix, threat summary) → facilitated review meeting or async approval → checklist sign-off → production gate. Outputs are documented decisions, waivers with expiry, or required changes — not informal verbal OK.

### Detailed Answer (3–5 minutes)

**Review package contents:**
1. Context + container C4 diagrams
2. ADRs for significant decisions (linked, Accepted status)
3. NFR matrix (latency, availability, RTO/RPO, cost)
4. STRIDE threat model summary
5. Cost estimate with FinOps tags
6. Migration/rollback and runbook outline

**Process flow:**
```
Team submits package → Tier classification → Async pre-review (security, data)
    → Review meeting (Tier-0) or delegate approval (Tier-1)
    → Checklist sign-off recorded in PR/ticket
    → Production deploy authorized
```

**Checklist categories:** Requirements traceability, security, data classification, reliability, observability, operations, cost, governance.

**Facilitation:** Time-boxed agenda — presenter 15 min, structured Q&A, action items with owners. Conflict escalates to architecture board.

**Architect:** Tiered process ensures Tier-0 rigor without making every team wait weeks for internal tool approval.

### Architecture Perspective

Enterprise review process makes quality repeatable — architects design tiers, checklists, and artifacts.

### Follow-up Questions

1. **Pre-review vs full review? — Pre-review at RFC stage catches issues early; full review at production gate.**
2. **Waivers? — Documented exception with expiry, compensating controls, executive sponsor.**

### Common Mistakes in Interviews

- Verbal VP approval with no recorded sign-off
- Same heavyweight checklist for POC and payment system
- Security not involved in external-facing API review

---

## Q006: Healthcare HIPAA Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Enterprise |
| **Frequency** | Very Common |

### Question

Design cloud architecture for HIPAA-regulated healthcare application.

### Short Answer (30 seconds)

BAA with cloud provider, PHI encryption at rest/transit, access audit logs, minimum necessary access, private networking, BAAs with subprocessors, breach notification runbook.

### Detailed Answer (3–5 minutes)

**Architecture layers:**
- **Identity** — MFA, role-based, break-glass audited
- **Network** — Private Link, no public PHI endpoints
- **Data** — Encrypted DB, column-level PHI tagging
- **Audit** — Immutable logs 6+ years
- **Ops** — No prod PHI in dev; de-identified test data

**Azure:** HIPAA BAA eligible services only — verify before use.

**Architect:** HIPAA is administrative + technical — policies as important as VPC.

### Architecture Perspective

Healthcare architecture interviews test BAA, PHI boundaries, and audit.

### Follow-up Questions

1. **HIPAA vs HITRUST? — HITRUST certifies controls; HIPAA is law — both may apply.**
2. **ePHI in logs? — Redact — logging PHI is violation vector.**

### Common Mistakes in Interviews

- HIPAA eligible service used without BAA
- Prod PHI copied to developer laptop
- Shared tenant database without access controls

---

## Q007: PHI Data Boundaries

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Healthcare |
| **Frequency** | Very Common |

### Question

Define PHI data boundaries in multi-service healthcare architecture.

### Short Answer (30 seconds)

PHI zone: systems storing/transmitting PHI — stricter controls. Non-PHI zone: scheduling UI without clinical data. Clear API contracts — PHI never leaks to analytics without de-identification.

### Detailed Answer (3–5 minutes)

**Boundary diagram:**
```
[PHI Zone: EHR API, Clinical DB] ←private link→ [Integration Layer]
[Non-PHI: Marketing site] — no PHI paths
[Analytics: De-identified warehouse only]
```

**Controls at boundary:**
- Token scopes limit PHI fields
- DLP scan outbound integrations
- Service accounts per zone — no shared admin

**Architect:** Document PHI flow in threat model — every arrow questioned.

### Architecture Perspective

PHI boundary errors cause compliance breach — architect explicit zones.

### Follow-up Questions

1. **De-identification Safe Harbor? — Remove 18 identifiers before analytics zone.**
2. **Break-glass access? — Emergency PHI access logged and reviewed.**

### Common Mistakes in Interviews

- Analytics lake has raw PHI 'for convenience'
- Microservice logs full patient record JSON
- PHI in cache without encryption

---

## Q008: Fintech PCI Scope

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Enterprise |
| **Frequency** | Very Common |

### Question

Reduce PCI DSS scope in payment architecture.

### Short Answer (30 seconds)

Scope reduction: tokenization, hosted payment fields (Stripe Elements, iframe), no PAN/CVV touch application servers — SAQ A or A-EP instead of full D.

### Detailed Answer (3–5 minutes)

**Scoped architecture:**
```
Browser → PSP iframe (PAN entry) → PSP vault
Merchant server receives token only — out of PCI scope for PAN
```

**Still in scope:**
- Systems handling authentication to payment
- Merchant web server (even if no PAN — SAQ A-EP)

**Architect:** Never log payment payloads; network segment CDE if any card data transits.

### Architecture Perspective

PCI scope directly drives architecture cost — minimize card data touch.

### Follow-up Questions

1. **SAQ types? — A simplest (iframe); D full card environment.**
2. **PAN storage? — Prohibited post-auth except token vault — even encrypted.**

### Common Mistakes in Interviews

- Custom card form posting PAN to own API
- PAN in application logs during debug
- Full PCI audit for whole datacenter unnecessarily

---

## Q009: Payment Tokenization

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Fintech |
| **Frequency** | Very Common |

### Question

Design payment tokenization architecture.

### Short Answer (30 seconds)

PSP tokenizes PAN at capture; merchant stores PSP token for recurring charges. Network tokens (Visa/MC) for higher auth rates. Vault in PSP or dedicated vault HSM — not app database.

### Detailed Answer (3–5 minutes)

**Flows:**
1. **One-time** — Client confirms PaymentIntent; server never sees PAN
2. **Recurring** — Store `payment_method_id` token; charge off-session
3. **Network token** — Scheme-level token replaces PAN in wallet flows

**Architect:** Token lifecycle — revoke on account closure; PCI scope doc updated when flow changes.

### Architecture Perspective

Tokenization is primary PCI scope reduction pattern.

### Follow-up Questions

1. **Store tokens where? — PSP vault preferred; own vault = heavy PCI burden.**
2. **Token reuse across merchants? — Generally no — merchant-scoped tokens.**

### Common Mistakes in Interviews

- Encrypt PAN in DB instead of tokenize
- Tokens in client localStorage
- No webhook signature verify on payment events

---

## Q010: Retail Peak Season Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Enterprise |
| **Frequency** | Very Common |

### Question

Architect e-commerce platform for Black Friday peak season.

### Short Answer (30 seconds)

Pre-scale capacity, CDN cache product pages, queue checkout, read replicas, autoscale with caps tested, degrade non-critical features, war room, synthetic monitoring, freeze changes.

### Detailed Answer (3–5 minutes)

**Peak playbook:**
- Load test 3× expected peak 6 weeks prior
- Pre-warm AKS nodes + Redis
- Checkout queue (virtual waiting room) if overload
- Static product catalog ISR/CDN
- Payment path isolated bulkhead thread pool

**Architect:** Peak architecture ADR with measured headroom — not hope.

### Architecture Perspective

Retail peak is predictable chaos — architecture plans months ahead.

### Follow-up Questions

1. **Virtual queue? — Azure Front Door waiting room or custom — protects origin.**
2. **Feature freeze? — 2 weeks before peak — only hotfix.**

### Common Mistakes in Interviews

- First load test day before Black Friday
- Autoscale never tested at 3×
- Single region for global retail

---

## Q011: Multi-Tenant SaaS Isolation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Enterprise |
| **Frequency** | Very Common |

### Question

Design tenant isolation for multi-tenant SaaS architecture.

### Short Answer (30 seconds)

Isolation levels: shared DB shared schema (row-level tenantId), shared DB separate schema, database per tenant, silo per tenant. Choose by compliance, scale, and noisy neighbor tolerance.

### Detailed Answer (3–5 minutes)

| Model | Isolation | Cost | Use case |
|-------|-----------|------|----------|
| Pooled row | Low | Low | SMB SaaS |
| Schema per tenant | Medium | Medium | Mid-market |
| DB per tenant | High | High | Enterprise/regulated |

**Architect:** Tenant context in every query — middleware enforces tenantId; integration tests for cross-tenant leak.

### Architecture Perspective

Tenant isolation failure is company-ending for SaaS — architect defense in depth.

### Follow-up Questions

1. **Noisy neighbor? — Rate limit per tenant; dedicated pool for whales.**
2. **Tenant provisioning? — Automated pipeline creates schema/DB + config.**

### Common Mistakes in Interviews

- Missing tenantId filter in one query
- Cross-tenant cache key collision
- Enterprise customer on pooled row without contract review

---

## Q012: Tenant Data Partitioning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Enterprise |
| **Frequency** | Very Common |

### Question

Implement tenant data partitioning strategies in SaaS.

### Short Answer (30 seconds)

Partition key = tenantId in shared tables, shard large tenants to dedicated resources, geo-partition by tenant residency requirement, elastic pools for DB cost efficiency.

### Detailed Answer (3–5 minutes)

**Patterns:**
- **Row-level** — `WHERE tenantId = @t` enforced in ORM interceptor
- **Citus/sharding** — tenantId hash for horizontal scale
- **Geo** — EU tenants in EU region — routing at gateway

**Migration:** Tenant lift from pooled to silo without downtime — dual-write ADR.

**Architect:** Partition strategy in ADR — hard to change after 10K tenants.

### Architecture Perspective

Partitioning affects compliance residency and performance isolation.

### Follow-up Questions

1. **Hot tenant? — Detect outlier storage/QPS — move to dedicated shard.**
2. **Backup per tenant? — Required for enterprise SLA — logical export.**

### Common Mistakes in Interviews

- Global table scan without tenant predicate
- Shard key not in unique constraints — cross-shard duplicates
- Residency requirement after pooled design shipped

---

## Q013: Architecture Review Board — Enterprise

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Enterprise |
| **Frequency** | Very Common |

### Question

Run architecture review board for regulated enterprise programs.

### Short Answer (30 seconds)

Charter, tiered review, compliance reps (legal, privacy, security), ADR/RFC workflow, exception registry, audit trail for regulators, SLA for decision.

### Detailed Answer (3–5 minutes)

**Enterprise additions:**
- Compliance sign-off matrix by data classification
- Integration with enterprise risk management (ERM)
- Recordings/minutes retained 7 years
- Pre-audit architecture evidence pack

**Architect:** Board outputs feed SOC2/ISO evidence — not informal.

### Architecture Perspective

Enterprise ARB connects engineering decisions to audit artifacts.

### Follow-up Questions

1. **ARB vs CAB? — CAB change control operational; ARB design decisions — coordinate.**
2. **Waivers? — Time-bound with compensating controls documented.**

### Common Mistakes in Interviews

- Undocumented architecture 'approved in meeting'
- No compliance delegate on board
- Exceptions without expiry review

---

## Q014: Compliance Audit Preparation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Enterprise |
| **Frequency** | Very Common |

### Question

Prepare architecture artifacts for SOC2/ISO compliance audit.

### Short Answer (30 seconds)

Evidence pack: C4 diagrams, ADRs, access control matrices, data flow diagrams, change management records, DR test results, vendor risk assessments, penetration test remediation.

### Detailed Answer (3–5 minutes)

**Auditor requests map to:**
- **CC6 Logical access** — IAM architecture diagram
- **CC7 System ops** — Monitoring SLO dashboards
- **CC8 Change mgmt** — PR + ARB minutes
- **A.12 Operations** — Backup/DR drill logs

**Architect:** Maintain living compliance folder — not scramble before audit.

### Architecture Perspective

Auditors trace controls to diagrams — architecture docs are evidence.

### Follow-up Questions

1. **SOC2 Type II? — Prove controls operated over period — continuous not point-in-time.**
2. **Gap remediation? — Risk register tracks open findings with owner.**

### Common Mistakes in Interviews

- Diagrams outdated vs production
- ADRs missing for major system changes during audit period
- No DR drill evidence

---

## Q015: Vendor Risk Assessment

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Enterprise |
| **Frequency** | Very Common |

### Question

Assess third-party vendor architectural risk.

### Short Answer (30 seconds)

Questionnaire: security certs, data residency, subprocessors, SLA, exit strategy, API lock-in, breach history. Score risk; architecture mitigations (abstraction, data export, multi-vendor).

### Detailed Answer (3–5 minutes)

**Assessment dimensions:**
1. **Security** — SOC2, pen test summary
2. **Privacy** — DPA, GDPR subprocessors
3. **Availability** — SLA, multi-region
4. **Lock-in** — Export API, standard formats
5. **Financial** — Vendor stability

**Architect:** High-risk vendor → wrapper service + ADR documenting dependency and fallback.

### Architecture Perspective

Vendor risk is architecture risk — SolarWinds lesson.

### Follow-up Questions

1. **Fourth party risk? — Vendor's subprocessors — chain responsibility.**
2. **Exit plan? — Export data quarterly test — prove portability.**

### Common Mistakes in Interviews

- Vendor chosen without security review
- Single vendor for identity/payment/database
- No contractual data deletion on exit

---

## Q016: EU Data Residency Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Enterprise |
| **Frequency** | Very Common |

### Question

Design architecture for EU data residency (GDPR).

### Short Answer (30 seconds)

EU tenant data stored/processed in EU region only; no transfer to US without SCCs/adequacy; geo-routing at gateway; residency tags enforced in IaC policy.

### Detailed Answer (3–5 minutes)

**Architecture:**
- Azure West Europe / North Europe region pair
- Tenant metadata `region=EU` → deploy to EU stamp
- Global control plane OK if no personal data
- Pseudonymized analytics only cross-border with legal review

**Architect:** Data residency ADR per product line — Schrems II aware.

### Architecture Perspective

GDPR residency errors trigger fines and customer churn.

### Follow-up Questions

1. **Schrems II impact? — US cloud requires Transfer Impact Assessment.**
2. **Global SaaS admin? — Admin actions audited; admin in EU or SCC.**

### Common Mistakes in Interviews

- EU customer data in US region 'for support'
- Backup replicated to US without legal basis
- No geo-routing — DNS sends EU user to US API

---

## Q017: Acquisition Integration Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Enterprise |
| **Frequency** | Very Common |

### Question

Architect technical integration after corporate acquisition.

### Short Answer (30 seconds)

Due diligence: stack inventory, security debt, data classification. Integration patterns: coexist, federated identity, API bridge, data sync, eventual retire — phased roadmap not big-bang.

### Detailed Answer (3–5 minutes)

**Phases:**
1. **Day 1** — SSO federation, network connectivity, security baseline
2. **Months 1–6** — Customer-facing integration via API/BFF
3. **Year 1–2** — Data consolidation, retire duplicate systems

**Architect:** Integration factory team — reusable patterns, not one-off hacks.

**Risk:** Cultural velocity mismatch — document in program plan.

### Architecture Perspective

M&A architecture is program management + integration patterns.

### Follow-up Questions

1. **Reverse acquihire? — Keep stack temporarily — strangler off legacy.**
2. **Data merge? — Master data management — customer golden record ADR.**

### Common Mistakes in Interviews

- Big-bang cutover weekend merge
- Ignore acquired company's security incidents
- Duplicate CRM forever without retirement plan

---

## Q018: Legacy Modernization Roadmap

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Enterprise |
| **Frequency** | Very Common |

### Question

Build legacy modernization roadmap for enterprise portfolio.

### Short Answer (30 seconds)

Application portfolio assessment: business value vs technical health. Strategies: retain, replatform, refactor, rearchitect, replace, retire (6 R's). Prioritize by risk reduction and ROI.

### Detailed Answer (3–5 minutes)

**Roadmap artifact:**
| System | Health | Value | Strategy | Year | Cost |

**Patterns:**
- **Strangler fig** — incremental replace modules
- **Anti-corruption layer** — isolate legacy model
- **Event intercept** — sync legacy to new world

**Architect:** Roadmap is 3-year living doc — quarterly reprioritize with executives.

### Architecture Perspective

Modernization is portfolio problem — not 'rewrite everything'.

### Follow-up Questions

1. **6 R's? — Gartner — pick per system not one strategy for all.**
2. **Funding? — Tie to risk reduction $ and revenue enablement.**

### Common Mistakes in Interviews

- Rewrite without business case
- Ignore integration dependencies
- No success metrics per wave

---

## Q019: Executive Architecture Briefing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Enterprise |
| **Frequency** | Very Common |

### Question

Deliver executive architecture briefing for major program.

### Short Answer (30 seconds)

30 minutes: business problem, options summary, recommendation, cost/risk/timeline, decision needed today. Visual: one context diagram, three bullets per option, no jargon.

### Detailed Answer (3–5 minutes)

**Structure:**
1. **Hook** — Cost of inaction / regulatory deadline
2. **Options** — A/B/C with trade-off table
3. **Recommendation** — Single clear ask
4. **Investment** — Year 1 vs Year 3 TCO
5. **Risks** — Top 3 with mitigation one-liner
6. **Q&A** — Pre-seed friendly exec questions

**Architect:** Rehearse with product lead — align narrative.

### Architecture Perspective

Executive briefing skill separates senior architects from diagram-only architects.

### Follow-up Questions

1. **Pre-read? — One-page sent 24h before — meeting for decision not education.**
2. **Backup slide? — Technical deep-dive appendix — not in main deck.**

### Common Mistakes in Interviews

- 50-slide architecture review to board
- No decision ask — meeting ends with 'more analysis'
- Technical jargon without business translation

---

## Q020: Board-Level Risk Communication

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Enterprise |
| **Frequency** | Very Common |

### Question

Communicate technology risk to board of directors.

### Short Answer (30 seconds)

Risk register summary, cyber posture trend, major program status, incident themes, regulatory outlook, investment asks — non-technical language, quantified where possible.

### Detailed Answer (3–5 minutes)

**Board deck sections:**
- **Top 5 enterprise tech risks** — likelihood × impact heat map
- **Cyber** — Maturity vs peers, open critical findings
- **Resilience** — DR tier coverage %, last drill outcome
- **Programs** — ERP migration RAG status
- **Ask** — Budget for risk mitigation initiative

**Architect/CIO:** Honest — board hates surprises more than bad news.

### Architecture Perspective

Board communication is fiduciary duty — architecture risks become business risks.

### Follow-up Questions

1. **Material incident? — When to notify board — legal counsel involved.**
2. **Metrics? — MTTR trend, phishing click rate, unpatched critical count.**

### Common Mistakes in Interviews

- Hide cloud misconfiguration from board
- Technical CVE list without business impact
- No linkage between risk register and investment

---

## Q021: Industry Reference Architectures

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Enterprise |
| **Frequency** | Very Common |

### Question

Use industry reference architectures (e.g., Azure Well-Architected, TOGAF, vendor blueprints).

### Short Answer (30 seconds)

Start from reference for speed and audit familiarity; customize with ADRs documenting deltas; map controls to compliance frameworks; don't treat reference as mandatory unchangeable.

### Detailed Answer (3–5 minutes)

**Examples:**
- **Azure WAF** — Five pillars checklist per workload
- **Microsoft Cloud Adoption Framework** — Landing zones
- **Industry** — HL7 FHIR for healthcare, BIAN for banking

**Architect:** Reference = accelerator — gap analysis doc shows what's different and why.

### Architecture Perspective

Reference architectures shorten interviews and audits — know major ones.

### Follow-up Questions

1. **CAF landing zone? — Enterprise-scale Azure foundation — hub-spoke identity.**
2. **FHIR server architecture? — API layer, consent, audit for healthcare interchange.**

### Common Mistakes in Interviews

- Copy reference without threat modeling your data
- Ignore reference when it conflicts with compliance
- Reference architecture shelfware — never mapped to systems

---

## Q022: Regulated Change Control

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Enterprise |
| **Frequency** | Very Common |

### Question

Design change control for regulated environments (SOX, GxP).

### Short Answer (30 seconds)

Separate dev/prod, PR review, automated tests, CAB approval for prod, segregation of duties, audit trail immutable, emergency change process with retrospective.

### Detailed Answer (3–5 minutes)

**SOX ITGC mapping:**
- Change management control — PR + approval evidence
- Access — no developer prod write
- Operations — monitoring alerts

**Emergency change:** Break glass with ticket, deploy, ARB review within 48h.

**Architect:** IaC pipelines are change control — Terraform plan approval artifact.

### Architecture Perspective

Regulated change control is architecture process — not optional paperwork.

### Follow-up Questions

1. **GxP validated system? — Revalidation scope on change — CSV documentation.**
2. **Segregation of duties? — Same person can't code and approve prod deploy.**

### Common Mistakes in Interviews

- Direct prod DB edit by developer
- No audit trail on infrastructure changes
- Emergency change without retrospective review

---

## Q023: BAA with Cloud Providers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Healthcare |
| **Frequency** | Very Common |

### Question

Manage Business Associate Agreements for cloud architecture.

### Short Answer (30 seconds)

Execute BAA with Azure/AWS before PHI; use only BAA-covered services; subprocessors listed; breach notification timelines; document in vendor register.

### Detailed Answer (3–5 minutes)

**Azure:** Microsoft BAA covers eligible PaaS — verify service list quarterly.

**Architecture impact:**
- No PHI in non-eligible service (e.g., certain AI features without BAA)
- Region selection affects BAA coverage

**Architect:** Legal owns BAA signature; architect owns service eligibility matrix.

### Architecture Perspective

BAA gaps stop healthcare deployments — check before design finalization.

### Follow-up Questions

1. **Subprocessor notification? — Cloud provider updates — legal review pipeline.**
2. **Multi-cloud PHI? — Separate BAA per provider — complexity.**

### Common Mistakes in Interviews

- PHI in service without BAA coverage
- Assumed all Azure services covered
- BAA signed but architecture uses non-eligible feature

---

## Q024: SOX IT General Controls

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Enterprise |
| **Frequency** | Very Common |

### Question

Map architecture to SOX IT general controls.

### Short Answer (30 seconds)

Access control, change management, computer operations, program development — architecture provides evidence: IAM design, CI/CD approvals, monitoring, SDLC gates.

### Detailed Answer (3–5 minutes)

**Architect artifacts for auditors:**
- Identity: Entra ID PIM, no shared accounts
- Change: Git PR, pipeline environment gates
- Ops: Backup, DR, incident management integration
- Development: Test environments, code review policy

**Scope:** Systems affecting financial reporting — identify in application inventory.

### Architecture Perspective

SOX drives access and change architecture for finance-related systems.

### Follow-up Questions

1. **In scope system? — If touches GL, revenue recognition — SOX applies.**
2. **PIM? — Just-in-time admin — SOX-friendly privileged access.**

### Common Mistakes in Interviews

- Shared admin password on production
- Deploy pipeline skips approval for 'speed'
- Financial reporting DB accessible from dev network

---

## Q025: GDPR Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Enterprise |
| **Frequency** | Very Common |

### Question

Implement GDPR principles in system architecture.

### Short Answer (30 seconds)

Lawful basis documented, data minimization, purpose limitation, storage limitation, right to erasure pipeline, DPIA for high-risk processing, DPO consultation, privacy by design.

### Detailed Answer (3–5 minutes)

**Technical measures:**
- Consent management platform integration
- Erasure workflow across microservices (event `UserDeleted`)
- Pseudonymization in analytics
- ROPA (Record of Processing Activities) linked to services

**Architect:** Erasure is cross-system orchestration — not single DELETE SQL.

### Architecture Perspective

GDPR is architectural — erasure and consent propagate across services.

### Follow-up Questions

1. **DPIA trigger? — Large-scale special category data, systematic monitoring.**
2. **Data portability? — Export API machine-readable format.**

### Common Mistakes in Interviews

- Analytics retains data after erasure request
- No lawful basis documented per processing purpose
- Privacy policy only — no technical controls

---

## Q026: High Availability Retail

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Enterprise |
| **Frequency** | Very Common |

### Question

Design high availability for retail transaction systems.

### Short Answer (30 seconds)

Multi-AZ deployment, no single point of failure, health checks, autoscale, circuit breakers, graceful degradation (browse without checkout), geo-DR for Tier-1, cache product catalog.

### Detailed Answer (3–5 minutes)

**HA patterns:**
- Active-active API across AZs
- DB with synchronous replica in-region
- CDN for static/browse path
- Queue buffers order spikes
- Idempotent payment processing

**Target:** 99.99% availability during peak — error budget managed year-round.

### Architecture Perspective

Retail HA balances cost with revenue loss per minute downtime.

### Follow-up Questions

1. **Graceful degradation? — Disable recommendations before checkout fails.**
2. **Inventory oversell? — Distributed lock or reservation pattern at peak.**

### Common Mistakes in Interviews

- Single AZ database for checkout
- No health check on payment dependency
- Cold DR region never tested before peak

---

## Q027: Omnichannel Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Enterprise |
| **Frequency** | Very Common |

### Question

Architect omnichannel retail (web, mobile, store, call center).

### Short Answer (30 seconds)

Unified customer identity, inventory visibility across channels, order orchestration, consistent pricing/promo engine, event-driven sync, BOPIS (buy online pickup in store).

### Detailed Answer (3–5 minutes)

**Core services:**
- **Customer MDM** — Golden profile
- **Inventory** — Real-time ATP (available-to-promise)
- **Order hub** — Route to store/DC for fulfillment
- **Store POS integration** — API or event sync

**Architect:** Omnichannel is integration architecture — not channel silos.

### Architecture Perspective

Omnichannel breaks without unified inventory and identity.

### Follow-up Questions

1. **BOPIS? — Reserve inventory at store — race condition architecture.**
2. **Call center view? — Same order history API as web — single source.**

### Common Mistakes in Interviews

- Separate inventory silos per channel
- Store returns can't see online purchase
- Promo engine different rules web vs store

---

## Q028: Supply Chain Integration Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Enterprise |
| **Frequency** | Very Common |

### Question

Integrate supply chain systems (ERP, WMS, TMS) with e-commerce architecture.

### Short Answer (30 seconds)

Event-driven integration, anti-corruption layers around ERP, idempotent sync, batch for heavy master data, real-time for inventory ATP, clear system of record per entity.

### Detailed Answer (3–5 minutes)

**Patterns:**
- **ERP (SAP)** — System of record for finance/inventory master
- **WMS** — Fulfillment execution events → Order service
- **EDI/API** — Supplier ASN inbound

**Integration hub:** Azure Service Bus / iPaaS (Logic Apps, MuleSoft) with canonical model.

**Architect:** Latency expectations — ERP not synchronous in checkout path.

### Architecture Perspective

Supply chain integration is async-first — don't block UX on SAP round-trip.

### Follow-up Questions

1. **ATP calculation? — Near-real-time cache fed by inventory events — not live SAP query.**
2. **Failure? — Stale inventory better than checkout hang — TTL and fallback.**

### Common Mistakes in Interviews

- Synchronous SAP call in checkout request
- No idempotency on inventory adjustment events
- Duplicate product master in ecommerce and ERP

---

## Q029: Case Study Presentation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Enterprise |
| **Frequency** | Very Common |

### Question

Structure architecture case study presentation for interview or executive review.

### Short Answer (30 seconds)

Situation, constraints, options considered, decision, implementation highlights, outcomes/metrics, lessons learned — 20 minutes with diagram, show trade-off thinking not perfection.

### Detailed Answer (3–5 minutes)

**Template:**
1. **Context** — Business, scale, team
2. **Problem** — NFRs and pain
3. **Constraints** — Budget, legacy, timeline
4. **Options** — 2–3 with pros/cons table
5. **Decision** — ADR summary
6. **Results** — Latency, cost, incidents before/after
7. **Reflection** — What you'd do differently

**Interview:** Interviewer probes alternatives — defend with data.

### Architecture Perspective

Case study presentation proves architect judgment — not memorized patterns.

### Follow-up Questions

1. **STAR vs architecture case? — Add explicit options and trade-offs — STAR alone weak.**
2. **Metrics? — 'Reduced p99 800ms→220ms' beats 'improved performance'.**

### Common Mistakes in Interviews

- Only happy path — no constraints mentioned
- No alternatives considered in story
- Cannot explain why rejected option was rejected

---

## Q030: Architecture Portfolio

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Enterprise |
| **Frequency** | Very Common |

### Question

Maintain architecture portfolio for enterprise architect role.

### Short Answer (30 seconds)

Collection of ADRs, reference diagrams, case studies, assessments, standards authored — demonstrates breadth, depth, and business impact for promotion and interviews.

### Detailed Answer (3–5 minutes)

**Portfolio contents:**
- 3–5 deep case studies with metrics
- ADR samples showing lifecycle including supersede
- C4 diagram pack
- Modernization roadmap you led
- Conference/internal talk slides

**Maintenance:** Redact confidential names; use anonymized metrics.

**Architect:** Portfolio is career asset — update quarterly after major programs.

### Architecture Perspective

Architecture portfolio proves seniority better than certification list alone.

### Follow-up Questions

1. **Interview portfolio? — 30-min walkthrough rehearsed — one flagship case.**
2. **Anonymization? — 'Fortune 500 retailer' — real numbers where allowed.**

### Common Mistakes in Interviews

- No written record of decisions led
- Portfolio only diagrams no outcomes
- Identical resume bullet without depth material

---
