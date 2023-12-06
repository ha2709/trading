import bs4 as bs
import pickle
import requests
import datetime as dt
import os
import yfinance as yf
import pandas_datareader.data as web

def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text)
    # print(8, soup)
    table = soup.find('table', {'class': 'wikitable sortable'} )
    # print(9, table)
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)

    with open("sp500tickers.pickle", "wb") as f:
        pickle.dump(tickers, f)
    # print(tickers)
    return tickers
    # print(8, soup)
save_sp500_tickers()

def get_data_from_yahoo(reload_sp500 = False):
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open("sp500tickers.pickle", "rb") as f:
            tickers = pickle.load(f)

    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')

    start = dt.datetime(2022,1,1)
    end = dt.datetime(2023,12,5)

    for ticker in tickers:
        print(41, ticker)
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
            # df = web.DataReader(ticker, 'yahoo', start, end )
            df = yf.download(ticker, start=start, end=end)
            df.to_csv('stock_dfs/{}.csv'.format(ticker))
        else:
            print('ALready have {}'.format(ticker))

get_data_from_yahoo()