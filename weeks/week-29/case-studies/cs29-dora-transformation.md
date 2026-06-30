# Case Study 29 — DORA Transformation at Legacy Bank

## Scenario

A 200-person .NET monolith team deploys quarterly via CAB. Change failure rate is 35%. MTTR is 8 hours. Leadership wants "DevOps" in 12 months.

## Your Role

Solution Architect — design the transformation roadmap without big-bang rewrite.

## Constraints
- Regulatory: production changes need audit trail
- 15-year-old .NET Framework app (partial .NET 8 strangler in progress)
- Ops team resistant to "developers deploying to prod"

## Discussion Points

1. **Baseline DORA metrics** — How do you measure today?
2. **Quick wins** — CI on every PR? Automated tests? Staging auto-deploy?
3. **Trunk-based adoption** — Pilot with one microservice first?
4. **Feature flags** — Decouple deploy from release for CAB comfort?
5. **Platform team** — Golden path pipeline for new .NET 8 services?
6. **12-month roadmap** — Phases with measurable targets

## Sample Architecture Decisions

| Quarter | Target | Action |
|---------|--------|--------|
| Q1 | CI on all PRs | GitHub Actions, SonarQube gate |
| Q2 | Weekly deploys (one service) | Strangler order-api to .NET 8 |
| Q3 | Daily deploys (3 services) | Feature flags, automated staging |
| Q4 | Elite DORA on new platform | 80% traffic on microservices |

## Rubric

| Criteria | Weight |
|----------|--------|
| Realistic phased plan | 30% |
| Addresses compliance | 25% |
| DORA metrics tied to actions | 25% |
| Change management (people) | 20% |
