from pprint import pprint
from pybit.unified_trading import HTTP
import os
from dotenv import load_dotenv

load_dotenv()

session = HTTP(
    testnet=False,
    api_key=os.getenv("BYBIT_API_KEY"),
    api_secret=os.getenv("BYBIT_API_SECRET"),
)
res = (session.get_wallet_balance(
    accountType="UNIFIED",
    coin="USDT",
))

pprint(res)
#Unified Trading acc