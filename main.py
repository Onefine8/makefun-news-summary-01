"""make.fun bounty news-summary-01: writes one summary of the world's news
of Wednesday 11 November 2026 to /output/entry.txt.

Deterministic: no network, no randomness, no clock. The summary is embedded
in this file and written byte-for-byte on every run.
"""
import os

SUMMARY = """Wednesday, 11 November 2026

Ukraine and Russia ended two days of US-mediated talks in Abu Dhabi with no ceasefire and no deal on territory, but agreed in principle on a prisoner swap of 1,000 to 1,500 people each side - envoy Jared Kushner called it the biggest release of the war. It was their first such meeting in nine months.

President Trump, after meeting Qatar's prime minister, said the war with Iran was "militarily effectively over" and the US would hold the status quo. Tehran struck a different note: its negotiator said the Strait of Hormuz, closed for more than 250 days, would "never return" to how it was, after two more tankers reportedly hit mines and caught fire. Brent crude fell below $90 a barrel for the first time in four months.

In Washington, the House voted 211-204 to refer impeachment articles against Defense Secretary Pete Hegseth to committee, killing the effort. The Justice Department charged three men over alleged Iran-backed plots including an attack on RAF Fairford in Britain, as Treasury Secretary Scott Bessent moved onto a military base after threats to his life. A US Army officer was arrested in Britain on suspicion of spying for Russia.

China's trade surplus passed $1 trillion in the first ten months of the year, a record pace, with October alone adding $105.3 billion. US inflation ran hotter than expected: consumer prices rose 0.4% in October, above the 0.3% forecast. Anthropic filed to list on the Nasdaq under the ticker ANT, and TSMC said demand for its chips was insatiable.

At the COP31 climate summit in Antalya, leaders began two days of speeches as the UN chief warned the climate crisis was outrunning the world; the US is sitting out the talks for a second year. Spain held its first general strike in 14 years over the housing crisis, and Gaza's fragile truce frayed as Israeli strikes killed at least eight people. In Sudan, drone attacks knocked out power in parts of the country."""

OUT = os.environ.get("ENTRY_PATH", "/output/entry.txt")


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(SUMMARY)


if __name__ == "__main__":
    main()
