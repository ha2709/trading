 

# Prediction on Price of SP 500

This project collect price of stocks in SP 500 lists. It can draw candle stick plot with Moving Average 5 , 20, 50 days

## generate the requirements.txt file by running the following command:

`pip freeze > requirements.txt`

`source env/bin/activate`

`pip3 install -r requirements.txt`

## To collect data run 

`python3 collect_data.py`

## to view the plot of moving average run 

`python3 moving_average.py`

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
