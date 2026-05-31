# Methodology - reading Justin Sun X posts as market catalysts

## Purpose

Classify Justin Sun's public X posts by how directly they can move related
tokens, crypto equities, or US-listed stocks. Rank signals by immediate reaction
reliability, then separately label durability, because many Sun-linked moves are
attention-driven and fade quickly.

Treat every output as a catalyst read, not a recommendation. Confirm price,
liquidity, market status, and broker data separately before any manual action.

## Source hierarchy

1. **Verified X permalink observed in the current run**: strongest post source.
2. **Authenticated browser view of `@justinsuntron`**: acceptable if timestamp
   and text are visible.
3. **Credible news quoting the post with timestamp/permalink**: acceptable when
   X is blocked.
4. **User-pasted text or screenshot**: usable, but label as user-provided.
5. **Unverified repost, mirror, or paraphrase**: use only for lead generation;
   do not score as a confirmed signal.

## Tier 1 - Direct asset call

Use Tier 1 when the post directly names or unmistakably points to a tradable
asset, token, stock, treasury company, or exchange.

**1A. Explicit buy/accumulate/support language.**
- Examples: `buying more`, `keep going`, `new TRX`, `support`, `accumulate`,
  `treasury`, `burn`, `listed`, `launch`.
- Likely affected assets: the named token/equity first, then close ecosystem
  proxies from `ecosystem-map.md`.
- Reliability: highest for immediate direction, especially when paired with a
  treasury buyback, exchange listing, token burn, or public-company filing.
- Durability: medium only when backed by verifiable buybacks, filings, TVL,
  revenue, stablecoin flows, or real liquidity.

**1B. Direct attack or dispute.**
- Examples: allegations of unfair treatment, freezing, insolvency, extortion,
  user harm, exchange/security failures.
- Direction: usually negative for the target project/token; can be positive for
  competing Justin-linked assets if the post redirects attention.
- Durability: depends on legal/fundamental follow-through. Governance disputes
  can keep pressure on the target longer than ordinary promotional posts.

**1C. Personal status or political access with a named asset.**
- Examples: top holder claim, VIP dinner, advisory role, public bell-ringing,
  government/political access.
- Direction: positive attention burst for the named memecoin, public company, or
  ecosystem; high reversal risk after the event.
- Durability: low unless a new capital flow, listing, or legal/regulatory event
  follows.

## Tier 2 - Ecosystem announcement

Use Tier 2 when the post is not a single-asset call but affects a clear Sun/TRON
ecosystem basket.

**2A. TRON network utility / stablecoin rails.**
- Triggers: USDT on TRON, settlement volume, fee revenue, active addresses,
  tokenized assets, institutional settlement, cross-chain integrations.
- Likely assets: TRX first; then TRON ecosystem tokens and Nasdaq TRON if it is
  trading as a TRX-treasury proxy.
- Durability: better than pure hype when metrics are independently verifiable.

**2B. Tokenomics: burn, buyback, staking, treasury accumulation.**
- Triggers: burn amounts, buyback cadence, staking yield, public-company TRX
  purchases, balance-sheet accumulation.
- Likely assets: the named token and related treasury equity.
- Durability: medium if repeated and disclosed; low if only rhetorical.

**2C. Exchange / platform / launchpad catalyst.**
- Triggers: HTX, Poloniex, SunPump, new listing, liquidity campaign, memecoin
  launch, perpetual DEX, fee campaign.
- Likely assets: platform token if liquid, listed memecoin, TRX gas/attention,
  exchange-sensitive crypto equities by second order.
- Durability: usually low. Treat as flow-driven unless data proves retention.

**2D. WBTC / custody / DeFi collateral narrative.**
- Triggers: WBTC custody, BitGo, BiT Global, wrapped BTC, Maker/Aave/DeFi risk,
  collateral acceptance/removal.
- Direction: project-specific. Sun-association confidence posts can help WBTC
  confidence; governance-risk posts can pressure WBTC-linked DeFi collateral.
- Durability: event-driven. Verify protocol votes and custody updates.

## Tier 3 - Crypto macro or policy narrative

Use Tier 3 when the post comments on broad crypto policy, US politics, ETF flows,
stablecoin regulation, rates, Bitcoin, or risk appetite without a direct asset.

- Direction: broad crypto beta first; TRX reacts only if the post links the
  macro theme to TRON utility.
- Reliability: lower than Tier 1/2.
- Durability: low unless the same theme is confirmed by policy, exchange data,
  ETF flows, or on-chain stablecoin flows.

## Amplifiers

Add conviction when multiple factors stack:

1. Names a specific asset, ticker, or public company.
2. Uses direct action language: `buy`, `buying more`, `keep going`, `burn`,
   `launch`, `first`, `largest`, `settlement`.
3. Includes verifiable mechanics: transaction hash, buyback size, filing, court
   filing, listing notice, protocol vote, bridge/custody update.
4. Comes from Justin Sun plus official TRON/HTX/Poloniex/TRON Inc. channels
   within the same window.
5. Posts pre-open or during liquid trading hours for the affected asset.
6. Repeats the same theme over several posts.
7. Connects crypto narrative to a US-listed equity or public-company treasury.

## Anti-patterns

Do not over-score these:

- Generic bullish crypto slogans with no named asset.
- Retweets without original commentary.
- Partnership language without a counterparty confirmation.
- Memecoin launch hype after the token already spiked.
- Ambiguous emoji-only posts.
- Legal threats without docket, complaint, filing, or named counterparty.
- Any quote that cannot be tied to a current permalink or credible source.

## Per-post checklist

1. Record source type, timestamp, permalink, and exact observed text summary.
2. Decide whether the post is market-relevant. Skip pure personal updates.
3. Assign Tier 1/2/3 and direction: up, down, mixed, or unclear.
4. List named assets and second-order proxies from `ecosystem-map.md`.
5. Count amplifiers and anti-patterns.
6. Check `track-record.md` for similar prior cases and measured hit rate.
7. State expected window: intraday, 1-3 days, 1-2 weeks, or event-dependent.
8. Name invalidation triggers: no volume follow-through, official denial,
   failed listing, adverse court filing, depeg, hack, regulatory pushback.
9. Label price sources as public market context, not broker truth.

## Output shape

Use this compact format:

```text
Post: <date/time, source, permalink>
Signal: <one-line post summary>
Tier: <1A/1B/1C/2A/2B/2C/2D/3> | Direction: <up/down/mixed>
Likely movers: <primary assets> | Secondary: <proxies>
Reliability: <high/medium/low> | Duration: <intraday/1-3d/1-2w/event>
Why it may work: <amplifiers>
Why it may fail: <anti-patterns/invalidation>
Data caveat: <X/source/price freshness>
```
