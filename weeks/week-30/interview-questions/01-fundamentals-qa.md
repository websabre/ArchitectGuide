# Week 30 — Fundamentals Interview Q&A

> Q001–Q030: Premium format (Week 1 quality).
> See also: [DevOps Top 50](../../../interview-prep/devops-top-50-index.md)

---


## Q001: CI/CD Pipeline Stages

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | CI/CD |
| **Frequency** | Very Common |

### Question

What stages should a production CI/CD pipeline include for a .NET 8 microservice?

### Short Answer (30 seconds)

Build, unit test, SAST/dependency scan, package immutable artifact, deploy dev, integration test, deploy staging, approval, deploy prod with health check. Same artifact promotes through all environments.

### Detailed Answer (3–5 minutes)

Fail fast at each gate. Typical timing: build 2m, test 3m, scan 2m, deploy staging 5m, integration 5m.

Architect principles: never rebuild for prod; parallelize security scan with tests; cache NuGet.

E2E tests run in staging nightly or pre-prod — not blocking every PR if >15 min.

### Architecture Perspective

Pipeline design reflects quality priorities — skipping integration tests means prod is your test env.

### Follow-up Questions

1. PR vs main pipeline? — PR: build+test only. Main: full deploy path.
2. Target CI time? — <15 min for PR feedback.

### Common Mistakes in Interviews

- Rebuilding per environment
- No security scan stage
- Manual deploy steps that should be automated

---

## Q002: GitHub Actions OIDC to Azure

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | GitHub Actions |
| **Frequency** | Very Common |

### Question

How does OIDC federation work between GitHub Actions and Azure? Why prefer it over service principal secrets?

### Short Answer (30 seconds)

GitHub issues short-lived JWT; Entra validates federated credential trusting repo/environment; Azure token returned. No long-lived secret to leak or rotate.

### Detailed Answer (3–5 minutes)

Configure federated credential: issuer `token.actions.githubusercontent.com`, subject `repo:org/app:environment:production`.

Mandate OIDC for all new repos. Block `AZURE_CREDENTIALS` JSON pattern in platform lint rules.

### Architecture Perspective

Security baseline for cloud CI/CD — expected knowledge for senior architects.

### Follow-up Questions

1. AWS equivalent? — IAM OIDC trust to GitHub.
2. Self-hosted runners? — When VNet access to private resources required.

### Common Mistakes in Interviews

- Long-lived SP secrets in GitHub
- Federated credential scoped to entire org
- Running deploy on PR to production

---

## Q003: App Service Deployment Slots

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Deployment Strategy |
| **Frequency** | Common |

### Question

How do Azure App Service deployment slots enable blue-green deployment for .NET APIs?

### Short Answer (30 seconds)

Deploy to staging slot, warm up, run health checks including DB, swap with production. Instant rollback by swapping back. Slots share App Service Plan.

### Detailed Answer (3–5 minutes)

Slot config: `WEBSITE_SWAP_WARMUP_PING_PATH=/health`. Health check must validate SQL and Redis — not just `return Ok()`.

Pair with backward-compatible EF migrations — expand before deploy, contract after all instances on new version.

### Architecture Perspective

Blue-green at PaaS layer without Kubernetes complexity — right choice for many .NET APIs.

### Follow-up Questions

1. SignalR/WebSockets? — Drain connections before swap.
2. Cost? — Staging slot on same plan shares compute.

### Common Mistakes in Interviews

- Swap without health check
- Breaking DB migration with slot swap
- Health check without dependency validation

---

## Q004: Blue-Green vs Canary vs Rolling

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Deployment Strategy |
| **Frequency** | Very Common |

### Question

Compare deployment strategies for a high-traffic .NET order API.

### Short Answer (30 seconds)

Rolling for low-risk stateless updates. Blue-green (slots) for instant swap. Canary when high-risk — route 5% traffic, monitor 5xx and p99, auto-rollback on breach.

### Detailed Answer (3–5 minutes)

| Strategy | Rollback | Risk |
|----------|----------|------|
| Rolling | Slow | Medium |
| Blue-green | Instant swap | Low |
| Canary | Stop traffic shift | Lowest |

AKS: rolling default, Argo Rollouts for canary.

### Architecture Perspective

Strategy is risk management — justify choice with failure blast radius.

### Follow-up Questions

1. Canary metrics? — 5xx rate, p99 latency, business conversion.
2. Database? — Expand-contract required for all except recreate.

