#!/usr/bin/env python3
"""One-letter day report.

Emits exactly one character: the initial of a single word that
summarizes an ordinary, relatable day in one sharp image.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

# The whole report is one initial letter. No gloss, no punctuation,
# no trailing newline: the gate measures the file length exactly.
# One letter, chosen to carry the day in a single sharp picture:
# the half-awake shuffle of running on autopilot.
LETTER = "Z"


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LETTER, encoding="utf-8")


if __name__ == "__main__":
    main()
