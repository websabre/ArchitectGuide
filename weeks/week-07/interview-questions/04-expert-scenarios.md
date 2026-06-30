# Week 07 — Expert Scenario Q&A

> Q101–Q120: Premium format (Week 1 quality).

---


## Q101: TDE encryption Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

A SQL Server Architecture system experiences cascading failures. Walk through your response using concepts including TDE encryption.

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing TDE encryption and tde cmk key vault.

### Detailed Answer

**Situation (Production incident):** A SQL Server Architecture system experiences cascading failures. Walk through your response using concepts including TDE encryption.

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around TDE encryption
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of TDE encryption
- Check recent changes (deploy, config, scale event)
- Reference production pattern: TDE CMK Key Vault

**Recommendation:**
- Short-term containment with explicit residual risk
- Medium-term fix with measurable acceptance criteria
- Long-term ADR update and guardrails (dashboards, tests, runbooks)

**Executive summary:** Business impact, root cause hypothesis, decision needed, timeline.

### Architecture Perspective

Expert scenarios test leadership under uncertainty — structured response beats heroic debugging.

### Follow-up Questions

1. **What if initial hypothesis wrong? — Time-box investigation; pivot with new evidence.**
2. **Who must sign off residual risk? — Product + ops + security as applicable.**

### Common Mistakes in Interviews

- Panic changes without rollback plan
- Technical fix without communication plan
- No follow-up ADR or runbook update after incident

---

## Q102: Always Encrypted Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Review a team's SQL Server Architecture design that omits Always Encrypted. What risks do you flag?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Always Encrypted and deterministic ae limited.

### Detailed Answer

**Situation (Architecture review):** Review a team's SQL Server Architecture design that omits Always Encrypted. What risks do you flag?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Always Encrypted
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Always Encrypted
- Check recent changes (deploy, config, scale event)
- Reference production pattern: Deterministic AE limited

**Recommendation:**
- Short-term containment with explicit residual risk
- Medium-term fix with measurable acceptance criteria
- Long-term ADR update and guardrails (dashboards, tests, runbooks)

**Executive summary:** Business impact, root cause hypothesis, decision needed, timeline.

### Architecture Perspective

Expert scenarios test leadership under uncertainty — structured response beats heroic debugging.

### Follow-up Questions

1. **What if initial hypothesis wrong? — Time-box investigation; pivot with new evidence.**
2. **Who must sign off residual risk? — Product + ops + security as applicable.**

### Common Mistakes in Interviews

- Panic changes without rollback plan
- Technical fix without communication plan
- No follow-up ADR or runbook update after incident

---

## Q103: Dynamic data masking Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Leadership wants to build in-house vs buy SaaS for SQL Server Architecture. How does Dynamic data masking inform your recommendation?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Dynamic data masking and ddm credit card mask.

### Detailed Answer

**Situation (Build vs buy):** Leadership wants to build in-house vs buy SaaS for SQL Server Architecture. How does Dynamic data masking inform your recommendation?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Dynamic data masking
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Dynamic data masking
- Check recent changes (deploy, config, scale event)
- Reference production pattern: DDM credit card mask

**Recommendation:**
- Short-term containment with explicit residual risk
- Medium-term fix with measurable acceptance criteria
- Long-term ADR update and guardrails (dashboards, tests, runbooks)

**Executive summary:** Business impact, root cause hypothesis, decision needed, timeline.

### Architecture Perspective

Expert scenarios test leadership under uncertainty — structured response beats heroic debugging.

### Follow-up Questions

1. **What if initial hypothesis wrong? — Time-box investigation; pivot with new evidence.**
2. **Who must sign off residual risk? — Product + ops + security as applicable.**

### Common Mistakes in Interviews

- Panic changes without rollback plan
- Technical fix without communication plan
- No follow-up ADR or runbook update after incident

---

## Q104: Row level security Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Auditors question your SQL Server Architecture architecture regarding Row level security. How do you respond?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Row level security and rls predicate tenant.

### Detailed Answer

