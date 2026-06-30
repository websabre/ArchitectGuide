#!/usr/bin/env python3
"""Build premium_qa_data_weeks_09_16_banks.py from _banks_data_09_16.py."""

from __future__ import annotations

import os

from _banks_data_09_16 import ALL

OUT = os.path.join(os.path.dirname(__file__), "premium_qa_data_weeks_09_16_banks.py")

HEADER = '''"""Hand-crafted premium interview banks for Weeks 9–16 — Azure Solution Architect track.

Week 09: Azure Fundamentals & WAF
Week 10: Azure Compute & App Services
Week 11: Azure Data Platform
Week 12: Azure Identity
Week 13: Azure Networking
Week 14: Azure Security
Week 15: Azure Integration & Messaging
Week 16: Azure Production Capstone

Exports per week: INTERMEDIATE (40), ADVANCED (30), EXPERT (20) = 90 questions.
Total: 720 questions. Aligns with azure-top-50 and week 01-qa-bank themes.
Uses Intermediate difficulty marker in intermediate tier content.
"""

from premium_qa_data import q

'''

FOOTER = '''
ALL_WEEKS_09_16_BANKS = {
    9: {
        "INTERMEDIATE": WEEK_09_INTERMEDIATE,
        "ADVANCED": WEEK_09_ADVANCED,
        "EXPERT": WEEK_09_EXPERT,
    },
    10: {
        "INTERMEDIATE": WEEK_10_INTERMEDIATE,
        "ADVANCED": WEEK_10_ADVANCED,
        "EXPERT": WEEK_10_EXPERT,
    },
    11: {
        "INTERMEDIATE": WEEK_11_INTERMEDIATE,
        "ADVANCED": WEEK_11_ADVANCED,
        "EXPERT": WEEK_11_EXPERT,
    },
    12: {
        "INTERMEDIATE": WEEK_12_INTERMEDIATE,
        "ADVANCED": WEEK_12_ADVANCED,
        "EXPERT": WEEK_12_EXPERT,
    },
    13: {
        "INTERMEDIATE": WEEK_13_INTERMEDIATE,
        "ADVANCED": WEEK_13_ADVANCED,
        "EXPERT": WEEK_13_EXPERT,
    },
    14: {
        "INTERMEDIATE": WEEK_14_INTERMEDIATE,
        "ADVANCED": WEEK_14_ADVANCED,
        "EXPERT": WEEK_14_EXPERT,
    },
    15: {
        "INTERMEDIATE": WEEK_15_INTERMEDIATE,
        "ADVANCED": WEEK_15_ADVANCED,
        "EXPERT": WEEK_15_EXPERT,
    },
    16: {
        "INTERMEDIATE": WEEK_16_INTERMEDIATE,
        "ADVANCED": WEEK_16_ADVANCED,
        "EXPERT": WEEK_16_EXPERT,
    },
}
'''


def esc(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")


def fmt_q(t: tuple) -> str:
    title, cat, freq, question, short, detailed, perspective, fu1, fu2, m1, m2, m3 = t
    return (
        f'    q("{esc(title)}", "{esc(cat)}", "{esc(freq)}",\n'
        f'      "{esc(question)}",\n'
        f'      "{esc(short)}",\n'
        f'      "{esc(detailed)}",\n'
        f'      "{esc(perspective)}",\n'
        f'      "{esc(fu1)}",\n'
        f'      "{esc(fu2)}",\n'
        f'      "{esc(m1)}",\n'
        f'      "{esc(m2)}",\n'
        f'      "{esc(m3)}"),'
    )


def write_bank(name: str, tuples: list, fh) -> None:
    fh.write(f"\n{name} = [\n")
    for t in tuples:
        fh.write(fmt_q(t) + "\n")
    fh.write("]\n")


def tuples_to_q(tuples: list) -> list:
    return [
        q(title, cat, freq, question, short, detailed, perspective, fu1, fu2, m1, m2, m3)
        for title, cat, freq, question, short, detailed, perspective, fu1, fu2, m1, m2, m3 in tuples
    ]


def main() -> None:
    total = 0
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(HEADER)
        for week in range(9, 17):
            banks = ALL[week]
            assert len(banks["intermediate"]) == 40, week
            assert len(banks["advanced"]) == 30, week
            assert len(banks["expert"]) == 20, week
            write_bank(f"WEEK_{week:02d}_INTERMEDIATE", banks["intermediate"], fh)
            write_bank(f"WEEK_{week:02d}_ADVANCED", banks["advanced"], fh)
            write_bank(f"WEEK_{week:02d}_EXPERT", banks["expert"], fh)
            total += 90
        fh.write(FOOTER)

    # Verify import and counts
    import importlib.util
    spec = importlib.util.spec_from_file_location("banks", OUT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    from premium_qa_data import q as qfn

    grand = 0
    for week, banks in mod.ALL_WEEKS_09_16_BANKS.items():
        for tier, items in banks.items():
            assert len(items) in (20, 30, 40), f"Week {week} {tier}: {len(items)}"
            for item in items:
                assert isinstance(item, dict)
                assert "title" in item and "question" in item
            grand += len(items)
    assert grand == 720, grand

    print(f"Wrote {OUT}")
    print(f"Total questions: {grand}")
    for week in range(9, 17):
        b = mod.ALL_WEEKS_09_16_BANKS[week]
        print(
            f"Week {week:02d}: I={len(b['INTERMEDIATE'])} "
            f"A={len(b['ADVANCED'])} E={len(b['EXPERT'])}"
        )


if __name__ == "__main__":
    main()
