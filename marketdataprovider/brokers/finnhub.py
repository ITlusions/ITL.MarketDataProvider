import json
import finnhub
from models import CompanyInfo, Fundamentals
from base.broker import BaseBroker

class FinnhubBroker(BaseBroker):
    """Broker implementation using Finnhub API."""

    def __init__(self, api_key: str):
        self.client = finnhub.Client(api_key=api_key)

    def get_price(self, symbol: str) -> str:
        try:
            quote = self.client.quote(symbol)
            price = quote.get('c')
            return f"{price:.4f}" if price else json.dumps({"error": f"Could not fetch price for {symbol}"})
        except Exception as e:
            return json.dumps({"error": f"Error fetching price for {symbol}: {e}"})

    def get_profile(self, symbol: str) -> str:
        try:
            profile = self.client.company_profile2(symbol=symbol)
            company_info = CompanyInfo(
                Name=profile.get("name"),
                Symbol=symbol,
                Sector=profile.get("finnhubIndustry"),
                Industry=profile.get("finnhubIndustry"),
                Website=profile.get("weburl"),
                Summary=profile.get("description"),
                # Add other fields as available
            )
            return json.dumps(company_info.model_dump(), indent=4)
        except Exception as e:
            return json.dumps({"error": f"Error fetching profile for {symbol}: {e}"})

    def get_history(self, symbol: str, period: str = "1mo", interval: str = "1d") -> str:
        # Finnhub uses UNIX timestamps for historical data
        import time
        from datetime import datetime, timedelta

        try:
            now = int(time.time())
            if period == "1mo":
                start = int((datetime.now() - timedelta(days=30)).timestamp())
            else:
                start = int((datetime.now() - timedelta(days=7)).timestamp())
            res = self.client.stock_candles(symbol, interval, start, now)
            return json.dumps(res, indent=2)
        except Exception as e:
            return json.dumps({"error": f"Error fetching history for {symbol}: {e}"})

    def get_fundamentals(self, symbol: str) -> str:
        try:
            metrics = self.client.company_basic_financials(symbol, 'all')
            fundamentals = Fundamentals(
                symbol=symbol,
                company_name=metrics.get("name"),
                sector=metrics.get("sector"),
                industry=metrics.get("industry"),
                market_cap=metrics.get("marketCapitalization"),
                pe_ratio=metrics.get("peBasicExclExtraTTM"),
                pb_ratio=metrics.get("pbAnnual"),
                dividend_yield=metrics.get("dividendYieldIndicatedAnnual"),
                eps=metrics.get("epsBasicExclExtraItemsTTM"),
                beta=metrics.get("beta"),
                week_high_52=metrics.get("52WeekHigh"),
                week_low_52=metrics.get("52WeekLow"),
            )
            return json.dumps(fundamentals.model_dump(), indent=2)
        except Exception as e:
            return json.dumps({"error": f"Error fetching fundamentals for {symbol}: {e}"})

    # Implement other methods as needed, following Finnhub API docs.