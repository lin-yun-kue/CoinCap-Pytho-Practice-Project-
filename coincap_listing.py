import json
import requests

listing_url = 'https://api.coinmarketcap.com/v2/listings/'

request = requests.get(listing_url)
results = request.json()

#print(json.dumps(results, sort_keys=True, indent=4))
data = results['data']

for currency in data:
    rank = currency['id']
    name = currency['name']
    symbol = currency['symbol']
    msg = str(rank) + ':' + name + '(' + symbol + ')'
    if(rank < 1000):
        print(msg)
