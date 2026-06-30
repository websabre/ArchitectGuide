#!/usr/bin/env python3
"""Generate _banks_data_29_36_extra.py with 480 premium Q&A tuples."""

import textwrap
from pathlib import Path

OUTPUT = Path(__file__).parent / "_banks_data_29_36_extra.py"


def T(title, category, freq, question, short, detailed, perspective, fu1, fu2, m1, m2, m3):
    return (title, category, freq, question, short, detailed, perspective, fu1, fu2, m1, m2, m3)


def fmt_tuple(t):
    lines = ["    ("]
    for i, field in enumerate(t):
        comma = "," if i < len(t) - 1 else ","
        if "\n" in field or len(field) > 72:
            lines.append(f'     {field!r}{comma}')
        else:
            lines.append(f'     {field!r}{comma}')
    lines.append("    ),")
    return "\n".join(lines)


def write_list(name, items):
    out = [f"{name} = ["]
    for item in items:
        out.append(fmt_tuple(item))
    out.append("]")
    return "\n".join(out)


# ─── Week 29: DevOps Culture & DORA ─────────────────────────────────────────

W29_EXTRA_I = [
    T("CALMS Framework DevOps", "DevOps Culture", "Very Common",
      "Explain the CALMS framework and how it guides a DevOps transformation.",
      "Culture, Automation, Lean, Measurement, Sharing — culture and sharing first; automation without trust fails.",
      "**CALMS pillars:**\n- **Culture** — blameless learning, cross-functional ownership\n- **Automation** — CI/CD, IaC, repeatable releases\n- **Lean** — value stream, WIP limits, eliminate wait time\n- **Measurement** — DORA metrics, flow metrics, SLOs\n- **Sharing** — internal conferences, shared runbooks, open postmortems\n\n**Azure/.NET example:** Platform team publishes golden-path GitHub Actions templates; stream teams adopt without ticket queue.\n\n**Architect:** CALMS is diagnostic — score each pillar before buying more Jenkins agents.",
      "CALMS shows maturity is cultural before tooling — interviewers probe whether you lead with culture.",
      "CALMS vs DORA? — CALMS is philosophy; DORA quantifies outcomes.",
      "Where start? — Value stream map + one bottleneck automation win.",
      "CALMS as checklist without culture change",
      "Buy tools before measuring baseline",
      "Ignore Sharing pillar entirely"),
    T("DORA Four Key Metrics", "DORA", "Very Common",
      "What are the four DORA metrics and what do Elite performers achieve?",
      "Deployment frequency, lead time for changes, change failure rate, MTTR — Elite: on-demand deploys, <1hr lead time, <15% CFR, <1hr restore.",
      "**DORA four keys:**\n| Metric | Elite (indicative) | What it measures |\n|--------|-------------------|------------------|\n| Deployment frequency | On-demand / multiple/day | Delivery throughput |\n| Lead time for changes | <1 hour | Flow efficiency |\n| Change failure rate | 0–15% | Quality of change |\n| MTTR | <1 hour | Recovery capability |\n\n**Collect in Azure DevOps:** Deployment records + work item cycle time + incident linkage.\n\n```csharp\n// Tag releases in Application Insights for CFR correlation\ntelemetry.TrackEvent(\"Deployment\", new Dictionary<string,string> {\n    [\"version\"] = buildId, [\"environment\"] = \"prod\"\n});\n```\n\n**Architect:** Never optimize one metric in isolation — faster deploys with rising CFR is regressing.",
      "DORA metrics are the lingua franca of engineering leadership conversations.",
      "Accelerate book? — Forsgren et al. — research backing, not vendor marketing.",
      "Low performers? — Monthly deploys, >1 month lead time — baseline before goals.",
      "Cherry-pick deployment frequency only",
      "No baseline before transformation",
      "Claim Elite without measurement method"),
    T("Team Topologies Overview", "Team Topologies", "Very Common",
      "Describe the four Team Topologies team types and their interaction modes.",
      "Stream-aligned, platform, enabling, complicated-subsystem — modes: collaboration, X-as-a-Service, facilitation.",
      "**Team types:**\n1. **Stream-aligned** — owns feature flow end-to-end (Checkout squad)\n2. **Platform** — internal APIs, golden paths, self-service (Azure landing zone portal)\n3. **Enabling** — temporary coaching (observability adoption sprint)\n4. **Complicated-subsystem** — deep specialty (payments PCI, ML ranking)\n\n**Interaction modes:**\n- **X-as-a-Service** — platform provides documented APIs\n- **Facilitation** — enabler pairs with stream temporarily\n- **Collaboration** — joint work on complex integration\n\n**Architect:** Platform as ticket queue violates X-as-a-Service — embed enablers instead.",
      "Team Topologies connects Conway's Law to deliberate org design.",
      "Thinnest viable platform? — One golden path (.NET 8 + AKS) done well.",
      "Reverse Conway? — Reorg streams before extracting microservices.",
      "Platform team as approval gate",
      "Every team owns Kubernetes upgrades",
      "No interaction mode documented"),
    T("SRE vs DevOps Role", "SRE", "Very Common",
      "How does Site Reliability Engineering differ from traditional DevOps?",
      "SRE applies software engineering to operations with error budgets and SLOs; DevOps is broader cultural movement — SRE is one implementation pattern.",
      "**SRE principles (Google):**\n- **SLIs/SLOs** — measurable reliability targets\n- **Error budgets** — balance velocity vs stability\n- **Toil reduction** — automate repetitive ops (<50% toil target)\n- **Blameless postmortems** — learn from incidents\n\n**DevOps broader:** CALMS, whole-team ownership, value stream.\n\n**.NET on AKS example:** SRE team owns cluster SLOs + golden Helm charts; stream teams own app SLOs within budget.\n\n**Architect:** SRE is not 'ops with a new title' — it requires engineering investment in automation.",
      "Clarifying SRE vs DevOps shows you understand industry nuance beyond buzzwords.",
      "SRE team size? — Rule of thumb: 5–8 SREs per 100 devs at scale.",
      "DevOps engineer title? — Often platform/SRE hybrid — define scope explicitly.",
      "SRE as gatekeeper approving all deploys",
      "100% reliability goal — no error budget",
      "SRE team disconnected from development"),
    T("Platform Engineering Basics", "Platform Engineering", "Very Common",
      "What is platform engineering and how does it differ from a traditional ops team?",
      "Platform engineering builds internal developer platforms (IDP) as products — self-service golden paths reduce cognitive load for stream teams.",
      "**IDP components:**\n- Developer portal (Backstage, Azure Dev Center)\n- Golden path templates (Bicep + GitHub Actions + AKS)\n- Shared observability, secrets, identity\n- Service catalog with ownership metadata\n\n**Difference from ops:**\n| Ops | Platform Engineering |\n|-----|---------------------|\n| Ticket queue | Self-service APIs |\n| Snowflake servers | Standardized modules |\n| Reactive | Product roadmap + NPS |\n\n**Architect:** Measure platform success via adoption % and DORA improvement of consuming teams.",
      "Platform engineering is hot because it operationalizes Team Topologies at scale.",
      "Build vs buy IDP? — Backstage + Azure primitives common hybrid.",
      "Platform PM? — Needed at 150+ engineers for roadmap prioritization.",
      "Platform team builds everything custom",
      "No developer feedback loop",
      "Golden path optional — most teams bypass"),
    T("Value Stream Mapping DevOps", "Value Stream", "Common",
      "How use value stream mapping in a DevOps transformation?",
      "Map steps from commit to production customer value; measure wait time vs process time; attack biggest wait — often environment provisioning or approval gates.",
      "**VSM exercise:**\n1. Walk one feature from idea → prod\n2. Time each state: coding, review, CI, staging, CAB, deploy\n3. Calculate **process ratio** = value-add time / total lead time\n\n**Typical finding:** 5 days total, 4 hours coding — 95% wait.\n\n**Azure fix:** Ephemeral PR environments via Bicep + GitHub Actions; remove CAB for low-risk paths.\n\n**Architect:** VSM data beats opinion in steering committee debates.",
      "Value stream mapping grounds DevOps in measurable flow, not toolchain shopping.",
      "Kanban vs VSM? — VSM is one-time diagnostic; Kanban sustains flow.",
      "Deployment pipeline as VSM? — Yes — visualize wait states in Azure DevOps.",
      "Optimize compile time when CAB waits 2 weeks",
      "VSM without executive sponsor",
      "Ignore downstream ops wait states"),
    T("Westrum Organizational Culture", "Culture", "Common",
      "What is Westrum's organizational culture typology and why does DORA research cite it?",
      "Generative (high cooperation, shared risk), Bureaucratic (rules), Pathological (blame) — generative culture correlates with better software delivery performance.",
      "**Three types:**\n| Type | Information flow | Failure response |\n|------|-----------------|------------------|\n| Pathological | Hoarded | Blame individuals |\n| Bureaucratic | Siloed by role | Cover up |\n| Generative | Shared across teams | Learn collectively |\n\n**Assessment:** Survey questions on collaboration and incident response.\n\n**Intervention:** Blameless postmortems, cross-team guilds, leadership modeling.\n\n**Architect:** Culture metrics belong in transformation dashboards alongside DORA.",
      "Westrum links culture to delivery outcomes — architects influence culture via rituals.",
      "Measure culture? — Annual Westrum survey + incident response qualitative review.",
      "Toxic culture fix? — Executive sponsorship required — grassroots alone fails.",
      "Assume generative because you use Kubernetes",
      "Skip culture in transformation plan",
      "Blame individuals in incident reviews"),
    T("Error Budget Concept", "SRE", "Very Common",
      "Explain error budgets and how they resolve the velocity vs stability conflict.",
      "Error budget = 1 − SLO (e.g., 99.9% SLO → 43 min/month downtime budget). While budget remains, ship features; when exhausted, freeze features and fix reliability.",
      "**Policy example:**\n```\nSLO: 99.95% availability (21 min/month budget)\nBurn rate alert: 14.4× → page immediately\nBudget exhausted → reliability sprint, no feature deploys\n```\n\n**.NET API on App Service:** Track availability SLI via Application Insights availability tests + request success rate.\n\n**Negotiation:** Product owns feature velocity within budget; SRE owns measurement.\n\n**Architect:** Error budget policy must be pre-agreed in writing — not invented during outage.",
      "Error budgets are the diplomatic bridge between product and reliability teams.",
      "Multi-window burn alerts? — Google SRE workbook — fast + slow burn.",
      "Budget for dependencies? — Track internal platform SLO separately.",
      "100% uptime SLO — no budget for velocity",
      "Error budget without enforcement policy",
      "Ignore budget until major outage"),
    T("Blameless Postmortem Practice", "Incident Culture", "Very Common",
      "What makes a postmortem truly blameless and effective?",
      "Focus on systems and processes that allowed failure; action items with owners and dates; publish widely; never name individuals as root cause.",
      "**Blameless postmortem template:**\n1. **Summary** — impact, duration, customer effect\n2. **Timeline** — UTC timestamps from monitoring\n3. **Root cause** — contributing factors (usually multiple)\n4. **What went well** — effective mitigations\n5. **Action items** — preventive, detective, process\n6. **Lessons** — shareable patterns\n\n**Azure example:** App Configuration flag rollback failed — action: add flag kill-switch integration test in CI.\n\n**Architect:** Track action item completion rate — postmortems without follow-through breed cynicism.",
      "Blameless culture is tested during the first major outage — rituals matter.",
      "Blameless vs no accountability? — Accountability for actions, not punishment for mistakes.",
      "Customer-facing postmortem? — Status page summary without internal jargon.",
      "Name engineer in root cause",
      "Postmortem without action items",
      "Incident closed before postmortem scheduled"),
    T("Trunk-Based Development", "DevOps Practices", "Very Common",
      "Explain trunk-based development and its relationship to CI/CD maturity.",
      "All developers commit to main/trunk at least daily; short-lived branches (<1 day); feature flags hide incomplete work; requires strong CI and test automation.",
      "**Practices:**\n- Main branch always releasable\n- Feature flags (LaunchDarkly, Azure App Configuration)\n- Small commits — easier bisect on failure\n- Branch by abstraction for large refactors\n\n**vs GitFlow:** GitFlow suits release trains; trunk suits continuous delivery.\n\n```csharp\nif (await _featureFlags.IsEnabledAsync(\"NewCheckoutFlow\", userId))\n    return await _checkoutV2.ProcessAsync(order);\nreturn await _checkoutV1.ProcessAsync(order);\n```\n\n**Architect:** Trunk without CI test gate causes main branch chaos — automate first.",
      "Trunk-based development is prerequisite for elite deployment frequency.",
      "Release branches exception? — Short-lived for LTS products only.",
      "Pair with code review? — Yes — small PRs reviewed within hours.",
      "Long-lived feature branches months",
      "Trunk without feature flags",
      "Skip CI on main merges"),
]

