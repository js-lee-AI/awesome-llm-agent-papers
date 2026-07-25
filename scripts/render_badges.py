#!/usr/bin/env python3
"""Render the header badges as self-hosted PNGs under assets/badges/.

Why self-host at all: GitHub's Camo image proxy has repeatedly failed to fetch
from img.shields.io for this repo, so badges hotlinked to shields.io render as
broken images while relative-path assets/*.png always render (see eccfb52).
The cost of self-hosting is staleness, and that is what this script removes:
run on a schedule by .github/workflows/badges.yml, it re-reads the counts from
the GitHub API and re-renders the PNGs, so "stars" tracks reality without
depending on Camo at render time.

Style matches the existing badges: flat-square geometry, near-black label
block, burgundy value block from the survey palette, Lato, rendered at 2x and
displayed at height="20".

Usage:
    python3 scripts/render_badges.py [--repo owner/name] [--check]

--check exits 1 if any PNG would change, without writing.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "assets" / "badges"
FONT_PATH = ROOT / "assets" / "fonts" / "Lato-Regular.ttf"
FONT_FALLBACKS = [
    "/usr/share/fonts/truetype/lato/Lato-Regular.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]

REPO_DEFAULT = "js-lee-AI/awesome-llm-agent-papers"
LABEL_BG = (43, 43, 43)  # #2b2b2b
VALUE_BG = (139, 38, 53)  # #8B2635, the survey's burgundy
TEXT = (255, 255, 255)
SCALE = 2  # rendered at 2x, displayed at height="20"
HEIGHT = 20 * SCALE
FONT_SIZE = 11 * SCALE
PAD = 7 * SCALE  # horizontal padding on each side of each text block


def load_font() -> ImageFont.FreeTypeFont:
    for path in [FONT_PATH, *map(Path, FONT_FALLBACKS)]:
        if path.exists():
            return ImageFont.truetype(str(path), FONT_SIZE)
    raise SystemExit(
        f"No usable font. Expected {FONT_PATH} (vendored) or one of: "
        + ", ".join(FONT_FALLBACKS)
    )


def repo_facts(repo: str, token: str | None) -> dict:
    req = urllib.request.Request(
        f"https://api.github.com/repos/{repo}",
        headers={"User-Agent": "badge-renderer", "Accept": "application/vnd.github+json"},
    )
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read())
    return {
        "stars": data["stargazers_count"],
        "forks": data["forks_count"],
        "license": (data.get("license") or {}).get("spdx_id") or "MIT",
    }


def render(label: str, value: str, font: ImageFont.FreeTypeFont) -> Image.Image:
    probe = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    label_w = round(probe.textlength(label, font=font)) + 2 * PAD
    value_w = round(probe.textlength(value, font=font)) + 2 * PAD

    img = Image.new("RGB", (label_w + value_w, HEIGHT), LABEL_BG)
    draw = ImageDraw.Draw(img)
    draw.rectangle([label_w, 0, label_w + value_w, HEIGHT], fill=VALUE_BG)
    draw.text((label_w / 2, HEIGHT / 2), label, font=font, fill=TEXT, anchor="mm")
    draw.text(
        (label_w + value_w / 2, HEIGHT / 2), value, font=font, fill=TEXT, anchor="mm"
    )
    return img


def png_bytes(img: Image.Image) -> bytes:
    from io import BytesIO

    buf = BytesIO()
    img.save(buf, format="PNG", optimize=True)
    return buf.getvalue()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=os.environ.get("GITHUB_REPOSITORY", REPO_DEFAULT))
    ap.add_argument("--check", action="store_true", help="exit 1 if a PNG would change")
    args = ap.parse_args()

    facts = repo_facts(args.repo, os.environ.get("GITHUB_TOKEN"))
    font = load_font()
    badges = {
        "stars": ("stars", str(facts["stars"])),
        "forks": ("forks", str(facts["forks"])),
        "license": ("License", facts["license"]),
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    # Re-render on a change of *value*, not of bytes. Pillow's PNG output is not
    # byte-stable across versions, so comparing bytes would commit a new "badge"
    # every time the runner image bumps Pillow, with the numbers identical.
    manifest_path = OUT_DIR / "manifest.json"
    previous = {}
    if manifest_path.exists():
        try:
            previous = json.loads(manifest_path.read_text())
        except json.JSONDecodeError:
            pass
    current = {name: value for name, (_, value) in badges.items()}

    changed = []
    for name, (label, value) in badges.items():
        path = OUT_DIR / f"{name}.png"
        if path.exists() and previous.get(name) == value:
            print(f"unchanged     {name}.png  ({label} {value})")
            continue
        changed.append(name)
        if args.check:
            print(f"WOULD CHANGE  {name}.png  ({label} {previous.get(name)} -> {value})")
        else:
            path.write_bytes(png_bytes(render(label, value, font)))
            print(f"wrote         {name}.png  ({label} {value})")

    if changed and not args.check:
        manifest_path.write_text(json.dumps(current, indent=2, sort_keys=True) + "\n")

    return 1 if (args.check and changed) else 0


if __name__ == "__main__":
    sys.exit(main())
