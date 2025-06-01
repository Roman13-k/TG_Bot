# Telegram Currency Bot

A simple Telegram bot to get the current exchange rates of currencies to the Russian ruble using data from the Central Bank of Russia.

---

## Features

- Generate a 7-day exchange rate chart using the /graph <currency> command, e.g., /graph USD
- Get the current exchange rate with /kurs <currency>, e.g., /kurs USD
- The /start command displays a welcome message and a list of available currencies
- Supports major currencies: USD, EUR, GBP, and more

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/Roman13-k/TG_Bot.git
cd telegram-currency-bot
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a .env file:

```bash
TOKEN=your_telegram_bot_token
CB_URL="https://www.cbr.ru/scripts/XML_daily.asp"
CB_DYNAMIC_URL = "https://www.cbr.ru/scripts/XML_dynamic.asp"
DB_NAME = "db/cache.db"
```
