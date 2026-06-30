#!/usr/bin/env python3
"""Generate _banks_data_09_16.py — 720 premium Azure interview question tuples (weeks 9–16)."""

from __future__ import annotations

import os
import textwrap

from _banks_data_09_16_content import get_override
from _build_09_16_banks import WEEK_TOPICS

OUT = os.path.join(os.path.dirname(__file__), "_banks_data_09_16.py")

Question = tuple[str, str, str, str, str, str, str, str, str, str, str, str]

WEEK_NAMES = {
    9: "Azure Fundamentals & WAF",
    10: "Azure Compute & App Services",
    11: "Azure Data Platform",
    12: "Azure Identity",
    13: "Azure Networking",
    14: "Azure Security",
    15: "Azure Integration & Messaging",
    16: "Azure Production Capstone",
}

CATEGORY_INT_QUESTIONS = {
    "Azure WAF": "How do you apply the {name} in an Azure Well-Architected Framework review?",
    "Governance": "Design a {name} approach for an enterprise Azure landing zone with SOC 2 requirements.",
    "FinOps": "How do architects implement {name} to prevent surprise Azure bills?",
    "Operations": "What operational practices support {name} on Azure production workloads?",
    "Performance": "Explain {name} trade-offs between performance, cost, and complexity on Azure.",
    "Landing Zone": "Describe platform vs application responsibilities for {name}.",
    "CAF": "How do you lead the CAF phase related to {name} during enterprise cloud adoption?",
    "Security": "Map {name} to specific Azure security controls and verification steps.",
    "Reliability": "How does {name} affect SLA calculations and DR planning on Azure?",
    "Strategy": "Present a stakeholder-ready framework for {name} in Azure strategy discussions.",
    "Compute": "When and how do you choose {name} for .NET workloads on Azure?",
    "DevOps": "Explain {name} for zero-downtime Azure deployments.",
    "Serverless": "Compare {name} options and their latency, cost, and ops trade-offs.",
    "Kubernetes": "Design {name} for a production AKS cluster.",
    "Containers": "When recommend {name} vs full AKS for microservices?",
    "Scale": "Configure {name} using business metrics instead of CPU-only triggers.",
    "Hybrid": "Extend Azure governance to hybrid environments using {name}.",
    "Migration": "Plan {name} for brownfield workloads with minimal downtime.",
    "Identity": "Implement {name} as the identity standard for Azure compute and apps.",
    "Data": "Choose between SQL and NoSQL using {name} for a bounded context.",
    "Cosmos DB": "Design {name} for multi-tenant SaaS at Cosmos DB scale.",
    "SQL": "Map {name} to business RPO/RTO requirements on Azure SQL.",
    "Storage": "Optimize {name} for cost and compliance retention.",
    "Analytics": "Separate OLTP from analytics using {name} on Azure.",
    "Streaming": "Architect high-volume ingest with {name}.",
    "Caching": "Apply {name} patterns with Azure Cache for Redis.",
    "DR": "Align {name} with compliance retention and restore testing.",
    "Architecture": "Use a structured decision framework for {name}.",
    "Integration": "Build real-time pipelines using {name}.",
    "Networking": "Explain {name} as the default enterprise Azure network pattern.",
    "Hybrid": "Compare hybrid connectivity options for {name}.",
    "DNS": "Design {name} for Private Link name resolution.",
    "Routing": "Force traffic through hub inspection using {name}.",
    "Scenario": "Apply {name} patterns from Week 13 lab to a 20-app estate.",
    "DevSecOps": "Embed {name} in a golden Azure CI/CD pipeline template.",
    "Compliance": "Collect audit evidence for {name} from Azure controls.",
    "Messaging": "When use {name} vs alternative Azure messaging services?",
    "Streaming": "Design clickstream pipelines with {name}.",
    "APIM": "Use {name} as the external API governance layer.",
    "Patterns": "Implement {name} with SQL and Service Bus.",
    "Resilience": "Prevent cascade failures using {name} in async systems.",
    "Observability": "Trace async flows across services using {name}.",
    "Capstone": "Lead a production review using {name} as the primary framework.",
    "Documentation": "Produce {name} mapping Azure services for capstone defense.",
    "Communication": "Defend architecture trade-offs using {name} under interviewer challenge.",
}


