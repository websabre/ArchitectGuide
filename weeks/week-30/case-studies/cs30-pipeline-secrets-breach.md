# Case Study 30 — Pipeline Breach: Secrets in Git History

## Scenario

Security scan finds Azure connection string committed 6 months ago in `appsettings.json`. Repo is public fork of internal template. Credential was rotated once but remains in Git history.

## Your Role

Architect + incident lead. Board meeting in 48 hours.

## Timeline
- T+0: Secret detected by GitGuardian
- T+2h: Confirm scope — 12 repos forked from same template
- T+4h: Credential still valid for read-only storage account

## Tasks

1. **Immediate containment** — Rotate, revoke, audit access logs
2. **Pipeline fix** — OIDC federation, Key Vault references, pre-commit hooks
3. **Governance** — Secret scanning mandatory on all repos; policy as code
4. **Board communication** — Non-technical summary of risk and remediation

## Architecture Deliverables

- ADR: CI/CD authentication model (OIDC vs service principals)
- Updated pipeline template with `azure/login@v2` OIDC
- Runbook: secret leak response

## Discussion

- Why `git filter-repo` alone is insufficient
- How to prevent recurrence without blocking developer velocity
- Separation: build-time secrets vs runtime secrets (Managed Identity)
