from collections import Counter


class SignalGenerator:
    def __init__(self, requirement):
        self.requirement = requirement

    def buy_sell_hold(self, *args):
        cols = [col for col in args]
        for col in cols:
            if col > self.requirement:
                return 1
            elif col < -self.requirement:
                return -1
        return 0
