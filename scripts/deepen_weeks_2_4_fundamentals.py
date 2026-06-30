#!/usr/bin/env python3
"""Deepen weeks 2–4 fundamentals to full premium format."""

from pathlib import Path

from deepen_all_qa import PREMIUM_QA, build_question
from qa_question_bank import CONCEPTS, QUESTION_FORMS, WEEK_TOPICS

ROOT = Path(__file__).resolve().parent.parent

WEEK_BANK_KEY = {
    2: ".NET", 3: "Architecture", 4: "Design Patterns",
    17: "AWS", 18: "AWS", 19: "AWS", 20: "Multi-Cloud",
}

PREMIUM_HEADER = """# Week {week:02d} — Fundamentals Interview Q&A

> Q001–Q010: Premium format (Week 1 quality). Q011–Q030: Practice bank (premium depth).  
> See also: [Interview prep hub](../../../interview-prep/README.md)

---

"""


def build_premium(week: int, q_num: int, concept_idx: int) -> dict:
    bank_key = WEEK_BANK_KEY[week]
    concepts = CONCEPTS[bank_key]
    title, category, when_use, when_avoid, example = concepts[concept_idx % len(concepts)]
    topic, _ = WEEK_TOPICS[week]
    form_name, form_tpl = QUESTION_FORMS[concept_idx % len(QUESTION_FORMS)]
    data = build_question(week, q_num + week, concept_idx, "Fundamentals")
    data["title"] = title
    data["category"] = category
    data["question"] = form_tpl.format(title=title, topic=topic)
    data["short"] = (
        f"{title}: use when {when_use.lower()}; avoid when {when_avoid.lower()}. "
        f"In {topic}, this shapes maintainability and team velocity."
    )
    data["detailed"] = (
        f"**{title}** — {example}\n\n"
        f"**When to use:** {when_use}\n\n"
        f"**When to avoid:** {when_avoid}\n\n"
        f"**Production example:** {example}\n\n"
        f"**Architect lens:** Document the decision in an ADR. Measure via code review adherence, defect rate, and onboarding time for new developers."
    )
    data["fu1"] = f"How do you enforce {title} in a 50-developer .NET org?"
    data["fu2"] = f"What metrics show {title} is working or failing?"
    data["perspective"] = (
        f"Senior developers explain *how* {title} works. Architects explain *when* it applies, "
        f"what it costs to operate, and what you give up. Tie {category} choices to "
        f"maintainability, testability, and team autonomy."
    )
    data["mistakes"] = (
        f"- Applying {title} dogmatically without context\n"
        f"- Ignoring team skill and delivery pressure\n"
        f"- No examples in internal engineering handbook"
    )
    return data


def deepen_week(week: int, preserve_q001_q010: bool = False) -> None:
    path = ROOT / f"weeks/week-{week:02d}/interview-questions/01-fundamentals-qa.md"
    existing = path.read_text(encoding="utf-8")
    start_q = 1
    if preserve_q001_q010:
        idx = existing.find("## Q011:")
        if idx == -1:
            raise ValueError(f"Q011 not found week {week}")
        prefix = existing[:idx]
        start_q = 11
    else:
        prefix = PREMIUM_HEADER.format(week=week)

    parts = [prefix]
    count = 30 if start_q == 1 else 20
    bank_key = WEEK_BANK_KEY[week]
    concepts = CONCEPTS[bank_key]
    for i in range(count):
        q_num = start_q + i
        data = build_premium(week, q_num, i)
        parts.append(PREMIUM_QA.format(num=q_num, difficulty="Fundamentals", **data))
    path.write_text("".join(parts), encoding="utf-8")
    label = "Q001–Q030" if start_q == 1 else "Q011–Q030"
    print(f"Week {week:02d} fundamentals {label} deepened")


def main():
    deepen_week(2, preserve_q001_q010=True)
    deepen_week(3)
    deepen_week(4)
    for week in range(17, 21):
        deepen_week(week, preserve_q001_q010=True)
    print("Done — weeks 2–4 and 17–20 fundamentals deepened")


if __name__ == "__main__":
    main()
