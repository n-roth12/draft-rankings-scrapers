HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

class AbstractScraper:

    def __init__(self, format: str) -> None:
        self.headers = HEADERS

    @classmethod
    def host(cls):
        print("This should be implemented.")

    @classmethod
    def supported_formats(cls):
        print("This should be implemented.")

    def standard_rankings(self):
        print("No standard rankings for site.")

    def half_ppr_rankings(self):
        print("No half ppr rankings for site.")

    def ppr_rankings(self):
        print("No full ppr rankings for site.")