# Continue with ADVANCED and EXPERT in separate data structures - using a builder for remaining weeks
# Due to file size, the generator builds all weeks programmatically with topic banks

WEEK_TOPICS = {
    29: {
        "category": "DevOps Culture",
        "adv_topics": [
            ("DevSecOps Shift Left", "DevSecOps", "Integrate security in CI: SAST, dependency scan, container scan, secrets detection before merge — not gate at release."),
            ("Conway's Law Application", "Conway's Law", "System architecture mirrors communication structure — align service boundaries to team ownership or pay collaboration tax."),
            ("Feature Flag Architecture", "Feature Flags", "Azure App Configuration + targeting; kill switches; flag lifecycle cleanup; test all combinations in CI."),
            ("Deployment Frequency Improvement", "DORA", "Reduce batch size, trunk-based, automated deploy pipeline, eliminate manual CAB for low-risk tiers."),
            ("Lead Time Reduction", "DORA", "Parallelize CI, ephemeral environments, shift tests left, reduce handoffs between teams."),
            ("Change Failure Rate Reduction", "DORA", "Canary deploys, automated rollback, contract tests, progressive delivery, feature flags."),
            ("MTTR Improvement", "DORA", "Runbooks, observability, on-call rotation, chaos drills, automated rollback on SLO burn."),
            ("Platform as Product", "Platform Engineering", "Internal NPS surveys, roadmap from stream team pain, adoption metrics, thin vertical slices."),
            ("Enabling Team Rotation", "Team Topologies", "6-week embed with stream squad teaching observability; exit when self-sufficient; avoid permanent dependency."),
            ("DORA Benchmark Tiers", "DORA", "Elite/High/Medium/Low classifications — compare year-over-year, not vanity absolute numbers."),
            ("Toil Reduction SRE", "SRE", "Identify repetitive manual ops; automate or eliminate; target <50% toil; track toil budget per sprint."),
            ("Internal Developer Portal", "Platform Engineering", "Backstage catalog: services, APIs, ownership, runbooks, scorecards for production readiness."),
            ("Golden Path Template", "Platform Engineering", "Opinionated .NET 8 + AKS + Bicep + GitHub Actions starter — 80% teams adopt without customization."),
            ("Cognitive Load Reduction", "Team Topologies", "Abstract K8s complexity behind platform abstractions; stream teams focus on domain not ingress YAML."),
            ("SRE Embedding Model", "SRE", "SRE pairs with stream team for launch; shared on-call first 90 days; hand off with runbooks."),
            ("On-Call Rotation Design", "SRE", "Follow-the-sun or regional; max 1 week primary; secondary backup; compensation; burnout monitoring."),
            ("Incident Command System", "Incident Response", "IC, comms lead, scribe roles; status page updates every 15 min; separate war room from debugging."),
            ("CAB Alternative Risk Tiers", "Governance", "Low-risk auto-deploy; medium peer review; high architecture review — replace blanket CAB."),
            ("Progressive Delivery Culture", "Delivery", "Canary, blue-green, feature flags as default conversation — not big-bang releases."),
            ("Developer Experience Metrics", "Platform Engineering", "Time to first PR merge, time to prod, local dev setup minutes, platform ticket wait time."),
            ("Psychological Safety", "Culture", "Leaders admit mistakes; reward incident reporting; no retribution for outage participation."),
            ("Flow Efficiency vs Resource", "Lean", "Optimize end-to-end flow not individual team utilization — 90% busy teams create queues."),
            ("WIP Limits Kanban", "Lean", "Cap in-progress items per team; reduces context switching; surfaces bottlenecks visibly."),
            ("Continuous Learning Culture", "Culture", "Guilds, internal tech talks, postmortem reviews as training, budget for conferences."),
            ("Architecture Runway", "Planning", "Reserve 20% capacity for platform improvements enabling next quarter features."),
            ("Technical Debt vs Velocity", "Planning", "Visible debt register tied to incident correlation; negotiate paydown in planning."),
            ("Transformation Success Metrics", "DORA", "Baseline → 6-month → 12-month DORA; developer survey; incident trend; business outcome linkage."),
            ("CALMS Automation Depth", "CALMS", "IaC everything, policy as code, automated compliance evidence — not shell scripts on laptops."),
            ("DevOps Team Anti-Pattern", "Anti-Patterns", "Separate DevOps team doing ops for devs — creates handoff; embed or platform instead."),
            ("Value Stream Bottleneck Fix", "Value Stream", "Environment provisioning 3 days → Bicep PR environments in 15 min — measure lead time delta."),
        ],
        "exp_scenarios": [
            ("DORA Metrics Stagnant Six Months", "DORA metrics flat after initial CI investment — diagnose and plan 90-day recovery."),
            ("Blame Culture After Sev-1", "Engineer named in exec email after outage — rebuild blameless culture in 30 days."),
            ("Platform Team Ticket Queue", "2-week wait for K8s namespace — transform platform to self-service in 90 days."),
            ("CTO Ten X Deploy Frequency", "CEO demands 10× deployment frequency in Q2 — phased plan with risk acceptance."),
            ("SRE DevOps Turf War", "SRE and DevOps teams blocking each other — org design resolution in 60 days."),
            ("Conway Misalignment Delivery", "4 teams, 12 services, every feature crosses 3 teams — inverse Conway maneuver."),
            ("Feature Flag Kill Switch Failure", "Flag stuck on floods bad checkout — incident response and prevention plan."),
            ("Trunk-Based Adoption Resistance", "Senior devs refuse short branches — change management and pilot plan."),
            ("Error Budget Burned Pre-Launch", "Black Friday launch with exhausted budget — negotiate freeze vs business risk."),
            ("Westrum Assessment Pathological", "Survey shows blame culture — executive-led transformation roadmap."),
            ("DevSecOps Blocking Releases", "Security scans add 4 hours; teams bypass — balanced pipeline in 30 days."),
            ("Value Stream Three Week Wait", "VSM reveals 18-day CAB wait — governance redesign with risk tiers."),
            ("On-Call Burnout Crisis", "Two engineers quit after on-call rotation — sustainable model in 60 days."),
            ("Postmortem Actions Ignored", "Same failure repeats — action item tracking system in 30 days."),
            ("Elite DORA Claim Audit", "Marketing claims Elite; data shows Medium — honest assessment plan."),
            ("Platform Adoption Twenty Percent", "IDP built but ignored — adoption strategy with enabling team."),
            ("CAB Blocking Daily Deploys", "Fortnightly release only due to CAB — tiered change governance."),
            ("Team Topologies Reorg", "Reorganize 200 engineers into stream-aligned topology — 90-day plan."),
            ("DevOps Transformation Mandate", "New CTO mandates DevOps in 90 days — realistic phased program."),
            ("Culture Change Measurement", "Board asks how you know culture improved — metrics and evidence plan."),
        ],
    },
    30: {
        "category": "CI/CD",
        "adv_topics": [
            ("GitHub Actions Matrix Build", "GitHub Actions", ".NET matrix across OS versions; cache NuGet; reusable workflows for org standards."),
            ("Azure DevOps Multi-Stage YAML", "Azure DevOps", "Stages: build, test, deploy dev/staging/prod; environment approvals; template libraries."),
            ("Blue-Green App Service", "Deployment", "Two deployment slots; warm swap; smoke tests; instant rollback via swap back."),
            ("Canary AKS with Flagger", "Deployment", "5% traffic canary; Prometheus metrics gate; auto-promote or rollback."),
            ("OIDC Azure Federated Credentials", "Security", "GitHub Actions OIDC to Azure — no long-lived service principal secrets in repos."),
            ("Database Migration Pipeline", "CI/CD", "Flyway/Liquibase in pipeline; backward-compatible migrations; expand-contract pattern."),
            ("SAST in CI Pipeline", "DevSecOps", "SonarQube/CodeQL on PR; quality gate blocks merge; suppressions require security review."),
            ("Pact Contract Testing CI", "Testing", "Consumer-driven contracts in pipeline; provider verification before deploy; pact broker."),
            ("Automated Rollback Pipeline", "CI/CD", "Health check failure post-deploy triggers previous artifact redeploy; max 5 min rollback SLA."),
            ("SBOM Generation Pipeline", "Supply Chain", "Syft/SPDX on container build; store in artifact registry; vulnerability scan against SBOM."),
            ("SLSA Level 3 Pipeline", "Supply Chain", "Hermetic builds, signed provenance, isolated build workers — document supply chain."),
            ("Immutable Artifact Promotion", "CI/CD", "Same container digest dev→staging→prod; never rebuild; tag promotion only."),
            ("Pipeline Secret Management", "Security", "Azure Key Vault references; no secrets in YAML; rotation without pipeline edit."),
            ("Ephemeral PR Environments", "CI/CD", "Bicep deploy on PR; smoke test; tear down on merge — full integration per PR."),
            ("Pipeline Parallelization", "CI/CD", "Split test suites; test impact analysis; distributed test agents — cut 45min to 12min."),
            ("Deployment Gates Quality", "CI/CD", "Azure DevOps gates: performance baseline, security scan, manual approval for prod."),
            ("Container Image Signing", "Supply Chain", "Cosign sign images; admission controller verifies signature in AKS."),
            ("Pipeline as Code Review", "Governance", "CI YAML in PR review; policy checks via OPA/Conftest; no UI-only pipeline edits."),
            ("Release Orchestration", "CI/CD", "Coordinate multi-service deploy order; health aggregation; coordinated rollback."),
            ("Feature Branch CI Cost", "CI/CD", "Self-hosted runners for private network; spot VMs for non-prod; cache aggressively."),
            ("Pipeline Observability", "CI/CD", "Track pipeline duration, failure rate, flaky test rate — DORA lead time input."),
            ("DAST in Staging Gate", "DevSecOps", "OWASP ZAP against staging post-deploy; block prod promote on critical findings."),
            ("Infrastructure Pipeline", "CI/CD", "Terraform/Bicep plan on PR; apply on merge to main; drift detection scheduled."),
            ("Mobile CI Code Signing", "CI/CD", "Secure cert storage in Key Vault; Fastlane match pattern; separate signing stage."),
            ("Monorepo CI Strategy", "CI/CD", "Path filters trigger affected services only; Nx/Turborepo affected graph."),
            ("Pipeline Failure Notification", "CI/CD", "Slack/Teams with actionable context; link to logs; auto-create incident if prod deploy fails."),
            ("Compliance Evidence Pipeline", "Governance", "Auto-collect SOC2 change management evidence from deployment records."),
            ("Zero-Downtime DB Deploy", "CI/CD", "Expand-contract migrations; dual-write period; feature flag for new schema reads."),
            ("Pipeline Disaster Recovery", "CI/CD", "Backup pipeline definitions; runner failover; artifact registry geo-replication."),
            ("GitOps vs Push Deploy", "CI/CD", "Argo CD pull vs pipeline push — when each fits Azure landing zone model."),
        ],
        "exp_scenarios": [
            ("Production Deploy Pipeline Breach", "Secrets leaked in GitHub Actions logs — 30-day remediation and pipeline hardening."),
            ("Blue-Green Swap Failed Smoke Test", "Swap triggered outage — incident response and pipeline fix in 30 days."),
            ("Canary False Positive Promotion", "Canary promoted despite latent bug — metric selection fix in 60 days."),
            ("OIDC Migration From SP Secrets", "200 repos with service principal secrets — federated credential migration plan."),
            ("Breaking DB Migration Production", "Migration locked orders table 40 min — zero-downtime strategy in 90 days."),
            ("SAST Blocking All PRs", "Developers disable scans — balanced security gate in 30 days."),
            ("Pact Broker Outage Deploy", "Contract tests unavailable — deploy policy and broker HA in 60 days."),
            ("Rollback Failed Bad Artifact", "Rollback deployed wrong version — immutable artifact discipline in 30 days."),
            ("SBOM Critical CVE Flood", "1000 images with log4j — SBOM-driven remediation in 14 days."),
            ("SLSA Audit Failure", "Customer requires SLSA L3 — 90-day supply chain upgrade program."),
            ("Pipeline 2 Hour Lead Time", "CI blocks elite DORA — parallelization program in 60 days."),
            ("Multi-Service Deploy Partial Failure", "3 of 5 services deployed; inconsistent state — orchestration fix."),
            ("GitHub Actions Minute Budget", "Org exceeds Actions minutes — cost optimization in 30 days."),
            ("Prod Deploy Without Approval", "Misconfigured environment bypass — governance fix in 14 days."),
            ("Container Image Tag Mutable", "latest tag caused wrong deploy — immutable digest policy in 30 days."),
            ("PR Environment Cost Overrun", "Ephemeral envs cost $50K/month — lifecycle policy in 30 days."),
            ("Flaky Tests Block Releases", "20% flaky rate — test stabilization sprint in 60 days."),
            ("Cross-Region Pipeline Failover", "Primary region pipeline down — DR pipeline in 90 days."),
            ("Compliance Pipeline Gap", "Auditor finds missing deploy evidence — automated collection in 60 days."),
            ("Monorepo CI Explosion", "Every commit runs 4 hours CI — affected-build optimization in 90 days."),
        ],
    },
    31: {
        "category": "Infrastructure as Code",
        "adv_topics": [
            ("Bicep Module Composition", "Bicep", "Reusable modules for VNet, AKS, Key Vault; semantic versioning; what-if on PR."),
            ("Terraform State Backend", "Terraform", "Azure Storage backend with state locking; separate state per environment; RBAC on state container."),
            ("ARM vs Bicep vs Terraform", "IaC", "ARM verbose; Bicep Azure-native transpile; Terraform multi-cloud — choose per team skill and scope."),
            ("Drift Detection Scheduled", "IaC", "Terraform plan cron; Azure Policy compliance scan; alert on unmanaged changes."),
            ("GitOps Infrastructure Argo", "GitOps", "Argo CD syncs cluster desired state from Git; PR for infra changes; automated sync with manual prod approve."),
            ("Bicep Parameter Files", "Bicep", "Environment-specific .bicepparam; Key Vault references for secrets; no secrets in Git."),
            ("Terraform Module Registry", "Terraform", "Private registry for org modules; version pinning; changelog per module."),
            ("Remote State Partitioning", "Terraform", "State per subscription/environment; blast radius isolation; cross-stack data sources."),
            ("Policy as Code Azure", "Policy", "Azure Policy definitions in Git; deploy via pipeline; deny non-compliant resources."),
            ("Landing Zone Accelerator", "Landing Zones", "Azure Landing Zone reference architecture; platform subscription vs workload subscriptions."),
            ("IaC Testing Terratest", "IaC", "Integration tests post-deploy; validate NSG rules, RBAC assignments programmatically."),
            ("Import Existing Resources", "IaC", "Terraform import for brownfield; document in ADR; avoid manual portal edits going forward."),
            ("IaC Secret Rotation", "IaC", "Key Vault auto-rotation; update references not hardcoded values; pipeline validates connectivity."),
            ("Multi-Subscription Deployment", "IaC", "Pipeline service principal scoped per sub; management group hierarchy in Bicep."),
            ("IaC Code Review Checklist", "IaC", "NSG overly permissive, public endpoints, missing tags, no diagnostic settings."),
            ("Bicep CI What-If", "Bicep", "az deployment group what-if in PR comment; block merge on destructive unexpected changes."),
            ("Terraform Workspace Strategy", "Terraform", "Workspaces vs separate directories — recommend separate state for prod isolation."),
            ("IaC Rollback Strategy", "IaC", "Git revert + pipeline apply; state backup before major changes; never manual state edit."),
            ("Resource Naming Convention", "IaC", "CAF naming in Bicep variables; enforce via policy; consistent across 50 subscriptions."),
            ("IaC Documentation", "IaC", "README per module: inputs, outputs, dependencies, example usage."),
            ("Brownfield IaC Adoption", "IaC", "Inventory portal resources; import critical path first; freeze manual changes."),
            ("IaC Performance Large State", "IaC", "State file >50MB — split stacks; targeted applies; reduce resource count per state."),
            ("Cross-Stack References", "Terraform", "Remote state outputs consumed by app stack; version output contracts."),
            ("IaC Security Scanning", "IaC", "Checkov/tfsec on PR; block public storage accounts; require private endpoints."),
            ("Hub-Spoke Bicep Module", "Bicep", "Hub VNet module; spoke peering; Azure Firewall routes; reusable across workloads."),
            ("AKS IaC Best Practices", "IaC", "Private cluster, workload identity, Azure CNI overlay, node pool autoscale in Bicep."),
            ("IaC Environment Parity", "IaC", "Same modules dev/prod; scale parameters differ; avoid snowflake prod-only config."),
            ("Terraform Cloud vs Self-Hosted", "IaC", "TFC for state/run management vs Azure DevOps agents — cost and compliance trade-off."),
            ("IaC Disaster Recovery", "IaC", "State geo-replication; module source mirror; rebuild region from Git in RTO target."),
            ("Platform Team IaC Standards", "IaC", "Approved module catalog; exception process; quarterly module deprecation review."),
        ],
        "exp_scenarios": [
            ("Terraform State Corruption", "State file corrupted during apply — recovery and prevention in 30 days."),
            ("Manual Portal Change Drift", "Critical NSG edited in portal — drift remediation program in 60 days."),
            ("Bicep Deploy Deleted Production", "What-if missed dependency — blast radius and process fix in 30 days."),
            ("IaC Adoption Resistance", "Teams prefer click-ops — brownfield import and mandate in 90 days."),
            ("Policy Deny Blocks Deploy", "Azure Policy blocks valid deployment — policy refinement in 30 days."),
            ("Multi-Sub State Lock Conflict", "Two pipelines lock same state — partitioning fix in 14 days."),
            ("Landing Zone 12 Month Overdue", "LZ program stalled — executive recovery plan in 90 days."),
            ("Module Breaking Change Cascade", "VNet module v3 breaks 40 consumers — versioning policy in 60 days."),
            ("GitOps Desync Incident", "Argo CD auto-sync reverted manual hotfix — sync policy fix in 30 days."),
            ("IaC Secret in Git History", "Key Vault password committed — rotation and secret scanning in 14 days."),
            ("Terraform Import Wrong Resource", "Imported wrong RG — state surgery and guardrails in 30 days."),
            ("Prod Dev Environment Skew", "Prod-only Bicep params caused outage — parity enforcement in 60 days."),
            ("IaC Pipeline 45 Min Apply", "Monolithic stack — stack splitting program in 90 days."),
            ("Compliance IaC Gap Audit", "Auditor finds untagged resources — policy remediation in 60 days."),
            ("Cross-Team Module Fork", "5 teams forked same VNet module — consolidation in 90 days."),
            ("Disaster Recovery IaC Rebuild", "Region lost — rebuild from Git validation in 90 days."),
            ("Checkov False Positive Flood", "500 findings block all PRs — rule tuning in 30 days."),
            ("Hub-Spoke Peering Limit", "Peering limit hit at 400 spokes — topology redesign in 90 days."),
            ("IaC Engineer Bus Factor", "One person knows Terraform — knowledge transfer in 60 days."),
            ("Brownfield 500 Resources Import", "Acquire company infrastructure — import program in 90 days."),
        ],
    },
    32: {
        "category": "Observability",
        "adv_topics": [
            ("OpenTelemetry .NET SDK", "OpenTelemetry", "Add OTel to ASP.NET Core; auto-instrumentation; export to Azure Monitor via OTLP."),
            ("RED Metrics Method", "Metrics", "Rate, Errors, Duration per service — dashboard template for each API."),
            ("USE Metrics Infrastructure", "Metrics", "Utilization, Saturation, Errors for nodes, DB pools, queue depth."),
            ("Structured Logging Serilog", "Logging", "JSON logs with traceId, spanId, tenantId; sink to Log Analytics; no string concatenation."),
            ("Distributed Trace Propagation", "Tracing", "W3C tracecontext header across HTTP, Service Bus, background workers."),
            ("SLI SLO Definition", "SLO", "SLI: successful requests / total; SLO: 99.9% monthly; error budget policy documented."),
            ("Dashboard Design Hierarchy", "Dashboards", "L1 executive SLO; L2 service health; L3 diagnostic drill-down — avoid vanity metrics."),
            ("Alerting SLO Burn Rate", "Alerting", "Multi-window burn rate alerts; page on fast burn; ticket on slow burn."),
            ("Application Insights Sampling", "App Insights", "Adaptive sampling in prod; 100% on errors; custom telemetry for business events always kept."),
            ("Metric Cardinality Control", "Metrics", "Never label userId on metrics; use bounded labels; aggregate high-cardinality in logs."),
            ("Log Analytics KQL Patterns", "Logging", "join traces to logs on operation_Id; parse JSON properties; summarize p99 by dependency."),
            ("Observability Cost Control", "FinOps", "Sampling, retention tiers, metric aggregation, drop debug in prod — budget alerts."),
            ("Service Map Dependency", "Tracing", "App Insights application map; identify sync call chains; async boundary gaps."),
            ("Custom Business Metrics", "Metrics", "Track orders/min, payment failures — correlate with technical metrics in same dashboard."),
            ("Health Check Endpoints", "Observability", "/health/live vs /health/ready; include DB, cache, queue checks on ready only."),
            ("Correlation ID Middleware", "Logging", ".NET middleware injects traceId; propagate to HttpClient, Service Bus message properties."),
            ("Alert Fatigue Reduction", "Alerting", "Alert on symptoms (SLO burn) not causes (CPU 80%); runbook link required per alert."),
            ("Synthetic Monitoring", "Observability", "Availability tests from 5 regions; critical journey every 5 min; alert before users notice."),
            ("OpenTelemetry Collector", "OpenTelemetry", "Collector sidecar in AKS; batch, filter, export to multiple backends."),
            ("Exception Tracking Strategy", "App Insights", "TrackException with custom properties; group by outer message; link to release version."),
            ("Live Metrics Debug", "App Insights", "Live Metrics Stream for deploy validation; compare error rate pre/post swap."),
            ("Profiler On Demand", "App Insights", "Trigger snapshot profiler on high CPU alert; capture stack traces in production."),
            ("Observability Maturity Model", "Observability", "Level 1 uptime ping → Level 4 SLO-driven auto-rollback — assess and roadmap."),
            ("Trace Sampling Tail", "Tracing", "Tail-based sampling in collector — keep all errors, sample 1% success."),
            ("Log PII Redaction", "Logging", "Serilog destructuring policy; never log card numbers; compliance scan on log fields."),
            ("Dashboard as Code", "Dashboards", "Grafana/Azure Workbooks in Git; PR review for dashboard changes."),
            ("On-Call Runbook Integration", "Alerting", "Alert links to runbook in wiki; auto-page includes last 5 deploys."),
            ("Observability Testing", "Observability", "Chaos test verifies alerts fire; synthetic failure in staging monthly."),
            ("Multi-Tenant Observability", "Observability", "tenantId dimension on logs/traces; per-tenant SLO for enterprise tier."),
            ("Legacy App Instrumentation", "Observability", "OpenTelemetry auto-instrument without code change where possible; manual spans for critical paths."),
        ],
        "exp_scenarios": [
            ("Observability Blind During Outage", "No traces for failing service — instrumentation sprint in 30 days."),
            ("Cardinality Explosion Bill", "Log Analytics cost 5× budget — cardinality and sampling fix in 60 days."),
            ("Alert Fatigue Engineers Ignore", "200 alerts/day — SLO-based alerting redesign in 30 days."),
            ("Missing Trace Across Services", "Broken propagation — W3C header standardization in 30 days."),
            ("SLO Not Measurable", "No SLI data — instrumentation and SLO definition in 60 days."),
            ("Dashboard Vanity Metrics", "CPU graphs but no user impact — RED/USE dashboard program in 30 days."),
            ("Sampling Hides Production Bug", "Bug only in unsampled requests — tail sampling in 60 days."),
            ("PII in Logs Audit Failure", "GDPR breach risk from logs — redaction and scan in 14 days."),
            ("Post-Deploy No Visibility", "Deploy succeeded but errors spike undetected — deploy markers and alerts in 30 days."),
            ("Multi-Region Trace Fragmentation", "Traces split across regions — collector architecture in 90 days."),
            ("On-Call No Runbooks", "Engineers page without context — runbook program in 60 days."),
            ("App Insights Agent Overhead", "OTel agent adds 200ms latency — tuning in 30 days."),
            ("Synthetic False Negatives", "Tests pass but users fail — journey test redesign in 30 days."),
            ("Tenant Noisy Neighbor Metrics", "One tenant skews aggregates — per-tenant observability in 60 days."),
            ("Legacy Monolith Black Box", "No spans in core monolith — phased instrumentation in 90 days."),
            ("Observability Vendor Lock-In", "Migrate from vendor A to OTel — 90-day portability plan."),
            ("Incident No Timeline Reconstruction", "Cannot build timeline — structured logging mandate in 30 days."),
            ("SLO Burn Unnoticed Weekend", "Outage Sunday — burn rate alerting in 14 days."),
            ("FinOps Observability Cut", "CFO cuts budget 50% — retain SLO-critical signals in 30 days."),
            ("Compliance Log Retention", "7-year retention required — tiered storage architecture in 90 days."),
        ],
    },
    33: {
        "category": "System Design Methodology",
        "adv_topics": [
            ("RESHADED Framework", "Methodology", "Requirements, Estimation, Storage, High-level, API, Data model, Estimation refine, Design deep-dive — interview structure."),
            ("Back-of-Envelope Estimation", "Estimation", "QPS = DAU × actions/day / 86400; storage = records × size × retention; state assumptions aloud."),
            ("Functional Requirements Extraction", "Requirements", "Clarify actors, use cases, read vs write ratio, consistency needs before drawing boxes."),
            ("Non-Functional Requirements", "Requirements", "Latency p99, availability, durability, compliance — prioritize top 3 explicitly."),
            ("API Design REST Conventions", "API Design", "Resource nouns, pagination cursor, idempotency keys, versioning, error schema RFC 7807."),
            ("Failure Mode Enumeration", "Reliability", "List: DB down, cache miss storm, dependency timeout, deploy bad version — mitigation per mode."),
            ("Scope Management Interview", "Interview Skills", "State what's out of scope; parking lot deep dives; time-box sections — show discipline."),
            ("Capacity Estimation Storage", "Estimation", "1B users × 1KB profile = 1TB; replication 3×; growth 50%/year — round generously."),
            ("Capacity Estimation Bandwidth", "Estimation", "1M QPS × 2KB response = 2GB/s egress — CDN reduces origin load."),
            ("Read Write Ratio Impact", "Design", "100:1 read — cache + replicas; 1:1 — optimize writes, sharding earlier."),
            ("Consistency Requirements Clarify", "Design", "Strong for payments; eventual for social feed — per operation not global."),
            ("High-Level Component Diagram", "Design", "5-7 boxes max initially: client, CDN, API, cache, DB, queue, workers — label protocols."),
            ("Data Model First Pass", "Design", "Entities, relationships, access patterns drive schema — not normalized academic ERD."),
            ("Bottleneck Identification", "Design", "After diagram, ask 'what breaks first at 10× load?' — proactive deep dive invitation."),
            ("Trade-off Table Interview", "Interview Skills", "SQL vs NoSQL, push vs pull, sync vs async — 2×2 table with decision column."),
            ("Deep Dive Selection", "Interview Skills", "Let interviewer choose path — auth, scale, or data — don't force your favorite."),
            ("Assumption Documentation", "Interview Skills", "Write assumptions on board: '10M DAU, 100:1 read, 99.9% availability' — refer back."),
            ("Migration Path Discussion", "Design", "Phase 1 monolith → Phase 2 cache → Phase 3 shard — shows pragmatism."),
            ("Security Scope Brief", "Security", "2-minute pass: auth, encryption, rate limit — don't derail unless Tier-0."),
            ("Observability Design Inclusion", "Observability", "Name metrics, alerts, trace propagation in design — not afterthought."),
            ("Multi-Tenant Design Clarify", "Requirements", "Shared vs silo isolation — affects every downstream decision."),
            ("Latency Budget Allocation", "Design", "200ms p99 total: 20ms CDN, 50ms API, 80ms DB, 50ms buffer — allocate explicitly."),
            ("Idempotency Design Default", "API Design", "All mutating APIs accept Idempotency-Key — platform concern in design."),
            ("Pagination Design Choice", "API Design", "Cursor for live feeds; offset only for admin static lists."),
            ("Rate Limiting Design", "API Design", "Per-client tier at gateway; 429 with Retry-After; document in API design."),
            ("Caching Layer Placement", "Design", "CDN for static; Redis for hot reads; application L1 for viral keys."),
            ("Async Boundary Identification", "Design", "Email, analytics, search index — async queue; keep sync path minimal."),
            ("Interview Time Management", "Interview Skills", "5 clarify, 10 high-level, 20 deep dive, 5 trade-offs — narrate clock."),
            ("Requirement Change Mid-Interview", "Interview Skills", "Adapt diagram — add GDPR delete without restart — flexibility signal."),
            ("Diagram Narration Technique", "Interview Skills", "Narrate while drawing — explain data flow arrows; interviewer follows logic without reading your mind."),
        ],
        "exp_scenarios": [
            ("45 Min Design No Clarification", "Candidate jumped to diagram — coaching on RESHADED in mock prep."),
            ("Estimation Order of Magnitude Wrong", "Claimed 1B QPS for niche app — estimation drill program."),
            ("Scope Creep Notification Search Payment", "Interviewer adds requirements — scope management exercise."),
            ("Interviewer Challenges SQL Choice", "Defend or pivot with trade-off table — communication practice."),
            ("No Failure Modes Mentioned", "Design ignores DB failure — failure mode checklist adoption."),
            ("Over-Engineer Day One Google", "Staff candidate proposes 50 microservices — phased evolution coaching."),
            ("Under-Engineer No Scale Path", "No answer for 10× growth — bottleneck methodology training."),
            ("API Design Missing Idempotency", "Payment API without idempotency — API review checklist."),
            ("NFR Not Prioritized", "Listed 10 NFRs without ranking — top-3 prioritization practice."),
            ("Deep Dive Wrong Path", "Spent 30 min on auth when scale was hint — active listening coaching."),
            ("No Trade-off Summary", "Ended without decisions table — closing ritual practice."),
            ("Assumptions Contradicted Later", "Said 1M DAU then sized for 1B — assumption board discipline."),
            ("Missing Observability Close", "Strong design, zero monitoring — observability checklist."),
            ("Data Model Afterthought", "Boxes without schema — data-first design practice."),
            ("Latency Budget Exceeded", "Design sums to 2s p99 — budget allocation exercise."),
            ("Multi-Tenant Assumption Missed", "Designed single-tenant; SaaS context given — requirements extraction."),
            ("Security Derail 20 Minutes", "Over-indexed security on social app — scope calibration."),
            ("No Migration Path", "Only final state — phased evolution narrative practice."),
            ("Interviewer Says Won't Work", "Defensive response — collaborative redirect training."),
            ("Whiteboard Unreadable", "Diagram chaos — structure and narration practice."),
        ],
    },
    34: {
        "category": "Scalability & Caching",
        "adv_topics": [
            ("Cache-Aside Pattern .NET", "Caching", "Read: check Redis, miss → DB → populate. Write: update DB, invalidate cache key."),
            ("Read-Through vs Write-Through", "Caching", "Read-through: cache loads on miss. Write-through: sync write cache+DB. Choose per consistency need."),
            ("CDN Azure Front Door", "CDN", "Static assets, cacheable API GETs; cache key rules; purge on deploy via versioned URLs."),
            ("Database Read Replicas", "Scaling", "Route analytics to replica; primary for writes; monitor replication lag threshold."),
            ("Horizontal Sharding Strategy", "Sharding", "Shard key: tenantId hash; avoid cross-shard queries in hot path; resharding plan documented."),
            ("Load Balancer Layer 7", "Load Balancing", "Azure App Gateway path routing, WAF, cookie affinity only when required."),
            ("Hot Key Mitigation Redis", "Caching", "Split key replicas, local L1 cache, read replicas, request coalescing."),
            ("Cache Stampede Prevention", "Caching", "TTL jitter, single-flight mutex, stale-while-revalidate, probabilistic early refresh."),
            ("Write-Behind Caching", "Caching", "Buffer writes to cache, async flush to DB — risk of data loss; only for analytics counts."),
            ("Cache Invalidation Strategy", "Caching", "TTL + event-driven invalidation on write; versioned cache keys for deploy safety."),
            ("Consistent Hashing Ring", "Distributed Cache", "Redis Cluster slot migration; minimal key remap on node add/remove."),
            ("Connection Pool Sizing", "Scaling", "pods × pool size < DB max_connections; formula in runbook."),
            ("Autoscale Rules AKS", "Scaling", "CPU + custom metric (queue depth); scale-out fast, scale-in slow; min replicas for baseline."),
            ("Database Vertical Scale Limits", "Scaling", "When CPU >70% sustained — plan shard before vertical ceiling."),
            ("Geo-Distributed Cache", "Caching", "Redis Enterprise active-active; session stickiness; conflict resolution policy."),
            ("Cache Warming Strategy", "Caching", "Pre-load hot keys before launch; scheduled refresh; monitor hit rate."),
            ("Negative Caching", "Caching", "Cache 404 for non-existent keys short TTL — prevent DB hammer on attacks."),
            ("Cache Penetration Attack", "Caching", "Bloom filter for existence; rate limit; random TTL on miss."),
            ("Multi-Level Cache", "Caching", "L1 in-memory 2s TTL + L2 Redis + L3 CDN — measure hit rate per tier."),
            ("Shard Key Selection", "Sharding", "High cardinality, even distribution, query locality — tenantId classic for SaaS."),
            ("Read Your Writes", "Consistency", "Session token routes to primary post-write; or short TTL blocking read."),
            ("Replica Lag Handling", "Scaling", "Monitor lag; route away if >5s; stale read acceptable endpoints documented."),
            ("Load Test Methodology", "Scaling", "Baseline, 2× peak, soak 4hr, spike — in staging with prod-like data volume."),
            ("Rate Limit at Edge", "Scaling", "Front Door rate limit per IP/client; protect origin during viral event."),
            ("Partition Tolerance Cache", "Distributed Cache", "Split brain: prefer availability with stale cache vs hard fail — document."),
            ("Elasticache vs Azure Redis", "Caching", "Enterprise features, clustering, persistence — tier selection matrix."),
            ("SQL Read Scale-Out", "Scaling", "Azure SQL Hyperscale read replicas; elastic pools for dev/test."),
            ("Aspire Connection Resilience", "Scaling", ".NET Polly retry, circuit breaker on HttpClient and DB connections."),
            ("Capacity Headroom Planning", "Scaling", "2× headroom for failover; autoscale max from capacity calc."),
            ("Scaling State Machines", "Scaling", "Identify stateful vs stateless components — scale stateless horizontally first."),
        ],
        "exp_scenarios": [
            ("Cache Stampede Black Friday", "DB collapsed on TTL expiry — stampede mitigation before next sale."),
            ("Hot Key Celebrity Product", "Single Redis key 100K QPS — hot key runbook execution."),
            ("Shard Resharding Live Traffic", "Tenant growth requires resharding — zero-downtime migration plan."),
            ("Replica Lag User Complaints", "Users see stale data post-purchase — read routing fix in 30 days."),
            ("CDN Cache Poisoning", "Wrong content served from edge — cache key and purge fix."),
            ("Connection Pool Exhaustion", "Hikari maxed during spike — pool sizing and scale plan."),
            ("Autoscale Thrashing", "Pods scale up/down every minute — stabilization policy in 30 days."),
            ("Cache Invalidation Bug", "Stale inventory caused oversell — invalidation event fix in 14 days."),
            ("Cross-Shard Query Requirement", "Report needs cross-shard join — async aggregation architecture."),
            ("Geo-Cache Inconsistency", "EU/US cache diverge — consistency policy in 60 days."),
            ("Load Balancer Sticky Session Fail", "Session lost on scale-out — stateless JWT migration."),
            ("Read Replica Cost Overrun", "10 replicas unused — right-sizing in 30 days."),
            ("Negative Cache Attack", "Attacker queries random IDs — bloom filter deployment."),
            ("Write-Behind Data Loss", "Cache flush failed — durability policy change."),
            ("Sharding Wrong Key", "Sharded by date — hot latest shard — resharding program."),
            ("L1 Cache Memory Pressure", "In-process cache OOM — size limits and eviction policy."),
            ("Front Door Origin Overload", "CDN miss storm — origin protection in 30 days."),
            ("Scale Test Never Run", "First prod spike failed — load test mandate before launch."),
            ("Hyperscale Tier Migration", "Azure SQL hitting limits — Hyperscale migration 90-day plan."),
            ("Multi-Tenant Noisy Neighbor Cache", "One tenant fills Redis — per-tenant quota in 60 days."),
        ],
    },
    35: {
        "category": "Messaging & Events",
        "adv_topics": [
            ("Kafka Partition Strategy", "Kafka", "Partition key = orderId for ordering; enough partitions for consumer parallelism."),
            ("Azure Service Bus Sessions", "Service Bus", "FIFO per sessionId; session lock; duplicate detection window."),
            ("Event-Driven Architecture", "Event-Driven", "Domain events decouple services; event schema registry; versioned contracts."),
            ("Saga Orchestration vs Choreography", "Saga", "Orchestrator for complex flows; choreography for simple event chains — checkout example."),
            ("Transactional Outbox Pattern", "Outbox", "Same DB transaction for entity + outbox row; relay to Service Bus; idempotent consumers."),
            ("Idempotent Consumer Design", "Idempotency", "Processed message table with messageId; business idempotency key; at-least-once safe."),
            ("Message Ordering Guarantees", "Messaging", "Order within partition/session only; design for out-of-order across partitions."),
            ("Dead Letter Queue Handling", "DLQ", "DLQ monitor alert; replay tooling with audit; poison message quarantine."),
            ("Event Schema Evolution", "Events", "Backward compatible additive fields; schema registry validation; reject breaking changes."),
            ("Exactly-Once Semantics Reality", "Messaging", "True exactly-once rare; idempotent consumer + dedup = practical exactly-once effect."),
            ("Service Bus vs Event Hubs", "Azure Messaging", "Service Bus: commands, sessions, DLQ. Event Hubs: high-throughput event stream, Kafka API."),
            ("Competing Consumers Scale", "Messaging", "Multiple consumers same subscription; partition count = max parallelism."),
            ("Message Size Limits", "Messaging", "Large payload → blob storage reference in message; 256KB Service Bus limit."),
            ("Scheduled Messages", "Service Bus", "Delayed delivery for retry backoff; scheduled enqueue time."),
            ("Priority Queues Pattern", "Messaging", "Separate queues OTP vs batch; never block critical on bulk."),
            ("Event Sourcing vs Event-Driven", "Events", "ES stores state as events; ED uses events for integration — different concerns."),
            ("CQRS with Event Bus", "CQRS", "Write model publishes events; read models subscribe and project."),
            ("Poison Message Detection", "DLQ", "Max delivery count 5 → DLQ; alert; manual triage workflow."),
            ("Message Correlation", "Observability", "correlationId, causationId in message properties; trace across async boundary."),
            ("Bulkhead Queue Isolation", "Messaging", "Separate namespace per domain; failure in analytics doesn't block orders."),
            ("Kafka Consumer Group Rebalance", "Kafka", "Rebalance storm mitigation; cooperative sticky assignor; adequate partition count."),
            ("Event Hub Capture Archive", "Event Hubs", "Auto-archive to ADLS for replay, audit, ML training pipeline."),
            ("Saga Compensation Logic", "Saga", "Payment succeeded, ship failed → refund idempotent with sagaId."),
            ("Inbox Pattern Consumer", "Inbox", "Consumer inbox table dedup before processing; pairs with outbox producer."),
            ("Message Encryption Transit", "Security", "TLS 1.2+; Premium Service Bus private endpoint; CMK at rest."),
            ("Event Replay Strategy", "Events", "Replay from offset with idempotent consumers; new consumer group for rebuild."),
            ("Ordering vs Throughput Trade", "Messaging", "Global FIFO kills throughput — scope ordering to entity."),
            ("Azure Functions Service Bus Trigger", "Azure", "Prefetch count tuning; max concurrent calls; DLQ handling in function."),
            ("CloudEvents Specification", "Events", "Standard envelope: type, source, id, time — interoperability across services."),
            ("Message Bus HA Design", "Messaging", "Zone-redundant namespace; geo-disaster pairing; documented RPO for messages."),
        ],
        "exp_scenarios": [
            ("DLQ Depth 50000 Messages", "DLQ flood after bad deploy — triage and replay in 14 days."),
            ("Duplicate Charge Events", "At-least-once caused double payment — idempotency fix in 30 days."),
            ("Kafka Rebalance Storm", "Consumer lag spike during deploy — rebalance tuning in 30 days."),
            ("Outbox Relay Stuck", "Events not publishing 6 hours — relay monitoring in 14 days."),
            ("Saga Compensation Failed", "Refund failed mid-saga — manual intervention queue in 30 days."),
            ("Schema Breaking Change", "Consumer crash loop — schema compatibility CI in 60 days."),
            ("Service Bus Throttling", "Hit messaging units limit — capacity plan in 30 days."),
            ("Event Order Violation", "Inventory deducted before payment — saga redesign in 60 days."),
            ("Poison Message Loop", "Message reprocessed infinitely — DLQ policy in 14 days."),
            ("Cross-Service Event Storm", "Circular events melted CPU — choreography audit in 30 days."),
            ("Message Loss Claim", "Customer says order lost — durability audit and fix."),
            ("Session Lock Timeout", "FIFO broken under load — session handler tuning."),
            ("Event Hub Lag Analytics", "Consumers 2 hours behind — scale-out plan in 30 days."),
            ("No DLQ Monitoring", "DLQ grew 3 months unnoticed — alerting in 7 days."),
            ("Outbox Table Bloat", "Millions of unpublished rows — retention and relay fix."),
            ("Kafka Key Hot Partition", "One partition 90% traffic — key redesign in 60 days."),
            ("Service Bus Premium Migration", "Standard tier limits hit — Premium migration 90 days."),
            ("Event Replay Production", "Need rebuild read model — replay runbook in 30 days."),
            ("Message PII Leak", "Events contain email in clear — schema scrub in 14 days."),
            ("Saga Timeout Undefined", "Stuck sagas never complete — timeout compensation in 30 days."),
        ],
    },
    36: {
        "category": "System Design Capstone",
        "adv_topics": [
            ("E-Commerce High-Level Design", "E-Commerce", "Catalog, cart, checkout, payment, inventory, search — async order fulfillment."),
            ("Checkout Flow Design", "Checkout", "Reserve inventory → payment → confirm → async ship; saga with compensation."),
            ("Uber-Like Matching Design", "Ride-Sharing", "Geospatial index, driver location stream, matching algorithm, surge pricing cache."),
            ("Notification System Design", "Notifications", "Multi-channel fanout, template engine, preference center, rate limit per user."),
            ("Search System Design", "Search", "Elasticsearch indexing pipeline, query parsing, ranking, autocomplete from trie/ES suggest."),
            ("Payment Idempotency Design", "Payments", "Idempotency-Key, ledger double-entry, webhook dedup, reconciliation batch."),
            ("Inventory Consistency Design", "E-Commerce", "Optimistic concurrency, reservation TTL, oversell prevention audit."),
            ("Cart Service Redis Design", "E-Commerce", "Redis hash per cart; TTL 30 days; merge anonymous on login."),
            ("Product Catalog CDN Design", "E-Commerce", "CDN cache product pages; API cache-aside; invalidation on price change event."),
            ("Order Status Tracking", "E-Commerce", "State machine; WebSocket or SSE push; event sourcing optional for audit."),
            ("Recommendation Engine Integration", "E-Commerce", "Async batch + real-time feature store; fallback to popular if model down."),
            ("Flash Sale Architecture", "E-Commerce", "Queue checkout, waiting room, cache inventory count, rate limit."),
            ("Driver Location Geospatial", "Ride-Sharing", "Redis GEO or H3 cells; update stream Kafka; query nearest N drivers."),
            ("Surge Pricing Design", "Ride-Sharing", "Demand/supply ratio per geohash; cache multiplier; broadcast price update."),
            ("Ride Matching Algorithm", "Ride-Sharing", "Greedy nearest; batch matching at scale; cancel and re-match flow."),
            ("Push Notification Scale", "Notifications", "APNs/FCM token registry; batch send; priority queue for OTP."),
            ("Email SMS Notification Pipeline", "Notifications", "Queue workers per channel; provider failover; unsubscribe compliance."),
            ("Notification Preference Store", "Notifications", "Per-user channel prefs; quiet hours; GDPR marketing opt-out."),
            ("Search Index Pipeline", "Search", "CDC from DB → Kafka → ES bulk index; alias swap for reindex."),
            ("Autocomplete Latency", "Search", "ES completion suggester <50ms; prefix cache; debounce client."),
            ("Full Stack Observability Design", "Capstone", "Trace checkout path end-to-end; SLO per step; alert on burn."),
            ("Multi-Region E-Commerce", "E-Commerce", "Read local catalog; write central orders or cell-based users."),
            ("Fraud Detection Hook", "Payments", "Pre-auth fraud score; async ML; block high-risk before capture."),
            ("Return Refund Flow", "E-Commerce", "Reverse saga; inventory return; partial refund state machine."),
            ("Wishlist and Personalization", "E-Commerce", "User-scoped data; event stream for recommendations."),
            ("Rate Limit Public APIs", "API Design", "Tier per API key; sliding window Redis; 429 response."),
            ("API Gateway Aggregation", "API Design", "BFF aggregates cart+user+promo; reduce chatty mobile calls."),
            ("Data Model E-Commerce", "Data Model", "Orders, line items, payments, shipments — access pattern driven."),
            ("Capstone Time Management", "Interview Skills", "45-min full design: 5 clarify, 10 boxes, 20 checkout deep dive, 5 scale."),
            ("Capstone Phased Evolution", "Interview Skills", "MVP → scale → global — close every capstone with phases."),
        ],
        "exp_scenarios": [
            ("45-Min E-Commerce Whiteboard", "Full timed e-commerce design with panel feedback — capstone mock."),
            ("Checkout Double Charge Incident", "Design review: what failed in checkout architecture."),
            ("Uber Surge Outage Design", "Surge pricing bug — geospatial architecture postmortem design."),
            ("Notification Delay 2 Hours", "Redesign notification pipeline for 99% <30s delivery."),
            ("Search Zero Results Revenue Hit", "Search ranking and fallback architecture fix in 60 days."),
            ("Flash Sale Complete Failure", "End-to-end flash sale architecture retrospective and redesign."),
            ("Payment Reconciliation Gap", "$2M discrepancy — ledger and reconciliation design."),
            ("Inventory Oversell Black Friday", "Consistency model redesign before next event."),
            ("Multi-Region Checkout Latency", "200ms p99 global — cell architecture for checkout."),
            ("Notification Opt-Out Compliance", "GDPR complaint — preference architecture in 30 days."),
            ("Ride Matching Unfairness", "Algorithm bias allegations — matching design review."),
            ("Cart Abandonment Scale", "10M abandoned carts — storage and cleanup architecture."),
            ("Search Index 6 Hour Lag", "Near-real-time indexing architecture in 90 days."),
            ("Capstone Interviewer Scale Twist", "10× users mid-mock — adapt design under pressure."),
            ("Capstone Security Twist PCI", "Add PCI mid-session — scope minimization response."),
            ("Capstone Multi-Tenant Twist", "B2B SaaS added mid-mock — tenant isolation adaptation."),
            ("Capstone GDPR Delete Twist", "Right to delete added — saga delete orchestration."),
            ("Capstone Cost Cut 40%", "VP cost reduction — architecture trade-off negotiation."),
            ("Capstone Panel Defense", "Defend monolith choice to skeptical principal engineer."),
            ("Capstone Retrospective Plan", "Post-mock improvement plan for next capstone session."),
        ],
    },
}


