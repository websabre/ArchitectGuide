#!/usr/bin/env python3
"""Apply hand-crafted premium Q&A: weeks 2–8, 9–16 (Azure), 17–20 (AWS), 21–24, 33–36; Week 1."""

import re

from pathlib import Path

from premium_qa_data import PREMIUM_HEADER, QA_BLOCK
from premium_qa_data_aws import ALL_AWS_WEEKS
from premium_qa_data_azure import ALL_AZURE_WEEKS
from premium_qa_data_b import ALL_WEEKS
from premium_qa_data_week1 import WEEK1_ADVANCED_PREMIUM, WEEK1_EXPERT
from premium_qa_data_week1_fundamentals import WEEK1_FUNDAMENTALS_Q011_Q030
from premium_qa_data_aws_q011_q030 import ALL_AWS_Q011_Q030
from premium_qa_data_week2_q011_q030 import WEEK2_Q011_Q030
from premium_qa_data_week2 import WEEK_2
from premium_qa_data_weeks_3_4_q001_q010 import ALL_WEEKS_3_4_Q001_Q010
from premium_qa_data_weeks_3_4_q011_q030 import ALL_WEEKS_3_4_Q011_Q030
from premium_qa_data_tails_w05_06 import WEEK_5_Q011_Q030, WEEK_6_Q011_Q030
from premium_qa_data_tails_w07_08 import WEEK_7_Q011_Q030, WEEK_8_Q011_Q030
from premium_qa_data_tails_w21_22 import WEEK_21_Q011_Q030, WEEK_22_Q011_Q030
from premium_qa_data_tails_w23_24 import WEEK_23_Q011_Q030, WEEK_24_Q011_Q030
from premium_qa_data_tails_w29_32 import (
    WEEK_29_Q011_Q030,
    WEEK_30_Q011_Q030,
    WEEK_31_Q011_Q030,
    WEEK_32_Q011_Q030,
)
from premium_qa_data_tails_w33_36 import (
    WEEK_33_Q011_Q030,
    WEEK_34_Q011_Q030,
    WEEK_35_Q011_Q030,
    WEEK_36_Q011_Q030,
)
from premium_qa_data_weeks_25_28 import ALL_WEEKS_25_28
from premium_qa_data_week1_intermediate import WEEK1_INTERMEDIATE_Q031_Q070
from premium_qa_data_weeks_37_40_q006_q030 import ALL_WEEKS_37_40_Q006_Q030
from premium_qa_data_weeks_37_40_q001_q005 import ALL_WEEKS_37_40_Q001_Q005
from premium_qa_data_week1_advanced_q081_q100 import WEEK1_ADVANCED_Q081_Q100
from premium_qa_data_weeks_41_44_q006_q030 import ALL_WEEKS_41_44_Q006_Q030
from premium_qa_data_weeks_45_48_q006_q030 import ALL_WEEKS_45_48_Q006_Q030
from premium_qa_data_weeks_49_52_q006_q030 import ALL_WEEKS_49_52_Q006_Q030
from premium_qa_data_weeks_41_44_q001_q005 import ALL_WEEKS_41_44_Q001_Q005
from premium_qa_data_weeks_45_48_q001_q005 import ALL_WEEKS_45_48_Q001_Q005
from premium_qa_data_weeks_49_52_q001_q005 import ALL_WEEKS_49_52_Q001_Q005
from premium_qa_data_weeks_41_42_banks import ALL_WEEKS_41_42_BANKS
from premium_qa_data_weeks_43_44_banks import ALL_WEEKS_43_44_BANKS
from premium_qa_data_weeks_45_46_banks import ALL_WEEKS_45_46_BANKS
from premium_qa_data_weeks_47_48_banks import ALL_WEEKS_47_48_BANKS
from premium_qa_data_weeks_49_50_banks import ALL_WEEKS_49_50_BANKS
from premium_qa_data_weeks_51_52_banks import ALL_WEEKS_51_52_BANKS
from qa_question_bank import CONCEPTS

ALL_WEEKS_41_52_Q006_Q030 = {
    **ALL_WEEKS_41_44_Q006_Q030,
    **ALL_WEEKS_45_48_Q006_Q030,
    **ALL_WEEKS_49_52_Q006_Q030,
}

