# Week 35 — Expert Scenario Q&A

> Q101–Q120: Premium format (Week 1 quality).

---


## Q101: DLQ Depth 50000 Messages

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Messaging & Events |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when dlq flood after bad deploy?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** DLQ flood after bad deploy — triage and replay in 14 days.

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
| 4 | Runbook + training | Documented standard for messaging |

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

## Q102: Duplicate Charge Events

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Messaging & Events |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when at-least-once caused double payment?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** At-least-once caused double payment — idempotency fix in 30 days.

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
| 4 | Runbook + training | Documented standard for messaging |

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

## Q103: Kafka Rebalance Storm

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Messaging & Events |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when consumer lag spike during deploy?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Consumer lag spike during deploy — rebalance tuning in 30 days.

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
| 4 | Runbook + training | Documented standard for messaging |

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

## Q104: Outbox Relay Stuck

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Messaging & Events |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when events not publishing 6 hours?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Events not publishing 6 hours — relay monitoring in 14 days.

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
| 4 | Runbook + training | Documented standard for messaging |

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

## Q105: Saga Compensation Failed

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Messaging & Events |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when refund failed mid-saga?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Refund failed mid-saga — manual intervention queue in 30 days.

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
| 4 | Runbook + training | Documented standard for messaging |

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

## Q106: Schema Breaking Change

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Messaging & Events |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when consumer crash loop?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Consumer crash loop — schema compatibility CI in 60 days.

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
| 4 | Runbook + training | Documented standard for messaging |

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

## Q107: Service Bus Throttling

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Messaging & Events |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when hit messaging units limit?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Hit messaging units limit — capacity plan in 30 days.

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
| 4 | Runbook + training | Documented standard for messaging |

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

## Q108: Event Order Violation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Messaging & Events |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when inventory deducted before payment?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Inventory deducted before payment — saga redesign in 60 days.

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
| 4 | Runbook + training | Documented standard for messaging |

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

## Q109: Poison Message Loop

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Messaging & Events |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when message reprocessed infinitely?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Message reprocessed infinitely — DLQ policy in 14 days.

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
| 4 | Runbook + training | Documented standard for messaging |

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

## Q110: Cross-Service Event Storm

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Messaging & Events |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when circular events melted cpu?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Circular events melted CPU — choreography audit in 30 days.

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
| 4 | Runbook + training | Documented standard for messaging |

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

## Q111: Message Loss Claim

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Messaging & Events |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when customer says order lost?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Customer says order lost — durability audit and fix.

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
| 4 | Runbook + training | Documented standard for messaging |

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

## Q112: Session Lock Timeout

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Messaging & Events |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when fifo broken under load?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** FIFO broken under load — session handler tuning.

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
| 4 | Runbook + training | Documented standard for messaging |

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

## Q113: Event Hub Lag Analytics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Messaging & Events |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when consumers 2 hours behind?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Consumers 2 hours behind — scale-out plan in 30 days.

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
| 4 | Runbook + training | Documented standard for messaging |

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

## Q114: No DLQ Monitoring

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Messaging & Events |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when dlq grew 3 months unnoticed?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** DLQ grew 3 months unnoticed — alerting in 7 days.

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
| 4 | Runbook + training | Documented standard for messaging |

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

## Q115: Outbox Table Bloat

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Messaging & Events |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when millions of unpublished rows?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Millions of unpublished rows — retention and relay fix.

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
| 4 | Runbook + training | Documented standard for messaging |

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

## Q116: Kafka Key Hot Partition

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Messaging & Events |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when one partition 90% traffic?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** One partition 90% traffic — key redesign in 60 days.

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
| 4 | Runbook + training | Documented standard for messaging |

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

## Q117: Service Bus Premium Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Messaging & Events |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when standard tier limits hit?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Standard tier limits hit — Premium migration 90 days.

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
| 4 | Runbook + training | Documented standard for messaging |

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

## Q118: Event Replay Production

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Messaging & Events |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when need rebuild read model?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Need rebuild read model — replay runbook in 30 days.

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
| 4 | Runbook + training | Documented standard for messaging |

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

## Q119: Message PII Leak

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Messaging & Events |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when events contain email in clear?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Events contain email in clear — schema scrub in 14 days.

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
| 4 | Runbook + training | Documented standard for messaging |

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

## Q120: Saga Timeout Undefined

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Messaging & Events |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when stuck sagas never complete?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Stuck sagas never complete — timeout compensation in 30 days.

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
| 4 | Runbook + training | Documented standard for messaging |

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
