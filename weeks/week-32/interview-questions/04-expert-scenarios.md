# Week 32 — Expert Scenario Q&A

> Q101–Q120: Premium format (Week 1 quality).

---


## Q101: Observability Blind During Outage

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Observability |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when no traces for failing service?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** No traces for failing service — instrumentation sprint in 30 days.

**Immediate (Days 1–7):**
- Form tiger team with platform + stream DRI
- Stabilize customer impact; exec comms every 24h
- Preserve evidence: deploy logs, traces, config snapshots

**30-day plan:**
| Week | Focus | Deliverable |
|------|-------|-------------|
| 1 | Triage + postmortem | Blameless doc, action owners |
| 2 | Baseline metrics | DORA/SLO dashboard before state |
| 3 | Pilot fix one squad | Measured improvement vs control |
| 4 | Runbook + training | Documented standard for observability |

**90-day plan:**
- **Days 31–60:** Roll out pattern to all affected teams; platform self-service to remove bottlenecks
- **Days 61–90:** Policy/gates in CI; game day validation; steering review with trend charts

**Success metrics:** Lead time, MTTR, CFR, or adoption % — targets set from baseline, not arbitrary.

**Stakeholder map:** VP Engineering sponsor, affected product director, platform lead.

**Azure/.NET example:** Instrument fix in Application Insights; tag deployments to correlate with change failure rate improvement.

**Architect:** Residual risk documented with expiry review date — not 'monitor' alone.

### Architecture Perspective

Expert scenarios test program leadership — structured plans beat ad-hoc heroics.

### Follow-up Questions

1. **CEO demands skip pilot? — Risk matrix with phased alternative; written acceptance if override.**
2. **Prove success? — Before/after dashboard on DORA or SLO — not team sentiment alone.**

### Common Mistakes in Interviews

- Jump to permanent tooling before stabilizing the incident
- Single 90-day big-bang without 30-day quick wins
- No measurable success criteria or executive sponsor

---

## Q102: Cardinality Explosion Bill

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Observability |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when log analytics cost 5× budget?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Log Analytics cost 5× budget — cardinality and sampling fix in 60 days.

**Immediate (Days 1–7):**
- Form tiger team with platform + stream DRI
- Stabilize customer impact; exec comms every 24h
- Preserve evidence: deploy logs, traces, config snapshots

**30-day plan:**
| Week | Focus | Deliverable |
|------|-------|-------------|
| 1 | Triage + postmortem | Blameless doc, action owners |
| 2 | Baseline metrics | DORA/SLO dashboard before state |
| 3 | Pilot fix one squad | Measured improvement vs control |
| 4 | Runbook + training | Documented standard for observability |

**90-day plan:**
- **Days 31–60:** Roll out pattern to all affected teams; platform self-service to remove bottlenecks
- **Days 61–90:** Policy/gates in CI; game day validation; steering review with trend charts

**Success metrics:** Lead time, MTTR, CFR, or adoption % — targets set from baseline, not arbitrary.

**Stakeholder map:** VP Engineering sponsor, affected product director, platform lead.

**Azure/.NET example:** Instrument fix in Application Insights; tag deployments to correlate with change failure rate improvement.

**Architect:** Residual risk documented with expiry review date — not 'monitor' alone.

### Architecture Perspective

Expert scenarios test program leadership — structured plans beat ad-hoc heroics.

### Follow-up Questions

1. **CEO demands skip pilot? — Risk matrix with phased alternative; written acceptance if override.**
2. **Prove success? — Before/after dashboard on DORA or SLO — not team sentiment alone.**

### Common Mistakes in Interviews

- Jump to permanent tooling before stabilizing the incident
- Single 90-day big-bang without 30-day quick wins
- No measurable success criteria or executive sponsor

---

## Q103: Alert Fatigue Engineers Ignore

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Observability |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when 200 alerts/day?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** 200 alerts/day — SLO-based alerting redesign in 30 days.

**Immediate (Days 1–7):**
- Form tiger team with platform + stream DRI
- Stabilize customer impact; exec comms every 24h
- Preserve evidence: deploy logs, traces, config snapshots

**30-day plan:**
| Week | Focus | Deliverable |
|------|-------|-------------|
| 1 | Triage + postmortem | Blameless doc, action owners |
| 2 | Baseline metrics | DORA/SLO dashboard before state |
| 3 | Pilot fix one squad | Measured improvement vs control |
| 4 | Runbook + training | Documented standard for observability |

