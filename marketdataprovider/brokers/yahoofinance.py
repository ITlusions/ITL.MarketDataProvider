import json
from models import CompanyInfo, Fundamentals
from base.broker import BaseBroker

class YFinanceBroker(BaseBroker):
    """Broker implementation using yfinance."""
    def __init__(self):
        try:
            import yfinance as yf
            self.yf = yf
        except ImportError:
            raise ImportError('Please install the yfinance package using pip install -U yfinance')

    def get_price(self, symbol: str) -> str:
        try:
            stock = self.yf.Ticker(symbol)
            current_price = stock.info.get("regularMarketPrice", stock.info.get("currentPrice"))
            if current_price is not None:
                return f"{current_price:.4f}"
            return json.dumps({"error": f"Could not fetch current price for {symbol}"})
        except Exception as e:
            return json.dumps({"error": f"Error fetching current price for {symbol}: {e}"})

    def get_profile(self, symbol: str) -> str:
        try:
            info = self.yf.Ticker(symbol).info
            if not info:
                return json.dumps({"error": f"Could not fetch company info for {symbol}"})
            company_info = CompanyInfo(
                Name=info.get("shortName"),
                Symbol=info.get("symbol"),
                CurrentStockPrice=f"{info.get('regularMarketPrice', info.get('currentPrice'))} {info.get('currency', 'USD')}",
                MarketCap=f"{info.get('marketCap', info.get('enterpriseValue'))} {info.get('currency', 'USD')}",
                Sector=info.get("sector"),
                Industry=info.get("industry"),
                Address=info.get("address1"),
                City=info.get("city"),
                State=info.get("state"),
                Zip=info.get("zip"),
                Country=info.get("country"),
                EPS=info.get("trailingEps"),
                PERatio=info.get("trailingPE"),
                WeekLow52=info.get("fiftyTwoWeekLow"),
                WeekHigh52=info.get("fiftyTwoWeekHigh"),
                DayAverage50=info.get("fiftyDayAverage"),
                DayAverage200=info.get("twoHundredDayAverage"),
                Website=info.get("website"),
                Summary=info.get("longBusinessSummary"),
                AnalystRecommendation=info.get("recommendationKey"),
                NumberOfAnalystOpinions=info.get("numberOfAnalystOpinions"),
                Employees=info.get("fullTimeEmployees"),
                TotalCash=info.get("totalCash"),
                FreeCashflow=info.get("freeCashflow"),
                OperatingCashflow=info.get("operatingCashflow"),
                EBITDA=info.get("ebitda"),
                RevenueGrowth=info.get("revenueGrowth"),
                GrossMargins=info.get("grossMargins"),
                EbitdaMargins=info.get("ebitdaMargins"),
            )
            return json.dumps(company_info.model_dump(), indent=4)
        except Exception as e:
            return json.dumps({"error": f"Error fetching company profile for {symbol}: {e}"})

    def get_history(self, symbol: str, period: str = "1mo", interval: str = "1d") -> str:
        try:
            stock = self.yf.Ticker(symbol)
            historical_price = stock.history(period=period, interval=interval)
            if historical_price.empty:
                return json.dumps({"error": f"No historical data found for {symbol}"})
            return historical_price.to_json(orient="index")
        except Exception as e:
            return json.dumps({"error": f"Error fetching historical prices for {symbol}: {e}"})

    def get_fundamentals(self, symbol: str) -> str:
        try:
            info = self.yf.Ticker(symbol).info
            fundamentals = Fundamentals(
                symbol=symbol,
                company_name=info.get("longName", ""),
                sector=info.get("sector", ""),
                industry=info.get("industry", ""),
                market_cap=info.get("marketCap", "N/A"),
                pe_ratio=info.get("forwardPE", "N/A"),
                pb_ratio=info.get("priceToBook", "N/A"),
                dividend_yield=info.get("dividendYield", "N/A"),
                eps=info.get("trailingEps", "N/A"),
                beta=info.get("beta", "N/A"),
                week_high_52=info.get("fiftyTwoWeekHigh", "N/A"),
                week_low_52=info.get("fiftyTwoWeekLow", "N/A"),
            )
            return json.dumps(fundamentals.model_dump(), indent=2)
        except Exception as e:
            return json.dumps({"error": f"Error getting fundamentals for {symbol}: {e}"})

    def get_financials(self, symbol: str) -> str:
        try:
            financials = self.yf.Ticker(symbol).financials
            if financials.empty:
                return json.dumps({"error": f"No income statements found for {symbol}"})
            return financials.to_json(orient="index")
        except Exception as e:
            return json.dumps({"error": f"Error fetching income statements for {symbol}: {e}"})

    def get_ratios(self, symbol: str) -> str:
        try:
            key_ratios = self.yf.Ticker(symbol).info
            return json.dumps(key_ratios, indent=2)
        except Exception as e:
            return json.dumps({"error": f"Error fetching key financial ratios for {symbol}: {e}"})

    def get_recommendations(self, symbol: str) -> str:
        try:
            recommendations = self.yf.Ticker(symbol).recommendations
            if recommendations is None or recommendations.empty:
                return json.dumps({"error": f"No analyst recommendations found for {symbol}"})
            return recommendations.to_json(orient="index")
        except Exception as e:
            return json.dumps({"error": f"Error fetching analyst recommendations for {symbol}: {e}"})

    def get_news(self, symbol: str, num_stories: int = 3) -> str:
        try:
            news = self.yf.Ticker(symbol).news
            if not news:
                return json.dumps({"error": f"No news found for {symbol}"})
            return json.dumps(news[:num_stories], indent=2)
        except Exception as e:
            return json.dumps({"error": f"Error fetching company news for {symbol}: {e}"})

    def get_indicators(self, symbol: str, period: str = "3mo") -> str:
        try:
            indicators = self.yf.Ticker(symbol).history(period=period)
            if indicators.empty:
                return json.dumps({"error": f"No technical indicators found for {symbol}"})
            return indicators.to_json(orient="index")
        except Exception as e:
            return json.dumps({"error": f"Error fetching technical indicators for {symbol}: {e}"})
