# Week 02 — Expert Scenario Q&A

> Q101–Q120: Premium format (Week 1 quality).

---


## Q101: Hybrid cache .NET 9 Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

A .NET Runtime & Ecosystem system experiences cascading failures. Walk through your response using concepts including Hybrid cache .NET 9.

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Hybrid cache .NET 9 and hybridcache automatic l1 memory l2 redis.

### Detailed Answer

**Situation (Production incident):** A .NET Runtime & Ecosystem system experiences cascading failures. Walk through your response using concepts including Hybrid cache .NET 9.

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Hybrid cache .NET 9
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Hybrid cache .NET 9
- Check recent changes (deploy, config, scale event)
- Reference production pattern: HybridCache automatic L1 memory L2 Redis

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

## Q102: Rate limit partition keys Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Review a team's .NET Runtime & Ecosystem design that omits Rate limit partition keys. What risks do you flag?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Rate limit partition keys and partitionedratelimiter by tenantid.

### Detailed Answer

**Situation (Architecture review):** Review a team's .NET Runtime & Ecosystem design that omits Rate limit partition keys. What risks do you flag?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Rate limit partition keys
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Rate limit partition keys
- Check recent changes (deploy, config, scale event)
- Reference production pattern: PartitionedRateLimiter by tenantId

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

## Q103: Output cache policies Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Leadership wants to build in-house vs buy SaaS for .NET Runtime & Ecosystem. How does Output cache policies inform your recommendation?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Output cache policies and varybyquery policy on catalog.

### Detailed Answer

**Situation (Build vs buy):** Leadership wants to build in-house vs buy SaaS for .NET Runtime & Ecosystem. How does Output cache policies inform your recommendation?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Output cache policies
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Output cache policies
- Check recent changes (deploy, config, scale event)
- Reference production pattern: VaryByQuery policy on catalog

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

## Q104: IdentityServer vs Entra Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Auditors question your .NET Runtime & Ecosystem architecture regarding IdentityServer vs Entra. How do you respond?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing IdentityServer vs Entra and entra id for workforce customers.

### Detailed Answer

**Situation (Regulatory audit):** Auditors question your .NET Runtime & Ecosystem architecture regarding IdentityServer vs Entra. How do you respond?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around IdentityServer vs Entra
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of IdentityServer vs Entra
- Check recent changes (deploy, config, scale event)
- Reference production pattern: Entra ID for workforce customers

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

## Q105: Data annotations vs FluentValidation Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Traffic will 10x in 6 months. What changes involving Data annotations vs FluentValidation do you prioritize in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Data annotations vs FluentValidation and one validation layer per boundary.

### Detailed Answer

**Situation (Scale 10x):** Traffic will 10x in 6 months. What changes involving Data annotations vs FluentValidation do you prioritize in .NET Runtime & Ecosystem?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Data annotations vs FluentValidation
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Data annotations vs FluentValidation
- Check recent changes (deploy, config, scale event)
- Reference production pattern: One validation layer per boundary

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

## Q106: Swagger security definitions Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

A .NET Runtime & Ecosystem system experiences cascading failures. Walk through your response using concepts including Swagger security definitions.

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Swagger security definitions and oauth2 security scheme in swagger.

### Detailed Answer

**Situation (Production incident):** A .NET Runtime & Ecosystem system experiences cascading failures. Walk through your response using concepts including Swagger security definitions.

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Swagger security definitions
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Swagger security definitions
- Check recent changes (deploy, config, scale event)
- Reference production pattern: OAuth2 security scheme in swagger

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

## Q107: Grpc health checks Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Review a team's .NET Runtime & Ecosystem design that omits Grpc health checks. What risks do you flag?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Grpc health checks and mapgrpchealthchecksservice.

### Detailed Answer

**Situation (Architecture review):** Review a team's .NET Runtime & Ecosystem design that omits Grpc health checks. What risks do you flag?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Grpc health checks
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Grpc health checks
- Check recent changes (deploy, config, scale event)
- Reference production pattern: MapGrpcHealthChecksService

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

