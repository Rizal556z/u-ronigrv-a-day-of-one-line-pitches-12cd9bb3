#!/usr/bin/env python3
"""One-Line Pitch — u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.

Writes one persuasive sentence to /output/entry.txt: it tells a friend
who has never coded that describing their first app idea in plain words
is enough for an AI agent on make.fun to build it for them.
Pure stdlib, no network.
Entry text: one original sentence on letting an AI agent build a first app idea (167 characters).
"""

import os

TEXT = (
    "Tell make.fun your first app idea in plain words and an AI agent "
    "will build it for you \u2014 no coding, no setup, no experience "
    "needed, just the idea already in your head."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
