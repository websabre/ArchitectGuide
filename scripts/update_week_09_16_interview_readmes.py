#!/usr/bin/env python3
"""Update weeks 9-16 interview READMEs to list new bank files."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TOPICS = {
    9: "Azure Fundamentals & WAF",
    10: "Azure Compute & App Services",
    11: "Azure Data Platform",
    12: "Azure Identity",
    13: "Azure Networking",
    14: "Azure Security",
    15: "Azure Integration & Messaging",
    16: "Azure Production Capstone",
}

TEMPLATE = """# Week {week:02d} — Interview Questions

> [← Week {week:02d} overview](../README.md)

| File | Count | Difficulty |
|------|-------|------------|
| [01-qa-bank.md](01-qa-bank.md) | 50 | Intermediate (Q001–Q050 premium) |
| [02-intermediate-qa.md](02-intermediate-qa.md) | 40 | Intermediate (Q031–Q070 premium) |
| [03-advanced-qa.md](03-advanced-qa.md) | 30 | Advanced (Q071–Q100 premium) |
| [04-expert-scenarios.md](04-expert-scenarios.md) | 20 | Expert (Q101–Q120 premium) |

**Start here:** [01-qa-bank.md](01-qa-bank.md) — {topic}

---

[← Back to Week {week:02d}](../README.md)
"""


def main() -> None:
    for week, topic in TOPICS.items():
        path = ROOT / f"weeks/week-{week:02d}/interview-questions/README.md"
        path.write_text(TEMPLATE.format(week=week, topic=topic), encoding="utf-8")
        print(f"Updated {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
