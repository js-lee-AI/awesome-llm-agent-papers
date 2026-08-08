#!/usr/bin/env python3
"""Fail on entry glosses that were cut off mid-sentence.

A backfill once truncated nine glosses, three of them leaving a parenthesis
hanging open, and none of it was visible from a diff of the count lines. The
entries still rendered, still linked correctly, and still read as prose until
you reached the end of one. Nothing else in this repo would have caught it.

Two rules, both chosen so that a clean README passes with zero exceptions:

  brackets   a gloss with unbalanced ( ) or [ ] is always a truncation
  dangling   a gloss ending on a word that cannot end an English sentence

The dangling list deliberately leaves out "from", "on" and "for", which end
perfectly good sentences ("the trace to learn from", "work builds on"). Better
to miss a truncation than to train people to ignore this check.

    python3 scripts/check_glosses.py          # check, exit 1 on failure
    python3 scripts/check_glosses.py -v       # also print the entry count
"""
import re
import sys
from pathlib import Path

README = Path(__file__).resolve().parent.parent / "README.md"

ENTRY = re.compile(
    r"^- \*\*\[(?P<title>.+?)\]\((?P<url>[^)]+)\)\*\*"
    r" \((?P<who>[^)]*)\) - \*(?P<gloss>.*?)\*(?P<tail>.*)$"
)

DANGLING = re.compile(
    r"\b(?:and|or|but|the|a|an|of|with|to|in|into|at|as|by|that|which|who|"
    r"than|beyond|across|over|under|through|per|via|between|among|"
    r"e\.g\.|i\.e\.|such|these|those|its|their)$",
    re.IGNORECASE,
)


def problems(gloss):
    out = []
    for opener, closer in (("(", ")"), ("[", "]")):
        if gloss.count(opener) != gloss.count(closer):
            out.append(f"unbalanced {opener}{closer} "
                       f"({gloss.count(opener)} open, {gloss.count(closer)} closed)")
    if not gloss.rstrip().endswith((".", "!", "?")):
        out.append("no sentence-ending punctuation")
    if DANGLING.search(gloss.rstrip().rstrip(".").rstrip()):
        out.append("ends on a word that cannot close a sentence")
    return out


def main():
    verbose = "-v" in sys.argv
    text = README.read_text(encoding="utf-8")
    entries = failures = 0

    for lineno, line in enumerate(text.split("\n"), 1):
        m = ENTRY.match(line)
        if not m:
            continue
        entries += 1
        found = problems(m.group("gloss"))
        if not found:
            continue
        failures += 1
        print(f"README.md:{lineno}: {'; '.join(found)}")
        print(f"    {m.group('title')[:88]}")
        print(f"    ...{m.group('gloss')[-100:]}")

    if failures:
        print(f"\n{failures} truncated gloss(es) in {entries} entries. "
              f"Rewrite them from the paper's own abstract.")
        return 1
    if verbose:
        print(f"all {entries} glosses end in a complete sentence")
    else:
        print(f"glosses OK ({entries} entries)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
