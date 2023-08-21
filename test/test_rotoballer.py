import unittest
from draft_rankings_scrapers import scrape


class TestRotoballerScraper(unittest.TestCase):
    def test_scrape_rankings(self):
        scraper = scrape("rotoballer.com")
        self.assertGreaterEqual(len(scraper.half_ppr_rankings()), 1)
