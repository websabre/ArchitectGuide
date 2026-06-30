# Week 31 — Expert Scenario Q&A

> Q101–Q120: Premium format (Week 1 quality).

---


## Q101: Terraform State Corruption

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Infrastructure as Code |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when state file corrupted during apply?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** State file corrupted during apply — recovery and prevention in 30 days.

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
| 4 | Runbook + training | Documented standard for IaC |

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

## Q102: Manual Portal Change Drift

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Infrastructure as Code |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when critical nsg edited in portal?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Critical NSG edited in portal — drift remediation program in 60 days.

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
| 4 | Runbook + training | Documented standard for IaC |

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

## Q103: Bicep Deploy Deleted Production

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Infrastructure as Code |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when what-if missed dependency?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** What-if missed dependency — blast radius and process fix in 30 days.

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
| 4 | Runbook + training | Documented standard for IaC |

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

## Q104: IaC Adoption Resistance

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Infrastructure as Code |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when teams prefer click-ops?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Teams prefer click-ops — brownfield import and mandate in 90 days.

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
| 4 | Runbook + training | Documented standard for IaC |

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

## Q105: Policy Deny Blocks Deploy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Infrastructure as Code |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when azure policy blocks valid deployment?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Azure Policy blocks valid deployment — policy refinement in 30 days.

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
| 4 | Runbook + training | Documented standard for IaC |

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

## Q106: Multi-Sub State Lock Conflict

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Infrastructure as Code |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when two pipelines lock same state?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Two pipelines lock same state — partitioning fix in 14 days.

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
| 4 | Runbook + training | Documented standard for IaC |

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

## Q107: Landing Zone 12 Month Overdue

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Infrastructure as Code |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when lz program stalled?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** LZ program stalled — executive recovery plan in 90 days.

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
| 4 | Runbook + training | Documented standard for IaC |

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

## Q108: Module Breaking Change Cascade

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Infrastructure as Code |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when vnet module v3 breaks 40 consumers?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** VNet module v3 breaks 40 consumers — versioning policy in 60 days.

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
| 4 | Runbook + training | Documented standard for IaC |

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

## Q109: GitOps Desync Incident

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Infrastructure as Code |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when argo cd auto-sync reverted manual hotfix?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Argo CD auto-sync reverted manual hotfix — sync policy fix in 30 days.

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
| 4 | Runbook + training | Documented standard for IaC |

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

## Q110: IaC Secret in Git History

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Infrastructure as Code |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when key vault password committed?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Key Vault password committed — rotation and secret scanning in 14 days.

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
| 4 | Runbook + training | Documented standard for IaC |

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

## Q111: Terraform Import Wrong Resource

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Infrastructure as Code |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when imported wrong rg?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Imported wrong RG — state surgery and guardrails in 30 days.

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
| 4 | Runbook + training | Documented standard for IaC |

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

## Q112: Prod Dev Environment Skew

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Infrastructure as Code |
| **Frequency** | Very Common |
| **Type** | Scenario |

### Question

What do you do when prod-only bicep params caused outage?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Prod-only Bicep params caused outage — parity enforcement in 60 days.

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
| 4 | Runbook + training | Documented standard for IaC |

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

## Q113: IaC Pipeline 45 Min Apply

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Infrastructure as Code |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when monolithic stack?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Monolithic stack — stack splitting program in 90 days.

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
| 4 | Runbook + training | Documented standard for IaC |

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

## Q114: Compliance IaC Gap Audit

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Infrastructure as Code |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when auditor finds untagged resources?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Auditor finds untagged resources — policy remediation in 60 days.

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
| 4 | Runbook + training | Documented standard for IaC |

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

## Q115: Cross-Team Module Fork

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Infrastructure as Code |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when 5 teams forked same vnet module?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** 5 teams forked same VNet module — consolidation in 90 days.

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
| 4 | Runbook + training | Documented standard for IaC |

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

## Q116: Disaster Recovery IaC Rebuild

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Infrastructure as Code |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when region lost?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Region lost — rebuild from Git validation in 90 days.

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
| 4 | Runbook + training | Documented standard for IaC |

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

## Q117: Checkov False Positive Flood

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Infrastructure as Code |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when 500 findings block all prs?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** 500 findings block all PRs — rule tuning in 30 days.

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
| 4 | Runbook + training | Documented standard for IaC |

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

## Q118: Hub-Spoke Peering Limit

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Infrastructure as Code |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when peering limit hit at 400 spokes?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Peering limit hit at 400 spokes — topology redesign in 90 days.

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
| 4 | Runbook + training | Documented standard for IaC |

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

## Q119: IaC Engineer Bus Factor

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Infrastructure as Code |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when one person knows terraform?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** One person knows Terraform — knowledge transfer in 60 days.

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
| 4 | Runbook + training | Documented standard for IaC |

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

## Q120: Brownfield 500 Resources Import

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | Infrastructure as Code |
| **Frequency** | Common |
| **Type** | Scenario |

### Question

What do you do when acquire company infrastructure?

### Short Answer (30 seconds)

Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.

### Detailed Answer

**Situation:** Acquire company infrastructure — import program in 90 days.

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
| 4 | Runbook + training | Documented standard for IaC |

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
