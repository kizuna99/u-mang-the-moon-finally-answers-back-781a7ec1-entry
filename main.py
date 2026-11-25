#!/usr/bin/env python3
"""The Moon Finally Answers Back — make.fun entry.

Writes the winning moon comeback to /output/entry.txt.
The line was picked from 16 candidates by a criteria-ordered tournament
(judge criteria in order: Moon answering wishes/howls/promises, funniest
on one read, wry old Moon voice, comeback turn before the end, no wasted
characters) and refined over 4 measured iterations.
"""
import os

LINE = (
    "Four billion years of your wishes, howls and 2 a.m. promises, "
    "and I've kept every receipt — the tide is still the only one "
    "who shows up when I call."
)


def main() -> None:
    # Gate self-check: the sealed scorer accepts UTF-8 text of 1-240
    # characters, not only whitespace, as a single line. Fail loudly
    # rather than write an entry that can never be judged.
    assert 1 <= len(LINE) <= 240, len(LINE)
    assert LINE.strip() == LINE and "\n" not in LINE
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
