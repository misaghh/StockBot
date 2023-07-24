import finnhub
import pandas as pd
import datetime
import matplotlib.pyplot as plt




# Setup Client
finnhub_client = finnhub.Client(api_key="ciu3ac1r01qkv67u3l4gciu3ac1r01qkv67u3l50")

t = input('Enter a valid Ticker: ').upper()


start_date = input("enter your start date: (format m/d/yyyy): ")       # 8/6/2021
startDate_format = datetime.datetime.strptime(start_date, "%m/%d/%Y")
startUnix_time = int(datetime.datetime.timestamp(startDate_format))


end_date = input("enter your end date: (format m/d/yyyy): ")       # 8/6/2021
endDate_format = datetime.datetime.strptime(end_date, "%m/%d/%Y")
endUnix_time = int(datetime.datetime.timestamp(endDate_format))


# res = finnhub_client.stock_candles(t, 'D', startUnix_time, endUnix_time)
# quote = finnhub_client.quote(t) 
# df = pd.DataFrame(res)   # , index=pd.date_range(start=start_date, end=end_date, freq="m")


#gets Data for specific stock and prints it
# def getStockDataCandle(ticker, startDate, endDate):
#     res = finnhub_client.stock_candles(t, 'D', startUnix_time, endUnix_time)
#     quote = finnhub_client.quote(t) 
#     df = pd.DataFrame(res, )
#     df['t'] = pd.to_datetime(df['t'], unit='ms')

#     #create figure
#     plt.figure()

#     #define width of candlestick elements
#     width = .4
#     width2 = .05

#     #define up and down prices
#     up = df[df.c>=df.o]
#     down = df[df.c<df.o]

#     #define colors to use
#     col1 = 'green'
#     col2 = 'red'

#     #plot up prices
#     plt.bar(up.index,up.c-up.o,width,bottom=up.o,color=col1)
#     plt.bar(up.index,up.h-up.c,width2,bottom=up.c,color=col1)
#     plt.bar(up.index,up.l-up.o,width2,bottom=up.o,color=col1)

#     #plot down prices
#     plt.bar(down.index,down.c-down.o,width,bottom=down.o,color=col2)
#     plt.bar(down.index,down.h-down.o,width2,bottom=down.o,color=col2)
#     plt.bar(down.index,down.l-down.c,width2,bottom=down.c,color=col2)

#     #rotate x-axis tick labels
#     plt.xticks(rotation=45, ha='right')

#     #display candlestick chart
#     plt.show()
#     print(df)
#     print(quote)




# getStockDataCandle(t, startUnix_time,endUnix_time)





# # Read the data from the CSV file into a Pandas DataFrame
# data = pd.read_csv("test.csv")


def getDailyReturn(t, startUnix_time, endUnix_time):
    res = finnhub_client.stock_candles(t, 'D', startUnix_time, endUnix_time)
    df = pd.DataFrame(res)
    df['t'] = pd.to_datetime(df['t'], unit='ms')
    # Create a new column "Daily_Return" to store the calculated daily return
    res["Daily_Return"] = 0.0
    # Calculate the daily return for each day and populate the "Daily_Return" column              
    for i in range(len(df)):
        prev_close = df['c'].iloc[i-1]
        current_close = df['c'].iloc[i]
        daily_return = (current_close - prev_close) / prev_close
        df[i, 'Daily_Return'] = daily_return

    # Print the DataFrame with the daily return column
    print(res)
    print(df)

getDailyReturn(t, startUnix_time, endUnix_time)



# PublicKey = '67408876c3c94112d7107ab82baefaea32d4a050a8b386edc4bf564bc68d7cf8'

# TOKEN = 'MTEzMjY5ODI3ODA0ODMyMTY0Nw.GPKD3S.zaK5BhD6qCdUgbHtbS2nG2luxobNb0aMCpg7Q8'