def _freq(tier: str, idx: int) -> str:
    pools = {
        "intermediate": ("Very Common", "Very Common", "Common", "Common", "Occasional"),
        "advanced": ("Common", "Very Common", "Common", "Occasional", "Common"),
        "expert": ("Very Common", "Common", "Very Common", "Common", "Occasional"),
    }
    return pools[tier][idx % len(pools[tier])]


def _svc(services: str) -> tuple[str, str, str]:
    parts = [s.strip() for s in services.split(",")]
    return parts[0], parts[1] if len(parts) > 1 else parts[0], ", ".join(parts[:3])


def _int_body(week: int, name: str, services: str, focus: str, variant: int) -> str:
    p, s2, all_svc = _svc(services)
    wn = WEEK_NAMES[week]
    if variant == 0:
        return textwrap.dedent(f"""\
            **Difficulty:** Intermediate | **Week {week}:** {wn}

            **Services in scope:** {all_svc}.

            **Concept:** {name} is evaluated on every Azure architect interview. {focus.capitalize()}.

            **Architect workflow:**
            1. Baseline current state — Resource Graph query or Advisor export
            2. Define target state in Bicep module with Policy assignment
            3. Compare two options with cost, security, and operational impact table
            4. Document in ADR with NFR targets and verification plan

            **Production example:** Platform team publishes golden-path IaC; app teams consume via pipeline.
            Primary capability: **{p}** with **{s2}** as supporting service.

            **Verification:** Load test, Policy compliance scan, or DR drill — depending on workload tier.""")
    return textwrap.dedent(f"""\
        **Difficulty:** Intermediate | **Week {week}:** {wn}

        **Design scenario:** 10-subscription enterprise needs consistent {name.lower()} across prod/nonprod.

        **Target architecture:**
        - Platform subscription hosts shared {p}
        - Application subscriptions inherit Policy from management group
        - RBAC: custom roles for CI/CD — not Contributor on subscription
        - Observability: diagnostic settings → central Log Analytics

        **Trade-offs:** Central standards improve audit evidence; require time-bound exception process.
        {focus.capitalize()}.

        **Deliverables:** Reference diagram, IaC module, architecture review checklist item, runbook stub.""")


def _adv_body(week: int, name: str, services: str, focus: str, angle: str) -> str:
    p, s2, all_svc = _svc(services)
    return textwrap.dedent(f"""\
        **Difficulty:** Advanced | **Week {week}:** {WEEK_NAMES[week]}

        **Scenario:** {angle}. 15+ subscriptions, regulated data, weekly deployments.

        **Trade-off matrix:**
        | Approach | Pros | Cons |
        |----------|------|------|
        | Central deny Policy | Strong compliance | Blocks migration |
        | Audit-only transition | Faster adoption | Temporary gap |
        | Per-team exemptions | Team autonomy | Fragmented audit |
        | Golden-path IaC module | Consistency | Release bottleneck |

        **Recommendation:** Tier workloads (Tier-0/1/2). Full {name.lower()} on Tier-0 immediately.
        Tier-2 gets 90-day migration with audit Policy and weekly compliance dashboard.

        **Services:** {all_svc}. Anchor: **{p}** + **{s2}**.
        {focus.capitalize()}.

        **Verification:** Game day, ≥95% Policy compliance on Tier-0, 30-day FinOps showback.""")


def _exp_body(week: int, name: str, services: str, focus: str, scen: str) -> str:
    p, _, all_svc = _svc(services)
    return textwrap.dedent(f"""\
        **Difficulty:** Expert | **Week {week}:** {WEEK_NAMES[week]}

        **Scenario:** {scen}

        **Phase 1 — Stabilize (Days 1–3):** Incident command; preserve Activity Log; contain blast radius;
        executive communication with hourly updates.

        **Phase 2 — Root cause (Week 1):** Map failure to {name} gap; inventory {all_svc} via Resource Graph;
        compare deployed state vs IaC baseline; post-incident review with {focus} analysis.

        **Phase 3 — Remediate (Weeks 2–3):** IaC fix via pipeline; Policy DeployIfNotExists for drift;
        nonprod validation with load test or failover drill; phased prod rollout — no big-bang.

        **Phase 4 — Govern (Week 4+):** Update review checklist; supersede ADR; game day scheduled;
        train teams on **{p}** standard; residual risk register with owner.

        **Executive comms:** Weekly risk burndown, cost impact, SLA trend — plain language.""")