**Situation (Regulatory audit):** Auditors question your SQL Server Architecture architecture regarding Row level security. How do you respond?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Row level security
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Row level security
- Check recent changes (deploy, config, scale event)
- Reference production pattern: RLS predicate tenant

**Recommendation:**
- Short-term containment with explicit residual risk
- Medium-term fix with measurable acceptance criteria
- Long-term ADR update and guardrails (dashboards, tests, runbooks)

**Executive summary:** Business impact, root cause hypothesis, decision needed, timeline.

### Architecture Perspective

Expert scenarios test leadership under uncertainty — structured response beats heroic debugging.

### Follow-up Questions

1. **What if initial hypothesis wrong? — Time-box investigation; pivot with new evidence.**
2. **Who must sign off residual risk? — Product + ops + security as applicable.**

### Common Mistakes in Interviews

- Panic changes without rollback plan
- Technical fix without communication plan
- No follow-up ADR or runbook update after incident

---

## Q105: Column encryption keys Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Traffic will 10x in 6 months. What changes involving Column encryption keys do you prioritize in SQL Server Architecture?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Column encryption keys and cek ssn column.

### Detailed Answer

**Situation (Scale 10x):** Traffic will 10x in 6 months. What changes involving Column encryption keys do you prioritize in SQL Server Architecture?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Column encryption keys
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Column encryption keys
- Check recent changes (deploy, config, scale event)
- Reference production pattern: CEK SSN column

**Recommendation:**
- Short-term containment with explicit residual risk
- Medium-term fix with measurable acceptance criteria
- Long-term ADR update and guardrails (dashboards, tests, runbooks)

**Executive summary:** Business impact, root cause hypothesis, decision needed, timeline.

### Architecture Perspective

Expert scenarios test leadership under uncertainty — structured response beats heroic debugging.

### Follow-up Questions

1. **What if initial hypothesis wrong? — Time-box investigation; pivot with new evidence.**
2. **Who must sign off residual risk? — Product + ops + security as applicable.**

### Common Mistakes in Interviews

- Panic changes without rollback plan
- Technical fix without communication plan
- No follow-up ADR or runbook update after incident

---

## Q106: Audit specification Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

A SQL Server Architecture system experiences cascading failures. Walk through your response using concepts including Audit specification.

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Audit specification and server audit specification.

### Detailed Answer

**Situation (Production incident):** A SQL Server Architecture system experiences cascading failures. Walk through your response using concepts including Audit specification.

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Audit specification
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Audit specification
- Check recent changes (deploy, config, scale event)
- Reference production pattern: Server audit specification

**Recommendation:**
- Short-term containment with explicit residual risk
- Medium-term fix with measurable acceptance criteria
- Long-term ADR update and guardrails (dashboards, tests, runbooks)

**Executive summary:** Business impact, root cause hypothesis, decision needed, timeline.

### Architecture Perspective

Expert scenarios test leadership under uncertainty — structured response beats heroic debugging.

### Follow-up Questions

1. **What if initial hypothesis wrong? — Time-box investigation; pivot with new evidence.**
2. **Who must sign off residual risk? — Product + ops + security as applicable.**

### Common Mistakes in Interviews

- Panic changes without rollback plan
- Technical fix without communication plan
- No follow-up ADR or runbook update after incident

---

## Q107: Extended events lightweight Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Review a team's SQL Server Architecture design that omits Extended events lightweight. What risks do you flag?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Extended events lightweight and xevent deadlock capture.

### Detailed Answer

**Situation (Architecture review):** Review a team's SQL Server Architecture design that omits Extended events lightweight. What risks do you flag?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Extended events lightweight
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Extended events lightweight
- Check recent changes (deploy, config, scale event)
- Reference production pattern: XEvent deadlock capture

**Recommendation:**
- Short-term containment with explicit residual risk
- Medium-term fix with measurable acceptance criteria
- Long-term ADR update and guardrails (dashboards, tests, runbooks)

**Executive summary:** Business impact, root cause hypothesis, decision needed, timeline.

### Architecture Perspective

Expert scenarios test leadership under uncertainty — structured response beats heroic debugging.

