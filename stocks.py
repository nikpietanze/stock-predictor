import requests
import config


class Stock:
  def __init__(self, symbol, region):
    self.symbol = symbol
    self.region = region

  def getDetails(self):
    details = 'Stock: ' + self.symbol + '\n' + 'Region: ' + self.region
    return details

  def getStockData(self):
    url = config.API_URL
    querystring = {
        'symbol': self.symbol,
        'region': self.region
    }
    headers = {
        'x-rapidapi-key': config.API_KEY,
        'x-rapidapi-host': config.API_HOST
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    return response.text
