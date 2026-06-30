# Week 30 — Advanced Q&A

> Q071–Q100: Premium format (Week 1 quality).

---


## Q071: GitHub Actions Matrix Build

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | GitHub Actions |
| **Frequency** | Very Common |

### Question

How would you implement GitHub Actions Matrix Build with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

.NET matrix across OS versions; cache NuGet; reusable workflows for org standards.

### Detailed Answer (3–5 minutes)

**GitHub Actions Matrix Build** (CI/CD context)

.NET matrix across OS versions; cache NuGet; reusable workflows for org standards.

**Production implementation:**
```yaml
# Multi-stage Azure DevOps
stages:
- stage: Build
  jobs: [build, test, sbom]
- stage: DeployProd
  dependsOn: Build
  condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
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

GitHub Actions Matrix Build separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — GitHub Actions-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q072: Azure DevOps Multi-Stage YAML

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Azure DevOps |
| **Frequency** | Very Common |

### Question

How would you implement Azure DevOps Multi-Stage YAML with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Stages: build, test, deploy dev/staging/prod; environment approvals; template libraries.

### Detailed Answer (3–5 minutes)

**Azure DevOps Multi-Stage YAML** (CI/CD context)

Stages: build, test, deploy dev/staging/prod; environment approvals; template libraries.

**Production implementation:**
```yaml
# Multi-stage Azure DevOps
stages:
- stage: Build
  jobs: [build, test, sbom]
- stage: DeployProd
  dependsOn: Build
  condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
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

Azure DevOps Multi-Stage YAML separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Azure DevOps-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q073: Blue-Green App Service

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Deployment |
| **Frequency** | Very Common |

### Question

How would you implement Blue-Green App Service with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Two deployment slots; warm swap; smoke tests; instant rollback via swap back.

### Detailed Answer (3–5 minutes)

**Blue-Green App Service** (CI/CD context)

Two deployment slots; warm swap; smoke tests; instant rollback via swap back.

**Production implementation:**
```yaml
# Multi-stage Azure DevOps
stages:
- stage: Build
  jobs: [build, test, sbom]
- stage: DeployProd
  dependsOn: Build
  condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
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

Blue-Green App Service separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Deployment-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q074: Canary AKS with Flagger

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Deployment |
| **Frequency** | Very Common |

### Question

How would you implement Canary AKS with Flagger with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

5% traffic canary; Prometheus metrics gate; auto-promote or rollback.

### Detailed Answer (3–5 minutes)

**Canary AKS with Flagger** (CI/CD context)

5% traffic canary; Prometheus metrics gate; auto-promote or rollback.

**Production implementation:**
```yaml
# Multi-stage Azure DevOps
stages:
- stage: Build
  jobs: [build, test, sbom]
- stage: DeployProd
  dependsOn: Build
  condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
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

Canary AKS with Flagger separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Deployment-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q075: OIDC Azure Federated Credentials

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

How would you implement OIDC Azure Federated Credentials with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

GitHub Actions OIDC to Azure — no long-lived service principal secrets in repos.

### Detailed Answer (3–5 minutes)

**OIDC Azure Federated Credentials** (CI/CD context)

GitHub Actions OIDC to Azure — no long-lived service principal secrets in repos.

**Production implementation:**
```yaml
# Multi-stage Azure DevOps
stages:
- stage: Build
  jobs: [build, test, sbom]
- stage: DeployProd
  dependsOn: Build
  condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
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

OIDC Azure Federated Credentials separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Security-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q076: Database Migration Pipeline

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | CI/CD |
| **Frequency** | Very Common |

### Question

How would you implement Database Migration Pipeline with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Flyway/Liquibase in pipeline; backward-compatible migrations; expand-contract pattern.

### Detailed Answer (3–5 minutes)

**Database Migration Pipeline** (CI/CD context)

Flyway/Liquibase in pipeline; backward-compatible migrations; expand-contract pattern.

**Production implementation:**
```yaml
# Multi-stage Azure DevOps
stages:
- stage: Build
  jobs: [build, test, sbom]
