from bs4 import BeautifulSoup
import requests
from scrapers.abstract_scraper import AbstractScraper

URLS = {
    "standard": "https://www.cbssports.com/fantasy/football/rankings/standard/top200/"
}

class CBSSportsScraper(AbstractScraper):
    @classmethod
    def host(cls):
        return "cbssports.com"

    @classmethod
    def supported_formats(cls) -> list:
        return list(URLS.keys())

    def __init__(self, url):
        super().__init__(url)

    def scrape(self, format: str):
        results = requests.get(URLS[format], headers=super.headers, timeout=5)
        soup = BeautifulSoup(results.text, "html.parser")
        self.standard_data = soup

    def standard_rankings(self):
        return self.standard_data