**90-day plan:**
- **Days 31–60:** Roll out pattern to all affected teams; platform self-service to remove bottlenecks
- **Days 61–90:** Policy/gates in CI; game day validation; steering review with trend charts

**Success metrics:** Lead time, MTTR, CFR, or adoption % — targets set from baseline, not arbitrary.

**Stakeholder map:** VP Engineering sponsor, affected product director, platform lead.

**Azure/.NET example:** Instrument fix in Application Insights; tag deployments to correlate with change failure rate improvement.

**Architect:** Residual risk documented with expiry review date — not 'monitor' alone.

### Architecture Perspective

Expert scenarios test program leadership — structured plans beat ad-hoc heroics.

### Follow-up Questions

1. **CEO demands skip pilot? — Risk matrix with phased alternative; written acceptance if override.**
2. **Prove success? — Before/after dashboard on DORA or SLO — not team sentiment alone.**

### Common Mistakes in Interviews

- Jump to permanent tooling before stabilizing the incident
- Single 90-day big-bang without 30-day quick wins
- No measurable success criteria or executive sponsor

---

## Q104: Missing Trace Across Services

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Observability |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when broken propagation?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Broken propagation — W3C header standardization in 30 days.

**Immediate (Days 1–7):**
- Form tiger team with platform + stream DRI
- Stabilize customer impact; exec comms every 24h
- Preserve evidence: deploy logs, traces, config snapshots

**30-day plan:**
| Week | Focus | Deliverable |
|------|-------|-------------|
| 1 | Triage + postmortem | Blameless doc, action owners |
| 2 | Baseline metrics | DORA/SLO dashboard before state |
| 3 | Pilot fix one squad | Measured improvement vs control |
| 4 | Runbook + training | Documented standard for observability |

**90-day plan:**
- **Days 31–60:** Roll out pattern to all affected teams; platform self-service to remove bottlenecks
- **Days 61–90:** Policy/gates in CI; game day validation; steering review with trend charts

**Success metrics:** Lead time, MTTR, CFR, or adoption % — targets set from baseline, not arbitrary.

**Stakeholder map:** VP Engineering sponsor, affected product director, platform lead.

**Azure/.NET example:** Instrument fix in Application Insights; tag deployments to correlate with change failure rate improvement.

**Architect:** Residual risk documented with expiry review date — not 'monitor' alone.

### Architecture Perspective

Expert scenarios test program leadership — structured plans beat ad-hoc heroics.

### Follow-up Questions

1. **CEO demands skip pilot? — Risk matrix with phased alternative; written acceptance if override.**
2. **Prove success? — Before/after dashboard on DORA or SLO — not team sentiment alone.**

### Common Mistakes in Interviews

- Jump to permanent tooling before stabilizing the incident
- Single 90-day big-bang without 30-day quick wins
- No measurable success criteria or executive sponsor

---

## Q105: SLO Not Measurable

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Observability |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when no sli data?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** No SLI data — instrumentation and SLO definition in 60 days.

**Immediate (Days 1–7):**
- Form tiger team with platform + stream DRI
- Stabilize customer impact; exec comms every 24h
- Preserve evidence: deploy logs, traces, config snapshots

**30-day plan:**
| Week | Focus | Deliverable |
|------|-------|-------------|
| 1 | Triage + postmortem | Blameless doc, action owners |
| 2 | Baseline metrics | DORA/SLO dashboard before state |
| 3 | Pilot fix one squad | Measured improvement vs control |
| 4 | Runbook + training | Documented standard for observability |

**90-day plan:**
- **Days 31–60:** Roll out pattern to all affected teams; platform self-service to remove bottlenecks
- **Days 61–90:** Policy/gates in CI; game day validation; steering review with trend charts

**Success metrics:** Lead time, MTTR, CFR, or adoption % — targets set from baseline, not arbitrary.

**Stakeholder map:** VP Engineering sponsor, affected product director, platform lead.

**Azure/.NET example:** Instrument fix in Application Insights; tag deployments to correlate with change failure rate improvement.

**Architect:** Residual risk documented with expiry review date — not 'monitor' alone.

### Architecture Perspective

Expert scenarios test program leadership — structured plans beat ad-hoc heroics.

### Follow-up Questions

1. **CEO demands skip pilot? — Risk matrix with phased alternative; written acceptance if override.**
2. **Prove success? — Before/after dashboard on DORA or SLO — not team sentiment alone.**

### Common Mistakes in Interviews

