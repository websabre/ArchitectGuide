#!/usr/bin/env python3
"""Generate interview-prep Top 50 Part 2 and Part 3 markdown from premium data."""

from pathlib import Path

from premium_interview_prep_microservices import (
    MICROSERVICES_PART2_Q009_Q030,
    MICROSERVICES_PART3_Q031_Q050,
)
from premium_interview_prep_system_design import (
    SYSTEM_DESIGN_PART2_Q009_Q030,
    SYSTEM_DESIGN_PART3_Q031_Q050,
)

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "interview-prep"

# --- System Design (Frequency + Architecture Perspective) ---

SD_QA_BLOCK = """
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

{followups}

### Common Mistakes in Interviews

{mistakes}

---
"""

SD_PART2_HEADER = """# System Design Top 50 — Part 2 (Q009–Q030)

> [Part 1](system-design-top-50-qa-part1.md) | [Part 3](system-design-top-50-qa-part3.md) | [Index](system-design-top-50-index.md)

---

"""

SD_PART3_HEADER = """# System Design Top 50 — Part 3 (Q031–Q050)

> [Part 1](system-design-top-50-qa-part1.md) | [Part 2](system-design-top-50-qa-part2.md) | [Index](system-design-top-50-index.md)

---

"""

SD_DIFFICULTY_BY_NUM = {
    range(9, 16): "Intermediate",
    range(16, 24): "Advanced",
    range(24, 31): "Advanced",
    range(31, 41): "Advanced",
    range(41, 51): "Expert",
}


def sd_difficulty_for(num: int) -> str:
    for r, label in SD_DIFFICULTY_BY_NUM.items():
        if num in r:
            return label
    return "Advanced"


# --- Microservices (Week field, matches part 1 Q001 format) ---

MS_QA_BLOCK = """
## Q{num:03d}: {title}

| Attribute | Value |
|-----------|-------|
| **Difficulty** | {difficulty} |
| **Category** | {category} |
| **Week** | {week} |

### Question

{question}

### Short Answer (30 seconds)

{short}

### Detailed Answer (3–5 minutes)

{detailed}

### Follow-up Questions

{followups}

### Common Mistakes

{mistakes}

---
"""

MS_PART2_HEADER = """# Microservices Top 50 — Part 2 (Q009–Q030)

> **Resilience, Data, DDD, API Gateway** | Weeks 21–24 | [Part 1](microservices-top-50-qa-part1.md) | [Part 3](microservices-top-50-qa-part3.md) | [Index](microservices-top-50-index.md)

---

"""

MS_PART3_HEADER = """# Microservices Top 50 — Part 3 (Q031–Q050)

> **Sagas, Migration, Scenarios, Capstone** | Weeks 21–24 | [Part 1](microservices-top-50-qa-part1.md) | [Part 2](microservices-top-50-qa-part2.md) | [Index](microservices-top-50-index.md)

---

"""


def write_system_design() -> tuple[int, int]:
    def render_block(num: int, item: dict) -> str:
        return SD_QA_BLOCK.format(num=num, difficulty=sd_difficulty_for(num), **item)

    def write_part(path: Path, header: str, questions: list, start_num: int, footer: str) -> int:
        parts = [header]
        for i, item in enumerate(questions):
            parts.append(render_block(start_num + i, item))
        parts.append(footer)
        path.write_text("".join(parts), encoding="utf-8")
        return len(questions)

    n2 = write_part(
        OUT_DIR / "system-design-top-50-qa-part2.md",
        SD_PART2_HEADER,
        SYSTEM_DESIGN_PART2_Q009_Q030,
        9,
        "\n**Next:** [Part 3](system-design-top-50-qa-part3.md) →\n",
    )
    n3 = write_part(
        OUT_DIR / "system-design-top-50-qa-part3.md",
        SD_PART3_HEADER,
        SYSTEM_DESIGN_PART3_Q031_Q050,
        31,
        "\n**Complete:** [Index](system-design-top-50-index.md) | [Mock interviews](mock-interviews/README.md)\n",
    )
    return n2, n3


def write_microservices() -> tuple[int, int]:
    def render_block(num: int, item: dict) -> str:
        return MS_QA_BLOCK.format(num=num, **item)

    def write_part(path: Path, header: str, questions: list, start_num: int, footer: str) -> int:
        parts = [header]
        for i, item in enumerate(questions):
            parts.append(render_block(start_num + i, item))
        parts.append(footer)
        path.write_text("".join(parts), encoding="utf-8")
        return len(questions)

    n2 = write_part(
        OUT_DIR / "microservices-top-50-qa-part2.md",
        MS_PART2_HEADER,
        MICROSERVICES_PART2_Q009_Q030,
        9,
        "\n**Next:** [Part 3](microservices-top-50-qa-part3.md) →\n",
    )
    n3 = write_part(
        OUT_DIR / "microservices-top-50-qa-part3.md",
        MS_PART3_HEADER,
        MICROSERVICES_PART3_Q031_Q050,
        31,
        "\n**Complete:** [Index](microservices-top-50-index.md)\n",
    )
    return n2, n3


def main() -> None:
    sd_n2, sd_n3 = write_system_design()
    ms_n2, ms_n3 = write_microservices()

    print("System Design:")
    print(f"  Wrote {sd_n2} questions → system-design-top-50-qa-part2.md")
    print(f"  Wrote {sd_n3} questions → system-design-top-50-qa-part3.md")
    print(f"  Total: {sd_n2 + sd_n3} questions")

    print("Microservices:")
    print(f"  Wrote {ms_n2} questions → microservices-top-50-qa-part2.md")
    print(f"  Wrote {ms_n3} questions → microservices-top-50-qa-part3.md")
    print(f"  Total: {ms_n2 + ms_n3} questions")

    assert ms_n2 == 22, f"Expected 22 microservices part-2 questions, got {ms_n2}"
    assert ms_n3 == 20, f"Expected 20 microservices part-3 questions, got {ms_n3}"
    assert ms_n2 + ms_n3 == 42, f"Expected 42 microservices questions total, got {ms_n2 + ms_n3}"


if __name__ == "__main__":
    main()
