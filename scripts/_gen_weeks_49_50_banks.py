#!/usr/bin/env python3
"""Generate premium_qa_data_weeks_49_50_banks.py from existing Q001-Q030 + extra banks."""

from __future__ import annotations

import os

from premium_qa_data import q
from premium_qa_data_weeks_49_52_q001_q005 import WEEK_49_Q001_Q005, WEEK_50_Q001_Q005
from premium_qa_data_weeks_49_52_q006_q030 import WEEK_49_Q006_Q030, WEEK_50_Q006_Q030

OUT = os.path.join(os.path.dirname(__file__), "premium_qa_data_weeks_49_50_banks.py")

# Tuple: title, category, frequency, question, short, detailed, perspective, fu1, fu2, m1, m2, m3
def _qs(rows):
    return [q(*r) for r in rows]


W49_I_EXTRA = _qs([
    ("Tenant Isolation Tiers", "Whiteboard Mock", "Very Common",
     "What tenant isolation tiers should you present in a multi-tenant SaaS whiteboard?",
     "Standard (shared + RLS), professional (schema-per-tenant), enterprise (dedicated silo). Match tier to compliance, revenue, and noisy-neighbor risk.",
     "**Tier model:**\n| Tier | Isolation | Ops | When |\n|------|-----------|-----|------|\n| Standard | Shared DB + tenantId + RLS | Low | SMB |\n| Professional | Schema per tenant | Medium | Mid-market |\n| Enterprise | Dedicated DB/cluster | High | HIPAA/regulated |\n\n**Must cover:** JWT `tenant_id`, per-tenant rate limits, observability dimension, backup/export per tenant.\n\n**Upsell path:** Migration runbook from RLS → schema → silo without rewrite.",
     "Isolation tiers show commercial and technical alignment — not one-size-fits-all.",
     "Noisy neighbor controls per tier? — Rate limits, pool caps, fair queue scheduling.",
     "Cross-tenant admin? — Break-glass role with audit — never default query.",
     "Microservice per tenant by default",
     "No enterprise dedicated option",
     "Tenant missing from logs and metrics"),
    ("Acquisition Discovery Checklist", "Whiteboard Mock", "Very Common",
     "What discovery checklist opens an acquisition integration architecture mock?",
     "Systems of record, data quality, volume/SLAs, team skills, customer overlap, regulatory constraints, and decommission timeline before drawing integration.",
     "**Discovery checklist:**\n1. Inventory APIs, batch jobs, data stores\n2. Identify system of record per domain (orders, customers, billing)\n3. Data quality score — duplicates, null keys, currency rules\n4. Transaction volume and peak patterns\n5. Acquired team retention and skill map\n6. Customer overlap — migrate all or new-only?\n7. Contractual/regulatory constraints\n8. Hard decommission date or flexible?\n\n**Output:** Current-state context diagram + integration risk list before target state.\n\n**Governance:** Joint integration squad with executive milestone map.",
     "Acquisition mocks fail when integration is drawn before inventory.",
     "Strangler default? — Yes unless EOL forces big-bang — state in opening.",
     "Golden customer record? — Identity mapping table is first-class artifact.",
     "API design before systems-of-record map",
     "Ignoring legacy data quality",
     "No rollback cohort strategy"),
    ("Migration Wave Criteria", "Whiteboard Mock", "Very Common",
     "How define migration wave criteria in a whiteboard migration strategy mock?",
     "Order waves by dependency graph, risk, and business criticality — pilot stateless first, platform next, revenue path third, long tail last.",
     "**Wave selection matrix:**\n| Wave | Criteria | Example count |\n|------|----------|---------------|\n| Pilot | Stateless, low revenue risk | 5–10 |\n| Platform | Shared dependencies | 20–30 |\n| Core | Revenue path | 40–80 |\n| Long tail | Legacy deps, manual steps | Remainder |\n\n**Per wave:** Rollback window (DNS warm 30 days), success metrics, runbook updates.\n\n**Parallel track:** Data migration often separate program — call out explicitly.\n\n**Anti-pattern:** Big-bang weekend cutover for 200 services.",
     "Wave criteria prove sequencing discipline — assess before Azure boxes.",
     "Replatform vs refactor? — Containerize first; refactor incrementally in cloud.",
     "Landing zone before pilot? — Identity and network policy before prod workload.",
     "Lift-and-shift everything wave 1",
     "No dependency-ordered batches",
     "Ignore team training and runbooks"),
    ("Risk Scoring Model", "Whiteboard Mock", "Very Common",
     "How score risks in an architecture risk register whiteboard mock?",
     "Likelihood × impact heat map, categories (technical, security, ops, compliance, vendor), owner per risk, mitigation with residual risk and review cadence.",
     "**Scoring:** L/M/H × L/M/H → heat map; top-right escalates to steering.\n\n**Categories:** Technical, security, operational, compliance, vendor.\n\n**Table columns:** Risk | L | I | Score | Mitigation | Owner | Residual | Review date\n\n**Process:** Biweekly arch guild; red items with options not alerts only.\n\n**Link:** High risks map to ADR, spike, or accepted residual with exec sign-off.\n\n**Distinction:** Risk (may happen) vs issue (occurred) — separate logs.",
     "Risk register mock tests governance — 'monitor' is not mitigation.",
     "Heat map for exec? — 5×5 grid translation for non-technical audience.",
     "Residual risk acceptance? — Document with exec sign-off and expiry.",
     "Generic risks without domain specificity",
     "No owners or review cadence",
     "Mitigation column says monitor only"),
    ("Executive BLUF Structure", "Whiteboard Mock", "Very Common",
     "What BLUF structure should architects use in executive communication mocks?",
     "Bottom line up front: business outcome, scope in plain language, phased how, three milestones, cost/benefit, explicit ask — no jargon in first minute.",
     "**5-minute BLUF:**\n1. Why now — pain in dollars or risk\n2. What — scope plain language\n3. How — phased; customer impact minimal\n4. When — 3 milestones with dates\n5. Cost/benefit — invest vs save; break-even\n6. Ask — budget, headcount, or decision\n\n**Rules:** No acronyms without expansion; one diagram max; rehearse hard time limit.\n\n**Anticipate:** 'Why not buy SaaS?' 'Why now vs next year?'",
     "Executive comms intro is BLUF discipline — headline before architecture vocabulary.",
     "Yellow status? — Early yellow preferred over surprise red.",
     "CEO vs board depth? — CEO outcomes; board risk, audit, materiality.",
     "Opening with Kubernetes and microservices",
     "No dollar figures or timeline",
     "Ending without explicit ask"),
    ("Power Interest Grid", "Whiteboard Mock", "Very Common",
     "How use a power/interest stakeholder map in architecture whiteboard mocks?",
     "Plot stakeholders on power vs interest; strategies: manage closely, keep satisfied, consult, monitor. Add engagement cadence and RACI for key decisions.",
     "**Quadrants:**\n- High power, high interest → manage closely (CTO, sponsor)\n- High power, low interest → keep satisfied (CFO — cost dashboard)\n- Low power, high interest → consult (team leads)\n- Low power, low interest → monitor\n\n**Add:** Engagement cadence table, RACI on schema/budget/vendor decisions.\n\n**Political risk:** Competing VP fiefdoms — exec sponsor resolves escalations.\n\n**Update live:** Missing stakeholder discovered late — revise map in mock.",
     "Stakeholder maps show architecture ships through people.",
     "Sponsor vs champion? — Sponsor has budget; champion drives adoption.",
     "Blocker strategy? — Co-opt as migration leads — not ignore.",
     "All stakeholders same cadence",
     "Map without engagement plan",
     "No plan for identified blockers"),
    ("Build vs Buy Scorecard", "Whiteboard Mock", "Very Common",
     "What belongs on a build vs buy scorecard in a whiteboard mock?",
     "Requirements, 3-year TCO, time-to-market, customization need, team skills, ops burden, exit strategy. Score matrix with rejected alternative documented in ADR.",
     "**Criteria weights example (APIM):**\n| Criterion | Weight |\n|-----------|--------|\n| TTM | 25% |\n| TCO 3yr | 25% |\n| Customization | 20% |\n| Ops burden | 15% |\n| Team skills | 15% |\n\n**Options:** Buy (APIM/Kong), build (YARP+custom), hybrid.\n\n**Document:** Rejected option with honest trade-off — not ideology.\n\n**Exit:** OpenAPI, portable policies — conscious lock-in ADR.",
     "Build vs buy mocks need numbers and rejected alternatives.",
     "When build wins? — Unique protocol, regulatory constraint, strategic differentiator.",
     "Hybrid boundary? — APIM front + custom auth plugin — document line.",
     "Build because we are special",
     "SaaS TCO missing headcount",
     "No exit strategy for vendor lock-in"),
    ("Tech Debt ICE Score", "Whiteboard Mock", "Very Common",
     "How prioritize technical debt in an executive presentation mock?",
     "Categorize (reliability, security, velocity, cost); ICE or risk×effort; tie to incidents and dollars; ask for bounded capacity (e.g., 20%) with 90-day measurable outcomes.",
     "**Categories:**\n1. Reliability — deploy time, outage correlation\n2. Security — CVE count, unsupported runtime\n3. Velocity — lead time drag from coupling\n4. Cost — overprovisioned infra\n\n**Prioritization:** ICE or risk matrix; quick wins + strategic items.\n\n**Ask:** 20% sprint capacity + platform engineers for Q3.\n\n**Metrics:** Deploy frequency, MTTR, CVE count — baseline and 90-day target.",
     "Tech debt presentations must speak executive — incidents and dollars.",
     "Interest vs principal? — Interest = ongoing cost; principal = paydown effort.",
     "Stop-the-line debt? — Critical CVEs may preempt features.",
     "Complaint list without prioritization",
     "No metrics to prove improvement",
     "Asking 100% capacity for debt"),
    ("Now Next Later Roadmap", "Whiteboard Mock", "Very Common",
     "How structure a 3-year architecture roadmap for whiteboard mocks?",
     "Horizon 1 stabilize (0–12mo), H2 scale (12–24mo), H3 innovate (24–36mo). Link capabilities to business OKRs; show dependencies between initiatives.",
     "**Year 1 — Foundation:** Observability, CI/CD golden path, identity standardization.\n\n**Year 2 — Scale:** Multi-region, event hub, self-service portal.\n\n**Year 3 — Optimize:** FinOps automation, cell-based blast radius.\n\n**Mapping:** Each initiative → OKR (time-to-market, uptime 99.95%).\n\n**Dependencies:** Identity before zero-trust; observability before SLO scaling.\n\n**Communication:** Now/Next/Later board for stakeholders.",
     "Roadmap mocks test strategic sequencing — not technology laundry lists.",
     "Theme vs project? — Themes for flexibility; committed projects for near term.",
     "Re-baseline when? — Quarterly on acquisition or market shift.",
     "Everything in year 1",
     "No dependency arrows",
     "No business outcome linkage"),
    ("Vendor POC Scope", "Whiteboard Mock", "Very Common",
     "How scope a vendor evaluation POC in an observability platform mock?",
     "20 representative services, 2 weeks, weighted criteria scorecard, security review, TCO at scale, reference calls — success metrics defined before POC starts.",
     "**Criteria (example weights):** Cloud integration 20%, K8s APM 20%, cost at scale 20%, SIEM export 15%, UX 10%, support 15%.\n\n**POC success:** 99% trace coverage, <5min alert latency, ingest cost model validated.\n\n**Security:** Data residency, SSO, pen test results.\n\n**Portable telemetry:** OpenTelemetry instrumentation regardless of vendor choice.",
     "Vendor eval mocks prove structured procurement — not brand preference.",
     "Build vs buy observability? — Rarely build at 500+ services.",
     "Negotiation leverage? — Competitive quote even if staying incumbent.",
     "POC on toy app only",
     "Ignore ingest cost at scale",
     "Single quote without comparison"),
    ("Internal SLA Error Budget", "Whiteboard Mock", "Very Common",
     "How negotiate internal platform SLA with error budget in a mock?",
     "Platform commits SLO (uptime, ack time); product squads commit standards (golden path, limits, runbooks). Error budget policy when burned — freeze changes, focus reliability.",
     "**Platform SLOs:** Control plane 99.9%, node pool 99.95%, P1 ack 15 min.\n\n**Squad obligations:** Golden path templates, pod limits, incident cooperation.\n\n**Error budget:** ~43 min/month at 99.9% — if burned, reliability sprint.\n\n**Exclusions:** Customer DNS, misconfigured manifests — documented.\n\n**Review:** Quarterly with metrics dashboard.",
     "SLA negotiation tests bilateral accountability — not one-sided guarantees.",
     "Internal vs customer SLA? — Internal enables customer SLA — cascade requirements.",
     "Penalty without error budget? — Blame culture — pair SLO with budget policy.",
     "Vague best-effort commitment",
     "No squad responsibilities",
     "SLA without measurement method"),
    ("Team Topologies Modes", "Whiteboard Mock", "Very Common",
     "What Team Topologies interaction modes apply in a platform org mock?",
     "Platform as X-as-a-Service, enabling team facilitation, complicated-subsystem collaboration, stream-aligned ownership. Avoid platform ticket-queue bottleneck.",
     "**Modes:**\n- **X-as-a-Service** — Platform provides self-service APIs/portal\n- **Facilitation** — Enabling team rotates to upskill streams\n- **Collaboration** — Complex subsystem (payments, identity) pairs with streams\n\n**Structure example:** Platform 8, Enabling 3, Complicated subsystem 4, Streams 15×6.\n\n**Anti-pattern:** 2-week platform ticket queue — embed enablers instead.",
     "Team topology mock connects org design to deliverability.",
     "Platform as product? — Internal devs are customers — NPS, roadmap.",
     "Conway alignment? — Service boundaries match team ownership where possible.",
     "Central ticket queue bottleneck",
     "Stream teams own cluster upgrades",
     "Topology without interaction modes"),
    ("Inverse Conway Maneuver", "Whiteboard Mock", "Common",
     "What is the inverse Conway maneuver and when recommend it?",
     "Deliberately reshape team structure to match desired architecture boundaries — reorg to stream-aligned teams before or alongside service extraction.",
     "**Problem:** 12 services, 4 layer-based teams → every feature crosses 3 teams.\n\n**Inverse Conway:** Reorganize to Checkout, Catalog, Fulfillment streams owning vertical slices.\n\n**If reorg impossible:** Service owner DRI per service, weekly cross-team sync, API contracts.\n\n**Quantify:** Collaboration tax via lead time data in ADR.\n\n**Change management:** Executive sponsor, phased reorg, communication plan.",
     "Conway mock tests org-technical feedback loop awareness.",
     "Melvin Conway 1968? — Organizations design systems mirroring communication structure.",
     "Service owner without team change? — Interim pattern with explicit collaboration tax.",
     "12 services 4 teams no interaction plan",
     "Reorg proposal without change management",
     "Ignore communication overhead in estimates"),
    ("Platform ROI Model", "Whiteboard Mock", "Very Common",
     "How model ROI for an internal developer platform pitch mock?",
     "Pain (DORA, survey NPS), vision (golden path), team size, engineer-hours saved × loaded rate, adoption milestones, risk of low adoption with enabling team mitigation.",
     "**ROI example:**\n- 200 engineers × 2 hr/week saved × $75/hr × 50 weeks = $1.5M/yr\n- Team: 6 platform engineers + 1 PM\n- Milestones: Q1 portal MVP, Q2 50% adoption\n\n**Metrics:** Deployment frequency, lead time, platform adoption %.\n\n**Risk:** Adoption — embed enabling team in pilot squads.\n\n**Thin start:** One golden path language first.",
     "Platform pitch is internal sales — quantify developer time.",
     "Platform PM needed? — Yes at 200+ engineers.",
     "Thinnest viable platform? — One path done well beats five half-built.",
     "Build everything before pilot",
     "ROI without baseline DORA",
     "Platform disconnected from stream pain"),
    ("NPV Sensitivity Analysis", "Whiteboard Mock", "Very Common",
     "How present cost-benefit with sensitivity in a cloud migration mock?",
     "3-year TCO, CAPEX→OPEX shift, stated assumptions, ±30% sensitivity on run rate, phased proceed (dev/test first), include egress and staffing.",
     "**Costs:** Migration project, cloud run rate, training, contract exit penalties.\n\n**Benefits:** HW maintenance saved, elastic dev clusters, revenue enablement (assumption stated).\n\n**NPV:** Positive if key assumptions ≥50% credible.\n\n**Sensitivity:** ±30% cloud run rate; document real options value of phased commit.\n\n**Honesty:** Cloud not always cheaper — show math.",
     "Cost-benefit mock requires explicit assumptions and sensitivity.",
     "Stranded on-prem cost? — Datacenter exit penalties in model.",
     "Real options? — Phase 1 buys learning — defer full commit.",
     "Cloud always cheaper claim",
     "Ignore egress and support staffing",
     "Benefits without credible attribution"),
])