- Jump to permanent tooling before stabilizing the incident
- Single 90-day big-bang without 30-day quick wins
- No measurable success criteria or executive sponsor

---

## Q106: Dashboard Vanity Metrics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Observability |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when cpu graphs but no user impact?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** CPU graphs but no user impact — RED/USE dashboard program in 30 days.

**Immediate (Days 1–7):**
- Form tiger team with platform + stream DRI
- Stabilize customer impact; exec comms every 24h
- Preserve evidence: deploy logs, traces, config snapshots

**30-day plan:**
| Week | Focus | Deliverable |
|------|-------|-------------|
| 1 | Triage + postmortem | Blameless doc, action owners |
| 2 | Baseline metrics | DORA/SLO dashboard before state |
| 3 | Pilot fix one squad | Measured improvement vs control |
| 4 | Runbook + training | Documented standard for observability |

**90-day plan:**
- **Days 31–60:** Roll out pattern to all affected teams; platform self-service to remove bottlenecks
- **Days 61–90:** Policy/gates in CI; game day validation; steering review with trend charts

**Success metrics:** Lead time, MTTR, CFR, or adoption % — targets set from baseline, not arbitrary.

**Stakeholder map:** VP Engineering sponsor, affected product director, platform lead.

**Azure/.NET example:** Instrument fix in Application Insights; tag deployments to correlate with change failure rate improvement.

**Architect:** Residual risk documented with expiry review date — not 'monitor' alone.

### Architecture Perspective

Expert scenarios test program leadership — structured plans beat ad-hoc heroics.

### Follow-up Questions

1. **CEO demands skip pilot? — Risk matrix with phased alternative; written acceptance if override.**
2. **Prove success? — Before/after dashboard on DORA or SLO — not team sentiment alone.**

### Common Mistakes in Interviews

- Jump to permanent tooling before stabilizing the incident
- Single 90-day big-bang without 30-day quick wins
- No measurable success criteria or executive sponsor

---

## Q107: Sampling Hides Production Bug

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Observability |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when bug only in unsampled requests?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Bug only in unsampled requests — tail sampling in 60 days.

**Immediate (Days 1–7):**
- Form tiger team with platform + stream DRI
- Stabilize customer impact; exec comms every 24h
- Preserve evidence: deploy logs, traces, config snapshots

**30-day plan:**
| Week | Focus | Deliverable |
|------|-------|-------------|
| 1 | Triage + postmortem | Blameless doc, action owners |
| 2 | Baseline metrics | DORA/SLO dashboard before state |
| 3 | Pilot fix one squad | Measured improvement vs control |
| 4 | Runbook + training | Documented standard for observability |

**90-day plan:**
- **Days 31–60:** Roll out pattern to all affected teams; platform self-service to remove bottlenecks
- **Days 61–90:** Policy/gates in CI; game day validation; steering review with trend charts

**Success metrics:** Lead time, MTTR, CFR, or adoption % — targets set from baseline, not arbitrary.

**Stakeholder map:** VP Engineering sponsor, affected product director, platform lead.

**Azure/.NET example:** Instrument fix in Application Insights; tag deployments to correlate with change failure rate improvement.

**Architect:** Residual risk documented with expiry review date — not 'monitor' alone.

### Architecture Perspective

Expert scenarios test program leadership — structured plans beat ad-hoc heroics.

### Follow-up Questions

1. **CEO demands skip pilot? — Risk matrix with phased alternative; written acceptance if override.**
2. **Prove success? — Before/after dashboard on DORA or SLO — not team sentiment alone.**

### Common Mistakes in Interviews

- Jump to permanent tooling before stabilizing the incident
- Single 90-day big-bang without 30-day quick wins
- No measurable success criteria or executive sponsor

---

## Q108: PII in Logs Audit Failure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Observability |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when gdpr breach risk from logs?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** GDPR breach risk from logs — redaction and scan in 14 days.

**Immediate (Days 1–7):**
- Form tiger team with platform + stream DRI
- Stabilize customer impact; exec comms every 24h
- Preserve evidence: deploy logs, traces, config snapshots

**30-day plan:**
| Week | Focus | Deliverable |
|------|-------|-------------|
| 1 | Triage + postmortem | Blameless doc, action owners |
| 2 | Baseline metrics | DORA/SLO dashboard before state |
| 3 | Pilot fix one squad | Measured improvement vs control |
| 4 | Runbook + training | Documented standard for observability |