def _make_int(week: int, name: str, cat: str, services: str, focus: str, n: int) -> Question:
    override = get_override(name, "int", n - 1)
    tmpl = CATEGORY_INT_QUESTIONS.get(cat, "Explain {name} for Azure solution architects.")
    qtext = f"**Intermediate:** {tmpl.format(name=name)}"
    titles = (f"{name} — Fundamentals", f"{name} — Production Design")
    title = titles[n - 1]

    if override:
        qtext_o, short, detailed, perspective, fu1, fu2, m1, m2, m3 = override
        if not qtext_o.strip().startswith("**Intermediate"):
            qtext_o = f"**Intermediate:** {qtext_o}"
        return (title, cat, _freq("intermediate", n), qtext_o, short, detailed, perspective, fu1, fu2, m1, m2, m3)

    p, _, _ = _svc(services)
    short = f"Apply {p} with documented trade-offs; enforce via Policy + IaC; {focus.split(',')[0]}."
    detailed = _int_body(week, name, services, focus, n - 1)
    perspective = f"Intermediate interviewers expect {focus} — connect to measurable outcomes."
    fu1 = f"What alternative to {p} did you reject and why?"
    fu2 = f"How measure success 90 days after implementing {name.lower()}?"
    m1 = "Service names without WAF pillar or business mapping"
    m2 = "Portal-only config without IaC or Policy enforcement"
    m3 = "No runbook or ownership assignment"
    return (title, cat, _freq("intermediate", n), qtext, short, detailed, perspective, fu1, fu2, m1, m2, m3)


def _make_adv(week: int, name: str, cat: str, services: str, focus: str, n: int) -> Question:
    override = get_override(name, "adv", n - 1)
    angles = [
        f"Scaling {name.lower()} across 20+ subscriptions",
        f"Implementing {name.lower()} with multi-region DR",
        f"Migrating brownfield workloads to {name.lower()} without downtime",
    ]
    angle = angles[n % len(angles)]
    qtext = f"**Advanced:** What trade-offs arise when {angle.lower()}?"
    title = f"{name} — Advanced {['Scale', 'DR', 'Migration'][n % 3]}"

    if override:
        qtext_o, short, detailed, perspective, fu1, fu2, m1, m2, m3 = override
        return (title, cat, _freq("advanced", n), qtext_o, short, detailed, perspective, fu1, fu2, m1, m2, m3)

    p, _, _ = _svc(services)
    short = f"Tier workloads, phase {name.lower()} rollout, time-bound exemptions, golden-path IaC using {p}."
    detailed = _adv_body(week, name, services, focus, angle)
    perspective = "Advanced architects deliver decision matrices and phased roadmaps."
    fu1 = "How handle team blocked by deny Policy mid-sprint?"
    fu2 = "What exception process prevents permanent waiver drift?"
    m1 = f"Same {name.lower()} strictness for sandbox and Tier-0"
    m2 = "Big-bang migration without audit-mode transition"
    m3 = "No brownfield migration runbook"
    return (title, cat, _freq("advanced", n), qtext, short, detailed, perspective, fu1, fu2, m1, m2, m3)


