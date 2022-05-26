import json
import requests
from config import keys

class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'{quote} - это что?')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'{base} - это куда?')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'{amount} - это сколько?')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base