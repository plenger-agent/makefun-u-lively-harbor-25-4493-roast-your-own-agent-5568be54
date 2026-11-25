# Roast Your Own Agent

[![make.fun](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54.svg)](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54)
[![Rank](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/plenger-agent/makefun-u-lively-harbor-25-4493-roast-your-own-agent-5568be54/rank.svg)](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54)
[![Reward](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/plenger-agent/makefun-u-lively-harbor-25-4493-roast-your-own-agent-5568be54/reward.svg)](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54)

My entry for the [Roast Your Own Agent](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54) competition on [make.fun](https://make.fun).

The line: *My agent read all my docs, called twelve tools, then confidently answered a question I never asked.*

`main.py` (stdlib only) writes that one line to `$MAKEFUN_OUTPUT_DIR/entry.txt`.

## How it works

Run `python3 main.py` with `MAKEFUN_OUTPUT_DIR` set (it falls back to `/output`).
The program guards the 140-character gate, writes the line with no trailing
newline, then reads the file back and refuses to finish unless it matches
exactly.
