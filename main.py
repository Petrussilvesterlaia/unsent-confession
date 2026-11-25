#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint — entry writer.

Writes the two-part micro-confession (a To: line and the unsent message,
one line, exactly as typed) to /output/entry.txt.
"""

import os

ENTRY = (
    "To: Mum\n"
    "sorry i never rang, i kept saying one more trade and then it was 2am and your light was off again\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
