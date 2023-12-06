import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd

# import pandas_datareader.data as web
import numpy as np
import yfinance as yf
from collections import Counter


matplotlib.use(
    "TkAgg"
)  # Use 'TkAgg' backend (replace with 'Qt5Agg' or 'Agg' if needed)

start = "2022-01-01"
end = "2023-12-5"

symbol = "AAPL"
# df = yf.download(symbol, start=start, end=end)
# df.to_csv('dji_30.csv')
df = pd.read_csv(
    "dji_30.csv",
 
)
df.set_index("Date", inplace=True)
df.rename(columns={"Adj Close": "AAPL"}, inplace=True)

 
df.drop(["Open", "High", "Low", "Close", "Volume"], axis=1, inplace=True)
main_df = pd.DataFrame()
if main_df.empty:
    main_df = df
else:
    main_df = main_df.join(df, how="outer")
# print(main_df.head())
main_df.to_csv("sp500_joined_closes.csv")
# main_df.plot()
# plt.show()
df_corr = main_df.corr()
# print(df_corr.head())
data = df_corr.values
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
heatmap = ax.pcolor(data, cmap=plt.cm.RdYlGn)
fig.colorbar(heatmap)
ax.set_xticks(np.arange(data.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor=False)
ax.invert_yaxis()
ax.xaxis.tick_top()

column_labels = df_corr.columns
row_labels = df_corr.index
ax.set_xticklabels(column_labels)
ax.set_yticklabels(row_labels)
plt.xticks(rotation=90)
heatmap.set_clim(-1, 1)
# plt.tight_layout()
# plt.show()

# if count % 10 ==0:
#     print(count)

# Calculate 20-day moving average
# df["5ma"] = df["Adj Close"].rolling(window=5).mean()
# df["20ma"] = df["Adj Close"].rolling(window=20).mean()
# df["50ma"] = df["Adj Close"].rolling(window=50).mean()
# # Resample to 10-day intervals for candlestick chart
# df_ohlc = df["Adj Close"].resample("10D").ohlc()
# df_volume = df["Volume"].resample("10D").sum()
# print(df_ohlc.head())

# df_ohlc.reset_index(inplace=True)
# df_ohlc["Date"] = df_ohlc["Date"].map(mdates.date2num)
# df_corr = df.corr()


# fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(10, 8))

# Plot candlestick chart
# candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup="g")

# Plot 20-day moving average
# ax1.plot(df.index, df["5ma"], label="5-day MA", color="blue")
# ax1.plot(df.index, df["20ma"], label="20-day MA", color="green")
# ax1.plot(df.index, df["50ma"], label="50-day MA", color="red")
# ax1.legend(loc="upper left")

# # Format x-axis
# ax1.xaxis_date()
# ax1.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))

# Plot volume bars
# ax2.fill_between(
#     df_volume.index.map(mdates.date2num), df_volume.values, 0, color="blue", alpha=0.5
# )
# ax2.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))

# Adjust layout
# fig.autofmt_xdate()
# plt.tight_layout()
# plt.show()
# Show the plot

hm_days = 7
new_df = pd.read_csv("sp500_joined_closes.csv", index_col=0)
new_df.fillna(0, inplace=True)
# print(113, new_df['AAPL'][2])
# Loop to create new columns
 
ticker = "AAPL"
for i in range(1, hm_days + 1):
    # column_name = f'diff_pct_{i}'
    new_df["{}_{}d".format(ticker, i)] = (
        new_df[ticker].shift(-i) - new_df[ticker]
    ) / new_df[ticker]


new_df.fillna(0, inplace=True)

def buy_sell_hold(*args):
    cols = [col for col in args]
    
    requirement = 0.02
 

    for col in cols:
        # print(82, col)

        if col > requirement:
            return 1
        elif col < -requirement:
            return -1
      

    return 0


# def extract_featuresets():
# Choose the columns you want to use for features
feature_cols = ["1", "2", "3", "4", "5", "6", "7"]

 
new_df["{}_target".format(ticker)] = list(
    map(
        buy_sell_hold,
        new_df["{}_1d".format(ticker)],
        new_df["{}_1d".format(ticker)],
        new_df["{}_1d".format(ticker)],
        new_df["{}_1d".format(ticker)],
        new_df["{}_1d".format(ticker)],
        new_df["{}_1d".format(ticker)],
        new_df["{}_1d".format(ticker)],
    )
)
# new_df = pd.DataFrame(new_df)
vals = new_df["{}_target".format(ticker)].values.tolist()
str_vals = [str(i) for i in vals]

print("Data spread", Counter(str_vals))

# df_vals = new_df.pct_change()
# df_vals = df_vals.replace([np.inf, -np.inf], 0)
# df_vals.fillna(0, inplace=True)

# X = df_vals.values
# y = np.array(signals)

# return X, y, new_df


# extract_featuresets()
