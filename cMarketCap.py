#listings_api = "https://api.coinmarketcap.com/v2/listings/"
import requests # package for api calls
from prettytable import PrettyTable
from config import ReplaceWithYourOwnApiKey

listings_api = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/' \
               'listings/latest?sort=market_cap&start=1&limit=5000&convert=USD'

headers = {
  f'content-type': 'application/json',
  'X-CMC_PRO_API_KEY': f'{ReplaceWithYourOwnApiKey}',
}

# make api request and convert to json
listings_data = requests.get(listings_api,headers=headers).json()
listings_data = listings_data['data']
#print(listings_data)

table = PrettyTable()
table.field_names = ['Name', 'Symbol', 'Price', 'Volume', 'MarketCap', 'Change 1h',
                     'Change 24h', 'Change 7d']


for coin in listings_data:

    name = coin['name']
    symbol = coin['symbol']
    coin_data = coin['quote']['USD']

    table.add_row([name,
                   symbol,
                   coin_data['price'],
                   coin_data['volume_24h'],
                   coin_data['market_cap'],
                   coin_data['percent_change_1h'],
                   coin_data['percent_change_24h'],
                   coin_data['percent_change_7d']])

table.sortby = table.field_names[6]
table.reversesort = True
print(table)