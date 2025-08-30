from abc import ABC

class BaseBroker(ABC):
    broker_name: str = "BaseBroker"

    def get_price(self, symbol: str) -> str:
        """Return the latest price for the symbol or 'not implemented'."""
        return f"not implemented: get_price for {symbol}"

    def get_profile(self, symbol: str) -> str:
        """Return the company profile or 'not implemented'."""
        return f"not implemented: get_profile for {symbol}"

    def get_history(self, symbol: str, period: str = "1mo", interval: str = "1d") -> str:
        """Return historical prices or 'not implemented'."""
        return f"not implemented: get_history for {symbol}"

    def get_fundamentals(self, symbol: str) -> str:
        """Return fundamentals or 'not implemented'."""
        return f"not implemented: get_fundamentals for {symbol}"

    def get_financials(self, symbol: str) -> str:
        """Return financials or 'not implemented'."""
        return f"not implemented: get_financials for {symbol}"

    def get_ratios(self, symbol: str) -> str:
        """Return ratios or 'not implemented'."""
        return f"not implemented: get_ratios for {symbol}"

    def get_recommendations(self, symbol: str) -> str:
        """Return recommendations or 'not implemented'."""
        return f"not implemented: get_recommendations for {symbol}"

    def get_news(self, symbol: str, num_stories: int = 3) -> str:
        """Return news or 'not implemented'."""
        return f"not implemented: get_news for {symbol}"

    def get_indicators(self, symbol: str, period: str = "3mo") -> str:
        """Return indicators or 'not implemented'."""
        return f"not implemented: get_indicators for {symbol}"
    
    def test(self, symbol: str) -> str:
        """Test method to demonstrate NotImplementedError."""
        return f"Test method called from {self.broker_name} is not implemented in {self.__class__.__name__}."