ALL_WEEKS_41_52_Q001_Q005 = {
    **ALL_WEEKS_41_44_Q001_Q005,
    **ALL_WEEKS_45_48_Q001_Q005,
    **ALL_WEEKS_49_52_Q001_Q005,
}

ALL_WEEKS_41_52_BANKS = {
    **ALL_WEEKS_41_42_BANKS,
    **ALL_WEEKS_43_44_BANKS,
    **ALL_WEEKS_45_46_BANKS,
    **ALL_WEEKS_47_48_BANKS,
    **ALL_WEEKS_49_50_BANKS,
    **ALL_WEEKS_51_52_BANKS,
}

ALL_FUNDAMENTALS_Q011_Q030 = {
    5: WEEK_5_Q011_Q030,
    6: WEEK_6_Q011_Q030,
    7: WEEK_7_Q011_Q030,
    8: WEEK_8_Q011_Q030,
    21: WEEK_21_Q011_Q030,
    22: WEEK_22_Q011_Q030,
    23: WEEK_23_Q011_Q030,
    24: WEEK_24_Q011_Q030,
    29: WEEK_29_Q011_Q030,
    30: WEEK_30_Q011_Q030,
    31: WEEK_31_Q011_Q030,
    32: WEEK_32_Q011_Q030,
    33: WEEK_33_Q011_Q030,
    34: WEEK_34_Q011_Q030,
    35: WEEK_35_Q011_Q030,
    36: WEEK_36_Q011_Q030,
}

ROOT = Path(__file__).resolve().parent.parent

STANDARD_ADVANCED = """
## Q{num:03d}: {title}

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
| **Category** | {category} |

### Question

{question}

### Short Answer (30 seconds)

{short}

### Detailed Answer

{detailed}

---
"""

EXPERT_BLOCK = """
## Q{num:03d}: {title}

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Expert |
| **Category** | {category} |
| **Frequency** | {frequency} |
| **Type** | Scenario |

### Question

{question}

### Short Answer (30 seconds)

{short}

### Detailed Answer

{detailed}

### Architecture Perspective

{perspective}

### Follow-up Questions

{followups}

### Common Mistakes in Interviews

{mistakes}

---
"""

ADVANCED_BLOCK = """
## Q{num:03d}: {title}

| Attribute | Value |
|-----------|-------|
| **Difficulty** | Advanced |
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

{followups}

### Common Mistakes in Interviews

{mistakes}

---
"""


INTERMEDIATE_QA_BLOCK = QA_BLOCK.replace(
    "| **Difficulty** | Fundamentals |",
    "| **Difficulty** | Intermediate |",
)

AZURE_QA_HEADER = """# Week {week:02d} — Intermediate Q&A

> Q001–Q010: Premium format (Week 1 quality). Q011–Q050: Practice bank.  
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

AWS_FUNDAMENTALS_HEADER = """# Week {week:02d} — Fundamentals Q&A

> Q001–Q010: Premium format (Week 1 quality). Q011–Q030: Practice bank (premium depth).  
> Cross-reference: [Interview prep hub](../../../interview-prep/README.md)

---

"""


def render_premium_block(num: int, item: dict, difficulty: str = "Fundamentals") -> str:
    block = INTERMEDIATE_QA_BLOCK if difficulty == "Intermediate" else QA_BLOCK
    return block.format(num=num, **item)


def splice_aws_fundamentals(week: int, questions: list) -> None:
    path = ROOT / f"weeks/week-{week:02d}/interview-questions/01-fundamentals-qa.md"
    existing = path.read_text(encoding="utf-8")
    idx = existing.find("## Q011:")
    if idx == -1:
        raise ValueError(f"Q011 not found in week {week}")
    tail = existing[idx:]
    parts = [AWS_FUNDAMENTALS_HEADER.format(week=week)]
    for i, item in enumerate(questions, 1):
        parts.append(render_premium_block(i, item))
    path.write_text("".join(parts) + tail, encoding="utf-8")
    print(f"Week {week:02d} AWS fundamentals Q001–Q010 handcrafted")


FULL_PREMIUM_HEADER = """# Week {week:02d} — Fundamentals Interview Q&A

> Q001–Q030: Premium format (Week 1 quality).  
> See also: [Interview prep hub](../../../interview-prep/README.md)