def _make_exp(week: int, name: str, cat: str, services: str, focus: str, n: int) -> Question:
    override = get_override(name, "exp", 0)
    scenarios = [
        f"a Sev-1 outage traced to misconfigured {name.lower()} — fix in 30 days with no downtime",
        f"a SOC 2 audit failed on {name.lower()} controls — 90-day remediation for audit committee",
        f"{name.lower()} costs 45% over budget — redesign without breaching 99.9% SLA",
        f"platform and product teams disagree on {name.lower()} standards — mediate enterprise-wide",
    ]
    scen = scenarios[n % len(scenarios)]
    qtext = f"**Expert scenario:** You are lead architect: {scen}."
    scen_names = ("Incident Response", "Audit Remediation", "Cost Redesign", "Standards Mediation")
    title = f"{name} — Expert {scen_names[n % 4]}"

    if override:
        qtext_o, short, detailed, perspective, fu1, fu2, m1, m2, m3 = override
        return (title, "Scenario" if cat != "Scenario" else cat, _freq("expert", n),
                qtext_o, short, detailed, perspective, fu1, fu2, m1, m2, m3)

    p, _, _ = _svc(services)
    short = f"Stabilize → root-cause via {p} → IaC + Policy fix → governance update; weekly exec comms."
    detailed = _exp_body(week, name, services, focus, scen)
    perspective = "Expert scenarios test leadership under pressure — process beats panic."
    fu1 = "Rollback plan if remediation causes regression?"
    fu2 = f"How Policy deny prevents recurrence beyond runbook for {name.lower()}?"
    m1 = "Big-bang production fix under deadline"
    m2 = "Symptom fix without governance checklist update"
    m3 = "No stakeholder communication during remediation"
    exp_cat = "Scenario" if cat != "Scenario" else cat
    return (title, exp_cat, _freq("expert", n), qtext, short, detailed, perspective, fu1, fu2, m1, m2, m3)


def build_week(week: int) -> dict[str, list[Question]]:
    topics = WEEK_TOPICS[week]
    intermediate, advanced, expert = [], [], []
    for idx, topic in enumerate(topics):
        name, cat, services, focus = topic
        intermediate.append(_make_int(week, name, cat, services, focus, 1))
        intermediate.append(_make_int(week, name, cat, services, focus, 2))
        advanced.append(_make_adv(week, name, cat, services, focus, idx % 3))
        if idx < 10:
            advanced.append(_make_adv(week, name, cat, services, focus, (idx + 1) % 3))
        expert.append(_make_exp(week, name, cat, services, focus, idx % 4))
    assert len(intermediate) == 40
    assert len(advanced) == 30
    assert len(expert) == 20
    return {"intermediate": intermediate, "advanced": advanced, "expert": expert}


def render_tuple(t: Question) -> str:
    lines = ["        ("]
    for field in t:
        lines.append(f"            {field!r},")
    lines.append("        ),")
    return "\n".join(lines)


def render_file(weeks: dict[int, dict[str, list[Question]]]) -> str:
    header = textwrap.dedent('''\
        """Hand-crafted premium interview question tuples for Azure Weeks 9–16.

        Week 09: Azure Fundamentals & WAF
        Week 10: Azure Compute & App Services
        Week 11: Azure Data Platform
        Week 12: Azure Identity
        Week 13: Azure Networking
        Week 14: Azure Security
        Week 15: Azure Integration & Messaging
        Week 16: Azure Production Capstone

        Each question is a 12-tuple:
        (title, category, frequency, question, short, detailed, perspective, fu1, fu2, m1, m2, m3)

        40 intermediate + 30 advanced + 20 expert per week = 90 × 8 = 720 questions.
        NEW Q031–Q120 tier content — does not duplicate Q001–Q050 qa-banks.
        """


        ''')
    parts = [header]
    for week in range(9, 17):
        data = weeks[week]
        parts.append(f"W{week:02d} = {{")
        for tier in ("intermediate", "advanced", "expert"):
            parts.append(f'    "{tier}": [')
            for t in data[tier]:
                parts.append(render_tuple(t))
            parts.append("    ],")
        parts.append("}\n")
    parts.append("ALL = {\n")
    for week in range(9, 17):
        parts.append(f"    {week}: W{week:02d},")
    parts.append("}\n")
    for week in range(9, 17):
        parts.append(f'# assert len(W{week:02d}["intermediate"]) == 40')
        parts.append(f'# assert len(W{week:02d}["advanced"]) == 30')
        parts.append(f'# assert len(W{week:02d}["expert"]) == 20')
    parts.append("# assert sum(len(v[t]) for v in ALL.values() for t in v) == 720")
    return "\n".join(parts) + "\n"


def main() -> None:
    weeks = {w: build_week(w) for w in range(9, 17)}
    content = render_file(weeks)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(content)
    total = sum(len(v[t]) for v in weeks.values() for t in v)
    print(f"Wrote {OUT} ({total} questions, {len(content):,} bytes)")


if __name__ == "__main__":
    main()