### Common Mistakes in Interviews

- Canary without automated rollback
- Blue-green ignoring schema compatibility
- Recreate deploy in production

---

## Q005: Build Once Deploy Many

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Artifacts |
| **Frequency** | Common |

### Question

Why must the same artifact promote through dev, staging, and production?

### Short Answer (30 seconds)

Rebuild introduces non-determinism — different NuGet resolution, wrong build config. What you tested is not what you ship. Audit trail breaks.

### Detailed Answer (3–5 minutes)

Flow: commit abc123 → `order-api:1.2.3` in ACR → same tag to staging and prod.

Never `dotnet publish` on production VM. Config per environment via App Settings and Key Vault — not recompile.

### Architecture Perspective

Supply chain integrity — connects SLSA, SBOM, and compliance audits.

### Follow-up Questions

1. latest tag? — Anti-pattern in production; use semver + git SHA label.
2. Config differences? — Outside artifact via Key Vault references.

### Common Mistakes in Interviews

- Rebuilding on prod server
- Different binaries in staging vs prod
- Cannot answer what code is in prod

---

## Q006: Secret Management in Pipelines

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Security |
| **Frequency** | Common |

### Question

How should secrets be managed in CI/CD for .NET on Azure?

### Short Answer (30 seconds)

OIDC for CI auth. Runtime secrets in Key Vault via Managed Identity. Build-time tokens in GitHub Environments scoped to environment. Never commit appsettings with secrets.

### Detailed Answer (3–5 minutes)

Pre-commit hooks + GitGuardian on all repos. Rotate immediately on any leak suspicion — `git filter-repo` does not eliminate exposure if key was public.

### Architecture Perspective

Golden path templates make secure path the easy path.

### Follow-up Questions

1. Secrets in ARM/Bicep? — Reference Key Vault secrets, never plain text.
2. CI access to Key Vault? — Separate OIDC scope for deploy-time only.

### Common Mistakes in Interviews

- Connection strings in App Service plain text
- Shared secrets across environments
- Secrets echoed in pipeline logs

---

## Q007: SAST and Dependency Scanning

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DevSecOps |
| **Frequency** | Common |

### Question

What security scanning belongs in a .NET CI pipeline?

### Short Answer (30 seconds)

Dependabot/Snyk for CVEs, CodeQL/SonarQube for SAST, GitGuardian for secrets, Trivy for containers. Gate on critical/high; medium to backlog.

### Detailed Answer (3–5 minutes)

Baseline existing debt — block new critical issues, not all historical. Parallelize scan with tests to avoid slowing CI.

### Architecture Perspective

DevSecOps shifts left — architects define non-negotiable gates.

### Follow-up Questions

1. DAST? — Staging nightly, not every PR.
2. Alert fatigue? — Severity-based gates only.

### Common Mistakes in Interviews

- No scanning because slow
- Blocking on informational findings
- No baseline for legacy debt

---

## Q008: Contract Testing with Pact

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Testing |
| **Frequency** | Common |

### Question

How does Pact fit into microservices CI/CD?

### Short Answer (30 seconds)

Consumer defines contract; provider verifies in CI before deploy. Broken contract blocks merge — prevents integration failures across independent deploys.

### Detailed Answer (3–5 minutes)

Order API (consumer) publishes pact → broker → Payment API verifies on every PR.

Complements staging integration tests — faster, runs without full stack.

### Architecture Perspective

Contract tests are the safety net for independent deployment at scale.

### Follow-up Questions

1. Pact vs integration tests? — Pact is consumer-driven and faster.
2. Broker required? — Yes for sharing contracts across teams.

### Common Mistakes in Interviews

- Only staging integration tests
- No versioned contracts
- Skipping provider verification in CI

---

## Q009: Database Migrations in CD

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | CI/CD |
| **Frequency** | Common |

### Question

How do you run EF Core migrations in a zero-downtime pipeline?

### Short Answer (30 seconds)

Expand-contract pattern: backward-compatible migrations only. Run expand migration before app deploy. Contract phase after all instances on new code.

### Detailed Answer (3–5 minutes)

Pipeline order: migrate (expand) → deploy v2 (dual-write) → backfill → deploy v3 → migrate (contract).

Never breaking schema change with rolling deploy or slot swap.

### Architecture Perspective

Schema strategy constrains deployment strategy — architects align both.

### Follow-up Questions

