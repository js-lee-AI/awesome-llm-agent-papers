# Vendored font

`Lato-Regular.ttf` (Lukasz Dziedzic / tyPoland), the version distributed in TeX Live.

Licensed under the [SIL Open Font License, Version 1.1](https://scripts.sil.org/OFL), which permits redistribution.

It is vendored rather than installed so that `scripts/render_badges.py` produces byte-identical PNGs locally and in CI. Without a pinned font file the badge widths shift with whatever fonts the runner happens to have, and every scheduled run would commit a "changed" badge.
