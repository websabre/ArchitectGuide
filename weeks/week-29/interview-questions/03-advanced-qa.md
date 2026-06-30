# Week 29 — Advanced Q&A

> Q071–Q100: Premium format (Week 1 quality).

---


## Q071: DevSecOps Shift Left

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | DevSecOps |
| **Frequency** | Very Common |

### Question

How would you implement DevSecOps Shift Left with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Integrate security in CI: SAST, dependency scan, container scan, secrets detection before merge — not gate at release.

### Detailed Answer (3–5 minutes)

**DevSecOps Shift Left** (DevOps context)

Integrate security in CI: SAST, dependency scan, container scan, secrets detection before merge — not gate at release.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

DevSecOps Shift Left separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — DevSecOps-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q072: Conway's Law Application

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Conway's Law |
| **Frequency** | Very Common |

### Question

How would you implement Conway's Law Application with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

System architecture mirrors communication structure — align service boundaries to team ownership or pay collaboration tax.

### Detailed Answer (3–5 minutes)

**Conway's Law Application** (DevOps context)

System architecture mirrors communication structure — align service boundaries to team ownership or pay collaboration tax.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Conway's Law Application separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Conway's Law-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q073: Feature Flag Architecture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Feature Flags |
| **Frequency** | Very Common |

### Question

How would you implement Feature Flag Architecture with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Azure App Configuration + targeting; kill switches; flag lifecycle cleanup; test all combinations in CI.

### Detailed Answer (3–5 minutes)

**Feature Flag Architecture** (DevOps context)

Azure App Configuration + targeting; kill switches; flag lifecycle cleanup; test all combinations in CI.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Feature Flag Architecture separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Feature Flags-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q074: Deployment Frequency Improvement

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | DORA |
| **Frequency** | Very Common |

### Question

How would you implement Deployment Frequency Improvement with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Reduce batch size, trunk-based, automated deploy pipeline, eliminate manual CAB for low-risk tiers.

### Detailed Answer (3–5 minutes)

**Deployment Frequency Improvement** (DevOps context)

Reduce batch size, trunk-based, automated deploy pipeline, eliminate manual CAB for low-risk tiers.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Deployment Frequency Improvement separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — DORA-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q075: Lead Time Reduction

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | DORA |
| **Frequency** | Very Common |

### Question

How would you implement Lead Time Reduction with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Parallelize CI, ephemeral environments, shift tests left, reduce handoffs between teams.

### Detailed Answer (3–5 minutes)

**Lead Time Reduction** (DevOps context)

Parallelize CI, ephemeral environments, shift tests left, reduce handoffs between teams.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Lead Time Reduction separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — DORA-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q076: Change Failure Rate Reduction

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | DORA |
| **Frequency** | Very Common |

### Question

How would you implement Change Failure Rate Reduction with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Canary deploys, automated rollback, contract tests, progressive delivery, feature flags.

### Detailed Answer (3–5 minutes)

**Change Failure Rate Reduction** (DevOps context)

Canary deploys, automated rollback, contract tests, progressive delivery, feature flags.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Change Failure Rate Reduction separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — DORA-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q077: MTTR Improvement

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | DORA |
| **Frequency** | Very Common |

### Question

How would you implement MTTR Improvement with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Runbooks, observability, on-call rotation, chaos drills, automated rollback on SLO burn.

### Detailed Answer (3–5 minutes)

**MTTR Improvement** (DevOps context)

Runbooks, observability, on-call rotation, chaos drills, automated rollback on SLO burn.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

MTTR Improvement separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — DORA-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q078: Platform as Product

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Platform Engineering |
| **Frequency** | Very Common |

### Question

How would you implement Platform as Product with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Internal NPS surveys, roadmap from stream team pain, adoption metrics, thin vertical slices.

### Detailed Answer (3–5 minutes)

**Platform as Product** (DevOps context)

Internal NPS surveys, roadmap from stream team pain, adoption metrics, thin vertical slices.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Platform as Product separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Platform Engineering-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q079: Enabling Team Rotation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Team Topologies |
| **Frequency** | Very Common |

### Question

How would you implement Enabling Team Rotation with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

6-week embed with stream squad teaching observability; exit when self-sufficient; avoid permanent dependency.

### Detailed Answer (3–5 minutes)

**Enabling Team Rotation** (DevOps context)

6-week embed with stream squad teaching observability; exit when self-sufficient; avoid permanent dependency.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Enabling Team Rotation separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Team Topologies-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q080: DORA Benchmark Tiers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | DORA |
| **Frequency** | Very Common |

### Question

How would you implement DORA Benchmark Tiers with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Elite/High/Medium/Low classifications — compare year-over-year, not vanity absolute numbers.

### Detailed Answer (3–5 minutes)

**DORA Benchmark Tiers** (DevOps context)

Elite/High/Medium/Low classifications — compare year-over-year, not vanity absolute numbers.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

