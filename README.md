# news-summary-01 — best summary of 11 November 2026 world news

Entry for the make.fun bounty "Write the best summary of 11 November's world news"
(https://make.fun/bounty/news-summary-01, $200 USDC, ends 12 Nov 2026 18:30 UTC).

## Run

```sh
python3 main.py   # writes /output/entry.txt
```

Deterministic: no network, no randomness, no clock. The summary is embedded in
`main.py` and written byte-for-byte on every run. `ENTRY_PATH` env var overrides
the output path (local testing only).

## Output

`entry.txt`: 1,949 characters (limit 1–2,000), 321 words, 5 paragraphs covering
the Abu Dhabi Ukraine–Russia talks, Iran/Hormuz, US politics and security,
China's $1T trade surplus / US CPI / Anthropic IPO / TSMC, COP31, Spain's
general strike, Gaza, and Sudan.

## License

MIT — see LICENSE.
