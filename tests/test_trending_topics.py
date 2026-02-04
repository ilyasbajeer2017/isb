import unittest
from pathlib import Path

import trending_topics


class TrendingTopicsTests(unittest.TestCase):
    def test_parse_trending_topics(self):
        fixture = Path(__file__).parent / "fixtures" / "sample_trends.xml"
        topics = trending_topics.parse_trending_topics(fixture.read_bytes())
        self.assertEqual(topics, ["Sample Topic One", "Sample Topic Two"])

    def test_format_topics_respects_limit(self):
        formatted = trending_topics.format_topics(["A", "B", "C"], limit=2)
        self.assertEqual(formatted.splitlines(), ["1. A", "2. B"])

    def test_format_topics_empty(self):
        self.assertEqual(trending_topics.format_topics([], limit=3), "No trending topics found.")


if __name__ == "__main__":
    unittest.main()