### Follow-up Questions

1. **What if initial hypothesis wrong? — Time-box investigation; pivot with new evidence.**
2. **Who must sign off residual risk? — Product + ops + security as applicable.**

### Common Mistakes in Interviews

- Panic changes without rollback plan
- Technical fix without communication plan
- No follow-up ADR or runbook update after incident

---

## Q108: DMV performance baseline Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Leadership wants to build in-house vs buy SaaS for SQL Server Architecture. How does DMV performance baseline inform your recommendation?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing DMV performance baseline and baseline wait stats weekly.

### Detailed Answer

**Situation (Build vs buy):** Leadership wants to build in-house vs buy SaaS for SQL Server Architecture. How does DMV performance baseline inform your recommendation?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around DMV performance baseline
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of DMV performance baseline
- Check recent changes (deploy, config, scale event)
- Reference production pattern: Baseline wait stats weekly

**Recommendation:**
- Short-term containment with explicit residual risk
- Medium-term fix with measurable acceptance criteria
- Long-term ADR update and guardrails (dashboards, tests, runbooks)

**Executive summary:** Business impact, root cause hypothesis, decision needed, timeline.

### Architecture Perspective

Expert scenarios test leadership under uncertainty — structured response beats heroic debugging.

### Follow-up Questions

1. **What if initial hypothesis wrong? — Time-box investigation; pivot with new evidence.**
2. **Who must sign off residual risk? — Product + ops + security as applicable.**

### Common Mistakes in Interviews

- Panic changes without rollback plan
- Technical fix without communication plan
- No follow-up ADR or runbook update after incident

---

## Q109: Query hash plan analysis Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Auditors question your SQL Server Architecture architecture regarding Query hash plan analysis. How do you respond?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Query hash plan analysis and query hash regression compare.

### Detailed Answer

**Situation (Regulatory audit):** Auditors question your SQL Server Architecture architecture regarding Query hash plan analysis. How do you respond?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Query hash plan analysis
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Query hash plan analysis
- Check recent changes (deploy, config, scale event)
- Reference production pattern: Query hash regression compare

**Recommendation:**
- Short-term containment with explicit residual risk
- Medium-term fix with measurable acceptance criteria
- Long-term ADR update and guardrails (dashboards, tests, runbooks)

**Executive summary:** Business impact, root cause hypothesis, decision needed, timeline.

### Architecture Perspective

Expert scenarios test leadership under uncertainty — structured response beats heroic debugging.

### Follow-up Questions

1. **What if initial hypothesis wrong? — Time-box investigation; pivot with new evidence.**
2. **Who must sign off residual risk? — Product + ops + security as applicable.**

### Common Mistakes in Interviews

- Panic changes without rollback plan
- Technical fix without communication plan
- No follow-up ADR or runbook update after incident

---

## Q110: DBCC CHECKDB integrity Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Traffic will 10x in 6 months. What changes involving DBCC CHECKDB integrity do you prioritize in SQL Server Architecture?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing DBCC CHECKDB integrity and checkdb weekly maintenance.

### Detailed Answer

**Situation (Scale 10x):** Traffic will 10x in 6 months. What changes involving DBCC CHECKDB integrity do you prioritize in SQL Server Architecture?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around DBCC CHECKDB integrity
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of DBCC CHECKDB integrity
- Check recent changes (deploy, config, scale event)
- Reference production pattern: CHECKDB weekly maintenance

**Recommendation:**
- Short-term containment with explicit residual risk
- Medium-term fix with measurable acceptance criteria
- Long-term ADR update and guardrails (dashboards, tests, runbooks)

**Executive summary:** Business impact, root cause hypothesis, decision needed, timeline.

### Architecture Perspective

Expert scenarios test leadership under uncertainty — structured response beats heroic debugging.

### Follow-up Questions

1. **What if initial hypothesis wrong? — Time-box investigation; pivot with new evidence.**
2. **Who must sign off residual risk? — Product + ops + security as applicable.**

### Common Mistakes in Interviews

- Panic changes without rollback plan
- Technical fix without communication plan
- No follow-up ADR or runbook update after incident

