# DevOps Culture — Intermediate

> **Week 29** | Platform engineering, change management, compliance in CI/CD

## 1. Platform Engineering

Internal Developer Platform (IDP) components:

| Layer | Examples |
|-------|----------|
| Templates | .NET 8 API scaffold, Helm chart |
| Pipelines | Reusable GitHub Actions workflows |
| Environments | Ephemeral preview envs per PR |
| Docs | Backstage, internal wiki |
| Self-service | Request DB, namespace, Key Vault access |

**Architect KPI:** Time from `git clone` to deployed hello-world < 1 day.

---

## 2. Change Advisory Board (CAB) vs Continuous Delivery

| CAB Model | Continuous Delivery |
|-----------|---------------------|
| Weekly/monthly release windows | Deploy on merge |
| Manual approvals | Automated gates |
| Fits regulated industries | Fits SaaS |

**Hybrid:** Automated deploy to staging; CAB approval only for production promotion in regulated sectors. Feature flags decouple deploy from release.

---

## 3. Compliance in Pipelines

- **SOC 2 / ISO 27001:** Audit trail of who deployed what, when
- **Separation of duties:** Developer cannot approve own prod deploy
- **Immutable audit logs:** Pipeline run IDs linked to commit SHA
- **SBOM:** Software Bill of Materials for supply chain

```yaml
# GitHub environment protection rules
environment:
  name: production
  # Requires 2 reviewers, 30-min wait timer
```

---

## 4. Organizational Metrics Beyond DORA

| Metric | Meaning |
|--------|---------|
| **Developer satisfaction** | DX survey scores |
| **Toil reduction** | % time on manual ops |
| **Incident frequency** | Per service per month |
| **Cost per deploy** | CI minutes + infra |

**Next:** Week 30 CI/CD pipelines
