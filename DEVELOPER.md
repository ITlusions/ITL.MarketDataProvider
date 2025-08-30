# MarketDataProvider Developer Guide

This guide will help you understand, extend, and use the MarketDataProvider package for integrating multiple financial data sources (brokers) in Python.

---

## 1. Package Structure

```
marketdataprovider/
    __init__.py
    models.py
    provider.py
    broker.py
    demo_brokers.py
    setup.py
    README.md
    requirements.txt
    base/
        __init__.py
        broker.py
    brokers/
        finnhub.py
        mock.py
        yahoofinance.py
```

---

## 2. Core Concepts

- **Broker:** A class that implements methods for fetching financial data (e.g., price, profile, history). Examples: `YFinanceBroker`, `MockBroker`, `FinnhubBroker`.
- **MarketDataProvider:** A wrapper that delegates calls to the selected broker.
- **BaseBroker:** Provides default "not implemented" responses for all broker methods.
- **BrokerAPI:** Protocol/interface for broker implementations.
- **Demo Script:** Shows how to use different brokers.

---

## 3. Adding a New Broker

1. **Create a Broker Class**
    - Inherit from `BaseBroker` (in `base/broker.py`) or implement `BrokerAPI` (in `broker.py`).
    - Override methods you want to support.

    ```python
    # filepath: marketdataprovider/brokers/mycustom.py
    from marketdataprovider.base.broker import BaseBroker

    class MyCustomBroker(BaseBroker):
        def get_price(self, symbol: str) -> str:
            # Your implementation here
            return "..."

        # Implement other methods as needed
    ```

2. **Register and Use Your Broker**
    - Pass your broker to `MarketDataProvider`.

    ```python
    from marketdataprovider.provider import MarketDataProvider
    from marketdataprovider.brokers.mycustom import MyCustomBroker

    provider = MarketDataProvider(MyCustomBroker())
    print(provider.get_price("AAPL"))
    ```

---

## 4. Using Existing Brokers

- **YFinanceBroker:** Uses Yahoo Finance via `yfinance` (in `brokers/yahoofinance.py`).
- **MockBroker:** Returns mock data for testing (in `brokers/mock.py`).
- **FinnhubBroker:** Uses Finnhub API (requires API key, in `brokers/finnhub.py`).

Example usage:

```python
from marketdataprovider.provider import MarketDataProvider
from marketdataprovider.broker import YFinanceBroker, MockBroker, FinnhubBroker

provider = MarketDataProvider(YFinanceBroker())
print(provider.get_price("AAPL"))

mock_provider = MarketDataProvider(MockBroker())
print(mock_provider.get_price("AAPL"))

finnhub_provider = MarketDataProvider(FinnhubBroker("YOUR_FINNHUB_API_KEY"))
print(finnhub_provider.get_price("AAPL"))
```

---

## 5. Demo Script

Run the demo to see all brokers in action:

```bash
python marketdataprovider/demo_brokers.py
```

**Example output:**
```python
--- Data for AAPL using YFinanceBroker ---
Current Price: ...
Company Profile: ...
...
--- Data for AAPL using MockBroker ---
Current Price: ...
...
--- Data for AAPL using FinnhubBroker ---
Current Price: ...
...
```

---

## 6. Extending Functionality

- Add new methods to `BaseBroker` and `BrokerAPI` as needed.
- Implement those methods in your broker classes.
- Update `MarketDataProvider` if you add new broker methods.

---

## 7. Error Handling

- If a broker method is not implemented, it returns a "not implemented" string (from `BaseBroker`).
- Handle errors gracefully in your broker implementations (e.g., try/except, return error messages).

---

## 8. Configuration

- Store sensitive data (like API keys) in environment variables or config files.
- Do not hardcode secrets in your code.

---

## 9. Requirements

- Python 3.12+
- yfinance
- pydantic
- finnhub-python (for FinnhubBroker)

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 10. Conventions

- Use descriptive method names.
- Document your broker classes and methods.
- Follow PEP8 for code style.

---

## 11. Example: Implementing a Broker

```python
# filepath: marketdataprovider/brokers/example.py
from marketdataprovider.base.broker import BaseBroker

class ExampleBroker(BaseBroker):
    def get_price(self, symbol: str) -> str:
        # Fetch price from your data source
        return "100.00"
```

---

## 12. File Overview

- **models.py:** Contains Pydantic models for structured data (`CompanyInfo`, `Fundamentals`).
- **provider.py:** Main provider class that delegates to a broker.
- **broker.py:** Protocol and broker implementations (may import from `brokers/`).
- **base/broker.py:** Base class with default "not implemented" methods.
- **brokers/:** Folder for individual broker implementations.
- **demo_brokers.py:** Demo script to show usage of all brokers.
- **setup.py:** Package setup for pip installation.
- **README.md:** Main documentation.

---

## 13. Implementing a Custom Broker Outside the Package

You can implement a custom broker in your own project, outside the package, by inheriting from `BaseBroker` or implementing `BrokerAPI`.

**Example:**

```python
from marketdataprovider.base.broker import BaseBroker
from marketdataprovider import MarketDataProvider

class MyExternalBroker(BaseBroker):
    def get_price(self, symbol: str) -> str:
        # Custom logic, e.g., fetch from your own API
        return f"Custom price for {symbol}: 42.00"

    # Optionally override other methods

# Usage
provider = MarketDataProvider(MyExternalBroker())
print(provider.get_price("AAPL"))
```

No need to modify the package itself—just import and use!

---

## 14. Further Reading

- See [README.md](README.md) for more details and API reference.
- Refer to broker-specific documentation (e.g., [Finnhub API](https://finnhub.io/docs/api)) for integration details.

---