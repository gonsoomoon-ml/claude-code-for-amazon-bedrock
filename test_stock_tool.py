import sys
sys.path.insert(0, '.')
from tools.stock_tool import get_stock_price

# Test with Apple stock
result = get_stock_price('AAPL')
print(f'Symbol: {result["symbol"]}')
print(f'Name: {result["name"]}')
print(f'Price: {result["current_price"]} {result["currency"]}')
