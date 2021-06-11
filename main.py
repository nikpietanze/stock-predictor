from stocks import Stock
import pandas as pd
import os.path
import json


GME = Stock('GME', 'US')

if (not os.path.isfile('./data/' + GME.ticker + '.json') or not GME.cached()):
  print('File doesn\'t exist or cache is expired...updating file')
  stock_data = GME.getStockData()

  with open('./data/' + GME.ticker + '.json', 'w') as f:
    f.write(stock_data + '\n')

f = open('./data/' + GME.ticker + '.json')
GME_json_data = json.load(f)

GME_data = pd.json_normalize(GME_json_data)
df = pd.DataFrame(GME_data['prices'][0])
print(df)
