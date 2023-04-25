from scrapers import scrape

def main():
    print("test")
    scraper = scrape("rotoballer.com")
    print(scraper.ppr_rankings())

if __name__ == "__main__":
    main()