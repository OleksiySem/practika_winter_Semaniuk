import requests
import time
import hmac
import hashlib
from urllib.parse import urlencode

class MexcClient:
    def __init__(self, api_key, api_secret):
        self.base_url = "https://api.mexc.com"
        self.api_key = api_key
        self.api_secret = api_secret

    def _get_signature(self, params):
        query_string = urlencode(params)
        return hmac.new(
            self.api_secret.encode('utf-8'),
            query_string.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()

    def _send_request(self, method, endpoint, params=None):
        if params is None:
            params = {}

        # Додаємо обов'язковий таймстамп
        params['timestamp'] = int(time.time() * 1000)
        params['signature'] = self._get_signature(params)

        headers = {
            'X-MEXC-APIKEY': self.api_key,
            'Content-Type': 'application/json'
        }

        url = f"{self.base_url}{endpoint}"

        if method == "POST":
            response = requests.post(url, params=params, headers=headers)
        else:
            response = requests.get(url, params=params, headers=headers)

        return response.json()

    def buy_market(self, symbol, usdt_amount):
        """Купівля по маркету (на певну суму в USDT)"""
        params = {
            'symbol': symbol,
            'side': 'BUY',
            'type': 'MARKET',
            'quoteOrderQty': usdt_amount
        }
        return self._send_request("POST", "/api/v3/order", params)

    def place_limit_order(self, symbol, side, quantity, price):
        """Виставлення лімітного ордера"""
        params = {
            'symbol': symbol,
            'side': side.upper(), # 'BUY' або 'SELL'
            'type': 'LIMIT',
            'quantity': quantity,
            'price': price,
            'timeInForce': 'GTC'
        }
        return self._send_request("POST", "/api/v3/order", params)

# --- Налаштування ---
API_KEY = "mx0vglbthuvMgKNHSo"
API_SECRET = "eb9c25ee8b0642a7bd07f7859100a485"

bot = MexcClient(API_KEY, API_SECRET)


#print(bot.buy_market('SOLUSDC', 5))
# Приклад: Купити BTC на 10 USDT по маркету
# print(bot.buy_market('BTCUSDT', 10))

# Приклад: Ліміт на продаж 0.001 BTC за ціною 100 000 USDT
print(bot.place_limit_order('SOLUSDC', 'BUY', 0.05, 117.8))
