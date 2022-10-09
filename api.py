
import openpyxl
from configparser import ConfigParser as cfgparserwhat
import requests


class EtherAPI():
    def __init__(self):

        self.cfg = cfgparserwhat()
        self.cfg.read('cfg.ini')
        self.ether_value = 10 ** 18
        self.ether_api_key = self.cfg['KEYS']['etherscan_key']
        self.ether_main_url = 'https://api.etherscan.io/api'
    async def get_etherscanapi_url(self, action,module,address,**kwargs):
        url = f"{self.ether_main_url}/?module={module}&action={action}&address={address}&apikey={self.ether_api_key}"
        return url
    async def get_balance(self,address):
        r=requests.get(await self.get_etherscanapi_url('balance','account',address))
        balance = int(r.json()["result"]) / self.ether_value
        return balance
