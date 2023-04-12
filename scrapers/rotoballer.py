import requests
from .abstract_scraper import AbstractScraper

URLS = {
    "standard": "https://rankings.rotoballer.com:8000/api/players?league=Overall&leagueSize=10&page=1&perPage=100&spreadsheet=standard&twoQb=false",
    "half": "https://rankings.rotoballer.com:8000/api/players?league=Overall&leagueSize=10&page=1&perPage=100&spreadsheet=half-ppr&twoQb=false",
    "full": "https://rankings.rotoballer.com:8000/api/players?league=Overall&leagueSize=10&page=1&perPage=100&spreadsheet=ppr&twoQb=false"
}

class RotoBallerScraper(AbstractScraper):
    @classmethod
    def host(cls):
        return "rotoballer.com"

    @classmethod
    def supported_formats(cls):
        return list(URLS.keys())

    def __init__(self) -> None:
        super().__init__()
        self.standard_data = self.scrape("standard")
        self.half_ppr_data = self.scrape("half")
        self.full_ppr_data = self.scrape("full")

    def scrape(self, format):
        result = requests.get(URLS[format])
        return result.json()["data"]

    def standard_rankings(self):
        return self.standard_data

    def half_ppr_rankings(self):
        return self.half_ppr_data
    
    def ppr_rankings(self):
        return self.full_ppr_data
