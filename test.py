from scrapers import scrape

def main():
    print("test")
    scraper = scrape("fantasyfootballcalculator.com")
    print(scraper.ppr_rankings())

if __name__ == "__main__":
    main()