def build_intermediate_i(week_num, topics_config):
    """Build 10 intermediate questions from week theme."""
    themes = {
        30: [
            ("CI/CD Pipeline Purpose", "CI automates build/test; CD automates deploy to environments; goal is small safe frequent releases."),
            ("GitHub Actions Basics", "Workflow YAML triggered on push/PR; jobs, steps, actions marketplace; secrets from repo/org settings."),
            ("Azure DevOps Pipelines", "YAML multi-stage pipelines; build artifacts; release gates; integration with Azure RBAC."),
            ("Blue-Green Deployment", "Two identical environments; deploy to idle; swap traffic; instant rollback by swap back."),
            ("Canary Deployment", "Route small % traffic to new version; monitor metrics; promote or rollback automatically."),
            ("Build Artifact Immutability", "Same binary/container digest promoted dev→prod; never rebuild for production deploy."),
            ("Pipeline Environment Secrets", "Azure Key Vault integration; OIDC federated credentials; no plaintext secrets in YAML."),
            ("Automated Testing in CI", "Unit → integration → smoke in pipeline; fail fast; parallel test execution."),
            ("Database Migration in CD", "Backward-compatible migrations only in pipeline; expand-contract for breaking schema."),
            ("Rollback Strategy CI/CD", "Automated rollback on health check failure; previous artifact always retained N versions."),
        ],
        31: [
            ("Infrastructure as Code Definition", "Declarative resource definitions in Git; reproducible environments; reviewable infra changes."),
            ("Bicep vs ARM Templates", "Bicep transpiles to ARM; cleaner syntax; first-class Azure support; what-if preview."),
            ("Terraform Core Concepts", "Providers, resources, state, plan/apply; HCL syntax; module composition."),
            ("IaC State Management", "State tracks real-world mapping; remote backend with locking; never commit state to Git."),
            ("Drift Detection Concept", "Compare desired (Git) vs actual (cloud); scheduled plan; alert on manual portal changes."),
            ("GitOps for Infrastructure", "Git as source of truth; automated sync to cloud; PR review for infra changes."),
            ("IaC Module Reuse", "Parameterized modules for VNet, AKS; versioned; consumed by workload repos."),
            ("Policy as Code Basics", "Azure Policy / OPA enforce tags, regions, SKUs; deny non-compliant deploys."),
            ("Landing Zone Concept", "Pre-configured subscription hierarchy, networking, identity, governance for workloads."),
            ("IaC Benefits Over Click-Ops", "Reproducibility, audit trail, disaster recovery from Git, team collaboration."),
        ],
        32: [
            ("Observability Three Pillars", "Metrics (aggregated numbers), logs (events), traces (request flow) — correlated via traceId."),
            ("OpenTelemetry Overview", "Vendor-neutral instrumentation; auto-instrument .NET; export OTLP to Azure Monitor."),
            ("SLI vs SLO vs SLA", "SLI measures; SLO internal target; SLA contractual commitment — SLO stricter than SLA."),
            ("Application Insights Basics", "Azure APM; dependency tracking; live metrics; integration with .NET SDK."),
            ("Structured Logging Benefits", "JSON queryable fields; correlation; no regex parsing in production."),
            ("Distributed Tracing Value", "See cross-service latency; find slow dependency; debug microservices."),
            ("Dashboard Design Principles", "Actionable metrics; SLO-first; avoid dashboard sprawl; hierarchy L1/L2/L3."),
            ("Alerting Best Practices", "Alert on symptoms; runbook linked; reduce noise; on-call rotation integration."),
            ("Metric Cardinality Problem", "High-cardinality labels explode cost; never userId on metrics; use logs for detail."),
            ("Sampling in Production", "Trace/log sampling reduces cost; always keep errors; tail sampling for rare bugs."),
        ],
        33: [
            ("RESHADED Acronym", "Requirements, Estimation, Storage, High-level, API, Data model, Estimation, Deep-dive — interview framework."),
            ("System Design Interview Flow", "Clarify → estimate → diagram → deep dive → trade-offs → wrap — time-box each."),
            ("Requirements Clarification", "Ask about scale, users, read/write, consistency, latency before designing."),
            ("Back-of-Envelope Math", "QPS, storage, bandwidth — round assumptions; state aloud for interviewer correction."),
            ("API Design in Interviews", "REST resources, pagination, errors, auth — sketch key endpoints early."),
            ("Failure Modes Brainstorm", "What if DB down, cache miss, network partition — show resilience thinking."),
            ("Scope Management Technique", "Explicit in/out of scope; parking lot; don't gold-plate v1."),
            ("Trade-off Communication", "SQL vs NoSQL table with pros/cons and your choice — decisive but flexible."),
            ("High-Level Diagram Discipline", "5-7 boxes; label protocols; iterate don't erase — add revision box."),
            ("Phased Evolution Close", "MVP → scale phases triggered by metrics — pragmatic architect signal."),
        ],
        34: [
            ("Cache-Aside Pattern", "App checks cache, on miss reads DB and populates; on write updates DB and invalidates."),
            ("CDN Purpose", "Edge cache static and cacheable API; reduce latency and origin load; purge/version strategy."),
            ("Database Sharding Concept", "Horizontal partition by shard key; scale writes; avoid cross-shard hot path queries."),
            ("Read Replica Use Cases", "Offload analytics and browse; not for read-your-writes without routing logic."),
            ("Load Balancing Types", "L4 TCP distribute; L7 HTTP route by path; health checks remove sick instances."),
            ("Hot Key Problem", "Disproportionate traffic to one cache key; split, local cache, or coalescing mitigations."),
            ("Cache Stampede", "Many requests miss expired key simultaneously; jitter TTL, single-flight, pre-warm."),
            ("Consistent Hashing Purpose", "Minimize key remap when cache nodes added/removed in distributed cluster."),
            ("Autoscaling Concept", "Horizontal pod/instance scale on CPU, queue depth, custom metrics; scale-in carefully."),
            ("Connection Pool Exhaustion", "Limited DB connections; size pool × pods < max_connections; monitor wait time."),
        ],
        35: [
            ("Event-Driven Architecture", "Services communicate via events; loose coupling; async processing; eventual consistency."),
            ("Kafka vs Service Bus", "Kafka: high-throughput log, replay. Service Bus: enterprise messaging, sessions, DLQ."),
            ("Saga Pattern Purpose", "Distributed transaction across services; compensating actions on failure."),
            ("Outbox Pattern Reliability", "Atomic DB write + outbox; relay publishes; no dual-write inconsistency."),
            ("Idempotent Consumer", "Same message processed once effect; messageId dedup table; safe at-least-once."),
            ("Message Ordering Scope", "FIFO per partition/session/entity — not global across system."),
            ("Dead Letter Queue Purpose", "Poison messages isolated after max retries; manual triage; prevent block."),
            ("At-Least-Once Delivery", "Default for most buses; design consumers idempotent; embrace not fight."),
            ("Event Schema Versioning", "Additive changes backward compatible; breaking changes need new topic/version."),
            ("Competing Consumers", "Multiple workers same subscription; scale with partition count."),
        ],
        36: [
            ("E-Commerce Core Services", "Catalog, cart, checkout, payment, inventory, order, search — identify in any retail design."),
            ("Checkout Saga Overview", "Multi-step distributed flow with compensation; payment + inventory + shipping."),
            ("Uber Design Components", "Riders, drivers, matching, geospatial, pricing, trip state machine."),
            ("Notification System Channels", "Push, email, SMS — fanout, templates, preferences, rate limits."),
            ("Search Architecture Basics", "Index pipeline, query service, ranking, autocomplete — ES common choice."),
            ("Capstone Time Boxing", "45 minutes: clarify 5, diagram 10, deep dive 20, trade-offs 5, buffer 5."),
            ("Idempotency in Checkout", "Idempotency-Key on place-order; prevent double charge on retry."),
            ("Inventory Reservation", "Soft reserve on checkout start; TTL releases; prevent oversell."),
            ("Observability in Capstone", "Always close with metrics, traces, SLO — checkout p99 alert example."),
            ("Phased Capstone Evolution", "Phase 1 monolith+SQL; Phase 2 cache+queue; Phase 3 shard+multi-region."),
        ],
    }
    cat = topics_config["category"]
    items = themes.get(week_num, [])
    result = []
    for i, (title, short_core) in enumerate(items[:10]):
        result.append(T(
            title, cat, "Very Common" if i < 6 else "Common",
            f"Explain {title.lower()} for a system design or architecture interview.",
            short_core,
            f"**{title}:**\n\n{short_core}\n\n**Production context (.NET/Azure):**\n"
            f"Apply in ASP.NET Core on Azure App Service or AKS with patterns from week {week_num}.\n\n"
            f"**Key points:**\n- When to use vs avoid\n- Measurable outcome (latency, DORA, SLO)\n"
            f"- Common production pitfall and mitigation\n\n"
            f"**Example:** Instrument with Application Insights; track deployment in Azure DevOps.\n\n"
            f"**Architect:** Capture trade-offs in ADR when multiple valid approaches exist.",
            f"{title} is foundational for week {week_num} — articulate clearly before tool names.",
            f"How measure success? — Tie {title.lower()} to SLI, DORA metric, or business KPI.",
            f"Common anti-pattern? — Adopting tools before understanding {title.lower()} principles.",
            f"Define {title.lower()} with buzzwords only",
            "No concrete Azure/.NET example",
            "Cannot link concept to measurable outcome",
        ))
    return result


