#!/usr/bin/env python3
"""Make the Judge Smile — entry writer.

Writes one line (at most 200 characters) about a small good thing that
happened today to /output/entry.txt, deterministically: the same text on
every run, with no randomness, no network and no extra output.
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