1. Who approves prod migrations? — Automated for expand-only; manual for contract.
2. Rollback? — Tested forward-fix or down migration script.

### Common Mistakes in Interviews

- Migration after deploy with breaking change
- No rollback plan
- Manual migration on production server

---

## Q010: CI/CD Security Checklist

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Pipeline Security |
| **Frequency** | Common |

### Question

What security controls are non-negotiable in an enterprise CI/CD pipeline?

### Short Answer (30 seconds)

OIDC auth, branch protection, environment approval for prod, secret scanning, SAST, dependency CVE gate, signed artifacts, segregation of duties, immutable audit logs.

### Detailed Answer (3–5 minutes)

Architect sign-off checklist: no long-lived cloud credentials; CodeQL on every PR; Dependabot enabled; production reviewers configured; deployment linked to commit SHA; SBOM for containers.

### Architecture Perspective

Security checklist is architecture governance encoded in pipelines.

### Follow-up Questions

1. Self-hosted runner security? — Harden VM, rotate tokens, network isolate.
2. Supply chain? — Pin action versions to commit SHA.

### Common Mistakes in Interviews

- Security as optional stage
- Developer approves own production deploy
- Floating `@v4` action tags without pinning

---




## Q011: Pipeline as Code Principles

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | CI/CD |
| **Frequency** | Very Common |

### Question

Why must CI/CD pipelines be defined as code in version control?

### Short Answer (30 seconds)

Pipeline as code enables review, audit, rollback, and reproducibility. YAML in Git — not click-ops in UI — same PR process as application code.

### Detailed Answer (3–5 minutes)

**Benefits:**
- **Reviewability** — security team reviews pipeline changes
- **Auditability** — git blame on who added prod approval gate
- **Reproducibility** — branch builds use same pipeline definition
- **DR** — pipeline definition survives portal UI changes

**Implementation:** `.github/workflows/deploy.yml` or `azure-pipelines.yml` in repo. Reusable workflows in `.github/workflows/` shared org-wide.

**Architect:** Platform team owns reusable workflow library; product teams consume via `uses:` reference.

### Architecture Perspective

Pipeline as code is governance foundation for enterprise CI/CD.

### Follow-up Questions

1. **UI-defined pipelines? — Acceptable for spike; migrate to code before production.**
2. **Pipeline versioning? — Pin reusable workflow to tag or SHA — not `@main`.**

### Common Mistakes in Interviews

- Production pipeline only configurable in portal UI
- No PR review on pipeline YAML changes
- Different pipeline definition per environment ad hoc

---

## Q012: Reusable GitHub Actions Workflows

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | GitHub Actions |
| **Frequency** | Very Common |

### Question

How do you design reusable workflows for .NET microservices across 20 repos?

### Short Answer (30 seconds)

Central `org-actions` repo with `dotnet-build.yml`, `dotnet-deploy-azure.yml`. Caller passes inputs: `serviceName`, `environment`, `projectPath`. OIDC auth baked into reusable workflow.

### Detailed Answer (3–5 minutes)

**Pattern:**
```yaml
jobs:
  deploy:
    uses: org/actions/.github/workflows/dotnet-deploy.yml@v2
    with:
      service-name: order-api
      environment: production
    secrets: inherit
```

**Design rules:**
- Inputs for variation; secrets via `secrets: inherit` or explicit mapping
- Version reusable workflows with tags (`@v2`)
- Document required inputs in README

**Architect:** One security fix in reusable workflow patches 20 repos on version bump.

### Architecture Perspective

Reusable workflows are IDP core — encode org standards once.

### Follow-up Questions

1. **Composite actions vs reusable workflows? — Composites for steps bundle; workflows for full job orchestration.**
2. **Breaking change? — Major version tag + migration guide.**

### Common Mistakes in Interviews

- Copy-paste 200-line workflow per repo
- Reusable workflow pinned to `@main`
- Each team invents different OIDC configuration

---

## Q013: Environment Promotion Gates

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | CI/CD |
| **Frequency** | Very Common |

### Question

Design environment promotion gates from dev through production for a .NET API.

### Short Answer (30 seconds)

Same artifact promotes: dev (auto) → staging (auto + integration tests) → prod (manual approval + smoke tests). Gates block on test failure, scan critical CVE, or missing approval.

### Detailed Answer (3–5 minutes)

**Gate types:**
- **Automated:** unit test pass, SAST clean, integration test pass
- **Manual:** prod approval from on-call lead + change ticket
- **Temporal:** no Friday prod deploy without exec approval

