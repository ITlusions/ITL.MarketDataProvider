from broker import YFinanceBroker, MockBroker, FinnhubBroker
from provider import MarketDataProvider

def show_data(provider, symbol):
    print(f"--- Data for {symbol} using {provider.broker.__class__.__name__} ---")
    print("Current Price:", provider.get_price(symbol))
    print("Company Profile:", provider.get_profile(symbol))
    print("Historical Prices:", provider.get_history(symbol))
    print("Fundamentals:", provider.get_fundamentals(symbol))
    print("Financials:", provider.get_financials(symbol))
    print("Ratios:", provider.get_ratios(symbol))
    print("Recommendations:", provider.get_recommendations(symbol))
    print("News:", provider.get_news(symbol, num_stories=2))
    print("Indicators:", provider.get_indicators(symbol))
    print("NotImplemented:", provider.broker.test(symbol))
    print()

def main():
    symbol = "AAPL"

    # Real broker: Yahoo Finance
    yf_provider = MarketDataProvider(YFinanceBroker())
    show_data(yf_provider, symbol)

    # Mock broker
    mock_provider = MarketDataProvider(MockBroker())
    show_data(mock_provider, symbol)

    # Finnhub broker (requires API key)
    api_key = "YOUR_FINNHUB_API_KEY"
    finnhub_provider = MarketDataProvider(FinnhubBroker(api_key))
    show_data(finnhub_provider, symbol)

if __name__ == "__main__":
    main()