**90-day plan:**
- **Days 31–60:** Roll out pattern to all affected teams; platform self-service to remove bottlenecks
- **Days 61–90:** Policy/gates in CI; game day validation; steering review with trend charts

**Success metrics:** Lead time, MTTR, CFR, or adoption % — targets set from baseline, not arbitrary.

**Stakeholder map:** VP Engineering sponsor, affected product director, platform lead.

**Azure/.NET example:** Instrument fix in Application Insights; tag deployments to correlate with change failure rate improvement.

**Architect:** Residual risk documented with expiry review date — not 'monitor' alone.

### Architecture Perspective

Expert scenarios test program leadership — structured plans beat ad-hoc heroics.

### Follow-up Questions

1. **CEO demands skip pilot? — Risk matrix with phased alternative; written acceptance if override.**
2. **Prove success? — Before/after dashboard on DORA or SLO — not team sentiment alone.**

### Common Mistakes in Interviews

- Jump to permanent tooling before stabilizing the incident
- Single 90-day big-bang without 30-day quick wins
- No measurable success criteria or executive sponsor

---

## Q109: Post-Deploy No Visibility

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Observability |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when deploy succeeded but errors spike undetected?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Deploy succeeded but errors spike undetected — deploy markers and alerts in 30 days.

**Immediate (Days 1–7):**
- Form tiger team with platform + stream DRI
- Stabilize customer impact; exec comms every 24h
- Preserve evidence: deploy logs, traces, config snapshots

**30-day plan:**
| Week | Focus | Deliverable |
|------|-------|-------------|
| 1 | Triage + postmortem | Blameless doc, action owners |
| 2 | Baseline metrics | DORA/SLO dashboard before state |
| 3 | Pilot fix one squad | Measured improvement vs control |
| 4 | Runbook + training | Documented standard for observability |

**90-day plan:**
- **Days 31–60:** Roll out pattern to all affected teams; platform self-service to remove bottlenecks
- **Days 61–90:** Policy/gates in CI; game day validation; steering review with trend charts

**Success metrics:** Lead time, MTTR, CFR, or adoption % — targets set from baseline, not arbitrary.

**Stakeholder map:** VP Engineering sponsor, affected product director, platform lead.

**Azure/.NET example:** Instrument fix in Application Insights; tag deployments to correlate with change failure rate improvement.

**Architect:** Residual risk documented with expiry review date — not 'monitor' alone.

### Architecture Perspective

Expert scenarios test program leadership — structured plans beat ad-hoc heroics.

### Follow-up Questions

1. **CEO demands skip pilot? — Risk matrix with phased alternative; written acceptance if override.**
2. **Prove success? — Before/after dashboard on DORA or SLO — not team sentiment alone.**

### Common Mistakes in Interviews

- Jump to permanent tooling before stabilizing the incident
- Single 90-day big-bang without 30-day quick wins
- No measurable success criteria or executive sponsor

---

## Q110: Multi-Region Trace Fragmentation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Observability |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when traces split across regions?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Traces split across regions — collector architecture in 90 days.

**Immediate (Days 1–7):**
- Form tiger team with platform + stream DRI
- Stabilize customer impact; exec comms every 24h
- Preserve evidence: deploy logs, traces, config snapshots

**30-day plan:**
| Week | Focus | Deliverable |
|------|-------|-------------|
| 1 | Triage + postmortem | Blameless doc, action owners |
| 2 | Baseline metrics | DORA/SLO dashboard before state |
| 3 | Pilot fix one squad | Measured improvement vs control |
| 4 | Runbook + training | Documented standard for observability |

**90-day plan:**
- **Days 31–60:** Roll out pattern to all affected teams; platform self-service to remove bottlenecks
- **Days 61–90:** Policy/gates in CI; game day validation; steering review with trend charts

**Success metrics:** Lead time, MTTR, CFR, or adoption % — targets set from baseline, not arbitrary.

**Stakeholder map:** VP Engineering sponsor, affected product director, platform lead.

**Azure/.NET example:** Instrument fix in Application Insights; tag deployments to correlate with change failure rate improvement.

**Architect:** Residual risk documented with expiry review date — not 'monitor' alone.

### Architecture Perspective

Expert scenarios test program leadership — structured plans beat ad-hoc heroics.

### Follow-up Questions

1. **CEO demands skip pilot? — Risk matrix with phased alternative; written acceptance if override.**
2. **Prove success? — Before/after dashboard on DORA or SLO — not team sentiment alone.**

### Common Mistakes in Interviews

