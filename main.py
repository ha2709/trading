from services.data_loader import DataLoader
from services.feature_engineering import FeatureEngineering
from services.signal_generator import SignalGenerator
from services.data_processor import DataProcessor
from services.model_trainer import ModelTrainer


def main():
    hm_days = 7
    new_df = DataLoader().load_csv("sp500_joined_closes.csv")

    ticker = "AAPL"

    feature_engineering = FeatureEngineering(hm_days)
    feature_engineering.calculate_diff_pct(new_df, ticker)

    signal_generator = SignalGenerator(requirement=0.02)
    data_processor = DataProcessor(ticker, signal_generator, hm_days)
    X, y = data_processor.process_data(new_df)

    model_trainer = ModelTrainer()
    model_trainer.train_model(X, y)


if __name__ == "__main__":
    main()
