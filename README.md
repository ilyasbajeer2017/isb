# Trending Topics CLI

A small command-line utility to quickly list trending topics so article writers can find ideas fast.

## Usage

```bash
python trending_topics.py
```

Options:

- `--geo`: Two-letter country code (default `US`).
- `--limit`: Number of topics to display (default `10`).
- `--source-file`: Path to a local RSS XML file to parse instead of fetching online.

Example:

```bash
python trending_topics.py --geo=GB --limit=5
```

Offline example:

```bash
python trending_topics.py --source-file tests/fixtures/sample_trends.xml
```

## Data source

This tool reads the daily trending searches RSS feed from Google Trends.

## Testing

```bash
python -m unittest discover -s tests
```