- Jump to permanent tooling before stabilizing the incident
- Single 90-day big-bang without 30-day quick wins
- No measurable success criteria or executive sponsor

---

## Q111: On-Call No Runbooks

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Observability |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when engineers page without context?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Engineers page without context — runbook program in 60 days.

**Immediate (Days 1–7):**
- Form tiger team with platform + stream DRI
- Stabilize customer impact; exec comms every 24h
- Preserve evidence: deploy logs, traces, config snapshots

**30-day plan:**
| Week | Focus | Deliverable |
|------|-------|-------------|
| 1 | Triage + postmortem | Blameless doc, action owners |
| 2 | Baseline metrics | DORA/SLO dashboard before state |
| 3 | Pilot fix one squad | Measured improvement vs control |
| 4 | Runbook + training | Documented standard for observability |

**90-day plan:**
- **Days 31–60:** Roll out pattern to all affected teams; platform self-service to remove bottlenecks
- **Days 61–90:** Policy/gates in CI; game day validation; steering review with trend charts

**Success metrics:** Lead time, MTTR, CFR, or adoption % — targets set from baseline, not arbitrary.

**Stakeholder map:** VP Engineering sponsor, affected product director, platform lead.

**Azure/.NET example:** Instrument fix in Application Insights; tag deployments to correlate with change failure rate improvement.

**Architect:** Residual risk documented with expiry review date — not 'monitor' alone.

### Architecture Perspective

Expert scenarios test program leadership — structured plans beat ad-hoc heroics.

### Follow-up Questions

1. **CEO demands skip pilot? — Risk matrix with phased alternative; written acceptance if override.**
2. **Prove success? — Before/after dashboard on DORA or SLO — not team sentiment alone.**

### Common Mistakes in Interviews

- Jump to permanent tooling before stabilizing the incident
- Single 90-day big-bang without 30-day quick wins
- No measurable success criteria or executive sponsor

---

## Q112: App Insights Agent Overhead

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Observability |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when otel agent adds 200ms latency?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** OTel agent adds 200ms latency — tuning in 30 days.

**Immediate (Days 1–7):**
- Form tiger team with platform + stream DRI
- Stabilize customer impact; exec comms every 24h
- Preserve evidence: deploy logs, traces, config snapshots

**30-day plan:**
| Week | Focus | Deliverable |
|------|-------|-------------|
| 1 | Triage + postmortem | Blameless doc, action owners |
| 2 | Baseline metrics | DORA/SLO dashboard before state |
| 3 | Pilot fix one squad | Measured improvement vs control |
| 4 | Runbook + training | Documented standard for observability |

**90-day plan:**
- **Days 31–60:** Roll out pattern to all affected teams; platform self-service to remove bottlenecks
- **Days 61–90:** Policy/gates in CI; game day validation; steering review with trend charts

**Success metrics:** Lead time, MTTR, CFR, or adoption % — targets set from baseline, not arbitrary.

**Stakeholder map:** VP Engineering sponsor, affected product director, platform lead.

**Azure/.NET example:** Instrument fix in Application Insights; tag deployments to correlate with change failure rate improvement.

**Architect:** Residual risk documented with expiry review date — not 'monitor' alone.

### Architecture Perspective

Expert scenarios test program leadership — structured plans beat ad-hoc heroics.

### Follow-up Questions

1. **CEO demands skip pilot? — Risk matrix with phased alternative; written acceptance if override.**
2. **Prove success? — Before/after dashboard on DORA or SLO — not team sentiment alone.**

### Common Mistakes in Interviews

- Jump to permanent tooling before stabilizing the incident
- Single 90-day big-bang without 30-day quick wins
- No measurable success criteria or executive sponsor

---

## Q113: Synthetic False Negatives

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Observability |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when tests pass but users fail?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Tests pass but users fail — journey test redesign in 30 days.

**Immediate (Days 1–7):**
- Form tiger team with platform + stream DRI
- Stabilize customer impact; exec comms every 24h
- Preserve evidence: deploy logs, traces, config snapshots

**30-day plan:**
| Week | Focus | Deliverable |
|------|-------|-------------|
| 1 | Triage + postmortem | Blameless doc, action owners |
| 2 | Baseline metrics | DORA/SLO dashboard before state |
| 3 | Pilot fix one squad | Measured improvement vs control |
| 4 | Runbook + training | Documented standard for observability |

**90-day plan:**
- **Days 31–60:** Roll out pattern to all affected teams; platform self-service to remove bottlenecks
- **Days 61–90:** Policy/gates in CI; game day validation; steering review with trend charts

