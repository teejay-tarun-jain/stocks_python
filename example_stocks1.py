#Connects yfinance and gets historical data for stock daily price
import yfinance as yf

msft = yf.Ticker("MSFT")
print(msft)

print(msft.info)

print(msft.history(period="max"))
