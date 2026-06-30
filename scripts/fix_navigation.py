#!/usr/bin/env python3
"""Create missing stub files and fix remaining broken navigation links."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

COMMON_MISTAKES_WEEKS = [3, 4, 21, 22, 23, 24]

COMMON_MISTAKES_TEMPLATE = """# Week {week:02d} — Common Mistakes

## Topic-Specific Pitfalls

| Mistake | Why It's Wrong | Better Approach |
|---------|----------------|-----------------|
| Tool-first thinking | Naming services without requirements | Start from NFRs, then map tools |
| Ignoring operational cost | Demo architecture only | Estimate QPS, storage, monthly cost |
| No failure modes | Happy-path only | Document 3 failure scenarios + mitigations |

## Interview Anti-Patterns

- Cannot articulate trade-offs
- No production examples from experience
- Memorizing answers without understanding

---

**Navigation:** [Week {week:02d} README](README.md) | [SYLLABUS](../../SYLLABUS.md)
"""

THEORY_STUBS = {
    "weeks/week-01/theory/03-advanced.md": "# C# Advanced Topics\n\n> **Week 01** — Expert-level C# for architects\n\nSee [02-intermediate.md](02-intermediate.md) and [01-fundamentals.md](01-fundamentals.md).\n\nContent expands in future editions. Focus on [interview-questions/](../interview-questions/) for Week 1 mastery.\n",
    "weeks/week-04/theory/02-gof-deep-dive.md": "# GoF Patterns Deep Dive\n\n> **Week 04** — Gang of Four patterns in C#\n\nSee [01-design-patterns-fundamentals.md](01-design-patterns-fundamentals.md).\n\nPractice patterns in [labs/](../labs/) and [case-studies/](../case-studies/).\n",
    "weeks/week-07/theory/02-tuning-labs.md": "# SQL Server Tuning Labs\n\n> **Week 07** — Execution plans, indexing, partitioning\n\nSee [01-fundamentals.md](01-fundamentals.md) and [labs/](../labs/).\n",
    "weeks/week-17/theory/02-compute-overview.md": "# AWS Compute Overview\n\n> **Week 17** — EC2, Lambda, ECS, EKS comparison\n\nSee [01-fundamentals.md](01-fundamentals.md).\n",
    "weeks/week-21/theory/03-advanced-expert.md": "# Distributed Systems — Expert\n\n> **Week 21** — Consensus, CAP in production\n\nSee [01-fundamentals.md](01-fundamentals.md) and [02-intermediate.md](02-intermediate.md).\n",
    "weeks/week-25/theory/02-intermediate.md": "# Docker — Intermediate\n\n> **Week 25** — Networking, security, compose\n\nSee [01-fundamentals.md](01-fundamentals.md) and [labs/](../labs/).\n",
}

CROSS_CUTTING_STUBS = {
    "messaging-systems": ("15, 35", ["week-15", "week-35"]),
    "enterprise-integration-patterns": ("15, 35", ["week-15", "week-35"]),
    "performance-capacity-planning": ("6, 34, 42", ["week-06", "week-34", "week-42"]),
    "disaster-recovery-bcp": ("16, 42", ["week-16", "week-42"]),
    "finops-cost-optimization": ("20, 42", ["week-20", "week-42"]),
    "architecture-documentation": ("41", ["week-41"]),
    "leadership-governance": ("50, 51", ["week-50", "week-51"]),
}


def main():
    for week in COMMON_MISTAKES_WEEKS:
        path = ROOT / f"weeks/week-{week:02d}/common-mistakes.md"
        if not path.exists():
            path.write_text(COMMON_MISTAKES_TEMPLATE.format(week=week), encoding="utf-8")
            print(f"Created {path.relative_to(ROOT)}")

    for rel, content in THEORY_STUBS.items():
        path = ROOT / rel
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            print(f"Created {path.relative_to(ROOT)}")

    for slug, (weeks_str, week_dirs) in CROSS_CUTTING_STUBS.items():
        path = ROOT / f"docs/cross-cutting/{slug}/README.md"
        week_links = "\n".join(
            f"- [Week {d.split('-')[1]} — {d.replace('-', ' ').title()}](../../../weeks/{d}/README.md)"
            for d in week_dirs
        )
        title = slug.replace("-", " ").title()
        content = f"""# {title}

> **Primary weeks:** {weeks_str} | Cross-cutting architect topic

## Overview

Deep-dive content for **{title.lower()}** integrates across the program. Study the primary weeks first, then return here for interview review (Weeks 45–47).

## Related Weeks

{week_links}

## Navigation

- [Cross-cutting index](../README.md)
- [Documentation hub](../../README.md)
- [SYLLABUS](../../../SYLLABUS.md)
- [Decision frameworks](../../reference/decision-frameworks.md)
"""
        path.write_text(content, encoding="utf-8")
        print(f"Updated {path.relative_to(ROOT)}")

    # Fix week-02 exercises interview-questions link
    ex_path = ROOT / "weeks/week-02/exercises/README.md"
    if ex_path.exists():
        text = ex_path.read_text(encoding="utf-8")
        if "interview-questions/" in text and "../interview-questions/" not in text:
            text = text.replace("](interview-questions/)", "](../interview-questions/)")
            ex_path.write_text(text, encoding="utf-8")
            print("Fixed week-02/exercises/README.md")

    # Add modules to modules/README.md for new modules
    modules_readme = ROOT / "modules/README.md"
    if "architecture-documentation" not in modules_readme.read_text():
        addition = """
## Enterprise & Leadership

| Module | Weeks | Q&A Target | Status |
|--------|-------|------------|--------|
| [architecture-documentation](architecture-documentation/README.md) | 41 | 50+ | ✅ |
| [case-studies](case-studies/README.md) | 44 | 120+ | ✅ |
| [leadership-governance](leadership-governance/README.md) | 50–51 | 50+ | ✅ |
"""
        modules_readme.write_text(
            modules_readme.read_text() + addition, encoding="utf-8"
        )
        print("Updated modules/README.md")


if __name__ == "__main__":
    main()