from _banks_data_49_50_extra import (  # noqa: E402
    W49_ADVANCED,
    W49_EXPERT,
    W50_I_EXTRA,
    W50_ADVANCED,
    W50_EXPERT,
)

WEEK_49_INTERMEDIATE = WEEK_49_Q001_Q005 + WEEK_49_Q006_Q030[:20] + W49_I_EXTRA
WEEK_49_ADVANCED = WEEK_49_Q006_Q030[20:] + W49_ADVANCED
WEEK_49_EXPERT = W49_EXPERT

WEEK_50_INTERMEDIATE = WEEK_50_Q001_Q005 + WEEK_50_Q006_Q030[:20] + W50_I_EXTRA
WEEK_50_ADVANCED = WEEK_50_Q006_Q030[20:] + W50_ADVANCED
WEEK_50_EXPERT = W50_EXPERT

ALL_WEEKS_49_50_BANKS = {
    49: {
        "INTERMEDIATE": WEEK_49_INTERMEDIATE,
        "ADVANCED": WEEK_49_ADVANCED,
        "EXPERT": WEEK_49_EXPERT,
    },
    50: {
        "INTERMEDIATE": WEEK_50_INTERMEDIATE,
        "ADVANCED": WEEK_50_ADVANCED,
        "EXPERT": WEEK_50_EXPERT,
    },
}

