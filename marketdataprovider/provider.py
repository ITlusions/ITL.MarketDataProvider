from .broker import BrokerAPI

class MarketDataProvider:
    """Generic market data provider that can use any broker API."""
    def __init__(self, broker: BrokerAPI):
        self.broker = broker

    def get_price(self, symbol: str) -> str:
        return self.broker.get_price(symbol)

    def get_profile(self, symbol: str) -> str:
        return self.broker.get_profile(symbol)

    def get_history(self, symbol: str, period: str = "1mo", interval: str = "1d") -> str:
        return self.broker.get_history(symbol, period, interval)

    def get_fundamentals(self, symbol: str) -> str:
        return self.broker.get_fundamentals(symbol)

    def get_financials(self, symbol: str) -> str:
        return self.broker.get_financials(symbol)

    def get_ratios(self, symbol: str) -> str:
        return self.broker.get_ratios(symbol)

    def get_recommendations(self, symbol: str) -> str:
        return self.broker.get_recommendations(symbol)

    def get_news(self, symbol: str, num_stories: int = 3) -> str:
        return self.broker.get_news(symbol, num_stories)

    def get_indicators(self, symbol: str, period: str = "3mo") -> str:
        return self.broker.get_indicators(symbol, period)