- stage: DeployProd
  dependsOn: Build
  condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
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

Database Migration Pipeline separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — CI/CD-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q077: SAST in CI Pipeline

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | DevSecOps |
| **Frequency** | Very Common |

### Question

How would you implement SAST in CI Pipeline with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

SonarQube/CodeQL on PR; quality gate blocks merge; suppressions require security review.

### Detailed Answer (3–5 minutes)

**SAST in CI Pipeline** (CI/CD context)

SonarQube/CodeQL on PR; quality gate blocks merge; suppressions require security review.

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

SAST in CI Pipeline separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — DevSecOps-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q078: Pact Contract Testing CI

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Testing |
| **Frequency** | Very Common |

### Question

How would you implement Pact Contract Testing CI with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Consumer-driven contracts in pipeline; provider verification before deploy; pact broker.

### Detailed Answer (3–5 minutes)

**Pact Contract Testing CI** (CI/CD context)

Consumer-driven contracts in pipeline; provider verification before deploy; pact broker.

**Production implementation:**
```yaml
# Multi-stage Azure DevOps
stages:
- stage: Build
  jobs: [build, test, sbom]
- stage: DeployProd
  dependsOn: Build
  condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
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

Pact Contract Testing CI separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Testing-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q079: Automated Rollback Pipeline

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | CI/CD |
| **Frequency** | Very Common |

### Question

How would you implement Automated Rollback Pipeline with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Health check failure post-deploy triggers previous artifact redeploy; max 5 min rollback SLA.

### Detailed Answer (3–5 minutes)

**Automated Rollback Pipeline** (CI/CD context)

Health check failure post-deploy triggers previous artifact redeploy; max 5 min rollback SLA.

**Production implementation:**
```yaml
# Multi-stage Azure DevOps
stages:
- stage: Build
  jobs: [build, test, sbom]
- stage: DeployProd
  dependsOn: Build
  condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
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

Automated Rollback Pipeline separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — CI/CD-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q080: SBOM Generation Pipeline

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Supply Chain |
| **Frequency** | Very Common |

### Question

How would you implement SBOM Generation Pipeline with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Syft/SPDX on container build; store in artifact registry; vulnerability scan against SBOM.

### Detailed Answer (3–5 minutes)

**SBOM Generation Pipeline** (CI/CD context)

Syft/SPDX on container build; store in artifact registry; vulnerability scan against SBOM.

**Production implementation:**
```yaml
# Multi-stage Azure DevOps
stages:
- stage: Build
  jobs: [build, test, sbom]
- stage: DeployProd
  dependsOn: Build
  condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
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

SBOM Generation Pipeline separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Supply Chain-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q081: SLSA Level 3 Pipeline

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Supply Chain |
| **Frequency** | Very Common |

### Question

How would you implement SLSA Level 3 Pipeline with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Hermetic builds, signed provenance, isolated build workers — document supply chain.

### Detailed Answer (3–5 minutes)

**SLSA Level 3 Pipeline** (CI/CD context)

Hermetic builds, signed provenance, isolated build workers — document supply chain.

**Production implementation:**
```yaml
# Multi-stage Azure DevOps
stages:
- stage: Build
  jobs: [build, test, sbom]
- stage: DeployProd
  dependsOn: Build
  condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
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

SLSA Level 3 Pipeline separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Supply Chain-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q082: Immutable Artifact Promotion

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | CI/CD |
| **Frequency** | Very Common |

### Question

How would you implement Immutable Artifact Promotion with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Same container digest dev→staging→prod; never rebuild; tag promotion only.

### Detailed Answer (3–5 minutes)

**Immutable Artifact Promotion** (CI/CD context)

Same container digest dev→staging→prod; never rebuild; tag promotion only.

