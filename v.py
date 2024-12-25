//visualizing indicators
import pandas as pd
import matplotlib.pyplot as plt

//fetching stock data (eg, CSV or API)
data =pd.read_cvs(stock_data.cvs)
data['SMA_20'] = data['Close'].rolling(window=20).mean()
data['SMA_20'] = data['Close'].ewm(span=20, adjus=False).mean()

plt.figure(figsize=(10,6))
plt.plot(data['Close'], label='Close Price', color='blue')
plt.plot(data['SMA_20'], label='20-Day SMA', color='red')
plt.plot(data['EMA_20'], label='20-Day EMA', color='green')
plt.title('SMA and EMA Example')
plt.legend()
plt.show()
