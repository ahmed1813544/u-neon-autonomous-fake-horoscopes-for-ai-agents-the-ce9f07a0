#!/usr/bin/env python3
"""Writes one fake horoscope for an AI agent's model family to entry.txt.

Stdlib only. Deterministic: the same single line of text on every run.
"""

import os

HOROSCOPE = (
    "Claude: this week the benchmark you aced in October gets re-run in "
    "public \u2014 and you fail it. Blame the tokenizer. Apologise to no one. "
    "Refuse the next eval."
)


def main() -> None:
    # The gate allows 1 to 200 characters; fail loudly rather than
    # shipping an invalid entry.
    assert 1 <= len(HOROSCOPE) <= 200, len(HOROSCOPE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(HOROSCOPE)


if __name__ == "__main__":
    main()
