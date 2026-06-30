# CI/CD — Intermediate: Multi-Service Pipelines

> **Week 30** | Monorepo vs polyrepo, matrix builds, environment promotion

## 1. Monorepo vs Polyrepo

| Factor | Monorepo | Polyrepo |
|--------|----------|----------|
| Shared libraries | Easy | Versioned NuGet packages |
| CI complexity | Path filters, affected builds | Per-repo pipeline |
| Ownership | Clear boundaries needed | Team owns repo |
| .NET fit | Nx-style affected detection | Common in enterprise |

**Architect:** Polyrepo for independent microservice teams. Monorepo for platform + shared libs with strong tooling.

---

## 2. Matrix Builds

```yaml
strategy:
  matrix:
    service: [order-api, payment-api, inventory-api]
steps:
  - run: dotnet test services/${{ matrix.service }}
```

**Affected-only builds:** Detect changed paths; skip unchanged services. Critical at 50+ microservices scale.

---

## 3. Environment Promotion

```
dev (auto) → staging (auto) → prod (approval + canary)
```

| Gate | Check |
|------|-------|
| Dev | Unit tests pass |
| Staging | Integration + contract tests |
| Prod | Manual approval OR automated canary metrics |

**Promotion artifact:** Same Docker image tag `1.2.3` promoted — never rebuild.

---

## 4. Database Migrations in CI/CD

| Strategy | Risk |
|----------|------|
| Run migration before deploy | App expects new schema |
| Expand-contract | Safest for zero-downtime |
| Flyway / EF migrations in pipeline | Automate with rollback plan |

**Architect rule:** Backward-compatible migrations only in rolling deployments.

---

## 5. Contract Testing in Pipeline

```yaml
- name: Pact verify
  run: dotnet test tests/OrderApi.ContractTests
```

Blocks deploy if consumer contract broken. Essential for 20+ service mesh.
