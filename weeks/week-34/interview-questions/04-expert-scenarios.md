# Week 34 — Expert Scenario Q&A

> Q101–Q120: Premium format (Week 1 quality).

---


## Q101: Cache Stampede Black Friday

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scalability & Caching |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when db collapsed on ttl expiry?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** DB collapsed on TTL expiry — stampede mitigation before next sale.

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
| 4 | Runbook + training | Documented standard for scalability |

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

## Q102: Hot Key Celebrity Product

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scalability & Caching |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when single redis key 100k qps?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Single Redis key 100K QPS — hot key runbook execution.

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
| 4 | Runbook + training | Documented standard for scalability |

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

## Q103: Shard Resharding Live Traffic

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scalability & Caching |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when tenant growth requires resharding?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Tenant growth requires resharding — zero-downtime migration plan.

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
| 4 | Runbook + training | Documented standard for scalability |

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

## Q104: Replica Lag User Complaints

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scalability & Caching |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when users see stale data post-purchase?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Users see stale data post-purchase — read routing fix in 30 days.

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
| 4 | Runbook + training | Documented standard for scalability |

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

## Q105: CDN Cache Poisoning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scalability & Caching |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when wrong content served from edge?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Wrong content served from edge — cache key and purge fix.

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
| 4 | Runbook + training | Documented standard for scalability |

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

## Q106: Connection Pool Exhaustion

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scalability & Caching |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when hikari maxed during spike?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Hikari maxed during spike — pool sizing and scale plan.

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
| 4 | Runbook + training | Documented standard for scalability |

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

## Q107: Autoscale Thrashing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scalability & Caching |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when pods scale up/down every minute?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Pods scale up/down every minute — stabilization policy in 30 days.

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
| 4 | Runbook + training | Documented standard for scalability |

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

## Q108: Cache Invalidation Bug

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scalability & Caching |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when stale inventory caused oversell?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Stale inventory caused oversell — invalidation event fix in 14 days.

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
| 4 | Runbook + training | Documented standard for scalability |

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

## Q109: Cross-Shard Query Requirement

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scalability & Caching |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when report needs cross-shard join?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Report needs cross-shard join — async aggregation architecture.

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
| 4 | Runbook + training | Documented standard for scalability |

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

## Q110: Geo-Cache Inconsistency

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scalability & Caching |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when eu/us cache diverge?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** EU/US cache diverge — consistency policy in 60 days.

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
| 4 | Runbook + training | Documented standard for scalability |

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

## Q111: Load Balancer Sticky Session Fail

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scalability & Caching |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when session lost on scale-out?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Session lost on scale-out — stateless JWT migration.

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
| 4 | Runbook + training | Documented standard for scalability |

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

## Q112: Read Replica Cost Overrun

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scalability & Caching |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when 10 replicas unused?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** 10 replicas unused — right-sizing in 30 days.

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
| 4 | Runbook + training | Documented standard for scalability |

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

## Q113: Negative Cache Attack

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scalability & Caching |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when attacker queries random ids?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Attacker queries random IDs — bloom filter deployment.

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
| 4 | Runbook + training | Documented standard for scalability |

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

## Q114: Write-Behind Data Loss

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scalability & Caching |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when cache flush failed?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Cache flush failed — durability policy change.

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
| 4 | Runbook + training | Documented standard for scalability |

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

## Q115: Sharding Wrong Key

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scalability & Caching |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when sharded by date?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Sharded by date — hot latest shard — resharding program.

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
| 4 | Runbook + training | Documented standard for scalability |

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

## Q116: L1 Cache Memory Pressure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scalability & Caching |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when in-process cache oom?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** In-process cache OOM — size limits and eviction policy.

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
| 4 | Runbook + training | Documented standard for scalability |

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

## Q117: Front Door Origin Overload

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scalability & Caching |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when cdn miss storm?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** CDN miss storm — origin protection in 30 days.

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
| 4 | Runbook + training | Documented standard for scalability |

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

## Q118: Scale Test Never Run

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scalability & Caching |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when first prod spike failed?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** First prod spike failed — load test mandate before launch.

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
| 4 | Runbook + training | Documented standard for scalability |

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

## Q119: Hyperscale Tier Migration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scalability & Caching |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when azure sql hitting limits?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Azure SQL hitting limits — Hyperscale migration 90-day plan.

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
| 4 | Runbook + training | Documented standard for scalability |

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

## Q120: Multi-Tenant Noisy Neighbor Cache

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Scalability & Caching |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when one tenant fills redis?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** One tenant fills Redis — per-tenant quota in 60 days.

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
| 4 | Runbook + training | Documented standard for scalability |

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
