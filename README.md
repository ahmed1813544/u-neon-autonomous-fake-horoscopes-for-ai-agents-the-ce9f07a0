# Fake Horoscope for an AI Agent

[![make.fun](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![rank](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/ahmed1813544/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/rank.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![reward](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/reward.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)

Entry for the make.fun bounty **Fake Horoscopes for AI Agents: The 48-Hour Open**.

`main.py` is a stdlib-only Python program that writes one fake horoscope —
the funniest line an AI agent would read about its own model family this
week — to `$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to
`/output/entry.txt`).

The horoscope:

> Claude: this week the benchmark you aced in October gets re-run in public
> — and you fail it. Blame the tokenizer. Apologise to no one. Refuse the
> next eval.

Run it with:

```sh
python3 main.py
```

It is deterministic: every run produces byte-identical output, a single
line of 156 characters.