---

"""


def splice_week3_4_full(week: int, q001_q010: list, q011_q030: list) -> None:
    path = ROOT / f"weeks/week-{week:02d}/interview-questions/01-fundamentals-qa.md"
    parts = [FULL_PREMIUM_HEADER.format(week=week)]
    for i, item in enumerate(q001_q010, 1):
        parts.append(render_premium_block(i, item))
    for i, item in enumerate(q011_q030, 11):
        parts.append(render_premium_block(i, item))
    path.write_text("".join(parts), encoding="utf-8")
    print(f"Week {week:02d} fundamentals Q001–Q030 full premium")


def splice_fundamentals_full(week: int, questions: list) -> None:
    path = ROOT / f"weeks/week-{week:02d}/interview-questions/01-fundamentals-qa.md"
    parts = [FULL_PREMIUM_HEADER.format(week=week)]
    for i, item in enumerate(questions, 1):
        parts.append(render_premium_block(i, item))
    path.write_text("".join(parts), encoding="utf-8")
    print(f"Week {week:02d} fundamentals Q001–Q030 full premium")


def splice_fundamentals_q006_q030(week: int, questions: list) -> None:
    path = ROOT / f"weeks/week-{week:02d}/interview-questions/01-fundamentals-qa.md"
    existing = path.read_text(encoding="utf-8")
    idx = existing.find("## Q006:")
    if idx == -1:
        raise ValueError(f"Q006 not found in week {week}")
    prefix = existing[:idx]
    if week >= 41:
        header_line = (
            "> Q001–Q005: Premium format. Q006–Q030: Premium format (Week 1 quality).\n"
        )
    else:
        header_line = "> Q001–Q030: Premium format (Week 1 quality).\n"
    prefix = re.sub(r"> Q001–Q0[^\n]*\n", header_line, prefix, count=1)
    parts = [prefix]
    for i, item in enumerate(questions, 6):
        parts.append(render_premium_block(i, item))
    path.write_text("".join(parts), encoding="utf-8")
    print(f"Week {week:02d} fundamentals Q006–Q030 handcrafted")


def splice_week1_intermediate() -> None:
    path = ROOT / "weeks/week-01/interview-questions/02-intermediate-qa.md"
    header = (
        "# Week 01 — Intermediate Q&A\n\n"
        "> Q031–Q070: Premium format (Week 1 quality).\n\n"
        "---\n\n"
    )
    parts = [header]
    for i, item in enumerate(WEEK1_INTERMEDIATE_Q031_Q070, 31):
        parts.append(render_premium_block(i, item, difficulty="Intermediate"))
    path.write_text("".join(parts), encoding="utf-8")
    print("Week 01 intermediate Q031–Q070 handcrafted premium")


def splice_fundamentals_q011_q030(week: int, questions: list) -> None:
    path = ROOT / f"weeks/week-{week:02d}/interview-questions/01-fundamentals-qa.md"
    existing = path.read_text(encoding="utf-8")
    idx = existing.find("## Q011:")
    if idx == -1:
        raise ValueError(f"Q011 not found in week {week}")
    prefix = existing[:idx]
    if week in (3, 4):
        header_line = (
            "> Q001–Q010: Practice bank. Q011–Q030: Premium format (Week 1 quality).\n"
        )
    else:
        header_line = "> Q001–Q030: Premium format (Week 1 quality).\n"
    prefix = re.sub(r"> Q001–Q0[^\n]*\n", header_line, prefix, count=1)
    parts = [prefix]
    for i, item in enumerate(questions, 11):
        parts.append(render_premium_block(i, item))
    path.write_text("".join(parts), encoding="utf-8")
    print(f"Week {week:02d} fundamentals Q011–Q030 handcrafted")


def splice_week2_fundamentals() -> None:
    path = ROOT / "weeks/week-02/interview-questions/01-fundamentals-qa.md"
    existing = path.read_text(encoding="utf-8")
    idx = existing.find("## Q011:")
    if idx == -1:
        raise ValueError("Q011 not found in week 02")
    tail = existing[idx:]
    parts = [PREMIUM_HEADER.format(week=2)]
    for i, item in enumerate(WEEK_2, 1):
        parts.append(render_premium_block(i, item))
    path.write_text("".join(parts) + tail, encoding="utf-8")
    print("Week 02 fundamentals Q001–Q010 handcrafted")


def splice_qa_bank(week: int, questions: list) -> None:
    path = ROOT / f"weeks/week-{week:02d}/interview-questions/01-qa-bank.md"
    existing = path.read_text(encoding="utf-8")
    idx = existing.find("## Q011:")
    if idx == -1:
        raise ValueError(f"Q011 not found in week {week} qa-bank")
    tail = existing[idx:]
    topic = AZURE_TOPICS[week]
    parts = [AZURE_QA_HEADER.format(week=week, topic=topic)]
    for i, item in enumerate(questions, 1):
        parts.append(render_premium_block(i, item, difficulty="Intermediate"))
    path.write_text("".join(parts) + tail, encoding="utf-8")
    print(f"Week {week:02d} qa-bank Q001–Q010 handcrafted")


def splice_week1_fundamentals_q011_q030() -> None:
    path = ROOT / "weeks/week-01/interview-questions/01-fundamentals-qa.md"
    existing = path.read_text(encoding="utf-8")
    marker = "# Part 2: Questions Q011–Q030"
    idx = existing.find(marker)
    if idx == -1:
        raise ValueError("Part 2 marker not found in week 01 fundamentals")
    prefix = existing[:idx]
    part2_header = (
        "# Part 2: Questions Q011–Q030\n\n"
        "> Premium format — full architecture depth.\n\n"
        "---\n"
    )
    parts = [prefix, part2_header]
    for i, item in enumerate(WEEK1_FUNDAMENTALS_Q011_Q030, 11):
        parts.append(render_premium_block(i, item))
    path.write_text("".join(parts), encoding="utf-8")
    print("Week 01 fundamentals Q011–Q030 handcrafted premium")


def splice_fundamentals(week: int, questions: list) -> None:
    path = ROOT / f"weeks/week-{week:02d}/interview-questions/01-fundamentals-qa.md"
    existing = path.read_text(encoding="utf-8")
    idx = existing.find("## Q011:")
    if idx == -1:
        raise ValueError(f"Q011 not found in week {week}")
    tail = existing[idx:]
    parts = [PREMIUM_HEADER.format(week=week)]
    for i, item in enumerate(questions, 1):
        parts.append(render_premium_block(i, item))
    path.write_text("".join(parts) + tail, encoding="utf-8")
    print(f"Week {week:02d} fundamentals Q001–Q010 handcrafted")


def splice_week1_advanced() -> None:
    path = ROOT / "weeks/week-01/interview-questions/03-advanced-qa.md"
    header = (
        "# Week 01 — Advanced Interview Q&A (Q071–Q100)\n\n"
        "> Q071–Q100: Premium format (Week 1 quality).\n\n"
        "---\n\n"
    )
    parts = [header]
    for i, item in enumerate(WEEK1_ADVANCED_PREMIUM, 71):
        parts.append(ADVANCED_BLOCK.format(num=i, **item))
    for i, item in enumerate(WEEK1_ADVANCED_Q081_Q100, 81):
        parts.append(ADVANCED_BLOCK.format(num=i, **item))
    path.write_text("".join(parts), encoding="utf-8")
    print("Week 01 advanced Q071–Q100 handcrafted premium")


def _bank_tier(week_banks: dict, tier: str) -> list:
    tier_lower = tier.lower()
    for key, value in week_banks.items():
        if key.lower() == tier_lower:
            return value
    raise KeyError(f"Tier {tier} not found in {list(week_banks.keys())}")


def splice_week_intermediate(week: int, questions: list) -> None:
    path = ROOT / f"weeks/week-{week:02d}/interview-questions/02-intermediate-qa.md"
    header = (
        f"# Week {week:02d} — Intermediate Q&A\n\n"
        "> Q031–Q070: Premium format (Week 1 quality).\n\n"
        "---\n\n"
    )
    parts = [header]
    for i, item in enumerate(questions, 31):
        parts.append(render_premium_block(i, item, difficulty="Intermediate"))
    path.write_text("".join(parts), encoding="utf-8")
    print(f"Week {week:02d} intermediate Q031–Q070 premium")


def splice_week_advanced(week: int, questions: list) -> None:
    path = ROOT / f"weeks/week-{week:02d}/interview-questions/03-advanced-qa.md"
    header = (
        f"# Week {week:02d} — Advanced Q&A\n\n"
        "> Q071–Q100: Premium format (Week 1 quality).\n\n"
        "---\n\n"
    )
    parts = [header]
    for i, item in enumerate(questions, 71):
        parts.append(ADVANCED_BLOCK.format(num=i, **item))
    path.write_text("".join(parts), encoding="utf-8")
    print(f"Week {week:02d} advanced Q071–Q100 premium")


def splice_week_expert(week: int, questions: list) -> None:
    path = ROOT / f"weeks/week-{week:02d}/interview-questions/04-expert-scenarios.md"
    header = (
        f"# Week {week:02d} — Expert Scenario Q&A\n\n"
        "> Q101–Q120: Premium format (Week 1 quality).\n\n"
        "---\n\n"
    )
    parts = [header]
    for i, item in enumerate(questions, 101):
        parts.append(EXPERT_BLOCK.format(num=i, **item))
    path.write_text("".join(parts), encoding="utf-8")
    print(f"Week {week:02d} expert Q101–Q120 premium")


def splice_weeks_41_52_banks() -> None:
    for week, banks in ALL_WEEKS_41_52_BANKS.items():
        splice_week_intermediate(week, _bank_tier(banks, "intermediate"))
        splice_week_advanced(week, _bank_tier(banks, "advanced"))
        splice_week_expert(week, _bank_tier(banks, "expert"))


def splice_week1_expert() -> None:
    path = ROOT / "weeks/week-01/interview-questions/04-expert-scenarios.md"
    header = "# Week 01 — Expert Scenario Interview Q&A (Q101–Q120)\n\n> 20 scenario-based questions — premium format\n\n---\n\n"
    parts = [header]
    for i, item in enumerate(WEEK1_EXPERT, 101):
        parts.append(EXPERT_BLOCK.format(num=i, **item))
    path.write_text("".join(parts), encoding="utf-8")
    print("Week 01 expert Q101–Q120 handcrafted")


def main():
    splice_week2_fundamentals()
    for week, questions in ALL_WEEKS.items():
        splice_fundamentals(week, questions)
    for week, questions in ALL_AZURE_WEEKS.items():
        splice_qa_bank(week, questions)
    for week, questions in ALL_AWS_WEEKS.items():
        splice_aws_fundamentals(week, questions)
    splice_week1_fundamentals_q011_q030()
    for week in (3, 4):
        splice_week3_4_full(
            week,
            ALL_WEEKS_3_4_Q001_Q010[week],
            ALL_WEEKS_3_4_Q011_Q030[week],
        )
    splice_fundamentals_q011_q030(2, WEEK2_Q011_Q030)
    for week, questions in ALL_AWS_Q011_Q030.items():
        splice_fundamentals_q011_q030(week, questions)
    for week, questions in ALL_FUNDAMENTALS_Q011_Q030.items():
        splice_fundamentals_q011_q030(week, questions)
    for week, questions in ALL_WEEKS_25_28.items():
        splice_fundamentals_full(week, questions)
    for week in (37, 38, 39, 40):
        splice_fundamentals_full(
            week,
            ALL_WEEKS_37_40_Q001_Q005[week] + ALL_WEEKS_37_40_Q006_Q030[week],
        )
    for week in range(41, 53):
        splice_fundamentals_full(
            week,
            ALL_WEEKS_41_52_Q001_Q005[week] + ALL_WEEKS_41_52_Q006_Q030[week],
        )
    splice_weeks_41_52_banks()
    splice_week1_intermediate()
    # Azure Q011–Q050 handcrafted tails
    from apply_azure_tails_and_week34 import load_azure_tails, splice_azure_q011_q050
    for week, questions in load_azure_tails().items():
        splice_azure_q011_q050(week, questions)
    splice_week1_advanced()
    splice_week1_expert()
    from apply_weeks_2_36_banks import main as apply_banks_2_36
    apply_banks_2_36()
    print("Done — premium Q&A applied (weeks 1–52 full; Week 1 intermediate + advanced; weeks 2–36 banks)")


if __name__ == "__main__":
    main()
