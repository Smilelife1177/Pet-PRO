from pprint import pprint
from pybit.unified_trading import HTTP

session = HTTP(
    testnet=False,
    api_key="ehEP3TXvZX2HYa8cUg",
    api_secret="zqaxoEWwmcp4ywo325K51zyXWv9beYi7vf0n",
)
res = (session.get_wallet_balance(
    accountType="UNIFIED",
    coin="USDT",
))

pprint(res)