assert len(WEEK_49_INTERMEDIATE) == 40, len(WEEK_49_INTERMEDIATE)
assert len(WEEK_49_ADVANCED) == 30, len(WEEK_49_ADVANCED)
assert len(WEEK_49_EXPERT) == 20, len(WEEK_49_EXPERT)
assert len(WEEK_50_INTERMEDIATE) == 40, len(WEEK_50_INTERMEDIATE)
assert len(WEEK_50_ADVANCED) == 30, len(WEEK_50_ADVANCED)
assert len(WEEK_50_EXPERT) == 20, len(WEEK_50_EXPERT)

HEADER = '''"""Hand-crafted premium interview banks for Weeks 49–50 — Whiteboard Mock 2 and Leadership.

Week 49 Whiteboard Mock 2: multi-tenant SaaS, acquisition integration, migration strategy,
risk register, executive comms, stakeholder map, build vs buy, technical debt presentation,
architecture roadmap, vendor evaluation, SLA negotiation, team topology, Conway's law,
platform pitch, cost-benefit, compliance gap, DR presentation, scale 10x, data mesh,
board presentation.

Week 50 Leadership & Behavioral: stakeholder management, managing up, conflict resolution,
influencing without authority, executive communication, prioritization, saying no,
technical vision, consensus building, cross-functional leadership, mentoring, feedback,
difficult conversations, psychological safety, incident leadership, budget justification,
hiring, delegation, remote leadership, negotiation.
"""

from premium_qa_data import q

'''


