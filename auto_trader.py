import os
import time

import yfinance as yf
from alpaca_trade_api.rest import REST


class MovingAverageTrader:
    """Simple moving average trading example using Alpaca API."""

    def __init__(self, symbol: str, window: int = 20):
        self.symbol = symbol
        self.window = window
        self.api = REST(
            os.getenv("ALPACA_API_KEY"),
            os.getenv("ALPACA_SECRET_KEY"),
            os.getenv("ALPACA_BASE_URL", "https://paper-api.alpaca.markets"),
        )

    def latest_price(self) -> float:
        data = yf.Ticker(self.symbol).history(period="1d", interval="1m")
        return float(data["Close"].iloc[-1])

    def moving_average(self) -> float:
        data = yf.Ticker(self.symbol).history(period=f"{self.window}m", interval="1m")
        return float(data["Close"].rolling(self.window).mean().iloc[-1])

    def trade(self):
        price = self.latest_price()
        ma = self.moving_average()
        side = "buy" if price > ma else "sell"
        self.api.submit_order(
            symbol=self.symbol,
            qty=1,
            side=side,
            type="market",
            time_in_force="day",
        )
        print(f"{side.capitalize()} {self.symbol} at {price:.2f}")


def main():
    symbol = os.getenv("TRADE_SYMBOL", "AAPL")
    trader = MovingAverageTrader(symbol)
    while True:
        try:
            trader.trade()
            time.sleep(60)
        except Exception as exc:
            print(f"Error during trade: {exc}")
            time.sleep(60)


if __name__ == "__main__":
    main()