**Success metrics:** Lead time, MTTR, CFR, or adoption % — targets set from baseline, not arbitrary.

**Stakeholder map:** VP Engineering sponsor, affected product director, platform lead.

**Azure/.NET example:** Instrument fix in Application Insights; tag deployments to correlate with change failure rate improvement.

**Architect:** Residual risk documented with expiry review date — not 'monitor' alone.

### Architecture Perspective

Expert scenarios test program leadership — structured plans beat ad-hoc heroics.

### Follow-up Questions

1. **CEO demands skip pilot? — Risk matrix with phased alternative; written acceptance if override.**
2. **Prove success? — Before/after dashboard on DORA or SLO — not team sentiment alone.**

### Common Mistakes in Interviews

- Jump to permanent tooling before stabilizing the incident
- Single 90-day big-bang without 30-day quick wins
- No measurable success criteria or executive sponsor

---

## Q114: Tenant Noisy Neighbor Metrics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Observability |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when one tenant skews aggregates?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** One tenant skews aggregates — per-tenant observability in 60 days.

**Immediate (Days 1–7):**
- Form tiger team with platform + stream DRI
- Stabilize customer impact; exec comms every 24h
- Preserve evidence: deploy logs, traces, config snapshots

**30-day plan:**
| Week | Focus | Deliverable |
|------|-------|-------------|
| 1 | Triage + postmortem | Blameless doc, action owners |
| 2 | Baseline metrics | DORA/SLO dashboard before state |
| 3 | Pilot fix one squad | Measured improvement vs control |
| 4 | Runbook + training | Documented standard for observability |

**90-day plan:**
- **Days 31–60:** Roll out pattern to all affected teams; platform self-service to remove bottlenecks
- **Days 61–90:** Policy/gates in CI; game day validation; steering review with trend charts

**Success metrics:** Lead time, MTTR, CFR, or adoption % — targets set from baseline, not arbitrary.

**Stakeholder map:** VP Engineering sponsor, affected product director, platform lead.

**Azure/.NET example:** Instrument fix in Application Insights; tag deployments to correlate with change failure rate improvement.

**Architect:** Residual risk documented with expiry review date — not 'monitor' alone.

### Architecture Perspective

Expert scenarios test program leadership — structured plans beat ad-hoc heroics.

### Follow-up Questions

1. **CEO demands skip pilot? — Risk matrix with phased alternative; written acceptance if override.**
2. **Prove success? — Before/after dashboard on DORA or SLO — not team sentiment alone.**

### Common Mistakes in Interviews

- Jump to permanent tooling before stabilizing the incident
- Single 90-day big-bang without 30-day quick wins
- No measurable success criteria or executive sponsor

---

## Q115: Legacy Monolith Black Box

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Observability |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when no spans in core monolith?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** No spans in core monolith — phased instrumentation in 90 days.

**Immediate (Days 1–7):**
- Form tiger team with platform + stream DRI
- Stabilize customer impact; exec comms every 24h
- Preserve evidence: deploy logs, traces, config snapshots

**30-day plan:**
| Week | Focus | Deliverable |
|------|-------|-------------|
| 1 | Triage + postmortem | Blameless doc, action owners |
| 2 | Baseline metrics | DORA/SLO dashboard before state |
| 3 | Pilot fix one squad | Measured improvement vs control |
| 4 | Runbook + training | Documented standard for observability |

**90-day plan:**
- **Days 31–60:** Roll out pattern to all affected teams; platform self-service to remove bottlenecks
- **Days 61–90:** Policy/gates in CI; game day validation; steering review with trend charts

**Success metrics:** Lead time, MTTR, CFR, or adoption % — targets set from baseline, not arbitrary.

**Stakeholder map:** VP Engineering sponsor, affected product director, platform lead.

**Azure/.NET example:** Instrument fix in Application Insights; tag deployments to correlate with change failure rate improvement.

**Architect:** Residual risk documented with expiry review date — not 'monitor' alone.

### Architecture Perspective

Expert scenarios test program leadership — structured plans beat ad-hoc heroics.

### Follow-up Questions

1. **CEO demands skip pilot? — Risk matrix with phased alternative; written acceptance if override.**
2. **Prove success? — Before/after dashboard on DORA or SLO — not team sentiment alone.**

### Common Mistakes in Interviews

- Jump to permanent tooling before stabilizing the incident
- Single 90-day big-bang without 30-day quick wins
- No measurable success criteria or executive sponsor

