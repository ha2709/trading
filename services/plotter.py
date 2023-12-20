import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc


class Plotter:
    def plot_candlestick_chart(self, ax, df_ohlc):
        candlestick_ohlc(ax, df_ohlc.values, width=2, colorup="g")

    def plot_moving_averages(self, ax, df):
        ax.plot(df.index, df["5ma"], label="5-day MA", color="blue")
        ax.plot(df.index, df["20ma"], label="20-day MA", color="green")
        ax.plot(df.index, df["50ma"], label="50-day MA", color="red")
        ax.legend(loc="upper left")

    def plot_volume_bars(self, ax, df_volume):
        ax.fill_between(
            df_volume.index.map(mdates.date2num),
            df_volume.values,
            0,
            color="blue",
            alpha=0.5,
        )