## Q108: Wolverine messaging handler Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Leadership wants to build in-house vs buy SaaS for .NET Runtime & Ecosystem. How does Wolverine messaging handler inform your recommendation?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Wolverine messaging handler and wolverine for local + external.

### Detailed Answer

**Situation (Build vs buy):** Leadership wants to build in-house vs buy SaaS for .NET Runtime & Ecosystem. How does Wolverine messaging handler inform your recommendation?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Wolverine messaging handler
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Wolverine messaging handler
- Check recent changes (deploy, config, scale event)
- Reference production pattern: Wolverine for local + external

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

## Q109: Orleans virtual actors Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Auditors question your .NET Runtime & Ecosystem architecture regarding Orleans virtual actors. How do you respond?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Orleans virtual actors and orleans for session/game state.

### Detailed Answer

**Situation (Regulatory audit):** Auditors question your .NET Runtime & Ecosystem architecture regarding Orleans virtual actors. How do you respond?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Orleans virtual actors
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Orleans virtual actors
- Check recent changes (deploy, config, scale event)
- Reference production pattern: Orleans for session/game state

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

## Q110: Dapr sidecar .NET Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Traffic will 10x in 6 months. What changes involving Dapr sidecar .NET do you prioritize in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Dapr sidecar .NET and dapr pub/sub from .net service.

### Detailed Answer

**Situation (Scale 10x):** Traffic will 10x in 6 months. What changes involving Dapr sidecar .NET do you prioritize in .NET Runtime & Ecosystem?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Dapr sidecar .NET
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Dapr sidecar .NET
- Check recent changes (deploy, config, scale event)
- Reference production pattern: Dapr pub/sub from .NET service

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

## Q111: FusionCache Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

A .NET Runtime & Ecosystem system experiences cascading failures. Walk through your response using concepts including FusionCache.

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing FusionCache and fusioncache with fail-safe.

### Detailed Answer

**Situation (Production incident):** A .NET Runtime & Ecosystem system experiences cascading failures. Walk through your response using concepts including FusionCache.

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around FusionCache
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of FusionCache
- Check recent changes (deploy, config, scale event)
- Reference production pattern: FusionCache with fail-safe

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

## Q112: AWS SDK vs Azure SDK DI Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Review a team's .NET Runtime & Ecosystem design that omits AWS SDK vs Azure SDK DI. What risks do you flag?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing AWS SDK vs Azure SDK DI and iamazons3 injected singleton.

### Detailed Answer

**Situation (Architecture review):** Review a team's .NET Runtime & Ecosystem design that omits AWS SDK vs Azure SDK DI. What risks do you flag?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around AWS SDK vs Azure SDK DI
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of AWS SDK vs Azure SDK DI
- Check recent changes (deploy, config, scale event)
- Reference production pattern: IAmazonS3 injected singleton

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

## Q113: Azure App Configuration refresh Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Leadership wants to build in-house vs buy SaaS for .NET Runtime & Ecosystem. How does Azure App Configuration refresh inform your recommendation?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Azure App Configuration refresh and configurerefresh sentinel key.

### Detailed Answer

**Situation (Build vs buy):** Leadership wants to build in-house vs buy SaaS for .NET Runtime & Ecosystem. How does Azure App Configuration refresh inform your recommendation?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Azure App Configuration refresh
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Azure App Configuration refresh
- Check recent changes (deploy, config, scale event)
- Reference production pattern: ConfigureRefresh sentinel key

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

## Q114: Feature management Microsoft Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Auditors question your .NET Runtime & Ecosystem architecture regarding Feature management Microsoft. How do you respond?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Feature management Microsoft and ifeaturemanager percentage filter.

### Detailed Answer

**Situation (Regulatory audit):** Auditors question your .NET Runtime & Ecosystem architecture regarding Feature management Microsoft. How do you respond?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Feature management Microsoft
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Feature management Microsoft
- Check recent changes (deploy, config, scale event)
- Reference production pattern: IFeatureManager percentage filter

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

