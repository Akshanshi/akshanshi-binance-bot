# src/market_orders.py
print("✅ Script is running")


from binance.client import Client
from binance.enums import *
import logging

# Setup logging
logging.basicConfig(
    filename='bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class MarketOrderBot:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret, testnet=True)

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=SIDE_BUY if side == "BUY" else SIDE_SELL,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
            logging.info(f"✅ Market order placed: {order}")
            print("✅ Market Order Executed. Order ID:", order["orderId"])
        except Exception as e:
            logging.error(f"❌ Market order failed: {e}")
            print("❌ Error placing order:", e)

# === CLI Input ===
if __name__ == '__main__':
    api_key = input("Enter your Binance Testnet API Key: ").strip()
    api_secret = input("Enter your Binance Testnet API Secret: ").strip()
    symbol = input("Enter trading pair (e.g., BTCUSDT): ").strip().upper()
    side = input("Enter order side (BUY or SELL): ").strip().upper()
    quantity = input("Enter quantity to trade: ").strip()

    # Validation
    if side not in ["BUY", "SELL"]:
        print("❌ Invalid side. Must be 'BUY' or 'SELL'")
        exit()

    try:
        quantity = float(quantity)
    except ValueError:
        print("❌ Quantity must be a number.")
        exit()

    bot = MarketOrderBot(api_key, api_secret)
    bot.place_market_order(symbol, side, quantity)
