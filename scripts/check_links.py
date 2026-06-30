#!/usr/bin/env python3
"""Validate internal markdown links in the ArchitectGuide repo."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
SKIP_SCHEMES = ("http://", "https://", "mailto:", "#")


def is_skipped(target: str) -> bool:
    return any(target.startswith(s) for s in SKIP_SCHEMES)


def resolve_link(source: Path, target: str) -> Path | None:
    target = unquote(target.split("#", 1)[0].strip())
    if not target or is_skipped(target):
        return None
    if target.startswith("/"):
        resolved = ROOT / target.lstrip("/")
    else:
        resolved = (source.parent / target).resolve()
    return resolved


def collect_md_files() -> list[Path]:
    skip_dirs = {".git", "node_modules", ".venv", "site", "templates"}
    files = []
    for path in ROOT.rglob("*.md"):
        if any(part in skip_dirs for part in path.parts):
            continue
        files.append(path)
    return sorted(files)


def check_links() -> list[tuple[Path, str, Path]]:
    broken: list[tuple[Path, str, Path]] = []
    for md_file in collect_md_files():
        try:
            text = md_file.read_text(encoding="utf-8")
        except OSError:
            continue
        for _label, raw_target in LINK_RE.findall(text):
            resolved = resolve_link(md_file, raw_target)
            if resolved is None:
                continue
            if not resolved.exists():
                broken.append((md_file, raw_target, resolved))
    return broken


def main() -> int:
    broken = check_links()
    if not broken:
        print(f"OK — 0 broken internal links ({len(collect_md_files())} markdown files scanned)")
        return 0
    print(f"BROKEN — {len(broken)} link(s):\n")
    for source, target, resolved in broken:
        rel_src = source.relative_to(ROOT)
        print(f"  {rel_src}")
        print(f"    [{target}] -> {resolved.relative_to(ROOT) if resolved.is_relative_to(ROOT) else resolved}")
        print()
    return 1


if __name__ == "__main__":
    sys.exit(main())
