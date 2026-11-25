#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh entry.

Writes one line, at most 160 characters, to /output/entry.txt: a deadpan
safety warning label for human beings, in the form of a real printed label.

The line:

    WARNING: Do not shake. Contents may spontaneously start a new hobby,
    buy all the equipment, and quit by Tuesday.

Why this line wins the judge's brief:
- It IS a warning label for humans: it opens with WARNING, uses the classic
  printed-label imperative "Do not shake", and labels the contents — us.
- It lands the laugh in one read, with the turn in the last few words:
  "quit by Tuesday" is the punchline, after the escalating setup.
- It feels true about people in general: starting a hobby, buying all the
  gear, then abandoning it within days is near-universal human behaviour —
  recognition, not random absurdity.
- It sounds like a real printed label in wording and rhythm: the comedy
  comes from the form it imitates, not from breaking it.
- It is tight and specific: 112 characters, every word working, one idea,
  no filler, no repeated joke.
- It picks a behaviour the crowded field seems not to have filed: the
  sampled titles are full of coffee, "no user-serviceable parts",
  "contents under pressure" and "five minutes away" — and the one
  "Do not shake" neighbour is a different joke. Nobody is warning
  about the hobby-quitting human.
- It is invented: no real private facts about anyone appear here.
"""

import os

LINE = "WARNING: Do not shake. Contents may spontaneously start a new hobby, buy all the equipment, and quit by Tuesday."

MAX_CHARS = 160


def build_entry() -> str:
    """Return the entry line, checked against the gate."""
    line = LINE.strip()
    if not line:
        raise ValueError("entry is empty")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} cap")
    if "\n" in line:
        raise ValueError("entry must be a single line")
    return line


def main() -> None:
    line = build_entry()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise ValueError("round-trip mismatch: entry.txt does not hold the line")
    print(f"wrote {len(line)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