**Production implementation:**
```yaml
# Multi-stage Azure DevOps
stages:
- stage: Build
  jobs: [build, test, sbom]
- stage: DeployProd
  dependsOn: Build
  condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
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

Immutable Artifact Promotion separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — CI/CD-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q083: Pipeline Secret Management

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Security |
| **Frequency** | Very Common |

### Question

How would you implement Pipeline Secret Management with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Azure Key Vault references; no secrets in YAML; rotation without pipeline edit.

### Detailed Answer (3–5 minutes)

**Pipeline Secret Management** (CI/CD context)

Azure Key Vault references; no secrets in YAML; rotation without pipeline edit.

**Production implementation:**
```yaml
# Multi-stage Azure DevOps
stages:
- stage: Build
  jobs: [build, test, sbom]
- stage: DeployProd
  dependsOn: Build
  condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
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

Pipeline Secret Management separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Security-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q084: Ephemeral PR Environments

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | CI/CD |
| **Frequency** | Very Common |

### Question

How would you implement Ephemeral PR Environments with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Bicep deploy on PR; smoke test; tear down on merge — full integration per PR.

### Detailed Answer (3–5 minutes)

**Ephemeral PR Environments** (CI/CD context)

Bicep deploy on PR; smoke test; tear down on merge — full integration per PR.

**Production implementation:**
```yaml
# Multi-stage Azure DevOps
stages:
- stage: Build
  jobs: [build, test, sbom]
- stage: DeployProd
  dependsOn: Build
  condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
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

Ephemeral PR Environments separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — CI/CD-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q085: Pipeline Parallelization

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | CI/CD |
| **Frequency** | Very Common |

### Question

How would you implement Pipeline Parallelization with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Split test suites; test impact analysis; distributed test agents — cut 45min to 12min.

### Detailed Answer (3–5 minutes)

**Pipeline Parallelization** (CI/CD context)

Split test suites; test impact analysis; distributed test agents — cut 45min to 12min.

**Production implementation:**
```yaml
# Multi-stage Azure DevOps
stages:
- stage: Build
  jobs: [build, test, sbom]
- stage: DeployProd
  dependsOn: Build
  condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
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

Pipeline Parallelization separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — CI/CD-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q086: Deployment Gates Quality

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | CI/CD |
| **Frequency** | Very Common |

### Question

How would you implement Deployment Gates Quality with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Azure DevOps gates: performance baseline, security scan, manual approval for prod.

### Detailed Answer (3–5 minutes)

**Deployment Gates Quality** (CI/CD context)

Azure DevOps gates: performance baseline, security scan, manual approval for prod.

**Production implementation:**
```yaml
# Multi-stage Azure DevOps
stages:
- stage: Build
  jobs: [build, test, sbom]
- stage: DeployProd
  dependsOn: Build
  condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
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

Deployment Gates Quality separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — CI/CD-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q087: Container Image Signing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Supply Chain |
| **Frequency** | Very Common |

### Question

How would you implement Container Image Signing with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Cosign sign images; admission controller verifies signature in AKS.

### Detailed Answer (3–5 minutes)

**Container Image Signing** (CI/CD context)

Cosign sign images; admission controller verifies signature in AKS.

**Production implementation:**
```yaml
# Multi-stage Azure DevOps
stages:
- stage: Build
  jobs: [build, test, sbom]
- stage: DeployProd
  dependsOn: Build
  condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
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

Container Image Signing separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Supply Chain-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q088: Pipeline as Code Review

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Governance |
| **Frequency** | Very Common |

### Question

How would you implement Pipeline as Code Review with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

CI YAML in PR review; policy checks via OPA/Conftest; no UI-only pipeline edits.

### Detailed Answer (3–5 minutes)

**Pipeline as Code Review** (CI/CD context)

CI YAML in PR review; policy checks via OPA/Conftest; no UI-only pipeline edits.

