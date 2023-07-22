import finnhub
import pandas as pd
import datetime
import time

# Setup Client
finnhub_client = finnhub.Client(api_key="ciu3ac1r01qkv67u3l4gciu3ac1r01qkv67u3l50")

# res = finnhub_client.stock_candles('AAPL', 'D', 1590988249, 1591852249)

# print(pd.DataFrame(finnhub_client.symbol_lookup('apple')))

t = input('Enter a valid Ticker: ').upper()


start_date = input("enter your start date: (format m/d/yyyy): ")       # 8/6/2021
startDate_format = datetime.datetime.strptime(start_date, "%m/%d/%Y")
startUnix_time = int(datetime.datetime.timestamp(startDate_format))


end_date = input("enter your end date: (format m/d/yyyy): ")       # 8/6/2021
endDate_format = datetime.datetime.strptime(end_date, "%m/%d/%Y")
endUnix_time = int(datetime.datetime.timestamp(endDate_format))



res = finnhub_client.stock_candles(t, 'D', startUnix_time, endUnix_time)
print(pd.DataFrame(res))