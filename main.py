#!/usr/bin/env python3
"""Write one line to /output/entry.txt: a one-line laugh for make.fun's
The One-Line Laugh bounty."""
import os

LINE = "I bought noise-cancelling headphones so I could ignore my kids in high definition."

# The gate requires 1-200 UTF-8 characters, not only whitespace:
# fail loudly here rather than shipping an invalid entry.
if not 1 <= len(LINE) <= 200 or not LINE.strip():
    raise ValueError("entry line must be 1-200 non-blank characters")


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
