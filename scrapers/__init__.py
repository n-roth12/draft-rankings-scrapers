from .abstract_scraper import AbstractScraper
from .cbssports import CBSSportsScraper
from .fantasyfootballcalculator import FantasyFootballCalculatorScraper
from .fantasypros import FantasyProsScraper
from .rotoballer import RotoBallerScraper

SCRAPERS = {
    CBSSportsScraper.host(): CBSSportsScraper,
    FantasyFootballCalculatorScraper.host(): FantasyFootballCalculatorScraper,
    FantasyProsScraper.host(): FantasyProsScraper,
    RotoBallerScraper.host(): RotoBallerScraper
}

def scrape(site: str, format: str) -> AbstractScraper:
    scraper = SCRAPERS[site](format)
    return scraper
    
