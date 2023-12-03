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

start = '2022-01-01'
end = '2023-12-1'

symbol = 'DIA'
# df = yf.download(symbol, start=start, end=end)
# df.to_csv('dji_30.csv')
df = pd.read_csv('dji_30.csv', parse_dates=True, index_col=0, date_parser=lambda x: pd.to_datetime(x, format='%Y-%m-%d'))
 
# Calculate 20-day moving average
df['5ma'] = df['Adj Close'].rolling(window=5).mean()
df['20ma'] = df['Adj Close'].rolling(window=20).mean()
df['50ma'] = df['Adj Close'].rolling(window=50).mean()
# Resample to 10-day intervals for candlestick chart
df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()
# print(df_ohlc.head())

df_ohlc.reset_index(inplace=True)
df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

# Create subplots
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(10, 8))

# Plot candlestick chart
candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')

# Plot 20-day moving average
ax1.plot(df.index, df['5ma'], label='50-day MA', color='blue')
ax1.plot(df.index, df['20ma'], label='20-day MA', color='green')
ax1.plot(df.index, df['50ma'], label='50-day MA', color='red')
ax1.legend(loc='upper left')

# Format x-axis
ax1.xaxis_date()
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

# Plot volume bars
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0, color='blue', alpha=0.5)
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

# Adjust layout
fig.autofmt_xdate()
plt.tight_layout()

# Show the plot
plt.show()