DORA Benchmark Tiers separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — DORA-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q081: Toil Reduction SRE

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | SRE |
| **Frequency** | Very Common |

### Question

How would you implement Toil Reduction SRE with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Identify repetitive manual ops; automate or eliminate; target <50% toil; track toil budget per sprint.

### Detailed Answer (3–5 minutes)

**Toil Reduction SRE** (DevOps context)

Identify repetitive manual ops; automate or eliminate; target <50% toil; track toil budget per sprint.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Toil Reduction SRE separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — SRE-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q082: Internal Developer Portal

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Platform Engineering |
| **Frequency** | Very Common |

### Question

How would you implement Internal Developer Portal with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Backstage catalog: services, APIs, ownership, runbooks, scorecards for production readiness.

### Detailed Answer (3–5 minutes)

**Internal Developer Portal** (DevOps context)

Backstage catalog: services, APIs, ownership, runbooks, scorecards for production readiness.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Internal Developer Portal separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Platform Engineering-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q083: Golden Path Template

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Platform Engineering |
| **Frequency** | Very Common |

### Question

How would you implement Golden Path Template with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Opinionated .NET 8 + AKS + Bicep + GitHub Actions starter — 80% teams adopt without customization.

### Detailed Answer (3–5 minutes)

**Golden Path Template** (DevOps context)

Opinionated .NET 8 + AKS + Bicep + GitHub Actions starter — 80% teams adopt without customization.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Golden Path Template separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Platform Engineering-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q084: Cognitive Load Reduction

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Team Topologies |
| **Frequency** | Very Common |

### Question

How would you implement Cognitive Load Reduction with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Abstract K8s complexity behind platform abstractions; stream teams focus on domain not ingress YAML.

### Detailed Answer (3–5 minutes)

**Cognitive Load Reduction** (DevOps context)

Abstract K8s complexity behind platform abstractions; stream teams focus on domain not ingress YAML.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Cognitive Load Reduction separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Team Topologies-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q085: SRE Embedding Model

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | SRE |
| **Frequency** | Very Common |

### Question

How would you implement SRE Embedding Model with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

SRE pairs with stream team for launch; shared on-call first 90 days; hand off with runbooks.

### Detailed Answer (3–5 minutes)

**SRE Embedding Model** (DevOps context)

SRE pairs with stream team for launch; shared on-call first 90 days; hand off with runbooks.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

SRE Embedding Model separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — SRE-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q086: On-Call Rotation Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | SRE |
| **Frequency** | Very Common |

### Question

How would you implement On-Call Rotation Design with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Follow-the-sun or regional; max 1 week primary; secondary backup; compensation; burnout monitoring.

### Detailed Answer (3–5 minutes)

**On-Call Rotation Design** (DevOps context)

Follow-the-sun or regional; max 1 week primary; secondary backup; compensation; burnout monitoring.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

On-Call Rotation Design separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — SRE-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q087: Incident Command System

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Incident Response |
| **Frequency** | Very Common |

### Question

How would you implement Incident Command System with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

IC, comms lead, scribe roles; status page updates every 15 min; separate war room from debugging.

### Detailed Answer (3–5 minutes)

**Incident Command System** (DevOps context)

IC, comms lead, scribe roles; status page updates every 15 min; separate war room from debugging.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Incident Command System separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Incident Response-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q088: CAB Alternative Risk Tiers

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Governance |
| **Frequency** | Very Common |

### Question

How would you implement CAB Alternative Risk Tiers with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Low-risk auto-deploy; medium peer review; high architecture review — replace blanket CAB.

### Detailed Answer (3–5 minutes)

**CAB Alternative Risk Tiers** (DevOps context)

Low-risk auto-deploy; medium peer review; high architecture review — replace blanket CAB.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

CAB Alternative Risk Tiers separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Governance-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q089: Progressive Delivery Culture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Delivery |
| **Frequency** | Very Common |

### Question

How would you implement Progressive Delivery Culture with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Canary, blue-green, feature flags as default conversation — not big-bang releases.

### Detailed Answer (3–5 minutes)

**Progressive Delivery Culture** (DevOps context)

Canary, blue-green, feature flags as default conversation — not big-bang releases.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Progressive Delivery Culture separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Delivery-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q090: Developer Experience Metrics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Platform Engineering |
| **Frequency** | Very Common |

### Question

How would you implement Developer Experience Metrics with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Time to first PR merge, time to prod, local dev setup minutes, platform ticket wait time.

### Detailed Answer (3–5 minutes)

**Developer Experience Metrics** (DevOps context)

Time to first PR merge, time to prod, local dev setup minutes, platform ticket wait time.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Developer Experience Metrics separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Platform Engineering-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q091: Psychological Safety

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Culture |
| **Frequency** | Common |

### Question

How would you implement Psychological Safety with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Leaders admit mistakes; reward incident reporting; no retribution for outage participation.

