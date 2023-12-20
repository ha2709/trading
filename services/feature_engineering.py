import pandas as pd
import numpy as np


class FeatureEngineering:
    def __init__(self, hm_days):
        self.hm_days = hm_days

    def create_joined_closes(self, df, ticker):
        main_df = pd.DataFrame()
        df.set_index("Date", inplace=True)
        df.rename(columns={"Adj Close": "AAPL"}, inplace=True)
        df.drop(["Open", "High", "Low", "Close", "Volume"], axis=1, inplace=True)
        # for df in dfs:
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how="outer")
        print(19)
        main_df.to_csv("data_join/{}.csv".format(ticker))

    def calculate_diff_pct(self, new_df, ticker):
        for i in range(1, self.hm_days + 1):
            new_df["{}_{}d".format(ticker, i)] = (
                new_df[ticker].shift(-i) - new_df[ticker]
            ) / new_df[ticker]
        new_df.fillna(0, inplace=True)