---

## Q111: Index rebuild online Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

A SQL Server Architecture system experiences cascading failures. Walk through your response using concepts including Index rebuild online.

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Index rebuild online and online=on enterprise.

### Detailed Answer

**Situation (Production incident):** A SQL Server Architecture system experiences cascading failures. Walk through your response using concepts including Index rebuild online.

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Index rebuild online
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Index rebuild online
- Check recent changes (deploy, config, scale event)
- Reference production pattern: ONLINE=ON Enterprise

**Recommendation:**
- Short-term containment with explicit residual risk
- Medium-term fix with measurable acceptance criteria
- Long-term ADR update and guardrails (dashboards, tests, runbooks)

**Executive summary:** Business impact, root cause hypothesis, decision needed, timeline.

### Architecture Perspective

Expert scenarios test leadership under uncertainty — structured response beats heroic debugging.

### Follow-up Questions

1. **What if initial hypothesis wrong? — Time-box investigation; pivot with new evidence.**
2. **Who must sign off residual risk? — Product + ops + security as applicable.**

### Common Mistakes in Interviews

- Panic changes without rollback plan
- Technical fix without communication plan
- No follow-up ADR or runbook update after incident

---

## Q112: Maxdop degree parallelism Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Review a team's SQL Server Architecture design that omits Maxdop degree parallelism. What risks do you flag?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Maxdop degree parallelism and maxdop 4 oltp guidance.

### Detailed Answer

**Situation (Architecture review):** Review a team's SQL Server Architecture design that omits Maxdop degree parallelism. What risks do you flag?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Maxdop degree parallelism
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Maxdop degree parallelism
- Check recent changes (deploy, config, scale event)
- Reference production pattern: MAXDOP 4 OLTP guidance

**Recommendation:**
- Short-term containment with explicit residual risk
- Medium-term fix with measurable acceptance criteria
- Long-term ADR update and guardrails (dashboards, tests, runbooks)

**Executive summary:** Business impact, root cause hypothesis, decision needed, timeline.

### Architecture Perspective

Expert scenarios test leadership under uncertainty — structured response beats heroic debugging.

### Follow-up Questions

1. **What if initial hypothesis wrong? — Time-box investigation; pivot with new evidence.**
2. **Who must sign off residual risk? — Product + ops + security as applicable.**

### Common Mistakes in Interviews

- Panic changes without rollback plan
- Technical fix without communication plan
- No follow-up ADR or runbook update after incident

---

## Q113: Cost threshold parallelism Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Leadership wants to build in-house vs buy SaaS for SQL Server Architecture. How does Cost threshold parallelism inform your recommendation?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Cost threshold parallelism and raise cost threshold oltp.

### Detailed Answer

**Situation (Build vs buy):** Leadership wants to build in-house vs buy SaaS for SQL Server Architecture. How does Cost threshold parallelism inform your recommendation?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Cost threshold parallelism
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Cost threshold parallelism
- Check recent changes (deploy, config, scale event)
- Reference production pattern: Raise cost threshold OLTP

**Recommendation:**
- Short-term containment with explicit residual risk
- Medium-term fix with measurable acceptance criteria
- Long-term ADR update and guardrails (dashboards, tests, runbooks)

**Executive summary:** Business impact, root cause hypothesis, decision needed, timeline.

### Architecture Perspective

Expert scenarios test leadership under uncertainty — structured response beats heroic debugging.

### Follow-up Questions

1. **What if initial hypothesis wrong? — Time-box investigation; pivot with new evidence.**
2. **Who must sign off residual risk? — Product + ops + security as applicable.**

### Common Mistakes in Interviews

- Panic changes without rollback plan
- Technical fix without communication plan
- No follow-up ADR or runbook update after incident

---

## Q114: Cardinality estimator CE Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Auditors question your SQL Server Architecture architecture regarding Cardinality estimator CE. How do you respond?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Cardinality estimator CE and test with compatibility ce.

### Detailed Answer

