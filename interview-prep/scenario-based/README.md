# Scenario-Based Architect Interview Questions

> Questions that test judgment, trade-offs, and production thinking — not trivia.

## Format

Each scenario presents a real-world situation. Answer using:
1. Clarifying questions you'd ask
2. Your recommendation
3. Trade-offs accepted
4. Risks and mitigations
5. How you'd measure success

---

## Sample Scenario 01: The Microservices Mandate

**Context:** Your CTO attended a conference and mandates "microservices everywhere" for the 15-year-old .NET monolith serving 2000 RPS with 99.9% uptime. Team of 20 developers. No Kubernetes experience.

**Question:** How do you respond?

**Model Answer Outline:**
- **Clarify:** What problem are we solving? (deployment frequency? scaling? team autonomy?)
- **Assess:** Current pain points — is the monolith actually the bottleneck?
- **Recommend:** Strangler fig, not big-bang. Start with one bounded context.
- **Trade-off:** Accept dual maintenance during migration; reject all-at-once rewrite
- **Risk:** Operational complexity of K8s without expertise → start with Azure App Service / Container Apps
- **Measure:** Deployment frequency, lead time, incident rate — DORA metrics
- **Influence:** Present ADR with data, not opinion. Propose 90-day pilot.

---

## Sample Scenario 02: The Cloud Bill Shock

**Context:** Azure bill jumped from $50K to $180K/month. CFO wants 40% reduction in 60 days without downtime.

**Question:** What's your action plan?

**Model Answer Outline:**
- **Week 1:** Cost analysis by resource, tag, and environment (Azure Cost Management)
- **Quick wins:** Dev/test environment scheduling, right-sizing VMs, reserved instances
- **Medium:** Storage tier optimization, unused resources cleanup
- **Architectural:** Review over-provisioned PaaS tiers, consider spot instances for batch
- **Governance:** Implement tagging policy, budget alerts, FinOps review cadence
- **Avoid:** Cutting redundancy that affects SLA

---

## Scenario Index (Planned)

| # | Scenario | Topic | Week |
|---|----------|-------|------|
| S01 | Microservices mandate | Architecture governance | 22 |
| S02 | Cloud bill shock | FinOps | 42 |
| S03 | Database outage during peak | DR/BCP | 42 |
| S04 | Security vulnerability in production | Security | 14 |
| S05 | Team wants to rewrite in Go | Technology decisions | 1 |
| S06 | Multi-cloud requirement from client | Multi-cloud | 20 |
| S07 | AI copilot data privacy concern | AI architecture | 39 |
| S08 | Legacy SOAP integration | Enterprise integration | 15 |
| S09 | Kubernetes vs PaaS debate | Platform decisions | 26 |
| S10 | Monorepo vs polyrepo | DevOps | 29 |

**Target:** 50+ scenario questions by Week 47.
