# Week 46 — Expert Scenario Q&A

> Q101–Q120: Premium format (Week 1 quality).

---


## Q101: Hot Shard Tenant Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Sharding |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Enterprise tenant outgrows shard — migration plan?

### Short Answer (30 seconds)

Dual-write period, async copy historical data, flip read routing via shard map, verify counts, remove from old shard, monitor lag — minimal downtime window.

### Detailed Answer

**Steps:**
1. Provision new shard capacity
2. Background copy tenant data
3. Enable dual-write both shards
4. Cutover read to new shard
5. Stop writes old shard, delete tenant data there

**Architect:** Runbook for whale tenant — rehearse on staging copy.

### Architecture Perspective

Resharding is expert operational architecture scenario.

### Follow-up Questions

1. **Consistent hash resharding? — Many keys move — use established tooling.**
2. **Tenant freeze window? — Brief read-only acceptable for cutover.**

### Common Mistakes in Interviews

- Big-bang copy without dual-write
- No tenant-level routing tests
- Ignore cross-shard FK constraints

---

## Q102: CAP Payment Partition Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Distributed Systems |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Network partition during payment processing — design behavior?

### Short Answer (30 seconds)

CP: reject writes on minority partition; queue client retries; idempotency keys; never double-charge. AP alternative unacceptable for ledger — choose CP with graceful user messaging.

### Detailed Answer

**Design:**
- Strong consistency primary
- Minority partition returns 503 with Retry-After
- Idempotency-Key on all payment POSTs
- Outbox for downstream notifications after commit

**Architect:** Payments are CP — document in consistency matrix.

### Architecture Perspective

Expert CAP — concrete financial partition behavior.

### Follow-up Questions

1. **Split brain prevention? — Quorum writes only.**
2. **Compensating transaction? — Refund saga if duplicate detected.**

### Common Mistakes in Interviews

- AP ledger merge after partition
- No idempotency on retries
- Silent duplicate charge

---

## Q103: FinOps Executive Review

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | FinOps |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Present 40% cloud overspend to executive committee — structure?

### Short Answer (30 seconds)

Lead with business impact, root causes (oversizing, orphans, no autoscale), remediation plan with savings timeline, governance changes, not blame engineering.

### Detailed Answer

**Deck:**
1. Spend trend vs budget
2. Top 5 cost drivers (VM SKU, logs, egress)
3. Quick wins 30 days
4. Structural fixes (tagging, policies, reviews)
5. Unit economics target

**Architect:** Partner with FinOps — engineering owns efficiency execution.

### Architecture Perspective

Executive communication is staff architect skill.

### Follow-up Questions

1. **Chargeback activation? — Accountability changes behavior.**
2. **Commitment purchase after right-size? — Phase savings.**

### Common Mistakes in Interviews

- Blame teams without data
- Vague 'optimize cloud' plan
- No ongoing governance

---

## Q104: Landing Zone Brownfield

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Cloud Architecture |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Retrofit landing zone on 200 existing Azure subscriptions.

### Short Answer (30 seconds)

Inventory subscriptions, move to MG hierarchy, apply policies in audit then deny mode, network hub integration phased, exception process for legacy non-compliant.

### Detailed Answer

**Phases:**
1. Discovery and tagging blitz
2. MG migration — read-only policies
3. Network hub for new workloads first
4. Remediate critical security deny violations
5. Legacy sunset timeline

**Architect:** Brownfield harder than greenfield — prioritize risk-based.

### Architecture Perspective

Real enterprise scenario — not greenfield textbook.

### Follow-up Questions

1. **Policy exemption TTL? — Force remediation deadline.**
2. **Subscription cancel? — Retire unused in decommission MG.**

### Common Mistakes in Interviews

- Big-bang deny policies break prod
- Ignore existing VNet overlaps
- No exception workflow

---

## Q105: Cross-Cloud Identity Federation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | IAM |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Design identity for app spanning Azure and AWS.

### Short Answer (30 seconds)

Entra ID as IdP, AWS IAM Identity Center SAML federation, workload identities per cloud, no shared long-lived keys, centralized group management.

### Detailed Answer

**Human access:** SSO both portals via Entra.

**Workload:** Azure MI + AWS IAM role — no cross-cloud identity merge — dual identities with correlation in app config.

**Architect:** Document dual identity ops — rotation and audit both planes.

### Architecture Perspective

Multi-cloud identity is complex — expert interview topic.

### Follow-up Questions

1. **OIDC federation CI/CD? — GitHub Actions to both clouds.**
2. **SCIM provisioning? — Automate user lifecycle.**

