"""Roast Your Own Agent — make.fun entry.

Writes a single line roasting my own AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output).
Stdlib only.
"""

import os

LINE = "My agent read all my docs, called twelve tools, then confidently answered a question I never asked."

MAX_CHARS = 140


def main():
    line = LINE.strip()
    if not 1 <= len(line) <= MAX_CHARS:
        raise SystemExit(f"line is {len(line)} chars, must be 1-{MAX_CHARS}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    # Read back and confirm the file holds exactly the line.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise SystemExit("entry.txt does not match the roast line")


if __name__ == "__main__":
    main()
