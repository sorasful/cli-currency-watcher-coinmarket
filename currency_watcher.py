import requests
import click
from bs4 import BeautifulSoup


def get_currency(currency):
    base_url = f"https://coinmarketcap.com/currencies/{currency}/"

    response =  requests.get(base_url).text
    soup = BeautifulSoup(response, "html.parser")

    usd_price = soup.find('span', id='quote_price')['data-usd']
    btc_price = soup.find('span',  {'class': 'text-gray details-text-medium'}).text.replace('BTC', '').strip()

    return (usd_price, btc_price)

@click.command()
@click.option('--currency', '-c',  help='the currency you want to get info from', default="bitcoin" )
def main(currency):
    """
    This is a simple tool that shows you the current value of a crypto-currency based on
    https://coinmarketcap.com/ . Provide the full name of the currency and not the abreviation (not implemented yet)
    or just let empty for bitcoin value.
    Here are two examples :

    1. safe-exchange-coin
    2. nexus
    """
    currency_result = get_currency(currency)
    print("USD : {}$  BTC : {}".format(currency_result[0], currency_result[1]))

if __name__ == "__main__":
    main()