### Detailed Answer (3–5 minutes)

**Psychological Safety** (DevOps context)

Leaders admit mistakes; reward incident reporting; no retribution for outage participation.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Psychological Safety separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Culture-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q092: Flow Efficiency vs Resource

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Lean |
| **Frequency** | Common |

### Question

How would you implement Flow Efficiency vs Resource with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Optimize end-to-end flow not individual team utilization — 90% busy teams create queues.

### Detailed Answer (3–5 minutes)

**Flow Efficiency vs Resource** (DevOps context)

Optimize end-to-end flow not individual team utilization — 90% busy teams create queues.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Flow Efficiency vs Resource separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Lean-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q093: WIP Limits Kanban

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Lean |
| **Frequency** | Common |

### Question

How would you implement WIP Limits Kanban with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Cap in-progress items per team; reduces context switching; surfaces bottlenecks visibly.

### Detailed Answer (3–5 minutes)

**WIP Limits Kanban** (DevOps context)

Cap in-progress items per team; reduces context switching; surfaces bottlenecks visibly.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

WIP Limits Kanban separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Lean-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q094: Continuous Learning Culture

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Culture |
| **Frequency** | Common |

### Question

How would you implement Continuous Learning Culture with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Guilds, internal tech talks, postmortem reviews as training, budget for conferences.

### Detailed Answer (3–5 minutes)

**Continuous Learning Culture** (DevOps context)

Guilds, internal tech talks, postmortem reviews as training, budget for conferences.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Continuous Learning Culture separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Culture-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q095: Architecture Runway

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Planning |
| **Frequency** | Common |

### Question

How would you implement Architecture Runway with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Reserve 20% capacity for platform improvements enabling next quarter features.

### Detailed Answer (3–5 minutes)

**Architecture Runway** (DevOps context)

Reserve 20% capacity for platform improvements enabling next quarter features.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Architecture Runway separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Planning-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q096: Technical Debt vs Velocity

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Planning |
| **Frequency** | Common |

### Question

How would you implement Technical Debt vs Velocity with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Visible debt register tied to incident correlation; negotiate paydown in planning.

### Detailed Answer (3–5 minutes)

**Technical Debt vs Velocity** (DevOps context)

Visible debt register tied to incident correlation; negotiate paydown in planning.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Technical Debt vs Velocity separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Planning-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q097: Transformation Success Metrics

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | DORA |
| **Frequency** | Common |

### Question

How would you implement Transformation Success Metrics with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Baseline → 6-month → 12-month DORA; developer survey; incident trend; business outcome linkage.

### Detailed Answer (3–5 minutes)

**Transformation Success Metrics** (DevOps context)

Baseline → 6-month → 12-month DORA; developer survey; incident trend; business outcome linkage.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Transformation Success Metrics separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — DORA-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q098: CALMS Automation Depth

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | CALMS |
| **Frequency** | Common |

### Question

How would you implement CALMS Automation Depth with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

IaC everything, policy as code, automated compliance evidence — not shell scripts on laptops.

### Detailed Answer (3–5 minutes)

**CALMS Automation Depth** (DevOps context)

IaC everything, policy as code, automated compliance evidence — not shell scripts on laptops.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

CALMS Automation Depth separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — CALMS-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q099: DevOps Team Anti-Pattern

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Anti-Patterns |
| **Frequency** | Common |

### Question

How would you implement DevOps Team Anti-Pattern with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Separate DevOps team doing ops for devs — creates handoff; embed or platform instead.

### Detailed Answer (3–5 minutes)

**DevOps Team Anti-Pattern** (DevOps context)

Separate DevOps team doing ops for devs — creates handoff; embed or platform instead.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

DevOps Team Anti-Pattern separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Anti-Patterns-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q100: Value Stream Bottleneck Fix

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Value Stream |
| **Frequency** | Common |

### Question

How would you implement Value Stream Bottleneck Fix with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Environment provisioning 3 days → Bicep PR environments in 15 min — measure lead time delta.

### Detailed Answer (3–5 minutes)

**Value Stream Bottleneck Fix** (DevOps context)

Environment provisioning 3 days → Bicep PR environments in 15 min — measure lead time delta.

**Production implementation:**
```yaml
# GitHub Actions — security gate on PR
- name: CodeQL
  uses: github/codeql-action/analyze@v3
- name: Dependency scan
  run: dotnet list package --vulnerable
```

**Trade-offs:**
| Option | When to choose | Risk |
|--------|----------------|------|
| Managed Azure service | Team <10 ops engineers | Cost at scale |
| Self-managed OSS | Deep customization need | Ops toil |
| Hybrid | Enterprise compliance | Integration complexity |

**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot on one squad for 2 weeks before org-wide mandate.

**Operational readiness:** Dashboard, alert, and runbook required before production cutover.

**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption.

### Architecture Perspective

Value Stream Bottleneck Fix separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Value Stream-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---