**Situation (Regulatory audit):** Auditors question your SQL Server Architecture architecture regarding Cardinality estimator CE. How do you respond?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Cardinality estimator CE
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Cardinality estimator CE
- Check recent changes (deploy, config, scale event)
- Reference production pattern: Test with compatibility CE

**Recommendation:**
- Short-term containment with explicit residual risk
- Medium-term fix with measurable acceptance criteria
- Long-term ADR update and guardrails (dashboards, tests, runbooks)

**Executive summary:** Business impact, root cause hypothesis, decision needed, timeline.

### Architecture Perspective

Expert scenarios test leadership under uncertainty — structured response beats heroic debugging.

### Follow-up Questions

1. **What if initial hypothesis wrong? — Time-box investigation; pivot with new evidence.**
2. **Who must sign off residual risk? — Product + ops + security as applicable.**

### Common Mistakes in Interviews

- Panic changes without rollback plan
- Technical fix without communication plan
- No follow-up ADR or runbook update after incident

---

## Q115: Database compatibility level Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Traffic will 10x in 6 months. What changes involving Database compatibility level do you prioritize in SQL Server Architecture?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Database compatibility level and compat 150 test before.

### Detailed Answer

**Situation (Scale 10x):** Traffic will 10x in 6 months. What changes involving Database compatibility level do you prioritize in SQL Server Architecture?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Database compatibility level
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Database compatibility level
- Check recent changes (deploy, config, scale event)
- Reference production pattern: Compat 150 test before

**Recommendation:**
- Short-term containment with explicit residual risk
- Medium-term fix with measurable acceptance criteria
- Long-term ADR update and guardrails (dashboards, tests, runbooks)

**Executive summary:** Business impact, root cause hypothesis, decision needed, timeline.

### Architecture Perspective

Expert scenarios test leadership under uncertainty — structured response beats heroic debugging.

### Follow-up Questions

1. **What if initial hypothesis wrong? — Time-box investigation; pivot with new evidence.**
2. **Who must sign off residual risk? — Product + ops + security as applicable.**

### Common Mistakes in Interviews

- Panic changes without rollback plan
- Technical fix without communication plan
- No follow-up ADR or runbook update after incident

---

## Q116: Query hint use sparingly Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

A SQL Server Architecture system experiences cascading failures. Walk through your response using concepts including Query hint use sparingly.

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Query hint use sparingly and recompile hint targeted.

### Detailed Answer

**Situation (Production incident):** A SQL Server Architecture system experiences cascading failures. Walk through your response using concepts including Query hint use sparingly.

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Query hint use sparingly
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Query hint use sparingly
- Check recent changes (deploy, config, scale event)
- Reference production pattern: RECOMPILE hint targeted

**Recommendation:**
- Short-term containment with explicit residual risk
- Medium-term fix with measurable acceptance criteria
- Long-term ADR update and guardrails (dashboards, tests, runbooks)

**Executive summary:** Business impact, root cause hypothesis, decision needed, timeline.

### Architecture Perspective

Expert scenarios test leadership under uncertainty — structured response beats heroic debugging.

### Follow-up Questions

1. **What if initial hypothesis wrong? — Time-box investigation; pivot with new evidence.**
2. **Who must sign off residual risk? — Product + ops + security as applicable.**

### Common Mistakes in Interviews

- Panic changes without rollback plan
- Technical fix without communication plan
- No follow-up ADR or runbook update after incident

---

## Q117: Table variable cardinality Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Review a team's SQL Server Architecture design that omits Table variable cardinality. What risks do you flag?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Table variable cardinality and temp table instead tv.

### Detailed Answer

**Situation (Architecture review):** Review a team's SQL Server Architecture design that omits Table variable cardinality. What risks do you flag?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Table variable cardinality
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Table variable cardinality
- Check recent changes (deploy, config, scale event)
- Reference production pattern: Temp table instead TV

**Recommendation:**
- Short-term containment with explicit residual risk
- Medium-term fix with measurable acceptance criteria
- Long-term ADR update and guardrails (dashboards, tests, runbooks)

**Executive summary:** Business impact, root cause hypothesis, decision needed, timeline.