---

## Q116: Observability Vendor Lock-In

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Observability |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when migrate from vendor a to otel?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Migrate from vendor A to OTel — 90-day portability plan.

**Immediate (Days 1–7):**
- Form tiger team with platform + stream DRI
- Stabilize customer impact; exec comms every 24h
- Preserve evidence: deploy logs, traces, config snapshots

**30-day plan:**
| Week | Focus | Deliverable |
|------|-------|-------------|
| 1 | Triage + postmortem | Blameless doc, action owners |
| 2 | Baseline metrics | DORA/SLO dashboard before state |
| 3 | Pilot fix one squad | Measured improvement vs control |
| 4 | Runbook + training | Documented standard for observability |

**90-day plan:**
- **Days 31–60:** Roll out pattern to all affected teams; platform self-service to remove bottlenecks
- **Days 61–90:** Policy/gates in CI; game day validation; steering review with trend charts

**Success metrics:** Lead time, MTTR, CFR, or adoption % — targets set from baseline, not arbitrary.

**Stakeholder map:** VP Engineering sponsor, affected product director, platform lead.

**Azure/.NET example:** Instrument fix in Application Insights; tag deployments to correlate with change failure rate improvement.

**Architect:** Residual risk documented with expiry review date — not 'monitor' alone.

### Architecture Perspective

Expert scenarios test program leadership — structured plans beat ad-hoc heroics.

### Follow-up Questions

1. **CEO demands skip pilot? — Risk matrix with phased alternative; written acceptance if override.**
2. **Prove success? — Before/after dashboard on DORA or SLO — not team sentiment alone.**

### Common Mistakes in Interviews

- Jump to permanent tooling before stabilizing the incident
- Single 90-day big-bang without 30-day quick wins
- No measurable success criteria or executive sponsor

---

## Q117: Incident No Timeline Reconstruction

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Observability |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when cannot build timeline?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Cannot build timeline — structured logging mandate in 30 days.

**Immediate (Days 1–7):**
- Form tiger team with platform + stream DRI
- Stabilize customer impact; exec comms every 24h
- Preserve evidence: deploy logs, traces, config snapshots

**30-day plan:**
| Week | Focus | Deliverable |
|------|-------|-------------|
| 1 | Triage + postmortem | Blameless doc, action owners |
| 2 | Baseline metrics | DORA/SLO dashboard before state |
| 3 | Pilot fix one squad | Measured improvement vs control |
| 4 | Runbook + training | Documented standard for observability |

**90-day plan:**
- **Days 31–60:** Roll out pattern to all affected teams; platform self-service to remove bottlenecks
- **Days 61–90:** Policy/gates in CI; game day validation; steering review with trend charts

**Success metrics:** Lead time, MTTR, CFR, or adoption % — targets set from baseline, not arbitrary.

**Stakeholder map:** VP Engineering sponsor, affected product director, platform lead.

**Azure/.NET example:** Instrument fix in Application Insights; tag deployments to correlate with change failure rate improvement.

**Architect:** Residual risk documented with expiry review date — not 'monitor' alone.

### Architecture Perspective

Expert scenarios test program leadership — structured plans beat ad-hoc heroics.

### Follow-up Questions

1. **CEO demands skip pilot? — Risk matrix with phased alternative; written acceptance if override.**
2. **Prove success? — Before/after dashboard on DORA or SLO — not team sentiment alone.**

### Common Mistakes in Interviews

- Jump to permanent tooling before stabilizing the incident
- Single 90-day big-bang without 30-day quick wins
- No measurable success criteria or executive sponsor

---

## Q118: SLO Burn Unnoticed Weekend

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Observability |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when outage sunday?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Outage Sunday — burn rate alerting in 14 days.

**Immediate (Days 1–7):**
- Form tiger team with platform + stream DRI
- Stabilize customer impact; exec comms every 24h
- Preserve evidence: deploy logs, traces, config snapshots

**30-day plan:**
| Week | Focus | Deliverable |
|------|-------|-------------|
| 1 | Triage + postmortem | Blameless doc, action owners |
| 2 | Baseline metrics | DORA/SLO dashboard before state |
| 3 | Pilot fix one squad | Measured improvement vs control |
| 4 | Runbook + training | Documented standard for observability |

**90-day plan:**
- **Days 31–60:** Roll out pattern to all affected teams; platform self-service to remove bottlenecks
- **Days 61–90:** Policy/gates in CI; game day validation; steering review with trend charts

