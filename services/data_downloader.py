import os

import yfinance as yf


class DataDownloader:
    @staticmethod
    def download_data(tickers, start, end):
        for ticker in tickers:
            print(f"Downloading data for {ticker}")
            if not os.path.exists(f"stock_dfs/{ticker}.csv"):
                df = yf.download(ticker, start=start, end=end)
                df.to_csv(f"stock_dfs/{ticker}.csv")
            else:
                print(f"Already have data for {ticker}")
