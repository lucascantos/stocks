
from src.configs.configs import IEX_CLOUD_API_TOKEN
import requests
class IEX:
    def __init__(self):
        self.url = 'https://sandbox.iexapis.com/stable'
        self.token = IEX_CLOUD_API_TOKEN

    def stocks(self, symbol, s_type='quote'):
        # sp_500_
        params = {
            'token': IEX_CLOUD_API_TOKEN
        }
        response = requests.get(f'{self.url}/stock/{symbol}/{s_type}', params=params)
        if response.status_code > 299:
            print(response)
            return
        return response.json()

    def batch(self, symbols_string, s_type='quote', kwargs=None):
        params = {
            'symbols': symbols_string,
            'types': s_type,
            'token': IEX_CLOUD_API_TOKEN
        }
        if kwargs:
            params.update(**kwargs)

        response = requests.get(f'{self.url}/stock/market/batch', params=params)
        if response.status_code != 200:
            print(response)
            return
        return response.json()

    def stats(self, symbol):
        params = {
            'token': IEX_CLOUD_API_TOKEN
        }
        response = requests.get(f'{self.url}/stock/{symbol}/stats', params=params)
        if response.status_code != 200:
            print(response)
            return
        return response.json()
    
    def chart(self, symbol, range, date=None):
        params = {
            'token': IEX_CLOUD_API_TOKEN
        }
        response = requests.get(f'{self.url}/stock/{symbol}/chart/{range}', params=params) #{date}
        if response.status_code != 200:
            print(response)
            return
        return response.json()

