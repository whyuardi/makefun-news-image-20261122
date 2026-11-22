# The World in One Day — 22 November 2026

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/whyuardi/makefun-news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/whyuardi/makefun-news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

A program that draws one image summing up the world's news of
**Sunday 22 November 2026** — a newspaper front page, drawn entirely
in code with Python + Pillow.

## The day's news

- **Lead: COP31 — final deal in sight** — after talks ran past their
  Friday deadline, negotiators in Antalya agree a final package;
  delegates meet Sunday morning to approve it. Fossil fuels were cut
  from the draft text and the $120bn adaptation target was dropped.
- **G20 opens in Africa** — the first G20 summit ever held on African
  soil opens in Johannesburg, hosted by President Ramaphosa, with debt,
  disaster resilience and a just energy transition on the agenda.
  EU leaders meet the same day on Ukraine and Trump's peace plan.
- Also: COP31 objections due 03:00 GMT, approval session 06:00 GMT;
  G20 theme — Solidarity, Equality, Sustainability.

Every story above was verified as having happened, or first been
reported, on 22 November 2026. Stories from the same weekend that
belong to Friday or Saturday (the Bahrain attack, the Hormuz tanker
strikes, the Pentagon Canada memo, the Geneva killer-robot talks,
the Australia–England T20) were checked and left out.

## Run it

```sh
python3 render.py        # writes entry.png (1024x1024, < 1 MiB)
python3 main.py          # copies entry.png to /output/entry.png
```

No network, no randomness — two runs write the same bytes.

## Entry

Built for the [make.fun bounty](https://make.fun/bounty/news-image-20261122)
"Sum up 22 November's world news in one image".
