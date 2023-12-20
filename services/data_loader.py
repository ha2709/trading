import pandas as pd


class DataLoader:
    def load_data(self, filename):
        return pd.read_csv(
            filename,
            parse_dates=True,
            index_col=0,
            date_parser=lambda x: pd.to_datetime(x, format="%Y-%m-%d"),
        )

    def load_csv(self, filename):
        return pd.read_csv(filename)

    def preprocess_data(self, df):
        df.set_index("Date", inplace=True)
        df.rename(columns={"Adj Close": "AAPL"}, inplace=True)
        df.drop(["Open", "High", "Low", "Close", "Volume"], axis=1, inplace=True)
        return df
