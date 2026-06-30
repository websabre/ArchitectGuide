#!/usr/bin/env python3
"""Generate subfolder README indexes and fix week README location links."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FOLDER_LINKS = {
    "theory/": "theory/README.md",
    "diagrams/": "diagrams/README.md",
    "labs/": "labs/README.md",
    "exercises/": "exercises/README.md",
    "interview-questions/": "interview-questions/README.md",
    "case-studies/": "case-studies/README.md",
    "assessments/": "assessments/README.md",
}


def list_md_files(folder: Path) -> list[Path]:
    if not folder.exists():
        return []
    return sorted(folder.glob("*.md"))


def write_theory_readme(week_dir: Path, week: int):
    folder = week_dir / "theory"
    folder.mkdir(parents=True, exist_ok=True)
    files = list_md_files(folder)
    lines = [
        f"# Week {week:02d} — Theory\n",
        f"\n> [← Week {week:02d} overview](../README.md)\n\n",
        "## Files\n\n",
    ]
    if files:
        for f in files:
            if f.name == "README.md":
                continue
            lines.append(f"- [{f.name}]({f.name})\n")
        start = next((f for f in files if f.name.startswith("01-")), files[0])
        lines.append(f"\n**Start here:** [{start.name}]({start.name})\n")
    else:
        lines.append("*Content coming soon.*\n")
    lines.append(f"\n---\n\n[← Back to Week {week:02d}](../README.md)\n")
    (folder / "README.md").write_text("".join(lines), encoding="utf-8")


def write_labs_readme(week_dir: Path, week: int):
    folder = week_dir / "labs"
    folder.mkdir(parents=True, exist_ok=True)
    files = [f for f in list_md_files(folder) if f.name != "README.md"]
    lines = [
        f"# Week {week:02d} — Labs\n",
        f"\n> [← Week {week:02d} overview](../README.md)\n\n",
        "## Hands-on Labs\n\n",
    ]
    if files:
        for f in files:
            lines.append(f"- [{f.stem.replace('-', ' ').title()}]({f.name})\n")
    else:
        lines.append("*Lab content coming soon.*\n")
    lines.append(f"\n---\n\n[← Back to Week {week:02d}](../README.md)\n")
    (folder / "README.md").write_text("".join(lines), encoding="utf-8")


def write_case_studies_readme(week_dir: Path, week: int):
    folder = week_dir / "case-studies"
    folder.mkdir(parents=True, exist_ok=True)
    files = [f for f in list_md_files(folder) if f.name != "README.md"]
    lines = [
        f"# Week {week:02d} — Case Studies\n",
        f"\n> [← Week {week:02d} overview](../README.md)\n\n",
    ]
    if files:
        lines.append("## Scenarios\n\n")
        for f in files:
            lines.append(f"- [{f.name}]({f.name})\n")
    else:
        lines.append("*Case study coming soon.*\n")
    lines.append(f"\n---\n\n[← Back to Week {week:02d}](../README.md)\n")
    (folder / "README.md").write_text("".join(lines), encoding="utf-8")


def write_assessments_readme(week_dir: Path, week: int):
    folder = week_dir / "assessments"
    folder.mkdir(parents=True, exist_ok=True)
    files = [f for f in list_md_files(folder) if f.name != "README.md"]
    assessment = folder / f"week-{week:02d}-assessment.md"
    lines = [
        f"# Week {week:02d} — Assessment\n",
        f"\n> [← Week {week:02d} overview](../README.md)\n\n",
    ]
    if assessment.exists():
        lines.append(f"## Weekly Quiz\n\n- **[Take assessment]({assessment.name})**\n")
    elif files:
        lines.append("## Files\n\n")
        for f in files:
            lines.append(f"- [{f.name}]({f.name})\n")
    else:
        lines.append("*Assessment coming soon.*\n")
    lines.append(f"\n---\n\n[← Back to Week {week:02d}](../README.md)\n")
    (folder / "README.md").write_text("".join(lines), encoding="utf-8")


def write_exercises_readme(week_dir: Path, week: int):
    folder = week_dir / "exercises"
    folder.mkdir(parents=True, exist_ok=True)
    readme = folder / "README.md"
    if readme.exists() and "Back to Week" not in readme.read_text(encoding="utf-8"):
        text = readme.read_text(encoding="utf-8")
        if not text.startswith(f"# Week {week:02d}"):
            text = f"# Week {week:02d} — Exercises\n\n> [← Week {week:02d} overview](../README.md)\n\n" + text
        text += f"\n---\n\n[← Back to Week {week:02d}](../README.md)\n"
        readme.write_text(text, encoding="utf-8")
    elif not readme.exists():
        files = [f for f in list_md_files(folder) if f.name != "README.md"]
        lines = [
            f"# Week {week:02d} — Exercises\n",
            f"\n> [← Week {week:02d} overview](../README.md)\n\n",
        ]
        if files:
            for f in files:
                lines.append(f"- [{f.name}]({f.name})\n")
        else:
            lines.append("1. **Design exercise** — Whiteboard a solution (30 min).\n")
            lines.append("2. **Trade-off analysis** — Document pros/cons (1 page).\n")
            lines.append("3. **Teach-back** — Explain a core concept to a colleague (5 min).\n")
        lines.append(f"\n---\n\n[← Back to Week {week:02d}](../README.md)\n")
        readme.write_text("".join(lines), encoding="utf-8")


def write_interview_readme(week_dir: Path, week: int):
    folder = week_dir / "interview-questions"
    folder.mkdir(parents=True, exist_ok=True)
    readme = folder / "README.md"
    qa_files = [f for f in list_md_files(folder) if f.name != "README.md" and "qa" in f.name]
    if readme.exists():
        text = readme.read_text(encoding="utf-8")
        if "[← Back to Week" not in text:
            text += f"\n---\n\n[← Back to Week {week:02d}](../README.md)\n"
            readme.write_text(text, encoding="utf-8")
    else:
        lines = [
            f"# Week {week:02d} — Interview Questions\n",
            f"\n> [← Week {week:02d} overview](../README.md)\n\n",
            "| File | Count | Difficulty |\n|------|-------|------------|\n",
        ]
        for f in qa_files:
            lines.append(f"| [{f.name}]({f.name}) | — | — |\n")
        if qa_files:
            lines.append(f"\n**Start here:** [{qa_files[0].name}]({qa_files[0].name})\n")
        lines.append(f"\n---\n\n[← Back to Week {week:02d}](../README.md)\n")
        readme.write_text("".join(lines), encoding="utf-8")


def write_diagrams_readme(week_dir: Path, week: int):
    folder = week_dir / "diagrams"
    folder.mkdir(parents=True, exist_ok=True)
    readme = folder / "README.md"
    if readme.exists():
        text = readme.read_text(encoding="utf-8")
        if "[← Back to Week" not in text:
            text += f"\n---\n\n[← Back to Week {week:02d}](../README.md)\n"
            readme.write_text(text, encoding="utf-8")
    else:
        content = f"""# Week {week:02d} — Diagrams

