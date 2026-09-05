import unittest

from scripts.public_x_profile import extract_profile_status_ids, parse_status_page


class PublicXProfileTests(unittest.TestCase):
    def test_extracts_target_statuses(self):
        html = '<a href="/justinsuntron/status/222"></a><a href="/other/status/999"></a><a href="/justinsuntron/status/111"></a>'
        self.assertEqual(extract_profile_status_ids(html, "justinsuntron"), ["222", "111"])

    def test_parses_jina_status(self):
        page = """URL Source: http://x.com/justinsuntron/status/222
Published Time: 2026-09-05T01:02:03.000Z
Markdown Content:
# Justin Sun on X: "HTX update"
"""
        post = parse_status_page(page, "justinsuntron", "902839045356744704", "Justin Sun", "222")
        self.assertEqual(post["createdAtISO"], "2026-09-05T01:02:03Z")
        self.assertEqual(post["text"], "HTX update")


if __name__ == "__main__":
    unittest.main()
