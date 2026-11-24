#!/usr/bin/env python3
"""Two Lines to Your Past Self — entry generator.

Writes the original two-line entry to $MAKEFUN_OUTPUT_DIR/entry.txt
(default ./output/) and self-checks the competition gate before exiting:
exactly two lines, UTF-8 text of 1 to 280 characters, not only whitespace.
"""

import os
import sys

LINE_1 = "Don't send that 2 a.m. text to her on the night of 14 March, the one that starts \"we need to talk\"."
LINE_2 = "You lost the friendship you spent three years rebuilding, and the silence after it taught you that some doors only open once."

ENTRY = LINE_1 + "\n" + LINE_2 + "\n"


def check_gate(text: str) -> None:
    """Fail loudly if the entry breaks the competition gate."""
    if not (1 <= len(text) <= 280):
        raise SystemExit(f"gate fail: entry is {len(text)} chars, must be 1-280")
    if not text.strip():
        raise SystemExit("gate fail: entry is only whitespace")
    lines = text.strip("\n").split("\n")
    if len(lines) != 2:
        raise SystemExit(f"gate fail: entry has {len(lines)} lines, must be exactly 2")
    for i, line in enumerate(lines, 1):
        if not line.strip():
            raise SystemExit(f"gate fail: line {i} is blank")
        if not line.rstrip().endswith((".", "!", "?")):
            raise SystemExit(f"gate fail: line {i} is not a complete sentence")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "./output")
    os.makedirs(out_dir, exist_ok=True)
    check_gate(ENTRY)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {path} ({len(ENTRY)} chars, 2 lines)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
