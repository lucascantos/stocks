
from src.configs.configs import IEX_CLOUD_API_TOKEN
import requests
class IEX:
    def __init__(self):
        self.url = 'https://sandbox.iexapis.com/stable'
        self.token = IEX_CLOUD_API_TOKEN

    def stocks(self, symbol, s_type='quote'):
        params = {
            'token': IEX_CLOUD_API_TOKEN
        }
        response = requests.get(f'{self.url}/stock/{symbol}/{s_type}', params=params)
        if response.status_code > 299:
            print(response)
            return
        return response.json()

    def batch(self, symbols_string, s_type='quote'):
        params = {
            'symbols': symbols_string,
            'types': s_type,
            'token': IEX_CLOUD_API_TOKEN
        }
        response = requests.get(f'{self.url}/stock/market/batch', params=params)
        if response.status_code != 200:
            print(response)
            return
        return response.json()