**Azure DevOps:** `environment` resources with checks. **GitHub:** `environment: production` with required reviewers.

**Architect:** Never rebuild artifact at prod gate — promote immutable `order-api:1.2.3+abc123` tag.

### Architecture Perspective

Promotion gates encode risk management in pipeline — architect defines gate policy.

### Follow-up Questions

1. **Skip staging? — Only for low-risk internal tools — document exception.**
2. **Gate bypass? — Break-glass role with mandatory post-incident review.**

### Common Mistakes in Interviews

- Rebuild on production promotion
- Staging gate skipped for 'hotfix'
- No smoke test after prod deploy

---

## Q014: Immutable Artifacts in ACR

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Artifacts |
| **Frequency** | Very Common |

### Question

How do you manage immutable container artifacts in Azure Container Registry?

### Short Answer (30 seconds)

Build once, push image with semver + git SHA tag. Enable ACR retention policies and content trust. Prod deploy references digest not `latest`.

### Detailed Answer (3–5 minutes)

**Tagging strategy:**
- `order-api:1.4.2` — semver release
- `order-api:1.4.2+abc1234` — traceable to commit
- `order-api:sha-abc1234` — immutable fallback

**ACR practices:**
- Geo-replication for prod pulls
- Quarantine policy for unscanned images
- Retention: keep last 10 semver tags per repo

**Architect:** Artifact digest in deployment audit log — proves exact bits in prod.

### Architecture Perspective

Immutable artifacts are supply chain foundation — connects to SLSA and SBOM.

### Follow-up Questions

1. **latest tag in prod? — Anti-pattern — impossible rollback to known version.**
2. **Mutate image after push? — Violates immutability — rebuild and retag.**

### Common Mistakes in Interviews

- Production deploys `latest` tag
- Different image built for staging vs prod
- No artifact-to-commit traceability

---

## Q015: Semantic Versioning in CI/CD

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Release Management |
| **Frequency** | Common |

### Question

How does semantic versioning integrate with automated CI/CD for .NET APIs?

### Short Answer (30 seconds)

MAJOR.MINOR.PATCH: breaking change bumps major, feature bumps minor, fix bumps patch. GitVersion or MinVer calculates from conventional commits on main.

### Detailed Answer (3–5 minutes)

**Pipeline flow:**
1. Conventional commit on PR (`feat:`, `fix:`, `BREAKING CHANGE:`)
2. GitVersion on main computes `1.5.0`
3. Build tags Docker image and NuGet package `1.5.0`
4. Git tag `v1.5.0` created automatically

**Consumer impact:** NuGet clients pin major; internal APIs use contract tests for minor bumps.

**Architect:** Document semver policy in ADR — when major bump required for API changes.

### Architecture Perspective

Semver communicates breaking change risk to consumers — architect enforces on public APIs.

### Follow-up Questions

1. **Calendar versioning? — Acceptable for SaaS with no library consumers — document choice.**
2. **0.x semver? — Unstable API — anything may break.**

### Common Mistakes in Interviews

- Manual version bump forgotten in release rush
- Breaking API change as patch bump
- No conventional commit discipline

---

## Q016: Rollback Strategies in Production

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Deployment Strategy |
| **Frequency** | Very Common |

### Question

Compare rollback strategies when a .NET API deploy causes elevated 5xx errors.

### Short Answer (30 seconds)

App Service slot swap back (instant), redeploy previous artifact digest (minutes), feature flag disable (seconds for logic), database forward-fix (slowest — avoid).

### Detailed Answer (3–5 minutes)

**Decision tree:**
1. **Feature flag** — if new code path flagged → disable flag first
2. **Slot swap** — if binary regression → swap staging/previous slot
3. **Artifact redeploy** — pin previous digest in pipeline
4. **DB rollback** — last resort; expand-contract should make rare

**Automation:** Pipeline monitors 5xx for 10 min post-deploy; auto-swap on breach.

**Architect:** Rollback must be tested quarterly — untested rollback is wishful thinking.

### Architecture Perspective

Rollback strategy is architecture requirement — design deploy for reversibility.

### Follow-up Questions

1. **Blue-green vs rolling rollback? — Blue-green instant; rolling must drain connections.**
2. **Canary rollback? — Stop traffic shift — previous version still serving majority.**

### Common Mistakes in Interviews

- Only rollback plan is restore database backup
- Breaking migration deployed with rolling update
- Rollback never tested in staging

