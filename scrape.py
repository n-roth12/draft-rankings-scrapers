import sys
from draft_rankings_scrapers import scrape
from draft_rankings_scrapers.format import Format


def optimize(args: list[str]):
    if len(args) < 3:
        print('Missin arguments: must include both site and player pool filename.')
        return
    site = args[1]
    format = args[2]

    rankings = scrape(site)
    print(rankings.get_format(Format(int(format))))


if __name__ == '__main__':
    optimize(sys.argv)
