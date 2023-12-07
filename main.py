import sys
from services.data_loader import DataLoader
from services.feature_engineering import FeatureEngineering
from services.signal_generator import SignalGenerator
from services.data_processor import DataProcessor
from services.model_trainer import ModelTrainer


def main():
    hm_days = 7
    # ticker = "AAPL"
    # Check if a ticker symbol is provided as a command line argument
    if len(sys.argv) < 2:
        print("Usage: python your_script.py <ticker>")
        ticker = "AAPL"

    ticker = sys.argv[1]
    print(f"Downloading data for {ticker}")
    new_df = DataLoader().load_csv("stock_dfs/{}.csv".format(ticker))
    
    feature_engineering = FeatureEngineering(hm_days)
    feature_engineering.create_joined_closes(new_df, ticker)
    new_join_data = DataLoader().load_csv("data_join/{}.csv".format(ticker))
    feature_engineering.calculate_diff_pct(new_df, ticker)

    signal_generator = SignalGenerator(requirement=0.02)
    data_processor = DataProcessor(ticker, signal_generator, hm_days)
    X, y = data_processor.process_data(new_df)

    model_trainer = ModelTrainer()
    model_trainer.train_model(X, y)


if __name__ == "__main__":
    main()
