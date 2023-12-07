import bs4 as bs
import requests


class TickerScraper:
    @staticmethod
    def scrape_tickers(url="https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"):
        resp = requests.get(url)
        soup = bs.BeautifulSoup(resp.text, features="html.parser")
        table = soup.find("table", {"class": "wikitable sortable"})
        tickers = [row.findAll("td")[0].text for row in table.findAll("tr")[1:]]
        return tickers
