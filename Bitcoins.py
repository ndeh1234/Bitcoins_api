from decimal import Decimal

import json
import urllib.request


def main():
    get_price_of_bitcoins()

def get_price_of_bitcoins():
    # getting number of bit coins from the user
    bitcoin = int(input('Enter the number of bitcoins: '))

    try:

        # url for retrieving the bitcoin price
        url = 'https://api.coindesk.com/v1/bpi/currentprice/CNY.json'

        # getting response from the url
        r = urllib.request.urlopen(url)

        # reading the data
        raw_data = r.read()

        # decoding the data to json data type
        data = json.loads(raw_data.decode(r.info().get_param('charset') or 'utf-8'))

        # getting the US dollar price of one bitcoin from json data
        bitcoin_price = data['bpi']['USD']['rate_float']

        # calculating the US price for n bitcoins
        total = bitcoin * bitcoin_price

        # displaying the total cost
        print('\nThe price of {0:d} bitcoin(s) is ${1:.2f}'.format(bitcoin, total))

    except urllib.error.URLError as e:

        # error message, when connectivity fails
        print(e.reason)

        # return bitcoin_price


if __name__ == '__main__':
    main()