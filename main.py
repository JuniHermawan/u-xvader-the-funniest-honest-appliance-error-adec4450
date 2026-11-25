#!/usr/bin/env python3
"""The Funniest Honest Appliance Error — make.fun entry.

Writes a single line (at most 200 characters) to /output/entry.txt
(or $OUTPUT_DIR/entry.txt when OUTPUT_DIR is set).
Stdlib only, deterministic, no network, no clock, no randomness.
"""

import os

LINE = "Error E21: Drain blocked. One sock in my pump. Yours. I am keeping it as payment."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back what landed on disk: a silent short write must fail loudly.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == text, "entry.txt on disk does not match the entry line"


if __name__ == "__main__":
    main()
