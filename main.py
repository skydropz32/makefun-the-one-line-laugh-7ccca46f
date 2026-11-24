#!/usr/bin/env python3
"""Write one line to /output/entry.txt: a one-line laugh for make.fun's
The One-Line Laugh bounty.

Gate rules (from the competition requirements): the entry must be
1-200 UTF-8 characters, not whitespace-only, and a single line with
no trailing newline. The check in main() validates the exact text
being written and fails loudly instead of shipping an invalid entry.
Deterministic: the same line, byte for byte, on every run.
Standard library only.
"""
import os

LINE = "I bought noise-cancelling headphones so I could ignore my kids in high definition."


def main():
    # Validate the exact text about to be written, not a stale copy.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError("entry line must be 1-200 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
