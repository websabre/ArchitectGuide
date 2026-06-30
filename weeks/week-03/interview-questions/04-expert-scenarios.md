# Week 03 — Expert Scenario Q&A

> Q101–Q120: Premium format (Week 1 quality).

---


## Q101: Transactional email side effect Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

A SOLID & Clean Architecture system experiences cascading failures. Walk through your response using concepts including Transactional email side effect.

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Transactional email side effect and domain event after uow commit.

### Detailed Answer

**Situation (Production incident):** A SOLID & Clean Architecture system experiences cascading failures. Walk through your response using concepts including Transactional email side effect.

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Transactional email side effect
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Transactional email side effect
- Check recent changes (deploy, config, scale event)
- Reference production pattern: Domain event after UoW commit

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

## Q102: Saga local vs distributed Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Review a team's SOLID & Clean Architecture design that omits Saga local vs distributed. What risks do you flag?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Saga local vs distributed and orchestrated saga with compensations.

### Detailed Answer

**Situation (Architecture review):** Review a team's SOLID & Clean Architecture design that omits Saga local vs distributed. What risks do you flag?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Saga local vs distributed
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Saga local vs distributed
- Check recent changes (deploy, config, scale event)
- Reference production pattern: Orchestrated saga with compensations

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

## Q103: Compensating transactions Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Leadership wants to build in-house vs buy SaaS for SOLID & Clean Architecture. How does Compensating transactions inform your recommendation?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Compensating transactions and releaseinventory on payment failure.

### Detailed Answer

**Situation (Build vs buy):** Leadership wants to build in-house vs buy SaaS for SOLID & Clean Architecture. How does Compensating transactions inform your recommendation?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Compensating transactions
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Compensating transactions
- Check recent changes (deploy, config, scale event)
- Reference production pattern: ReleaseInventory on payment failure

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

## Q104: Eventual consistency UX Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Auditors question your SOLID & Clean Architecture architecture regarding Eventual consistency UX. How do you respond?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Eventual consistency UX and pending state polling webhook.

### Detailed Answer

**Situation (Regulatory audit):** Auditors question your SOLID & Clean Architecture architecture regarding Eventual consistency UX. How do you respond?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Eventual consistency UX
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Eventual consistency UX
- Check recent changes (deploy, config, scale event)
- Reference production pattern: Pending state polling webhook

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

## Q105: Read side denormalization Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Traffic will 10x in 6 months. What changes involving Read side denormalization do you prioritize in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Read side denormalization and ordersummary table updated by events.

### Detailed Answer

**Situation (Scale 10x):** Traffic will 10x in 6 months. What changes involving Read side denormalization do you prioritize in SOLID & Clean Architecture?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Read side denormalization
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Read side denormalization
- Check recent changes (deploy, config, scale event)
- Reference production pattern: OrderSummary table updated by events

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

## Q106: Schema per bounded context Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

A SOLID & Clean Architecture system experiences cascading failures. Walk through your response using concepts including Schema per bounded context.

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Schema per bounded context and orders db vs catalog db.

### Detailed Answer

**Situation (Production incident):** A SOLID & Clean Architecture system experiences cascading failures. Walk through your response using concepts including Schema per bounded context.

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Schema per bounded context
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Schema per bounded context
- Check recent changes (deploy, config, scale event)
- Reference production pattern: Orders DB vs Catalog DB

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

## Q107: Database per service pragmatic Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Review a team's SOLID & Clean Architecture design that omits Database per service pragmatic. What risks do you flag?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Database per service pragmatic and schema separation first step.

### Detailed Answer

**Situation (Architecture review):** Review a team's SOLID & Clean Architecture design that omits Database per service pragmatic. What risks do you flag?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Database per service pragmatic
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Database per service pragmatic
- Check recent changes (deploy, config, scale event)
- Reference production pattern: Schema separation first step

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

## Q108: API composition vs aggregation Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Leadership wants to build in-house vs buy SaaS for SOLID & Clean Architecture. How does API composition vs aggregation inform your recommendation?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing API composition vs aggregation and bff aggregates order view.

### Detailed Answer

**Situation (Build vs buy):** Leadership wants to build in-house vs buy SaaS for SOLID & Clean Architecture. How does API composition vs aggregation inform your recommendation?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around API composition vs aggregation
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of API composition vs aggregation
- Check recent changes (deploy, config, scale event)
- Reference production pattern: BFF aggregates order view

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

## Q109: Gateway vs direct service Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Auditors question your SOLID & Clean Architecture architecture regarding Gateway vs direct service. How do you respond?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Gateway vs direct service and apim policies auth rate limit.

### Detailed Answer

**Situation (Regulatory audit):** Auditors question your SOLID & Clean Architecture architecture regarding Gateway vs direct service. How do you respond?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Gateway vs direct service
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Gateway vs direct service
- Check recent changes (deploy, config, scale event)
- Reference production pattern: APIM policies auth rate limit

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

## Q110: Versioning bounded context APIs Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Traffic will 10x in 6 months. What changes involving Versioning bounded context APIs do you prioritize in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Versioning bounded context APIs and url version per context.

### Detailed Answer

**Situation (Scale 10x):** Traffic will 10x in 6 months. What changes involving Versioning bounded context APIs do you prioritize in SOLID & Clean Architecture?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Versioning bounded context APIs
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Versioning bounded context APIs
- Check recent changes (deploy, config, scale event)
- Reference production pattern: URL version per context

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

