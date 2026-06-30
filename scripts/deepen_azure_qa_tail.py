#!/usr/bin/env python3
"""Deepen Azure weeks 9–16 Q011–Q050 with unique per-week concepts."""

from pathlib import Path

from azure_week_concepts import AZURE_WEEK_CONCEPTS
from deepen_all_qa import build_question
from premium_qa_data import QA_BLOCK
from qa_question_bank import QUESTION_FORMS, WEEK_TOPICS

ROOT = Path(__file__).resolve().parent.parent

INTERMEDIATE_BLOCK = QA_BLOCK.replace(
    "| **Difficulty** | Fundamentals |",
    "| **Difficulty** | Intermediate |",
)


def render_tail_block(num: int, data: dict) -> str:
    return INTERMEDIATE_BLOCK.format(
        num=num,
        title=data["title"],
        category=data["category"],
        frequency=data.get("frequency", "Common"),
        question=data["question"],
        short=data["short"],
        detailed=data["detailed"],
        perspective=data["perspective"],
        followups=f"1. **{data['fu1']}**\n2. **{data['fu2']}**",
        mistakes=data["mistakes"],
    )


def deepen_week(week: int) -> None:
    path = ROOT / f"weeks/week-{week:02d}/interview-questions/01-qa-bank.md"
    text = path.read_text(encoding="utf-8")
    idx = text.find("## Q011:")
    if idx == -1:
        raise ValueError(f"Q011 not found in week {week}")
    prefix = text[:idx]
    concepts = AZURE_WEEK_CONCEPTS[week]
    topic, _ = WEEK_TOPICS[week]
    parts = [prefix]
    for i, concept in enumerate(concepts[:40]):
        q_num = 11 + i
        title, category, when_use, when_avoid, example = concept
        form_name, form_tpl = QUESTION_FORMS[i % len(QUESTION_FORMS)]
        data = build_question(week, q_num + week, i, "Intermediate")
        data["title"] = title
        data["category"] = category
        data["question"] = form_tpl.format(title=title, topic=topic)
        data["short"] = (
            f"{title}: use when {when_use.lower()}; avoid when {when_avoid.lower()}. "
            f"Example: {example}."
        )
        data["detailed"] = (
            f"**{title}** — {example}\n\n"
            f"**When to use:** {when_use}\n\n"
            f"**When to avoid:** {when_avoid}\n\n"
            f"**Architect lens:** Document in ADR; validate with Azure Monitor metrics, cost dashboards, and failure drills."
        )
        data["fu1"] = f"How does {title} affect SLA and cost at scale?"
        data["fu2"] = f"What Azure tooling validates {title} in CI/CD?"
        data["perspective"] = (
            f"Senior developers explain *how* {title} works. Architects explain *when* it applies, "
            f"what it costs to operate, and what you give up. Tie {category} choices to "
            f"reliability, security posture, and FinOps accountability."
        )
        data["mistakes"] = (
            f"- Misapplying {title} without workload context\n"
            f"- Ignoring operational cost of {category.lower()} choices\n"
            f"- No rollback or exemption process"
        )
        parts.append(render_tail_block(q_num, data))
    path.write_text("".join(parts), encoding="utf-8")
    print(f"Week {week:02d} qa-bank Q011–Q050 deepened")


def main():
    for week in range(9, 17):
        deepen_week(week)
    print("Done — Azure Q011–Q050 deepened for weeks 9–16")


if __name__ == "__main__":
    main()
