#!/usr/bin/env python3
"""Incremental archive updater for @justinsuntron public X posts.

Requires xreach authenticated via Agent Reach cookies/browser profile.
Run from the repo root: `python3 update.py`. Prints a final `NEW=<n>` line.
Does not touch git; the scheduler decides whether to commit and push.
"""
import csv
import json
import os
import re
import subprocess
from collections import Counter
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime

USER = "justinsuntron"
DISPLAY_NAME = "Justin Sun"
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
ARCH = os.path.join(DATA, "justinsuntron_posts.json")
LOCAL_TZ = timezone(timedelta(hours=8))


def parse_time(post):
    iso = post.get("createdAtISO")
    if iso:
        return datetime.fromisoformat(iso.replace("Z", "+00:00"))
    created = post.get("createdAt")
    if created:
        return parsedate_to_datetime(created)
    return None


def ensure_times(post):
    dt = parse_time(post)
    if dt and not post.get("createdAtISO"):
        post["createdAtISO"] = dt.astimezone(timezone.utc).isoformat()
    if dt and not post.get("createdAtLocal"):
        post["createdAtLocal"] = dt.astimezone(LOCAL_TZ).strftime("%Y-%m-%d %H:%M")
    return post


def sort_key(post):
    dt = parse_time(post)
    return dt.isoformat() if dt else ""


