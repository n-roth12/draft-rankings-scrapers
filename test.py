from scrapers import scrape

def main():
    print("test")
    scraper = scrape("fantasypros.com", "0.0")
    print(scraper.half_ppr_rankings())
    print(scraper.supported_formats())

if __name__ == "__main__":
    main()