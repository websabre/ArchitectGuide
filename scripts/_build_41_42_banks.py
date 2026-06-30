#!/usr/bin/env python3
"""Build premium_qa_data_weeks_41_42_banks.py from existing Q006-Q030 + extra banks."""

from __future__ import annotations

import os

from premium_qa_data_weeks_41_44_q006_q030 import WEEK_41_Q006_Q030, WEEK_42_Q006_Q030
from _banks_data_41_42_extra import W41_ADV, W41_EXP, W42_EXTRA_I, W42_ADV, W42_EXP

OUT = os.path.join(os.path.dirname(__file__), "premium_qa_data_weeks_41_42_banks.py")

W41_EXTRA_I = [
    ("Michael Nygard ADR Format", "ADRs", "Very Common",
     "What is the Michael Nygard ADR format and why is it widely adopted?",
     "Title, status, context, decision, consequences — minimal sections that force explicit trade-off thinking and stay readable in Git diffs.",
     "**Nygard template** is the de facto open-source ADR standard.\n\n**Sections:** Context (forces), Decision (chosen path), Consequences (good/bad).\n\n**Enterprise extensions:** Add deciders, options considered, compliance — but keep core short.\n\n**Architect:** Publish org template derived from Nygard in `docs/adr/README.md` with examples.",
     "Interviewers expect you to name Nygard and explain why brevity beats encyclopedic design docs for decisions.",
     "ADR tools supporting Nygard? — adr-tools CLI, Log4brains, Backstage ADR plugin.",
     "Markdown vs YAML front matter? — YAML metadata aids search; body stays Markdown.",
     "ADR without consequences section",
     "Copy-paste template without filling options",
     "Storing ADRs only in Confluence"),
    ("Structurizr for C4", "C4 Model", "Common",
     "When recommend Structurizr over hand-drawn C4 diagrams?",
     "Structurizr DSL gives consistent C4 notation, relationship validation, and diagram views generated from one model — ideal for enterprises with many systems.",
     "**Structurizr workflow:**\n1. Define software system, people, containers in DSL\n2. Generate context, container, component views automatically\n3. Export to PlantUML/Mermaid for docs site\n\n**When yes:** 20+ services, architecture guild enforces notation.\n**When no:** Single POC — Mermaid in README faster.\n\n**Architect:** Structurizr workspace in Git — PR review on model changes.",
     "Tool choice signals whether you scale architecture documentation beyond whiteboards.",
     "Structurizr Lite vs cloud? — Lite self-hosted; cloud for collaboration features.",
     "IcePanel vs Structurizr? — IcePanel more UX; Structurizr purer C4 DSL.",
     "Every architect must learn Structurizr day one",
     "DSL model diverges from deployed reality",
     "Generated diagrams never updated after first sprint"),
    ("PlantUML Architecture Diagrams", "Documentation", "Common",
     "Use PlantUML for architecture diagrams in a docs-as-code pipeline.",
     "PlantUML text diagrams diff in Git, render in CI to SVG/PNG, embed in MkDocs — same review flow as code.",
     "**Pipeline:**\n```bash\nplantuml -tsvg docs/architecture/*.puml\n```\n\n**Strengths:** Sequence, component, deployment diagrams; IDE plugins.\n\n**C4 integration:** Structurizr exports PlantUML; or C4-PlantUML macros.\n\n**Architect:** Standardize on one diagram-as-code tool per org — avoid Visio attachments.",
     "Diagram-as-code is table stakes for senior architect interviews in 2026.",
     "Mermaid vs PlantUML? — Mermaid lighter for README; PlantUML richer for complex UML.",
     "Render in PR preview? — CI bot posts diagram diff image on PR.",
     "Binary Visio as source of truth",
     "PlantUML files not rendered in docs site",
     "No naming legend on diagrams"),
    ("ADR Numbering Convention", "ADRs", "Common",
     "Define ADR numbering and file naming conventions for a monorepo.",
     "Sequential `NNNN-short-title.md` — never reuse numbers; supersede links old number; pad to 4 digits for sort order.",
     "**Convention:**\n- `docs/adr/0042-event-sourcing-orders.md`\n- Index table in `docs/adr/README.md`\n- CI lint: new ADR must increment max number\n\n**Monorepo:** Central `architecture/adr/` repo or per-service `adr/` with federated index.\n\n**Architect:** Number is permanent identifier — title slug can change in front matter only before merge.",
     "Numbering discipline prevents 'which ADR is current?' confusion during audits.",
     "Per-service vs central numbering? — Central sequential; service prefix if federated (`ORDER-0042`).",
     "Auto-generate number in PR template? — Script suggests next ID.",
     "Reuse ADR number after supersede",
     "Random UUID filenames — not human searchable",
     "No index README in adr folder"),
    ("Architecture Review Pre-Read Pack", "Reviews", "Very Common",
     "What belongs in an architecture review pre-read pack sent 48 hours before the meeting?",
     "RFC/ADR, C4 context+container, NFR matrix, threat model summary, cost estimate, open questions, explicit decision ask.",
     "**Pack contents:**\n1. Problem statement (1 paragraph)\n2. Recommended option + alternatives table\n3. Diagrams (linked, not 40-page embed)\n4. NFR targets with verification plan\n5. Risk register top 5\n6. Migration/rollback outline\n\n**Architect:** Pre-read mandatory — meeting cancelled if not distributed 48h ahead for Tier-0.",
     "Pre-read quality predicts review meeting productivity.",
     "Who prepares pack? — Author owns; architect reviews completeness before scheduling.",
     "Redact secrets in pre-read? — Use sample data; link to secure vault for creds.",
     "Slide deck only — no written decision ask",
     "Diagrams attached as unreadable screenshots",
     "Open questions buried on slide 38"),
    ("Data-Flow Diagram for Threat Modeling", "Security", "Very Common",
     "Draw a data-flow diagram (DFD) for STRIDE threat modeling — what elements are required?",
     "Processes, data stores, external entities, data flows, trust boundaries — DFD is prerequisite before STRIDE enumeration.",
     "**DFD elements:**\n- **External entity** — User, partner API\n- **Process** — Order API, payment worker\n- **Data store** — Order DB, cache\n- **Flow** — labeled with data classification\n- **Trust boundary** — dashed line (Internet/DMZ/internal)\n\n**Architect:** DFD Level 1 for threat model; don't confuse with C4 container (related but different purpose).",
     "DFD + STRIDE is the standard security review combo for external-facing designs.",
     "DFD vs C4? — C4 for structure; DFD for security data movement.",
     "Microsoft Threat Modeling Tool? — Auto STRIDE from DFD elements.",
     "STRIDE without DFD — threats guessed not systematic",
     "Missing trust boundaries on diagram",
     "Unlabeled data flows ('data')"),
    ("Architecture Review Tiering", "Reviews", "Very Common",
     "Define architecture review tiers (Tier-0/1/2) and what depth each requires.",
     "Tier-0: full checklist, STRIDE, DR, FinOps, board sign-off. Tier-1: standard checklist + ADR. Tier-2: lightweight self-certification with spot audits.",
     "**Example matrix:**\n| Tier | Examples | Review depth |\n|------|----------|-------------|\n| 0 | Payment, PHI | Full board + security |\n| 1 | Customer-facing non-PII | Domain architect |\n| 2 | Internal tools | Team checklist |\n\n**Architect:** Tier assigned by data classification + revenue impact — not team preference.",
     "Tiering prevents governance bottleneck while protecting critical paths.",
     "Who assigns tier? — Architecture guild + data classification auto-tag.",
     "Tier escalation? — POC becomes Tier-0 when scope adds PII.",
     "Everything Tier-0 — board exhaustion",
     "Payment path labeled Tier-2 to skip review",
     "Tiers undocumented — subjective every time"),
    ("Decision Record vs Meeting Minutes", "ADRs", "Common",
     "Why are ADRs not substitutes for meeting minutes?",
     "ADRs record decisions and rationale — immutable. Minutes capture discussion, attendees, actions — ephemeral. Link minutes to ADR PR but don't bury decision in minutes only.",
     "**Distinction:**\n- **Minutes:** Who said what, action items, next meeting\n- **ADR:** What we decided, why, consequences\n\n**Practice:** Review meeting minutes reference ADR PR number; decision merges as Accepted ADR.\n\n**Architect:** Slack/Teams threads are not ADRs — export decision to Git.",
     "Confusing minutes and ADRs loses audit trail for regulators.",
     "Notion meeting notes as ADR? — Must promote decision to Git ADR.",
     "Recording videos? — Supplement, not replace written ADR.",
     "Decision only in meeting minutes",
     "ADR listing attendees instead of deciders",
     "No link between RFC comment thread and ADR"),
    ("Architecture Review Outcomes", "Reviews", "Common",
     "What are valid outcomes of an architecture review?",
     "Accepted, Accepted with conditions, Revise and resubmit, Deferred (needs spike), Rejected — each with documented actions and owners.",
     "**Outcome definitions:**\n- **Accepted** — Proceed; conditions tracked as tickets\n- **Revise** — Specific gaps (NFR, threat model) before re-review\n- **Deferred** — Spike/time-boxed prototype required\n- **Rejected** — Alternative approach mandated with rationale\n\n**Architect:** 'Accepted verbally' without written record is not an outcome.",
     "Clear outcomes prevent ambiguous 'we sort of approved it'.",
     "Conditions expiry? — Must complete before prod gate — tracked in Jira.",
     "Re-review SLA? — 5 days after revision submitted.",
     "Vague 'looks good' email",
     "Rejected design deployed anyway",
     "Conditions never tracked to completion"),
    ("Mermaid C4 in README", "Documentation", "Very Common",
     "Embed C4 container diagrams in Markdown using Mermaid — benefits and limits.",
     "Mermaid in GitHub/GitLab/MkDocs renders C4-ish diagrams from text — great for PR review and quick updates; limited vs Structurizr for large models.",
     "**Example:**\n```mermaid\nC4Container\ntitle Order System\nPerson(customer)\nContainer(api, Order API, .NET)\n```\n\n**Benefits:** Zero tooling install for readers; diffs visible.\n\n**Limits:** Large diagrams clutter; not all C4 macros in older renderers.\n\n**Architect:** Mermaid for service README; Structurizr for enterprise landscape.",
     "Mermaid lowers barrier to diagrams-as-code for every team.",
     "C4 extension support? — Verify renderer version in docs CI.",
     "Auto-render in Backstage? — TechDocs plugin renders Mermaid.",
     "Mermaid so complex it exceeds renderer limits",
     "Diagram in image only — not source",
     "C4 levels mixed on one unreadable diagram"),
    ("Architecture Risk Heat Map", "Risk Management", "Common",
     "Present architecture risks on a 5×5 heat map to executives.",
     "Likelihood × impact matrix with color zones — scores ≥15 get mitigation plan and executive visibility; link each risk to ADR or STRIDE item.",
     "**Heat map zones:**\n- Green 1–6: monitor\n- Yellow 7–14: mitigate this quarter\n- Red 15–25: escalate / block release\n\n**Executive view:** Top 10 red risks with owner, ETA, residual risk after mitigation.\n\n**Architect:** Heat map in monthly architecture governance deck — not spreadsheet only.",
     "Executives understand heat maps faster than technical threat lists.",
     "Qualitative vs quantitative scoring? — Start qualitative; refine with incident data.",
     "Risk appetite statement? — Board defines acceptable red count.",
     "All risks scored medium — useless",
     "Heat map never updated after launch",
     "Risks without named owners"),
    ("Architecture Standards Document", "Documentation", "Very Common",
     "What belongs in an enterprise architecture standards document vs principles?",
     "Standards are mandatory rules (TLS 1.2+, approved regions, tagging schema). Principles are directional values (API-first). Standards enforced in CI; principles guide ADR trade-offs.",
     "**Standards examples:**\n- All external APIs behind API gateway\n- No plaintext secrets in repos\n- Mandatory cost allocation tags\n- Approved auth pattern (OIDC + PKCE)\n\n**Enforcement:** Azure Policy, OPA, fitness functions, review checklist.\n\n**Architect:** Standards versioned in Git — change via RFC + ADR.",
     "Standards vs principles confusion causes either chaos or paralysis.",
     "Exception process? — Time-boxed waiver with compensating controls.",
     "Standards review cadence? — Quarterly — remove obsolete entries.",
     "Standards doc 200 pages unread",
     "Standards with no enforcement mechanism",
     "Principles duplicated as mandatory standards"),
    ("Sign-off Workflow in Git", "Governance", "Very Common",
     "Implement architecture sign-off using Git PR approvals.",
     "ADR/RFC PR requires CODEOWNERS approvals from architect, security, FinOps delegates — merge = auditable sign-off; branch protection enforces.",
     "**Setup:**\n```\n# CODEOWNERS\ndocs/adr/ @enterprise-architects @security-architecture\n```\n\n**Branch protection:** 2 approvals including security for Tier-0 paths.\n\n**Evidence:** GitHub/GitLab audit log + ADR deciders field matches approvers.\n\n**Architect:** Sign-off in email is supplement — Git is source of truth.",
     "Git-based sign-off satisfies SOC2 change management evidence.",
     "Emergency break-glass? — Retroactive ADR PR within 48h with incident link.",
     "Delegated approvers? — Document in ADR metadata when primary OOO.",
     "Verbal approval without PR",
     "CODEOWNERS file empty",
     "Same person authors and sole approves Tier-0 ADR"),
    ("NFR Traceability Matrix", "NFRs", "Common",
     "Link NFRs to test cases and monitoring in a traceability matrix.",
     "Matrix columns: NFR ID, requirement, ADR, test (k6/QA), dashboard/alert, owner — proves each NFR is built, tested, and observed.",
     "**Example row:**\nNFR-07 | p99 <300ms | ADR-0042 | k6 threshold PR gate | App Insights workbook | Team Checkout\n\n**Audit value:** Regulators ask 'how prove availability claim?' — matrix answers.\n\n**Architect:** NFR matrix required in Tier-0 review pack appendix.",
     "Traceability is how NFRs survive from slide to production.",
     "Bi-directional links? — ADR cites NFR IDs; tests cite NFR IDs.",
     "Orphan NFRs? — Quarterly audit for NFRs with no test.",
     "NFRs in Word doc disconnected from CI",
     "Tests exist but not mapped to NFR IDs",
     "Monitoring without alert linked to NFR"),
    ("Architecture Review Facilitation Agenda", "Reviews", "Common",
     "Provide a 60-minute architecture review agenda template.",
     "0–5 context, 5–20 author presentation, 20–45 structured feedback rounds, 45–55 decision, 5–60 actions — timeboxed with parking lot.",
     "**Agenda template:**\n1. **Context** (5m) — Decision ask stated\n2. **Presentation** (15m) — Author only, no interruptions\n3. **Round-robin** (25m) — Security, data, ops, FinOps\n4. **Decision** (10m) — Accepted/Revise/Defer\n5. **Actions** (5m) — Owners + dates\n\n**Architect facilitator:** Cut tool debates — park for offline spike.",
     "Agenda discipline respects senior reviewer time.",
     "Recording allowed? — Yes for absent stakeholders; not substitute for ADR.",
     "Parking lot tracking? — Jira tickets from parking lot same day.",
     "Unstructured 90-minute debate",
     "No decision in meeting — another meeting scheduled",
     "Author not presenting — architect presents for them"),
]


