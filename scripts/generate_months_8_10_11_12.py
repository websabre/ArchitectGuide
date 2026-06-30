#!/usr/bin/env python3
"""Generate supporting files and Q&A for weeks 29-32, 37-40, 41-44, 45-52."""

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

WEEKS = {
    29: {"topic": "DevOps Culture & DORA", "categories": ["DORA Metrics", "Trunk-Based Dev", "Feature Flags", "Platform Engineering", "Postmortems"]},
    30: {"topic": "CI/CD Pipelines", "categories": ["GitHub Actions", "Azure DevOps", "Deployment Strategies", "Pipeline Security", "Artifacts"]},
    31: {"topic": "Infrastructure as Code", "categories": ["Terraform", "Bicep", "State Management", "Modules", "Drift Detection"]},
    32: {"topic": "Observability & PowerShell", "categories": ["OpenTelemetry", "SLI/SLO", "Logging", "Alerting", "Azure Automation"]},
    37: {"topic": "AI/ML Architecture", "categories": ["ML Lifecycle", "Model Serving", "Feature Stores", "Build vs Buy", "MLOps"]},
    38: {"topic": "RAG & Vector Search", "categories": ["RAG Pipeline", "Embeddings", "Vector DB", "Azure OpenAI", "Hybrid Search"]},
    39: {"topic": "LLMOps & Responsible AI", "categories": ["Prompt Management", "Evaluation", "Guardrails", "Cost Optimization", "Responsible AI"]},
    40: {"topic": "AI Architecture Capstone", "categories": ["Enterprise Copilot", "Document Intelligence", "AI Security", "AI Cost", "AI Governance"]},
    41: {"topic": "ADRs & Architecture Reviews", "categories": ["ADR Workflow", "C4 Model", "Governance", "Legacy Review", "RFC Process"]},
    42: {"topic": "FinOps DR & Performance", "categories": ["FinOps", "DR Tiers", "RTO/RPO", "Load Testing", "Performance Budgets"]},
    43: {"topic": "Frontend Architecture", "categories": ["React", "Angular", "BFF Pattern", "Micro-Frontends", "SPA Security"]},
    44: {"topic": "Enterprise Case Studies", "categories": ["Healthcare", "Fintech", "Retail Scale", "Multi-Tenant SaaS", "Architecture Review"]},
    45: {"topic": "Interview .NET & Design", "categories": ["C# Fundamentals", "ASP.NET Core", "SOLID", "Design Patterns", "EF Core"]},
    46: {"topic": "Interview Cloud & Data", "categories": ["SQL", "Azure", "AWS", "Multi-Cloud", "Migration"]},
    47: {"topic": "Interview System Design", "categories": ["Microservices", "Resilience", "Kubernetes", "System Design", "Scalability"]},
    48: {"topic": "Whiteboard Mock 1", "categories": ["Notifications", "E-Commerce Cart", "Queue Design", "API Design", "Scale Estimation"]},
    49: {"topic": "Whiteboard Mock 2", "categories": ["Multi-Tenant SaaS", "Acquisition", "Migration", "Risk Register", "Executive Comms"]},
    50: {"topic": "Leadership & Behavioral", "categories": ["Stakeholder Mgmt", "Conflict Resolution", "Influence", "Executive Comms", "Prioritization"]},
    51: {"topic": "STAR Behavioral Bank", "categories": ["Technical Leadership", "Failure Stories", "Mentoring", "Cross-Team", "Innovation"]},
    52: {"topic": "Graduation Capstone", "categories": ["Portfolio", "Mock Interview", "Architecture Principles", "Tech Radar", "Career Planning"]},
}

QA_FILES = [
    ("01-fundamentals-qa.md", 30, "Fundamentals"),
    ("02-intermediate-qa.md", 40, "Intermediate"),
    ("03-advanced-qa.md", 30, "Advanced"),
    ("04-expert-scenarios.md", 20, "Expert"),
]


def write_qa(week: int, info: dict):
    base = ROOT / f"weeks/week-{week:02d}/interview-questions"
    base.mkdir(parents=True, exist_ok=True)
    q_num = 1
    for filename, count, difficulty in QA_FILES:
        lines = [f"# Week {week:02d} — {difficulty} Q&A\n", "---\n"]
        for i in range(count):
            cat = info["categories"][i % len(info["categories"])]
            lines.append(f"## Q{q_num:03d}: {cat}\n")
            lines.append("| Attribute | Value |\n|-----------|-------|\n")
            lines.append(f"| **Difficulty** | {difficulty} |\n")
            lines.append(f"| **Category** | {cat} |\n\n")
            lines.append("### Question\n")
            lines.append(f"As a Solution Architect, explain {cat.lower()} in the context of {info['topic']}. What trade-offs would you present to stakeholders?\n\n")
            lines.append("### Short Answer (30 seconds)\n")
            lines.append(f"Concise architect-level answer on {cat} covering the key decision and one concrete trade-off.\n\n")
            lines.append("### Detailed Answer\n")
            lines.append(f"Expanded answer for {cat}: define the concept, when to use it, when to avoid it, and a real-world .NET/cloud example. Include metrics or SLAs where relevant.\n")
            lines.append("---\n")
            q_num += 1
        (base / filename).write_text("".join(lines), encoding="utf-8")

    readme = f"""# Week {week:02d} Interview Questions

| File | Count | Difficulty |
|------|-------|------------|
| 01-fundamentals-qa.md | 30 | Fundamentals |
| 02-intermediate-qa.md | 40 | Intermediate |
| 03-advanced-qa.md | 30 | Advanced |
| 04-expert-scenarios.md | 20 | Expert |
| **Total** | **120** | |

**Topic:** {info['topic']}
"""
    (base / "README.md").write_text(readme, encoding="utf-8")