def _adv_detailed(week_num, title, subcat, core):
    wk = {29: "DevOps", 30: "CI/CD", 31: "IaC", 32: "Observability",
          33: "System Design", 34: "Scalability", 35: "Messaging", 36: "Capstone"}[week_num]
    dotnet_snippets = {
        "DevSecOps": '''```yaml\n# GitHub Actions — security gate on PR\n- name: CodeQL\n  uses: github/codeql-action/analyze@v3\n- name: Dependency scan\n  run: dotnet list package --vulnerable\n```''',
        "CI/CD": '''```yaml\n# Multi-stage Azure DevOps\nstages:\n- stage: Build\n  jobs: [build, test, sbom]\n- stage: DeployProd\n  dependsOn: Build\n  condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))\n```''',
        "IaC": '''```bicep\nmodule vnet 'br/public:avm/res/network/virtual-network:0.1.0' = {\n  params: { name: 'vnet-${environment}' }\n}\n```''',
        "Observability": '''```csharp\nbuilder.Services.AddOpenTelemetry()\n    .WithTracing(t => t.AddAspNetCoreInstrumentation()\n        .AddHttpClientInstrumentation())\n    .UseAzureMonitor();\n```''',
        "Messaging": '''```csharp\nawait using var tx = await _db.Database.BeginTransactionAsync();\nawait _db.Orders.AddAsync(order);\nawait _db.Outbox.AddAsync(new OutboxMessage(eventPayload));\nawait tx.CommitAsync();\n```''',
        "Caching": '''```csharp\nvar cached = await _cache.GetAsync<Product>(key);\nif (cached is null) {\n    cached = await _db.Products.FindAsync(id);\n    await _cache.SetAsync(key, cached, TimeSpan.FromMinutes(5));\n}\n```''',
    }
    snippet_key = subcat if subcat in dotnet_snippets else (
        "CI/CD" if week_num == 30 else "IaC" if week_num == 31 else
        "Observability" if week_num == 32 else "Messaging" if week_num == 35 else
        "Caching" if week_num == 34 else "DevSecOps")
    snippet = dotnet_snippets.get(snippet_key, dotnet_snippets["CI/CD"])
    return (
        f"**{title}** ({wk} context)\n\n{core}\n\n**Production implementation:**\n{snippet}\n\n"
        f"**Trade-offs:**\n| Option | When to choose | Risk |\n|--------|----------------|------|\n"
        f"| Managed Azure service | Team <10 ops engineers | Cost at scale |\n"
        f"| Self-managed OSS | Deep customization need | Ops toil |\n"
        f"| Hybrid | Enterprise compliance | Integration complexity |\n\n"
        f"**Conflict resolution:** When platform and stream teams disagree, use ADR with measured pilot "
        f"on one squad for 2 weeks before org-wide mandate.\n\n"
        f"**Operational readiness:** Dashboard, alert, and runbook required before production cutover.\n\n"
        f"**Architect:** Document rollback trigger — e.g., CFR >20% for 48h after adoption."
    )


