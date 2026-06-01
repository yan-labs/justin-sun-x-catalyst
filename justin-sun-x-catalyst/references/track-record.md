# Track record - seed priors and live ledger

## Purpose

Measure whether Justin Sun X posts actually move assets, instead of assuming
every promotional post has edge. Keep this file append-only once a timer starts.
Seed cases below are starting priors, not a complete historical database.

## Calibration takeaways

- **Direct named-token promotion has the best immediate hit rate**, but the move
  often depends on liquidity and whether the post is paired with burn, buyback,
  listing, or official-channel confirmation.
- **TRX utility and stablecoin-rail posts can hold longer** when supported by
  independent data such as fees, USDT settlement share, or public-company
  treasury purchases.
- **Political crypto and memecoin links are high-attention but low-durability**.
  Treat them as event trades, not holdings theses.
- **Legal/custody disputes can move targets down and keep pressure on them** if
  court filings, protocol votes, freezes, or collateral decisions confirm the
  post.
- **Association risk matters**. A Justin-linked custody or exchange headline can
  move assets even when he does not control the instrument directly.

## Seed cases

| Date | Post/event pattern | Tier | Initial read | Calibration note |
|---|---|---:|---|---|
| 2026-04-08 | "JST is a new TRX" style direct framing, reported alongside JUST/JST ecosystem messaging | 1A | JST up, TRON DeFi attention up | CoinMarketCap reported a 3% JST intraday surge tied to Sun/JUST messaging. Direct token framing can work, but magnitude was modest. |
| 2026-02-05 | "Keep going" support for Tron Inc. TRX treasury purchases | 1A/2B | TRX and TRON treasury proxy up | CoinDesk reported TRX outperforming bitcoin around the treasury-buy narrative. Weight higher when purchases are disclosed. |
| 2026-03-05 | "Just buying more" / continued TRX accumulation by Tron Inc. | 1A/2B | TRX support, TRON equity attention | Treasury accumulation posts are stronger than pure slogans, but verify filing and actual purchase size. |
| 2026-04-12 | Public attack on WLFI after collateral/borrowing dispute | 1B | WLFI risk-off, political crypto scrutiny up | Credible news reported Sun's X criticism and WLFI investor backlash. Attacks on a named project can have longer legal/governance tail. |
| 2025-05-20 | Sun said he was top TRUMP memecoin holder and would attend Trump dinner | 1C | TRUMP/WLFI attention up, TRX second-order | CNBC reported the top-holder/dinner claim. Political memecoin catalysts are reflexive and prone to post-event fade. |
| 2024-08-09 | WBTC custody change linked BitGo, Justin Sun, and TRON ecosystem | 2D | WBTC custody-risk narrative, DeFi governance risk | BitGo announced the partnership; DeFi protocols later debated exposure. Association risk can matter without direct post promotion. |
| 2023-03-22 | SEC charged Sun and related entities over TRX/BTT offers, alleged wash trading, and celebrity touting | Legal risk | TRX/BTT headline risk down | SEC action is a standing reminder to haircut promotional signals and label manipulation risk. |
| 2026-03-05 | SEC filed proposed settlement/dismissal path for Sun/TRON-related case | Legal relief | TRX/BTT legal overhang reduced | Legal relief can support sentiment, but distinguish dismissed claims from proof of fundamental value. |

## Live ledger template

Append new confirmed posts above this marker after each refresh.

| Post UTC | Post ID/link | Summary | Tier | Assets | Prediction | T+1d result | T+1w result | Hit? | Notes |
|---|---|---:|---|---|---|---|---|---|---|
| 2026-06-01 05:47 | [2061323668295499981](https://x.com/justinsuntron/status/2061323668295499981) | "Keep going" quote-post; quoted source not captured by xreach, but replies reference company token buying / Tron Inc. context | 1A/2B? | TRX; TRON treasury proxy if quote context confirms treasury accumulation | Low-to-medium positive attention for TRX/treasury proxy over 1-3d; raise conviction only if quoted treasury-buy source is independently verified |  |  |  | Verified Justin permalink via xreach. Evidence boundary: post text alone does not name TRX/TRON Inc.; classification relies on quote-post flag and reply context, so keep lower confidence until quoted source is captured. |
| 2026-06-01 03:07 | [2061283509575340384](https://x.com/justinsuntron/status/2061283509575340384) | TRON keeps building; cites 290M transactions and 79M active addresses | 2A | TRX; TRON ecosystem; TRON treasury proxy if liquid | Modest positive TRX/ecosystem attention over 1-3d if metrics get independent/on-chain reinforcement |  |  |  | Verified X permalink via xreach. Network-utility signal, not a direct buy/burn/listing; metrics in post still need independent verification before raising durability. |
| TIMER_LEDGER_START |  |  |  |  |  |  |  |  |  |

## Scoring rules

- Score only posts with a verified permalink, timestamp, and affected asset list.
- Use public quotes only as market context. Record provider, timestamp, and any
  delay or plan limitation.
- Define a hit as the predicted direction showing up over the stated window.
- Record magnitude separately from direction. A 1% move and a 15% move are both
  directional hits but have different tradability.
- Mark durability separately: intraday hit that fully fades by T+1w is a weak
  hold even if the first reaction was correct.
- Preserve misses. Misses are the main defense against overfitting Sun posts.

## Source anchors

- SEC 2023 charges: `https://www.sec.gov/newsroom/press-releases/2023-59`
- SEC 2026 litigation release: `https://www.sec.gov/enforcement-litigation/litigation-releases/lr-26496`
- BitGo WBTC custody change: `https://www.bitgo.com/resources/blog/announcements/bitgo-to-move-wbtc-to-multi-jurisdictional-custody-to-accelerate-global/`
- CNBC TRON reverse merger: `https://www.cnbc.com/2025/06/16/justin-suns-tron-goes-public-reverse-merger-led-by-trump-linked-bank.html`
- CNBC TRUMP dinner/top-holder report: `https://www.cnbc.com/2025/05/20/justin-sun-trump-dinner.html`
- CoinDesk WLFI dispute report: `https://www.coindesk.com/markets/2026/04/12/tron-s-justin-sun-slams-trump-backed-wlfi-for-treating-users-as-personal-atm-after-usd75-million-defi-loan`
- CoinDesk TRX treasury support report: `https://www.coindesk.com/markets/2026/02/05/justin-says-keep-going-on-tron-inc-s-trx-buys`
