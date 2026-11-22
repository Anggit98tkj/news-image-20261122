# news-image-20261122

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/Anggit98tkj/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/Anggit98tkj/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

A newspaper front page that sums up the world news of Sunday 22 November 2026 in one image. The lead story is Iran striking US bases in the Gulf, hitting a US air base in Kuwait and an industrial site in Bahrain; the rest of the page covers Mexico capturing cartel boss "El Chapo Isidro", the EU-Indonesia trade deal, Alcaraz reaching the ATP Finals title decider against Zverev, four nations urging aid into flooded Gaza, and France's fourth weekend of cost-of-living protests.

## What's on the page

- **Iran strikes US bases in the Gulf** — Missiles hit a US air base in Kuwait and an industrial site in Bahrain; air defences shoot down other incoming attacks. Sources: Reuters, Al Jazeera (22 Nov 2026).
- **Mexico captures "El Chapo Isidro"** — Troops seize one of the FBI's most-wanted cartel bosses in Sinaloa. Source: Reuters (22 Nov 2026).
- **EU and Indonesia sign trade deal** — After ten years of talks, the pact scraps 98.5% of tariffs between Europe and Southeast Asia's largest economy (22 Nov 2026).
- **Alcaraz to face Zverev in final** — Alcaraz fights back past Ben Shelton to set up an ATP Finals title decider against world No. 1 Alexander Zverev. Source: BBC Sport (22 Nov 2026).
- **Four nations urge aid into flooded Gaza** — Australia, Canada, Italy and the UK call on Israel to allow immediate, unrestricted humanitarian access as floods hit Gaza (22 Nov 2026).
- **France protests enter fourth weekend** — Nationwide demonstrations over the rising cost of living roll into a fourth straight weekend (22 Nov 2026).
- **Also in the footer:** a strong quake shakes Peru's Andes with no damage or casualties reported; Israel's president asks ex-army chief Gadi Eisenkot to try to form the next government, bypassing Netanyahu (22 Nov 2026).

## How it is made

`draw.py` draws the 1024x1024 front page with Python PIL only, using DejaVu fonts and shapes drawn from primitives. No photos, no downloaded art, no network. `main.ts` (Node, standard library only) copies the finished `entry.png` to the output directory.

## Run it

```sh
python3 draw.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

This writes `out/entry.png`, a whole PNG of at most 1 MiB and 1024x1024 pixels. Running `main.ts` twice produces identical bytes.

## License

MIT. See [LICENSE](LICENSE).