> [← Week {week:02d} overview](../README.md)

Architecture diagrams (Mermaid/C4) for this week.

---

[← Back to Week {week:02d}](../README.md)
"""
        readme.write_text(content, encoding="utf-8")


def fix_week_readme(week_dir: Path):
    readme = week_dir / "README.md"
    if not readme.exists():
        return
    text = readme.read_text(encoding="utf-8")
    original = text
    for old, new in FOLDER_LINKS.items():
        text = text.replace(f"]({old})", f"]({new})")
        text = text.replace(f"**{old.rstrip('/')}**", f"**[{new}]({new})**")  # unlikely

    # Fix week-52 misleading module link
    if "week-52" in str(week_dir):
        text = text.replace(
            "| **Module** | [all](../../README.md) |",
            "| **Module** | [Program overview](../../README.md) · [Interview prep](../../interview-prep/README.md) |",
        )

    # Ensure navigation table has docs link
    if "| Documentation hub |" not in text and "## Navigation" in text:
        text = text.replace(
            "| Phase Overview |",
            "| Documentation hub | [docs/README.md](../../docs/README.md) |\n| Phase Overview |",
        )

    if text != original:
        readme.write_text(text, encoding="utf-8")


def main():
    for week in range(1, 53):
        week_dir = ROOT / f"weeks/week-{week:02d}"
        if not week_dir.exists():
            continue
        write_theory_readme(week_dir, week)
        write_labs_readme(week_dir, week)
        write_case_studies_readme(week_dir, week)
        write_assessments_readme(week_dir, week)
        write_exercises_readme(week_dir, week)
        write_interview_readme(week_dir, week)
        write_diagrams_readme(week_dir, week)
        fix_week_readme(week_dir)
        print(f"Week {week:02d} fixed")

    print("Done.")


if __name__ == "__main__":
    main()