def _exp_detailed(title, scenario, week_num):
    wk_names = {29: "DevOps culture", 30: "CI/CD", 31: "IaC", 32: "observability",
                33: "system design practice", 34: "scalability", 35: "messaging", 36: "capstone design"}
    return (
        f"**Situation:** {scenario}\n\n"
        f"**Immediate (Days 1–7):**\n- Form tiger team with platform + stream DRI\n"
        f"- Stabilize customer impact; exec comms every 24h\n"
        f"- Preserve evidence: deploy logs, traces, config snapshots\n\n"
        f"**30-day plan:**\n| Week | Focus | Deliverable |\n|------|-------|-------------|\n"
        f"| 1 | Triage + postmortem | Blameless doc, action owners |\n"
        f"| 2 | Baseline metrics | DORA/SLO dashboard before state |\n"
        f"| 3 | Pilot fix one squad | Measured improvement vs control |\n"
        f"| 4 | Runbook + training | Documented standard for {wk_names[week_num]} |\n\n"
        f"**90-day plan:**\n- **Days 31–60:** Roll out pattern to all affected teams; "
        f"platform self-service to remove bottlenecks\n"
        f"- **Days 61–90:** Policy/gates in CI; game day validation; steering review with trend charts\n\n"
        f"**Success metrics:** Lead time, MTTR, CFR, or adoption % — targets set from baseline, not arbitrary.\n\n"
        f"**Stakeholder map:** VP Engineering sponsor, affected product director, platform lead.\n\n"
        f"**Azure/.NET example:** Instrument fix in Application Insights; tag deployments to correlate "
        f"with change failure rate improvement.\n\n"
        f"**Architect:** Residual risk documented with expiry review date — not 'monitor' alone."
    )