---

## Q017: Smoke Tests Post-Deploy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Testing |
| **Frequency** | Common |

### Question

What smoke tests run immediately after production deployment?

### Short Answer (30 seconds)

Critical path HTTP checks: `/health` with dependency validation, `POST /auth/token`, `GET /orders/{knownId}` — 60 seconds total, fail triggers auto-rollback.

### Detailed Answer (3–5 minutes)

**Smoke test design:**
- Run against prod URL from pipeline (not internal only)
- Validate DB connectivity in health endpoint
- Use test account with synthetic data
- Idempotent — safe to re-run

**Not smoke tests:** Full regression suite (staging), load tests (separate job).

**Example:**
```bash
curl -f https://api.contoso.com/health
curl -f -X POST https://api.contoso.com/api/v1/orders/smoke-test
```

**Architect:** Smoke tests are deployment gate — define in platform reusable workflow.

### Architecture Perspective

Smoke tests catch 'deploy succeeded but app broken' — common with config errors.

### Follow-up Questions

1. **Health check returns 200 without DB? — False positive — validate dependencies.**
2. **Synthetic vs smoke? — Smoke is post-deploy gate; synthetic is continuous probe.**

### Common Mistakes in Interviews

- No post-deploy verification
- Health endpoint always returns Ok()
- 15-minute E2E suite blocking every deploy

---

## Q018: Integration Test Pyramid in Pipelines

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Testing |
| **Frequency** | Very Common |

### Question

Where do integration tests sit in the test pyramid for CI/CD pipeline design?

### Short Answer (30 seconds)

Many unit tests (fast, PR gate), fewer integration tests (Testcontainers SQL/Redis, main branch gate), minimal E2E (staging/nightly). Integration tests validate real dependencies without full stack.

### Detailed Answer (3–5 minutes)

**Pipeline placement:**
- **PR:** unit + contract tests (< 10 min)
- **Main:** + integration with Testcontainers (< 20 min)
- **Staging:** E2E Playwright against deployed env (nightly or pre-prod gate)

**.NET:** `WebApplicationFactory` + Testcontainers for SQL. Don't hit prod dependencies from CI.

**Architect:** Integration test failures blocking main — not PR if slow — balance feedback speed vs coverage.

### Architecture Perspective

Test pyramid placement affects CI duration and CFR — architects own the strategy.

### Follow-up Questions

1. **Integration vs E2E? — Integration tests service with real DB; E2E tests user journey across services.**
2. **Flaky integration tests? — Quarantine and fix — don't disable category entirely.**

### Common Mistakes in Interviews

- E2E tests on every PR blocking 45 minutes
- No integration tests — only unit mocks
- Integration tests hitting production APIs

---

## Q019: E2E Test Placement Strategy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Testing |
| **Frequency** | Common |

### Question

When should E2E tests block deployment vs run asynchronously?

### Short Answer (30 seconds)

E2E blocks staging promotion if < 15 min and stable. Nightly E2E for full regression. Never block PR with 30-test Playwright suite — feedback too slow.

### Detailed Answer (3–5 minutes)

**Tiers:**
1. **Deploy gate (staging):** 5–10 critical journey tests (login, checkout)
2. **Nightly:** full regression 200+ scenarios
3. **Pre-release:** manual exploratory + automated full suite

**Flake management:** Retry once, quarantine chronic flakes, root cause fix required.

**Architect:** E2E tests user-visible contracts — fewer but high signal. Complement with contract tests for service boundaries.

### Architecture Perspective

E2E placement is trade-off between speed and confidence — document policy.

### Follow-up Questions

1. **Playwright in CI? — Containerized browsers, parallel shards, trace on failure.**
2. **E2E data setup? — Seed test tenant — never prod data.**

### Common Mistakes in Interviews

- 200 E2E tests blocking every commit
- Zero E2E — prod is test environment
- Flaky tests ignored with `@Ignore`

---

## Q020: Pipeline Parallelism

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | CI/CD |
| **Frequency** | Common |

### Question

How do you parallelize a .NET CI pipeline without wasting agent minutes?

### Short Answer (30 seconds)

Matrix builds per project, parallel jobs for test/scan/build, fan-in before deploy. Use `needs:` DAG — don't serialize independent stages.

### Detailed Answer (3–5 minutes)

