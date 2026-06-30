"""Parse premium Q&A blocks from week fundamentals markdown files."""

from __future__ import annotations

import re
from pathlib import Path

from premium_qa_data import q

ROOT = Path(__file__).resolve().parents[1]


def _parse_block(block: str) -> dict:
    def _field(name: str) -> str:
        pat = rf"### {re.escape(name)}\n\n(.*?)(?=\n### |\Z)"
        fm = re.search(pat, block, re.DOTALL)
        return fm.group(1).strip() if fm else ""

    def _table(field: str) -> str:
        pat = rf"\*\*{re.escape(field)}\*\* \| (.+?)(?:\s*\|)?\s*$"
        tm = re.search(pat, block, re.MULTILINE)
        return tm.group(1).strip() if tm else ""

    title_m = re.search(r"## Q\d+: (.+)", block)
    title = title_m.group(1).strip() if title_m else "Untitled"

    category = _table("Category") or "General"
    frequency = _table("Frequency") or "Common"
    question = _field("Question")
    short = _field("Short Answer (30 seconds)")
    detailed = _field("Detailed Answer (3–5 minutes)") or _field("Detailed Answer")
    perspective = _field("Architecture Perspective")

    fu_block = _field("Follow-up Questions")
    fu_lines = [ln.strip() for ln in fu_block.split("\n") if ln.strip()]
    fu1 = re.sub(r"^\d+\.\s*\*\*|\*\*$", "", fu_lines[0]) if fu_lines else ""
    fu2 = re.sub(r"^\d+\.\s*\*\*|\*\*$", "", fu_lines[1]) if len(fu_lines) > 1 else ""

    ms_block = _field("Common Mistakes in Interviews")
    mistakes = [ln.strip().lstrip("- ") for ln in ms_block.split("\n") if ln.strip().startswith("-")]
    while len(mistakes) < 3:
        mistakes.append("No concrete production example given")

    return q(
        title, category, frequency, question, short, detailed, perspective,
        fu1, fu2, mistakes[0], mistakes[1], mistakes[2],
    )


def parse_fundamentals_md_ordered(week: int, start: int = 1, end: int = 10) -> list[dict]:
    path = ROOT / f"weeks/week-{week:02d}/interview-questions/01-fundamentals-qa.md"
    text = path.read_text(encoding="utf-8")
    pattern = r"## Q(\d+): .+?\n\n\| Attribute \| Value \|.*?(?=\n---|\Z)"
    results: list[tuple[int, dict]] = []
    for m in re.finditer(pattern, text, re.DOTALL):
        num = int(re.search(r"## Q(\d+):", m.group(0)).group(1))  # type: ignore
        if num < start or num > end:
            continue
        results.append((num, _parse_block(m.group(0))))
    results.sort(key=lambda x: x[0])
    return [item for _, item in results]
