#!/usr/bin/env python3
"""Tiny prompt hygiene checker.

Usage:
  python scripts/prompt_linter.py prompt.md
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED = ["task", "context", "goal", "constraints", "return"]
FILLER = [
    "maybe",
    "whatever",
    "and so on",
    "stuff like that",
    "make it cool",
    "you know",
    "basically basically",
]


def score_prompt(text: str) -> tuple[int, list[str]]:
    lower = text.lower()
    score = 100
    notes: list[str] = []

    for section in REQUIRED:
        if not re.search(rf"(^|\n)\s*{section}\s*:", lower):
            score -= 10
            notes.append(f"Missing section: {section.title()}:")

    words = re.findall(r"\w+", text)
    if len(words) > 400:
        score -= 10
        notes.append("Prompt is long; check for removable context.")

    for phrase in FILLER:
        if phrase in lower:
            score -= 5
            notes.append(f"Possible filler phrase: {phrase!r}")

    if "do not" not in lower and "constraints" not in lower:
        score -= 10
        notes.append("No explicit constraints or non-goals found.")

    return max(score, 0), notes


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2

    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8")
    score, notes = score_prompt(text)

    print(f"Prompt hygiene score: {score}/100")
    if notes:
        print("\nSuggestions:")
        for note in notes:
            print(f"- {note}")
    else:
        print("No obvious issues found.")
    return 0 if score >= 80 else 1


if __name__ == "__main__":
    raise SystemExit(main())
