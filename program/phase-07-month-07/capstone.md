# Month 7 Capstone — Deploy .NET to AKS with GitOps

> **Phase 7** | Complete after weeks in this month.

## Brief

Containerize microservice, deploy AKS, configure HPA and ingress.

## Scenario

**CloudNative Retail** is moving its **Order Service** (.NET 8) from App Service to **Azure Kubernetes Service** to support custom autoscaling and GitOps delivery. The platform team has provisioned a non-production AKS cluster; your squad owns the first production-grade workload. Constraints: images must be non-root, secrets via Azure Key Vault CSI driver, and all cluster changes via Git (Argo CD or Flux). Stakeholders include platform engineering (cluster policies), security (Pod Security Standards), and SRE (SLO-based HPA). You are delivering the container, Kubernetes manifests, and GitOps pipeline for architecture sign-off.

## Architecture Expectations

A passing solution must show production Kubernetes operations knowledge:

- **Multi-stage Dockerfile** — build, publish, runtime; non-root user; minimal base image
- **Kubernetes manifests or Helm chart** — Deployment, Service, Ingress, ConfigMap, Secret references
- **HPA configuration** — CPU/memory or custom metrics; min/max replicas justified
- **Ingress / Gateway API** — TLS termination, path routing, rate-limit annotation if applicable
- **GitOps repo layout** — app repo vs platform repo separation
- **Observability** — liveness/readiness probes, resource requests/limits, OTel sidecar or agent
- **NFRs** — rollout strategy (rolling vs blue/green), PDB, cluster autoscaling interaction
- **Mermaid CI/CD + GitOps flow** — commit → build → push → sync → deploy

## Deliverables

- [ ] **Multi-stage Dockerfile** — with comments on layer caching and security
- [ ] **Helm chart or Kustomize overlays** — base + dev/staging/prod
- [ ] **HPA manifest** — metric targets and replica bounds documented
- [ ] **Ingress manifest** — TLS, host rules, backend service mapping
- [ ] **GitOps repo structure** — Argo CD Application or Flux Kustomization
- [ ] **ADR: Helm vs raw manifests** — team maintainability rationale
- [ ] **ADR: Argo CD vs Flux** — if both studied, justify choice
- [ ] **Runbook outline** — deploy, rollback, scale, debug pod failure
- [ ] **Mermaid pipeline diagram** — CI build → ACR → GitOps sync → AKS
- [ ] **Argo CD or Flux sync demo** — screenshot or recorded steps in README

## Evaluation Rubric

| Criteria | Points |
|----------|--------|
| Requirements clarity | 20 |
| Architecture quality | 30 |
| Trade-off documentation | 20 |
| Production realism | 15 |
| Presentation / ADRs | 15 |

**Requirements clarity (20 pts)**

- Workload resource profile estimated (CPU, memory, replicas)
- Environment promotion path (dev → staging → prod) defined
- Security constraints (non-root, secrets) explicit

**Architecture quality (30 pts)**

- Dockerfile follows best practices (multi-stage, slim runtime)
- Probes, limits, and HPA align with actual service behavior
- GitOps drift detection and sync policy configured

**Trade-off documentation (20 pts)**

- Helm/Kustomize ADR considers team skill and chart reuse
- GitOps tool ADR covers multi-cluster future
- Rollout strategy trade-offs documented

**Production realism (15 pts)**

- Key Vault CSI or equivalent secret injection
- PDB and anti-affinity for availability
- Rollback procedure tested or documented

**Presentation / ADRs (15 pts)**

- Demo or screenshots prove sync works
- Platform team review checklist completed
- Runbook covers on-call scenarios

**Pass:** ≥ 70 points

## Timeline

Suggested **2-week sprint** at end of Month 7:

| Day | Focus |
|-----|-------|
| **Mon W1** | Resource profiling — CPU/memory, replica bounds |
| **Tue W1** | Multi-stage Dockerfile + local container test |
| **Wed W1** | Kubernetes manifests — Deployment, Service, probes |
| **Thu W1** | HPA + Ingress configuration |
| **Fri W1** | GitOps repo scaffold — Argo CD or Flux |
| **Mon W2** | Key Vault CSI secrets; ADR: Helm vs manifests |
| **Tue W2** | ADR: GitOps tool; pipeline diagram |
| **Wed W2** | Deploy to AKS; verify HPA scale event |
| **Thu W2** | Runbook + rollback test |
| **Fri W2** | Submit package; self-score against rubric |

## References

- [Week 25 — Docker & Container Architecture](../../weeks/week-25/README.md)
- [Week 26 — Kubernetes Fundamentals](../../weeks/week-26/README.md)
- [Week 27 — Kubernetes Advanced & Production](../../weeks/week-27/README.md)
- [Week 28 — Linux for Architects](../../weeks/week-28/README.md)

← [Phase overview](README.md) | [SYLLABUS](../../SYLLABUS.md)