**Patterns:**
```yaml
jobs:
  test:
    strategy:
      matrix:
        project: [Order.Api, Payment.Api, Catalog.Api]
  security-scan:
    runs-on: ubuntu-latest  # parallel with test
  deploy:
    needs: [test, security-scan]
```

**Limits:** Agent pool concurrency caps — prioritize PR feedback over nightly jobs.

**Architect:** Parallelism reduces lead time — a DORA lever — but costs compute; right-size pools.

### Architecture Perspective

Parallelism directly attacks lead time — measure p95 pipeline duration.

### Follow-up Questions

1. **Over-parallelization? — NuGet restore per job — use cache or shared artifact.**
2. **Self-hosted parallelism? — Scale runner pool based on queue depth.**

### Common Mistakes in Interviews

- Fully serial pipeline 45 minutes
- Matrix 50 projects on every doc change
- Parallel deploys to same environment

---

## Q021: NuGet Cache Strategies in CI

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | CI/CD |
| **Frequency** | Common |

### Question

How do you cache NuGet packages in GitHub Actions for faster .NET builds?

### Short Answer (30 seconds)

Use `actions/cache` keyed on `**/packages.lock.json` or `**/*.csproj` hash. Enable lock files in SDK-style projects for deterministic restore.

### Detailed Answer (3–5 minutes)

**GitHub Actions:**
```yaml
- uses: actions/cache@v4
  with:
    path: ~/.nuget/packages
    key: nuget-${{ hashFiles('**/packages.lock.json') }}
```

**Azure DevOps:** Pipeline cache task with same key pattern.

**Also cache:** `~/.dotnet/tool` for dotnet-ef, GitVersion.

**Measure:** Restore drops from 90s to 8s — meaningful lead time improvement at scale.

### Architecture Perspective

Caching is low-effort lead time win — platform templates should include by default.

### Follow-up Questions

1. **Cache poisoning? — Key on lock file hash — invalidate on dependency change.**
2. **Azure Artifacts feed? — Cache + upstream proxy reduces public NuGet hits.**

### Common Mistakes in Interviews

- No cache — full restore every build
- Cache key `nuget` never invalidated
- Committing packages folder to git

---

## Q022: Self-Hosted Runners Trade-offs

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | CI/CD |
| **Frequency** | Common |

### Question

When do you use self-hosted GitHub Actions runners vs GitHub-hosted?

### Short Answer (30 seconds)

Self-hosted when: VNet access to private SQL/AKS, larger machines for build, compliance data residency, or GPU builds. GitHub-hosted for default OSS-style isolation and zero maintenance.

### Detailed Answer (3–5 minutes)

**Self-hosted requirements:**
- Hardened VM image, auto-patching
- Ephemeral runners preferred (one job per VM)
- Network isolate — runners not on corp desktop
- OIDC to Azure — no persistent SP on runner disk

**Risks:** Compromised runner accesses internal network — treat as production asset.

**Architect:** Platform team operates runner scale set with Terraform/Bicep — not developer laptops.

### Architecture Perspective

Runner choice is security and networking architecture decision.

### Follow-up Questions

1. **Azure DevOps agents? — Same trade-offs — Microsoft-hosted vs self-hosted VMSS.**
2. **Runner autoscaling? — Queue depth triggers scale out.**

### Common Mistakes in Interviews

- Developer laptop as production deploy runner
- Long-lived secrets on self-hosted runner
- Self-hosted without patching cadence

---

## Q023: Deployment Approvals Design

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Governance |
| **Frequency** | Common |

### Question

Design deployment approval workflow for production with segregation of duties.

### Short Answer (30 seconds)

PR author cannot approve prod deploy. Minimum 1 reviewer from on-call rotation + automated gate pass. Emergency break-glass with audit.

### Detailed Answer (3–5 minutes)

**Layers:**
1. Automated: tests, scans, smoke staging
2. Manual: environment protection rule — 1 of 2 on-call leads
3. Optional: change ticket ID required in deploy input

**GitHub Environments:** `required_reviewers`, `wait_timer` 5 min for cancel window.

**SOC 2:** Demonstrate deployer ≠ approver in audit export.

### Architecture Perspective

Approval design satisfies compliance without weekly CAB for every deploy.

### Follow-up Questions

1. **Same person codes and approves prod? — Violation for regulated workloads.**
2. **Approval fatigue? — Standard changes pre-approved via policy.**

### Common Mistakes in Interviews

- Developer self-approves production
- Manual approval with no automated gates
- Approval required but no on-call rotation defined

