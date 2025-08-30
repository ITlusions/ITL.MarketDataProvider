from setuptools import setup, find_packages

setup(
    name="marketdataprovider",
    version="0.1.0",
    description="Generic market data provider with pluggable brokers",
    author="Niels Weistra",
    packages=find_packages(),
    install_requires=[
        "yfinance>=0.2.37",
        "pydantic>=2.7.1"
    ],
    python_requires=">=3.12",
)