def esc(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")


def fmt_dict(d: dict) -> str:
    fu = d["followups"]
    fu1 = fu.split("\n")[0].replace("1. **", "").rstrip("*")
    fu2 = fu.split("2. **")[1].rstrip("*") if "2. **" in fu else ""
    ms = [x.lstrip("- ") for x in d["mistakes"].split("\n") if x.strip()]
    while len(ms) < 3:
        ms.append("")
    return (
        f'    q("{esc(d["title"])}", "{esc(d["category"])}", "{esc(d["frequency"])}",\n'
        f'      "{esc(d["question"])}",\n'
        f'      "{esc(d["short"])}",\n'
        f'      "{esc(d["detailed"])}",\n'
        f'      "{esc(d["perspective"])}",\n'
        f'      "{esc(fu1)}",\n'
        f'      "{esc(fu2)}",\n'
        f'      "{esc(ms[0])}",\n'
        f'      "{esc(ms[1])}",\n'
        f'      "{esc(ms[2])}"),'
    )


def fmt_tuple(t: tuple) -> str:
    title, cat, freq, question, short, detailed, perspective, fu1, fu2, m1, m2, m3 = t
    return (
        f'    q("{esc(title)}", "{esc(cat)}", "{esc(freq)}",\n'
        f'      "{esc(question)}",\n'
        f'      "{esc(short)}",\n'
        f'      "{esc(detailed)}",\n'
        f'      "{esc(perspective)}",\n'
        f'      "{esc(fu1)}",\n'
        f'      "{esc(fu2)}",\n'
        f'      "{esc(m1)}",\n'
        f'      "{esc(m2)}",\n'
        f'      "{esc(m3)}"),'
    )


def write_bank(name: str, items, fh) -> None:
    fh.write(f"\n{name} = [\n")
    for item in items:
        fmt = fmt_dict if isinstance(item, dict) else fmt_tuple
        fh.write(fmt(item) + "\n")
    fh.write("]\n")


HEADER = '''"""Hand-crafted premium interview banks for Weeks 41–42 — ADRs/Architecture Reviews & FinOps/DR/Performance.

Week 41: ADR writing, C4 diagrams, architecture review facilitation, legacy assessment,
RFC workflow, governance, STRIDE threat modeling, fitness functions, tech radar,
documentation standards, stakeholder sign-off, decision logs, architecture principles,
review checklists, diagram tooling, NFR documentation, risk registers,
post-decision review, executive summaries.

Week 42: FinOps culture, cost allocation, reserved instances, DR tiers, RTO/RPO,
Azure Site Recovery, chaos engineering, k6 load testing, performance budgets,
latency SLOs, capacity planning, right-sizing, DR drills, performance regression CI,
unit economics, backup strategies, multi-region cost, autoscale traps, FinOps team.

Exports per week: INTERMEDIATE (40), ADVANCED (30), EXPERT (20) = 90 questions.
Total: 180 questions.
"""

from premium_qa_data import q
'''

FOOTER = '''
ALL_WEEKS_41_42_BANKS = {
    41: {
        "intermediate": WEEK_41_INTERMEDIATE,
        "advanced": WEEK_41_ADVANCED,
        "expert": WEEK_41_EXPERT,
    },
    42: {
        "intermediate": WEEK_42_INTERMEDIATE,
        "advanced": WEEK_42_ADVANCED,
        "expert": WEEK_42_EXPERT,
    },
}
'''


def main() -> None:
    w41_intermediate = list(WEEK_41_Q006_Q030) + list(W41_EXTRA_I)
    w42_intermediate = list(WEEK_42_Q006_Q030) + list(W42_EXTRA_I)

    assert len(w41_intermediate) == 40, len(w41_intermediate)
    assert len(W41_ADV) == 30
    assert len(W41_EXP) == 20
    assert len(w42_intermediate) == 40, len(w42_intermediate)
    assert len(W42_ADV) == 30
    assert len(W42_EXP) == 20

    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(HEADER)
        write_bank("WEEK_41_INTERMEDIATE", w41_intermediate, fh)
        write_bank("WEEK_41_ADVANCED", W41_ADV, fh)
        write_bank("WEEK_41_EXPERT", W41_EXP, fh)
        write_bank("WEEK_42_INTERMEDIATE", w42_intermediate, fh)
        write_bank("WEEK_42_ADVANCED", W42_ADV, fh)
        write_bank("WEEK_42_EXPERT", W42_EXP, fh)
        fh.write(FOOTER)

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
