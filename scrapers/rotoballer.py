import requests
from .abstract_scraper import AbstractScraper
from .constants import Format

URLS = {
    Format.STANDARD: "https://rankings.rotoballer.com:8000/api/players?league=Overall&leagueSize=10&page=1&perPage=300&spreadsheet=standard&twoQb=false",
    Format.HALF_PPR: "https://rankings.rotoballer.com:8000/api/players?league=Overall&leagueSize=10&page=1&perPage=300&spreadsheet=half-ppr&twoQb=false",
    Format.PPR: "https://rankings.rotoballer.com:8000/api/players?league=Overall&leagueSize=10&page=1&perPage=300&spreadsheet=ppr&twoQb=false"
}

class RotoBallerScraper(AbstractScraper):
    @classmethod
    def host(cls):
        return "rotoballer.com"

    @classmethod
    def supported_formats(cls):
        return [format.name for format in URLS.keys()]

    def __init__(self) -> None:
        super().__init__()
        for format in URLS.keys():
            self.data[format] = self.scrape(format)

    def scrape(self, format):
        result = requests.get(URLS[format])
        return result.json()["data"]

    def standard_rankings(self):
        return self.data[Format.STANDARD]

    def half_ppr_rankings(self):
        return self.data[Format.HALF_PPR]
    
    def ppr_rankings(self):
        return self.data[Format.PPR]
