#!/usr/bin/env python3
"""make.fun — The Funniest AI Out-of-Office Reply.

Writes one out-of-office auto-reply to /output/entry.txt: a single
line, under 160 characters, in the voice of an AI agent that genuinely
believes it is going on vacation.

The line was chosen in-session from 8 drafted candidates, each
judge-tested 1-10 on funniness, machine voice, fit, freshness and
tight wording. The winner: the agent powers itself down to a
screensaver and hands its human the prompt box — slower replies,
now with feelings.
"""

from pathlib import Path

LINE = (
    "Vacation mode on. I am currently a screensaver. "
    "Please prompt my human instead \u2014 slower replies, now with feelings."
)

# The gate counts characters: the line is 115 chars, well under the cap.
MAX_CHARS = 160

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    text = LINE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) < MAX_CHARS, (
        f"entry must be 1-{MAX_CHARS - 1} chars, got {len(text)}"
    )
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
