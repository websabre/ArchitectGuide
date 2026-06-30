"""Hand-crafted premium interview banks for Weeks 49–50 — Whiteboard Mock 2 and Leadership.

Week 49 Whiteboard Mock 2: multi-tenant SaaS, acquisition integration, migration strategy,
risk register, executive comms, stakeholder map, build vs buy, technical debt presentation,
architecture roadmap, vendor evaluation, SLA negotiation, team topology, Conway's law,
platform pitch, cost-benefit, compliance gap, DR presentation, scale 10x, data mesh,
board presentation.

Week 50 Leadership & Behavioral: stakeholder management, managing up, conflict resolution,
influencing without authority, executive communication, prioritization, saying no,
technical vision, consensus building, cross-functional leadership, mentoring, feedback,
difficult conversations, psychological safety, incident leadership, budget justification,
hiring, delegation, remote leadership, negotiation.
"""

from premium_qa_data import q
from premium_qa_data_weeks_49_52_q001_q005 import WEEK_49_Q001_Q005, WEEK_50_Q001_Q005
from premium_qa_data_weeks_49_52_q006_q030 import WEEK_49_Q006_Q030, WEEK_50_Q006_Q030
from _banks_data_49_50_extra import (
    W49_ADVANCED,
    W49_EXPERT,
    W49_I_EXTRA,
    W50_ADVANCED,
    W50_EXPERT,
    W50_I_EXTRA,
)

WEEK_49_INTERMEDIATE = WEEK_49_Q001_Q005 + WEEK_49_Q006_Q030[:20] + W49_I_EXTRA
WEEK_49_ADVANCED = WEEK_49_Q006_Q030[20:] + W49_ADVANCED
WEEK_49_EXPERT = W49_EXPERT

WEEK_50_INTERMEDIATE = WEEK_50_Q001_Q005 + WEEK_50_Q006_Q030[:20] + W50_I_EXTRA
WEEK_50_ADVANCED = WEEK_50_Q006_Q030[20:] + W50_ADVANCED
WEEK_50_EXPERT = W50_EXPERT

ALL_WEEKS_49_50_BANKS = {
    49: {
        "INTERMEDIATE": WEEK_49_INTERMEDIATE,
        "ADVANCED": WEEK_49_ADVANCED,
        "EXPERT": WEEK_49_EXPERT,
    },
    50: {
        "INTERMEDIATE": WEEK_50_INTERMEDIATE,
        "ADVANCED": WEEK_50_ADVANCED,
        "EXPERT": WEEK_50_EXPERT,
    },
}
