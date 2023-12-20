class MovingAverageCalculator:
    def calculate_moving_averages(self, df):
        df["5ma"] = df["Adj Close"].rolling(window=5).mean()
        df["20ma"] = df["Adj Close"].rolling(window=20).mean()
        df["50ma"] = df["Adj Close"].rolling(window=50).mean()