### Architecture Perspective

Expert scenarios test leadership under uncertainty — structured response beats heroic debugging.

### Follow-up Questions

1. **What if initial hypothesis wrong? — Time-box investigation; pivot with new evidence.**
2. **Who must sign off residual risk? — Product + ops + security as applicable.**

### Common Mistakes in Interviews

- Panic changes without rollback plan
- Technical fix without communication plan
- No follow-up ADR or runbook update after incident

---

## Q118: Temp table vs table variable Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Leadership wants to build in-house vs buy SaaS for SQL Server Architecture. How does Temp table vs table variable inform your recommendation?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Temp table vs table variable and #temp stats optimizer.

### Detailed Answer

**Situation (Build vs buy):** Leadership wants to build in-house vs buy SaaS for SQL Server Architecture. How does Temp table vs table variable inform your recommendation?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Temp table vs table variable
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Temp table vs table variable
- Check recent changes (deploy, config, scale event)
- Reference production pattern: #temp stats optimizer

**Recommendation:**
- Short-term containment with explicit residual risk
- Medium-term fix with measurable acceptance criteria
- Long-term ADR update and guardrails (dashboards, tests, runbooks)

**Executive summary:** Business impact, root cause hypothesis, decision needed, timeline.

### Architecture Perspective

Expert scenarios test leadership under uncertainty — structured response beats heroic debugging.

### Follow-up Questions

1. **What if initial hypothesis wrong? — Time-box investigation; pivot with new evidence.**
2. **Who must sign off residual risk? — Product + ops + security as applicable.**

### Common Mistakes in Interviews

- Panic changes without rollback plan
- Technical fix without communication plan
- No follow-up ADR or runbook update after incident

---

## Q119: CTE vs temp table Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Auditors question your SQL Server Architecture architecture regarding CTE vs temp table. How do you respond?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing CTE vs temp table and temp table intermediate.

### Detailed Answer

**Situation (Regulatory audit):** Auditors question your SQL Server Architecture architecture regarding CTE vs temp table. How do you respond?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around CTE vs temp table
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of CTE vs temp table
- Check recent changes (deploy, config, scale event)
- Reference production pattern: Temp table intermediate

**Recommendation:**
- Short-term containment with explicit residual risk
- Medium-term fix with measurable acceptance criteria
- Long-term ADR update and guardrails (dashboards, tests, runbooks)

**Executive summary:** Business impact, root cause hypothesis, decision needed, timeline.

### Architecture Perspective

Expert scenarios test leadership under uncertainty — structured response beats heroic debugging.

### Follow-up Questions

1. **What if initial hypothesis wrong? — Time-box investigation; pivot with new evidence.**
2. **Who must sign off residual risk? — Product + ops + security as applicable.**

### Common Mistakes in Interviews

- Panic changes without rollback plan
- Technical fix without communication plan
- No follow-up ADR or runbook update after incident

---

## Q120: Window functions performance Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Traffic will 10x in 6 months. What changes involving Window functions performance do you prioritize in SQL Server Architecture?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Window functions performance and window over self join.

### Detailed Answer

**Situation (Scale 10x):** Traffic will 10x in 6 months. What changes involving Window functions performance do you prioritize in SQL Server Architecture?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Window functions performance
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Window functions performance
- Check recent changes (deploy, config, scale event)
- Reference production pattern: Window over self join

**Recommendation:**
- Short-term containment with explicit residual risk
- Medium-term fix with measurable acceptance criteria
- Long-term ADR update and guardrails (dashboards, tests, runbooks)

**Executive summary:** Business impact, root cause hypothesis, decision needed, timeline.

### Architecture Perspective

Expert scenarios test leadership under uncertainty — structured response beats heroic debugging.

### Follow-up Questions

1. **What if initial hypothesis wrong? — Time-box investigation; pivot with new evidence.**
2. **Who must sign off residual risk? — Product + ops + security as applicable.**

### Common Mistakes in Interviews

- Panic changes without rollback plan
- Technical fix without communication plan
- No follow-up ADR or runbook update after incident

---
