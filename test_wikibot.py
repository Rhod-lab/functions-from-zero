# from mylib.bot import scrape
from wikibot import scrape

def test_scrape():
    assert "Microsoft" in scrape("Microsoft")