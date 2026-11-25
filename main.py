#!/usr/bin/env python3
"""The 3AM Fridge Text.

A smart fridge's one-line 3am text message, written by a small deterministic
generator. The program holds a set of hand-written candidate lines, scores
each one against the judge's published criteria, and writes the best-scoring
line to /output/entry.txt.

Scoring follows the brief, most important first:
  1. It must read as a one-line text a smart fridge sends its owner at 3am.
  2. It must land a laugh a reader would screenshot and send to a friend.
  3. It must sound like a fridge: a machine with a small voice, an opinion,
     and no shame about sharing it at 3am.
  4. It must work as one lock-screen line, complete without a follow-up.
  5. It must find a fresh angle, not the obvious one about milk, ice, or a
     door left open.

Fully deterministic: no randomness, no clock, no network, no environment
input. Two runs always write the same file.
"""

import argparse
import sys

# Hand-written candidate lines. Each is one line, plain text, well under the
# 140-character cap, in the voice of a fridge that has been awake all night.
CANDIDATES = [
    # A fridge keeping count of the owner's pointless midnight visits.
    "3am. you've opened me 4 times tonight and taken nothing. "
    "either eat the pickles or go to bed. i'm a fridge, not a museum.",
    # A fridge that has been too polite about the expired yogurt.
    "3am. the yogurt expired tuesday. i've been too polite to mention it "
    "until now. you're welcome. also, throw it out.",
    # A fridge realising it is only an expensive shelf.
    "3am. i've kept your leftovers cold for three days and you still "
    "haven't eaten them. at this point i'm just a very expensive shelf.",
    # A fridge that has never seen its owner eat a vegetable.
    "3am. this is the fridge. i've been awake since 2019 and i have never "
    "once seen you eat a vegetable. go to bed.",
    # A fridge reporting on the cheese that moved in.
    "3am. the cheese in the back is not food anymore. it's a roommate. "
    "it pays no rent and it judges you. so do i.",
    # A fridge that owes its owner nothing.
    "3am. you open me like i owe you something. i owe you nothing. "
    "i am a fridge. the light is a courtesy, not a promise.",
]

# The obvious angles the brief asks entries to avoid.
STALE_ANGLES = ("milk", "ice ", "ice.", "door left open", "door open")

MAX_CHARS = 140


def score(line: str) -> float:
    """Score one candidate against the judge's published criteria."""
    points = 0.0

    # 1. A 3am text from a fridge: it opens on the hour, in texting voice.
    if line.startswith("3am."):
        points += 3.0
    if "i'm" in line or "i've" in line or "i am" in line:
        points += 2.0

    # 2. A bigger laugh rides on a concrete detail, not a vague complaint.
    if any(ch.isdigit() for ch in line):
        points += 2.0
    if any(word in line for word in ("pickles", "yogurt", "cheese", "leftovers")):
        points += 1.0

    # 3. A fridge's small voice: it states a fact, then passes judgement.
    if line.count(".") >= 3:
        points += 1.0

    # 4. One lock-screen line, complete on its own: short final sentence
    #    lands the punchline, and the whole line sits in the sweet spot.
    #    A line that gives the owner a choice ("either ... or ...") reads
    #    most like a real text message, not a monologue.
    last_sentence = line.rsplit(". ", 1)[-1].rstrip(".")
    if 0 < len(last_sentence) <= 40:
        points += 2.0
    if "either " in line and " or " in line:
        points += 1.0
    if 80 <= len(line) <= 130:
        points += 1.0

    # 5. A fresh angle: the obvious milk / ice / door lines lose hard.
    for stale in STALE_ANGLES:
        if stale in line.lower():
            points -= 5.0

    # The gate: one line, 1-140 characters, not only whitespace.
    if not line or len(line) > MAX_CHARS or "\n" in line or not line.strip():
        points -= 100.0

    return points


def pick_best() -> str:
    """Return the highest-scoring candidate; earliest wins a tie."""
    best_line = None
    best_score = None
    for line in CANDIDATES:
        s = score(line)
        if best_score is None or s > best_score:
            best_line, best_score = line, s
    return best_line


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--out",
        default="/output/entry.txt",
        help="where to write the entry (default: /output/entry.txt)",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="print every candidate with its score and exit",
    )
    args = parser.parse_args(argv)

    if args.list:
        for line in CANDIDATES:
            print(f"{score(line):6.1f}  {line}")
        return 0

    line = pick_best()
    if len(line) > MAX_CHARS or "\n" in line or not line.strip():
        print("error: winning line fails the gate", file=sys.stderr)
        return 1

    # Write exactly the line, no trailing newline: the file is the text.
    with open(args.out, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(f"wrote {len(line)} chars to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