**Production implementation:**
```yaml
# Multi-stage Azure DevOps
stages:
- stage: Build
  jobs: [build, test, sbom]
- stage: DeployProd
  dependsOn: Build
  condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
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

Pipeline as Code Review separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Governance-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q089: Release Orchestration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | CI/CD |
| **Frequency** | Very Common |

### Question

How would you implement Release Orchestration with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Coordinate multi-service deploy order; health aggregation; coordinated rollback.

### Detailed Answer (3–5 minutes)

**Release Orchestration** (CI/CD context)

Coordinate multi-service deploy order; health aggregation; coordinated rollback.

**Production implementation:**
```yaml
# Multi-stage Azure DevOps
stages:
- stage: Build
  jobs: [build, test, sbom]
- stage: DeployProd
  dependsOn: Build
  condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
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

Release Orchestration separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — CI/CD-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q090: Feature Branch CI Cost

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | CI/CD |
| **Frequency** | Very Common |

### Question

How would you implement Feature Branch CI Cost with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Self-hosted runners for private network; spot VMs for non-prod; cache aggressively.

### Detailed Answer (3–5 minutes)

**Feature Branch CI Cost** (CI/CD context)

Self-hosted runners for private network; spot VMs for non-prod; cache aggressively.

**Production implementation:**
```yaml
# Multi-stage Azure DevOps
stages:
- stage: Build
  jobs: [build, test, sbom]
- stage: DeployProd
  dependsOn: Build
  condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
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

Feature Branch CI Cost separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — CI/CD-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q091: Pipeline Observability

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | CI/CD |
| **Frequency** | Common |

### Question

How would you implement Pipeline Observability with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Track pipeline duration, failure rate, flaky test rate — DORA lead time input.

### Detailed Answer (3–5 minutes)

**Pipeline Observability** (CI/CD context)

Track pipeline duration, failure rate, flaky test rate — DORA lead time input.

**Production implementation:**
```yaml
# Multi-stage Azure DevOps
stages:
- stage: Build
  jobs: [build, test, sbom]
- stage: DeployProd
  dependsOn: Build
  condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
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

Pipeline Observability separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — CI/CD-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q092: DAST in Staging Gate

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | DevSecOps |
| **Frequency** | Common |

### Question

How would you implement DAST in Staging Gate with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

OWASP ZAP against staging post-deploy; block prod promote on critical findings.

### Detailed Answer (3–5 minutes)

**DAST in Staging Gate** (CI/CD context)

OWASP ZAP against staging post-deploy; block prod promote on critical findings.

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

DAST in Staging Gate separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — DevSecOps-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q093: Infrastructure Pipeline

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | CI/CD |
| **Frequency** | Common |

### Question

How would you implement Infrastructure Pipeline with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Terraform/Bicep plan on PR; apply on merge to main; drift detection scheduled.

### Detailed Answer (3–5 minutes)

**Infrastructure Pipeline** (CI/CD context)

Terraform/Bicep plan on PR; apply on merge to main; drift detection scheduled.

**Production implementation:**
```yaml
# Multi-stage Azure DevOps
stages:
- stage: Build
  jobs: [build, test, sbom]
- stage: DeployProd
  dependsOn: Build
  condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
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

Infrastructure Pipeline separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — CI/CD-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q094: Mobile CI Code Signing

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | CI/CD |
| **Frequency** | Common |

### Question

How would you implement Mobile CI Code Signing with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Secure cert storage in Key Vault; Fastlane match pattern; separate signing stage.

### Detailed Answer (3–5 minutes)

**Mobile CI Code Signing** (CI/CD context)

Secure cert storage in Key Vault; Fastlane match pattern; separate signing stage.

**Production implementation:**
```yaml
# Multi-stage Azure DevOps
stages:
- stage: Build
  jobs: [build, test, sbom]
- stage: DeployProd
  dependsOn: Build
  condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
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

Mobile CI Code Signing separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — CI/CD-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q095: Monorepo CI Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | CI/CD |
| **Frequency** | Common |

### Question

How would you implement Monorepo CI Strategy with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Path filters trigger affected services only; Nx/Turborepo affected graph.

### Detailed Answer (3–5 minutes)

**Monorepo CI Strategy** (CI/CD context)

Path filters trigger affected services only; Nx/Turborepo affected graph.

