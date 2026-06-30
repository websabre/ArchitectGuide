#!/usr/bin/env python3
"""Copy markdown content and generate navigation manifest for the static site."""

import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
CONTENT_OUT = SITE / "public" / "content"
NAV_OUT = SITE / "src" / "data" / "navigation.json"

WEEK_TOPICS = {
    1: "C# Language Mastery",
    2: ".NET Runtime & Ecosystem",
    3: "SOLID & Clean Architecture",
    4: "Design Patterns",
    5: "Data Structures",
    6: "Algorithms & Complexity",
    7: "SQL Server",
    8: "PostgreSQL",
    9: "Azure Fundamentals",
    10: "Azure Compute",
    11: "Azure Data Platform",
    12: "Azure Identity",
    13: "Azure Networking",
    14: "Azure Security",
    15: "Azure Integration",
    16: "Azure Capstone",
    17: "AWS Fundamentals",
    18: "AWS Compute",
    19: "AWS Data & VPC",
    20: "Multi-Cloud",
    21: "Distributed Systems",
    22: "Microservices",
    23: "Domain-Driven Design",
    24: "Microservices Capstone",
    25: "Docker & Containers",
    26: "Kubernetes Fundamentals",
    27: "Kubernetes Advanced",
    28: "Linux for Architects",
    29: "DevOps Culture",
    30: "CI/CD Pipelines",
    31: "Infrastructure as Code",
    32: "Observability",
    33: "System Design",
    34: "Scalability & Caching",
    35: "Messaging & Events",
    36: "System Design Capstone",
    37: "AI/ML Architecture",
    38: "RAG & Vector Search",
    39: "LLMOps",
    40: "AI Capstone",
    41: "Architecture Reviews",
    42: "FinOps & DR",
    43: "Frontend Architecture",
    44: "Enterprise Case Studies",
    45: "Interview Intensive I",
    46: "Interview Intensive II",
    47: "Interview Intensive III",
    48: "Whiteboard Mocks I",
    49: "Whiteboard Mocks II",
    50: "Leadership I",
    51: "Leadership II",
    52: "Graduation Capstone",
}

PHASE_NAMES = {
    1: "Month 1 — .NET Foundation",
    2: "Month 2 — Data & Algorithms",
    3: "Month 3 — Azure Core",
    4: "Month 4 — Azure Deep Dive",
    5: "Month 5 — AWS & Multi-Cloud",
    6: "Month 6 — Distributed Systems",
    7: "Month 7 — Containers & K8s",
    8: "Month 8 — DevOps",
    9: "Month 9 — System Design",
    10: "Month 10 — AI Architecture",
    11: "Month 11 — Enterprise",
    12: "Month 12 — Interview & Graduation",
}

WEEK_SECTIONS = [
    ("README.md", "Overview"),
    ("theory", "Theory"),
    ("diagrams", "Diagrams"),
    ("labs", "Labs"),
    ("exercises", "Exercises"),
    ("interview-questions", "Interview Q&A"),
    ("case-studies", "Case Studies"),
    ("assessments", "Assessments"),
]


def doc_path(rel: str) -> str:
    rel = rel.replace("\\", "/")
    if rel.endswith(".md"):
        rel = rel[:-3]
    if rel.endswith("/README"):
        rel = rel[: -len("/README")]
    return f"/doc/{rel}" if rel else "/doc"


def item(title: str, path: str, children=None):
    entry = {"title": title, "path": path}
    if children:
        entry["children"] = children
    return entry


def week_children(week_num: int) -> list:
    week_dir = ROOT / f"weeks/week-{week_num:02d}"
    if not week_dir.exists():
        return []
    base = f"weeks/week-{week_num:02d}"
    children = []
    for segment, label in WEEK_SECTIONS:
        if segment.endswith(".md"):
            if segment == "README.md":
                continue  # week overview = parent nav item
            p = week_dir / segment
            if p.exists():
                children.append(item(label, doc_path(f"{base}/{segment[:-3]}")))
        else:
            folder = week_dir / segment
            if folder.exists():
                sub = []
                section_path = doc_path(f"{base}/{segment}/README")
                for md in sorted(folder.glob("*.md")):
                    if md.name == "README.md":
                        continue
                    name = md.stem.replace("-", " ").title()
                    sub.append(item(name, doc_path(f"{base}/{segment}/{md.stem}")))
                if sub or (folder / "README.md").exists():
                    children.append(item(label, section_path, sub if sub else None))
    cm = week_dir / "common-mistakes.md"
    if cm.exists():
        children.append(item("Common Mistakes", doc_path(f"{base}/common-mistakes")))
    return children