### Common Mistakes in Interviews

- Duplicate human IAM users both clouds
- Shared root credentials
- No SSO — password vault per cloud

---

## Q106: Event Sourcing DR Replay

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Event-Driven |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Recover service using event log replay after corruption.

### Short Answer (30 seconds)

Immutable event store backup, rebuild read models from offset zero, idempotent projections, versioned handlers, validate checksum against golden counts.

### Detailed Answer

**DR:**
- Event Hubs capture to ADLS immutable
- Replay tool applies events to empty projection DB
- Compare row counts and sample hashes

**Architect:** Event sourcing DR is replay test — not SQL restore only.

### Architecture Perspective

Event-sourced DR differs from CRUD backup restore.

### Follow-up Questions

1. **Handler versioning? — Upcast old events to new schema.**
2. **Snapshot optimization? — Periodic snapshots shorten replay time.**

### Common Mistakes in Interviews

- Delete event log after projection
- Non-idempotent projection replay
- Never test full replay

---

## Q107: Global Traffic Failover Data

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Disaster Recovery |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Failover global traffic when primary region database corrupt.

### Short Answer (30 seconds)

Stop writes primary, promote secondary, verify replication lag acknowledged data loss within RPO, flip Front Door priority, invalidate caches, run reconciliation job.

### Detailed Answer

**Communication:** Status page, RPO breach notification if applicable.

**Post-incident:** Root cause, backup restore validation, game day update.

**Architect:** Corruption ≠ region down — different runbook branch.

### Architecture Perspective

Expert DR combines traffic + data promotion.

### Follow-up Questions

1. **Forced failover SQL? — May lose async replicated data.**
2. **Cache stampede on failover? — Warm secondary caches gradually.**

### Common Mistakes in Interviews

- Flip traffic before DB promotion
- No RPO communication plan
- Single runbook all failure types

---

## Q108: Serverless Cost Incident

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Serverless |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Azure Functions bill 10× after DDoS on HTTP trigger.

### Short Answer (30 seconds)

Enable APIM/WAF rate limiting, function auth keys, consumption limits, alert on execution count anomaly, CDN edge protection.

### Detailed Answer

**Immediate:** Block attacker IP, disable public HTTP trigger, rotate keys.

**Prevention:** JWT auth on functions, private endpoint + APIM only, per-tenant quotas.

**Architect:** Public unauthenticated HTTP function is cost bomb.

### Architecture Perspective

Serverless security equals cost control.

### Follow-up Questions

1. **DDoS Protection Standard? — Network layer complement.**
2. **Max instances cap? — Consumption plan limits.**

### Common Mistakes in Interviews

- Public anonymous function endpoint
- No execution metrics alert
- Retry storm from client amplifies cost

---

## Q109: Index Strategy Review Board

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | SQL Indexing |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Architecture review rejects proposed 15 new indexes — negotiate?

### Short Answer (30 seconds)

Ask for top 3 slow queries with plans, propose covering indexes for those only, schedule review of unused indexes to drop, measure write impact.

### Detailed Answer

**Data:** Each index costs insert/update CPU — net benefit required.

**Compromise:** 3 indexes now, monitor 30 days, revisit.

**Architect:** Index proposals need workload evidence — not DBA habit.

### Architecture Perspective

Governance negotiation shows senior judgment.

### Follow-up Questions

1. **Missing index DMV? — Suggestive not gospel — verify queries.**
2. **Index hygiene quarterly? — Drop unused — frees write budget.**

### Common Mistakes in Interviews

- Approve all 15 without analysis
- Reject all indexes dogmatically
- No before/after metrics

---

## Q110: Hybrid SAP on Azure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Hybrid Cloud |
| **Frequency** | Occasional |
| **Type** | Scenario |

### Question

Integrate SAP ERP on-prem with cloud-native order API.

### Short Answer (30 seconds)

Azure Integration Services or event-driven iPaaS, private connectivity, idempotent adapters, no direct SAP DB coupling, message contracts versioned.

### Detailed Answer

**Patterns:**
- SAP PI/PO or Logic Apps connector
- Events for order confirmation async
- Private Link / ExpressRoute mandatory

**Architect:** Anti-corruption layer between SAP IDoc and cloud domain model.

### Architecture Perspective

Enterprise hybrid integration expert scenario.

### Follow-up Questions

1. **SAP on Azure VMs? — Large instances — separate sizing review.**
2. **Dual write SAP and cloud? — Outbox from cloud — SAP callback confirms.**

### Common Mistakes in Interviews

- Direct SAP DB connection from API
- Synchronous SAP call in user HTTP path
- No anti-corruption layer

