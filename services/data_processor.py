from collections import Counter
import numpy as np


class DataProcessor:
    def __init__(self, ticker, signal_generator, hm_days):
        self.ticker = ticker
        self.signal_generator = signal_generator
        self.hm_days = hm_days

    def process_data(self, new_df):
        new_df["{}_target".format(self.ticker)] = list(
            map(
                self.signal_generator.buy_sell_hold,
                *[new_df["{}_1d".format(self.ticker)] for _ in range(self.hm_days)]
            )
        )
        vals = new_df["{}_target".format(self.ticker)].values.tolist()
        str_vals = [str(i) for i in vals]
        print("Data spread", Counter(str_vals))
        new_df.fillna(0, inplace=True)
        new_df = new_df.replace([np.inf, -np.inf], np.nan)
        new_df.dropna(inplace=True)
        df_vals = new_df[self.ticker].pct_change()
        df_vals = df_vals.replace([np.inf, -np.inf], 0)
        df_vals.fillna(0, inplace=True)
        X = df_vals.values
        y = new_df["{}_target".format(self.ticker)].values
        return X, y
