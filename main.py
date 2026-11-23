#!/usr/bin/env python3
"""Make the Judge Smile — entry writer.

Writes one line (at most 200 characters) about a small good thing that
happened today to /output/entry.txt, deterministically: the same text on
every run, with no randomness, no network and no extra output.

The line's craft:
- Warmth: a small kindness from a stranger ("for the road, son") that
  makes the narrator feel loved, not just fed.
- Surprise turn: the extra fried egg slips in quietly, then the whisper
  reframes an ordinary rice breakfast as someone caring.
- One concrete detail: the fried egg on the rice — a single vivid image
  carries the whole scene, no extra props needed.

Gate: the entry must be 1-200 characters (checked at runtime before
writing) and a single line, so it stays short, warm and judge-ready.
"""

import os

ENTRY = (
    "This morning the warung lady slipped an extra fried egg onto my rice "
    "and whispered, 'for the road, son' — and I walked to work feeling "
    "like somebody's favourite person."
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
