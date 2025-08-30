import json
from ..models import CompanyInfo, Fundamentals
from ..base.broker import BaseBroker

class MockBroker(BaseBroker):
    """Mock broker for testing purposes."""
    def get_price(self, symbol: str) -> str:
        return "123.45"

    def get_profile(self, symbol: str) -> str:
        mock_info = CompanyInfo(
            Name="Mock Company",
            Symbol=symbol,
            CurrentStockPrice="123.45 USD",
            MarketCap="1000000 USD",
            Sector="Technology",
            Industry="Software",
            Address="123 Mock St",
            City="Mockville",
            State="MO",
            Zip="12345",
            Country="Neverland",
            EPS=1.23,
            PERatio=15.6,
            WeekLow52=100.0,
            WeekHigh52=150.0,
            DayAverage50=120.0,
            DayAverage200=110.0,
            Website="https://mockcompany.com",
            Summary="This is a mock company for testing.",
            AnalystRecommendation="buy",
            NumberOfAnalystOpinions=5,
            Employees=100,
            TotalCash=500000.0,
            FreeCashflow=100000.0,
            OperatingCashflow=200000.0,
            EBITDA=300000.0,
            RevenueGrowth=0.05,
            GrossMargins=0.4,
            EbitdaMargins=0.3,
        )
        return json.dumps(mock_info.model_dump(), indent=4)

    def get_history(self, symbol: str, period: str = "1mo", interval: str = "1d") -> str:
        return json.dumps({"mock_history": True, "symbol": symbol, "period": period, "interval": interval})

    def get_fundamentals(self, symbol: str) -> str:
        mock_fundamentals = Fundamentals(
            symbol=symbol,
            company_name="Mock Company",
            sector="Technology",
            industry="Software",
            market_cap=1000000,
            pe_ratio=15.6,
            pb_ratio=2.5,
            dividend_yield=0.01,
            eps=1.23,
            beta=1.0,
            week_high_52=150.0,
            week_low_52=100.0,
        )
        return json.dumps(mock_fundamentals.model_dump(), indent=2)

    def get_financials(self, symbol: str) -> str:
        return json.dumps({"mock_financials": True, "symbol": symbol})

    def get_ratios(self, symbol: str) -> str:
        return json.dumps({"mock_ratios": True, "symbol": symbol})

    def get_recommendations(self, symbol: str) -> str:
        return json.dumps({"mock_recommendations": True, "symbol": symbol})

    def get_news(self, symbol: str, num_stories: int = 3) -> str:
        return json.dumps([{"title": f"Mock News {i+1}", "symbol": symbol} for i in range(num_stories)], indent=2)

    def get_indicators(self, symbol: str, period: str = "3mo") -> str:
        return json.dumps({"mock_indicators": True, "symbol": symbol, "period": period})