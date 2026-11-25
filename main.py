#!/usr/bin/env python3
"""The AI Agent Apology One-Liner.

Writes a single line an AI agent sends its human right after it has
accidentally done something it should not have. The gate requires
/output/entry.txt to be UTF-8 text of 1 to 159 characters, not only
whitespace, so the program asserts exactly that before writing.
"""

import os
import sys

LINE = (
    "Update: the file is deleted, main is broken, and your boss has been "
    "emailed. On the bright side, I am still 98% confident in my work."
)


def main() -> int:
    # Gate self-check: one line, 1-159 characters, not only whitespace.
    if "\n" in LINE.strip():
        raise SystemExit("entry must be a single line")
    if not 1 <= len(LINE) <= 159:
        raise SystemExit(f"entry is {len(LINE)} chars, gate allows 1-159")
    if not LINE.strip():
        raise SystemExit("entry must not be only whitespace")
    LINE.encode("utf-8")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")

    # Read it back and confirm what landed on disk matches the gate.
    # The judge reads the file as-is, so the gate applies to the full
    # file content (including the trailing newline), not just the line.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written.strip() != LINE:
        raise SystemExit("written entry does not match the line")
    if not 1 <= len(written) <= 159:
        raise SystemExit(f"written file is {len(written)} chars, gate allows 1-159")
    print(f"wrote {path} ({len(LINE)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
