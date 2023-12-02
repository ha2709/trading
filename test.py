import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web
import yfinance as yf
matplotlib.use('TkAgg')  # Use 'TkAgg' backend (replace with 'Qt5Agg' or 'Agg' if needed)

# start = '2022-01-01'
# end = '2022-12-31'

symbol = 'TSLA'
# df = yf.download(symbol, start=start, end=end)
# df.to_csv('tsla.csv')
df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0, date_parser=lambda x: pd.to_datetime(x, format='%Y-%m-%d'))
# df['100ma'] = df['Adj Close'].rolling(window=100, min_periods = 0).mean()
df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()
print(df_ohlc.head())

df_ohlc.reset_index(inplace=True)
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

# df.dropna(inplace=True)
# print(df.tail())
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan= 1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=5, colspan= 1, sharex =ax1)
ax1.xaxis_date()
candlestick_ohlc(ax1, df_ohlc.values, width =2, colorup ='g')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)
# ax1.plot(df.index, df['Adj Close'])
# ax1.plot(df.index, df['100ma'])
# ax2.bar(df.index, df['Volume'])
plt.show()
# Plotting
# plt.figure(figsize=(10, 6))
# plt.plot(df.index, df['Adj Close'], label='Close Price')
# plt.title(f'{symbol} Stock Price (Historical)')
# plt.xlabel('Date')
# plt.ylabel('Close Price')
# plt.legend()
# plt.grid(True)
# # plt.savefig('stock_plot.png')
# plt.show()

# print(df[['Open', 'High']].head())