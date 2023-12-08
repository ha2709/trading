import pickle
import datetime as dt
import os, sys
from services.ticker_scraper import TickerScraper
from services.data_downloader import DataDownloader


def save_sp500_tickers():
    tickers = TickerScraper.scrape_tickers()
    with open("sp500tickers.pickle", "wb") as f:
        pickle.dump(tickers, f)
    return tickers


def get_data_from_yahoo(reload_sp500=False):
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open("data/sp500tickers.pickle", "rb") as f:
            tickers = pickle.load(f)

    if not os.path.exists("stock_dfs"):
        os.makedirs("stock_dfs")

    start_date = dt.datetime(2022, 1, 1)
    end_date = dt.datetime(2023, 12, 5)

    DataDownloader.download_data(tickers, start_date, end_date)


def get_data_for_ticker(ticker):
    tickers = [ticker]
    if not os.path.exists("stock_dfs"):
        os.makedirs("stock_dfs")

    start_date = dt.datetime(2022, 1, 1)
    end_date = dt.datetime(2023, 12, 5)

    DataDownloader.download_data(tickers, start_date, end_date)

if __name__ == "__main__":
    # get_data_from_yahoo()
    if len(sys.argv) != 2:
        print("Usage: python collect_data.py <ticker>")
        sys.exit(1)

    user_ticker = sys.argv[1].upper()

    if not user_ticker.isalpha():
        print("Invalid ticker symbol. Please provide a valid stock ticker.")
        sys.exit(1)

    get_data_for_ticker(user_ticker)