def build_advanced(week_num, topics_config):
    result = []
    for title, subcat, core in topics_config["adv_topics"][:30]:
        q_text = (
            f"How would you implement {title} with trade-offs and conflict resolution in production?"
            if week_num != 33 else
            f"Apply {title} during a 45-minute system design interview — what do interviewers expect?"
        )
        result.append(T(
            title, subcat, "Very Common" if len(result) < 20 else "Common",
            q_text,
            core,
            _adv_detailed(week_num, title, subcat, core),
            f"{title} separates senior architects who've operated systems from those who've only read docs.",
            f"What breaks at 10× scale? — {subcat}-specific bottleneck: throughput, coupling, or cost ceiling.",
            f"Rollback plan? — Feature flag, Git revert + pipeline apply, or traffic shift — pick per blast radius.",
            "Choosing tools before requirements are clear",
            "No documented trade-off between speed and safety",
            "Enabling in production without observability and runbook",
        ))
    return result


def build_expert(week_num, topics_config):
    cat = topics_config["category"]
    result = []
    for title, scenario in topics_config["exp_scenarios"][:20]:
        situation = scenario.split("—")[0].strip().lower()
        result.append(T(
            title, cat, "Very Common" if len(result) < 12 else "Common",
            f"What do you do when {situation}?",
            "Stabilize, measure baseline, 30-day pilot fix, 90-day org-wide rollout with executive checkpoints.",
            _exp_detailed(title, scenario, week_num),
            "Expert scenarios test program leadership — structured plans beat ad-hoc heroics.",
            "CEO demands skip pilot? — Risk matrix with phased alternative; written acceptance if override.",
            "Prove success? — Before/after dashboard on DORA or SLO — not team sentiment alone.",
            "Jump to permanent tooling before stabilizing the incident",
            "Single 90-day big-bang without 30-day quick wins",
            "No measurable success criteria or executive sponsor",
        ))
    return result


