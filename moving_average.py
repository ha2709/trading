import os, sys
import matplotlib.pyplot as plt
from services.data_loader import DataLoader
from services.moving_average_calculator import MovingAverageCalculator
from services.resampler import Resampler
from services.plotter import Plotter
from services.visualization import Visualization


def main():
    # Get stock symbol from the terminal
    if len(sys.argv) != 2:
        print("Usage: python main.py <stock_symbol>")
        sys.exit(1)

    symbol = sys.argv[1].upper()
    filename = f"{symbol}.csv"
    data_folder = "stock_dfs"


    # Check if the CSV file exists in the stock_dfs folder
    file_path = os.path.join(data_folder, filename)
    if not os.path.exists(file_path):
        print(f"Data for {symbol} not found. Downloading...")
        
        # Download data and store it
        DataLoader.download_data(symbol, data_folder)
    print(28, file_path)
    # Load data
    data_loader = DataLoader()
    df = data_loader.load_data(file_path)
    if df is None:
        print(f"Error loading data for {symbol}. Please check the stock symbol.")
        sys.exit(1)
    # Calculate moving averages
    ma_calculator = MovingAverageCalculator()
    ma_calculator.calculate_moving_averages(df)

    # Resample data
    resampler = Resampler()
    df_ohlc, df_volume = resampler.resample_data(df)

    # Plot data
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(10, 8))
    plotter = Plotter()
    plotter.plot_candlestick_chart(ax1, df_ohlc)
    plotter.plot_moving_averages(ax1, df)
    plotter.plot_volume_bars(ax2, df_volume)

    # Format and show the plot
    vis = Visualization()
    vis.show_plot()


if __name__ == "__main__":
    main()
