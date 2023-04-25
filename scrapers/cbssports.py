from bs4 import BeautifulSoup
import requests
from .abstract_scraper import AbstractScraper
from .constants import Format

URLS = {
    Format.STANDARD: "https://www.cbssports.com/fantasy/football/rankings/standard/top200/",
    Format.PPR: "https://www.cbssports.com/fantasy/football/rankings/ppr/top200/"
}

class CBSSportsScraper(AbstractScraper):
    @classmethod
    def host(cls):
        return "cbssports.com"

    @classmethod
    def supported_formats(cls) -> list:
        return [format.name for format in URLS.keys()]

    def __init__(self):
        super().__init__()
        for format in URLS.keys():
            self.data[format] = self.scrape(format)

    def scrape(self, format: str):
        results = requests.get(URLS[format], headers=self.headers, timeout=5)
        soup = BeautifulSoup(results.text, "html.parser")
        player_wrappers = soup.find_all("div", { "class": "player-wrapper" })
        
        players = {}
        for column in player_wrappers:
            rows = column.find_all("div", { "class": "player-row" })
            for row in rows:
                rank = row.find({ "div": { "class": "rank" } }).text
                name = row.find({ "span": { "class": "player-name" } }).text
                team_pos = row.find({ "span": { "class": "team position" } }).text.split(" ")
                if name not in players:
                    players[name] = {
                        "ranks": [int(rank)],
                        "team": team_pos[0],
                        "position": team_pos[1]
                    }
                else:
                    players[name]["ranks"].append(int(rank))

        result = sorted([{ 
            "name": name, "position": data["position"], "team": data["team"], "avg": sum(data["ranks"]) / len(data["ranks"])
        } for name, data in players.items()], key=lambda x: x["avg"])

        for index, player in enumerate(result):
            player["rank"] = index + 1
        return result

    def standard_rankings(self):
        return self.data[Format.STANDARD]
    
    def ppr_rankings(self):
        return self.data[Format.PPR]