**Production implementation:**
```yaml
# Multi-stage Azure DevOps
stages:
- stage: Build
  jobs: [build, test, sbom]
- stage: DeployProd
  dependsOn: Build
  condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
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

Monorepo CI Strategy separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — CI/CD-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q096: Pipeline Failure Notification

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | CI/CD |
| **Frequency** | Common |

### Question

How would you implement Pipeline Failure Notification with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Slack/Teams with actionable context; link to logs; auto-create incident if prod deploy fails.

### Detailed Answer (3–5 minutes)

**Pipeline Failure Notification** (CI/CD context)

Slack/Teams with actionable context; link to logs; auto-create incident if prod deploy fails.

**Production implementation:**
```yaml
# Multi-stage Azure DevOps
stages:
- stage: Build
  jobs: [build, test, sbom]
- stage: DeployProd
  dependsOn: Build
  condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
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

Pipeline Failure Notification separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — CI/CD-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q097: Compliance Evidence Pipeline

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | Governance |
| **Frequency** | Common |

### Question

How would you implement Compliance Evidence Pipeline with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Auto-collect SOC2 change management evidence from deployment records.

### Detailed Answer (3–5 minutes)

**Compliance Evidence Pipeline** (CI/CD context)

Auto-collect SOC2 change management evidence from deployment records.

**Production implementation:**
```yaml
# Multi-stage Azure DevOps
stages:
- stage: Build
  jobs: [build, test, sbom]
- stage: DeployProd
  dependsOn: Build
  condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
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

Compliance Evidence Pipeline separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — Governance-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q098: Zero-Downtime DB Deploy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | CI/CD |
| **Frequency** | Common |

### Question

How would you implement Zero-Downtime DB Deploy with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Expand-contract migrations; dual-write period; feature flag for new schema reads.

### Detailed Answer (3–5 minutes)

**Zero-Downtime DB Deploy** (CI/CD context)

Expand-contract migrations; dual-write period; feature flag for new schema reads.

**Production implementation:**
```yaml
# Multi-stage Azure DevOps
stages:
- stage: Build
  jobs: [build, test, sbom]
- stage: DeployProd
  dependsOn: Build
  condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
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

Zero-Downtime DB Deploy separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — CI/CD-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q099: Pipeline Disaster Recovery

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | CI/CD |
| **Frequency** | Common |

### Question

How would you implement Pipeline Disaster Recovery with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Backup pipeline definitions; runner failover; artifact registry geo-replication.

### Detailed Answer (3–5 minutes)

**Pipeline Disaster Recovery** (CI/CD context)

Backup pipeline definitions; runner failover; artifact registry geo-replication.

**Production implementation:**
```yaml
# Multi-stage Azure DevOps
stages:
- stage: Build
  jobs: [build, test, sbom]
- stage: DeployProd
  dependsOn: Build
  condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
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

Pipeline Disaster Recovery separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — CI/CD-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---

## Q100: GitOps vs Push Deploy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | CI/CD |
| **Frequency** | Common |

### Question

How would you implement GitOps vs Push Deploy with trade-offs and conflict resolution in production?

### Short Answer (30 seconds)

Argo CD pull vs pipeline push — when each fits Azure landing zone model.

### Detailed Answer (3–5 minutes)

**GitOps vs Push Deploy** (CI/CD context)

Argo CD pull vs pipeline push — when each fits Azure landing zone model.

**Production implementation:**
```yaml
# Multi-stage Azure DevOps
stages:
- stage: Build
  jobs: [build, test, sbom]
- stage: DeployProd
  dependsOn: Build
  condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
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

GitOps vs Push Deploy separates senior architects who've operated systems from those who've only read docs.

### Follow-up Questions

1. **What breaks at 10× scale? — CI/CD-specific bottleneck: throughput, coupling, or cost ceiling.**
2. **Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.**

### Common Mistakes in Interviews

- Choosing tools before requirements are clear
- No documented trade-off between speed and safety
- Enabling in production without observability and runbook

---
