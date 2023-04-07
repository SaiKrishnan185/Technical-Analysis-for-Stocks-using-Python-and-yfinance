import yfinance as yf
import matplotlib.pyplot as plt
import ta

# Define the ticker symbol
ticker = "AAPL"

# Get the data from Yahoo Finance
data = yf.download(ticker, start="2020-01-01", end="2023-04-01")

# Fill NaN values with previous values
data.fillna(method='ffill', inplace=True)

# Calculate the technical indicators
data['SMA20'] = ta.trend.sma_indicator(data['Close'], window=20)
data['SMA50'] = ta.trend.sma_indicator(data['Close'], window=50)
data['RSI'] = ta.momentum.rsi(data['Close'])
data['MACD'] = ta.trend.macd_diff(data['Close'])
data['OBV'] = ta.volume.on_balance_volume(data['Close'], data['Volume'])

# Set figure size and spacing between subplots
fig, axes = plt.subplots(3, 1, figsize=(12, 12), sharex=True, gridspec_kw={'hspace': 0.5})

# Plot the stock price and moving averages
axes[0].plot(data['Close'], label='Close Price')
axes[0].plot(data['SMA20'], label='SMA20')
axes[0].plot(data['SMA50'], label='SMA50')
axes[0].legend(loc='upper left')
axes[0].set_title('Stock Price with Moving Averages')

# Plot the RSI
axes[1].plot(data['RSI'], label='RSI')
axes[1].axhline(y=30, color='r', linestyle='--', label='Oversold')
axes[1].axhline(y=70, color='g', linestyle='--', label='Overbought')
axes[1].legend(loc='upper left')
axes[1].set_title('Relative Strength Index (RSI)')

# Plot the MACD and OBV
axes[2].plot(data['MACD'], label='MACD')
axes[2].plot(data['OBV'], label='OBV')
axes[2].legend(loc='upper left')
axes[2].set_title('Moving Average Convergence Divergence (MACD) and On-Balance Volume (OBV)')

# Set x-axis label and tick size
axes[2].set_xlabel('Date')
axes[2].tick_params(axis='x', labelsize=10)

# Set y-axis labels and tick size
for ax in axes:
    ax.set_ylabel('Price')
    ax.tick_params(axis='y', labelsize=10)

# Add padding between subplots
fig.tight_layout(pad=2)

# Add a title to the overall plot
plt.suptitle(f"{ticker} Technical Analysis", fontsize=16)

# Adjust grid
plt.grid(True)

#Add titles and axis labels
plt.title('Stock Price with Technical Indicators')
plt.xlabel('Date')
plt.ylabel('Price')


plt.show()
