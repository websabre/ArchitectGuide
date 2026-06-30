#!/usr/bin/env python3
"""Build premium_qa_data_weeks_29_36_banks.py from Q001–Q030 + extra banks."""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from premium_qa_data import q
from premium_qa_data_b import WEEK_33, WEEK_34, WEEK_35, WEEK_36
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
from _parse_premium_md_q import parse_fundamentals_md_ordered
from _banks_data_29_36_extra import (
    W29_EXTRA_I, W29_ADVANCED, W29_EXPERT,
    W30_EXTRA_I, W30_ADVANCED, W30_EXPERT,
    W31_EXTRA_I, W31_ADVANCED, W31_EXPERT,
    W32_EXTRA_I, W32_ADVANCED, W32_EXPERT,
    W33_EXTRA_I, W33_ADVANCED, W33_EXPERT,
    W34_EXTRA_I, W34_ADVANCED, W34_EXPERT,
    W35_EXTRA_I, W35_ADVANCED, W35_EXPERT,
    W36_EXTRA_I, W36_ADVANCED, W36_EXPERT,
)

OUT = os.path.join(os.path.dirname(__file__), "premium_qa_data_weeks_29_36_banks.py")


def _qs(rows):
    return [q(*r) for r in rows]


def _base_29_32(week: int, tail: list) -> list:
    return parse_fundamentals_md_ordered(week, 1, 10) + tail


def _base_33_36(fundamentals: list, tail: list) -> list:
    return fundamentals + tail


WEEK_29_BASE = _base_29_32(29, WEEK_29_Q011_Q030)
WEEK_30_BASE = _base_29_32(30, WEEK_30_Q011_Q030)
WEEK_31_BASE = _base_29_32(31, WEEK_31_Q011_Q030)
WEEK_32_BASE = _base_29_32(32, WEEK_32_Q011_Q030)
WEEK_33_BASE = _base_33_36(WEEK_33, WEEK_33_Q011_Q030)
WEEK_34_BASE = _base_33_36(WEEK_34, WEEK_34_Q011_Q030)
WEEK_35_BASE = _base_33_36(WEEK_35, WEEK_35_Q011_Q030)
WEEK_36_BASE = _base_33_36(WEEK_36, WEEK_36_Q011_Q030)

WEEK_29_INTERMEDIATE = WEEK_29_BASE + _qs(W29_EXTRA_I)
WEEK_29_ADVANCED = _qs(W29_ADVANCED)
WEEK_29_EXPERT = _qs(W29_EXPERT)

WEEK_30_INTERMEDIATE = WEEK_30_BASE + _qs(W30_EXTRA_I)
WEEK_30_ADVANCED = _qs(W30_ADVANCED)
WEEK_30_EXPERT = _qs(W30_EXPERT)

WEEK_31_INTERMEDIATE = WEEK_31_BASE + _qs(W31_EXTRA_I)
WEEK_31_ADVANCED = _qs(W31_ADVANCED)
WEEK_31_EXPERT = _qs(W31_EXPERT)

WEEK_32_INTERMEDIATE = WEEK_32_BASE + _qs(W32_EXTRA_I)
WEEK_32_ADVANCED = _qs(W32_ADVANCED)
WEEK_32_EXPERT = _qs(W32_EXPERT)

WEEK_33_INTERMEDIATE = WEEK_33_BASE + _qs(W33_EXTRA_I)
WEEK_33_ADVANCED = _qs(W33_ADVANCED)
WEEK_33_EXPERT = _qs(W33_EXPERT)

WEEK_34_INTERMEDIATE = WEEK_34_BASE + _qs(W34_EXTRA_I)
WEEK_34_ADVANCED = _qs(W34_ADVANCED)
WEEK_34_EXPERT = _qs(W34_EXPERT)

WEEK_35_INTERMEDIATE = WEEK_35_BASE + _qs(W35_EXTRA_I)
WEEK_35_ADVANCED = _qs(W35_ADVANCED)
WEEK_35_EXPERT = _qs(W35_EXPERT)

WEEK_36_INTERMEDIATE = WEEK_36_BASE + _qs(W36_EXTRA_I)
WEEK_36_ADVANCED = _qs(W36_ADVANCED)
WEEK_36_EXPERT = _qs(W36_EXPERT)

