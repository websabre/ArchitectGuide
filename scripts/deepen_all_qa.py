#!/usr/bin/env python3
"""Deepen all stub weekly Q&A files with substantive architect-level content."""

from __future__ import annotations

import re
from pathlib import Path

from qa_question_bank import (
    CONCEPTS,
    EXPERT_SCENARIOS,
    QUESTION_FORMS,
    WEEK_BANK,
    WEEK_TOPICS,
)

ROOT = Path(__file__).resolve().parent.parent

STUB_MARKERS = (
    "Concise structured answer",
    "Concise answer.",
    "Concise answer\n",
    "Concise architect-level answer",
    "Architect question on",
    "Architect-level question",
    "Azure architect question on",
    "Detailed answer with trade-offs for",
    "Detailed answer with Azure service comparison",
    "Expanded answer for",
)

SKIP_FILES = {
    # Week 29-32 fundamentals Q001-Q010 manually deepened
    (29, "01-fundamentals-qa.md"),
    (30, "01-fundamentals-qa.md"),
    (31, "01-fundamentals-qa.md"),
    (32, "01-fundamentals-qa.md"),
}

FILE_SPECS = {
    "01-fundamentals-qa.md": (30, "Fundamentals"),
    "02-intermediate-qa.md": (40, "Intermediate"),
    "03-advanced-qa.md": (30, "Advanced"),
    "04-expert-scenarios.md": (20, "Expert"),
    "01-qa-bank.md": (50, "Intermediate"),
}

PREMIUM_HEADER = """> Q001–Q005: Premium format. Q006+: Practice bank with full answers.
> Cross-reference: [Interview prep hub](../../../interview-prep/README.md)

---

"""

PREMIUM_QA = """
## Q{num:03d}: {title}

| Attribute | Value |
|-----------|-------|
| **Difficulty** | {difficulty} |
| **Category** | {category} |
| **Frequency** | {frequency} |

### Question

{question}

### Short Answer (30 seconds)

{short}

### Detailed Answer (3–5 minutes)

{detailed}

### Architecture Perspective

{perspective}

### Follow-up Questions

1. {fu1}
2. {fu2}

### Common Mistakes in Interviews

{mistakes}

---
"""

STANDARD_QA = """
## Q{num:03d}: {title}

| Attribute | Value |
|-----------|-------|
| **Difficulty** | {difficulty} |
| **Category** | {category} |

### Question

{question}

### Short Answer (30 seconds)

{short}

### Detailed Answer

{detailed}

---
"""

EXPERT_QA = """
## Q{num:03d}: {title} — Scenario

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | {category} |
| **Type** | Scenario |

### Scenario

{question}

### What Interviewers Evaluate

{evaluate}

### Recommended Response Structure

{structure}

### Key Points to Cover

{points}

---
"""