def scan_dir_nav(folder: Path, base_path: str, max_depth: int = 2) -> list:
    if not folder.exists():
        return []
    items = []
    if max_depth <= 0:
        return items
    for child in sorted(folder.iterdir()):
        if child.is_dir() and not child.name.startswith("."):
            sub_path = f"{base_path}/{child.name}" if base_path else child.name
            readme = child / "README.md"
            md_files = [f for f in sorted(child.glob("*.md")) if f.name != "README.md"]
            sub_items = scan_dir_nav(child, sub_path, max_depth - 1) if max_depth > 1 else []

            if readme.exists():
                items.append(
                    item(
                        child.name.replace("-", " ").title(),
                        doc_path(f"{sub_path}/README"),
                        sub_items or None,
                    )
                )
            elif md_files:
                file_children = [
                    item(f.stem.replace("-", " ").title(), doc_path(f"{sub_path}/{f.stem}"))
                    for f in md_files
                ]
                items.append(
                    item(
                        child.name.replace("-", " ").title(),
                        file_children[0]["path"],
                        file_children if len(file_children) > 1 else None,
                    )
                )
            elif sub_items:
                items.append(
                    item(
                        child.name.replace("-", " ").title(),
                        sub_items[0]["path"],
                        sub_items if len(sub_items) > 1 else None,
                    )
                )
        elif child.suffix == ".md" and child.name != "README.md":
            rel = f"{base_path}/{child.stem}" if base_path else child.stem
            items.append(item(child.stem.replace("-", " ").title(), doc_path(rel)))
    return items


def build_navigation() -> dict:
    sections = []

    sections.append({
        "title": "Start",
        "items": [
            item("Home", "/"),
            item("How to Use", doc_path("docs/getting-started/how-to-use-this-guide")),
            item("Syllabus", doc_path("SYLLABUS")),
            item("Curriculum Map", doc_path("CURRICULUM-MAP")),
            item("12-Month Study Plan", doc_path("STUDY-PLAN-12-MONTHS")),
        ],
    })

    # Weeks by phase
    for phase in range(1, 13):
        week_items = []
        for w in range((phase - 1) * 4 + 1, min(phase * 4 + 1, 53)):
            if w > 52:
                break
            topic = WEEK_TOPICS.get(w, f"Week {w}")
            week_items.append(
                item(
                    f"Week {w:02d} — {topic}",
                    doc_path(f"weeks/week-{w:02d}/README"),
                    week_children(w),
                )
            )
        sections.append({
            "title": PHASE_NAMES[phase],
            "items": week_items,
        })

    sections.append({
        "title": "Program",
        "items": [
            item(f"Phase {i} Capstone", doc_path(f"program/phase-{i:02d}-month-{i:02d}/capstone"))
            for i in range(1, 13)
        ],
    })

    sections.append({
        "title": "Modules",
        "items": scan_dir_nav(ROOT / "modules", "modules", max_depth=1),
    })

    sections.append({
        "title": "Interview Prep",
        "items": scan_dir_nav(ROOT / "interview-prep", "interview-prep", max_depth=1),
    })

    sections.append({
        "title": "Documentation",
        "items": scan_dir_nav(ROOT / "docs", "docs", max_depth=2),
    })

    sections.append({
        "title": "Resources",
        "items": [
            item("Case Studies Index", doc_path("case-studies/README")),
            item("Templates", doc_path("templates/case-study-template")),
        ],
    })

    return {"sections": sections}


def copy_markdown():
    if CONTENT_OUT.exists():
        shutil.rmtree(CONTENT_OUT)
    CONTENT_OUT.mkdir(parents=True, exist_ok=True)

    skip_dirs = {".git", "site", "node_modules", ".cursor", "scripts"}
    count = 0
    for md in ROOT.rglob("*.md"):
        parts = set(md.relative_to(ROOT).parts)
        if parts & skip_dirs:
            continue
        rel = md.relative_to(ROOT)
        dest = CONTENT_OUT / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(md, dest)
        count += 1
    return count


def main():
    NAV_OUT.parent.mkdir(parents=True, exist_ok=True)
    nav = build_navigation()
    NAV_OUT.write_text(json.dumps(nav, indent=2), encoding="utf-8")
    count = copy_markdown()
    print(f"Navigation written to {NAV_OUT.relative_to(ROOT)}")
    print(f"Copied {count} markdown files to {CONTENT_OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
