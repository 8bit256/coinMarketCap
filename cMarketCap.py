#listings_api = "https://api.coinmarketcap.com/v2/listings/"
import requests # package for HTTP requests
from prettytable import PrettyTable
from config import ReplaceWithYourOwnApiKey

#url for the latest listings in USD
listings_api = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?sort=market_cap&start=1&limit=5000&convert=USD'

headers = {
  f'content-type': 'application/json',
  'X-CMC_PRO_API_KEY': f'{ReplaceWithYourOwnApiKey}',
}

# make an api request and convert to json
listings_data = requests.get(listings_api,headers=headers).json()

# extract data object
listings_data = listings_data['data']
#print(listings_data[0], sep='\n') # print first data item


table = PrettyTable()
#create table headings 9 in total
table.field_names = ['ID','Name', 'Symbol', 'Price', 'Volume', 'MarketCap', 'Change 1h',
                     'Change 24h', 'Change 7d']

#for every coin in data
for coin in listings_data:
    # extract from
    id = coin['id']
    name = coin['name']
    symbol = coin['symbol']
    # extract the following from quote / USD
    coin_data = coin['quote']['USD']

    table.add_row([id,
                   name,
                   symbol,
                   coin_data['price'],
                   coin_data['volume_24h'],
                   coin_data['market_cap'],
                   coin_data['percent_change_1h'],
                   coin_data['percent_change_24h'],
                   coin_data['percent_change_7d']])

table.sortby = table.field_names[0]
table.reversesort = False
print(table)