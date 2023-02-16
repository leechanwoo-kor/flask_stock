import yfinance as yf

tesla = yf.Ticker("TSLA")
df = tesla.history(period="max")
df = df.tail(120)
print(df)