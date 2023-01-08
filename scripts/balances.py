from apollox.rest_api import Client 
from dotenv import load_dotenv
import os
import json
import attr

load_dotenv()

@attr.s
class Balance:
    accountAlias = attr.ib()
    asset = attr.ib()
    availableBalance = attr.ib()
    balance: float = attr.ib(converter=float)
    crossUnPnl = attr.ib()
    crossWalletBalance = attr.ib()
    marginAvailable = attr.ib()
    maxWithdrawAmount = attr.ib()
    updateTime = attr.ib()

client = Client(key=os.environ.get('api_key'), secret=os.environ.get('api_secret'))

balances = json.loads(json.dumps(client.balance()), object_hook=lambda d: Balance(**d))

for item in balances:
    if(item.balance > 0 or item.asset=='USDT'):
        print('{} : {}'.format(item.asset,item.balance))
