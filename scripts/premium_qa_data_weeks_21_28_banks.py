"""Hand-crafted premium interview banks for Weeks 21–28.

Week 21: Distributed Systems — CAP, sagas, outbox, consensus, replication, idempotency.
Week 22: Microservices — boundaries, gateway, BFF, resilience, migration, contracts.
Week 23: DDD — bounded context, aggregates, domain events, context maps, CQRS.
Week 24: Microservices Capstone — E2E flows, observability, SLOs, PRR, team topology.
Week 25: Docker & Containers — images, multi-stage builds, security, supply chain.
Week 26: Kubernetes Fundamentals — pods, deployments, services, RBAC, GitOps.
Week 27: Kubernetes Advanced — HPA/KEDA, service mesh, observability, DR, policies.
Week 28: Linux for Architects — systemd, networking, performance, security, triage.

Exports per week: INTERMEDIATE (40), ADVANCED (30), EXPERT (20) = 90 questions.
Total: 720 questions.
"""

from premium_qa_data import q
from premium_qa_data_b import WEEK_21, WEEK_22, WEEK_23, WEEK_24
from premium_qa_data_tails_w21_22 import WEEK_21_Q011_Q030, WEEK_22_Q011_Q030
from premium_qa_data_tails_w23_24 import WEEK_23_Q011_Q030, WEEK_24_Q011_Q030
from premium_qa_data_weeks_25_28 import WEEK_25, WEEK_26, WEEK_27, WEEK_28
from _banks_data_21_28_extra import (
    W21_I_EXTRA,
    W21_ADVANCED,
    W21_EXPERT,
    W22_I_EXTRA,
    W22_ADVANCED,
    W22_EXPERT,
    W23_I_EXTRA,
    W23_ADVANCED,
    W23_EXPERT,
    W24_I_EXTRA,
    W24_ADVANCED,
    W24_EXPERT,
    W25_I_EXTRA,
    W25_ADVANCED,
    W25_EXPERT,
    W26_I_EXTRA,
    W26_ADVANCED,
    W26_EXPERT,
    W27_I_EXTRA,
    W27_ADVANCED,
    W27_EXPERT,
    W28_I_EXTRA,
    W28_ADVANCED,
    W28_EXPERT,
)

WEEK_21_INTERMEDIATE = WEEK_21 + WEEK_21_Q011_Q030 + W21_I_EXTRA
WEEK_21_ADVANCED = W21_ADVANCED
WEEK_21_EXPERT = W21_EXPERT

WEEK_22_INTERMEDIATE = WEEK_22 + WEEK_22_Q011_Q030 + W22_I_EXTRA
WEEK_22_ADVANCED = W22_ADVANCED
WEEK_22_EXPERT = W22_EXPERT

WEEK_23_INTERMEDIATE = WEEK_23 + WEEK_23_Q011_Q030 + W23_I_EXTRA
WEEK_23_ADVANCED = W23_ADVANCED
WEEK_23_EXPERT = W23_EXPERT

WEEK_24_INTERMEDIATE = WEEK_24 + WEEK_24_Q011_Q030 + W24_I_EXTRA
WEEK_24_ADVANCED = W24_ADVANCED
WEEK_24_EXPERT = W24_EXPERT

WEEK_25_INTERMEDIATE = WEEK_25 + W25_I_EXTRA
WEEK_25_ADVANCED = W25_ADVANCED
WEEK_25_EXPERT = W25_EXPERT

WEEK_26_INTERMEDIATE = WEEK_26 + W26_I_EXTRA
WEEK_26_ADVANCED = W26_ADVANCED
WEEK_26_EXPERT = W26_EXPERT

WEEK_27_INTERMEDIATE = WEEK_27 + W27_I_EXTRA
WEEK_27_ADVANCED = W27_ADVANCED
WEEK_27_EXPERT = W27_EXPERT

WEEK_28_INTERMEDIATE = WEEK_28 + W28_I_EXTRA
WEEK_28_ADVANCED = W28_ADVANCED
WEEK_28_EXPERT = W28_EXPERT

ALL_WEEKS_21_28_BANKS = {
    21: {
        "intermediate": WEEK_21_INTERMEDIATE,
        "advanced": WEEK_21_ADVANCED,
        "expert": WEEK_21_EXPERT,
    },
    22: {
        "intermediate": WEEK_22_INTERMEDIATE,
        "advanced": WEEK_22_ADVANCED,
        "expert": WEEK_22_EXPERT,
    },
    23: {
        "intermediate": WEEK_23_INTERMEDIATE,
        "advanced": WEEK_23_ADVANCED,
        "expert": WEEK_23_EXPERT,
    },
    24: {
        "intermediate": WEEK_24_INTERMEDIATE,
        "advanced": WEEK_24_ADVANCED,
        "expert": WEEK_24_EXPERT,
    },
    25: {
        "intermediate": WEEK_25_INTERMEDIATE,
        "advanced": WEEK_25_ADVANCED,
        "expert": WEEK_25_EXPERT,
    },
    26: {
        "intermediate": WEEK_26_INTERMEDIATE,
        "advanced": WEEK_26_ADVANCED,
        "expert": WEEK_26_EXPERT,
    },
    27: {
        "intermediate": WEEK_27_INTERMEDIATE,
        "advanced": WEEK_27_ADVANCED,
        "expert": WEEK_27_EXPERT,
    },
    28: {
        "intermediate": WEEK_28_INTERMEDIATE,
        "advanced": WEEK_28_ADVANCED,
        "expert": WEEK_28_EXPERT,
    },
}

for _week, _banks in ALL_WEEKS_21_28_BANKS.items():
    assert len(_banks["intermediate"]) == 40, f"Week {_week} intermediate: {len(_banks['intermediate'])}"
    assert len(_banks["advanced"]) == 30, f"Week {_week} advanced: {len(_banks['advanced'])}"
    assert len(_banks["expert"]) == 20, f"Week {_week} expert: {len(_banks['expert'])}"

_total = sum(
    len(_banks[t])
    for _banks in ALL_WEEKS_21_28_BANKS.values()
    for t in ("intermediate", "advanced", "expert")
)
assert _total == 720, _total
