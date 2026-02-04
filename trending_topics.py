#!/usr/bin/env python3
"""Fetch quick trending topic results from Google Trends RSS."""
from __future__ import annotations

import argparse
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

DEFAULT_GEO = "US"
DEFAULT_LIMIT = 10


def fetch_trending_topics(geo: str) -> list[str]:
    url = (
        "https://trends.google.com/trends/trendingsearches/daily/rss?"
        f"geo={geo}"
    )
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = response.read()
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Failed to fetch trends data: {exc}") from exc

    root = ET.fromstring(data)
    channel = root.find("channel")
    if channel is None:
        return []

    topics: list[str] = []
    for item in channel.findall("item"):
        title = item.findtext("title")
        if title:
            topics.append(title.strip())
    return topics


def format_topics(topics: list[str], limit: int) -> str:
    if not topics:
        return "No trending topics found."

    lines = []
    for idx, topic in enumerate(topics[:limit], start=1):
        lines.append(f"{idx}. {topic}")
    return "\n".join(lines)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Get quick trending topics for article writers.",
    )
    parser.add_argument(
        "--geo",
        default=DEFAULT_GEO,
        help="Two-letter country code (default: US).",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=DEFAULT_LIMIT,
        help="Number of topics to display (default: 10).",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    try:
        topics = fetch_trending_topics(args.geo)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    print(format_topics(topics, args.limit))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
