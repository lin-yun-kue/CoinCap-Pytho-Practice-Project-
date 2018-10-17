import requests
import json

convert = 'USD'

listing_url = 'https://api.coinmarketcap.com/v2/listings/'
url_end = '?structure=array&convert=' + convert

request = requests.get(listing_url)
results = request.json()

data = results['data']
# print(json.dumps(data, sort_keys=True, indent=4))

ticker_url_pairs = {}
for cur in data:
    symbol = cur['symbol']
    url = cur['id']
    ticker_url_pairs[symbol] = url

print(ticker_url_pairs)

while True:
    print()
    choice = input('Enter the ticker symbol of a cryptocurrency')
    choice = choice.upper()

    ticker_url = 'https://api.coinmarketcap.com/v2/ticker/' + \
        str(ticker_url_pairs[choice]) + '/' + url_end

    request = requests.get(ticker_url)
    results = request.json()
    print(json.dumps(results, sort_keys=True, indent=4))
