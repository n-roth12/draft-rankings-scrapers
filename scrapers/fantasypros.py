from bs4 import BeautifulSoup
import requests
import re
import json
from .abstract_scraper import AbstractScraper

URLS = {
    "standard": "https://www.fantasypros.com/nfl/rankings/consensus-cheatsheets.php",
    "half": "https://www.fantasypros.com/nfl/rankings/half-point-ppr-cheatsheets.php",
    "full": "https://www.fantasypros.com/nfl/rankings/ppr-cheatsheets.php"
}

class FantasyProsScraper(AbstractScraper):
    @classmethod
    def host(self):
        return "fantasypros.com"

    @classmethod
    def supported_formats(cls) -> list:
        return list(URLS.keys())

    def __init__(self, url):
        super().__init__(url)
        self.standard_data = self.scrape("standard")
        self.half_ppr_data = self.scrape("half")
        self.ppr_data = self.scrape("full")

    def scrape(self, format: str):
        results = requests.get(URLS[format], headers=self.headers, timeout=5)
        soup = BeautifulSoup(results.text, "html.parser")

        scripts = soup.find_all("script")
        p = re.compile('/var ecrData/')
        for script in scripts:
            if (script.string):
                z = re.search("var ecrData = {.*};", script.string)
                if z:
                    temp = z.group(0).replace("var ecrData = ", "").replace(";", "")
                    data = json.loads(temp)
                    return data

    def standard_rankings(self):
        return self.standard_data

    def half_ppr_rankings(self):
        return self.half_ppr_data

    def ppr_rankings(self):
        return self.ppr_data
