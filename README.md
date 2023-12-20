 

# Project Summary: Automated Financial Data Analysis and Modeling for S&P 500 Stocks

- Developed a Python script to automatically extract S&P 500 tickers from Wikipedia and download corresponding data from Yahoo Finance.
- Efficiently stored data in CSV format for ease of analysis.
- Conducted technical analysis, creating MA 20, MA 50, and candlestick charts to identify market trends.
- Implemented a machine learning model using Python tools like pandas and scikit-learn to predict stock price movements.
- Integrated risk management principles into the predictive model to mitigate potential trading risks.
- Utilized the insights from this analysis to inform algorithmic trading strategy development.

It train a k-nearest neighbors classifier and a voting classifier on  input data, and then evaluating the performance on a test set.

This project collect price of stocks in SP 500 lists. It can draw candle stick plot with Moving Average 5 , 20, 50 days

## generate the requirements.txt file by running the following command:

`pip freeze > requirements.txt`

`source env/bin/activate`

`pip3 install -r requirements.txt`

## To collect data run 

`python3 collect_data.py TSLA` it wil dowload data price of Tesla from 1-1-22 to 12-5-23 and store it in the `stock_dfs` folder 

## to view the plot of moving average run 

`python3 moving_average.py TSLA`

``


## Offers line-by-line profiling, Reports memory consumption for each line:

`kernprof -l -v  moving_average.py TSLA`

## To read the file and display the profiling results. Run the following command:

`python -m line_profiler moving_average.py.lprof`

## Redirect the output to a text file for easier analysis:

`python -m line_profiler moving_average.py.lprof > profile_results.txt` 

## Tracks memory usage moving average file 

`python3 -m memory_profiler  moving_average.py TSLA`

It will drawing moving average with Candle stick of TSLA. 

### To run prediction with KNeighbor run 

`python main.py AAPL`, it will run with Apple company, change the ticker of the company in the second parameter when running this program. 

## Project Structure

```plaintext
project/
|-- data/
|   |-- sp500_joined_closes.csv
|-- services/
|   |-- __init__.py
|   |-- signal_generator.py
|   |-- data_processor.py
|-- main.py
|-- README.md
|-- ...

```

`conda activate myenv`

`pypy`

