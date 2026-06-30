# Case Study 32 — Observability Gap During Multi-Region Failover

## Scenario

Primary region failed. Failover to secondary succeeded in 4 minutes (RTO met). However, dashboards showed "all green" — alerts didn't fire because health checks ran only in primary region.

## Impact
- 12 minutes before human noticed via customer support tickets
- No distributed traces across regions — couldn't pinpoint slow checkout
- SLO error budget consumed for the month in one incident

## Your Role

Redesign observability for active-passive multi-region .NET platform on Azure.

## Requirements

1. **Synthetic monitoring** — Probes from 3 geographic locations every 60s
2. **Cross-region traces** — Same Application Insights workspace or federated
3. **Alert routing** — PagerDuty with region dimension
4. **SLO dashboards** — Error budget burn rate alerts
5. **Runbooks** — Linked from every alert (PowerShell + Azure CLI steps)

## Design Exercise

Draw observability architecture:
- OpenTelemetry collector per region
- Centralized vs regional App Insights
- Log Analytics workspace strategy
- Cost vs visibility trade-off

## Rubric

| Criteria | Points |
|----------|--------|
| Multi-region alerting | 25 |
| Trace continuity | 25 |
| SLO/error budget design | 25 |
| Operational runbooks | 25 |