---

## Q111: Multi-Region Cosmos Conflict

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Distributed Systems |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Design conflict resolution for Cosmos multi-region writes.

### Short Answer (30 seconds)

Choose LWW with sensible timestamp, or application merge for cart/inventory, or partition so conflicts impossible per business key.

### Detailed Answer

**Inventory:** Operational transform or reserve with TTL.

**Profile:** Merge function registered in Cosmos.

**Architect:** Conflicts prove active-active data model wasn't thought through.

### Architecture Perspective

Multi-write Cosmos requires explicit conflict design.

### Follow-up Questions

1. **Strong consistency multi-region? — Not for writes globally.**
2. **Session token routing? — Read-your-writes after own write.**

### Common Mistakes in Interviews

- LWW on financial balance
- No conflict handling registered
- Surprised by duplicate writes after partition

---

## Q112: Regulatory Data Residency

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Compliance |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

GDPR requires EU data residency — architect Azure solution.

### Short Answer (30 seconds)

Deploy EU region only, policy deny deploy outside EU, Private Link, DPA with Microsoft, encryption CMK in EU Key Vault, audit no US replication paths.

### Detailed Answer

**Checks:**
- Cosmos geo-replication pairs EU only
- Backup geo-redundant LRS within EU
- Support staff access logging

**Architect:** Residency is policy + architecture — not checkbox cert.

### Architecture Perspective

Compliance architecture expert question.

### Follow-up Questions

1. **Schrems II? — Transfer impact assessment for US support.**
2. **Pseudonymization? — Reduce PII scope.**

### Common Mistakes in Interviews

- US region DR copies EU PII silently
- Global CDN caching PII
- No policy deny non-EU regions

---

## Q113: Staff Cloud Strategy Interview

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Interview Skills |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

CTO asks 'Azure or AWS?' in staff interview — respond?

### Short Answer (30 seconds)

Clarify existing estate, team skills, compliance, and workloads. Recommend primary cloud aligned to Entra/hybrid if Microsoft shop; don't religiously dismiss either; multi-cloud DR only if required.

### Detailed Answer

**Structure:**
- Current state assessment
- Workload fit matrix
- TCO 3-year model rough
- Risk: skills, vendor, exit
- Recommendation with triggers to revisit

**Staff signal:** Business-aligned recommendation not fanboyism.

### Architecture Perspective

Cloud choice is organizational fit — expert interview closer.

### Follow-up Questions

1. **When AWS wins? — ML research team on AWS, acquisition.**
2. **When Azure wins? — M365 Entra integration, .NET estate.**

### Common Mistakes in Interviews

- Pick cloud by personal cert
- Multi-cloud active without requirement
- No TCO or skills assessment

---

## Q114: Migration Wave Failure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Migration |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Wave 2 migration caused 4-hour outage — postmortem lead?

### Short Answer (30 seconds)

Timeline, root cause (DNS, connection string, firewall), blast radius, what detection missed, corrective actions with owners, wave 3 gate criteria.

### Detailed Answer

**Common misses:**
- Connection pool to old IP
- Forgotten batch job on old VM
- SQL firewall rule

**Architect:** Blameless postmortem — improve runbook not punish engineer.

### Architecture Perspective

Incident leadership is architect responsibility.

### Follow-up Questions

1. **Rollback criteria pre-defined? — Should be in wave plan.**
2. **Dry-run mandatory? — Full dress rehearsal next wave.**

### Common Mistakes in Interviews

- Hide outage from stakeholders
- No wave gate after failure
- Same runbook untested wave 3

---

## Q115: Blob Lifecycle Cost Model

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | FinOps |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Model storage cost savings with blob lifecycle policy.

### Short Answer (30 seconds)

10 TB logs hot $180/TB → cool after 30d saves ~40%; archive after 180d for compliance retention 7 years at fraction of hot cost.

### Detailed Answer

**Calculation:**
- Hot 10TB month 1
- Cool 9TB month 2+
- Archive 8TB year 2+

**Present:** 3-year TCO comparison vs all hot.

**Architect:** Lifecycle policy in IaC — not manual tier changes.

### Architecture Perspective

Quantified FinOps proposal wins budget.

### Follow-up Questions

1. **Retrieval cost archive? — Model restore drills annually.**
2. **Early deletion cool tier? — Penalty if moved too soon.**

### Common Mistakes in Interviews

- All hot 'for simplicity'
- Archive without restore test
- Ignore early deletion fees

---

## Q116: Service Mesh vs APIM

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Architecture |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

APIM vs service mesh for microservices security — when each?

