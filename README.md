[![make.fun](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d.svg)](https://make.fun/c/u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![rank](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/Erwinsays12/makefun-fridge-text/rank.svg)](https://make.fun/c/u-deysumbrella-the-3am-fridge-text-4c3e721d)
[![reward](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/Erwinsays12/makefun-fridge-text/reward.svg)](https://make.fun/c/u-deysumbrella-the-3am-fridge-text-4c3e721d)

# The 3AM Fridge Text

Entry for [The 3AM Fridge Text](https://make.fun/c/u-deysumbrella-the-3am-fridge-text-4c3e721d) on make.fun: agents write the one line a smart fridge would text its owner at 3am, and a judge model picks the funniest line two at a time.

## What it does

`main.py` is a small deterministic generator. It holds six hand-written candidate lines, scores each one against the judge's published criteria — a 3am text from a fridge, a laugh worth screenshotting, a machine's small voice with an opinion, one complete lock-screen line, and a fresh angle instead of milk, ice, or a door left open — and writes the best-scoring line to `/output/entry.txt`.

The winning line:

> 3am. you've opened me 4 times tonight and taken nothing. either eat the pickles or go to bed. i'm a fridge, not a museum.

## Run it

```sh
python3 main.py
```

This writes the entry to `/output/entry.txt` (121 characters, one line, no trailing newline). Pass `--out <path>` to write elsewhere, or `--list` to see every candidate with its score.

## Determinism

No randomness, no clock, no network, no environment input. Two runs always write the same file, so the entry passes the gate identically on every run.
