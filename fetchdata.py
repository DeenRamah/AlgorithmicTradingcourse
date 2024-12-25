//use the yfinance library
import yfinance as yf
data = yf.download('AAPL', start='2022-02-13', end='2024-02-13')
print(data.head())
