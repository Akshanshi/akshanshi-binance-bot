# Binance Futures Trading Bot (Testnet)

This is a command-line based crypto trading bot built for Binance USDT-M Futures Testnet.  
It allows users to place Market, Limit, and Stop-Market orders with API logging and input validation.

---

##  Features

- Place **Market** and **Limit** orders
- (Bonus) Place **Stop-Market** orders
- Uses `python-binance` library
- Supports interactive CLI input
- Handles error logging and validation
- Logs API responses to `bot.log`

---

##  Requirements

- Python 3.8+
- `python-binance` (`pip install python-binance`)

---

##  Testnet Setup

> Binance Testnet requires KYC for API key creation.
> You may use temporary demo API keys only for testing structure.  
> Actual orders may return `code -2015` (Invalid Key/IP), which is expected.

---

##  Usage

## Market Order
```bash
python src/market_orders.py
### Limit Order
python src/limit_orders.py
### Stop-Market Order (Advanced)
python src/advanced/stop_limit.py

You will be prompted to enter:

API key

Secret

Symbol (e.g., BTCUSDT)

BUY/SELL

Quantity (e.g., 0.01)

Limit/Stop price (when applicable)

📁 Files
File	             Description
market_orders.py	Places a Market Order
limit_orders.py	Places a Limit Order
stop_limit.py	Places a Stop-Market Order
bot.log	Logs actions & errors
report.pdf	Screenshots and summary"# akshanshi-binance-bot" 
"# akshanshi-binance-bot" 
"# akshanshi-binance-bot" 