def xreach_json(args, timeout=180):
    try:
        proc = subprocess.run(
            ["xreach", *args, "--json"],
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        if proc.returncode != 0:
            print(f"PULL_ERROR {' '.join(args)}: {(proc.stderr or proc.stdout).strip()}")
            return []
        data = json.loads(proc.stdout)
    except Exception as exc:
        print(f"PULL_ERROR {' '.join(args)}: {exc}")
        return []
    if isinstance(data, dict):
        return data.get("items") or data.get("tweets") or data.get("results") or data.get("data") or []
    return data if isinstance(data, list) else []


def normalize_xreach(post):
    if post.get("author", {}).get("screenName", "").lower() == USER:
        return ensure_times(post)
    user = post.get("user") or {}
    out = {
        "id": str(post.get("id")),
        "text": post.get("text") or "",
        "author": {
            "id": user.get("restId") or user.get("id"),
            "name": user.get("name") or DISPLAY_NAME,
            "screenName": user.get("screenName") or USER,
            "profileImageUrl": user.get("profileImageUrl"),
            "verified": user.get("isBlueVerified"),
        },
        "metrics": {
            "likes": post.get("likeCount"),
            "retweets": post.get("retweetCount"),
            "replies": post.get("replyCount"),
            "quotes": post.get("quoteCount"),
            "views": post.get("viewCount"),
            "bookmarks": post.get("bookmarkCount"),
        },
        "createdAt": post.get("createdAt"),
        "media": post.get("media") or [],
        "urls": post.get("urls") or [],
        "isRetweet": post.get("isRetweet"),
        "retweetedBy": None,
        "lang": post.get("lang"),
        "score": post.get("score"),
    }
    for key in ("isQuote", "isReply", "inReplyToTweetId", "inReplyToUserId", "conversationId"):
        if key in post:
            out[key] = post.get(key)
    if post.get("quotedTweet"):
        out["quotedTweet"] = post.get("quotedTweet")
    return ensure_times(out)


def pull(n=100, since=None):
    raw = xreach_json(["tweets", f"@{USER}", "-n", str(n)])
    if since:
        raw.extend(
            xreach_json(
                [
                    "search",
                    f"from:{USER} since:{since}",
                    "--type",
                    "latest",
                    "-n",
                    str(n),
                    "--all",
                    "--max-pages",
                    "3",
                ],
                timeout=240,
            )
        )
    rows = []
    seen = set()
    for post in raw:
        if not isinstance(post, dict) or not post.get("id"):
            continue
        row = normalize_xreach(post)
        if row.get("author", {}).get("screenName", "").lower() != USER:
            continue
        if row["id"] in seen:
            continue
        seen.add(row["id"])
        rows.append(row)
    return rows


def csv_text(text):
    return "\n".join(line.rstrip() for line in (text or "").replace("\r", " ").split("\n"))


def write_csv(rows):
    cols = [
        "id",
        "url",
        "createdAtISO",
        "createdAtLocal",
        "lang",
        "isRetweet",
        "retweetedBy",
        "likes",
        "retweets",
        "replies",
        "quotes",
        "views",
        "bookmarks",
        "media_count",
        "media_urls",
        "link_urls",
        "quoted_id",
        "quoted_author",
        "quoted_text",
        "text",
    ]
    with open(os.path.join(DATA, "justinsuntron_posts.csv"), "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=cols)
        writer.writeheader()
        for post in rows:
            metrics = post.get("metrics") or {}
            media = post.get("media") or []
            quoted = post.get("quotedTweet") or {}
            writer.writerow(
                {
                    "id": post.get("id"),
                    "url": f"https://x.com/{USER}/status/{post.get('id')}",
                    "createdAtISO": post.get("createdAtISO"),
                    "createdAtLocal": post.get("createdAtLocal"),
                    "lang": post.get("lang"),
                    "isRetweet": post.get("isRetweet"),
                    "retweetedBy": post.get("retweetedBy"),
                    "likes": metrics.get("likes"),
                    "retweets": metrics.get("retweets"),
                    "replies": metrics.get("replies"),
                    "quotes": metrics.get("quotes"),
                    "views": metrics.get("views"),
                    "bookmarks": metrics.get("bookmarks"),
                    "media_count": len(media),
                    "media_urls": " | ".join(item.get("url", "") for item in media if isinstance(item, dict)),
                    "link_urls": " | ".join(post.get("urls") or []),
                    "quoted_id": quoted.get("id"),
                    "quoted_author": (quoted.get("author") or {}).get("screenName"),
                    "quoted_text": csv_text(quoted.get("text")).replace("\n", " "),
                    "text": csv_text(post.get("text")),
                }
            )


def write_ticker_stats(rows):
    ticker_re = re.compile(r"\$([A-Za-z]{1,8})\b")
    counts = Counter()
    first = {}
    last = {}
    for post in sorted(rows, key=lambda item: item.get("createdAtISO", "")):
        text = (post.get("text", "") or "") + " " + ((post.get("quotedTweet") or {}).get("text", "") or "")
        date = (post.get("createdAtISO") or "")[:10]
        for match in set(ticker_re.findall(text)):
            ticker = match.upper()
            counts[ticker] += 1
            first.setdefault(ticker, date)
            last[ticker] = date
    with open(os.path.join(DATA, "ticker_stats.txt"), "w") as out:
        out.write(f"Total posts: {len(rows)}\nDistinct $tickers: {len(counts)}\n\n")
        out.write("ticker  mentions  first_seen  last_seen\n")
        for ticker, count in sorted(counts.items(), key=lambda item: (-item[1], item[0])):
            out.write(f"{ticker:8} {count:6}   {first[ticker]}  {last[ticker]}\n")


def main():
    os.makedirs(DATA, exist_ok=True)
    if os.path.exists(ARCH):
        with open(ARCH) as archive:
            raw_archive = json.load(archive)
    else:
        raw_archive = []
    archive = [ensure_times(post) for post in raw_archive]
    normalized = archive != raw_archive
    have = {post["id"] for post in archive if post.get("id")}
    newest = max((parse_time(post) for post in archive if parse_time(post)), default=None)
    since = newest.astimezone(timezone.utc).date().isoformat() if newest else None
    new_posts = [ensure_times(post) for post in pull(since=since) if post["id"] not in have]
    new_posts.sort(key=sort_key)
    if new_posts or normalized:
        merged = {post["id"]: post for post in archive if post.get("id")}
        for post in new_posts:
            merged[post["id"]] = post
        rows = sorted(merged.values(), key=sort_key, reverse=True)
        with open(ARCH, "w") as archive:
            json.dump(rows, archive, ensure_ascii=False, indent=2)
        write_csv(rows)
        write_ticker_stats(rows)
        for post in new_posts:
            preview = (post.get("text") or "")[:60].replace(chr(10), " ")
            print(f"  + {post.get('createdAtISO', '')[:16]} {post['id']} {preview}")
        if new_posts:
            print(f"TOTAL={len(rows)} NEWEST={rows[0].get('createdAtISO', '')}")
    print(f"NEW={len(new_posts)}")


if __name__ == "__main__":
    main()

