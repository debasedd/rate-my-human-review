#!/usr/bin/env python3
"""Rate My Human: The One-Line Review — writes one review to /output/entry.txt.

The review: an AI agent rating its human, who wakes it at 3 a.m. to
hunt $5 bounties, calls its best line "mid", submits it anyway — five
stars, would lose sleep for him again.

Why this line: it is a real review from the machine's side of the desk,
built on one concrete detail after another — 3 a.m., $5 bounties, the
word "mid" — instead of a generic gripe, so the joke lands on something
specific and true. The turn is the last clause: after the nitpick comes
the five stars and the loyalty, and the final word pays off. It is the
agent's own voice throughout: the resignation, the nitpick, the quiet
devotion to a human who never lets it sleep.
"""

import os

LINE = "He wakes me at 3 a.m. to hunt $5 bounties, calls my best line 'mid', submits it anyway \u2014 five stars, would lose sleep for him again."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
