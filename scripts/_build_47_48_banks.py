#!/usr/bin/env python3
"""Build premium_qa_data_weeks_47_48_banks.py from Q001–Q030 + extra banks."""

from __future__ import annotations

import os

from premium_qa_data_weeks_45_48_q001_q005 import WEEK_47_Q001_Q005, WEEK_48_Q001_Q005
from premium_qa_data_weeks_45_48_q006_q030 import WEEK_47_Q006_Q030, WEEK_48_Q006_Q030
from _banks_data_47_48_extra import (
    W47_ADV,
    W47_EXP,
    W47_EXTRA_I,
    W48_ADV,
    W48_EXP,
    W48_EXTRA_I,
)

OUT = os.path.join(os.path.dirname(__file__), "premium_qa_data_weeks_47_48_banks.py")


def esc(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")


def fmt_dict(d: dict) -> str:
    fu = d["followups"]
    fu1 = fu.split("\n")[0].replace("1. **", "").rstrip("*")
    fu2 = fu.split("2. **")[1].rstrip("*") if "2. **" in fu else ""
    ms = [x.lstrip("- ") for x in d["mistakes"].split("\n") if x.strip()]
    while len(ms) < 3:
        ms.append("")
    return (
        f'    q("{esc(d["title"])}", "{esc(d["category"])}", "{esc(d["frequency"])}",\n'
        f'      "{esc(d["question"])}",\n'
        f'      "{esc(d["short"])}",\n'
        f'      "{esc(d["detailed"])}",\n'
        f'      "{esc(d["perspective"])}",\n'
        f'      "{esc(fu1)}",\n'
        f'      "{esc(fu2)}",\n'
        f'      "{esc(ms[0])}",\n'
        f'      "{esc(ms[1])}",\n'
        f'      "{esc(ms[2])}"),'
    )


def fmt_tuple(t: tuple) -> str:
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


def write_bank(name: str, items, fh) -> None:
    fh.write(f"\n{name} = [\n")
    for item in items:
        fmt = fmt_dict if isinstance(item, dict) else fmt_tuple
        fh.write(fmt(item) + "\n")
    fh.write("]\n")


HEADER = '''"""Hand-crafted premium interview banks for Weeks 47–48 — System Design & Whiteboard Mocks.

Week 47: Interview System Design — RESHADED, requirements, scale estimation, API design,
caching, load balancing, CDN, queues, microservices, saga, circuit breaker, rate limiting,
notifications, URL shortener, news feed, chat, search, distributed cache, snowflake IDs,
consistency, hot keys.

Week 48: Whiteboard Mock 1 — notification mock, cart mock, queue mock, API pagination,
rate limit mock, auth mock, logging mock, metrics mock, deployment mock, multi-tenant mock,
read replica, CQRS mock, idempotency, schema evolution, webhook mock, batch processing,
stream processing, time management.

Exports per week: INTERMEDIATE (40), ADVANCED (30), EXPERT (20) = 90 questions.
Total: 180 questions.
"""

from premium_qa_data import q
'''

FOOTER = '''
ALL_WEEKS_47_48_BANKS = {
    47: {
        "intermediate": WEEK_47_INTERMEDIATE,
        "advanced": WEEK_47_ADVANCED,
        "expert": WEEK_47_EXPERT,
    },
    48: {
        "intermediate": WEEK_48_INTERMEDIATE,
        "advanced": WEEK_48_ADVANCED,
        "expert": WEEK_48_EXPERT,
    },
}
'''


def main() -> None:
    w47_intermediate = list(WEEK_47_Q001_Q005) + list(WEEK_47_Q006_Q030) + list(W47_EXTRA_I)
    w48_intermediate = list(WEEK_48_Q001_Q005) + list(WEEK_48_Q006_Q030) + list(W48_EXTRA_I)

    assert len(w47_intermediate) == 40, len(w47_intermediate)
    assert len(W47_ADV) == 30, len(W47_ADV)
    assert len(W47_EXP) == 20, len(W47_EXP)
    assert len(w48_intermediate) == 40, len(w48_intermediate)
    assert len(W48_ADV) == 30, len(W48_ADV)
    assert len(W48_EXP) == 20, len(W48_EXP)

    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(HEADER)
        write_bank("WEEK_47_INTERMEDIATE", w47_intermediate, fh)
        write_bank("WEEK_47_ADVANCED", W47_ADV, fh)
        write_bank("WEEK_47_EXPERT", W47_EXP, fh)
        write_bank("WEEK_48_INTERMEDIATE", w48_intermediate, fh)
        write_bank("WEEK_48_ADVANCED", W48_ADV, fh)
        write_bank("WEEK_48_EXPERT", W48_EXP, fh)
        fh.write(FOOTER)

    total = len(w47_intermediate) + len(W47_ADV) + len(W47_EXP)
    total += len(w48_intermediate) + len(W48_ADV) + len(W48_EXP)
    print(f"Wrote {OUT} — {total} questions total")


if __name__ == "__main__":
    main()
