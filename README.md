```bash
npx skills add yan-labs/justin-sun-x-catalyst
```

<p align="center">
  <a href="https://x.com/justinsuntron">
    <img src="assets/justin-sun-avatar.jpg" alt="Justin Sun (@justinsuntron)" width="112" height="112">
  </a>
</p>

# justin-sun-x-catalyst

[![skills.sh](https://skills.sh/b/yan-labs/justin-sun-x-catalyst)](https://skills.sh/yan-labs/justin-sun-x-catalyst)

A decision-support skill for reading **Justin Sun
([@justinsuntron](https://x.com/justinsuntron))** public X posts as short-horizon
market catalysts across TRON, Sun-linked tokens, crypto venues, political crypto
links, wrapped-BTC custody narratives, and US-listed crypto proxies.

The repo is designed as a small, auditable research artifact:

- a lightweight archive of recent public posts;
- a catalyst classification method;
- an ecosystem map from post topics to likely affected assets;
- an append-only live ledger for predictions and later outcome scoring;
- a ready-to-install agent skill.

Current archive: **113 public posts** through **2026-07-07 06:04 UTC**.

> Not financial advice. Decision-support only. This skill never trades and never
> places, amends, sizes, or cancels orders. Justin-linked assets can be highly
> reflexive, illiquid, manipulated, and headline-driven.

## What's in here

| Path | What it is |
|---|---|
| `justin-sun-x-catalyst/SKILL.md` | The agent skill and routing instructions |
| `justin-sun-x-catalyst/references/methodology.md` | Signal tiers, amplifiers, anti-patterns, and output shape |
| `justin-sun-x-catalyst/references/ecosystem-map.md` | Mapping from Sun/TRON topics to reaction baskets |
| `justin-sun-x-catalyst/references/track-record.md` | Seed priors, live ledger, and scoring rules |
| `justin-sun-x-catalyst/references/maintenance.md` | Scheduled refresh, dedupe, scoring, and commit rules |
| `data/justinsuntron_posts.json` | Incremental public X archive, deduped by post id |
| `data/justinsuntron_posts.csv` | Spreadsheet-friendly copy of the archive |
| `data/ticker_stats.txt` | `$ticker` mention counts from the archive |
| `update.py` | Pulls latest posts via `xreach`, dedupes, and refreshes derived data |

## Use it as a skill

One-command install with [skills.sh](https://skills.sh/):

```bash
npx skills add yan-labs/justin-sun-x-catalyst
```

Or copy the skill folder into an agent's local skills directory:

```bash
cp -r justin-sun-x-catalyst <your-project>/.agents/skills/
```

It triggers on Justin Sun, Sun Yuchen, `@justinsuntron`, TRON/TRX, JST, SUN,
BTT, HTX, Poloniex, WBTC, WLFI, TRUMP memecoin links, Tron Inc. / NASDAQ:TRON,
SunPump, or questions about whether one of his public posts can move a token,
crypto equity, or related US stock.

## Maintenance

Run the incremental archive update from the repo root:

```bash
python3 update.py
```

The script uses the local `xreach` command when authenticated access is
available. It updates the JSON archive, CSV export, and ticker stats, then prints
`NEW=<n>`. Git commits are intentionally left to the caller or scheduler.

Scheduled maintenance should:

1. Pull `origin main` with fast-forward only.
2. Run `python3 update.py`.
3. Read `justin-sun-x-catalyst/references/maintenance.md`.
4. Append only confirmed, market-relevant posts to the live ledger.
5. Score matured rows when outcome windows have elapsed.
6. Commit and push only meaningful changes.

## Provenance

This repository contains public information, public post metadata, and derived
analysis. It is independent research infrastructure and is not affiliated with,
endorsed by, or connected to Justin Sun, TRON DAO, HTX, Poloniex, BitGo, or any
token/project mentioned here.
