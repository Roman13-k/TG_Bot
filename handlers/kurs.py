from utils.currency.rates import get_daily_currency
from utils.rate_limiter import rate_limited
from db.cache import get_cached_currency, set_cached_currency

user_states = {}


def register_kurs_handler(bot):
    @bot.message_handler(commands=['kurs'])
    @rate_limited(bot)
    def ask_currency(message):
        parts = message.text.strip().split()
        if len(parts) == 2:
            currency_code = parts[1].upper()

            data = get_or_cache_currency(currency_code)

            if data:
                bot.send_message(message.chat.id,
                                 f"Курс: {data['nominal']} {currency_code} = {data['value']:.2f} ₽")
            else:
                bot.send_message(message.chat.id,
                                 "Не смог найти такую валюту. Попробуй USD, EUR, GBP и т.п.")
        else:
            user_states[message.chat.id] = 'waiting_for_currency'
            bot.send_message(message.chat.id,
                             "Пожалуйста, укажи код валюты (например: USD, EUR, GBP):")

    @bot.message_handler(func=lambda m: user_states.get(m.chat.id) == 'waiting_for_currency')
    @rate_limited(bot)
    def handle_currency_input(message):
        currency_code = message.text.strip().upper()

        data = get_or_cache_currency(currency_code)

        if data:
            bot.send_message(message.chat.id,
                             f"Курс: {data['nominal']} {currency_code} = {data['value']:.2f} ₽")
        else:
            bot.send_message(message.chat.id,
                             "Не смог найти такую валюту. Попробуй USD, EUR, GBP и т.п.")
        user_states[message.chat.id] = None


def get_or_cache_currency(code: str):
    data = get_cached_currency(code)
    if not data:
        data = get_daily_currency(code)
        if data:
            set_cached_currency(code, data)
    return data