---

## Q024: GitHub Environments Configuration

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | GitHub Actions |
| **Frequency** | Common |

### Question

How do GitHub Environments enforce deployment policy for production?

### Short Answer (30 seconds)

Create `production` environment with required reviewers, branch restriction (`main` only), secrets scoped to environment, deployment branch policies.

### Detailed Answer (3–5 minutes)

**Configuration:**
- **Protection rules:** 2 required reviewers, 5-minute wait timer
- **Secrets:** `AZURE_CLIENT_ID` prod-only — not available on PR workflows
- **Deployment branches:** `main` and `release/*` only
- **OIDC:** Federated credential subject includes `environment:production`

**Workflow:**
```yaml
environment: production
```

**Architect:** Environment-scoped OIDC limits blast radius of compromised workflow.

### Architecture Perspective

GitHub Environments implement least-privilege deploy credentials.

### Follow-up Questions

1. **Environment vs repository secrets? — Environment secrets only exposed during protected deploy job.**
2. **Preview environments? — `pull_request` environment auto-created — destroy on close.**

### Common Mistakes in Interviews

- Production secrets available on PR workflows
- No branch restriction on production environment
- OIDC federated credential trusts entire org

---

## Q025: Azure DevOps Multi-Stage YAML

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Azure DevOps |
| **Frequency** | Common |

### Question

Structure a multi-stage Azure DevOps pipeline for .NET with dev, staging, and prod.

### Short Answer (30 seconds)

Stages: Build → DeployDev → TestIntegration → DeployStaging → Approval → DeployProd. `dependsOn` chains stages; `deployment` jobs target environments.

### Detailed Answer (3–5 minutes)

**Template:**
```yaml
stages:
- stage: Build
  jobs: [build, test, publish artifact]
- stage: DeployStaging
  dependsOn: Build
  jobs:
  - deployment: Deploy
    environment: staging
- stage: DeployProd
  dependsOn: DeployStaging
  jobs:
  - deployment: Deploy
    environment: production
```

**Artifacts:** `PublishPipelineArtifact` — same package all stages.

**Architect:** ADO environments parallel GitHub Environments — unified policy across orgs if multi-VCS.

### Architecture Perspective

Multi-stage YAML is Azure-native promotion model — know syntax for interviews.

### Follow-up Questions

1. **Stage vs job parallelism? — Stages sequential by default; parallel stages with `dependsOn: []`.**
2. **Template repositories? — Extend shared pipeline template for DRY.**

### Common Mistakes in Interviews

- Single stage build and deploy prod
- Rebuild in DeployProd stage
- No environment checks on production stage

---

## Q026: Container Image Scanning with Trivy

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | DevSecOps |
| **Frequency** | Common |

### Question

How do you integrate Trivy container scanning into a .NET Docker build pipeline?

### Short Answer (30 seconds)

Scan image after `docker build`, before push to ACR. Gate on CRITICAL/HIGH CVEs; export SARIF to GitHub Security tab.

### Detailed Answer (3–5 minutes)

**Pipeline step:**
```yaml
- uses: aquasecurity/trivy-action@master
  with:
    image-ref: order-api:${{ github.sha }}
    severity: CRITICAL,HIGH
    exit-code: 1
```

**Policy:** Block new critical; grandfather existing with expiry ticket. Base image updates via Dependabot Dockerfile PRs.

**Architect:** Scanning is shift-left — cheaper than runtime breach.

### Architecture Perspective

Container scanning is non-negotiable gate for production images.

### Follow-up Questions

1. **Trivy vs Defender? — Trivy in CI; Defender for runtime — complementary.**
2. **False positives? — VEX document accepted risk with expiry.**

### Common Mistakes in Interviews

- Push to ACR before scan
- Scan disabled for 'speed'
- No base image update process

---

## Q027: SBOM Generation in CI

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Supply Chain |
| **Frequency** | Common |

### Question

What is an SBOM and how do you generate one for .NET container images?

### Short Answer (30 seconds)

Software Bill of Materials lists all components and versions. Generate with Syft or `dotnet sbom`, attach to release artifact and ACR metadata for incident CVE response.

### Detailed Answer (3–5 minutes)

**Generation:**
```bash
syft order-api:1.2.3 -o spdx-json > sbom.spdx.json
```

**Storage:** Attach to GitHub release, upload to dependency track, link in deployment audit.

**Incident use:** Log4Shell-style — query SBOM for affected library versions across fleet in minutes not weeks.