def main():
    sections = ['"""Extra premium Q&A tuples for Weeks 29–36 banks (480 questions)."""\n']
    counts = {}

    # Week 29 uses hand-crafted EXTRA_I
    sections.append(write_list("W29_EXTRA_I", W29_EXTRA_I))
    counts["W29_EXTRA_I"] = len(W29_EXTRA_I)

    for week in range(29, 37):
        cfg = WEEK_TOPICS[week]
        if week != 29:
            extra_i = build_intermediate_i(week, cfg)
            sections.append(write_list(f"W{week}_EXTRA_I", extra_i))
            counts[f"W{week}_EXTRA_I"] = len(extra_i)

        adv = build_advanced(week, cfg)
        exp = build_expert(week, cfg)
        sections.append(write_list(f"W{week}_ADVANCED", adv))
        sections.append(write_list(f"W{week}_EXPERT", exp))
        counts[f"W{week}_ADVANCED"] = len(adv)
        counts[f"W{week}_EXPERT"] = len(exp)

    # Verification block
    sections.append("\n# ─── Count verification ───")
    total = 0
    for week in range(29, 37):
        for tier, expected in [("EXTRA_I", 10), ("ADVANCED", 30), ("EXPERT", 20)]:
            name = f"W{week}_{tier}"
            n = counts[name]
            total += n
            sections.append(f"assert len({name}) == {expected}  # actual: {n}")
    sections.append(f"assert {total} == 480  # total questions")

    OUTPUT.write_text("\n\n".join(sections) + "\n")
    print(f"Wrote {OUTPUT} ({total} questions)")


if __name__ == "__main__":
    main()
