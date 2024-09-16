import yfinance

msft = yfinance.Ticker("AAPL").history(
                period = "1d",
                interval = '1h',
                start='2024-01-01',
                end='2024-01-03',
                prepost=True
            )

print(msft.head())