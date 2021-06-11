import requests
import config
from datetime import datetime


class Stock:
  def __init__(self, ticker, region):
    self.ticker = ticker
    self.region = region
    self.updated_at = datetime.utcnow()

  def cached(self):
    difference = datetime.utcnow() - self.updated_at
    if (difference.days == 0):
      return True
    else:
      return False

  def getDetails(self):
    details = 'Stock: ' + self.ticker + '\n' + 'Region: ' + self.region
    return details

  def getStockData(self):
    url = config.API_URL
    querystring = {
        'symbol': self.ticker,
        'region': self.region
    }
    headers = {
        'x-rapidapi-key': config.API_KEY,
        'x-rapidapi-host': config.API_HOST
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    return response.text