**Success metrics:** Lead time, MTTR, CFR, or adoption % — targets set from baseline, not arbitrary.

**Stakeholder map:** VP Engineering sponsor, affected product director, platform lead.

**Azure/.NET example:** Instrument fix in Application Insights; tag deployments to correlate with change failure rate improvement.

**Architect:** Residual risk documented with expiry review date — not 'monitor' alone.

### Architecture Perspective

Expert scenarios test program leadership — structured plans beat ad-hoc heroics.

### Follow-up Questions

1. **CEO demands skip pilot? — Risk matrix with phased alternative; written acceptance if override.**
2. **Prove success? — Before/after dashboard on DORA or SLO — not team sentiment alone.**

### Common Mistakes in Interviews

- Jump to permanent tooling before stabilizing the incident
- Single 90-day big-bang without 30-day quick wins
- No measurable success criteria or executive sponsor

---

## Q119: FinOps Observability Cut

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Observability |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when cfo cuts budget 50%?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** CFO cuts budget 50% — retain SLO-critical signals in 30 days.

**Immediate (Days 1–7):**
- Form tiger team with platform + stream DRI
- Stabilize customer impact; exec comms every 24h
- Preserve evidence: deploy logs, traces, config snapshots

**30-day plan:**
| Week | Focus | Deliverable |
|------|-------|-------------|
| 1 | Triage + postmortem | Blameless doc, action owners |
| 2 | Baseline metrics | DORA/SLO dashboard before state |
| 3 | Pilot fix one squad | Measured improvement vs control |
| 4 | Runbook + training | Documented standard for observability |

**90-day plan:**
- **Days 31–60:** Roll out pattern to all affected teams; platform self-service to remove bottlenecks
- **Days 61–90:** Policy/gates in CI; game day validation; steering review with trend charts

**Success metrics:** Lead time, MTTR, CFR, or adoption % — targets set from baseline, not arbitrary.

**Stakeholder map:** VP Engineering sponsor, affected product director, platform lead.

**Azure/.NET example:** Instrument fix in Application Insights; tag deployments to correlate with change failure rate improvement.

**Architect:** Residual risk documented with expiry review date — not 'monitor' alone.

### Architecture Perspective

Expert scenarios test program leadership — structured plans beat ad-hoc heroics.

### Follow-up Questions

1. **CEO demands skip pilot? — Risk matrix with phased alternative; written acceptance if override.**
2. **Prove success? — Before/after dashboard on DORA or SLO — not team sentiment alone.**

### Common Mistakes in Interviews

- Jump to permanent tooling before stabilizing the incident
- Single 90-day big-bang without 30-day quick wins
- No measurable success criteria or executive sponsor

---

## Q120: Compliance Log Retention

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Observability |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when 7-year retention required?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** 7-year retention required — tiered storage architecture in 90 days.

**Immediate (Days 1–7):**
- Form tiger team with platform + stream DRI
- Stabilize customer impact; exec comms every 24h
- Preserve evidence: deploy logs, traces, config snapshots

**30-day plan:**
| Week | Focus | Deliverable |
|------|-------|-------------|
| 1 | Triage + postmortem | Blameless doc, action owners |
| 2 | Baseline metrics | DORA/SLO dashboard before state |
| 3 | Pilot fix one squad | Measured improvement vs control |
| 4 | Runbook + training | Documented standard for observability |

**90-day plan:**
- **Days 31–60:** Roll out pattern to all affected teams; platform self-service to remove bottlenecks
- **Days 61–90:** Policy/gates in CI; game day validation; steering review with trend charts

**Success metrics:** Lead time, MTTR, CFR, or adoption % — targets set from baseline, not arbitrary.

**Stakeholder map:** VP Engineering sponsor, affected product director, platform lead.

**Azure/.NET example:** Instrument fix in Application Insights; tag deployments to correlate with change failure rate improvement.

**Architect:** Residual risk documented with expiry review date — not 'monitor' alone.

### Architecture Perspective

Expert scenarios test program leadership — structured plans beat ad-hoc heroics.

### Follow-up Questions

1. **CEO demands skip pilot? — Risk matrix with phased alternative; written acceptance if override.**
2. **Prove success? — Before/after dashboard on DORA or SLO — not team sentiment alone.**

### Common Mistakes in Interviews

- Jump to permanent tooling before stabilizing the incident
- Single 90-day big-bang without 30-day quick wins
- No measurable success criteria or executive sponsor

---