def _render_list(name: str, items: list) -> str:
    lines = [f"{name} = ["]
    for item in items:
        lines.append("    q(")
        for key in ("title", "category", "frequency", "question", "short", "detailed", "perspective"):
            lines.append(f"      {item[key]!r},")
        fu = item["followups"]
        fu_lines = [ln.strip() for ln in fu.split("\n") if ln.strip()]
        fu1 = fu_lines[0].replace("1. **", "").replace("**", "") if fu_lines else ""
        fu2 = fu_lines[1].replace("2. **", "").replace("**", "") if len(fu_lines) > 1 else ""
        mistakes = [m.strip("- ") for m in item["mistakes"].split("\n") if m.strip()]
        for val in (fu1, fu2, *mistakes[:3]):
            lines.append(f"      {val!r},")
        lines.append("    ),")
    lines.append("]")
    return "\n".join(lines)


def main():
    body = "\n\n".join([
        _render_list("WEEK_49_INTERMEDIATE", WEEK_49_INTERMEDIATE),
        _render_list("WEEK_49_ADVANCED", WEEK_49_ADVANCED),
        _render_list("WEEK_49_EXPERT", WEEK_49_EXPERT),
        _render_list("WEEK_50_INTERMEDIATE", WEEK_50_INTERMEDIATE),
        _render_list("WEEK_50_ADVANCED", WEEK_50_ADVANCED),
        _render_list("WEEK_50_EXPERT", WEEK_50_EXPERT),
        "ALL_WEEKS_49_50_BANKS = {\n    49: {\n        \"INTERMEDIATE\": WEEK_49_INTERMEDIATE,\n        \"ADVANCED\": WEEK_49_ADVANCED,\n        \"EXPERT\": WEEK_49_EXPERT,\n    },\n    50: {\n        \"INTERMEDIATE\": WEEK_50_INTERMEDIATE,\n        \"ADVANCED\": WEEK_50_ADVANCED,\n        \"EXPERT\": WEEK_50_EXPERT,\n    },\n}",
    ])
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(HEADER + body + "\n")
    total = sum(len(v[t]) for v in ALL_WEEKS_49_50_BANKS.values() for t in v)
    print(f"Wrote {OUT}")
    print(f"Week 49: I={len(WEEK_49_INTERMEDIATE)} A={len(WEEK_49_ADVANCED)} E={len(WEEK_49_EXPERT)}")
    print(f"Week 50: I={len(WEEK_50_INTERMEDIATE)} A={len(WEEK_50_ADVANCED)} E={len(WEEK_50_EXPERT)}")
    print(f"Total: {total}")


if __name__ == "__main__":
    main()
