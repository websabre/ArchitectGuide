# Week 30 — Expert Scenario Q&A

> Q101–Q120: Premium format (Week 1 quality).

---


## Q101: Production Deploy Pipeline Breach

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | CI/CD |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when secrets leaked in github actions logs?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Secrets leaked in GitHub Actions logs — 30-day remediation and pipeline hardening.

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
| 4 | Runbook + training | Documented standard for CI/CD |

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

## Q102: Blue-Green Swap Failed Smoke Test

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | CI/CD |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when swap triggered outage?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Swap triggered outage — incident response and pipeline fix in 30 days.

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
| 4 | Runbook + training | Documented standard for CI/CD |

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

## Q103: Canary False Positive Promotion

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | CI/CD |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when canary promoted despite latent bug?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Canary promoted despite latent bug — metric selection fix in 60 days.

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
| 4 | Runbook + training | Documented standard for CI/CD |

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

## Q104: OIDC Migration From SP Secrets

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | CI/CD |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when 200 repos with service principal secrets?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** 200 repos with service principal secrets — federated credential migration plan.

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
| 4 | Runbook + training | Documented standard for CI/CD |

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

## Q105: Breaking DB Migration Production

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | CI/CD |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when migration locked orders table 40 min?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Migration locked orders table 40 min — zero-downtime strategy in 90 days.

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
| 4 | Runbook + training | Documented standard for CI/CD |

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

## Q106: SAST Blocking All PRs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | CI/CD |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when developers disable scans?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Developers disable scans — balanced security gate in 30 days.

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
| 4 | Runbook + training | Documented standard for CI/CD |

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

## Q107: Pact Broker Outage Deploy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | CI/CD |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when contract tests unavailable?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Contract tests unavailable — deploy policy and broker HA in 60 days.

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
| 4 | Runbook + training | Documented standard for CI/CD |

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

## Q108: Rollback Failed Bad Artifact

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | CI/CD |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when rollback deployed wrong version?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Rollback deployed wrong version — immutable artifact discipline in 30 days.

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
| 4 | Runbook + training | Documented standard for CI/CD |

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

## Q109: SBOM Critical CVE Flood

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | CI/CD |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when 1000 images with log4j?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** 1000 images with log4j — SBOM-driven remediation in 14 days.

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
| 4 | Runbook + training | Documented standard for CI/CD |

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

## Q110: SLSA Audit Failure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | CI/CD |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when customer requires slsa l3?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Customer requires SLSA L3 — 90-day supply chain upgrade program.

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
| 4 | Runbook + training | Documented standard for CI/CD |

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

## Q111: Pipeline 2 Hour Lead Time

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | CI/CD |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when ci blocks elite dora?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** CI blocks elite DORA — parallelization program in 60 days.

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
| 4 | Runbook + training | Documented standard for CI/CD |

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

## Q112: Multi-Service Deploy Partial Failure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | CI/CD |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when 3 of 5 services deployed; inconsistent state?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** 3 of 5 services deployed; inconsistent state — orchestration fix.

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
| 4 | Runbook + training | Documented standard for CI/CD |

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

## Q113: GitHub Actions Minute Budget

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | CI/CD |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when org exceeds actions minutes?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Org exceeds Actions minutes — cost optimization in 30 days.

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
| 4 | Runbook + training | Documented standard for CI/CD |

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

## Q114: Prod Deploy Without Approval

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | CI/CD |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when misconfigured environment bypass?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Misconfigured environment bypass — governance fix in 14 days.

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
| 4 | Runbook + training | Documented standard for CI/CD |

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

## Q115: Container Image Tag Mutable

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | CI/CD |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when latest tag caused wrong deploy?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** latest tag caused wrong deploy — immutable digest policy in 30 days.

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
| 4 | Runbook + training | Documented standard for CI/CD |

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

## Q116: PR Environment Cost Overrun

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | CI/CD |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when ephemeral envs cost $50k/month?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Ephemeral envs cost $50K/month — lifecycle policy in 30 days.

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
| 4 | Runbook + training | Documented standard for CI/CD |

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

## Q117: Flaky Tests Block Releases

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | CI/CD |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when 20% flaky rate?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** 20% flaky rate — test stabilization sprint in 60 days.

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
| 4 | Runbook + training | Documented standard for CI/CD |

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

## Q118: Cross-Region Pipeline Failover

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | CI/CD |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when primary region pipeline down?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Primary region pipeline down — DR pipeline in 90 days.

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
| 4 | Runbook + training | Documented standard for CI/CD |

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

## Q119: Compliance Pipeline Gap

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | CI/CD |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when auditor finds missing deploy evidence?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Auditor finds missing deploy evidence — automated collection in 60 days.

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
| 4 | Runbook + training | Documented standard for CI/CD |

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

## Q120: Monorepo CI Explosion

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | CI/CD |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when every commit runs 4 hours ci?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Every commit runs 4 hours CI — affected-build optimization in 90 days.

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
| 4 | Runbook + training | Documented standard for CI/CD |

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