ALL_WEEKS_29_36_BANKS = {
    29: {
        "INTERMEDIATE": WEEK_29_INTERMEDIATE,
        "ADVANCED": WEEK_29_ADVANCED,
        "EXPERT": WEEK_29_EXPERT,
    },
    30: {
        "INTERMEDIATE": WEEK_30_INTERMEDIATE,
        "ADVANCED": WEEK_30_ADVANCED,
        "EXPERT": WEEK_30_EXPERT,
    },
    31: {
        "INTERMEDIATE": WEEK_31_INTERMEDIATE,
        "ADVANCED": WEEK_31_ADVANCED,
        "EXPERT": WEEK_31_EXPERT,
    },
    32: {
        "INTERMEDIATE": WEEK_32_INTERMEDIATE,
        "ADVANCED": WEEK_32_ADVANCED,
        "EXPERT": WEEK_32_EXPERT,
    },
    33: {
        "INTERMEDIATE": WEEK_33_INTERMEDIATE,
        "ADVANCED": WEEK_33_ADVANCED,
        "EXPERT": WEEK_33_EXPERT,
    },
    34: {
        "INTERMEDIATE": WEEK_34_INTERMEDIATE,
        "ADVANCED": WEEK_34_ADVANCED,
        "EXPERT": WEEK_34_EXPERT,
    },
    35: {
        "INTERMEDIATE": WEEK_35_INTERMEDIATE,
        "ADVANCED": WEEK_35_ADVANCED,
        "EXPERT": WEEK_35_EXPERT,
    },
    36: {
        "INTERMEDIATE": WEEK_36_INTERMEDIATE,
        "ADVANCED": WEEK_36_ADVANCED,
        "EXPERT": WEEK_36_EXPERT,
    },
}

HEADER = '''"""Hand-crafted premium interview banks for Weeks 29–36 — DevOps through System Design Capstone.

Week 29: DevOps Culture & DORA — CALMS, DORA metrics, Team Topologies, SRE, platform engineering,
value stream mapping, Westrum culture, error budgets, blameless postmortems, DevSecOps, Conway's Law.

Week 30: CI/CD Pipelines — GitHub Actions, Azure DevOps, blue-green, canary, OIDC, database migrations,
SAST, Pact contract testing, rollback, SBOM, SLSA, immutable artifacts, pipeline as code.

Week 31: Infrastructure as Code — Bicep, Terraform, ARM, drift detection, GitOps for infra, modules,
state management, policy as code, landing zones, module composition.

Week 32: Observability — OpenTelemetry, metrics, logs, traces, SLI/SLO, dashboards, alerting,
App Insights, cardinality control, sampling, production debugging workflows.

Week 33: System Design Methodology — RESHADED, estimation, requirements clarification, API design,
failure mode analysis, scope management, whiteboard communication, design evolution.

Week 34: Scalability & Caching — cache-aside, CDN, database sharding, read replicas, load balancing,
hot keys, cache stampede, multi-tier caching, consistency trade-offs.

Week 35: Messaging & Events — Kafka, Azure Service Bus, event-driven architecture, saga pattern,
transactional outbox, idempotency, message ordering, dead letter queues.

Week 36: System Design Capstone — checkout, e-commerce, ride-sharing, notification systems, search,
distributed ID generation, multi-region design, full end-to-end system design scenarios.

Exports per week: INTERMEDIATE (40), ADVANCED (30), EXPERT (20) = 90 questions.
Total: 720 questions.
"""

from premium_qa_data import q

'''


def esc(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")


def fmt_dict(d: dict) -> str:
    fu = d["followups"]
    fu1 = fu.split("\n")[0].replace("1. **", "").rstrip("*") if fu else ""
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


def write_bank(name: str, items: list, fh) -> None:
    fh.write(f"\n{name} = [\n")
    for item in items:
        fh.write(fmt_dict(item) + "\n")
    fh.write("]\n")


def main() -> None:
    for week in range(29, 37):
        banks = ALL_WEEKS_29_36_BANKS[week]
        assert len(banks["INTERMEDIATE"]) == 40, f"Week {week} INTERMEDIATE={len(banks['INTERMEDIATE'])}"
        assert len(banks["ADVANCED"]) == 30, f"Week {week} ADVANCED={len(banks['ADVANCED'])}"
        assert len(banks["EXPERT"]) == 20, f"Week {week} EXPERT={len(banks['EXPERT'])}"

    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(HEADER)
        for week in range(29, 37):
            write_bank(f"WEEK_{week}_INTERMEDIATE", ALL_WEEKS_29_36_BANKS[week]["INTERMEDIATE"], fh)
            write_bank(f"WEEK_{week}_ADVANCED", ALL_WEEKS_29_36_BANKS[week]["ADVANCED"], fh)
            write_bank(f"WEEK_{week}_EXPERT", ALL_WEEKS_29_36_BANKS[week]["EXPERT"], fh)
        fh.write(
            "\nALL_WEEKS_29_36_BANKS = {\n"
            + ",\n".join(
                f"    {w}: {{\n"
                f'        "INTERMEDIATE": WEEK_{w}_INTERMEDIATE,\n'
                f'        "ADVANCED": WEEK_{w}_ADVANCED,\n'
                f'        "EXPERT": WEEK_{w}_EXPERT,\n'
                f"    }}"
                for w in range(29, 37)
            )
            + ",\n}\n"
        )

    total = sum(
        len(ALL_WEEKS_29_36_BANKS[w][t])
        for w in range(29, 37)
        for t in ("INTERMEDIATE", "ADVANCED", "EXPERT")
    )
    print(f"Wrote {OUT}")
    for week in range(29, 37):
        b = ALL_WEEKS_29_36_BANKS[week]
        print(
            f"Week {week}: I={len(b['INTERMEDIATE'])} "
            f"A={len(b['ADVANCED'])} E={len(b['EXPERT'])}"
        )
    print(f"Total: {total}")


if __name__ == "__main__":
    main()
