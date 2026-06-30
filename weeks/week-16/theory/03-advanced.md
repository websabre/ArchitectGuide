# Azure Production Capstone — Advanced Review

> **Week 16** | **Level:** Advanced

## Production Readiness Review

### SLA Math

- App Service 99.95% ≈ 22 min downtime/month
- Multi-region active-active for 99.99%+
- Document dependency chain — weakest link sets SLA

### DR Runbook Outline

1. Detection (alert threshold)
2. Decision (failover criteria)
3. Execution (DNS, traffic manager)
4. Validation (synthetic tests)
5. Communication (status page, stakeholders)

### Interview Presentation (10 min)

1. Problem & requirements (2 min)
2. Architecture diagram walkthrough (4 min)
3. Key trade-offs & ADRs (3 min)
4. What you'd do with 6 more months (1 min)

**Month 4 capstone:** [program/phase-04](../../../program/phase-04-month-04/capstone.md)