**Architect:** SBOM mandatory for regulated customers — encode in golden path.

### Architecture Perspective

SBOM enables fleet-wide vulnerability response — supply chain architecture.

### Follow-up Questions

1. **SPDX vs CycloneDX? — Both accepted — pick one org standard.**
2. **NuGet SBOM? — `dotnet sbom` for managed dependencies inside image.**

### Common Mistakes in Interviews

- No component inventory during CVE crisis
- SBOM generated but not stored with release
- Assuming Dockerfile alone documents all deps

---

## Q028: SLSA Supply Chain Levels

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Supply Chain |
| **Frequency** | Common |

### Question

Explain SLSA levels and what your .NET CI/CD pipeline needs for SLSA Build Level 3.

### Short Answer (30 seconds)

SLSA (Supply-chain Levels for Software Artifacts) L3: non-falsifiable provenance, isolated build, signed provenance. GitHub OIDC + attestations + pinned actions moves toward L3.

### Detailed Answer (3–5 minutes)

**Requirements L3:**
- Build platform generates provenance (not modifiable by build)
- Ephemeral isolated build environment
- Provenance signed and verifiable

**Practices:**
- Pin GitHub Actions to commit SHA
- OIDC federation — no long-lived secrets
- `slsa-github-generator` for provenance attestation
- Hermetic builds — lock files, no network in compile if possible

**Architect:** Present SLSA roadmap to security — incremental not binary.

### Architecture Perspective

SLSA frames supply chain maturity — architects speak levels not buzzwords.

### Follow-up Questions

1. **Sigstore cosign? — Sign container images — complements SLSA provenance.**
2. **L4 realistic? — Hermetic reproducible builds — aspirational for most .NET shops.**

### Common Mistakes in Interviews

- Floating action tags `@v4`
- No build provenance attestation
- Developer laptop builds production artifacts

---

## Q029: Pipeline Secrets Rotation

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | Security |
| **Frequency** | Common |

### Question

How do you rotate CI/CD secrets without breaking deployments?

### Short Answer (30 seconds)

Prefer OIDC over secrets. For remaining secrets: dual-credential overlap window, rotate in Key Vault, update GitHub secret, verify deploy, revoke old.

### Detailed Answer (3–5 minutes)

**Rotation playbook:**
1. Generate new secret in Key Vault
2. Add as `SECRET_V2` in GitHub environment
3. Update workflow to prefer V2
4. Successful prod deploy → remove V1
5. Audit log rotation event

**OIDC migration:** Eliminate `AZURE_CREDENTIALS` JSON — federated credential only.

**Schedule:** 90-day rotation for any remaining PATs; immediate on leak suspicion.

### Architecture Perspective

Secrets rotation is operational requirement — OIDC reduces rotation burden.

### Follow-up Questions

1. **Key Vault reference in App Service? — Runtime secret separate from CI secret.**
2. **GitGuardian alert? — Rotate immediately — assume compromise.**

### Common Mistakes in Interviews

- Never rotated GitHub SP secret since 2019
- Rotation without dual-credential overlap
- Secrets in workflow YAML encoded base64

---

## Q030: Failed Deploy Auto-Rollback

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Fundamentals |
| **Category** | CI/CD |
| **Frequency** | Common |

### Question

Implement automatic rollback when post-deploy metrics breach SLO.

### Short Answer (30 seconds)

Pipeline deploys → monitors App Insights 5xx rate and p99 for 10 min → if threshold breached, swap slot back or redeploy previous digest → page on-call with incident.

### Detailed Answer (3–5 minutes)

**Implementation options:**
- **App Service:** Swap slots via Azure CLI in pipeline
- **AKS:** Argo Rollouts automatic promotion abort
- **GitHub Actions:** Custom step querying metrics API

**Thresholds:** 5xx > 1% for 5 min OR p99 > 2× baseline.

**Architect:** Auto-rollback requires health signal quality — bad metric causes false rollback.

### Architecture Perspective

Auto-rollback improves MTTR — DORA metric — but needs tuning.

### Follow-up Questions

1. **Rollback during intentional load test? — Suppress auto-rollback with pipeline flag.**
2. **Metric source? — User-facing synthetic + server 5xx — not CPU alone.**

### Common Mistakes in Interviews

- Manual rollback only — 45 min MTTR
- Auto-rollback on single failed health check
- No previous artifact retained for rollback

---