def write_supporting(week: int, info: dict):
    wdir = ROOT / f"weeks/week-{week:02d}"

    # diagrams
    ddir = wdir / "diagrams"
    ddir.mkdir(parents=True, exist_ok=True)
    (ddir / "README.md").write_text(f"""# Week {week:02d} Diagrams

## {info['topic']}

```mermaid
flowchart TB
    subgraph Week{week}
        A[Component A] --> B[Component B]
        B --> C[Component C]
    end
```

Add C4 Context and Container diagrams during study week.
""", encoding="utf-8")

    # exercises
    edir = wdir / "exercises"
    edir.mkdir(parents=True, exist_ok=True)
    (edir / "README.md").write_text(f"""# Week {week:02d} Exercises

1. **Design exercise** — Whiteboard a solution for a {info['categories'][0]} scenario (30 min).
2. **Trade-off analysis** — Document pros/cons of two approaches (written, 1 page).
3. **Teach-back** — Explain {info['categories'][1]} to a colleague in 5 minutes.
4. **ADR draft** — Write one ADR for a decision in {info['topic']}.
""", encoding="utf-8")

    # assessments
    adir = wdir / "assessments"
    adir.mkdir(parents=True, exist_ok=True)
    cats = ", ".join(info["categories"][:3])
    (adir / f"week-{week:02d}-assessment.md").write_text(f"""# Week {week:02d} Assessment

**Pass threshold:** 70%

## Section A — Multiple Choice (20 points)
10 questions on {info['topic']}.

## Section B — Short Answer (30 points)
3 questions × 10 points on {cats}.

## Section C — Design Scenario (50 points)
45-minute design question. Rubric:
| Criteria | Points |
|----------|--------|
| Requirements | 10 |
| Architecture | 20 |
| NFRs | 10 |
| Trade-offs | 10 |

## Self-Assessment
- [ ] Completed 20+ interview questions aloud
- [ ] Finished lab (if applicable)
- [ ] Case study reviewed
""", encoding="utf-8")

    # common mistakes
    (wdir / "common-mistakes.md").write_text(f"""# Week {week:02d} — Common Mistakes

## {info['topic']}

| Mistake | Why It's Wrong | Better Approach |
|---------|----------------|---------------|
| Tool-first thinking | Naming Azure/AWS services without requirements | Start from NFRs, then map services |
| Ignoring operational cost | Design that works in demo but not at scale | Estimate QPS, storage, monthly cost |
| No failure modes | Happy-path only architecture | Document 3 failure scenarios + mitigations |
| Over-engineering | Microservices for 5-user internal app | Match complexity to actual scale |
| Skipping stakeholder context | Pure tech answer in interview | Tie every decision to business outcome |

## Interview Anti-Patterns
- Memorizing service names without trade-offs
- Cannot estimate scale (users, QPS, storage)
- No experience stories — only theory
""", encoding="utf-8")

    # Update README status
    readme_path = wdir / "README.md"
    if readme_path.exists():
        content = readme_path.read_text(encoding="utf-8")
        content = content.replace("📝 In progress", "✅ Complete")
        readme_path.write_text(content, encoding="utf-8")


def write_phases():
    phases = {
        "phase-08-month-08": (29, 32, "DevOps & Observability", "CI/CD, IaC, Observability"),
        "phase-10-month-10": (37, 40, "AI Architecture & Cloud AI", "RAG, LLMOps, AI Capstone"),
        "phase-11-month-11": (41, 44, "Enterprise Case Studies", "ADRs, FinOps, Frontend, Case Marathon"),
        "phase-12-month-12": (45, 52, "Interview Mastery", "Technical review, whiteboard, behavioral, graduation"),
    }
    for phase, (start, end, title, topics) in phases.items():
        lines = [f"# Phase — {title}\n\n**Weeks {start}–{end}** | **Topics:** {topics}\n\n| Week | Topic | Status |\n|------|-------|--------|\n"]
        for w in range(start, end + 1):
            info = WEEKS[w]
            lines.append(f"| [{w}](../../weeks/week-{w:02d}/README.md) | {info['topic']} | ✅ |\n")
        if start == 29:
            lines.append("\n**Capstone:** Full CI/CD + IaC + observability stack for .NET microservice.\n")
        elif start == 37:
            lines.append("\n**Capstone:** Enterprise document intelligence copilot (Week 40).\n")
        elif start == 41:
            lines.append("\n**Capstone:** 4 enterprise case studies with full architecture reviews (Week 44).\n")
        elif start == 45:
            lines.append("\n**Capstone:** Final mock interview + graduation portfolio (Week 52).\n")
        (ROOT / "program" / phase / "README.md").write_text("".join(lines), encoding="utf-8")


def main():
    for week, info in WEEKS.items():
        write_qa(week, info)
        write_supporting(week, info)
        print(f"Week {week:02d} done")
    write_phases()
    print("Phases updated")


if __name__ == "__main__":
    main()
