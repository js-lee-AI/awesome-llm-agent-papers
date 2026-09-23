# Contributing

Contributions that add a relevant, verifiable paper are welcome.

## How to add a paper

Add an entry to the correct section of [`README.md`](README.md), matching the existing format:

```markdown
- **[Full Paper Title](https://arxiv.org/abs/XXXX.XXXXX)** (First-Author Surname et al., Venue Year) - *One-line reason it matters.* [[code](https://github.com/org/repo)]
```

Then open a pull request.

## Requirements

- A working **arXiv or DOI link** is mandatory.
- A **one-line gloss** (in *italics*) is mandatory.
- Add a **`[code]`** link only if an official implementation exists (verify it resolves).
- Put the paper in the section that matches its **role**, following the survey's taxonomy.
- The ⭐ marks the [Starter Kit](README.md#starter-kit); leave it for the maintainer to assign.

## Section counts

Each section states its count in three places: the Contents list, the section heading, and the **Show N papers** toggle. Do not edit them by hand. Run:

```bash
python3 scripts/sync_counts.py
```

It recounts every section and updates all three. CI runs `sync_counts.py --check` on pull requests touching `README.md` and fails if the numbers disagree with the actual entries.

To have it run automatically before each commit, enable the repo's hooks once per clone:

```bash
git config core.hooksPath .githooks
```

## Translations

The list is also published in Korean, Simplified Chinese and Japanese (`README.ko.md`, `README.zh-CN.md`, `README.ja.md`), each following `README.md` line for line. Edit `README.md` only. I bring the translations along when I merge, so the translation check on your pull request is expected to report a difference, and it won't fail the run.

If you'd like to improve a translation itself, a pull request against that file is welcome too. Keep it line for line with `README.md`; `python3 scripts/check_i18n.py` shows where they differ.
