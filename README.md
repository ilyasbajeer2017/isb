# Trending Topics CLI

A small command-line utility to quickly list trending topics so article writers can find ideas fast.

## Usage

```bash
python trending_topics.py
```

Options:

- `--geo`: Two-letter country code (default `US`).
- `--limit`: Number of topics to display (default `10`).

Example:

```bash
python trending_topics.py --geo=GB --limit=5
```

## Data source

This tool reads the daily trending searches RSS feed from Google Trends.