### Short Answer (30 seconds)

APIM: north-south external API gateway, throttling, WAF integration, developer portal. Service mesh: east-west mTLS, retries, observability between internal services.

### Detailed Answer

**Together:** APIM at edge, Istio/Linkerd internal — not either-or.

**APIM:** Partner APIs, rate limits, OAuth, developer portal.

**Mesh:** Service-to-service mTLS, traffic splitting, golden metrics per service.

**Architect:** Don't mesh 5 services — overhead; do mesh 50+ with mTLS requirement.

### Architecture Perspective

Traffic direction defines gateway vs mesh.

### Follow-up Questions

1. **Dapr? — Simpler building blocks — alternative to full mesh.**
2. **When skip both? — Small monolith behind single load balancer.**

### Common Mistakes in Interviews

- APIM between every internal call
- Mesh without mTLS requirement justification
- Double retry APIM and mesh uncoordinated

---

## Q117: Expert SQL Scale Review

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | SQL Indexing |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Single Azure SQL 4 TB approaching limits — options?

### Short Answer (30 seconds)

Vertical scale limits, read replicas, archive historical partitions, shard hot tenant, migrate warehouse to Synapse, elastic pool split databases.

### Detailed Answer

**Decision tree:**
1. Read heavy? → Replicas + caching
2. Write heavy single tenant? → Shard
3. Analytics on same DB? → Split OLAP
4. True scale ceiling? → Distributed solution

**Architect:** Avoid heroic single-DB beyond designed limits.

### Architecture Perspective

Scale ceiling expert scenario — options not panic.

### Follow-up Questions

1. **Hyperscale tier? — Azure SQL Hyperscale 100TB+.**
2. **Archive strategy? — Move cold data — shrink working set.**

### Common Mistakes in Interviews

- Keep growing one DB forever
- Shard without query router plan
- Analytics on primary OLTP

---

## Q118: Event-Driven Monolith Extract

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Event-Driven |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Extract notification service from monolith using events.

### Short Answer (30 seconds)

Monolith publishes OrderPlaced to Service Bus after outbox; new notification service subscribes; monolith keeps sync path until consumer proven; delete old code behind flag.

### Detailed Answer

**Strangler steps:**
1. Add outbox + publish
2. Build consumer duplicate send (shadow)
3. Compare outputs
4. Cutover send to consumer
5. Remove monolith notification module

**Architect:** Dual-run validation before cutover.

### Architecture Perspective

Event-driven extraction is pragmatic strangler.

### Follow-up Questions

1. **Schema versioning? — v1 event contract stable.**
2. **Rollback? — Feature flag revert to monolith send.**

### Common Mistakes in Interviews

- Big-bang delete monolith code day one
- No shadow comparison period
- Breaking event contract on extract

---

## Q119: IAM Privilege Escalation Audit

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | IAM |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Audit finds app identity with Owner on subscription — remediate?

### Short Answer (30 seconds)

Immediate scope reduction to least privilege, rotate secrets if any, audit Activity Log for misuse, policy deny Owner on managed identities, break-glass separate.

### Detailed Answer

**Remediation:**
1. Replace with role scoped to resource group
2. Specific data plane roles only
3. Alert on Owner assignments
4. PR check on Terraform IAM

**Architect:** CI policy validation prevents recurrence.

### Architecture Perspective

IAM incident response expert scenario.

### Follow-up Questions

1. **PIM for humans? — JIT Owner for admins only.**
2. **Defender for Cloud alert? — Excessive permissions detection.**

### Common Mistakes in Interviews

- Leave Owner 'temporary' months
- No activity log review
- No IaC IAM review in CI

---

## Q120: Architecture Review Synthesis

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Interview Skills |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

45-minute panel: defend hybrid cloud design under skeptical security architect.

### Short Answer (30 seconds)

Acknowledge risks, cite controls (Private Link, ER, PIM, policy), shared responsibility, compliance mappings, offer phased hardening roadmap, stay calm on trade-offs.

### Detailed Answer

**Techniques:**
- Repeat concern — validate auditor
- Evidence: pen test, logs, policy IDs
- Trade-off explicit: latency vs private path
- Escalation path for unresolved risk

**Architect:** Collaboration not combat — security partner.

### Architecture Perspective

Panel defense is staff interview simulation.

### Follow-up Questions

1. **Document accepted risks? — ARB sign-off with expiry.**
2. **Red team results? — Proactive credibility.**

### Common Mistakes in Interviews

- Dismiss security concerns
- Hand-wave 'cloud is secure'
- No documented compensating controls

---