def is_stub(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if any(m in text for m in STUB_MARKERS):
        return True
    if re.search(r"### Detailed Answer\n\n[A-Z][^\n]{0,80}\.\n", text):
        if "Architecture Perspective" not in text:
            return True
    return False


def premium_prefix(path: Path) -> tuple[str | None, int]:
    """Preserve hand-crafted Q001–Q010 in weeks 29–32 fundamentals."""
    text = path.read_text(encoding="utf-8")
    m = re.search(r"\n## Q011:", text)
    if m and "Architecture Perspective" in text[: m.start()]:
        return text[: m.start()], 11
    return None, 1


def should_skip(week: int, filename: str, path: Path) -> bool:
    if not is_stub(path):
        return True
    if week == 1 and filename == "01-fundamentals-qa.md":
        if path.stat().st_size > 15000 and premium_prefix(path)[0] is None:
            return True
    return False


def get_concepts(week: int) -> list[tuple]:
    bank_key = WEEK_BANK.get(week, "System Design")
    base = list(CONCEPTS.get(bank_key, CONCEPTS["System Design"]))
    # Blend secondary bank for variety
    topic, cat = WEEK_TOPICS[week]
    if bank_key != "Azure" and "Azure" in cat:
        base.extend(CONCEPTS["Azure"][:5])
    if week in range(45, 53):
        base.extend(CONCEPTS["Microservices"][:5])
    return base


def concept_at(concepts: list, index: int) -> tuple:
    return concepts[index % len(concepts)]


def build_question(week: int, q_index: int, form_index: int, difficulty: str) -> dict:
    topic, _ = WEEK_TOPICS[week]
    concepts = get_concepts(week)
    title, category, when_use, when_avoid, example = concept_at(concepts, q_index)
    form_name, form_tpl = QUESTION_FORMS[form_index % len(QUESTION_FORMS)]
    question = form_tpl.format(title=title, topic=topic)

    short = (
        f"{title}: use when {when_use.lower()}; avoid when {when_avoid.lower()}. "
        f"In {topic}, this shapes reliability, cost, and team autonomy."
    )
    detailed = (
        f"**{title}** in the context of {topic}.\n\n"
        f"**When to use:** {when_use}\n\n"
        f"**When to avoid:** {when_avoid}\n\n"
        f"**Production example:** {example}\n\n"
        f"**Architect lens ({form_name}):** Document the decision in an ADR. "
        f"Measure impact via SLIs — latency, error rate, and cost per transaction. "
        f"Present trade-offs to stakeholders in business terms, not only technology."
    )
    perspective = (
        f"Senior developers explain *how* {title} works. Architects explain *when* it applies, "
        f"what it costs to operate, and what you give up. Tie {category} choices to "
        f"deployment frequency, blast radius, and organizational structure."
    )
    return {
        "title": title,
        "category": category,
        "question": question,
        "short": short,
        "detailed": detailed,
        "perspective": perspective,
        "fu1": f"What changes at 10x scale for {title}?",
        "fu2": f"How do you test or validate {title} in CI/CD?",
        "mistakes": f"- Applying {title} without requirements\n- Ignoring operational cost\n- No rollback plan",
        "frequency": "Common" if difficulty == "Fundamentals" else "Occasional",
    }


def build_expert(week: int, q_index: int) -> dict:
    topic, _ = WEEK_TOPICS[week]
    concepts = get_concepts(week)
    title, category, when_use, when_avoid, example = concept_at(concepts, q_index)
    tpl = EXPERT_SCENARIOS[q_index % len(EXPERT_SCENARIOS)]
    scenario = tpl[1].format(topic=topic, title=title)
    return {
        "title": f"{topic} — {tpl[0]}",
        "category": category,
        "question": scenario,
        "evaluate": "Structured thinking, trade-offs, stakeholder communication, and measurable outcomes.",
        "structure": "Clarify constraints → State options → Recommend with ADR rationale → Risks and mitigations → Metrics for success.",
        "points": f"- Apply {title} correctly ({when_use})\n- Avoid anti-pattern: {when_avoid}\n- Reference: {example}",
    }


def generate_file(week: int, filename: str, count: int, difficulty: str, start_q: int = 1) -> str:
    topic, _ = WEEK_TOPICS[week]
    lines = [f"# Week {week:02d} — {difficulty} Q&A\n\n"]
    if filename == "01-fundamentals-qa.md" and start_q == 1:
        lines.append(PREMIUM_HEADER)
    elif filename == "01-qa-bank.md":
        lines.append(f"> **Topic:** {topic} | **Count:** {count}\n\n---\n\n")
    elif start_q == 1:
        lines.append("---\n\n")

    start_num = {"01-fundamentals-qa.md": 1, "02-intermediate-qa.md": 31,
                 "03-advanced-qa.md": 71, "04-expert-scenarios.md": 101,
                 "01-qa-bank.md": 1}.get(filename, 1)
    if start_q > start_num:
        start_num = start_q

    for i in range(count):
        q_num = start_num + i
        idx = i + week
        if filename == "04-expert-scenarios.md":
            ex = build_expert(week, idx)
            lines.append(EXPERT_QA.format(num=q_num, **ex))
        elif filename == "01-fundamentals-qa.md" and start_q == 1 and i < 5:
            data = build_question(week, idx, i, difficulty)
            lines.append(PREMIUM_QA.format(num=q_num, difficulty=difficulty, **data))
        else:
            data = build_question(week, idx, i + q_num, difficulty)
            lines.append(STANDARD_QA.format(num=q_num, difficulty=difficulty, **data))

    return "".join(lines)


def process_week(week: int) -> int:
    updated = 0
    iq_dir = ROOT / f"weeks/week-{week:02d}/interview-questions"
    if not iq_dir.exists():
        return 0
    for path in sorted(iq_dir.glob("*.md")):
        if path.name == "README.md":
            continue
        spec = FILE_SPECS.get(path.name)
        if not spec:
            continue
        if should_skip(week, path.name, path):
            print(f"  skip: week-{week:02d}/{path.name}")
            continue
        count, difficulty = spec
        prefix, start_q = premium_prefix(path)
        gen_count = count - (start_q - 1) if prefix else count
        content = generate_file(week, path.name, gen_count, difficulty, start_q=start_q)
        if prefix:
            content = prefix + content.split("---\n\n", 1)[-1] if "---\n\n" in content else prefix + content
            # Rebuild: keep prefix, append generated questions only
            topic, _ = WEEK_TOPICS[week]
            tail_lines = []
            start_num = start_q
            for i in range(gen_count):
                q_num = start_num + i
                data = build_question(week, i + week, i + q_num, difficulty)
                tail_lines.append(STANDARD_QA.format(num=q_num, difficulty=difficulty, **data))
            content = prefix + "".join(tail_lines)
        path.write_text(content, encoding="utf-8")
        updated += 1
        print(f"  deepened: week-{week:02d}/{path.name} ({gen_count} Q, start Q{start_q:03d})")
    return updated


def main():
    total = 0
    for week in range(1, 53):
        if week not in WEEK_TOPICS:
            continue
        n = process_week(week)
        total += n
    print(f"\nDone — {total} files deepened")


if __name__ == "__main__":
    main()
