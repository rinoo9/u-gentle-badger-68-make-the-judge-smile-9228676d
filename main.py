#!/usr/bin/env python3
"""Make the Judge Smile — entry writer.

Writes one line (at most 200 characters) about a small good thing that
happened today to /output/entry.txt, deterministically: the same text on
every run, with no randomness, no network and no extra output.

The line's craft:
- Warmth: a small child's trust ("it's magic, don't lose it") makes the
  narrator feel chosen, not just handed something.
- Surprise turn: a paper flower — worthless, weightless — becomes a secret
  treasure the narrator carries to work like something precious.
- One concrete detail: the paper flower pressed into the hand — a single
  vivid image carries the whole scene, no extra props needed.

Gate: the entry must be 1-200 characters (checked at runtime before
writing) and a single line, so it stays short, warm and judge-ready.
"""

import os

ENTRY = (
    "The neighbour's little girl pressed a paper flower into my hand this "
    "morning and whispered, \"it's magic, don't lose it\" — I carried it "
    "to work like a secret treasure."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry is {len(ENTRY)} characters, must be 1-200")
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