## Q111: Contract testing between contexts Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

A SOLID & Clean Architecture system experiences cascading failures. Walk through your response using concepts including Contract testing between contexts.

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Contract testing between contexts and pact between order and payment.

### Detailed Answer

**Situation (Production incident):** A SOLID & Clean Architecture system experiences cascading failures. Walk through your response using concepts including Contract testing between contexts.

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Contract testing between contexts
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Contract testing between contexts
- Check recent changes (deploy, config, scale event)
- Reference production pattern: Pact between Order and Payment

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

## Q112: Architecture fitness functions Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Review a team's SOLID & Clean Architecture design that omits Architecture fitness functions. What risks do you flag?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Architecture fitness functions and netarchtest domain no infra refs.

### Detailed Answer

**Situation (Architecture review):** Review a team's SOLID & Clean Architecture design that omits Architecture fitness functions. What risks do you flag?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Architecture fitness functions
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Architecture fitness functions
- Check recent changes (deploy, config, scale event)
- Reference production pattern: NetArchTest domain no infra refs

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

## Q113: ArchUnitNET layer rules Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Leadership wants to build in-house vs buy SaaS for SOLID & Clean Architecture. How does ArchUnitNET layer rules inform your recommendation?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing ArchUnitNET layer rules and ci fails on layer violation.

### Detailed Answer

**Situation (Build vs buy):** Leadership wants to build in-house vs buy SaaS for SOLID & Clean Architecture. How does ArchUnitNET layer rules inform your recommendation?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around ArchUnitNET layer rules
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of ArchUnitNET layer rules
- Check recent changes (deploy, config, scale event)
- Reference production pattern: CI fails on layer violation

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

## Q114: Package by feature Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Auditors question your SOLID & Clean Architecture architecture regarding Package by feature. How do you respond?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Package by feature and orders feature folder all layers.

### Detailed Answer

**Situation (Regulatory audit):** Auditors question your SOLID & Clean Architecture architecture regarding Package by feature. How do you respond?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Package by feature
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Package by feature
- Check recent changes (deploy, config, scale event)
- Reference production pattern: Orders feature folder all layers

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

## Q115: Screaming architecture Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Traffic will 10x in 6 months. What changes involving Screaming architecture do you prioritize in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Screaming architecture and orders not infrastructure top.

### Detailed Answer

**Situation (Scale 10x):** Traffic will 10x in 6 months. What changes involving Screaming architecture do you prioritize in SOLID & Clean Architecture?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Screaming architecture
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Screaming architecture
- Check recent changes (deploy, config, scale event)
- Reference production pattern: Orders not Infrastructure top

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

## Q116: When skip clean architecture Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

A SOLID & Clean Architecture system experiences cascading failures. Walk through your response using concepts including When skip clean architecture.

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing When skip clean architecture and pragmatic 3-layer internal tool.

### Detailed Answer

**Situation (Production incident):** A SOLID & Clean Architecture system experiences cascading failures. Walk through your response using concepts including When skip clean architecture.

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around When skip clean architecture
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of When skip clean architecture
- Check recent changes (deploy, config, scale event)
- Reference production pattern: Pragmatic 3-layer internal tool

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

## Q117: Clean architecture testing pyramid Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Review a team's SOLID & Clean Architecture design that omits Clean architecture testing pyramid. What risks do you flag?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Clean architecture testing pyramid and domain unit no db majority.

### Detailed Answer

**Situation (Architecture review):** Review a team's SOLID & Clean Architecture design that omits Clean architecture testing pyramid. What risks do you flag?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Clean architecture testing pyramid
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Clean architecture testing pyramid
- Check recent changes (deploy, config, scale event)
- Reference production pattern: Domain unit no DB majority

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

## Q118: Test doubles for ports Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Leadership wants to build in-house vs buy SaaS for SOLID & Clean Architecture. How does Test doubles for ports inform your recommendation?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Test doubles for ports and fake iemailport in handler test.

### Detailed Answer

**Situation (Build vs buy):** Leadership wants to build in-house vs buy SaaS for SOLID & Clean Architecture. How does Test doubles for ports inform your recommendation?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Test doubles for ports
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Test doubles for ports
- Check recent changes (deploy, config, scale event)
- Reference production pattern: Fake IEmailPort in handler test

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

## Q119: Integration test boundaries Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Auditors question your SOLID & Clean Architecture architecture regarding Integration test boundaries. How do you respond?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Integration test boundaries and testcontainers for repo adapter.

### Detailed Answer

**Situation (Regulatory audit):** Auditors question your SOLID & Clean Architecture architecture regarding Integration test boundaries. How do you respond?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Integration test boundaries
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Integration test boundaries
- Check recent changes (deploy, config, scale event)
- Reference production pattern: Testcontainers for repo adapter

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

## Q120: Seed data for integration Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Traffic will 10x in 6 months. What changes involving Seed data for integration do you prioritize in SOLID & Clean Architecture?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Seed data for integration and respawn reset between tests.

### Detailed Answer

**Situation (Scale 10x):** Traffic will 10x in 6 months. What changes involving Seed data for integration do you prioritize in SOLID & Clean Architecture?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Seed data for integration
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Seed data for integration
- Check recent changes (deploy, config, scale event)
- Reference production pattern: Respawn reset between tests

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
