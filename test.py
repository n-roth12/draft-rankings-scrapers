from scrapers import scrape

def main():
    print("test")
    scraper = scrape("cbssports.com")
    print(scraper.ppr_rankings())

if __name__ == "__main__":
    main()