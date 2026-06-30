# Month 8 Capstone — Full DevOps Platform

> **Phase 8** | Complete after weeks in this month.

## Brief

Month 8 capstone: Bicep + GitHub Actions OIDC + OTel + feature flags.

## Scenario

**PlatformOne** is an internal developer platform team (~25 engineers) serving **40 product squads** deploying to Azure. Leadership mandates: infrastructure as code only, no long-lived service principals in CI, full distributed tracing, and safe feature rollout via flags. You are designing the **reference DevOps platform** — Bicep modules, GitHub Actions OIDC to Azure, OpenTelemetry pipeline, and LaunchDarkly (or Azure App Configuration) integration — that squads will clone. Constraints: SOC 2 audit in Q3, all IaC changes require PR review, and prod deploys need manual approval gate. Stakeholders include security (OIDC federation), FinOps (Bicep what-if in CI), and squad leads (self-service without ticket queues).

## Architecture Expectations

A passing solution must integrate IaC, CI/CD, observability, and release engineering:

- **Bicep module library** — reusable modules for RG, App Service/AKS, Key Vault, App Insights
- **GitHub Actions OIDC** — federated credential to Azure, least-privilege RBAC per environment
- **CI/CD pipeline** — lint → what-if → deploy staging → approval → deploy prod
- **OpenTelemetry** — SDK in sample .NET app, export to App Insights or Grafana stack
- **Feature flags** — flag provider integration, kill-switch pattern, flag lifecycle
- **Environment strategy** — dev/staging/prod subscriptions or RGs with promotion flow
- **NFRs** — deployment frequency target, MTTR, change-failure rate (DORA metrics)
- **Mermaid platform diagram** — dev → CI → IaC → Azure → observability

## Deliverables

- [ ] **Bicep module repo** — at least 3 modules (networking, compute, observability)
- [ ] **GitHub Actions workflow** — OIDC auth, what-if, staged deploy with approval
- [ ] **OIDC setup doc** — Entra app registration, federated credential, RBAC roles
- [ ] **OpenTelemetry integration** — sample app with traces, metrics, logs correlation
- [ ] **Feature flag ADR** — provider choice, naming convention, retirement policy
- [ ] **ADR: Bicep vs Terraform** — for this organization's context
- [ ] **DORA metrics dashboard sketch** — what to measure and where
- [ ] **Platform onboarding guide** — how a new squad adopts the reference repo
- [ ] **Week 32 lab completion** — [lab-32-month8-capstone.md](../../weeks/week-32/labs/lab-32-month8-capstone.md)
- [ ] **Mermaid end-to-end platform diagram**

## Evaluation Rubric

| Criteria | Points |
|----------|--------|
| Requirements clarity | 20 |
| Architecture quality | 30 |
| Trade-off documentation | 20 |
| Production realism | 15 |
| Presentation / ADRs | 15 |

**Requirements clarity (20 pts)**

- Platform scope and squad onboarding path defined
- Security requirements (OIDC, no SP secrets) met
- DORA or equivalent ops metrics identified

**Architecture quality (30 pts)**

- Bicep modules are composable and parameterized
- CI pipeline enforces what-if before apply
- OTel signals correlate across deploy boundaries

**Trade-off documentation (20 pts)**

- IaC tool ADR considers team skills and Azure native fit
- Feature flag ADR covers blast radius and cleanup
- Environment promotion trade-offs documented

**Production realism (15 pts)**

- Least-privilege RBAC per environment
- Approval gates and rollback in pipeline
- Secret management never in workflow YAML

**Presentation / ADRs (15 pts)**

- Onboarding guide tested by peer squad simulation
- Platform diagram suitable for engineering all-hands
- Lab 32 artifacts linked and complete

**Pass:** ≥ 70 points

## Timeline

Suggested **2-week sprint** at end of Month 8:

| Day | Focus |
|-----|-------|
| **Mon W1** | Platform scope — modules, environments, squad onboarding |
| **Tue W1** | Bicep modules (networking, compute, observability) |
| **Wed W1** | GitHub Actions OIDC setup + federated credentials |
| **Thu W1** | CI pipeline — lint, what-if, staged deploy |
| **Fri W1** | OpenTelemetry in sample .NET app |
| **Mon W2** | Feature flags integration + ADR |
| **Tue W2** | ADR: Bicep vs Terraform; DORA dashboard sketch |
| **Wed W2** | Complete [Lab 32](../../weeks/week-32/labs/lab-32-month8-capstone.md) |
| **Thu W2** | Platform onboarding guide; peer squad walkthrough |
| **Fri W2** | Submit package; self-score against rubric |

## References

- [Week 29 — DevOps Culture & Practices](../../weeks/week-29/README.md)
- [Week 30 — CI/CD Pipelines](../../weeks/week-30/README.md)
- [Week 31 — Infrastructure as Code](../../weeks/week-31/README.md)
- [Week 32 — Observability & PowerShell](../../weeks/week-32/README.md)
- [Lab 32 — Month 8 Capstone](../../weeks/week-32/labs/lab-32-month8-capstone.md)

← [Phase overview](README.md) | [SYLLABUS](../../SYLLABUS.md)
