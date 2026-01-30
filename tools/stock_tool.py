import yfinance as yf
from strands import tool


@tool
def get_stock_price(symbol: str) -> dict:
    """
    Get the current stock price for a given symbol.

    Args:
        symbol: Stock ticker symbol (e.g., "AAPL", "TSLA", "GOOGL")

    Returns:
        Dictionary containing stock name, current price, and currency
    """
    ticker = yf.Ticker(symbol)
    info = ticker.info

    return {
        "symbol": symbol.upper(),
        "name": info.get("shortName", "N/A"),
        "current_price": info.get("currentPrice") or info.get("regularMarketPrice"),
        "currency": info.get("currency", "USD"),
    }
