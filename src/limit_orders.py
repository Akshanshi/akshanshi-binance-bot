# src/limit_orders.py

from binance.client import Client
from binance.enums import *
import logging

# Setup logging
logging.basicConfig(
    filename='bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class LimitOrderBot:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side == "BUY" else SIDE_SELL,
                type=ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=str(price)  # price must be a string for some brokers
            )
            logging.info(f"✅ Limit order placed: {order}")
            print("✅ Limit Order Placed. Order ID:", order["orderId"])
        except Exception as e:
            logging.error(f"❌ Limit order failed: {e}")
            print("❌ Error placing order:", e)

# === CLI Input ===
if __name__ == '__main__':
    print("✅ Script is running")

    api_key = input("Enter your Binance Testnet API Key: ").strip()
    api_secret = input("Enter your Binance Testnet API Secret: ").strip()
    symbol = input("Enter trading pair (e.g., BTCUSDT): ").strip().upper()
    side = input("Enter order side (BUY or SELL): ").strip().upper()
    quantity = input("Enter quantity to trade: ").strip()
    price = input("Enter limit price: ").strip()

    if side not in ["BUY", "SELL"]:
        print("❌ Invalid side. Must be 'BUY' or 'SELL'")
        exit()

    try:
        quantity = float(quantity)
        price = float(price)
    except ValueError:
        print("❌ Quantity and price must be numbers.")
        exit()

    bot = LimitOrderBot(api_key, api_secret)
    bot.place_limit_order(symbol, side, quantity, price)
