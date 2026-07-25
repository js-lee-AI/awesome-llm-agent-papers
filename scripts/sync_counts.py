#!/usr/bin/env python3
"""Keep the per-section paper counts in README.md in sync with reality.

Every section states its count in three places: the Contents list, the section
heading, and the "Show N papers" toggle. Editing a section by hand means
updating all three, and that has drifted before. This recomputes all three from
the actual number of entries.

An entry is a top-level list item of the form:

    - **[Title](link)** (Author et al., Venue Year) - *why it matters.*

Usage:
    python3 scripts/sync_counts.py            # rewrite README.md in place
    python3 scripts/sync_counts.py --check    # report drift, exit 1, write nothing

--check is what CI and the pre-commit hook run.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

README = Path(__file__).resolve().parent.parent / "README.md"

ANCHOR_RE = re.compile(r'^<a id="([^"]+)"></a>\s*$')
HEADING_RE = re.compile(r"^(### .*?)\((\d+)\)\s*$")
SUMMARY_RE = re.compile(r"^(<summary><b>Show )(\d+)( papers</b></summary>)\s*$")
ENTRY_RE = re.compile(r"^- \*\*\[")
TOC_RE = re.compile(r"^(\s*- \[.*?)\((\d+)\)(\]\(#([\w-]+)\))\s*$")


def scan(lines: list[str]) -> dict[str, dict]:
    """Map anchor slug -> {actual, heading_idx, summary_idx, declared, title}."""
    sections: dict[str, dict] = {}
    slug = None
    current = None
    for i, line in enumerate(lines):
        anchor = ANCHOR_RE.match(line)
        if anchor:
            slug = anchor.group(1)
            continue

        heading = HEADING_RE.match(line)
        if heading and slug:
            current = {
                "slug": slug,
                "prefix": heading.group(1),  # keeps the space before "(N)"
                "title": heading.group(1).strip(),
                "declared": int(heading.group(2)),
                "heading_idx": i,
                "summary_idx": None,
                "summary_declared": None,
                "actual": 0,
            }
            sections[slug] = current
            slug = None
            continue

        if current is None:
            continue

        if line.startswith("## ") or line.startswith("<a id="):
            current = None
            if line.startswith("<a id="):
                slug = ANCHOR_RE.match(line).group(1)
            continue

        summary = SUMMARY_RE.match(line)
        if summary:
            current["summary_idx"] = i
            current["summary_declared"] = int(summary.group(2))
        elif ENTRY_RE.match(line):
            current["actual"] += 1

    return sections


def apply(lines: list[str], sections: dict[str, dict]) -> tuple[list[str], list[str]]:
    out = list(lines)
    drift: list[str] = []

    for sec in sections.values():
        n = sec["actual"]
        if sec["declared"] != n:
            drift.append(f'heading  {sec["title"]}: {sec["declared"]} -> {n}')
            out[sec["heading_idx"]] = f'{sec["prefix"]}({n})'
        if sec["summary_idx"] is not None and sec["summary_declared"] != n:
            drift.append(
                f'summary  {sec["title"]}: {sec["summary_declared"]} -> {n}'
            )
            out[sec["summary_idx"]] = f"<summary><b>Show {n} papers</b></summary>"

    for i, line in enumerate(out):
        toc = TOC_RE.match(line)
        if not toc:
            continue
        slug = toc.group(4)
        if slug not in sections:
            continue
        n = sections[slug]["actual"]
        if int(toc.group(2)) != n:
            drift.append(f"contents {slug}: {toc.group(2)} -> {n}")
            out[i] = f"{toc.group(1)}({n}){toc.group(3)}"

    return out, drift


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="report drift and exit 1")
    args = ap.parse_args()

    lines = README.read_text(encoding="utf-8").split("\n")
    sections = scan(lines)
    if not sections:
        print("sync_counts: no sections found, README structure changed?", file=sys.stderr)
        return 2

    updated, drift = apply(lines, sections)
    total = sum(s["actual"] for s in sections.values())

    if not drift:
        print(f"counts in sync ({len(sections)} sections, {total} papers)")
        return 0

    for item in drift:
        print(("would fix  " if args.check else "fixed      ") + item)

    if args.check:
        print(
            "\nRun `python3 scripts/sync_counts.py` to fix, then commit README.md.",
            file=sys.stderr,
        )
        return 1

    README.write_text("\n".join(updated), encoding="utf-8")
    print(f"README.md updated ({len(sections)} sections, {total} papers)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