## Q115: Application Insights adaptive sampling Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Traffic will 10x in 6 months. What changes involving Application Insights adaptive sampling do you prioritize in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Application Insights adaptive sampling and adaptive sampling production.

### Detailed Answer

**Situation (Scale 10x):** Traffic will 10x in 6 months. What changes involving Application Insights adaptive sampling do you prioritize in .NET Runtime & Ecosystem?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Application Insights adaptive sampling
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Application Insights adaptive sampling
- Check recent changes (deploy, config, scale event)
- Reference production pattern: Adaptive sampling production

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

## Q116: OpenTelemetry resource attributes Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

A .NET Runtime & Ecosystem system experiences cascading failures. Walk through your response using concepts including OpenTelemetry resource attributes.

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing OpenTelemetry resource attributes and otel_resource_attributes deployment.

### Detailed Answer

**Situation (Production incident):** A .NET Runtime & Ecosystem system experiences cascading failures. Walk through your response using concepts including OpenTelemetry resource attributes.

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around OpenTelemetry resource attributes
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of OpenTelemetry resource attributes
- Check recent changes (deploy, config, scale event)
- Reference production pattern: OTEL_RESOURCE_ATTRIBUTES deployment

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

## Q117: Custom middleware vs filters Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Review a team's .NET Runtime & Ecosystem design that omits Custom middleware vs filters. What risks do you flag?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Custom middleware vs filters and middleware auth filters validation.

### Detailed Answer

**Situation (Architecture review):** Review a team's .NET Runtime & Ecosystem design that omits Custom middleware vs filters. What risks do you flag?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Custom middleware vs filters
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Custom middleware vs filters
- Check recent changes (deploy, config, scale event)
- Reference production pattern: Middleware auth filters validation

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

## Q118: IExceptionHandler .NET 8 Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Leadership wants to build in-house vs buy SaaS for .NET Runtime & Ecosystem. How does IExceptionHandler .NET 8 inform your recommendation?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing IExceptionHandler .NET 8 and iexceptionhandler pipeline.

### Detailed Answer

**Situation (Build vs buy):** Leadership wants to build in-house vs buy SaaS for .NET Runtime & Ecosystem. How does IExceptionHandler .NET 8 inform your recommendation?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around IExceptionHandler .NET 8
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of IExceptionHandler .NET 8
- Check recent changes (deploy, config, scale event)
- Reference production pattern: IExceptionHandler pipeline

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

## Q119: Results pattern minimal APIs Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

Auditors question your .NET Runtime & Ecosystem architecture regarding Results pattern minimal APIs. How do you respond?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing Results pattern minimal APIs and results<ok<orderdto>, notfound>.

### Detailed Answer

**Situation (Regulatory audit):** Auditors question your .NET Runtime & Ecosystem architecture regarding Results pattern minimal APIs. How do you respond?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around Results pattern minimal APIs
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of Results pattern minimal APIs
- Check recent changes (deploy, config, scale event)
- Reference production pattern: Results<Ok<OrderDto>, NotFound>

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

## Q120: ValidationProblemDetails Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scenario |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

Traffic will 10x in 6 months. What changes involving ValidationProblemDetails do you prioritize in .NET Runtime & Ecosystem?

### Short Answer (30 seconds)

Lead with stabilization, evidence gathering, and a phased plan referencing ValidationProblemDetails and validationproblem() standard.

### Detailed Answer

**Situation (Scale 10x):** Traffic will 10x in 6 months. What changes involving ValidationProblemDetails do you prioritize in .NET Runtime & Ecosystem?

**Immediate (0–48h):**
- Stabilize customer impact; communicate status
- Capture metrics/logs around ValidationProblemDetails
- Form cross-functional war room if revenue-impacting

**Diagnosis:**
- Compare expected vs actual behavior of ValidationProblemDetails
- Check recent changes (deploy, config, scale event)
- Reference production pattern: ValidationProblem() standard

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
