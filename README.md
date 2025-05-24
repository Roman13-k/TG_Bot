# Telegram Currency Bot

A simple Telegram bot to get the current exchange rates of currencies to the Russian ruble using data from the Central Bank of Russia.

---

## Features

- Get currency rates with the command `/kurs <currency>`, for example: `/kurs USD`
- The `/start` command shows a greeting and the list of available currencies
- Supports main currencies: USD, EUR, GBP, etc.

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/yourusername/telegram-currency-bot.git
cd telegram-currency-bot
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a .env file:

```bash
TOKEN=your_telegram_bot_token
CB_URL=https://www.cbr.ru/scripts/XML_daily.asp
```
