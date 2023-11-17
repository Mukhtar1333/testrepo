import yfinance as yf

amd = yf.Ticker("AMD")
amd_data = amd.history(period="1y")

amd_data.head()

print(amd_data)

