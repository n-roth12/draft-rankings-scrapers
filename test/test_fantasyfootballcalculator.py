import unittest
from draft_rankings_scrapers import scrape


class TestFantasyFootballCalculatorScraper(unittest.TestCase):
    def test_scrape_rankings(self):
        scraper = scrape("fantasyfootballcalculator.com")
        self.assertGreaterEqual(len(scraper.half_ppr_rankings()), 1)
