# src/advanced/stop_limit.py

from binance.client import Client
from binance.enums import *
import logging

# Setup logging
logging.basicConfig(
    filename='bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class StopLimitOrderBot:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'

    def place_stop_limit_order(self, symbol, side, quantity, stop_price, limit_price):
        try:
            order = self.client.futures_create_order(
            symbol=symbol,
            side="BUY" if side == "BUY" else "SELL",
            type="STOP_MARKET",
            timeInForce="GTC",
            quantity=quantity,
            stopPrice=str(stop_price),
            workingType='MARK_PRICE'
        )


            
            logging.info(f"✅ Stop-Limit order placed: {order}")
            print("✅ Stop-Limit Order Placed. Order ID:", order["orderId"])
        except Exception as e:
            logging.error(f"❌ Stop-Limit order failed: {e}")
            print("❌ Error placing order:", e)

# === CLI Input ===
if __name__ == '__main__':
    print("✅ Script is running")

    api_key = input("Enter your Binance Testnet API Key: ").strip()
    api_secret = input("Enter your Binance Testnet API Secret: ").strip()
    symbol = input("Enter trading pair (e.g., BTCUSDT): ").strip().upper()
    side = input("Enter order side (BUY or SELL): ").strip().upper()
    quantity = input("Enter quantity to trade: ").strip()
    stop_price = input("Enter stop price: ").strip()
    limit_price = input("Enter limit price: ").strip()

    if side not in ["BUY", "SELL"]:
        print("❌ Invalid side. Must be 'BUY' or 'SELL'")
        exit()

    try:
        quantity = float(quantity)
        stop_price = float(stop_price)
        limit_price = float(limit_price)
    except ValueError:
        print("❌ Quantity, stop price, and limit price must be numbers.")
        exit()

    bot = StopLimitOrderBot(api_key, api_secret)
    bot.place_stop_limit_order(symbol, side, quantity, stop_price, limit_price)
