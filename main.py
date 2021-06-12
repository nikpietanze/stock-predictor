from stocks import Stock
import pandas as pd
import matplotlib.pyplot as plt
import os.path
import json

stocks_of_interest = {
  'GME': Stock('GME', 'US'),
  'AMC': Stock('AMC', 'US'),
  'BB': Stock('BB', 'US'),
  'TSLA': Stock('TSLA', 'US'),
  'AAPL': Stock('AAPL', 'US'),
  'NVDA': Stock('NVDA', 'US'),
  'MSFT': Stock('MSFT', 'US'),
  'AMZN': Stock('AMZN', 'US'),
  'NET': Stock('NET', 'US'),
  'TECH': Stock('TECH', 'US'),
  'TME': Stock('TME', 'US'),
  'PINS': Stock('PINS', 'US'),
  'CAG': Stock('CAG', 'US'),
  'ICLN': Stock('ICLN', 'US'),
  'PLTR': Stock('PLTR', 'US'),
  'NIO': Stock('NIO', 'US'),
  'TLRY': Stock('TLRY', 'US'),
  'BABA': Stock('BABA', 'US'),
  'ACB': Stock('ACB', 'US'),
  'ARKG': Stock('ARKG', 'US'),
  'MT': Stock('MT', 'US'),
  'WISH': Stock('WISH', 'US'),
  'QS': Stock('QS', 'US'),
  'BBBY': Stock('BBBY', 'US'),
  'TAN': Stock('TAN', 'US'),
  'GLD': Stock('GLD', 'US'),
  'FB': Stock('FB', 'US'),
  'SQ': Stock('SQ', 'US'),
  'QQQ': Stock('QQQ', 'US'),
  'SLV': Stock('SLV', 'US'),
  'AMD': Stock('AMD', 'US'),
  'DKNG': Stock('DKNG', 'US'),
  'CAG': Stock('CAG', 'US')
}

for s in stocks_of_interest:
  stock = stocks_of_interest[s]
  if (not os.path.isfile('./data/' + stock.ticker + '.json') or not stock.cached()):
    stock_data = stock.getStockData()

    with open('./data/' + stock.ticker + '.json', 'w') as f:
      f.write(stock_data + '\n')

  f = open('./data/' + stock.ticker + '.json')
  json_data = json.load(f)

  data = pd.json_normalize(json_data)
  df = pd.DataFrame(data['prices'][0])

  data_high = df.drop(columns=['open', 'low', 'close', 'volume', 'adjclose'])
  plt.plot(data_high.date, data_high.high, marker='o')
  plt.xlabel('Date')
  plt.ylabel('Price')
  plt.title(stock.ticker + ' Daily Highs')
  plt.show()
