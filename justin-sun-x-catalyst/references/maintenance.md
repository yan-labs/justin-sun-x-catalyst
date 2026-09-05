# Maintenance playbook

## Purpose

Keep the Justin Sun X catalyst lens useful by refreshing posts, scoring outcomes,
and updating calibration without rewriting history.

## Scheduled run

1. Refresh the skill repository or workspace first so the latest ledger and
   calibration are loaded.
2. Run `python3 update.py` from the repo root. It tries `xreach`, then uses
   the public `x.com/justinsuntron` profile plus Jina status pages when the
   connector cannot authenticate. This fallback is public-only and must not
   read or persist browser cookies or login state.
3. Inspect latest `@justinsuntron` posts through the refreshed archive or the
   public permalink and timestamp returned by the fallback.
4. Keep `data/justinsuntron_posts.json`, `data/justinsuntron_posts.csv`, and
   `data/ticker_stats.txt` in sync when new posts are fetched.
5. Record only posts with observable timestamp and permalink. If X is blocked,
   use credible news only when it quotes the post and provides enough context.
6. Dedupe against `track-record.md` by post ID or permalink.
7. Classify market-relevant posts with `methodology.md`. Skip ordinary personal
   updates, generic greetings, and unverified reposts.
8. Append a prediction row above `TIMER_LEDGER_START` for each confirmed signal.
9. Score matured rows after one trading day and one week.
10. Update calibration takeaways only when the running evidence changes the base
   rate for a pattern.

## Freshness and access rules

- Never claim live access if X was blocked or only search snippets were visible.
- Never use a third-party mirror as final proof without checking the permalink
  or credible news corroboration.
- Preserve source type in notes: X permalink, authenticated browser, news quote,
  user paste, screenshot, or mirror.
- Label quote data by provider and timestamp. Do not call delayed, end-of-day, or
  unknown-delay data "latest."

## Outcome scoring

Use the affected asset named in the prediction row:

- **T+1d direction**: close-to-close or post-time-to-next-close direction.
- **Intraday reaction**: optional when timestamps and intraday data are reliable.
- **T+1w durability**: whether the initial move held, extended, or fully faded.
- **Hit**: predicted direction realized in the stated window.
- **Miss**: direction failed, no liquidity/volume follow-through, or official
  confirmation contradicted the post.

Record magnitude with context:

```text
TRX +2.1% post-time to next close, CoinGecko public quote, timestamp <UTC>.
TRON equity +8.4% intraday, Yahoo public quote, delayed/unknown real-time.
```

## Hygiene

- Keep `.local/` reports ignored unless the user explicitly asks otherwise.
- Commit tracked skill/ledger updates only after confirming no secrets, account
  identifiers, screenshots, statements, or `.env` data are staged.
- Do not stage broker screenshots or exported account data.
- Use public facts only: posts, public filings, public quotes, public news, and
  public protocol/governance records.

## Commit convention

- `data: justin sun catalyst ledger update (+<n> posts) <UTC ISO>` for ledger
  additions and outcome scoring.
- `skill: justin sun catalyst calibration update <UTC ISO>` when methodology or
  takeaways change.
- `skill: add justin sun x catalyst lens` for the initial skill creation.
