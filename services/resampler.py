import matplotlib.dates as mdates


class Resampler:
    def resample_data(self, df):
        df_ohlc = df["Adj Close"].resample("10D").ohlc()
        df_volume = df["Volume"].resample("10D").sum()
        df_ohlc.reset_index(inplace=True)
        df_ohlc["Date"] = df_ohlc["Date"].map(mdates.date2num)
        return df_ohlc, df_volume
