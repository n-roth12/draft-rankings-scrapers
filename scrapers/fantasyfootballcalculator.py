from bs4 import BeautifulSoup
import requests
from .abstract_scraper import AbstractScraper

URLS = {
    "standard": "https://fantasyfootballcalculator.com/rankings/standard",
    "half": "https://fantasyfootballcalculator.com/rankings/half-ppr",
    "full": "https://fantasyfootballcalculator.com/rankings/ppr"
}

class FantasyFootballCalculatorScraper(AbstractScraper):
    @classmethod
    def host(cls):
        return "fantasyfootballcalculator.com"

    @classmethod
    def supported_formats(cls) -> list:
        return list(URLS.keys())

    def __init__(self, url: str) -> None:
        super().__init__(url)
        self.standard_data = self.scrape("standard")
        self.half_ppr_data = self.scrape("half")
        self.ppr_data = self.scrape("full")

    def scrape(self, format: str):
        results = requests.get(URLS[format], headers=self.headers, timeout=5)
        soup = BeautifulSoup(results.text, "html.parser")

        table = soup.find("table")
        tbody = table.find("tbody")
        trs = tbody.find_all("tr")
        result = []    
        
        for tr in trs:
            tds = tr.find_all("td")
            result.append({
                "rank": tds[0].text,
                "name": tds[1].find("a").text,
                "team": tds[2].text,
                "position": tds[3].text,
                "bye": tds[4].text
            })

        return result
    
    def standard_rankings(self):
        return self.standard_data

    def half_ppr_rankings(self):
        return self.half_ppr_data

    def ppr_rankings(self):
        return self.ppr_data
