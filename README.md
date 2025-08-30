# MarketDataProvider

**MarketDataProvider** is a modular Python package for retrieving financial market data from multiple sources (brokers). It supports real and mock brokers, making it ideal for both production and testing environments.

---

## Features

- **Pluggable Broker Architecture:** Easily switch between real data sources (e.g., Yahoo Finance) and mock/test brokers.
- **Unified API:** Access price, profile, history, fundamentals, financials, ratios, recommendations, news, and indicators through a single provider interface.
- **Extensible:** Add new brokers by implementing the `BrokerAPI` protocol or inheriting from `BaseBroker`.
- **Mock Support:** Use `MockBroker` for testing without external dependencies.
- **Structured Data:** Uses Pydantic models for type safety and serialization.

---

## Installation

```bash
pip install -e .
```
or from PyPI (when published):
```bash
pip install marketdataprovider
```

---

## Usage

### Basic Example

```python
from marketdataprovider import MarketDataProvider, YFinanceBroker, MockBroker

symbol = "AAPL"

# Real broker (Yahoo Finance)
provider = MarketDataProvider(YFinanceBroker())
print(provider.get_price(symbol))
print(provider.get_profile(symbol))

# Mock broker (for testing)
mock_provider = MarketDataProvider(MockBroker())
print(mock_provider.get_price(symbol))
print(mock_provider.get_profile(symbol))
```

### Demo Script

Run the included demo to see both brokers in action:
```bash
python marketdataprovider/demo_brokers.py
```

---

## Adding a New Broker

1. **Inherit from `BaseBroker`** or implement the `BrokerAPI` protocol.
2. **Override required methods** (e.g., `get_price`, `get_profile`, etc.).
3. **Register your broker** in your application or demo.

Example:
```python
from marketdataprovider.base.broker import BaseBroker

class MyCustomBroker(BaseBroker):
    def get_price(self, symbol: str) -> str:
        # Your implementation here
        return "..."

    # Implement other methods as needed
```

---

## API Reference

### `MarketDataProvider`

- `get_price(symbol: str) -> str`
- `get_profile(symbol: str) -> str`
- `get_history(symbol: str, period: str = "1mo", interval: str = "1d") -> str`
- `get_fundamentals(symbol: str) -> str`
- `get_financials(symbol: str) -> str`
- `get_ratios(symbol: str) -> str`
- `get_recommendations(symbol: str) -> str`
- `get_news(symbol: str, num_stories: int = 3) -> str`
- `get_indicators(symbol: str, period: str = "3mo") -> str`

### Brokers

- **YFinanceBroker:** Real data from Yahoo Finance.
- **MockBroker:** Returns mock data for all methods.

---

## Requirements

- Python 3.12+
- yfinance
- pydantic

---

## Author

Niels Weistra

---

## Acknowledgements

- [yfinance](https://github.com/ranaroussi/yfinance)
- [pydantic](https://github.com/pydantic/pydantic)