#!/usr/bin/env python3
"""Splice hand-crafted Q001–Q010 for weeks 3–4 and Q011–Q050 for Azure weeks 9–16."""

import re
import sys
from pathlib import Path

from premium_qa_data import PREMIUM_HEADER, QA_BLOCK
from premium_qa_data_weeks_3_4_q001_q010 import ALL_WEEKS_3_4_Q001_Q010

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = Path(__file__).resolve().parent

INTERMEDIATE_QA_BLOCK = QA_BLOCK.replace(
    "| **Difficulty** | Fundamentals |",
    "| **Difficulty** | Intermediate |",
)

FULL_PREMIUM_HEADER = """# Week {week:02d} — Fundamentals Interview Q&A

> Q001–Q030: Premium format (Week 1 quality).  
> See also: [Interview prep hub](../../../interview-prep/README.md)

---

"""

AZURE_FULL_PREMIUM_HEADER = """# Week {week:02d} — Intermediate Q&A

> Q001–Q050: Premium format (Week 1 quality).  
> **Topic:** {topic} | **Count:** 50

---

"""

AZURE_TOPICS = {
    9: "Azure Fundamentals & WAF",
    10: "Azure Compute & App Services",
    11: "Azure Data Platform",
    12: "Azure Identity",
    13: "Azure Networking",
    14: "Azure Security",
    15: "Azure Integration & Messaging",
    16: "Azure Production Capstone",
}


def render_premium_block(num: int, item: dict, difficulty: str = "Fundamentals") -> str:
    block = INTERMEDIATE_QA_BLOCK if difficulty == "Intermediate" else QA_BLOCK
    return block.format(num=num, **item)


def splice_week3_4_q001_q010(week: int, questions: list) -> None:
    path = ROOT / f"weeks/week-{week:02d}/interview-questions/01-fundamentals-qa.md"
    existing = path.read_text(encoding="utf-8")
    idx = existing.find("## Q011:")
    if idx == -1:
        raise ValueError(f"Q011 not found week {week}")
    tail = existing[idx:]
    parts = [FULL_PREMIUM_HEADER.format(week=week)]
    for i, item in enumerate(questions, 1):
        parts.append(render_premium_block(i, item))
    path.write_text("".join(parts) + tail, encoding="utf-8")
    print(f"Week {week:02d} fundamentals Q001–Q010 handcrafted")


def splice_azure_q011_q050(week: int, questions: list) -> None:
    path = ROOT / f"weeks/week-{week:02d}/interview-questions/01-qa-bank.md"
    existing = path.read_text(encoding="utf-8")
    idx = existing.find("## Q011:")
    if idx == -1:
        raise ValueError(f"Q011 not found week {week} qa-bank")
    prefix = existing[:idx]
    prefix = re.sub(
        r"> Q001–Q010[^\n]*\n> \*\*Topic:\*\*",
        "> Q001–Q050: Premium format (Week 1 quality).  \n> **Topic:**",
        prefix,
        count=1,
    )
    if "Q001–Q050" not in prefix:
        # rebuild header from scratch keeping title line
        title_match = re.search(r"^# Week \d+ — .+$", prefix, re.M)
        title = title_match.group(0) if title_match else f"# Week {week:02d} — Intermediate Q&A"
        prefix = AZURE_FULL_PREMIUM_HEADER.format(week=week, topic=AZURE_TOPICS[week])
        # preserve Q001-Q010 from existing
        q001_idx = existing.find("## Q001:")
        q011_idx = existing.find("## Q011:")
        if q001_idx != -1 and q011_idx != -1:
            prefix = prefix + existing[q001_idx:q011_idx]
    parts = [prefix]
    for i, item in enumerate(questions, 11):
        parts.append(render_premium_block(i, item, difficulty="Intermediate"))
    path.write_text("".join(parts), encoding="utf-8")
    print(f"Week {week:02d} qa-bank Q011–Q050 handcrafted ({len(questions)} Q)")


def load_azure_tails() -> dict:
    """Import all azure tail modules weeks 9–16."""
    from premium_qa_data_azure_q11_50_w09 import WEEK_9_Q011_Q050, WEEK_10_Q011_Q050
    from premium_qa_data_azure_q11_50_w11 import WEEK_11_Q011_Q050
    from premium_qa_data_azure_q11_50_w12 import WEEK_12_Q011_Q050
    from premium_qa_data_azure_q11_50_w13 import WEEK_13_Q011_Q050, WEEK_14_Q011_Q050
    from premium_qa_data_azure_q11_50_w15 import WEEK_15_Q011_Q050, WEEK_16_Q011_Q050

    tails = {
        9: WEEK_9_Q011_Q050, 10: WEEK_10_Q011_Q050,
        11: WEEK_11_Q011_Q050, 12: WEEK_12_Q011_Q050,
        13: WEEK_13_Q011_Q050, 14: WEEK_14_Q011_Q050,
        15: WEEK_15_Q011_Q050, 16: WEEK_16_Q011_Q050,
    }
    for week, qs in tails.items():
        if len(qs) != 40:
            raise ValueError(f"Week {week} has {len(qs)} questions, expected 40")
    return tails


def main():
    for week, questions in ALL_WEEKS_3_4_Q001_Q010.items():
        splice_week3_4_q001_q010(week, questions)
    tails = load_azure_tails()
    for week, questions in tails.items():
        splice_azure_q011_q050(week, questions)
    print("Done — weeks 3–4 Q001–Q010 + Azure 9–16 Q011–Q050")


if __name__ == "__main__":
    main()
