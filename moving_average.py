import matplotlib.pyplot as plt
from services.data_loader import DataLoader
from services.moving_average_calculator import MovingAverageCalculator
from services.resampler import Resampler
from services.plotter import Plotter
from services.visualization import Visualization


def main():
    start_date = "2022-01-01"
    end_date = "2023-12-5"
    symbol = "DIA"
    filename = "dji_30.csv"

    # Load data
    data_loader = DataLoader()
    df = data_loader.load_data(filename)

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
